---
name: mapa-concorrentes
description: Levanta quem mais vende no seu nicho e o que cada um vende: produtos, promessa principal, preço e o caminho até a compra, com o link de onde cada dado saiu. Entrega dois documentos só com fatos, sem opinião: `mapa-concorrentes.md` (15 a 25 concorrentes em tabela + mapa de preços do mercado) e `dossie-concorrencia.md` (fichas fundas dos principais). Bloco 1 do Alicerce do Copy, junto com a /pesquisa-mercado (a /alicerce-copy roda as duas). Use SEMPRE que o usuário disser "mapa de concorrentes", "analisa a concorrência", "quem são meus concorrentes", "quem vende o mesmo que eu", "quanto os concorrentes cobram", "quanto cobram no meu nicho", "raio-x da concorrência", "dossiê de concorrência", "mapeia o mercado", ou receber um bloco BRIEFING pedindo o mapa da concorrência. NÃO é a pesquisa do público (/pesquisa-mercado) nem a persona (/persona-profunda).
---

# Mapa de Concorrentes — produtos, promessas, preços e funis do nicho

## O que essa skill faz

Recebe um **nicho** (ex: *"construção para venda"*, *"jiu-jitsu online"*, *"piano pra adulto iniciante"*) e o produto de quem está pedindo, e devolve **dois documentos** de inteligência competitiva:

| Arquivo | Função | Formato |
|---|---|---|
| `mapa-concorrentes.md` | **Varredura larga.** Todos os players, agrupados por vértice, cada um em tabela `produto · promessa · ticket`. Fecha com um **mapa de preços factual** + pendências. | Amplo — 15 a 25 players |
| `dossie-concorrencia.md` | **Mergulho.** Uma ficha **factual** funda por player prioritário (identidade, esteira com preços, big idea literal, funil, reputação) + pendências. | Fundo — top 4 a 6 players |

Os moldes exatos dos dois documentos estão em `references/templates.md`. O passo a passo da coleta está em `references/coleta-por-concorrente.md`.

> ## ⚠️ REGRA-MÃE: DADO BRUTO, ZERO RECOMENDAÇÃO
> Estes dois documentos são **matéria-prima factual pra análise** — não a análise. Catalogam o que cada concorrente **é, vende e cobra**. Eles **NÃO** contêm: "oportunidade pro aluno", "onde você entra/ataca", "território livre", "fácil de contra-posicionar", posicionamento sugerido, SWOT, matriz de recomendação, nem "leitura estratégica". A interpretação é um **passo separado, depois** (a persona e a oferta, dentro do Alicerce do Copy), que **consome** estes dados. Se você se pegar escrevendo o que o aluno *deveria fazer*, parou de mapear e começou a opinar. Corte.

## Os dois modos de rodar

Decida o modo pela **primeira mensagem**:

### Modo briefing (rodando como subagente da `/alicerce-copy`)

Se o prompt contém um bloco **`BRIEFING`** (nicho, produto, público, promessa, concorrentes já conhecidos — opcional — e PASTA DE SAÍDA):

- **NÃO faça perguntas.** Não peça aprovação. Não abra arquivo no final. Ninguém está olhando o chat — só o resultado conta.
- Use a **PASTA DE SAÍDA** do briefing exatamente como veio (`mkdir -p`).
- Se faltar algum campo, siga com o que tem e registre a lacuna nas pendências do documento. Só o **nicho** é indispensável; sem ele, devolva na hora "faltou o nicho no briefing" e pare.
- Rode as 4 fases até o fim, sem parar no meio.
- **Devolva um resumo curto** (é o que a skill maestra lê):

```
MAPA DA CONCORRÊNCIA — [nicho]
Arquivos: [caminho]/mapa-concorrentes.md · [caminho]/dossie-concorrencia.md
Players mapeados: [N] ([n] mesmo vértice · [n] adjacente · [n] genérico · [n] sem produto)
Faixa de preço confirmada: [entrada R$X–Y · principal R$X–Y · alto R$X+ · recorrência R$X/mês]
5 achados (fatos, sem recomendação):
1. [...]
2. [...]
3. [...]
4. [...]
5. [...]
Lacunas: [o que ficou não público / não varrido / ferramenta que faltou e o que isso deixou de fora]
```

