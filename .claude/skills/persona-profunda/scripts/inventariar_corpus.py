#!/usr/bin/env python3
"""inventariar_corpus.py — skill /persona-profunda

Lê o corpus e gera o bloco "Corpus Analisado" pronto pra colar na persona profunda,
mais o número que decide o modo (COMPLETO x PARCIAL).

Aceita:
  - o `01-corpus-bruto.md` da pesquisa de mercado (blocos `### [TAG | ...]`):
    agrupa os blocos pelo primeiro campo da tag (YT, Reddit, IG, Google,
    Concorrência...) e conta as falas (linhas) de cada um;
  - pasta(s) com material solto (arquivos avulsos): classifica cada arquivo
    pelo prefixo do nome.

Heurística de prefixo de nome de arquivo (sem diferenciar maiúscula):
  vsl_*                        → VSL transcrita
  yt_* / *_youtube             → Vídeo YouTube
  reddit_* / *_reddit          → Thread Reddit
  ig_* / *_instagram           → Post/reel Instagram
  e<N>_* / entrevista_*        → Entrevista 1:1
  review_* / depoimento_*      → Review/depoimento
  ad_* / anuncio_* / criativo_* → Copy de anúncio
  survey_* / form_*            → Survey/formulário
  comentario_* / dm_*          → Comentários/DMs
  call_* / venda_*             → Call de venda / atendimento
Arquivo sem casamento cai em "Outros — reclassificar".

Uso (rodando da raiz do projeto):
  python3 .claude/skills/persona-profunda/scripts/inventariar_corpus.py <corpus.md|pasta> [mais caminhos...]
  python3 .claude/skills/persona-profunda/scripts/inventariar_corpus.py <corpus.md> --data 2026-05-21
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _corpus import EXTENSOES_PADRAO, carregar  # noqa: E402

CATEGORIAS = [
    ("VSLs concorrentes transcritas",   [r"^vsl[_\-]", r"_vsl[_\-]"]),
    ("vídeos do YouTube",                [r"^yt[_\-]", r"_youtube", r"_yt[_\-]"]),
    ("threads do Reddit",                [r"^reddit[_\-]", r"_reddit"]),
    ("posts/reels do Instagram",         [r"^ig[_\-]", r"_instagram", r"_ig[_\-]"]),
    ("entrevistas 1:1",                  [r"^e\d+[_\-]", r"^entrevista[_\-]", r"_entrevista"]),
    ("reviews / depoimentos",            [r"^review[_\-]", r"^depoimento[_\-]", r"_review"]),
    ("copy de anúncio",                  [r"^ad[_\-]", r"^anuncio[_\-]", r"^criativo[_\-]"]),
    ("surveys / formulários",            [r"^survey[_\-]", r"^form[_\-]"]),
    ("comentários / DMs",                [r"^comentario[_\-]", r"^dm[_\-]", r"^comments[_\-]"]),
    ("calls de venda / atendimento",     [r"^call[_\-]", r"^venda[_\-]", r"^atendimento[_\-]"]),
]


def classificar_arquivo(nome: str) -> str:
    base = Path(nome).name.lower()
    for categoria, padroes in CATEGORIAS:
        if any(re.search(p, base) for p in padroes):
            return categoria
    return "Outros — RECLASSIFICAR manualmente"


def agrupar(blocos) -> dict[str, list]:
    grupos: dict[str, list] = defaultdict(list)
    for b in blocos:
        if b.tag == b.arquivo:                       # arquivo solto
            grupos[classificar_arquivo(b.arquivo)].append(b)
        else:                                        # bloco do corpus da pesquisa
            grupos[f"blocos [{b.tipo}]"].append(b)
    return grupos


def renderizar(grupos: dict[str, list], data_fechamento: str) -> str:
    total_materiais = sum(len(v) for v in grupos.values())
    total_falas = sum(len(b.falas) for v in grupos.values() for b in v)
    linhas = ["```", "📊 CORPUS ANALISADO",
              f"Total de materiais: {total_materiais} (blocos/arquivos) · {total_falas} falas distintas", "",
              "Decomposição:"]
    for categoria, blocos in grupos.items():
        falas = sum(len(b.falas) for b in blocos)
        nomes = ", ".join(b.tag[:70] for b in blocos[:6])
        if len(blocos) > 6:
            nomes += f", ... (+{len(blocos) - 6})"
        linhas.append(f"- {len(blocos)} {categoria} — {falas} falas ({nomes})")
    linhas.extend(["", f"Total: {total_materiais} materiais analisados ({total_falas} falas distintas).", "",
                   f"Data de fechamento do corpus: {data_fechamento}", "```"])
    return "\n".join(linhas)


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera o bloco Corpus Analisado (Persona Profunda)")
    parser.add_argument("caminhos", type=Path, nargs="+", help="Arquivo(s) de corpus e/ou pasta(s)")
    parser.add_argument("--data", default=date.today().isoformat(), help="Data de fechamento (AAAA-MM-DD); padrão = hoje")
    parser.add_argument("--extensoes", nargs="*", default=EXTENSOES_PADRAO, help="Extensões lidas dentro de pastas")
    args = parser.parse_args()

    for c in args.caminhos:
        if not c.exists():
            print(f"Erro: {c} não existe.", file=sys.stderr)
            return 1

    blocos = carregar(args.caminhos, args.extensoes)
    if not blocos:
        print("Erro: nenhuma fala encontrada nos caminhos informados.", file=sys.stderr)
        return 1

    print(renderizar(agrupar(blocos), args.data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
