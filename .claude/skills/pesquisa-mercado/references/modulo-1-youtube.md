# Módulo 1 — YouTube (top vídeos + comentários + capas)

**Tempo típico:** 15 min
**Ferramentas:** `scripts/pesquisa.py` (usa yt-dlp) + análise multimodal com a ferramenta Read
**Output:** SEÇÃO 1 do `01` + seção principal do `02` (vídeos curados, dores quantificadas, verbatim, padrões visuais)

Todos os comandos rodam a partir da raiz do repo. `S` abaixo é atalho para
`python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py` (no Windows, `python` ou `py` no lugar de `python3`).
`<W>` é a pasta de trabalho devolvida por `pesquisa.py workdir`.

## Princípio

YouTube é a fonte mais rica do nicho: concentra autoridades, criadores, conteúdo gratuito e comentários verbatim. **Não pular nunca.** Mesmo em nicho B2B existe conteúdo relevante.

## Passo 1: 5-6 buscas em paralelo — MAIS VISTOS + ESTE ANO

Adaptar as buscas ao nicho. Incluir 1-2 em inglês como referência de método/autoridade internacional.

**Regra:** a busca usa os filtros nativos do YouTube **"ordenar por: mais vistos" + "data de envio: este ano"** — nunca `ytsearch:` puro (relevância de todo o período, mistura vídeo de 10 anos atrás). O script já passa `sp=CAMSAggF` por padrão.

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-busca --out "<W>" \
  --q "<busca 1 pt>" --q "<busca 2 pt>" --q "<busca 3 pt>" --q "<busca 4 pt>" --q "<busca 5 en referência>"
```

A ordenação por mais vistos é global: buscas em PT podem trazer vídeo gringo no topo. Não é erro; a curadoria do Passo 3 mantém o equilíbrio 4-6 BR + 1-3 internacionais.

Playbook de variações de busca:
- Específica (palavra-chave do produto): *"preparação física jiu jitsu"*
- Próxima (sintoma): *"como evitar lesão jiu jitsu"*
- Ampla (categoria): *"treino pra lutadores"*
- Voltada ao público (idade/identidade): *"jiu jitsu depois dos 40"*
- Referência internacional: *"BJJ strength conditioning"*

## Passo 2: Dedupe + filtro + top 30 por views

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-top --dir "<W>" --min-views 5000 --n 30 \
  --exclude "<blacklist do nicho, ver tabela no fim>"
```

Gera `<W>/top.json` e imprime `views | duração | canal | id | título`.

**Calibragem com o filtro "este ano":** o universo é só o último ano, então os números são menores. Se sobrarem **menos de 15 vídeos**, rodar de novo com `--min-views 1000`. Se ainda vier pouco, adicionar 2-3 buscas extras (mantendo "este ano"). Ampliar pra todo o período só em último caso, com `--sp CAMSAhAB` ("mais vistos", sem filtro de data):
- modo direto: pedir OK do aluno antes;
- modo briefing: decidir sozinho e registrar no `02`.
Em ambos, marcar esses vídeos como `[all-time]` nas tabelas.

## Passo 3: Curadoria (CRÍTICA — não pular)

Olhar a tabela e **descartar** o que não é escopo:
- Música/rap do nicho
- Conteúdo infantil (se adulto é o alvo)
- Técnica pura quando o produto é outra coisa (e vice-versa)
- Canal genérico sem relevância

Selecionar **10 alvos pra ter 8 efetivos** (alguns vêm com comentários desligados ou poucos). Equilibrar 4-6 brasileiros (público primário) + 1-3 internacionais.

No modo briefing, a curadoria é sua: aplicar os critérios e registrar no `02` o que foi descartado e por quê (1 linha).

## Passo 4: Top 200 comentários de cada, em paralelo

`comment_sort=top` é obrigatório (os 200 baixados já são os mais curtidos segundo o YouTube). O script faz isso:

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-comentarios --out "<W>/comments" ID1 ID2 ID3 ID4 ID5 ID6 ID7 ID8 ID9 ID10
```

Imprime `[qtd] id — título` e lista os que vieram com menos de 30 → trocar pelos próximos da lista.

## Passo 5: Consolidar — ORDENADO POR LIKES

**Likes = voto do público.** O arquivo consolidado sai ordenado por likes, então toda leitura começa pelos comentários mais validados.

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py consolidar --dir "<W>/comments" --out "<W>/all_comments.txt"
```

Formato de cada linha: `[videoID|likes] texto` (texto truncado em 400 caracteres). Se sair < 500 linhas, o script avisa: fazer 2ª rodada de buscas antes de seguir.

### Passo 5.1: Ler o TOP 30 por likes (obrigatório)

Ler as 30 primeiras linhas de `<W>/all_comments.txt` (ferramenta Read com `limit: 30`) **na íntegra e com atenção**. Um comentário com centenas/milhares de likes é dor/desejo validado em massa, vale mais que dezenas de comentários órfãos. Esses 30 alimentam direto: dores prioritárias, verbatim de destaque, ângulos de big idea.

Depois, ler o arquivo inteiro (em blocos, se for grande) antes de quantificar.

## Passo 6: Quantificar padrões (menções + likes acumulados)

Categorias variam por nicho. Exemplos comuns:
- Dor física / sintoma específico
- Idade (30, 40, 50, "anos", "velho")
- Recomeço ("voltei", "comecei", "retorno")
- Fora de forma / autoimagem
- Pedido de programa ("quantas reps", "tem programa", "como faço")
- Jargão tribal do nicho
- Autoridades nomeadas
- Falta de tempo / conciliação

