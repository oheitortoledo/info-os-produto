---
name: pesquisa-mercado
description: Faz a pesquisa de mercado do seu infoproduto a partir do nicho. É a primeira peça do Alicerce do Copy. Vasculha YouTube (vídeos mais vistos do ano, comentários, capas), Reddit, Google (tamanho do mercado, estudos, autoridades), o que o público busca quando procura solução e os comentários nos vídeos dos concorrentes. Entrega `01-corpus-bruto.md` (material cru com fonte, que alimenta a `/persona-profunda`) e `02-pesquisa-lapidada.md` (resumo pra você ler) em `infoproduto/alicerce-do-copy/pesquisa-de-mercado/`. Use SEMPRE que o aluno disser "pesquisa de mercado", "pesquisa o meu nicho", "estuda meu mercado", "mapeia o mercado", "o que meu público fala", "quais as dores do meu público", "roda a pesquisa". A `/alicerce-copy` dispara esta skill como subagente com um BRIEFING, junto com as outras do Alicerce; o aluno também pode chamá-la sozinha. Ofertas e preços dos concorrentes são da `/mapa-concorrentes`.
metadata:
  type: research
  parte-de: alicerce-do-copy (bloco 1)
---

# Pesquisa de Mercado — bloco 1 do Alicerce do Copy

## O que essa skill faz

Recebe um **nicho/produto** (ex: *"violão para adultos"*, *"gestão de clínica veterinária"*, *"confeitaria para vender"*) e devolve **dois documentos**:

| Arquivo | Função | Quem consome |
|---|---|---|
| `01-corpus-bruto.md` | Material cru identificado por fonte, sem síntese editorial | **`/persona-profunda`** (próxima skill do Alicerce) |
| `02-pesquisa-lapidada.md` | Síntese estratégica (TL;DR, big idea, sub-avatares, headlines, gaps) | **O aluno** (leitura e decisão) |

**Distinção crítica:** o `02` é pra leitura humana. **Nunca** aponte a `/persona-profunda` pro `02` — ela herdaria os vieses da síntese em vez de contar e citar a partir do bruto. Sempre aponte pro `01`.

**Onde ela se encaixa.** O Alicerce do Copy tem 3 blocos: (1) pesquisa de mercado + mapa da concorrência, (2) Persona Profunda, (3) tom de voz do especialista. Esta skill é metade do bloco 1. A outra metade, `/mapa-concorrentes`, roda em paralelo e cuida do raio-x de ofertas, funis e preços. **Não duplicar o trabalho dela aqui.**

## Dois modos de execução

### Modo briefing (disparada como subagente pela `/alicerce-copy`)

Reconhecer pelo bloco `BRIEFING` no prompt:

```
BRIEFING
- Nicho: ...
- Produto: ...
- Público: ...
- Promessa: ...
- Concorrentes conhecidos: ... (opcional)
- Pasta de saída: infoproduto/alicerce-do-copy/pesquisa-de-mercado/
```

Nesse modo:
- **Não fazer perguntas, não pedir aprovação, não abrir arquivo.** Onde o método pede decisão humana (curadoria dos vídeos, ampliar período), decidir sozinho pelos critérios do módulo e registrar a decisão no `02`.
- Rodar tudo até o fim, mesmo em modo degradado.
- Se faltar campo no briefing, inferir do que veio e registrar a inferência nas lacunas. Se faltar a pasta de saída, usar `infoproduto/alicerce-do-copy/pesquisa-de-mercado/`.
- **Devolver só um resumo curto** (é o que volta pra `/alicerce-copy`):

```
PESQUISA DE MERCADO — CONCLUÍDA
Arquivos:
- <pasta>/01-corpus-bruto.md  (N itens de texto)
- <pasta>/02-pesquisa-lapidada.md
Modo: completo | degradado (o que ficou de fora)
5 achados principais:
1. ...
Lacunas:
- ...
```

### Modo direto (o aluno chamou `/pesquisa-mercado`)

