#!/usr/bin/env python3
"""Biblioteca de anúncios da Meta — parte mecânica da skill biblioteca-anuncios-meta.

Rodar a partir da raiz do repo:
  python3 .claude/skills/biblioteca-anuncios-meta/scripts/biblioteca.py <subcomando> ...
(no Windows, se "python3" não existir, use "python" ou "py")

Subcomandos:
  checar
            Confere chaves e programas antes de começar. Diz o que falta, em português,
            sem nunca mostrar o valor de uma chave.
  minerar   --link URL --dest DIR [--pais BR] [--count 100]
            Minera o link via Apify, junta com o anuncios.json que já existe e
            classifica cada peça em NOVA / CONTINUA / SAIU. Nada é apagado.
  processar --dest DIR --ids ID1,ID2  (máx. 5 por leva)
            Baixa a mídia pra midia/, transcreve (AssemblyAI), faz a análise
            visual (TwelveLabs pegasus1.5, fallback frames) e grava _trabalho/<id>.json.
  arquivo   --dest DIR --id ID --arquivo video.mp4
            Mesmo que processar, mas a partir de um arquivo local (quando o link da
            mídia expirou ou a coleta foi manual).
  status    --dest DIR
            Tabela do estado da biblioteca.
  marcar    --dest DIR --ids ID1,ID2
            Marca como processado depois que a ficha da peça foi escrita.

Chaves (do ambiente ou de um .env na pasta ou acima):
  APIFY_TOKEN                               obrigatória pra minerar
  ASSEMBLYAI_API_KEY ou ASSEMBLYAI_KEY      transcrição da fala
  TWELVELABS_KEY ou TWELVELABS_API_KEY      análise visual (sem ela: frames)
Nenhuma chave é impressa. Token da Apify vai no header, nunca na URL (URL cai em log).
Funciona em Mac e Windows: arquivos em UTF-8, pasta temporária do sistema, sem comando de shell.
"""
import argparse, base64, datetime as dt, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

# Console do Windows costuma não ser UTF-8: sem isto, acento derruba o print.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import warnings
warnings.filterwarnings("ignore", message=".*OpenSSL.*")  # aviso inofensivo do Python do sistema no Mac

try:
    import requests
except ImportError:
    sys.exit("Falta o pacote 'requests' do Python. Instale com:\n"
             "  Mac:     python3 -m pip install requests\n"
             "  Windows: python -m pip install requests\n"
             "e rode de novo.")

HOJE = dt.date.today().isoformat()
UTF8 = {"encoding": "utf-8"}

CHAVES = {
    "apify": ["APIFY_TOKEN"],
    "assemblyai": ["ASSEMBLYAI_API_KEY", "ASSEMBLYAI_KEY"],
    "twelvelabs": ["TWELVELABS_KEY", "TWELVELABS_API_KEY"],
}

PROMPT_VISUAL = """Você descreve VÍDEO. NÃO transcreva a fala — a transcrição vem de outro sistema.
Devolva EXATAMENTE nesta estrutura, em português do Brasil, sem nada além dela:

ABERTURA: os 3 primeiros segundos — o que aparece na imagem, movimento de câmera, texto sobreposto se houver. Uma descrição objetiva em até 3 frases. Não invente; se não houver texto na tela, não mencione texto.

ESTRUTURA VISUAL: descrição objetiva do que caracteriza o vídeo como formato — selfie ou câmera fixa? ambiente (academia, quarto, carro, estúdio, rua, cozinha)? há texto de pergunta/caixinha no início? há cortes rápidos ou plano único? há tela de celular/print/gráfico? há legenda dinâmica? pessoa fala com a câmera ou narra em off? Fatos observáveis, um por linha, começando com "- ". NÃO classifique — apenas descreva.

SPOKESPERSON: quem aparece — faixa etária aparente, gênero, vestimenta, postura, contexto (parece cliente, criador de conteúdo, apresentador). Fatos visíveis apenas.

TEXTO NA TELA: texto sobreposto FIXO — caixinha/sticker de pergunta, títulos, cartões, endcard de CTA. UM POR LINHA começando com "- ". NÃO inclua a legenda que acompanha a fala. Se não houver nenhum, escreva exatamente: nenhum

LEGENDA: se houver legenda dinâmica acompanhando a fala (karaokê), escreva: sim — e descreva o estilo (cor, posição). Se não houver: não

VISUAL: linha do tempo. UM evento por linha no formato "- [MM:SS–MM:SS] descrição". Inclua mudanças de cena, gestos marcantes, gráficos e aparições de texto."""


