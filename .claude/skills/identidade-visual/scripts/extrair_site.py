#!/usr/bin/env python3
"""
Lê as cores e as fontes que um site usa DE VERDADE, direto do HTML e do CSS.

Uso (Python 3, nada pra instalar):
    python3 extrair_site.py <url> [--saida arquivo.json]

O que sai (no terminal e, com --saida, num JSON):
  - cores mais usadas (hex normalizado, com quantas vezes aparecem)
  - variáveis de CSS que parecem da marca (--primary, --brand, --cor-...)
  - fontes declaradas (font-family) e as do Google Fonts
  - raios de canto mais usados (border-radius)

Por que contar: a cor que aparece 200 vezes é a da marca; a que aparece 1 vez é detalhe.
Branco, preto e cinzas puros vêm separados, porque todo site usa e não dizem nada da marca.

Limite: só lê o que vem no HTML e nos CSS linkados. Site montado todo por JavaScript (ou
Instagram, que bloqueia) volta quase vazio — aí o caminho é print.
"""
import json
import re
import sys
import urllib.request
from collections import Counter
from urllib.parse import urljoin

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


def baixar(url, limite=3_000_000):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read(limite).decode("utf-8", errors="replace")


def hex6(h):
    h = h.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    return "#" + h[:6]


def rgb_para_hex(m):
    partes = re.split(r"[\s,/]+", m.strip())
    try:
        r, g, b = (int(float(p.rstrip("%")) * (2.55 if p.endswith("%") else 1)) for p in partes[:3])
        return "#{:02x}{:02x}{:02x}".format(*(max(0, min(255, v)) for v in (r, g, b)))
    except (ValueError, IndexError):
        return None


def neutra(h):
    r, g, b = int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)
    return max(r, g, b) - min(r, g, b) < 12  # branco, preto e cinza puro


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    url = args[0]
    saida = args[args.index("--saida") + 1] if "--saida" in args else None

    html = baixar(url)
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))
    css += "\n" + "\n".join(re.findall(r'style="([^"]*)"', html, re.I))

    links = re.findall(r'<link[^>]+href="([^"]+)"[^>]*>', html, re.I)
    folhas = [l for l in links if ".css" in l or "fonts.googleapis" in l]
    google = []
    lidas = []
    for href in folhas[:15]:
        abs_url = urljoin(url, href.replace("&amp;", "&"))
        if "fonts.googleapis" in abs_url:
            google += [f.split(":")[0].replace("+", " ") for f in re.findall(r"family=([^&]+)", abs_url)]
            continue
        try:
            css += "\n" + baixar(abs_url)
            lidas.append(abs_url)
        except Exception as e:  # folha que não abre não derruba a leitura
            lidas.append(f"{abs_url} (falhou: {e.__class__.__name__})")
    for imp in re.findall(r"@import\s+url\(['\"]?([^'\")]+)", css):
        if "fonts.googleapis" in imp:
            google += [f.split(":")[0].replace("+", " ") for f in re.findall(r"family=([^&]+)", imp)]

    cores = Counter()
    for h in re.findall(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", css):
        cores[hex6(h)] += 1
    for m in re.findall(r"rgba?\(([^)]+)\)", css):
        h = rgb_para_hex(m)
        if h:
            cores[h] += 1

    variaveis = {}
    for nome, valor in re.findall(r"(--[\w-]+)\s*:\s*([^;}{]+)", css):
        if re.search(r"#|rgb|hsl", valor) and re.search(r"prim|brand|marca|cor|color|accent|destaque|main|secund|second", nome, re.I):
            variaveis.setdefault(nome, valor.strip()[:40])

    fontes = Counter()
    for f in re.findall(r"font-family\s*:\s*([^;}{]+)", css, re.I):
        primeira = f.split(",")[0].strip().strip("'\"")
        genericas = {"inherit", "initial", "sans-serif", "serif", "monospace", "system-ui", "cursive", "-apple-system"}
        if primeira and not primeira.startswith("var(") and primeira.lower() not in genericas and "icon" not in primeira.lower():
            fontes[primeira] += 1

    raios = Counter(r.strip() for r in re.findall(r"border-radius\s*:\s*([^;}{]+)", css, re.I))

    marca = [(h, n) for h, n in cores.most_common() if not neutra(h)][:12]
    neutras = [(h, n) for h, n in cores.most_common() if neutra(h)][:6]
    resultado = {
        "url": url,
        "css_lido": lidas,
        "cores_da_marca": marca,
        "neutras": neutras,
        "variaveis_de_cor": variaveis,
        "fontes": fontes.most_common(8),
        "google_fonts": sorted(set(google)),
        "raios": raios.most_common(6),
    }

    print(f"\n{url}")
    print(f"  CSS lido: {len(lidas)} arquivo(s)")
    print("  cores da marca (mais usadas):", ", ".join(f"{h} ×{n}" for h, n in marca) or "nenhuma — site por JavaScript? use print")
    print("  neutras:", ", ".join(f"{h} ×{n}" for h, n in neutras))
    if variaveis:
        print("  variáveis de cor:", ", ".join(f"{k}={v}" for k, v in list(variaveis.items())[:10]))
    print("  fontes:", ", ".join(f"{f} ×{n}" for f, n in fontes.most_common(8)) or "nenhuma declarada")
    print("  Google Fonts:", ", ".join(resultado["google_fonts"]) or "nenhuma")
    print("  raios:", ", ".join(f"{r} ×{n}" for r, n in raios.most_common(6)))
    if saida:
        with open(saida, "w", encoding="utf-8") as fh:
            json.dump(resultado, fh, ensure_ascii=False, indent=2)
        print(f"  salvo em {saida}")


if __name__ == "__main__":
    main()
