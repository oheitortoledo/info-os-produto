#!/usr/bin/env python3
"""
Ferramentas da skill /pesquisa-mercado (Info OS).

Só usa a biblioteca padrão do Python 3.8+ e roda igual no Mac, no Linux e no Windows.
O único programa externo é o yt-dlp (opcional): sem ele, os comandos de YouTube
avisam e saem com código 3, e a skill segue em modo degradado (WebSearch/WebFetch).

Uso (a partir da raiz do repo):
    python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py <comando> [opções]
    (no Windows: troque "python3" por "python" ou "py")

Comandos:
    check                       checa dependências e diz se o modo é COMPLETO ou DEGRADADO
    slug "<texto>"              transforma "Nome do Nicho" em "nome-do-nicho"
    workdir <slug>              cria e imprime a pasta temporária de trabalho da pesquisa
    yt-busca   --out DIR --q "..." [--q "..."] [--sp CAMSAggF] [--n 40]
    yt-top     --dir DIR [--min-views 5000] [--n 30] [--exclude "regex"]
    yt-comentarios --out DIR IDS...  [--max 200]
    consolidar --dir DIR --out ARQ.txt
    contar     --file ARQ.txt --regex "termo1|termo2" [--label NOME]
    thumbs     --out DIR IDS...
    yt-info    --out DIR IDS...     (título, views, canal e DESCRIÇÃO COMPLETA)
    yt-intent  --out DIR --q "..." [--q "..."] [--n 15]
    yt-canal   --out DIR (--handle NOME | --busca "nome do canal") [--n 15]
    reddit-check  SUBS...
    reddit-top    --sub SUB --out DIR [--t year]
    reddit-busca  --sub SUB --out DIR --q "..." [--q "..."]
    reddit-threads --sub SUB --out DIR IDS...
    reddit-consolidar --dir DIR --out ARQ.txt
"""

import argparse
import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (research-bot; pesquisa-mercado)"
SP_MAIS_VISTOS_ESTE_ANO = "CAMSAggF"
EXIT_SEM_YTDLP = 3


# ---------------------------------------------------------------- utilidades

def _print(msg=""):
    try:
        print(msg)
    except UnicodeEncodeError:  # console do Windows sem UTF-8
        print(msg.encode("ascii", "replace").decode("ascii"))


def ytdlp_cmd():
    """Devolve a forma de chamar o yt-dlp, ou None se não estiver instalado."""
    exe = shutil.which("yt-dlp")
    if exe:
        return [exe]
    if importlib.util.find_spec("yt_dlp") is not None:
        return [sys.executable, "-m", "yt_dlp"]
    return None


def exigir_ytdlp():
    cmd = ytdlp_cmd()
    if cmd is None:
        _print("SEM_YTDLP: o yt-dlp não está instalado. Instale com `pip install yt-dlp` "
               "(Mac também: `brew install yt-dlp`). Seguindo em modo degradado: use WebSearch/WebFetch "
               "e registre no documento o que ficou de fora.")
        sys.exit(EXIT_SEM_YTDLP)
    return cmd