Montar o mesmo briefing com **no máximo 3 perguntas curtas**, numa mensagem só, pulando o que o aluno já disse ou o que dá pra ler de `_contexto/` (se existir):

1. "Qual é o seu nicho e o que você vende (ou vai vender)?"
2. "Pra quem é: quem é a pessoa que compra, e o que ela quer conseguir?"
3. "É pro seu produto ou pro produto de um cliente? Se for de cliente, qual o nome?"

Concorrentes conhecidos: se o aluno citar, ótimo; não perguntar à parte.

**Como falar com o aluno no chat:** português simples, "você", sem jargão. Em vez de "VoC" diga "as frases que seu público usa"; em vez de "TAM", "tamanho do mercado"; em vez de "corpus", "material bruto"; em vez de "intent search", "o que as pessoas buscam no Google"; em vez de "SERP", "a primeira página do Google". Os **arquivos** gerados mantêm os termos técnicos e o rigor.

Durante a execução, dar notícias curtas a cada módulo ("Terminei o YouTube: 1.240 comentários lidos. Indo pro Reddit."). No fim, dizer onde estão os dois arquivos, em 5 linhas o que mais chamou atenção e o próximo passo (`/persona-profunda`). Pode abrir o `02` se o aluno quiser.

## Passo 0 — preparar

**0.1 Pasta de saída.** `infoproduto/alicerce-do-copy/pesquisa-de-mercado/`, caminho relativo à raiz do repo.

Criar com `mkdir -p "<pasta>"` (funciona no Mac, Linux e no terminal do Claude Code no Windows; se falhar, criar escrevendo o arquivo direto com a ferramenta Write, que cria as pastas).

Se `01-corpus-bruto.md` ou `02-pesquisa-lapidada.md` já existirem, **não sobrescrever**: salvar como `01-corpus-bruto-v2.md` / `02-pesquisa-lapidada-v2.md` (ou o próximo número livre). Nunca subpasta de data.

**0.2 Checar dependências.** Rodar a partir da raiz do repo:

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py check
```

No Windows, se `python3` não existir, usar `python` ou `py` no lugar (vale pra todos os comandos da skill).

- `MODO=COMPLETO` → seguir normal.
- `MODO=DEGRADADO` (falta o `yt-dlp`) → avisar em 1 linha: *"Pra pesquisa ficar completa, instale o yt-dlp: `pip install yt-dlp` (no Mac também dá `brew install yt-dlp`). Vou seguir agora mesmo assim, com busca no Google."* e **seguir**. Nunca travar esperando instalação. No modo briefing, não avisar: só registrar.
- **Sem Python nenhum** → rodar tudo em modo degradado só com WebSearch/WebFetch.
- `AVISO acesso ao Reddit` → o Reddit costuma bloquear acesso direto; o Módulo 2 tem plano B.

**O que fica de fora no modo degradado** (registrar na seção "Limitações desta rodada" do `02` e no header do `01`): comentários do YouTube em volume, ordenação por likes, contagem por likes acumulados, capas dos vídeos. O substituto está em cada módulo (seção "Modo degradado").

**0.3 Pasta de trabalho temporária** (arquivos pesados que não vão pro repo):

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py workdir "<nicho>"
# imprime o caminho, ex: /tmp/pesquisa-violao-para-adultos  (no Windows: ...\AppData\Local\Temp\pesquisa-...)
```

Guardar esse caminho como `<W>` e usar em todos os módulos. Só os dois `.md` finais vão pra pasta de saída.

## Pipeline em 5 módulos

| # | Módulo | Tempo típico | Ferramentas | Pular se… |
|---|---|---:|---|---|
| 1 | **YouTube** | ~15min | script (yt-dlp) + leitura das capas | nunca pular — é o core (em modo degradado, roda a versão WebSearch) |
| 2 | **Reddit** | ~10min | script (API pública) ou WebSearch `site:reddit.com` | sub principal < 1k inscritos (registrar e seguir) |
| 3 | **Google macro/ciência** | ~10min | WebSearch + WebFetch | nicho sem camada de dados (raro) |
| 4 | **Intent search** (o público buscando solução) | ~15min | WebSearch + script (ytsearch) | nunca pular — é onde aparecem gaps |
| 5 | **Concorrência pela audiência** (enxuto) | ~10min | script (yt-dlp) + WebSearch | nenhum concorrente com canal |