### Modo direto (o aluno chamou `/mapa-concorrentes`)

O aluno é especialista no assunto dele, mas **leigo em marketing**. Então:

1. **Primeiro, procure o que já existe.** Leia `_contexto/` e, se houver, a pesquisa de mercado e o que mais houver do Alicerce do Copy do projeto. O que você achar lá, não pergunte.
2. **No máximo 3 perguntas curtas, numa mensagem só**, só do que faltou. Exemplo:
   - "Qual é o assunto do seu produto e pra quem ele é? (ex: piano pra adulto que nunca tocou)"
   - "Você já conhece algum concorrente? Pode mandar nome, @ ou link — se não conhecer, eu acho."
3. Com as respostas, monte o briefing internamente e **rode até o fim sem mais perguntas**.
4. Ao terminar, diga em 3-5 linhas o que achou e onde salvou (ver "Como falar com o aluno").

### Como falar com o aluno (só no modo direto)

No chat, português simples, "você", frases curtas, e diga **o que está fazendo e por quê** em uma linha ("Agora vou abrir a página de compra de cada um, porque é lá que o preço aparece"). Nada de jargão no chat — traduza:

| Termo técnico (pode ficar nos arquivos) | Como falar no chat |
|---|---|
| funil | o caminho que o cliente faz até comprar |
| ticket | preço |
| front / tripwire / produto de entrada | produto de entrada (o mais barato) |
| high-ticket | produto caro (mentoria, acompanhamento) |
| esteira | a lista de produtos que ele vende, do mais barato ao mais caro |
| OTO / upsell / order bump | oferta extra na hora da compra |
| vértice | o tipo de promessa que ele vende |
| big idea | a promessa principal |
| landing / página de vendas | página de vendas |
| checkout | página de pagamento |
| lead | contato (quem deixou nome/WhatsApp) |
| perpétuo / lançamento | vende o ano todo / vende em datas específicas |

Nos **arquivos** os termos técnicos podem ficar — mas o topo de cada documento leva uma legenda curta explicando cada um (já está nos templates).

## Onde salvar

Padrão do produto — o bloco 1 do Alicerce é "pesquisa de mercado + mapa da concorrência", então tudo vai na **mesma pasta** da pesquisa de mercado:

```
infoproduto/alicerce-do-copy/pesquisa-de-mercado/
├── mapa-concorrentes.md       ← varredura larga + mapa de preços
├── dossie-concorrencia.md     ← fichas fundas + pendências
└── concorrentes/              ← material cru da coleta (páginas salvas, listas de vídeos, transcrições)
```

- Caminho relativo à raiz do repositório.
- Em ordem de prioridade: (1) se o briefing/prompt trouxe uma PASTA DE SAÍDA, use ela; (2) senão, o padrão acima.
- Crie a pasta com `mkdir -p "<pasta>/concorrentes"`. Nunca apague nada que já esteja lá (a pesquisa de mercado pode estar sendo escrita ao mesmo tempo, na mesma pasta).
- **Nunca sobrescreva.** Se `mapa-concorrentes.md` já existe, a nova rodada vira `mapa-concorrentes-v2.md` e `dossie-concorrencia-v2.md` (depois `-v3`...). Mapas de concorrência envelhecem rápido — a comparação entre rodadas é dado útil.
- O material cru vai em `concorrentes/`, não solto na pasta nem em pasta temporária do sistema (o aluno pode estar no Windows).

## Antes de começar — checar ferramentas (nunca travar)

A skill funciona só com o Claude Code (WebSearch, WebFetch e terminal). Uma ferramenta opcional deixa a coleta do YouTube melhor:

```bash
yt-dlp --version 2>/dev/null || echo "SEM_YTDLP"
curl --version 2>/dev/null | head -1 || echo "SEM_CURL"
```

