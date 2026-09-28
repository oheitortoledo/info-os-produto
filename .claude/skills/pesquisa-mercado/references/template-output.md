# Templates de output

A skill produz **DOIS** arquivos por pesquisa, na pasta de saída do projeto (nunca em subpasta de data; nova rodada = sufixo `-v2`):

```
infoproduto/alicerce-do-copy/pesquisa-de-mercado/
├── 01-corpus-bruto.md          ← INPUT da /persona-profunda
└── 02-pesquisa-lapidada.md     ← leitura humana
```


Os dois têm **header de aviso obrigatório no topo** dizendo quem consome. Não inverter.

Os exemplos abaixo usam um nicho fictício (preparação física pra jiu-jitsu) só pra mostrar o formato. Nunca copiar o conteúdo dos exemplos pro documento real.

---

## Template 1: `01-corpus-bruto.md`

**Função:** material cru identificado por fonte, **input da `/persona-profunda`**.
**Tamanho típico:** 150-400 KB / 1.500-3.000 linhas no modo completo (material bruto é volume). No modo degradado, bem menor: tudo bem, desde que registrado.

### Header obrigatório

```markdown
# Corpus Bruto — <Nicho/Produto>

> ✅ **DOCUMENTO INPUT da `/persona-profunda`.** Material cru com tag de fonte em cada bloco, sem síntese editorial. Pronto pra `/persona-profunda` contar menções, atribuir Intensidade e citar fontes literais.
>
> 📋 **Pra leitura humana** (TL;DR, big idea, headlines, sub-avatares): abrir `02-pesquisa-lapidada.md` nesta mesma pasta.
>
> **Comando sugerido:** `/persona-profunda` usando `<pasta de saída>/01-corpus-bruto.md`

---

**Gerado:** AAAA-MM-DD
**Modo:** completo | degradado — <o que ficou de fora, em 1 linha>
**Fontes:** [N comentários YT / M comentários Reddit / K comentários em concorrentes / X fontes web]

---
```

### Estrutura por seções

Cada seção agrupa uma fonte. Cada bloco tem **tag de fonte** padronizada.

```markdown
## SEÇÃO 1 — YouTube: comentários do nicho

Tag: `[YT | Canal | Título | Views | VideoID]`. Comentários no formato `[likes] texto`, **ordenados por likes (decrescente)** dentro de cada vídeo.

### [YT | Canal Exemplo | TREINO DE FORÇA PARA JIU-JITSU | 601k v | AbCdEfGhIjK]

_Comentários processados: 146_

[355] <comentário literal mais curtido>
[73] <comentário literal>
[62] <comentário literal>
[...]

---

[...repete pra cada vídeo do Módulo 1...]

> Modo degradado: blocos `[YT-web | Canal | Título | Views | URL]` com a descrição e o que a página trouxer; sem like count.


## SEÇÃO 2 — Reddit: threads + comentários

Tag: `[Reddit | r/sub | post_id | título do post | score]`. OP + comentários top no formato `[score] texto`.

### [Reddit | r/bjj | abc123 | I am a 44 yr old dad and I am obsessed with BJJ | 417 ups | 110 cm]

**OP:**

> <texto literal do post original>

**COMMENTS:**

[99] <comentário literal>
[70] <comentário literal>
[...]

> Plano B: blocos `[Reddit-web | r/sub | URL]` ou `[Reddit-snippet | r/sub | URL]`.


## SEÇÃO 3 — YouTube Concorrentes: descrições + comentários

Mesmo formato da SEÇÃO 1, com a DESCRIÇÃO COMPLETA do vídeo antes dos comentários.

### [YT-Concorrente | Canal Exemplo | Como Treinar 4x Por Semana Depois dos 35 Sem Se Quebrar | 845 v | XyZ123abcDE]

**Tipo:** mesmo vértice | vértice diferente | adjacente | autoridade lateral | mídia

**DESCRIÇÃO COMPLETA:**

```
[descrição literal do vídeo, com links e CTAs, até ~3000 caracteres]
```

**COMMENTS:**

[likes] texto...

---


## SEÇÃO 4 — Google e buscas do público (fontes + dados + quotes literais)

Sem síntese. Tag `[Web | domínio | título | URL]` em cada item.

### 4.1 Tamanho de mercado
- <dado literal> — [Web | dominio.gov.br | título | https://...]

### 4.2 Problemas com base em dado
- <prevalência literal> — [Web | ... | https://...]

### 4.3 Quotes de autoridades
**<Nome da autoridade>:**
"<quote literal>"
Fonte: [Web | ... | https://...]

[seguir pelos 8 vetores do Módulo 3]

### 4.9 Buscas do público (Módulo 4) — resultados crus
**Busca:** "<busca do público>"
- Google top 5: <título — domínio — URL> (x5)
- YouTube: [views v] canal — título (até 8)

[repetir pras 12 buscas]


## SEÇÃO 5 — Reddit BR (status)

Saída bruta do check:

```
r/<nicho>_brasil       [HTTP 404] subs=?
r/<nicho>brasil        [HTTP 200] subs=289
[...]
```

**Implicação factual:** ativo / morto / bloqueado (plano B). Sem interpretação estratégica.
```

### Princípios do corpus bruto

- **Sem TL;DR, sem big idea, sem ranking interpretativo**
- Texto **literal** de cada fonte, com tag de origem
- Tags padronizadas pra `/persona-profunda` parsear
- Pode ser gordo (200-500 KB) — esperado
- **Não filtrar verbatim** "feio" ou "irrelevante" — a `/persona-profunda` decide o que serve
- Único corte: limitar cada comentário a 400-500 caracteres

