"""_corpus.py — leitura de corpus compartilhada pelos scripts da skill /persona-profunda.

Entende dois formatos, e aceita os dois misturados:

1. **Corpus da pesquisa de mercado** (`01-corpus-bruto.md`): UM arquivo grande,
   dividido em blocos que começam com `### [TAG | ...]` (ex.: `### [YT | Canal |
   Título | 601k v | VideoID]`). Dentro de cada bloco, cada linha de texto é uma
   fala distinta (um comentário, uma resposta, um trecho).

2. **Pasta de arquivos soltos** (outras fontes salvas em arquivo: entrevista transcrita,
   export de comentários etc.). Cada arquivo é um material.
   Se um arquivo solto também tiver blocos `### [`, ele é lido como o formato 1.

Só biblioteca padrão do Python.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

RE_BLOCO = re.compile(r"^###\s*\[(?P<tag>[^\]]+)\]")
# Linhas que não são fala: títulos, separadores, metadados em itálico, citações de instrução.
RE_NAO_FALA = re.compile(r"^(#|---|___|\*\*\*|_[^_].*_$|>|```|\|?-{3,})")

EXTENSOES_PADRAO = [".txt", ".md", ".vtt", ".srt", ".csv"]


@dataclass
class Bloco:
    arquivo: str
    tag: str                      # conteúdo entre colchetes do "### [...]", ou nome do arquivo
    linha_inicio: int
    falas: list[tuple[int, str]] = field(default_factory=list)  # (nº da linha, texto)

    @property
    def tipo(self) -> str:
        """Primeiro campo da tag (YT, Reddit, IG, Google, Concorrência...)."""
        return self.tag.split("|")[0].strip() or "Outros"


def ler_texto(arquivo: Path) -> str:
    try:
        return arquivo.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return arquivo.read_text(encoding="latin-1", errors="ignore")


def eh_fala(linha: str) -> bool:
    t = linha.strip()
    return bool(t) and not RE_NAO_FALA.match(t) and len(t) >= 3


def blocos_do_arquivo(arquivo: Path, nome: str) -> list[Bloco]:
    texto = ler_texto(arquivo)
    linhas = texto.splitlines()
    tem_blocos = any(RE_BLOCO.match(l.strip()) for l in linhas)

    if not tem_blocos:
        bloco = Bloco(arquivo=nome, tag=nome, linha_inicio=1)
        bloco.falas = [(i, l.strip()) for i, l in enumerate(linhas, 1) if eh_fala(l)]
        return [bloco]

    blocos: list[Bloco] = []
    atual: Bloco | None = None
    for i, linha in enumerate(linhas, 1):
        m = RE_BLOCO.match(linha.strip())
        if m:
            atual = Bloco(arquivo=nome, tag=m.group("tag").strip(), linha_inicio=i)
            blocos.append(atual)
            continue
        if linha.startswith("## "):   # nova seção do corpus fecha o bloco anterior
            atual = None
            continue
        if atual is not None and eh_fala(linha):
            atual.falas.append((i, linha.strip()))
    return blocos


def carregar(caminhos: list[Path], extensoes: list[str] | None = None) -> list[Bloco]:
    """Lê arquivos e/ou pastas e devolve a lista de blocos-fonte."""
    exts = [e if e.startswith(".") else f".{e}" for e in (extensoes or EXTENSOES_PADRAO)]
    blocos: list[Bloco] = []
    for caminho in caminhos:
        if caminho.is_file():
            blocos.extend(blocos_do_arquivo(caminho, caminho.name))
        elif caminho.is_dir():
            for arq in sorted(caminho.rglob("*")):
                if arq.is_file() and arq.suffix.lower() in exts:
                    blocos.extend(blocos_do_arquivo(arq, arq.relative_to(caminho).as_posix()))
    return [b for b in blocos if b.falas]