- **Sem `yt-dlp`:** diga em uma linha (modo direto) — *"Pra olhar os vídeos do YouTube com mais detalhe dá pra instalar o yt-dlp (Mac: `brew install yt-dlp` · Windows: `winget install yt-dlp`). Vou seguir sem ele agora."* — e **siga em modo degradado**: descubra canais e vídeos por WebSearch (`site:youtube.com <nicho>`) e WebFetch na página do vídeo. Registre nas pendências do documento: "YouTube varrido sem yt-dlp — descrições de vídeo coletadas parcialmente".
- **Sem `curl`** (raro): use só WebFetch nas páginas de produto e registre "varredura de sitemap não feita" nas pendências.
- **Biblioteca de Anúncios da Meta** costuma bloquear leitura automática. Tente uma vez; se não vier, o **link da busca pronto** já é dado útil — entra no documento pra consulta manual. Não insista.
- Nenhuma dessas faltas para a skill. O documento sai com o que deu, e o que ficou de fora vira pendência escrita.

## As 4 dimensões que sempre extrair

Pra **cada** concorrente, o objetivo é preencher quatro coisas — nessa ordem de prioridade:

1. **PRODUTOS** — a esteira inteira, não só o carro-chefe. Entrada barata (tripwire), core, high-ticket, comunidade/assinatura, upsells. Um player pode ter 1 produto ou 5.
2. **PROMESSAS** — a big idea / headline literal. Copiar a frase como está na página (entre aspas). É o "lugar na cabeça do cliente" que ele ocupa.
3. **TICKETS** — o preço de **cada** produto da esteira. Com ancoragem (`R$X de R$Y`) e parcelamento quando houver, e **sempre com a fonte em link clicável** apontando pra página exata onde o número foi lido. `não público` é um dado válido — registrar + anotar como se conseguiria (entrar como lead), mas a página do produto entra linkada mesmo assim.
4. **FUNIL** — como capta e converte. Orgânico vs pago, lançamento vs perpétuo, webinar vs sessão estratégica vs venda por WhatsApp, isca → nutrição → oferta.

> **A regra de ouro:** um concorrente **não é uma URL, é um conjunto de URLs.** Site institucional, landing de vendas, checkout, produto na Hotmart/Kiwify/Eduzz, link da bio do Instagram, Biblioteca de Anúncios, Reclame Aqui, descrição dos vídeos do YouTube — cada uma revela uma peça diferente. Varrer só a home perde a esteira, os preços e o funil. O playbook está em `references/coleta-por-concorrente.md`.

## Pipeline em 4 fases

### Fase 0 — Escopo & eixo de batalha

Antes de buscar, definir (a partir do briefing ou das respostas):

- **O nicho exato** (o "lugar na cabeça do cliente", não o nicho amplo). *"Construção para venda"* ≠ *"mercado imobiliário"*. *"Piano pra adulto iniciante"* ≠ *"música"*.
- **O produto de referência** (o do aluno): promessa e público. É o que define o que conta como "mesmo vértice".
- **Os eixos de público que se confundem no nicho.** Ex: em imóveis, *investidor* vs *quem constrói pra vender* são públicos diferentes com a mesma palavra-chave. Separar isso cedo evita classificar errado depois.
- **Concorrentes que o aluno já conhece** entram direto na lista longa (e costumam ser prioridade no dossiê).

### Fase 1 — Descoberta (montar a lista longa)

Objetivo: **lista longa antes de filtrar.** Mirar 15-25 nomes. É melhor achar demais e cortar do que fechar cedo — uma segunda varredura costuma dobrar a lista. O mercado é sempre mais povoado do que parece.