# ---------- chaves e programas ----------
def chave(servico, dest=None):
    """Valor da chave do serviço (aceita os nomes alternativos). Nunca imprimir o retorno."""
    nomes = CHAVES[servico]
    for nome in nomes:
        v = os.getenv(nome)
        if v:
            return v.strip()
    for pasta in filter(None, [dest, os.getcwd()]):
        for p in [Path(pasta).resolve(), *Path(pasta).resolve().parents]:
            env = p / ".env"
            if env.is_file():
                for linha in env.read_text(**UTF8, errors="replace").splitlines():
                    for nome in nomes:
                        if linha.strip().startswith(nome + "="):
                            return linha.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def tem(programa):
    return shutil.which(programa) is not None


def checar(a=None):
    ok_apify = bool(chave("apify"))
    ok_aai = bool(chave("assemblyai"))
    ok_tl = bool(chave("twelvelabs"))
    ok_ff = tem("ffmpeg") and tem("ffprobe")
    print("Checagem da biblioteca de anúncios:")
    print(f"  Apify (buscar os anúncios) ........ {'ok' if ok_apify else 'FALTA — sem ela não dá pra minerar'}")
    print(f"  AssemblyAI (transcrever a fala) ... {'ok' if ok_aai else 'falta — os vídeos ficam sem transcrição'}")
    print(f"  TwelveLabs (descrever o vídeo) .... {'ok' if ok_tl else 'falta — vou tirar fotos do vídeo e olhar uma por uma (mais lento)'}")
    print(f"  ffmpeg (mexer em vídeo) ........... {'ok' if ok_ff else 'falta — sem fotos do vídeo nem compressão; instale: Mac `brew install ffmpeg` · Windows `winget install ffmpeg`'}")
    print("RESUMO:", json.dumps({"apify": ok_apify, "assemblyai": ok_aai, "twelvelabs": ok_tl, "ffmpeg": ok_ff}))
    return ok_apify


# ---------- anuncios.json ----------
def carregar(dest):
    f = Path(dest) / "anuncios.json"
    return json.loads(f.read_text(**UTF8)) if f.exists() else {"anunciante": None, "links": [], "atualizacoes": [], "anuncios": {}}


def salvar(dest, db):
    f = Path(dest) / "anuncios.json"
    f.write_text(json.dumps(db, ensure_ascii=False, indent=2), **UTF8)


def _achar(obj, chaves):
    """Primeiro valor não vazio de qualquer uma das chaves, em qualquer profundidade."""
    if isinstance(obj, dict):
        for k in chaves:
            if obj.get(k):
                return obj[k]
        for v in obj.values():
            r = _achar(v, chaves)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = _achar(v, chaves)
            if r:
                return r
    return None


def _data(v):
    if not v:
        return None
    if isinstance(v, (int, float)):
        return dt.datetime.fromtimestamp(v, dt.timezone.utc).date().isoformat()
    return str(v)[:10]


def normalizar(item):
    snap = item.get("snapshot") or {}
    video = _achar(snap, ["video_hd_url", "video_sd_url"]) or _achar(item, ["video_hd_url", "video_sd_url"])
    imagem = _achar(snap, ["original_image_url", "resized_image_url"]) if not video else None
    corpo = snap.get("body")
    if isinstance(corpo, dict):
        corpo = corpo.get("text")
    return {
        "id": str(item.get("ad_archive_id") or item.get("adArchiveID") or item.get("id")),
        "pagina": item.get("page_name") or snap.get("page_name"),
        "inicio": _data(item.get("start_date") or item.get("startDate")),
        "fim_declarado": _data(item.get("end_date") or item.get("endDate")),
        "variacoes": item.get("collation_count"),
        "grupo": item.get("collation_id"),
        "tipo": "video" if video else ("imagem" if imagem else "outro"),
        "midia_url": video or imagem,
        "texto_feed": (corpo or "")[:600],
        "titulo_feed": snap.get("title"),
        "destino": snap.get("link_url"),
        "cta_botao": snap.get("cta_text"),
    }


