#!/usr/bin/env python3
"""
Transforma o material do especialista em transcrição .txt, pronta pra análise de voz.

Aceita três tipos de entrada:
  1. Link do YouTube (público ou NÃO LISTADO) -> baixa a legenda (manual ou automática)
     Precisa do yt-dlp instalado (pip install yt-dlp).
  2. Arquivo de vídeo/áudio local (.mp4 .mov .mp3 .m4a .wav ...) -> transcreve na AssemblyAI
     Precisa da chave em ASSEMBLYAI_API_KEY (conta grátis em assemblyai.com).
  3. Transcrição pronta (.txt .srt .vtt) -> só limpa os códigos de tempo.

Uso:
    python3 transcrever.py <link-ou-arquivo> [<link-ou-arquivo> ...] --out PASTA

Saída: um .txt por entrada em PASTA + resumo de palavras e minutos.
Sem dependências além da biblioteca padrão do Python (e do yt-dlp pro caso 1).
"""

import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

VIDEO_AUDIO = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v",
               ".mp3", ".m4a", ".wav", ".aac", ".ogg", ".flac", ".opus"}
TEXTO = {".txt", ".srt", ".vtt"}
PALAVRAS_POR_MINUTO = 150  # fala média em português, só pra estimar quando não há duração real
AAI = "https://api.assemblyai.com/v2"


def slug(texto: str) -> str:
    import unicodedata
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:60] or "transcricao"


# ---------------------------------------------------------------- legendas

def limpar_legenda(bruto: str) -> str:
    """VTT/SRT -> texto corrido. Tira tempo, tags e as repetições da legenda automática."""
    linhas, ultima = [], None
    for linha in bruto.splitlines():
        l = linha.strip()
        if not l or l == "WEBVTT" or l.isdigit():
            continue
        if "-->" in l or l.startswith(("Kind:", "Language:", "NOTE", "STYLE")):
            continue
        l = re.sub(r"<[^>]+>", "", l)          # <c>, <00:00:01.000>, <i>
        l = re.sub(r"\[(música|musica|music|aplausos|risos)\]", "", l, flags=re.I).strip()
        if not l or l == ultima:
            continue
        # legenda automática "rola": a linha nova começa com o fim da anterior
        if ultima and l.startswith(ultima):
            linhas[-1] = l
        else:
            linhas.append(l)
        ultima = l
    return re.sub(r"\s+", " ", " ".join(linhas)).strip()


def ytdlp_cmd():
    if shutil.which("yt-dlp"):
        return ["yt-dlp"]
    try:
        subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                       capture_output=True, check=True)
        return [sys.executable, "-m", "yt_dlp"]
    except Exception:
        return None


def escolher_legenda(info: dict):
    """Prefere legenda manual em português; depois a automática no idioma original."""
    for chave in ("subtitles", "automatic_captions"):
        faixas = info.get(chave) or {}
        for idioma in ("pt-BR", "pt", "pt-orig", "pt-PT"):
            for f in faixas.get(idioma, []):
                if f.get("ext") == "vtt":
                    return f["url"], f"{chave}:{idioma}"
    return None, None


def do_youtube(url: str, out: pathlib.Path):
    cmd = ytdlp_cmd()
    if not cmd:
        sys.exit("ERRO: falta o yt-dlp. Instale com:  pip install yt-dlp   (ou no Mac: brew install yt-dlp)")
    r = subprocess.run(cmd + ["-J", "--skip-download", "--no-warnings", url],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ERRO: não consegui ler o vídeo. Ele é privado? (Não listado funciona, privado não.)\n{r.stderr[-400:]}")
    info = json.loads(r.stdout)
    titulo, dur = info.get("title", "video"), info.get("duration")
    legenda_url, origem = escolher_legenda(info)
    texto = None
    if legenda_url:
        try:
            with urllib.request.urlopen(legenda_url, timeout=60) as resp:
                texto = limpar_legenda(resp.read().decode("utf-8", "ignore"))
        except Exception:
            texto = None
    if not texto:  # plano B: deixa o próprio yt-dlp baixar o arquivo de legenda
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(cmd + ["--skip-download", "--write-subs", "--write-auto-subs",
                                  "--sub-langs", "pt.*,pt", "--sub-format", "vtt",
                                  "-o", f"{tmp}/leg.%(ext)s", url], capture_output=True)
            achados = sorted(pathlib.Path(tmp).glob("*.vtt"))
            if achados:
                texto = limpar_legenda(achados[0].read_text("utf-8", "ignore"))
                origem = origem or "yt-dlp"
    if not texto:
        sys.exit("ERRO: esse vídeo não tem legenda em português (nem automática). "
                 "Baixe o vídeo e mande o arquivo, que eu transcrevo pela AssemblyAI.")
    destino = out / f"{slug(titulo)}.txt"
    cab = (f"# fonte: {url}\n# titulo: {titulo}\n# legenda: {origem}\n"
           f"# aviso: legenda automatica do YouTube pode ter erros de palavra (e as vezes vem sem pontuacao)\n\n")
    destino.write_text(cab + texto + "\n", "utf-8")
    return destino, texto, dur


# ---------------------------------------------------------------- AssemblyAI

def aai(metodo, caminho, chave, corpo=None, dados=None):
    headers = {"authorization": chave}
    if corpo is not None:
        dados = json.dumps(corpo).encode()
        headers["content-type"] = "application/json"
    req = urllib.request.Request(AAI + caminho, data=dados, headers=headers, method=metodo)
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read().decode())