Pra cada categoria:

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py contar --file "<W>/all_comments.txt" \
  --label "IDADE" --regex "\b(30|40|50|60) anos|velho|idade|depois dos"
```

Saída: `IDADE: 87 menções | 4.312 likes acumulados | 8.1% do total (1073)`.

**Ranquear por LIKES ACUMULADOS, não só por menções.** Uma dor com 40 menções e 5.000 likes pesa mais que uma com 80 menções e 300 likes. Quando os dois rankings divergem, registrar: é insight (dor silenciosa vs dor ruidosa).

## Passo 7: Análise multimodal das capas

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py thumbs --out "<W>/thumbs" ID1 ID2 ID3 ID4 ID5 ID6 ID7 ID8
```

Depois abrir cada `.jpg` com a ferramenta **Read** (o Claude enxerga imagem). Extrair:
- Cores dominantes
- Tipografia (com/sem texto, tamanho)
- Composição (centralizado, split, antes/depois)
- Sinais visuais (equipamento, pessoa em ação, autoridade reconhecível)
- Estética (cinematográfica, didática, amadora)

## Modo degradado (sem yt-dlp)

Não dá pra puxar comentários em volume nem ordenar por likes. Fazer assim:
1. **WebSearch** com as mesmas buscas + `site:youtube.com` pra levantar os vídeos mais relevantes do nicho (título, canal, views quando o snippet mostrar).
2. **WebFetch** na página de 4-6 vídeos pedindo título, canal, views, data e a **descrição completa**. Comentários geralmente não vêm; se vierem, entram com a tag `[YT-web]` e sem like count.
3. Capas: WebFetch/download de `https://i.ytimg.com/vi/<ID>/hqdefault.jpg` costuma funcionar; se funcionar, analisar com Read.
4. Compensar o volume com mais peso nos Módulos 2 e 4 e em fóruns/comunidades BR achados via WebSearch (ex.: `"<nicho>" site:reclameaqui.com.br`, `"<nicho>" fórum`, perguntas no Quora/Brainly/grupos públicos).
5. **Registrar no `01` e no `02`:** "Módulo 1 em modo degradado: sem comentários em volume, sem ranking por likes, sem contagem por likes acumulados. Quantificação só por menções nas fontes disponíveis."

## O que gerar pra seção principal do `02`

1. **Tabela "Top vídeos analisados"**: views, canal, título, link, idioma
2. **Top 15-20 comentários por likes** (likes | vídeo | comentário), na íntegra
3. **Padrões de headline** (5-6 fórmulas que se repetem: "N exercícios pra X", "Como Y sem Z", autoridade + benefício…)
4. **Padrões visuais das capas** (3-4 estéticas dominantes + cores + elementos quase obrigatórios)
5. **Dores quantificadas** (tema, menções, **likes acumulados**, %, tradução pro público — ordenada por likes acumulados)
6. **Verbatim por categoria** (4-8 citações literais por categoria, **priorizando as mais curtidas**, com like count: `[355 likes] "..."`)
7. **Identidades / sub-avatares** (tabela com % aprox.)
8. **Jargão tribal** (termos que se repetem)

## Anti-padrões

- ❌ Pular curadoria e puxar comentários de vídeo irrelevante
- ❌ Buscar com `ytsearch:` puro — sempre "mais vistos + este ano" (padrão do script)
- ❌ Ampliar pra todo o período sem registrar (e, no modo direto, sem OK do aluno)
- ❌ Puxar mais de 200 comentários por vídeo (retorno decrescente)
- ❌ Esquecer das capas (perde o diferencial multimodal)
- ❌ Dar a um comentário de 0 like o mesmo peso de um com centenas
- ❌ Citar verbatim sem o like count

## Blacklist por categoria de nicho (usar em `--exclude`)

| Categoria | Blacklist comum |
|---|---|
| **Musicais** (instrumento, canto) | `funk\|sertanejo\|gospel\|hino\|clipe\|kondzilla\|ao vivo\|relaxante\|kids\|cover` |
| **Infantis** (se adulto é o alvo) | `kids\|criança\|infantil\|baby` |
| **Esportivos** | `funk\|memes\|fail\|compilation` |
| **Profissionais** (carreira) | `motivacional\|inspirational\|ted talk` |
| **Produto físico** | `unboxing\|haul\|gifted` |

Adaptar conforme o ruído da primeira rodada.

## Erros comuns

| Erro | Causa | Solução |
|---|---|---|
| Script sai com `SEM_YTDLP` | yt-dlp não instalado | Modo degradado (acima); sugerir `pip install yt-dlp` |
| Poucos vídeos após corte | filtro "este ano" encolhe o universo | `--min-views 1000`, depois buscas extras |
| 0 resultados numa busca | YouTube mudou algo / bloqueio temporário | Repetir 1 vez; atualizar yt-dlp (`pip install -U yt-dlp`); senão, modo degradado pra essa busca |
| Vídeo com < 30 comentários | comentários desligados ou vídeo novo | Trocar pelo próximo (overshoot de 10 pra 8) |
| Capa não baixa | maxres inexistente | O script já tenta `hqdefault` |
| < 500 comentários no total | vídeos com pouco engajamento | 2ª rodada de buscas antes de seguir |