Fontes de descoberta (rodar em paralelo quando possível):
- **YouTube** — canais que dominam o nicho (`yt-dlp "ytsearch20:<keyword>"`, ou WebSearch `site:youtube.com <keyword>` sem yt-dlp)
- **Google / busca de intenção** — buscar como o público digitaria: `"curso <nicho>"`, `"mentoria <nicho>"`, `"como <resultado que o público quer>"`
- **Hotmart / Kiwify / Eduzz** — quem vende infoproduto no tema (via WebSearch: `site:hotmart.com <nicho>`)
- **Instagram** — perfis com audiência no nicho (mesmo os sem produto → audiência órfã)
- **Biblioteca de Anúncios da Meta** — quem está pagando tráfego agora (sinal de operação viva)

Pra cada nome, já anotar a **tipologia** (ver "Agrupamento por vértice") — não tratar todo canal grande como concorrente direto. Salve a lista longa em `concorrentes/lista-longa.md` (nome · @ · URL onde foi achado).

**Um player conta pro mapa mesmo sem preço confirmado.** Se vende um produto no vértice mas o ticket ficou `não público` (típico da cauda longa da Hotmart), ele **é** um player mapeado — entra na tabela com `não público` e vira pendência. Preço confirmado é meta pros prioritários, não requisito de entrada no mapa.

### Fase 2 — Coleta por concorrente

Pra cada player da lista, varrer o **conjunto de URLs** e preencher as 4 dimensões. Este é o coração da skill.

→ **Ler `references/coleta-por-concorrente.md` antes de começar** — tem o checklist de URLs, os comandos prontos (sitemap, curl, yt-dlp, WebFetch estruturado), o contorno da Hotmart, o que fazer quando a página cai, e como tirar reputação do Reclame Aqui.

Priorizar profundidade nos players do **mesmo vértice** e nos que o aluno citou. Nos demais, um passe raso (produto · promessa · ticket) já basta pro mapa.

Faça a coleta **você mesmo** (sequencial ou em poucos lotes) — não abra um subagente por concorrente (ver aviso no reference).

### Fase 3 — Síntese (montar os dois documentos)

→ **Usar os templates exatos de `references/templates.md`** (incluindo a legenda de termos no topo).

1. **`mapa-concorrentes.md`** — todos os players nas tabelas, agrupados por vértice. Fechar com o **mapa de preços factual** (player · produto · ticket confirmado · fonte clicável) e as **pendências**. Nada de "onde você entra".
2. **`dossie-concorrencia.md`** — **panorama factual** do mercado (mecanismo, vértices, faixas de ticket) + uma ficha factual funda por player prioritário (identidade, audiência, esteira COM PREÇOS, big idea literal, método, funil, reputação) + pendências. Sem SWOT, sem matriz, sem "oportunidades".

### Fase 4 — Entregar

O entregável é o `.md` (não há exportação pra PDF).

- **Modo briefing:** devolva o resumo curto (formato em "Modo briefing") e pare. Não abra arquivo.
- **Modo direto:** diga ao aluno, em português simples, onde salvou, quantos concorrentes achou, a faixa de preço do mercado e 3 fatos que chamaram atenção — **fatos, não conselho**. Termine dizendo qual é o próximo passo do Alicerce (a persona, que vai usar este mapa). Se quiser abrir o arquivo pra ele: Mac `open "<arquivo>"` · Windows `start "" "<arquivo>"`.

## Agrupamento por vértice (classificação de dado)

Os players entram no mapa **agrupados por quão perto a oferta deles está da promessa do produto de referência**. Isso é classificação factual (o que o player *vende*), pra organizar o dado — **não** é ranking de ameaça nem recomendação:

| Grupo | Significado | Critério |
|---|---|---|
| 🔴 **Mesmo vértice** | Vende a mesma promessa central, pro mesmo público. | big idea equivalente |
| 🟡 **Vértice adjacente** | Mesmo público, promessa/mecanismo diferente. | ex: vende "técnica de venda", não "autoridade digital" |
| 🟢 **Vizinho / genérico** | Nicho vizinho, produto complementar, ou não específico do público. | — |
| ⚪ **Sem produto** | Tem público no tema mas não vende oferta paga identificada. | audiência órfã |

Classificar pela **oferta real** (o que vende), não pelo tamanho da audiência: 500 mil seguidores num vértice diferente segue sendo "vértice adjacente".