---

## Template 2: `02-pesquisa-lapidada.md`

**Função:** síntese estratégica pra leitura humana. **NÃO usar como input da `/persona-profunda`.**
**Tamanho típico:** 30-80 KB / 600-1.200 linhas.

### Header obrigatório

```markdown
# Pesquisa de Mercado — <Nicho/Produto>

> ⚠️ **DOCUMENTO LAPIDADO — síntese estratégica pra leitura humana.**
> ⚠️ **NÃO usar como input da `/persona-profunda`** — este documento já vem com curadoria, big idea, sub-avatares, headlines e interpretações. Se a `/persona-profunda` ler isto, herda estas hipóteses em vez de extrair do bruto.
> ⚠️ **Pra rodar a `/persona-profunda`, use o `01-corpus-bruto.md`** desta mesma pasta.
>
> Este `02` serve pra você ler, decidir estratégia e checar se a pesquisa foi na direção certa.

---

**Data:** AAAA-MM-DD
**Fontes:** [resumo]
**Modo:** completo | degradado
**Público primário (hipótese):** [1 linha]
```

### Estrutura completa

```markdown
## Sumário executivo (TL;DR)

1. [Achado mais importante — uma frase forte]
2. [Público consolidado em 1 frase: idade/identidade/contexto]
3. [Dor primária quantificada]
4. [Dor secundária / vetor adicional]
5. [Característica do nicho que muda a estratégia]
6. [Insight cultural ou de linguagem]
7. [Quem domina vs gap real]
8. [Maior oportunidade em 1 frase]

---

## Top vídeos / threads / fontes analisadas (curados)
[Tabela: Views/Score | Canal/Sub | Título | Origem | Link]
**Canais BR dominantes:** [lista]
**Descartados na curadoria:** [1 linha com critério]

## Padrões de headline (fórmulas que viralizam)
[Tabela: Fórmula | Exemplo | Por que funciona]

## Padrões visuais das capas
[Tabela: Estética | Quem usa | Sinal que transmite] + **Cores dominantes**

## Dores quantificadas
[Tabela: Tema | Menções | Likes acumulados | % | Tradução pro público — ordenada por likes acumulados]

## Top comentários por likes (validação em massa)
[Tabela: Likes | Vídeo/Fonte | Comentário — top 15-20 do corpus inteiro]

## Verbatim — citações curadas (amostras literais)
Priorizar os mais curtidos de cada categoria; citar o like count.

### Sobre [categoria 1]
> [355 likes] "..."
> [73 likes] "..."

[6-10 categorias, 4-8 amostras cada]

## Identidades / sub-avatares no nicho
[Tabela: Sub-avatar | Sinais | % aprox.]

## Objeções típicas (= ângulos de copy a desarmar)
1. **"[objeção literal]"** → resposta: [contra-argumento]
[7-10 objeções]

## Jargão tribal (linguagem pra incorporar na copy)
[Tabela: Termo | Uso | Onde aparece]

## Ângulos quentes pra big idea
### 🎯 1. "[nome do ângulo]"
**Por que:** [dados que sustentam]
**Lacuna:** [o que ninguém faz]
**Headline-teste:** *"..."*
[3-5 ângulos]

## Pontos cegos / oportunidades (gap analysis)
[Lista numerada de gaps confirmados pela SERP]

## Headlines candidatas testáveis
[4-5 headlines com promessa + prova embutida]

## Limitações desta rodada
- Modo: completo | degradado
- [O que ficou de fora e por quê — ex.: "sem yt-dlp: comentários do YouTube só via página, sem ranking por likes"]
- [Decisões tomadas sem o aluno no modo briefing — ex.: "ampliei o período pra todo o histórico porque o ano trouxe 9 vídeos"]
- [Inferências feitas a partir de briefing incompleto]

---

# APÊNDICE A — Reddit (síntese)
[Confirma / adiciona / refuta em relação ao Módulo 1]

# APÊNDICE B — Google (macro + ciência)
[Estatísticas-âncora prontas pra página de vendas + quotes de autoridade]

# APÊNDICE C — Intent search (o público buscando solução)
[Quem domina a SERP + linguagem absorvida + gaps]

# APÊNDICE D — Concorrência vista pela audiência
[Tipologia + promessas literais + verbatim dos comentários. Ofertas e preços: ver /mapa-concorrentes]

---

## Próximo passo recomendado

A síntese está aqui no `02`. O material bruto está em `01-corpus-bruto.md` nesta mesma pasta.

Próxima skill do Alicerce: **`/persona-profunda`**, apontando pro **`01-corpus-bruto.md`** (não pro 02).
Ela vai contar menções, atribuir Intensidade (Forte/Média/Fraca) com base em evidência real e citar fontes literais.
Se você está rodando a `/alicerce-copy`, ela já faz isso sozinha.
```

### Princípios da pesquisa lapidada

- **Tabelas** sempre que possível
- **Citações em blockquote** com aspas pro verbatim literal
- **Links em markdown** `[texto](url)` em todas as fontes
- **% aproximado** sempre que quantificar
- **Negrito** em conclusões-chave
- Bullets em vez de parágrafos longos
- Tom: direto, sem floreio, pt-BR coloquial-profissional
- **Sempre fecha** apontando pro `01` como input da `/persona-profunda`
