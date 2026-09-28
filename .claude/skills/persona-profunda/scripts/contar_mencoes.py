#!/usr/bin/env python3
"""contar_mencoes.py — skill /persona-profunda

Conta menções de termos (com sinônimos) no corpus, aplicando a regra
"1 fonte distinta = 1 menção" do v5 (a mesma fonte repetindo NÃO infla).

O que conta como "fonte distinta" (--unidade):
  auto  (padrão) — no corpus da pesquisa de mercado (arquivo com blocos
                   `### [TAG | ...]`), cada FALA (linha: um comentário, uma
                   resposta) é uma fonte; num arquivo solto sem blocos (uma
                   entrevista, uma call, um export de DMs), o ARQUIVO inteiro é
                   uma fonte.
  fala           — toda linha de fala é uma fonte (use em export onde cada linha
                   é uma pessoa diferente: respostas de formulário, lista de comentários).
  bloco          — cada bloco (vídeo, thread, página) ou arquivo solto é uma fonte.

Classifica automaticamente pelos thresholds do template:
  Dominante     ≥30
  Secundária    15-29
  Terciária      6-14
  Pontual        2-5
  Insuficiente   1

Arquivo de termos (JSON) — a chave é o rótulo do cluster (vai pra coluna
Elemento), a lista são as variantes buscadas como texto:

  {
    "esgotamento por falta de tempo": ["sem tempo", "vivo correndo", "acordo cansado"],
    "vergonha de pedir ajuda": ["tenho vergonha", "não consigo pedir"]
  }

Busca sem diferenciar maiúscula/minúscula nem acento.

Uso (rodando da raiz do projeto):
  python3 .claude/skills/persona-profunda/scripts/contar_mencoes.py <corpus.md|pasta> [mais caminhos...] --termos termos.json
  python3 .claude/skills/persona-profunda/scripts/contar_mencoes.py <corpus.md> --termos termos.json --formato json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _corpus import EXTENSOES_PADRAO, carregar  # noqa: E402

THRESHOLDS = [
    (30, "Dominante"),
    (15, "Secundária"),
    (6,  "Terciária"),
    (2,  "Pontual"),
    (1,  "Insuficiente"),
    (0,  "Ausente"),
]


def classificar(freq: int) -> str:
    for limite, rotulo in THRESHOLDS:
        if freq >= limite:
            return rotulo
    return "Ausente"


def normalizar(texto: str) -> str:
    """Remove acentos e força minúscula pra casar de forma resiliente."""
    nfkd = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def montar_unidades(blocos, unidade: str) -> dict[str, str]:
    """Devolve {id_da_fonte: texto} conforme a regra de unidade."""
    unidades: dict[str, str] = {}
    for b in blocos:
        solto = b.tag == b.arquivo  # arquivo sem blocos `### [`
        por_fala = unidade == "fala" or (unidade == "auto" and not solto)
        if por_fala:
            for n, texto in b.falas:
                unidades[f"{b.arquivo}:L{n} [{b.tag[:60]}]"] = texto
        else:
            unidades[f"{b.arquivo}:L{b.linha_inicio} [{b.tag[:60]}]"] = "\n".join(t for _, t in b.falas)
    return unidades


def contar(unidades: dict[str, str], termos: dict[str, list[str]]) -> list[dict]:
    norm = {k: normalizar(v) for k, v in unidades.items()}
    resultados = []
    for rotulo, variantes in termos.items():
        variantes_norm = [normalizar(v) for v in variantes if v.strip()]
        if not variantes_norm:
            continue
        padroes = [re.compile(rf"\b{re.escape(v)}\b") for v in variantes_norm]
        hits = [k for k, t in norm.items() if any(p.search(t) for p in padroes)]
        resultados.append({
            "cluster": rotulo,
            "variantes": variantes,
            "frequencia": len(hits),
            "classificacao": classificar(len(hits)),
            "fontes": hits,
        })
    resultados.sort(key=lambda x: x["frequencia"], reverse=True)
    return resultados


def renderizar_markdown(resultados: list[dict], total: int, unidade: str) -> str:
    linhas = [
        "# Contagem de menções — Persona Profunda",
        "",
        f"**Total de fontes distintas no corpus:** {total} (unidade: {unidade})",
        "",
        "Regra: 1 fonte distinta = 1 menção. Repetições na mesma fonte não inflam.",
        "",
        "| Cluster | Frequência | Classificação | Onde apareceu (arquivo:linha [bloco]) |",
        "|---|---:|---|---|",
    ]
    for r in resultados:
        fontes = "; ".join(r["fontes"][:6])
        if len(r["fontes"]) > 6:
            fontes += f"; ... (+{len(r['fontes']) - 6})"
        linhas.append(f"| {r['cluster']} | {r['frequencia']} | **{r['classificacao']}** | {fontes or '—'} |")
    linhas.extend([
        "",
        "> **Atenção:** estes números vêm de busca por texto com sinônimos. Ironia, negação "
        "(\"NÃO tenho medo de...\") e sentido figurado passam batido — revisar as linhas apontadas "
        "antes de usar o número como Frequência final na persona profunda. O script ajuda; quem decide é você.",
    ])
    return "\n".join(linhas)


def main() -> int:
    parser = argparse.ArgumentParser(description="Conta menções de termos no corpus (Persona Profunda)")
    parser.add_argument("caminhos", type=Path, nargs="+", help="Arquivo(s) de corpus e/ou pasta(s)")
    parser.add_argument("--termos", type=Path, required=True, help="JSON {cluster: [variantes]}")
    parser.add_argument("--unidade", choices=["auto", "fala", "bloco"], default="auto", help="O que conta como fonte distinta")
    parser.add_argument("--extensoes", nargs="*", default=EXTENSOES_PADRAO, help="Extensões lidas dentro de pastas")
    parser.add_argument("--formato", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    for c in args.caminhos:
        if not c.exists():
            print(f"Erro: {c} não existe.", file=sys.stderr)
            return 1
    if not args.termos.is_file():
        print(f"Erro: {args.termos} não encontrado.", file=sys.stderr)
        return 1
    try:
        termos = json.loads(args.termos.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Erro ao ler JSON {args.termos}: {e}", file=sys.stderr)
        return 1
    if not isinstance(termos, dict):
        print("Erro: o arquivo de termos deve ser um objeto JSON {cluster: [variantes]}", file=sys.stderr)
        return 1

    blocos = carregar(args.caminhos, args.extensoes)
    if not blocos:
        print("Erro: nenhuma fala encontrada nos caminhos informados.", file=sys.stderr)
        return 1

    unidades = montar_unidades(blocos, args.unidade)
    resultados = contar(unidades, termos)

    if args.formato == "json":
        print(json.dumps({"total_fontes": len(unidades), "unidade": args.unidade, "resultados": resultados},
                         ensure_ascii=False, indent=2))
    else:
        print(renderizar_markdown(resultados, len(unidades), args.unidade))
    return 0


if __name__ == "__main__":
    sys.exit(main())