Tempo total típico: **50-70 min**, em paralelo onde der.

**Antes de executar cada módulo, ler o arquivo dele em `references/`** — tem os comandos prontos, critérios de curadoria, anti-padrões e o plano do modo degradado.

### Módulo 1: YouTube → `references/modulo-1-youtube.md`
5-6 buscas (PT-BR + 1-2 EN de referência) com filtro nativo **"mais vistos" + "este ano"** (`sp=CAMSAggF`, já é o padrão do script), top 30 por views, **curadoria crítica** (tirar ruído: música, infantil, canal genérico), 10 alvos pra ter 8 efetivos → top 200 comentários de cada (`comment_sort=top`) + capas (análise multimodal). Consolidação **ordenada por likes**, leitura obrigatória do top 30 mais curtidos, quantificação por menções **e** likes acumulados, verbatim priorizando os mais curtidos com o like count citado.

### Módulo 2: Reddit → `references/modulo-2-reddit.md`
**Check de atividade antes das buscas temáticas.** Sub BR < 1.000 inscritos = insight ("o público BR não usa Reddit nesse nicho"), não falha. Depois: top do ano + 6-8 buscas temáticas no sub principal (pode ser em inglês) + comentários das 8-10 melhores threads. Se o Reddit bloquear o acesso direto, plano B via WebSearch.

### Módulo 3: Google macro/ciência → `references/modulo-3-google.md`
8 WebSearch em paralelo: tamanho de mercado, problemas com dado, ciência da prática, categorias oficiais, recomeço/transição, autoridades nomeadas, benefício adjacente, metodologia de referência. Os 8 vetores são **frames**: traduzir pro nicho antes de buscar.

### Módulo 4: Intent search → `references/modulo-4-intent.md`
6 buscas no Google + 6 no YouTube **escritas como o público digitaria**, uma por estado emocional. Analisar quem domina a primeira página, o vocabulário absorvido e os gaps (título perfeito + views baixas = gap de distribuição).

### Módulo 5: Concorrência pela audiência (enxuto) → `references/modulo-5-concorrencia.md`
Só o que alimenta as frases do público: comentários nos vídeos dos 3-5 concorrentes mais relevantes (quem comenta ali é o público mais qualificado que existe) + a descrição completa desses vídeos (promessas literais, CTAs, iscas). **Nada de varrer landing, checkout, preço, esteira ou funil** — isso é da `/mapa-concorrentes`, que roda em paralelo. Se o briefing trouxe concorrentes, começar por eles.

## Princípios operacionais

1. **Os dois arquivos servem propósitos opostos.** O `01` é input automatizado da `/persona-profunda`: sem síntese, sem viés. O `02` é entregável humano: síntese, big idea, opinião informada. Header de aviso obrigatório nos dois.
2. **Curadoria no meio do pipeline é parte do método.** Busca por palavra-chave traz ruído (ex.: um rap sobre o esporte com 10M de views no topo de uma busca de "preparação física"). Filtrar **antes** de puxar comentários.
3. **Comentário em vídeo de concorrente vale mais que comentário de busca aberta.** Quem comenta ali já passou pelo filtro de interesse.
4. **Análise das capas é diferencial.** Cor, composição, texto, prova social visual: coisa que só texto não pega. Olhar 6-8 capas no Módulo 1 com a ferramenta Read.
5. **"Subreddit morto" é insight, não falha.** Vira dado de canal: onde o público de fato está.
6. **Concorrente técnico ≠ concorrente de posicionamento.** Mesmo nicho amplo com vértice de promessa diferente não disputa o mesmo lugar na cabeça do cliente. Classificar certo no Módulo 5.
7. **Likes são o voto do público — priorizar em TODAS as etapas.** Coleta com `comment_sort=top`, consolidação ordenada por likes, leitura do top 30, ranking por likes acumulados (não só menções), verbatim sempre com o like count: `[355 likes] "..."`.
8. **Volume baixo → 2ª rodada.** Se o Módulo 1 consolidar < 500 comentários, rodar mais buscas antes de seguir (o script avisa).
9. **Toda citação é literal e tem fonte.** Nada de parafrasear e pôr entre aspas. Sem fonte, não entra.
10. **Nunca travar.** Ferramenta faltando, site bloqueado, landing fora do ar: usar o plano B do módulo, registrar a lacuna e seguir.
11. **Quando o script devolver `SEM_YTDLP` (código 3) ou `REDDIT_BLOQUEADO`**, não tentar consertar o ambiente: ir pro modo degradado daquele módulo.