def run(cmd, cwd=None, timeout=600):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def read_jsonl(path):
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def slugify(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    t = re.sub(r"[^a-z0-9]+", "-", t.lower())
    return t.strip("-") or "pesquisa"


def safe_name(texto, maxlen=60):
    return slugify(texto)[:maxlen]


def http_json(url, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            last = e.code
            if e.code == 429:
                time.sleep(2 * (i + 1))
                continue
            return e.code, None
        except Exception:  # rede, JSON inválido
            last = "erro"
            time.sleep(1)
    return last, None


# ------------------------------------------------------------------ comandos

def cmd_check(_a):
    ok = True
    _print("=== pesquisa-mercado: checando dependências ===")
    _print("OK python %s" % sys.version.split()[0])
    y = ytdlp_cmd()
    if y:
        rc, out, _ = run(y + ["--version"], timeout=60)
        _print("OK yt-dlp %s" % (out.strip() or "(versão não lida)"))
    else:
        ok = False
        _print("FALTA yt-dlp -> instale com `pip install yt-dlp` (Mac também: `brew install yt-dlp`)")
    status, data = http_json("https://www.reddit.com/r/AskReddit/about.json", tries=1)
    _print(("OK" if data else "AVISO") + " acesso ao Reddit (HTTP %s)" % status)
    tmp = tempfile.gettempdir()
    livre = shutil.disk_usage(tmp).free // (1024 * 1024)
    _print("OK pasta temporária %s (%d MB livres)" % (tmp, livre))
    _print("")
    _print("MODO=COMPLETO" if ok else "MODO=DEGRADADO")


def cmd_slug(a):
    _print(slugify(a.texto))


def cmd_workdir(a):
    d = os.path.join(tempfile.gettempdir(), "pesquisa-" + slugify(a.slug))
    for sub in ("", "comments", "thumbs", "reddit", "reddit/threads", "avatar_search", "concorrentes",
                "concorrentes/comments"):
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    _print(d)


def _yt_search_one(y, url, dest, n):
    rc, out, _ = run(y + [url, "--flat-playlist", "--playlist-end", str(n), "-j", "--no-warnings"])
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(out)
    return dest, len([l for l in out.splitlines() if l.strip()])


def cmd_yt_busca(a):
    y = exigir_ytdlp()
    os.makedirs(a.out, exist_ok=True)
    jobs = []
    for i, q in enumerate(a.q, 1):
        url = "https://www.youtube.com/results?search_query=%s&sp=%s" % (urllib.parse.quote(q), a.sp)
        jobs.append((url, os.path.join(a.out, "q%d.jsonl" % i), q))
    with ThreadPoolExecutor(max_workers=6) as ex:
        res = list(ex.map(lambda j: (_yt_search_one(y, j[0], j[1], a.n), j[2]), jobs))
    for (dest, cnt), q in res:
        _print("%4d vídeos | %s | %s" % (cnt, os.path.basename(dest), q))


def cmd_yt_top(a):
    vistos = {}
    for f in glob.glob(os.path.join(a.dir, "q*.jsonl")):
        for v in read_jsonl(f):
            if v.get("id") and v["id"] not in vistos:
                vistos[v["id"]] = v
    exc = re.compile(a.exclude, re.I) if a.exclude else None
    lista = [v for v in vistos.values()
             if (v.get("view_count") or 0) > a.min_views
             and not (exc and exc.search((v.get("title") or "") + " " + (v.get("channel") or "")))]
    lista.sort(key=lambda v: -(v.get("view_count") or 0))
    lista = lista[:a.n]
    top = [{"id": v["id"], "title": v.get("title"), "channel": v.get("channel"),
            "views": v.get("view_count"), "dur": v.get("duration_string"),
            "url": v.get("webpage_url") or v.get("url")} for v in lista]
    with open(os.path.join(a.dir, "top.json"), "w", encoding="utf-8") as fh:
        json.dump(top, fh, ensure_ascii=False, indent=1)
    for v in top:
        _print("%s | %s | %s | %s | %s" % (v["views"], v["dur"] or "?", v["channel"], v["id"], v["title"]))
    _print("\n%d vídeos acima de %d views (de %d únicos)." % (len(top), a.min_views, len(vistos)))
    if len(top) < 15:
        _print("POUCOS: menos de 15. Rode de novo com --min-views 1000 ou adicione 2-3 buscas.")


def _yt_comments_one(y, vid, out, mx):
    args = y + ["--write-info-json", "--write-comments", "--skip-download", "--no-warnings",
                "--extractor-args", "youtube:comment_sort=top;max_comments=%d" % mx,
                "-o", "%(id)s.%(ext)s", "https://www.youtube.com/watch?v=" + vid]
    run(args, cwd=out, timeout=900)
    p = os.path.join(out, vid + ".info.json")
    if not os.path.exists(p):
        return vid, 0, "(falhou)"
    with open(p, encoding="utf-8") as fh:
        d = json.load(fh)
    return vid, len(d.get("comments") or []), (d.get("title") or "")[:70]


def cmd_yt_comentarios(a):
    y = exigir_ytdlp()
    os.makedirs(a.out, exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        res = list(ex.map(lambda v: _yt_comments_one(y, v, a.out, a.max), a.ids))
    for vid, cnt, title in res:
        _print("[%d] %s — %s" % (cnt, vid, title))
    fracos = [r[0] for r in res if r[1] < 30]
    if fracos:
        _print("\nPOUCOS COMENTÁRIOS (<30): %s -> troque pelos próximos da lista." % ", ".join(fracos))


def cmd_consolidar(a):
    linhas = []
    for f in glob.glob(os.path.join(a.dir, "*.info.json")):
        vid = os.path.basename(f)[:-len(".info.json")]
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        for c in d.get("comments") or []:
            likes = c.get("like_count") or 0
            txt = re.sub(r"\s+", " ", c.get("text") or "").strip()[:400]
            if txt:
                linhas.append((likes, "[%s|%d] %s" % (vid, likes, txt)))
    linhas.sort(key=lambda x: -x[0])
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(l for _, l in linhas) + "\n")
    _print("%d comentários consolidados em %s (ordenados por likes)" % (len(linhas), a.out))
    if len(linhas) < 500:
        _print("VOLUME BAIXO (<500): faça uma 2ª rodada de buscas antes de seguir.")


def cmd_contar(a):
    rx = re.compile(a.regex, re.I)
    total = men = likes = 0
    with open(a.file, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            total += 1
            m = re.match(r"\[[^|\]]*\|(\d+)\]\s?(.*)", line)
            texto = m.group(2) if m else line
            if rx.search(texto):
                men += 1
                likes += int(m.group(1)) if m else 0
    pct = (100.0 * men / total) if total else 0
    _print("%s: %d menções | %d likes acumulados | %.1f%% do total (%d)" % (a.label or a.regex, men, likes, pct, total))


def cmd_thumbs(a):
    os.makedirs(a.out, exist_ok=True)
    for vid in a.ids:
        dest = os.path.join(a.out, vid + ".jpg")
        for q in ("maxresdefault", "hqdefault"):
            try:
                req = urllib.request.Request("https://i.ytimg.com/vi/%s/%s.jpg" % (vid, q), headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=30) as r:
                    data = r.read()
                if len(data) >= 5000:
                    with open(dest, "wb") as fh:
                        fh.write(data)
                    break
            except Exception:
                continue
        _print("%s -> %s" % (vid, dest if os.path.exists(dest) else "(sem thumb)"))


def _yt_info_one(y, vid):
    rc, out, _ = run(y + ["https://www.youtube.com/watch?v=" + vid, "--skip-download", "--no-warnings", "-j"], timeout=300)
    try:
        d = json.loads(out.strip().splitlines()[-1])
    except Exception:
        return {"id": vid, "erro": "falhou"}
    return {"id": vid, "title": d.get("title"), "channel": d.get("channel"), "views": d.get("view_count"),
            "likes": d.get("like_count"), "comments": d.get("comment_count"), "upload_date": d.get("upload_date"),
            "description": d.get("description")}


def cmd_yt_info(a):
    y = exigir_ytdlp()
    os.makedirs(a.out, exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        res = list(ex.map(lambda v: _yt_info_one(y, v), a.ids))
    for r in res:
        with open(os.path.join(a.out, "info_%s.json" % r["id"]), "w", encoding="utf-8") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=1)
        _print("%s | %s views | %s | %s" % (r["id"], r.get("views"), r.get("channel"), (r.get("title") or r.get("erro") or "")[:70]))


def cmd_yt_intent(a):
    y = exigir_ytdlp()
    os.makedirs(a.out, exist_ok=True)
    jobs = [("ytsearch%d:%s" % (a.n, q), os.path.join(a.out, "yt_%s.jsonl" % safe_name(q)), q) for q in a.q]
    with ThreadPoolExecutor(max_workers=6) as ex:
        list(ex.map(lambda j: _yt_search_one(y, j[0], j[1], a.n), jobs))
    for _, dest, q in jobs:
        _print("\n--- BUSCA DO PÚBLICO: %s ---" % q)
        vids = [v for v in read_jsonl(dest) if v.get("view_count") is not None]
        vids.sort(key=lambda v: -v["view_count"])
        for v in vids[:8]:
            _print("[%s v] %s — %s" % (v["view_count"], v.get("channel") or "?", v.get("title")))


def cmd_yt_canal(a):
    y = exigir_ytdlp()
    os.makedirs(a.out, exist_ok=True)
    if a.handle:
        url = "https://www.youtube.com/@%s/videos" % a.handle.lstrip("@")
        nome = a.handle
    else:
        rc, out, _ = run(y + ["ytsearch5:" + a.busca, "--flat-playlist", "-j", "--no-warnings"])
        cid = None
        for line in out.splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("channel_id"):
                cid = d["channel_id"]
                _print("canal encontrado: %s (%s)" % (d.get("channel"), cid))
                break
        if not cid:
            _print("Canal não encontrado pela busca. Tente outro nome ou um título de vídeo conhecido.")
            return
        url = "https://www.youtube.com/channel/%s/videos" % cid
        nome = a.busca
    dest = os.path.join(a.out, "ch_%s.jsonl" % safe_name(nome))
    _, cnt = _yt_search_one(y, url, dest, a.n)
    _print("%d vídeos -> %s" % (cnt, dest))
    for v in read_jsonl(dest)[:a.n]:
        _print("%s — %s" % (v.get("id"), v.get("title")))
    if cnt == 0:
        _print("0 vídeos: handle provavelmente errado. Rode de novo com --busca \"nome do canal\".")


REDDIT_BLOQUEADO = ("REDDIT_BLOQUEADO: o Reddit recusou o acesso direto (HTTP 403). Siga pelo plano B do "
                    "references/modulo-2-reddit.md (WebSearch site:reddit.com + WebFetch nas threads) e registre no documento.")


def cmd_reddit_check(a):
    bloqueado = False
    for sub in a.subs:
        code, d = http_json("https://www.reddit.com/r/%s/about.json" % sub, tries=2)
        dd = (d or {}).get("data") or {}
        _print("r/%s [HTTP %s] subs=%s — %s" % (sub, code, dd.get("subscribers", "?"),
                                                 (dd.get("public_description") or "")[:80].replace("\n", " ")))
        bloqueado = bloqueado or code == 403
        time.sleep(0.5)
    if bloqueado:
        _print("\n" + REDDIT_BLOQUEADO)


def _listar_posts(d):
    for c in ((d or {}).get("data") or {}).get("children") or []:
        p = c.get("data") or {}
        yield p


def cmd_reddit_top(a):
    os.makedirs(a.out, exist_ok=True)
    code, d = http_json("https://www.reddit.com/r/%s/top.json?t=%s&limit=100" % (a.sub, a.t))
    if code == 403:
        _print(REDDIT_BLOQUEADO)
    with open(os.path.join(a.out, "%s_top_%s.json" % (a.sub, a.t)), "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False)
    for p in list(_listar_posts(d))[:30]:
        _print("[%s up | %s cm] %s | %s" % (p.get("score"), p.get("num_comments"), p.get("id"), p.get("title")))


def cmd_reddit_busca(a):
    os.makedirs(a.out, exist_ok=True)
    for q in a.q:
        url = "https://www.reddit.com/r/%s/search.json?q=%s&restrict_sr=1&sort=top&t=all&limit=25" % (
            a.sub, urllib.parse.quote(q))
        code, d = http_json(url)
        with open(os.path.join(a.out, "q_%s.json" % safe_name(q)), "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False)
        _print("\n--- Busca: %s [HTTP %s] ---" % (q, code))
        if code == 403:
            _print(REDDIT_BLOQUEADO)
            return
        for p in list(_listar_posts(d))[:6]:
            _print("[%s up | %s cm] %s | %s" % (p.get("score"), p.get("num_comments"), p.get("id"), p.get("title")))
        time.sleep(0.5)


def cmd_reddit_threads(a):
    os.makedirs(a.out, exist_ok=True)
    for tid in a.ids:
        code, d = http_json("https://www.reddit.com/r/%s/comments/%s.json?limit=200&sort=top" % (a.sub, tid))
        with open(os.path.join(a.out, "%s.json" % tid), "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False)
        try:
            title = d[0]["data"]["children"][0]["data"]["title"][:80]
            n = len([c for c in d[1]["data"]["children"] if c.get("kind") == "t1"])
        except Exception:
            title, n = "(falhou HTTP %s)" % code, 0
        _print("[%s] %d comments | %s" % (tid, n, title))
        time.sleep(0.6)


def cmd_reddit_consolidar(a):
    blocos = []
    for f in sorted(glob.glob(os.path.join(a.dir, "*.json"))):
        tid = os.path.basename(f)[:-5]
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
            op = d[0]["data"]["children"][0]["data"]
        except Exception:
            continue
        b = ["========== POST [%s] ==========" % tid,
             "SUB: r/%s" % op.get("subreddit"),
             "TITLE: %s" % op.get("title"),
             "SCORE: %s up | %s comments" % (op.get("score"), op.get("num_comments")),
             "OP_BODY: %s" % re.sub(r"\s+", " ", op.get("selftext") or ""),
             "--- TOP COMMENTS ---"]
        coms = [c["data"] for c in d[1]["data"]["children"] if c.get("kind") == "t1"]
        coms.sort(key=lambda c: -(c.get("score") or 0))
        for c in coms:
            b.append("[%s] %s" % (c.get("score"), re.sub(r"\s+", " ", c.get("body") or "")[:500]))
        blocos.append("\n".join(b))
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(blocos) + "\n")
    _print("%d threads consolidadas em %s" % (len(blocos), a.out))


# ----------------------------------------------------------------------- CLI

def main():
    p = argparse.ArgumentParser(description="Ferramentas da skill /pesquisa-mercado")
    s = p.add_subparsers(dest="cmd")

    s.add_parser("check")
    x = s.add_parser("slug"); x.add_argument("texto")
    x = s.add_parser("workdir"); x.add_argument("slug")

    x = s.add_parser("yt-busca"); x.add_argument("--out", required=True)
    x.add_argument("--q", action="append", required=True); x.add_argument("--sp", default=SP_MAIS_VISTOS_ESTE_ANO)
    x.add_argument("--n", type=int, default=40)

    x = s.add_parser("yt-top"); x.add_argument("--dir", required=True)
    x.add_argument("--min-views", type=int, default=5000); x.add_argument("--n", type=int, default=30)
    x.add_argument("--exclude", default="")

    x = s.add_parser("yt-comentarios"); x.add_argument("--out", required=True); x.add_argument("ids", nargs="+")
    x.add_argument("--max", type=int, default=200)

    x = s.add_parser("consolidar"); x.add_argument("--dir", required=True); x.add_argument("--out", required=True)

    x = s.add_parser("contar"); x.add_argument("--file", required=True); x.add_argument("--regex", required=True)
    x.add_argument("--label", default="")

    x = s.add_parser("thumbs"); x.add_argument("--out", required=True); x.add_argument("ids", nargs="+")
    x = s.add_parser("yt-info"); x.add_argument("--out", required=True); x.add_argument("ids", nargs="+")

    x = s.add_parser("yt-intent"); x.add_argument("--out", required=True)
    x.add_argument("--q", action="append", required=True); x.add_argument("--n", type=int, default=15)

    x = s.add_parser("yt-canal"); x.add_argument("--out", required=True)
    g = x.add_mutually_exclusive_group(required=True); g.add_argument("--handle"); g.add_argument("--busca")
    x.add_argument("--n", type=int, default=15)

    x = s.add_parser("reddit-check"); x.add_argument("subs", nargs="+")
    x = s.add_parser("reddit-top"); x.add_argument("--sub", required=True); x.add_argument("--out", required=True)
    x.add_argument("--t", default="year")
    x = s.add_parser("reddit-busca"); x.add_argument("--sub", required=True); x.add_argument("--out", required=True)
    x.add_argument("--q", action="append", required=True)
    x = s.add_parser("reddit-threads"); x.add_argument("--sub", required=True); x.add_argument("--out", required=True)
    x.add_argument("ids", nargs="+")
    x = s.add_parser("reddit-consolidar"); x.add_argument("--dir", required=True); x.add_argument("--out", required=True)

    a = p.parse_args()
    if not a.cmd:
        p.print_help()
        return
    fn = {
        "check": cmd_check, "slug": cmd_slug, "workdir": cmd_workdir,
        "yt-busca": cmd_yt_busca, "yt-top": cmd_yt_top, "yt-comentarios": cmd_yt_comentarios,
        "consolidar": cmd_consolidar, "contar": cmd_contar, "thumbs": cmd_thumbs, "yt-info": cmd_yt_info,
        "yt-intent": cmd_yt_intent, "yt-canal": cmd_yt_canal,
        "reddit-check": cmd_reddit_check, "reddit-top": cmd_reddit_top, "reddit-busca": cmd_reddit_busca,
        "reddit-threads": cmd_reddit_threads, "reddit-consolidar": cmd_reddit_consolidar,
    }[a.cmd]
    fn(a)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
