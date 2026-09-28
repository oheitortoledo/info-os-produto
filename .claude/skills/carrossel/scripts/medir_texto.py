#!/usr/bin/env python3
"""
Mede o texto de cada slide do carrossel contra a régua, antes do visual.

Uso (Python 3, nada pra instalar), na raiz do Info OS:
    python3 .claude/skills/carrossel/scripts/medir_texto.py <pasta-do-carrossel>/texto.md

Lê as seções "## Slide NN · <layout>" do texto.md e conta as palavras do que vai NO SLIDE
(as linhas que começam com "> "). Notas, fontes e comentários fora do "> " não contam.

Régua:
  capa           título até 12 palavras · subtítulo até 18
  texto / foto   até 45 palavras no slide
  lista          até 4 itens, cada um até 12 palavras
  citacao        até 25 palavras
  numero / vs    até 35 palavras
  cta            até 30 palavras
  carrossel      de 6 a 10 slides
Acima disso a fonte encolhe no visual e o slide vira parede de texto.
"""
import re
import sys

LIMITE = {"capa": 30, "texto": 45, "foto": 45, "lista": 48, "citacao": 25, "numero": 35, "vs": 35, "cta": 30}


def palavras(s):
    return len(re.findall(r"[\wÀ-ÿ%$]+", s))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    txt = open(sys.argv[1], encoding="utf-8").read()
    partes = re.split(r"^## Slide (\d+)\s*·\s*(\w+).*$", txt, flags=re.M)
    slides = [(int(partes[i]), partes[i + 1].lower(), partes[i + 2]) for i in range(1, len(partes) - 2, 3)]
    if not slides:
        print('Nenhum "## Slide NN · <layout>" encontrado no arquivo.')
        sys.exit(1)
    problemas = []
    print(f"{'slide':<7}{'layout':<10}{'palavras':>9}  {'limite':>6}")
    for n, layout, corpo in slides:
        linhas = [l[1:].strip() for l in corpo.splitlines() if l.startswith(">")]
        total = sum(palavras(l) for l in linhas)
        lim = LIMITE.get(layout, 45)
        marca = "" if total <= lim else "  ⚠ longo"
        print(f"{n:<7}{layout:<10}{total:>9}  {lim:>6}{marca}")
        if total > lim:
            problemas.append(f"slide {n}: {total} palavras (máx {lim} pra {layout})")
        if layout == "capa":
            tit = next((l for l in linhas if l), "")
            if palavras(tit) > 12:
                problemas.append(f"slide {n}: título da capa com {palavras(tit)} palavras (máx 12)")
        if layout == "lista":
            itens = [l for l in linhas if re.match(r"^(\d+[.)]|-|•)\s", l)]
            if len(itens) > 4:
                problemas.append(f"slide {n}: {len(itens)} itens na lista (máx 4)")
            for it in itens:
                if palavras(it) > 12:
                    problemas.append(f"slide {n}: item com {palavras(it)} palavras (máx 12): {it[:40]}…")
    if not 6 <= len(slides) <= 10:
        problemas.append(f"{len(slides)} slides (o carrossel tem de 6 a 10)")
    print()
    if problemas:
        print("Reprovou:\n  " + "\n  ".join(problemas))
        sys.exit(2)
    print("Tudo dentro da régua.")


if __name__ == "__main__":
    main()