## Princípios operacionais

1. **Lista longa antes de filtrar.** Fechar a lista cedo é o erro nº 1. Mirar 15-25 nomes na descoberta, cortar depois.
2. **Um concorrente = várias URLs.** A home raramente tem preço. O preço mora no checkout / Hotmart / "falar com consultor". O funil mora na Biblioteca de Anúncios, na bio e na descrição dos vídeos. A reputação mora no Reclame Aqui.
3. **Tipologia importa mais que tamanho.** Não deixar a audiência inflar a classificação.
4. **`não público` é dado, não buraco.** Muito preço fica atrás de "falar com consultor", WhatsApp ou checkout que só carrega no navegador. Registrar como `não público` **e** anotar na pendência como fechar (entrar como lead, Wayback, site terceiro). **Nunca inventar preço.**
5. **Reputação é dado.** Checar o Reclame Aqui dos players do mesmo vértice e registrar os fatos (nota, volume, temas recorrentes). O que isso significa pro aluno é passo seguinte, não entra aqui.
6. **Fonte é link, não nota de rodapé.** Todo número, promessa literal, claim e garantia sai com a URL exata clicável. Produto sem preço confirmado também leva o link da sua página. Sem URL pública = `não público`/`não varrido` + pendência, nunca número solto nem link inventado.
7. **Dado bruto, zero recomendação (regra-mãe).**
8. **Hotmart bloqueia leitura direta.** Contorno (WebSearch em sites terceiros) em `references/coleta-por-concorrente.md`.
9. **Tente uma vez, depois siga.** Página caída, Ad Library, Reclame Aqui: uma tentativa, depois fallback ou pendência. Insistir na mesma URL morta é o maior desperdício de tempo.
10. **Datar e re-varrer.** A skill é feita pra rodar de novo em 60-90 dias (`-v2`). Quem entrou, quem subiu preço, quem mudou de funil — a comparação é dado por si só.

## Checklist de qualidade (antes de finalizar)

### Pra `mapa-concorrentes.md`
- [ ] Header com nicho + data + aviso "DADOS BRUTOS, sem recomendação" + legenda de termos
- [ ] Pelo menos 12 players, agrupados por vértice (descritivo)
- [ ] Cada player com `produto · promessa (entre aspas) · ticket` + @ do Instagram linkado (ou `@?` + pendência)
- [ ] Preço **confirmado em fonte viva** no máximo de players possível; `não público`/`não varrido` só quando exaurido
- [ ] **Toda fonte é link clicável** (`[texto](https://url)`) pra página exata do dado — zero URL em texto puro, zero caminho relativo (`/oferta/`, `home`)
- [ ] **Todo produto listado tem link** pra sua página/checkout — inclusive os de ticket `não público`
- [ ] **Mapa de preços factual** + **pendências** (incluindo ferramentas que faltaram e o que isso deixou de fora)
- [ ] ZERO: leitura estratégica, oportunidades, "onde você entra", recomendação

### Pra `dossie-concorrencia.md`
- [ ] Legenda de termos + panorama factual do mercado (mecanismo + vértices + faixas de ticket) — sem "conclusão"
- [ ] Ficha factual funda por player prioritário (identidade, audiência, esteira COM PREÇOS, big idea literal, método, funil, reputação)
- [ ] Coluna `Fonte` de cada esteira com link clicável pra página exata; produto sem preço também linkado
- [ ] Pendências de coleta (o que ficou `não público`/`não varrido` + como fechar)
- [ ] ZERO: SWOT, matriz, oportunidades, "onde você ataca"

## Princípio guia

Um mapa de concorrência bom é **factual, completo e conferível** — a esteira inteira de cada player, o **preço real** de cada produto (lido no site/checkout, não estimado) **com a fonte clicável ao lado**, a promessa literal, o funil de verdade. Um mapa fraco lista nomes e deixa metade dos preços em branco por preguiça de varrer o site. O valor está na **completude e na precisão do dado** — a interpretação é o próximo passo do Alicerce. Não opine; documente.