# ---------- minerar ----------
def _apify_recusou(r):
    txt = r.text[:300]
    if "limit" in txt.lower() or r.status_code == 402:
        return ("A Apify recusou por limite de uso do mês (o crédito acabou). "
                "Rode de novo quando o ciclo renovar ou adicione crédito na conta. Detalhe: " + txt)
    if r.status_code in (401, 403):
        return "A Apify não aceitou a chave (APIFY_TOKEN). Confira se copiou a chave inteira, sem espaço, e salve de novo."
    return f"A Apify recusou o pedido ({r.status_code}). Detalhe: {txt}"


def minerar(a):
    dest = Path(a.dest)
    token = chave("apify", a.dest)
    if not token:
        sys.exit("Falta a chave da Apify (APIFY_TOKEN). Sem ela não dá pra buscar os anúncios.\n"
                 "Veja a seção 'Configurar as chaves' da skill.")
    dest.mkdir(parents=True, exist_ok=True)
    H = {"Authorization": f"Bearer {token}"}
    entrada = {"urls": [{"url": a.link}], "count": a.count,
               "scrapePageAds.activeStatus": "active", "scrapePageAds.countryCode": a.pais}
    try:
        r = requests.post("https://api.apify.com/v2/acts/curious_coder~facebook-ads-library-scraper/runs",
                          json=entrada, headers=H, timeout=60)
    except requests.RequestException as e:
        sys.exit(f"Não consegui falar com a Apify (internet?): {type(e).__name__}")
    if r.status_code >= 400:
        sys.exit(_apify_recusou(r))
    run = r.json()["data"]
    while True:
        time.sleep(10)
        st = requests.get(f"https://api.apify.com/v2/actor-runs/{run['id']}", headers=H, timeout=60).json()["data"]["status"]
        if st == "SUCCEEDED":
            break
        if st in ("FAILED", "ABORTED", "TIMED-OUT"):
            sys.exit(f"A busca na Apify terminou sem sucesso ({st}). Tente de novo; se repetir, confira o link.")
    itens = requests.get(f"https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items?format=json&clean=true",
                         headers=H, timeout=180).json()
    (dest / "_bruto").mkdir(exist_ok=True)
    (dest / "_bruto" / f"apify-{HOJE}.json").write_text(json.dumps(itens, ensure_ascii=False), **UTF8)
    juntar(dest, a.link, [normalizar(i) for i in itens if isinstance(i, dict)], "apify")


def juntar(dest, link, vistos, metodo):
    """Junta a mineração nova com o que já existe. Nunca apaga: quem sumiu vira SAIU."""
    db = carregar(dest)
    if link not in db["links"]:
        db["links"].append(link)
    ids_vistos = set()
    novos, continuam = [], []
    for n in vistos:
        if not n["id"] or n["id"] == "None":
            continue
        ids_vistos.add(n["id"])
        atual = db["anuncios"].get(n["id"])
        if atual is None:
            n.update({"primeira_vez": HOJE, "ultima_vez": HOJE, "status": "ativo", "processado": False})
            db["anuncios"][n["id"]] = n
            novos.append(n["id"])
        else:
            atual.update({k: v for k, v in n.items() if v})  # URL de mídia nova (link da mídia expira)
            atual.update({"ultima_vez": HOJE, "status": "ativo"})
            continuam.append(n["id"])
        db["anunciante"] = db["anunciante"] or n.get("pagina")
    sairam = [i for i, x in db["anuncios"].items() if x["status"] == "ativo" and i not in ids_vistos]
    for i in sairam:
        db["anuncios"][i]["status"] = "saiu"
    db["atualizacoes"].append({"data": HOJE, "metodo": metodo, "vistos": len(ids_vistos),
                               "novos": len(novos), "continuam": len(continuam), "sairam": len(sairam)})
    salvar(dest, db)
    print(f"Mineração {HOJE}: {len(ids_vistos)} ativos · {len(novos)} NOVOS · {len(continuam)} continuam · {len(sairam)} SAÍRAM")
    status_tabela(db)


