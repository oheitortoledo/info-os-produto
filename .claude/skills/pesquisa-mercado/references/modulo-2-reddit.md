# Módulo 2 — Reddit (threads + verbatim)

**Tempo típico:** 10 min
**Ferramentas:** `scripts/pesquisa.py` (API JSON pública do Reddit, sem token) — plano B: WebSearch + WebFetch
**Output:** SEÇÃO 2 e SEÇÃO 5 do `01` + Apêndice A do `02`

Comandos a partir da raiz do repo; `<W>` = pasta de trabalho. No Windows, `python`/`py` no lugar de `python3`.

## Princípio

Reddit é a fonte mais crua de verbatim do mundo anglo-saxão. Comentários lá são mais elaborados e argumentativos que no YouTube: ótimos pra **objeção**, menos pra **dor crua**.

**Reddit BR costuma estar morto pro nicho.** Quando acontecer, **registrar como insight** ("o público BR não usa Reddit nesse nicho, está em IG/YouTube/grupos") e seguir com o sub principal em inglês.

**O Reddit bloqueia acesso direto com frequência** (HTTP 403, depende da rede). Quando o script imprimir `REDDIT_BLOQUEADO`, ir direto pro **plano B** no fim deste arquivo. Não gastar tempo tentando contornar.

## Passo 0 (obrigatório): check de atividade ANTES das buscas temáticas

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py reddit-check <nicho>_brasil <nicho>brasil <nicho>br <nicho_em_ingles>
```

Saída: `r/<sub> [HTTP 200] subs=289 — descrição`.

Critério de "morto": **< 1.000 inscritos** ou < 10 posts no último mês.

Se o BR estiver morto:
- `01` (SEÇÃO 5): colar a saída bruta do check
- `02`: insight de canal ("o público BR não está no Reddit nesse nicho, está em […]")
- Pular buscas temáticas no BR e seguir com o sub em inglês (se existir)
- Se o de inglês também não existir / for pequeno, **pular o Módulo 2** e seguir pro 3

## Passo 1: Top do ano do sub principal

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py reddit-top --sub <sub> --out "<W>/reddit"
```

Dá o panorama do que viraliza (costuma misturar meme/notícia). Só contexto inicial.

## Passo 2: Buscas temáticas (6-8)

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py reddit-busca --sub <sub> --out "<W>/reddit" \
  --q "<termo dor>" --q "<termo idade>" --q "<termo recomeço>" --q "<termo objeção principal>" --q "<termo solução comum>" --q "<termo resultado>"
```

Imprime, por busca, os 6 melhores posts: `[score up | comentários] post_id | título`.

## Passo 3: Curadoria das threads

Escolher 8-10 threads, priorizando **título com o público se declarando** (ex.: *"I am a fat out of shape 44 yr old dad and I am obsessed with BJJ"*). Essas são ouro.

## Passo 4: Puxar comentários das threads escolhidas

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py reddit-threads --sub <sub> --out "<W>/reddit/threads" <id1> <id2> <id3> <id4> <id5> <id6> <id7> <id8>
```

## Passo 5: Consolidar em texto

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py reddit-consolidar --dir "<W>/reddit/threads" --out "<W>/reddit_all.txt"
```

Formato: bloco por post (título, score, corpo do OP) + comentários `[score] texto` ordenados por score.

## Passo 6: Ler tudo

Ler `<W>/reddit_all.txt` com Read. Extrair:
- **Verbatim** que valida/refuta o Módulo 1
- **Padrões novos** que não apareceram no YouTube
- **Sub-avatares** do Reddit (EUA/UK diferem do BR)
- **Quantificação** de temas vs Módulo 1

## Plano B (Reddit bloqueado ou sem Python)

1. **WebSearch** com `site:reddit.com/r/<sub> <termo>` (e `site:reddit.com <nicho> <termo>`) pras mesmas 6-8 buscas temáticas.
2. **WebFetch** nas 5-8 threads mais promissoras, pedindo: *"título, texto do post original e os comentários mais votados na íntegra, cada um com a pontuação se aparecer"*. Tentar a URL com `old.reddit.com` se a `www` falhar.
3. Se o WebFetch também for bloqueado, usar só os trechos que o WebSearch devolve, com a tag `[Reddit-snippet | r/sub | URL]`.
4. **Registrar no `01` e no `02`:** "Módulo 2 via plano B (acesso direto bloqueado): N threads lidas pela web, sem contagem completa de comentários."

## O que gerar no Apêndice A do `02`

```markdown
# APÊNDICE A — Reddit

**Data:** AAAA-MM-DD
**Fonte:** r/<sub> + buscas temáticas (X comentários + Y threads) | acesso: direto / plano B
**Status BR:** ativo / morto (com insight)

## A.1 — O que muda em relação ao Módulo 1? (confirma / adiciona / refuta)
## A.2 — Padrões NOVOS (com citações)
## A.3 — Verbatim adicional (6-10 citações categorizadas, com score)
## A.4 — Ajustes às hipóteses (reforça / adiciona / refuta)
```

## Padrões culturais conhecidos

- Reddit BR é morto em quase todo nicho de massa (esporte, fitness, marketing); quando vive, é em comunidades bem específicas (tecnologia, games).
- r/<nicho> geral vence r/<nicho>_brasil em 9 de 10 nichos.

## Erros comuns

| Erro | Causa | Solução |
|---|---|---|
| `REDDIT_BLOQUEADO` / HTTP 403 | Reddit recusa acesso sem login nessa rede | Plano B |
| HTTP 429 | Muitas requisições | O script já espera e tenta de novo; se persistir, esperar 1 min |
| HTTP 302/404 no check | Sub não existe ou é privado | Testar variações do nome |
| Thread com 0 comentários | Travada/removida | Escolher outra |
