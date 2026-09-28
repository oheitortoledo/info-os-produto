#!/usr/bin/env python3
"""
Mede a voz do especialista nas transcrições — a parte contável da metodologia.

Não interpreta nada: devolve números pra análise não depender de impressão.
  - volume (palavras, minutos estimados) por arquivo e total
  - ritmo de frase (mediana, % curtas/médias/longas) — só se a transcrição tem pontuação
  - perguntas por 1.000 palavras
  - vícios de fala (tipo, né, então, aí...) por 1.000 palavras + política de copy escrito
  - expressões repetidas (2 e 3 palavras) e em QUANTOS arquivos aparecem
    (a regra H1 da metodologia pede 3+ ocorrências em contextos distintos)
  - aberturas de frase mais comuns

Uso:
    python3 medir_voz.py <pasta-ou-arquivos.txt ...> [--ignorar "Falante B"]

Sem dependências — só a biblioteca padrão do Python.
"""

import argparse
import collections
import pathlib
import re
import statistics

PPM = 150
VICIOS = ["tipo", "né", "então", "aí", "beleza", "tá", "cara", "mano", "galera", "pessoal",
          "gente", "olha", "ó", "sabe", "entendeu", "show", "bora", "vamo", "basicamente",
          "literalmente", "meio que", "vamos dizer assim", "tá ligado", "na real", "enfim",
          "assim", "bom", "certo", "ok", "sacou", "velho", "véi", "uai", "tchê", "bah"]
STOP = set("""a o e é de da do das dos em no na nos nas um uma uns umas que se por para pra pro
com sem mas ou como mais menos muito muita já não sim ele ela eles elas eu você vocês me te lhe
nos isso isto esse essa este esta aquele aquela aqui ali lá então aí tá né the to of and
foi ser ter tem está estou era vai vou vão faz fazer tudo todo toda também só quando porque
qual quem onde sobre até depois antes meu minha seu sua dele dela ao à às aos pelo pela
tipo cara coisa coisas assim bom tão bem ainda""".split())


def ler(arquivos, ignorar):
    textos = {}
    for p in arquivos:
        linhas = []
        for l in p.read_text("utf-8", "ignore").splitlines():
            if l.startswith("#"):
                continue
            if ignorar and l.startswith(f"[{ignorar}]"):
                continue
            linhas.append(re.sub(r"^\[Falante [A-Z]\]\s*", "", l))
        textos[p.name] = " ".join(linhas)
    return textos


def palavras(t):
    return re.findall(r"[a-záàâãéêíóôõúüç]+(?:-[a-záàâãéêíóôõúüç]+)?", t.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entradas", nargs="+")
    ap.add_argument("--ignorar", help='rótulo de falante pra excluir, ex.: "Falante B"')
    a = ap.parse_args()

    arquivos = []
    for e in a.entradas:
        p = pathlib.Path(e)
        arquivos += sorted(p.glob("*.txt")) if p.is_dir() else [p]
    textos = ler(arquivos, a.ignorar)
    todas = {n: palavras(t) for n, t in textos.items()}
    total = sum(len(w) for w in todas.values())
    if not total:
        raise SystemExit("Nenhuma palavra encontrada.")

    print("# Medição de voz\n")
    print("## Volume\n")
    for n, w in todas.items():
        print(f"- {n}: {len(w)} palavras · ~{len(w)/PPM:.0f} min")
    print(f"\n**Total: {total} palavras · ~{total/PPM:.0f} min · {len(todas)} arquivo(s)**\n")

    corpo = " ".join(textos.values())
    pontos = len(re.findall(r"[.!?]", corpo))
    print("## Ritmo de frase\n")
    if pontos < total / 40:
        print("⚠️  Transcrição quase sem pontuação (legenda automática). Métrica de frase NÃO é confiável —"
              " avalie o ritmo lendo trechos, não por número.\n")
    else:
        frases = [f for f in re.split(r"(?<=[.!?])\s+", corpo) if palavras(f)]
        tam = [len(palavras(f)) for f in frases]
        curtas = sum(t < 12 for t in tam) / len(tam) * 100
        longas = sum(t > 25 for t in tam) / len(tam) * 100
        print(f"- {len(frases)} frases · mediana {statistics.median(tam):.0f} palavras")
        print(f"- curtas (<12): {curtas:.0f}% · médias: {100-curtas-longas:.0f}% · longas (>25): {longas:.0f}%")
        print(f"- perguntas: {corpo.count('?')/total*1000:.1f} por 1.000 palavras\n")
        aberturas = collections.Counter(" ".join(palavras(f)[:2]) for f in frases if len(palavras(f)) >= 2)
        print("**Aberturas de frase mais comuns** (padrão dominante = 30%+ das ocorrências da função):\n")
        for exp, c in aberturas.most_common(12):
            print(f"- \"{exp}…\" — {c}×")
        print()

    print("## Vícios de fala (por 1.000 palavras)\n")
    print("| Marcador | Ocorrências | Por 1.000 | Política no texto escrito |\n|---|---|---|---|")
    baixo = " " + " ".join(palavras(corpo)) + " "
    linhas = []
    for v in VICIOS:
        c = len(re.findall(rf"(?<![a-záàâãéêíóôõúüç]){re.escape(v.rstrip('?'))}(?![a-záàâãéêíóôõúüç])", baixo))
        if c:
            linhas.append((c / total * 1000, v, c))
    for taxa, v, c in sorted(linhas, reverse=True)[:15]:
        pol = ("manter no informal · 30-50% no formal" if taxa > 5 else
               "manter no informal · 10-20% no formal" if taxa >= 2 else "usar pontualmente")
        print(f"| {v} | {c} | {taxa:.1f} | {pol} |")
    print()

    print("## Expressões repetidas\n")
    print("Candidatas a palavra-assinatura. **Em N arquivos** é o que separa assinatura de assunto do dia.\n")
    for n_gram in (3, 2):
        cont, onde = collections.Counter(), collections.defaultdict(set)
        for nome, w in todas.items():
            for i in range(len(w) - n_gram + 1):
                g = w[i:i + n_gram]
                if g[0] in STOP or g[-1] in STOP:
                    continue
                exp = " ".join(g)
                cont[exp] += 1
                onde[exp].add(nome)
        print(f"**{n_gram} palavras:**\n")
        for exp, c in cont.most_common(20):
            if c < 3:
                break
            print(f"- \"{exp}\" — {c}× em {len(onde[exp])} arquivo(s)")
        print()

    uni = collections.Counter(x for w in todas.values() for x in w if x not in STOP and len(x) > 3)
    print("**Palavras mais usadas (sem palavras comuns):** " +
          " · ".join(f"{p} ({c})" for p, c in uni.most_common(30)))


if __name__ == "__main__":
    main()