# ---------- processar ----------
def baixar(url, alvo):
    with requests.get(url, stream=True, timeout=180) as r:
        r.raise_for_status()
        with open(alvo, "wb") as f:
            for bloco in r.iter_content(1 << 20):
                f.write(bloco)


def transcrever(video, key):
    """Com ffmpeg, extrai só o áudio (upload menor). Sem ffmpeg, manda o vídeo inteiro — a AssemblyAI aceita."""
    with tempfile.TemporaryDirectory() as tmp:
        envio = Path(video)
        if tem("ffmpeg"):
            mp3 = Path(tmp) / "a.mp3"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-vn", "-ac", "1", "-b:a", "64k", str(mp3)])
            if not mp3.exists() or mp3.stat().st_size < 1000:
                return {"status": "sem_audio"}
            envio = mp3
        H = {"authorization": key}
        r = requests.post("https://api.assemblyai.com/v2/upload", data=envio.read_bytes(), headers=H, timeout=300)
        if r.status_code in (401, 403):
            return {"status": "erro", "erro": "a AssemblyAI não aceitou a chave — confira se copiou inteira"}
        if r.status_code >= 400:
            return {"status": "erro", "erro": f"AssemblyAI recusou o envio ({r.status_code})"}
        up = r.json()["upload_url"]

        def rodar(extra):
            t = requests.post("https://api.assemblyai.com/v2/transcript", headers=H, timeout=60,
                              json={"audio_url": up, "speech_model": "universal", **extra}).json()
            if "id" not in t:
                return {"status": "error", "error": t.get("error", "AssemblyAI não aceitou o pedido")}
            while True:
                time.sleep(4)
                d = requests.get(f"https://api.assemblyai.com/v2/transcript/{t['id']}", headers=H, timeout=60).json()
                if d["status"] in ("completed", "error"):
                    return d

        d = rodar({"language_code": "pt"})
        if d["status"] == "completed" and (d.get("confidence") or 0) < 0.62:
            d2 = rodar({"language_detection": True})
            if d2["status"] == "completed" and (d2.get("confidence") or 0) > (d.get("confidence") or 0):
                d = d2
        if d["status"] != "completed":
            erro = str(d.get("error") or "")
            if "no audio" in erro.lower() or "does not appear to contain audio" in erro.lower():
                return {"status": "sem_audio"}
            return {"status": "erro", "erro": erro}
        conf = d.get("confidence") or 0
        return {"status": "ok" if conf >= 0.62 else "fala_suspeita", "confianca": round(conf, 3),
                "idioma": d.get("language_code"), "texto": d.get("text"),
                "duracao_s": d.get("audio_duration")}


def visual_twelvelabs(video, key):
    # limite da API é 30 MB de base64, e base64 infla ~33%: acima de ~21 MB, comprime antes (precisa de ffmpeg)
    if video.stat().st_size > 21 * 1024 * 1024 and tem("ffmpeg"):
        menor = Path(tempfile.gettempdir()) / f"{video.stem}_720p.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-vf", "scale=-2:720",
                        "-b:v", "1200k", "-c:a", "aac", "-b:a", "64k", str(menor)])
        if menor.exists():
            video = menor
    if video.stat().st_size > 21 * 1024 * 1024:
        return {"erro": "vídeo grande demais pra análise visual (acima de ~21 MB)"}
    try:
        r = requests.post("https://api.twelvelabs.io/v1.3/analyze", headers={"x-api-key": key}, timeout=900, json={
            "model_name": "pegasus1.5", "prompt": PROMPT_VISUAL, "temperature": 0.2, "stream": False,
            "video": {"type": "base64_string", "base64_string": base64.b64encode(video.read_bytes()).decode()}})
    except requests.RequestException as e:
        return {"erro": f"não consegui falar com a TwelveLabs: {type(e).__name__}"}
    if r.status_code in (401, 403):
        return {"erro": "a TwelveLabs não aceitou a chave"}
    if r.status_code >= 400:
        return {"erro": f"{r.status_code}: {r.text[:200]}"}
    return {"metodo": "twelvelabs pegasus1.5", "texto": r.json().get("data")}