## Estrutura do output

Templates exatos dos dois arquivos em `references/template-output.md`. Resumo da diferença:

| Item | 01-corpus-bruto | 02-pesquisa-lapidada |
|---|:---:|:---:|
| TL;DR / sumário executivo | ❌ | ✅ |
| Comentários YT crus com tag de fonte | ✅ | ❌ |
| Threads Reddit cruas | ✅ | ❌ |
| Verbatim categorizado (amostra) | ❌ | ✅ |
| Big idea / ângulos | ❌ | ✅ |
| Headlines candidatas | ❌ | ✅ |
| Sub-avatares com % | ❌ | ✅ |
| Concorrência (comentários + descrições) | cru | interpretado |
| Quotes Google / estatísticas | cru | curado |
| Header de aviso | ✅ "INPUT da /persona-profunda" | ✅ "NÃO usar na /persona-profunda" |
| Limitações da rodada (modo degradado) | ✅ no header | ✅ seção própria |

## Checklist de qualidade (validar antes de finalizar)

### `01-corpus-bruto.md`
- [ ] Header de aviso "INPUT da `/persona-profunda`" no topo, com o modo (completo/degradado)
- [ ] Seções por fonte (YT, Reddit, YT-Concorrente, Google, status do Reddit BR)
- [ ] Cada bloco com tag: `[YT | Canal | Título | Views | ID]`, `[Reddit | r/sub | post_id]`, `[Web | domínio | título | URL]`, etc.
- [ ] Comentários do YT ordenados por likes dentro de cada bloco, com like count
- [ ] Pelo menos 800 itens de texto (modo completo). Em modo degradado, registrar o volume real
- [ ] Lista de fontes Google com URL completa

### `02-pesquisa-lapidada.md`
- [ ] Header de aviso "NÃO usar na `/persona-profunda`" no topo
- [ ] TL;DR com 6-10 bullets acionáveis
- [ ] 4+ sub-avatares com % aproximado
- [ ] "Top comentários por likes" (15-20 mais curtidos)
- [ ] Dores quantificadas com coluna de likes acumulados, ranqueadas por likes
- [ ] Verbatim em todas as categorias relevantes, com like count
- [ ] Concorrência vista pela audiência (e remissão à `/mapa-concorrentes` pro raio-x de ofertas e preços)
- [ ] Gaps confirmados pela SERP do Módulo 4
- [ ] 3+ ângulos de big idea com justificativa
- [ ] 4-5 headlines candidatas testáveis
- [ ] 6+ fontes acadêmicas / setoriais / autoridades nomeadas no Apêndice B
- [ ] Seção "Limitações desta rodada" (o que ficou de fora e por quê)
- [ ] Próximo passo: `/persona-profunda` apontando pro **01-corpus-bruto.md**

## Princípio guia

Pesquisa boa **descobre coisas que mudam a estratégia**. Pesquisa fraca confirma o que você já achava. Sempre tentar refutar a hipótese de público antes de validar. Se todos os achados batem com a hipótese inicial, **não houve pesquisa, houve busca por confirmação**: voltar e refazer com buscas que poderiam revelar contradição.

E: **o 01 é sagrado.** A qualidade da `/persona-profunda` depende dele estar cru e identificado por fonte. Nunca contaminar com síntese.