def do_arquivo_midia(caminho: pathlib.Path, out: pathlib.Path):
    chave = os.environ.get("ASSEMBLYAI_API_KEY") or os.environ.get("ASSEMBLYAI_KEY")
    if not chave:
        sys.exit("ERRO: falta a chave da AssemblyAI. Crie conta grátis em assemblyai.com, copie a API key e rode:\n"
                 "  Mac:     export ASSEMBLYAI_API_KEY=sua_chave\n"
                 "  Windows: setx ASSEMBLYAI_API_KEY sua_chave   (e abra um terminal novo)\n"
                 "Ou suba o vídeo no YouTube como NÃO LISTADO e me mande o link.")
    print(f"… enviando {caminho.name} ({caminho.stat().st_size // (1024*1024)} MB)", file=sys.stderr)
    try:
        up = aai("POST", "/upload", chave, dados=caminho.read_bytes())
        job = aai("POST", "/transcript", chave, corpo={
            "audio_url": up["upload_url"], "language_code": "pt", "speaker_labels": True})
        while True:
            res = aai("GET", f"/transcript/{job['id']}", chave)
            if res["status"] == "completed":
                break
            if res["status"] == "error":
                sys.exit(f"ERRO na AssemblyAI: {res.get('error')}")
            print("… transcrevendo", file=sys.stderr)
            time.sleep(10)
    except urllib.error.HTTPError as e:
        sys.exit(f"ERRO na AssemblyAI (HTTP {e.code}). Confira se a chave está certa.\n{e.read()[:300]!r}")
    falas = res.get("utterances") or []
    falantes = {u["speaker"] for u in falas}
    if len(falantes) > 1:
        corpo = "\n\n".join(f"[Falante {u['speaker']}] {u['text']}" for u in falas)
        aviso = (f"# aviso: {len(falantes)} vozes detectadas. So a do especialista entra na analise "
                 f"— identifique qual falante e ele antes de analisar.\n")
    else:
        corpo, aviso = res.get("text", ""), ""
    dur = (res.get("audio_duration") or 0) or None
    destino = out / f"{slug(caminho.stem)}.txt"
    destino.write_text(f"# fonte: {caminho.name}\n# transcricao: AssemblyAI\n{aviso}\n{corpo}\n", "utf-8")
    return destino, res.get("text", ""), dur


# ---------------------------------------------------------------- texto pronto

def do_texto(caminho: pathlib.Path, out: pathlib.Path):
    bruto = caminho.read_text("utf-8", "ignore")
    texto = limpar_legenda(bruto) if caminho.suffix.lower() in {".srt", ".vtt"} else bruto.strip()
    destino = out / f"{slug(caminho.stem)}.txt"
    if destino.resolve() != caminho.resolve():
        destino.write_text(f"# fonte: {caminho.name}\n\n{texto}\n", "utf-8")
    return destino, texto, None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entradas", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    total_pal, total_min = 0, 0.0
    print(f"# Transcrições em {out}\n")
    for e in a.entradas:
        p = pathlib.Path(e)
        if re.match(r"https?://", e):
            destino, texto, dur = do_youtube(e, out)
        elif p.suffix.lower() in VIDEO_AUDIO and p.exists():
            destino, texto, dur = do_arquivo_midia(p, out)
        elif p.suffix.lower() in TEXTO and p.exists():
            destino, texto, dur = do_texto(p, out)
        else:
            print(f"⚠️  ignorado (não achei ou formato desconhecido): {e}")
            continue
        pal = len(texto.split())
        minutos = dur / 60 if dur else pal / PALAVRAS_POR_MINUTO
        total_pal += pal
        total_min += minutos
        print(f"- {destino.name}: {pal} palavras · ~{minutos:.0f} min{'' if dur else ' (estimado)'}")

    print(f"\nTOTAL: {total_pal} palavras · ~{total_min:.0f} min")
    if total_min < 30:
        print(f"⚠️  Abaixo do mínimo de 30 min. Faltam ~{30 - total_min:.0f} min de fala.")
    elif total_min < 60:
        print("✓ Mínimo atingido (rascunho). Com 60 min em 2+ contextos diferentes o documento fica bem mais fiel.")
    else:
        print("✓ Volume bom.")


if __name__ == "__main__":
    main()