def frames(video, pasta):
    if not tem("ffmpeg"):
        return []
    pasta.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-vf", "fps=1/2,scale=480:-2",
                    str(pasta / "f_%03d.jpg")])
    return sorted(str(p) for p in pasta.glob("f_*.jpg"))


def duracao(video):
    if not tem("ffprobe"):
        return None
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
                       capture_output=True, text=True)
    try:
        return round(float(r.stdout.strip()), 1)
    except ValueError:
        return None


def processar_um(dest, db, ad_id, arquivo=None):
    ad = db["anuncios"].setdefault(ad_id, {"id": ad_id, "tipo": "video", "primeira_vez": HOJE, "ultima_vez": HOJE,
                                           "status": "ativo", "processado": False})
    midia = dest / "midia"
    midia.mkdir(exist_ok=True)
    trab = dest / "_trabalho"
    trab.mkdir(exist_ok=True)
    out = {"id": ad_id, "processado_em": HOJE, "ficou_de_fora": []}
    ext = ".mp4" if ad.get("tipo") == "video" else ".jpg"
    alvo = midia / f"{ad_id}{ext}"
    if arquivo:
        shutil.copyfile(arquivo, alvo)
    elif not alvo.exists():
        if not ad.get("midia_url"):
            out["erro"] = "sem URL de mídia"
            return out
        try:
            baixar(ad["midia_url"], alvo)
        except Exception as e:
            out["erro"] = f"download falhou (o link da mídia expira — minerar de novo): {type(e).__name__}"
            return out
    out["midia"] = alvo.relative_to(dest).as_posix()
    if ext == ".jpg":
        out["visual"] = {"metodo": "imagem estática — olhar o arquivo", "arquivo": str(alvo)}
        return out
    out["duracao_s"] = duracao(alvo)
    ak = chave("assemblyai", str(dest))
    if ak:
        try:
            out["fala"] = transcrever(alvo, ak)
        except requests.RequestException as e:
            out["fala"] = {"status": "erro", "erro": f"sem conexão com a AssemblyAI: {type(e).__name__}"}
    else:
        out["fala"] = {"status": "sem_chave"}
        out["ficou_de_fora"].append("transcrição (falta a chave da AssemblyAI)")
    if out["duracao_s"] is None:
        out["duracao_s"] = out["fala"].get("duracao_s")
    tk = chave("twelvelabs", str(dest))
    vis = visual_twelvelabs(alvo, tk) if tk else None
    if not vis or "erro" in vis:
        motivo = (vis or {}).get("erro", "falta a chave da TwelveLabs")
        fotos = frames(alvo, Path(tempfile.gettempdir()) / "biblioteca-frames" / ad_id)
        if fotos:
            out["visual"] = {"metodo": "frames (fallback) — OLHAR os frames e preencher a estrutura do PROMPT_VISUAL",
                             "motivo": motivo, "frames": fotos}
        else:
            out["visual"] = {"metodo": "sem análise visual", "motivo": motivo + " e falta o ffmpeg pra tirar fotos do vídeo"}
            out["ficou_de_fora"].append("análise visual (sem TwelveLabs e sem ffmpeg)")
    else:
        out["visual"] = vis
    return out


