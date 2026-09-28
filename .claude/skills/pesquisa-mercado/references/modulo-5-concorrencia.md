# Módulo 5 — Concorrência pela audiência (versão enxuta)

**Tempo típico:** 10 min
**Ferramentas:** `scripts/pesquisa.py` (yt-canal, yt-info, yt-comentarios, consolidar) + WebSearch
**Output:** SEÇÃO 3 do `01` + Apêndice D do `02`

## Escopo — o que este módulo FAZ e o que NÃO faz

Este módulo existe **só pra alimentar as frases do público**: quem comenta no vídeo de um concorrente é o público mais qualificado que existe (já passou pelo filtro de interesse no tema). E a descrição desses vídeos traz as promessas literais que o público está ouvindo.

| Faz aqui | NÃO faz aqui (é da `/mapa-concorrentes`) |
|---|---|
| Identificar 3-5 concorrentes relevantes com canal | Lista longa de 15-25 players |
| Comentários dos top 2-3 vídeos de cada (ordenados por likes) | Varrer landing, checkout, Hotmart, bio, Reclame Aqui |
| Descrição completa desses vídeos (promessas, CTAs, iscas, links) | Extrair preço, esteira, ancoragem, garantia, bônus |
| Classificar a tipologia (quem disputa o mesmo lugar na cabeça do cliente) | Mapear funil e mapa de preços |

A `/mapa-concorrentes` roda em paralelo no mesmo bloco do Alicerce. **Não abrir landing page nem buscar preço aqui.** Se um link de oferta aparecer numa descrição, ele vai pro `01` como texto literal (faz parte da descrição) e ponto.

## Distinção crítica: tipologia do concorrente

Antes de puxar comentários, classificar cada nome:

| Tipo | Exemplo (nicho: preparação física pra lutadores) | Disputa o público? |
|---|---|---|
| **Mesmo vértice de promessa** | canal de preparação física específica pra luta | ✅ SIM |
| **Nicho amplo, vértice diferente** | canal de drills técnicos | ❌ complementar |
| **Adjacente** | cursos de técnica | ❌ outro produto |
| **Conteúdo + autoridade lateral** | fisioterapeuta do esporte | ⚠️ fonte/parceiro |
| **Mídia/notícia** | canal de notícias do esporte | ❌ não vende |

Validar sempre: **ele vende algo que ocupa o mesmo "lugar na cabeça do cliente"?** Priorizar comentários de quem é ✅ e ⚠️.

## De onde vêm os nomes

Nesta ordem: (1) concorrentes do BRIEFING, (2) canais que apareceram no Módulo 1, (3) quem dominou a primeira página no Módulo 4 (C.4). Não fazer descoberta ampla: isso é da `/mapa-concorrentes`.

## Comandos

`<W>` = pasta de trabalho. No Windows, `python`/`py` no lugar de `python3`.

### Passo 1: Achar o canal e listar os vídeos

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-canal --out "<W>/concorrentes" --handle <HandleDoCanal>
# se der 0 vídeos (handle errado):
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-canal --out "<W>/concorrentes" --busca "<nome do concorrente> <nicho>"
```

Listagem de canal não traz views. Pra escolher os top 2-3 de cada, puxar info dos candidatos (Passo 2) e ordenar por views.

### Passo 2: Descrição completa + views (é aqui que estão as promessas)

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-info --out "<W>/concorrentes" ID1 ID2 ID3 ...
```

Gera `info_<ID>.json` com título, canal, views, likes, nº de comentários, data e **descrição completa**. A descrição vai **inteira** pro `01` (SEÇÃO 3).

### Passo 3: Comentários dos top 2-3 vídeos de cada concorrente

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-comentarios --out "<W>/concorrentes/comments" ID1 ID2 ID3 ID4 ID5 ID6
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py consolidar --dir "<W>/concorrentes/comments" --out "<W>/comments_concorrentes.txt"
```

Ler o top 20 por likes primeiro, depois o resto.

### Nicho B2B / técnico: descrição > comentários

Em nicho B2B (gestão de clínica, SaaS, contabilidade), 6-30 comentários por vídeo é normal. Não é falha. Dar mais peso às **descrições** (CTAs literais, promessas, iscas, bullets do produto).

## Modo degradado (sem yt-dlp)

- WebSearch `site:youtube.com "<concorrente>"` pra achar os vídeos mais vistos.
- WebFetch na página de 2-3 vídeos de cada, pedindo título, views e **descrição completa**.
- Comentários em volume ficam de fora: registrar no `01` e no `02`.

## O que gerar no Apêndice D do `02`

```markdown
# APÊNDICE D — Concorrência vista pela audiência

> Raio-x de ofertas, preços, esteiras e funis: ver os arquivos da `/mapa-concorrentes`
> (mesmo projeto, pasta `alicerce-do-copy/`). Este apêndice cobre só o que o público
> diz e ouve nos canais dos concorrentes.

## D.1 — Concorrentes analisados (tabela: concorrente | canal | tipo | disputa o público? | vídeos lidos)
## D.2 — Promessas literais que o público está ouvindo (das descrições e títulos, com fonte)
## D.3 — VERBATIM dos comentários nos concorrentes (priorizar os mais curtidos, sempre `[likes] "..."`)
## D.4 — O que o público cobra/pede/reclama nesses canais (pedidos, frustrações, objeções)
## D.5 — Clichês do nicho (promessas e CTAs que se repetem entre concorrentes)
## D.6 — Fontes consultadas
```

## Anti-padrões

- ❌ Tratar todo canal grande do nicho como concorrente direto (ignorar tipologia)
- ❌ Pular a descrição dos vídeos (perde as promessas literais)
- ❌ Pular os comentários dos concorrentes (perde o público mais qualificado)
- ❌ Abrir landing page / buscar preço aqui — duplica a `/mapa-concorrentes`