def processar(a):
    dest = Path(a.dest)
    db = carregar(dest)
    ids = [i.strip() for i in a.ids.split(",") if i.strip()]
    if len(ids) > 5:
        sys.exit("Leva máxima: 5 anúncios.")
    for ad_id in ids:
        if ad_id not in db["anuncios"]:
            print(f"{ad_id}: não está no anuncios.json — minerar antes.")
            continue
        out = processar_um(dest, db, ad_id)
        (dest / "_trabalho" / f"{ad_id}.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), **UTF8)
        fala = out.get("fala", {})
        fora = f" · ficou de fora: {', '.join(out['ficou_de_fora'])}" if out.get("ficou_de_fora") else ""
        print(f"{ad_id}: {out.get('erro') or 'ok'} · fala={fala.get('status')} conf={fala.get('confianca')} · "
              f"visual={out.get('visual', {}).get('metodo', '-')}{fora}")
    salvar(dest, db)


def arquivo(a):
    dest = Path(a.dest)
    dest.mkdir(parents=True, exist_ok=True)
    db = carregar(dest)
    out = processar_um(dest, db, a.id, a.arquivo)
    (dest / "_trabalho" / f"{a.id}.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), **UTF8)
    salvar(dest, db)
    print(json.dumps({k: v for k, v in out.items() if k != "visual"}, ensure_ascii=False, indent=2)[:1500])
    print("visual:", out.get("visual", {}).get("metodo"))


# ---------- status ----------
def dias(ad):
    try:
        ini = dt.date.fromisoformat(ad.get("inicio") or ad["primeira_vez"])
        fim = dt.date.fromisoformat(ad["ultima_vez"])
        return (fim - ini).days
    except (KeyError, ValueError, TypeError):
        return None


def status_tabela(db):
    ads = sorted(db["anuncios"].values(), key=lambda x: (x["status"] != "ativo", -(dias(x) or 0)))
    print(f"\n{'id':<18} {'status':<6} {'tipo':<7} {'início':<10} {'visto até':<10} {'dias':>4} {'var':>3} proc")
    for x in ads:
        print(f"{x['id']:<18} {x['status']:<6} {x.get('tipo','?'):<7} {x.get('inicio') or '?':<10} "
              f"{x['ultima_vez']:<10} {dias(x) if dias(x) is not None else '?':>4} {x.get('variacoes') or '-':>3} "
              f"{'sim' if x.get('processado') else 'não'}")


def status(a):
    if not (Path(a.dest) / "anuncios.json").exists():
        print("Essa biblioteca ainda não tem anúncios guardados — é a primeira rodada.")
        return
    db = carregar(a.dest)
    print(f"Anunciante: {db['anunciante']} · links: {db['links']}")
    for u in db["atualizacoes"]:
        print(f"  {u['data']} ({u['metodo']}): {u['vistos']} ativos, +{u['novos']} novos, {u['sairam']} saíram")
    status_tabela(db)


def marcar(a):
    """Marca como processado depois que a ficha da peça foi escrita."""
    db = carregar(a.dest)
    for i in a.ids.split(","):
        if i.strip() in db["anuncios"]:
            db["anuncios"][i.strip()]["processado"] = True
    salvar(a.dest, db)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    ck = s.add_parser("checar"); ck.set_defaults(f=checar)
    m = s.add_parser("minerar"); m.add_argument("--link", required=True); m.add_argument("--dest", required=True)
    m.add_argument("--pais", default="BR"); m.add_argument("--count", type=int, default=100); m.set_defaults(f=minerar)
    pr = s.add_parser("processar"); pr.add_argument("--dest", required=True); pr.add_argument("--ids", required=True); pr.set_defaults(f=processar)
    ar = s.add_parser("arquivo"); ar.add_argument("--dest", required=True); ar.add_argument("--id", required=True)
    ar.add_argument("--arquivo", required=True); ar.set_defaults(f=arquivo)
    st = s.add_parser("status"); st.add_argument("--dest", required=True); st.set_defaults(f=status)
    mk = s.add_parser("marcar"); mk.add_argument("--dest", required=True); mk.add_argument("--ids", required=True); mk.set_defaults(f=marcar)
    a = p.parse_args()
    a.f(a)
