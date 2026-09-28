---
name: persona-profunda
description: Bloco 2 do Alicerce do Copy. Lê só o que o bloco 1 produziu (corpus bruto da pesquisa de mercado + mapa e dossiê da concorrência) e entrega numa rodada 3 documentos com evidência literal em cada linha: a Persona Profunda (11 seções, cada item medido por intensidade e nº de menções), a matriz de benefícios por tipo de cliente e o banco de frases do público por ângulo. Use SEMPRE que o aluno disser "persona profunda", "persona", "quem é meu cliente", "dores do meu público", "o que meu cliente quer", "objeções", "desculpas pra não comprar", "tipos de cliente", "matriz de benefícios", "banco de frases", "banco de verbatim", "frases do meu público". A /alicerce-copy roda o Alicerce inteiro e dispara esta como subagente. Sem a pesquisa do bloco 1, manda rodar /pesquisa-mercado antes. Não escreve copy.
---

# Persona Profunda (bloco 2 do Alicerce do Copy)

Esta skill transforma a pesquisa de mercado bruta em **três documentos encadeados**, gerados numa rodada só:

1. **`persona-profunda-<nicho>-v1.md`** — a **Persona Profunda (esqueleto Deep Persona Research v5)**: 11 seções de captura quantificada, preenchendo o template canônico em [`references/template-persona-profunda.md`](references/template-persona-profunda.md).
2. **`matriz-beneficios-<nicho>-v1.md`** — a **Matriz de Benefícios por subpersona**: Feature → Funcional → Dimensional → Emocional → Identidade, cruzado com LF8 + 9 Desejos Secundários, uma matriz por subpersona do S11. Framework canônico em [`references/framework-matriz-beneficios.md`](references/framework-matriz-beneficios.md).
3. **`banco-verbatim-<nicho>-v1.md`** — o **Banco de Verbatims por Ângulo**: índice que organiza as falas literais do público por ângulo (dor, medo, desejo, objeção, inimigo, identidade, jargão, gatilho). Molde em [`references/template-banco-verbatim.md`](references/template-banco-verbatim.md).

A skill **não improvisa estrutura** — preenche os três moldes canônicos respeitando formato, prefixos, regras de evidência e o encadeamento: a matriz deriva da persona profunda; o banco deriva da persona profunda + matriz + corpus.

A regra inegociável da persona profunda: **toda informação vem com evidência**. Cada linha de cada tabela analítica carrega `[fonte] — [localização] — "[citação literal]"`. Nada é achismo. Frequência substitui opinião, verbatim substitui paráfrase, evidência substitui achismo.

A regra inegociável da matriz: **nada na matriz vem do nada — tudo deriva da persona profunda**.

A regra inegociável do banco: **fala literal, rastreável, com lastro no corpus**.

---

## Pra quem é esta skill (vale pra sessão inteira)

Quem usa **não é copywriter**. Está montando o próprio infoproduto (ou o de um cliente) e aprendendo o método agora. Duas regras:

1. **Por dentro, rigor total.** Dentro dos arquivos ficam os códigos (S1–S11, LF8, [M/L/P], [V/S], Intensidade × Frequência), a regra de evidência literal, os thresholds, os modos COMPLETO/PARCIAL e as lacunas. Nada disso é afrouxado.
2. **Por fora, zero jargão.** No chat, nunca diga "S5", "VoC", "LF8", "verbatim", "subpersona", "threshold", "cluster" sem traduzir. Fale curto, em português simples, tratando por "você", e diga em uma frase **o que está fazendo e por quê** — ele aprende o método enquanto usa.

### Nomes que o aluno vê

| Código (só nos arquivos) | Como falar com o aluno |
|---|---|
| Persona Profunda | "o retrato completo do seu cliente" (pode chamar de persona profunda também) |
| S1 | quem é o seu cliente (perfil) |
| S2 | o problema de verdade |
| S3 | como o problema aparece no dia a dia |
| S4.1 | o que dói |
| S4.2 | o que ele quer |
| S4.3 | o que ele tem medo que aconteça |
| S5 | o que ele pensa e não fala |
| S6 | o antes e o depois |
| S7 | como ele fala, onde presta atenção e como compra |
| S8 | o culpado (quem ele acha que atrapalha) |
| S9.1 | o que empurra ele pra comprar |
| S9.2 | o que faz ele desconfiar e fugir |
| S10 | as desculpas pra não comprar |
| S10.c | a desculpa que ele nunca fala em voz alta |
| S11 / subpersonas | os tipos de cliente que você tem |
| LF8 | os 8 desejos básicos do ser humano |
| Desejos Secundários | os desejos do dia a dia (economizar, praticidade, qualidade...) |
| verbatim / VoC | as frases exatas do seu público |
| banco de verbatim | o banco de frases do seu público, separado por assunto |
| Intensidade × Frequência | "o quanto dói" e "quantas pessoas falaram disso" |
| modo PARCIAL | "retrato inicial — dá pra começar, mas tem buraco" |
| lacuna | "o que ainda falta descobrir" |

---

## Modos de execução

### Modo briefing (subagente da `/alicerce-copy`)

A `/alicerce-copy` dispara esta skill depois que o bloco 1 (pesquisa de mercado + mapa da concorrência) termina, com uma mensagem contendo um bloco **BRIEFING**, por exemplo:

```
BRIEFING
Nicho: ...
Produto: ...
Pasta do bloco 1: infoproduto/alicerce-do-copy/pesquisa-de-mercado/
Pasta de saída: infoproduto/alicerce-do-copy/persona-profunda/
```

Regras do modo briefing:
- **Não pergunta nada.** Tudo que no modo direto seria pergunta (renda sem evidência, conflito entre fontes, depois sem evidência) vira `⚠ lacuna` no documento e item na lista de lacunas.
- Lê da pasta do bloco 1: `01-corpus-bruto.md` (mina principal de falas), `02-pesquisa-lapidada.md` (contexto e hipóteses — **não** é evidência; nunca citar como fonte de fala), `mapa-concorrentes.md` e `dossie-concorrencia.md` (tickets, promessas e funis do mercado — alimentam S7.5, S8, S9 e S10.3/10.4 como **fato de mercado**, marcados como tal, não como fala do público). Se algum faltar, seguir com o que existe e registrar a ausência nas lacunas.
- Roda os 3 documentos até o fim.
- **Devolve ao orquestrador um resumo curto**, neste formato exato:

```
PERSONA — [COMPLETO | PARCIAL] (N = [materiais] materiais · [falas] falas do público)
Arquivos:
- <pasta de saída>/persona-profunda-<nicho>-v1.md
- <pasta de saída>/matriz-beneficios-<nicho>-v1.md
- <pasta de saída>/banco-verbatim-<nicho>-v1.md
- <pasta de saída>/notas-brutas.md (lastro da contagem)
Tipos de cliente (S11):
- [Nome, idade, marcador] — [o diff dele em 1 linha]
- ...
Top 3 dores: 1) "[...]" ([N] menções) · 2) ... · 3) ...
Top 3 objeções: 1) [camada] "[...]" ([N]) · 2) ... · 3) ...
Lacunas: [lista curta do que falta pesquisar]
```

### Modo direto (`/persona-profunda`)

O aluno chamou a skill sozinho. Siga o **Passo 0** abaixo, rode tudo, e no fim apresente o resultado **em linguagem de gente** (ver "Entrega ao aluno"). A skill não pede material ao aluno: trabalha só com o que o bloco 1 produziu. Se ele colar material por conta própria, trate como corpus adicional, com a mesma regra de fonte.

---

## Onde salvar

```
infoproduto/alicerce-do-copy/persona-profunda/
```

- No modo briefing, usar a pasta de saída recebida.
- Criar com `mkdir -p` antes de escrever.
- **Versionar por sufixo, nunca sobrescrever**: se `persona-profunda-<nicho>-v1.md` já existe, a rodada nova gera `-v2` (e assim por diante), nos três documentos juntos.
- `<nicho>` = slug curto, minúsculo, sem acento, com hífen (ex.: `consorcio-imovel`).
- `notas-brutas.md` (extração crua, arquivo de trabalho) fica na mesma pasta.

---

## Passo 0 — Achar a pesquisa (modo direto)

Procure o corpus do bloco 1 dentro do projeto, rodando da raiz do repositório:

```bash
find infoproduto -path '*alicerce-do-copy/pesquisa-de-mercado*' -type f 2>/dev/null
```

- **Achou em um projeto só** → diga ao aluno qual pesquisa vai usar e siga.
- **Achou em mais de um** → pergunte uma vez: "Achei pesquisa em [A] e [B]. De qual projeto é essa persona?"
- **Não achou nada** → pare e diga, sem inventar:

> Pra montar o retrato do seu cliente eu preciso primeiro da pesquisa de mercado — é dela que saem as frases reais do seu público. Sem ela, eu estaria chutando. Rode `/pesquisa-mercado` (ou `/alicerce-copy`, que faz a pesquisa, o retrato do cliente e o tom de voz em sequência) e depois me chame de novo.

Achada a pesquisa, leia da mesma pasta os mesmos quatro arquivos do modo briefing (`01-corpus-bruto.md`, `02-pesquisa-lapidada.md` como contexto, `mapa-concorrentes.md`, `dossie-concorrencia.md`) e siga direto pro inventário.

---

## Modos de operação (COMPLETO x PARCIAL)

Decida no passo 1 (Inventário) e registre no header da persona profunda. No modo direto, avise o aluno em uma frase ("Tem material suficiente pra um retrato completo" / "Dá pra fazer um retrato inicial; vou marcar o que falta descobrir").

**Como contar materiais.** O `01-corpus-bruto.md` é um arquivo só, dividido em blocos `### [TAG | ...]` (um vídeo, uma thread, uma página). Dentro de cada bloco, **cada linha de fala (um comentário, uma resposta, um trecho) é uma menção distinta** — é a regra de contagem do v5 ("comentário distinto = 1 menção"). Arquivo solto sem blocos (uma entrevista transcrita, por exemplo) = 1 material. Blocos de concorrente, dados, jurisprudência e thumbs **não são fala do público**: entram no inventário, mas não contam pra decidir o modo.

### Modo COMPLETO
Corpus robusto: 50+ materiais de fala do público (idealmente 100+), vindos de mais de um bloco-fonte. Todas as seções preenchidas. Frequências reais permitem atingir o threshold Dominante (≥30). É a persona profunda definitiva da oferta.

### Modo PARCIAL
Corpus inicial (5–49 materiais de fala do público), ou tudo vindo de uma fonte só. Usado pra começar a copy antes da pesquisa fechar. Regras específicas:

- No header do documento, marcar explicitamente `⚠ PERSONA PROFUNDA PARCIAL — N=[total] materiais. Lacunas mapeadas ao final.`
- Onde NÃO houver evidência mínima (campo crítico sem fonte): preencher com `⚠ lacuna — falta [tipo de fonte: ex: entrevistas com persona-mãe; ticket histórico; transcrição VSL concorrente]` em vez de inventar.
- Frequências reportadas com a ressalva real (`12/15 fontes = 80%, MAS amostra pequena`).
- Thresholds suspendem o rótulo "Dominante" automaticamente quando N<30 — usar a frequência relativa em vez da absoluta como classificador provisório.
- Bloco obrigatório ao final: `## Lacunas a fechar — próximo ciclo de pesquisa`, listando exatamente que tipo de material precisa entrar pra fechar cada seção em falha.

Menos de 5 materiais de fala do público → não gere a persona profunda. Modo direto: diga ao aluno que a pesquisa veio fraca e sugira rodar `/pesquisa-mercado` de novo, com mais fontes. Modo briefing: devolva `PERSONA — BLOQUEADO (N=[x])` com o motivo e o que falta.

---

## O sistema de quantificação

Duas dimensões SEPARADAS — nunca confunda:

### Intensidade (qualitativa)
Quão forte é o elemento quando aparece. Três níveis:
- **Forte** — verbalizado com emoção alta, linguagem extrema, repetição dentro do mesmo material
- **Média** — verbalizado claramente mas sem ênfase extrema
- **Fraca** — mencionado de passagem, latente, inferido

### Frequência (quantitativa, absoluta)
Número absoluto de menções distintas no corpus. Thresholds:

| Frequência | Rótulo | Uso na copy |
|---|---|---|
| ≥30 menções | **Dominante** | Espinha narrativa obrigatória da VSL/sales page |
| 15–29 | **Secundária dominante** | Corpo da VSL, e-mails |
| 6–14 | **Terciária** | Bullets, FAQ, remarketing |
| 2–5 | **Pontual** | Cruzar com outras fontes antes de usar |
| 1 | **Insuficiente** | NÃO entra na persona profunda (a menos que coocorrência forte) |

### Regra de contagem
- **Conta como 1 menção** cada ocorrência em uma fonte distinta (review distinto, comentário distinto, trecho distinto de VSL com timestamp diferente).
- **Não inflar** repetições do mesmo prospect/material (a mesma pessoa repetindo a mesma dor 3x na mesma entrevista = 1).
- Se o corpus for muito pequeno (N<10 materiais), reportar com ressalva no Corpus Analisado (`amostra pequena`).

### MAPA DE REPETIÇÃO
Antes de preencher as seções analíticas, gere o MAPA DE REPETIÇÃO no topo do documento (logo após o bloco Corpus Analisado). Contém os elementos com **≥6 menções** (mínimo Terciária), ordenados por frequência decrescente, com 3 colunas: Elemento | Frequência | Categoria. É o overview que orienta o resto.

---

## Estrutura da Persona Profunda (11 seções)

O template canônico está em [`references/template-persona-profunda.md`](references/template-persona-profunda.md). **Leia esse arquivo INTEGRALMENTE antes de gerar a saída** — ele é a fonte de verdade do formato. Resumo das seções:

| Seção | Foco | Formato | Captura ou síntese? |
|---|---|---|---|
| Persona em 1 parágrafo | Resumo executivo | Prosa | Síntese |
| Corpus Analisado | Decomposição do corpus | Bloco de código | Captura |
| **MAPA DE REPETIÇÃO** | Top N ≥6 menções | Tabela 3 col | Captura |
| **S1 Demográfico** | Idade, renda, símbolos de status, ticket máximo, rotinas | Tabela 3 col (Atributo·Valor·Evidência) | Captura |
| **S2 Problemas** | Problemas estruturais (não sintomas) | Tabela 4 col | Captura |
| **S3 Sintomas** | Manifestação concreta (Corpo/Rotina/Relações/Calendário/Outro) | Tabela 4 col, prefixo obrigatório | Captura |
| **S4.1 Dores** | Dor emocional (o que SENTE) | Tabela 4 col | Captura |
| **S4.2 Desejos** | Desejos com prefixo [M/L/P] (manifesto/latente/proibido) | Tabela 4 col, prefixo obrigatório | Captura |
| **S4.3 Medos** | Medos com prefixo [V/S/V+S] (verbalizado/silenciado) | Tabela 4 col, prefixo obrigatório | Captura |
| **S5 Conversas internas** | Pensamentos verbatim | Tabela 4 col | Captura |
| **S6 Transformação** | Antes/Depois + frase-identidade | **PROSA**, não tabela | Síntese |
| **S7.1 Linguagem (VoC)** | 5 subtabelas: dor, desejo, objeção, jargão, inimigos nomeados | Tabela 4 col cada | Captura |
| **S7.2 Tópicos que prendem atenção** | Assuntos agnósticos de fonte | Tabela 4 col | Captura |
| **S7.3 Interesses no privado** | Consumo silencioso, prefixo [Busca/Canal/Livro/IA/Fórum/Compra-fantasma] | Tabela 4 col, prefixo obrigatório | Captura |
| **S7.4 Padrões de consumo** | Manhã/Comercial/Noite/Madrugada + janelas derivadas | Tabela 4 col + bloco de derivações | Captura |
| **S7.5.a Fact sheet de compra** | Últimas compras, ticket máximo, decisão, garantia | Tabela 3 col | Captura |
| **S7.5.b Gatilhos de compra** | Prefixo [aceito]/[rejeitado] | Tabela 4 col, prefixo obrigatório | Captura |
| **S8.a Vilões** | Prefixo [PRIMÁRIO]/[SECUNDÁRIO] + tipo (pessoa/instituição/crença/categoria) | Tabela 6 col, prefixo obrigatório | Captura |
| **S8.b Narrativa do inimigo** | Auto-culpa, reframe, frase de batalha, era de ouro | Tabela 2 col, **SEM evidência** | **Síntese editorial** |
| **S9.1 Vieses a explorar** | Cialdini/Sugarman aplicados | Tabela 4 col | Captura |
| **S9.2 Gatilhos de rejeição** | O que faz fechar a aba | Tabela 4 col | Captura |
| **S10.a Objeções (7 camadas)** | Preço/Tempo/Mentor/Método/Auto-confiança/Prioridade/Stakeholder | Tabela 4 col, prefixo obrigatório | Captura |
| **S10.b Demolição** | Reframe + prova social por camada | Tabela 3 col, **SEM evidência** | **Síntese editorial** |
| **S10.c Objeção silenciada** | A que ele nunca verbaliza | Tabela 2 col, **SEM evidência** | **Síntese editorial** |
| **S11 Subpersonas** | 8–15 variações com Identificação·Desejo·Medo·Contexto·Diferenças-chave | Tabela 5 col | Síntese (puxa de S4.2/S4.3) |

### Captura vs síntese editorial — distinção crítica

**Tabelas de captura** (a maioria): cada linha exige `[fonte] — [localização] — "[citação literal]"`. Sem fonte, a linha não entra. Linha com fonte fraca/única → marcar como Pontual e usar com cautela.

**Tabelas de síntese editorial** (S8.b, S10.b, S10.c): construção a partir de outras tabelas. **Não levam coluna Evidência**. Ancoram em padrões já capturados nas tabelas anteriores, mas a redação final é trabalho editorial. Não invente — derive.

**Convenção de fonte na coluna Evidência.** Usar a tag que o corpus já traz, pra rastreabilidade: `[YT|VideoID|likes]`, `[Reddit|r/sub|post_id|score]`, `[IG|@perfil|post]`, `[REV|produto|estrelas]`, `[E#1|min 12]`. Localização = linha do arquivo ou timestamp. Fato de mercado vindo do mapa/dossiê da concorrência: `[MERCADO|mapa-concorrentes.md|player]` — nunca apresentado como fala do público.

### Prefixos obrigatórios por seção

Estes prefixos são parte do conteúdo da célula "Elemento" — sem eles a tabela está malformada:

| Seção | Prefixo | Significado |
|---|---|---|
| S3 Sintomas | `[Corpo]` `[Rotina]` `[Relações]` `[Calendário]` `[Outro]` | Domínio onde o sintoma se manifesta |
| S4.2 Desejos | `[M]` `[L]` `[P]` | Manifesto / Latente / Proibido |
| S4.3 Medos | `[V]` `[S]` `[V+S]` | Verbalizado / Silenciado / Ambos |
| S7.3 Interesses privados | `[Busca]` `[Canal]` `[Livro]` `[IA]` `[Fórum]` `[Compra-fantasma]` | Tipo de consumo silencioso |
| S7.5.b Gatilhos | `[aceito]` `[rejeitado]` | Aceito (já comprou na prática) / Rejeitado (fecha a aba) |
| S8.a Vilões | `[PRIMÁRIO]` `[SECUNDÁRIO]` | Vilão central (1) ou de apoio (2–3 máx) |
| S10.a Objeções | `[10.1 Preço]` ... `[10.7 Stakeholder]` | Camada universal (todas as 7 precisam existir, mesmo que com "Insuficiente") |

---

## Segundo documento: Matriz de Benefícios por subpersona

A Persona Profunda é **insumo de pesquisa**. A Matriz é **ponte pra escrita**. Logo após fechar a persona profunda, gere a matriz — par obrigatório, não opcional. Framework canônico em [`references/framework-matriz-beneficios.md`](references/framework-matriz-beneficios.md). **Leia esse arquivo INTEGRALMENTE antes de gerar a matriz.**

### O que a Matriz é

Transforma cada subpersona do S11 em uma tabela operacional: **3-5 desejos filtrados** (do catálogo LF8 + 9 Desejos Secundários) × **4 camadas de benefício** (Funcional → Dimensional → Emocional → Identidade). Cada célula é **matéria-prima descritiva** que a etapa de escrita vai usar.

### Regra inegociável: matriz é DADO, não COPY

A matriz **não sugere copy**. Não escreve headline candidata, não propõe hook, não monta ângulo de ad, não fecha CTA, não desenha estrutura de campanha. Tudo isso é trabalho da etapa de escrita, que consome a matriz como insumo.

**Por que**: se a matriz já entrega frase de venda pronta, ela enviesa quem escreve depois — limita o leque criativo, congela a abordagem e transforma pesquisa em copy disfarçada. O criativo precisa receber **autoconceito, desejo, dor, cena e jargão como descrição de fato**.

**Cortar do output da matriz**:
- "Headline-mãe candidata" / "diagonal forte → headline"
- "Ângulos de ad sugeridos" / "hooks" / "leads"
- "CTA-mãe" / "frase de batalha pronta"
- "Estrutura de campanha sugerida" (tabelas de "Ad lead dor → ...")
- "Briefing-mãe" pra criativo
- Qualquer variante de copy escrita dentro do doc da matriz

**Manter no output da matriz**:
- Matriz por subpersona com 4 colunas (Funcional/Dimensional/Emocional/Identidade) preenchidas como descrição de fato — a coluna Identidade pode estar em 1ª pessoa ("Sou X") porque é o autoconceito do avatar, não copy de anúncio
- Síntese executiva com persona-mãe em 1 linha + LF8 dominantes do nicho + N de subpersonas (dado, não copy)
- Tabela de convergência entre subpersonas (cobertura de LF8 por subpersona)
- Desejos exclusivos por subpersona
- Lacunas a fechar (modo PARCIAL)

### Encadeamento com a persona profunda — contrato de derivação

| Campo da Matriz | Origem na Persona Profunda |
|---|---|
| Identificação da subpersona | S11 coluna 1 (cópia literal) |
| Desejo (input pra filtragem) | S11 coluna 2 + cruzamento com S4.2 (Desejos) |
| Medo (alimenta camada Identidade) | S11 coluna 3 + cruzamento com S4.3 (Medos) |
| Contexto de vida (alimenta Dimensional + Emocional) | S11 coluna 4 |
| Cenas concretas (camada Dimensional) | Verbatims de S5 (Conversas internas), S7.4 (Padrões de consumo), S3 (Sintomas) |
| Linguagem das células | VoC da S7.1 — usar jargão real do mercado, não tradução genérica |
| Identidade derivada | Cruzamento da identidade-âncora da S1 + medos identitários da S4.3 |

Se um campo da matriz não tiver origem clara na persona profunda, **volte à persona profunda** — provavelmente é subpersona incompleta ou desejo mal filtrado.

### O catálogo de desejos (LF8 + Secundários)

**8 Desejos Biológicos (LF8) — inatos, força máxima:**
1. Sobrevivência / aproveitar a vida / longevidade
2. Alimentos e bebidas
3. Liberdade do medo, dor e perigo
4. Companheirismo sexual
5. Condições de vida confortáveis
6. Superioridade / vencer / estar à frente
7. Proteção de entes queridos
8. Aprovação social

**9 Desejos Secundários — aprendidos, força moderada:**
1. Informação / curiosidade · 2. Limpeza · 3. Eficiência · 4. Conveniência · 5. Qualidade/confiabilidade · 6. Beleza/estilo · 7. Economia · 8. Lucro · 9. Barganhas

**Regra de hierarquia:** quando dois desejos competem, o biológico vence. O LF8 carrega o peso da promessa; os secundários sustentam credibilidade e justificam a compra racionalmente.

### Estrutura do documento Matriz de Benefícios

```
# Matriz de Benefícios — [Oferta/Nicho]
**Derivado de**: persona-profunda-<nicho>-v1.md (S11, S4.2, S4.3, S7.1, S1)
**Modo**: COMPLETO | PARCIAL (espelha a persona profunda)

## Síntese executiva
- Persona-mãe em 1 linha (descrição factual, puxa da persona profunda)
- N de subpersonas mapeadas
- LF8 dominantes do nicho como um todo (intersecção das matrizes — é dado de cobertura)

## Subpersona 1 — [Nome fictício, idade, 2-3 marcadores]
**Identificação**: [literal de S11]
**Deseja**: [literal de S11, com cross-ref pra S4.2]
**Teme**: [literal de S11, com cross-ref pra S4.3]
**Contexto**: [literal de S11]

### Desejos filtrados (3-5)
- LF8 #X — [nome] — por que essa subpersona ativa (1 frase descritiva, ancorada em verbatim da persona profunda)
- LF8 #Y — [nome] — ...
- Secundário — [nome] — ...

### Matriz
| Desejo | Funcional (o que o produto faz) | Dimensional (cena observável no mundo) | Emocional (sentimento situacional) | Identidade (autoconceito em 1ª pessoa) |
|---|---|---|---|---|
| LF8 #X | descrição factual da ação do produto | descrição da cena | descrição do sentimento | "Sou ..." (autoconceito do avatar) |
| LF8 #Y | ... | ... | ... | "Sou ..." |

---

## Subpersona 2 — [...]
[repete a estrutura para cada subpersona do S11]

---

## Convergências entre subpersonas (dado estruturado)
| LF8 / Desejo | Sub1 | Sub2 | Sub3 | ... | Cobertura |
|---|:---:|:---:|:---:|:---:|:---:|
| LF8 #X | ✅ DOM | ✅ | — | ✅ | N/total |

- LF8 que aparecem em ≥50% das subpersonas → desejos compartilhados do nicho
- LF8 que aparecem em 1-2 subpersonas → desejos exclusivos por subpersona

## Lacunas a fechar (apenas em modo PARCIAL)
- [O que precisa entrar na persona profunda pra fortalecer a matriz: ex: "S7.4 padrões de consumo de subpersona 3 está com Insuficiente — capturar entrevistas com perfil X"]
```

### Regras de execução da Matriz

1. **Uma matriz por subpersona do S11.** Se a persona profunda tem 8 subpersonas, a matriz tem 8 seções. Não compactar.
2. **Filtrar 3-5 desejos por subpersona.** Nunca menos de 3 (matriz rasa), nunca mais de 5 (perde foco). A filtragem cruza os 17 desejos do catálogo com S4.2 + S4.3 + contexto da S11.
3. **Cada célula é descrição de fato, não copy.** "Mais energia" é vago; "Termina o 3º round com gás" é específico (e segue sendo descrição, não headline). Ancorar a célula numa cena já presente na persona profunda (S3, S5, S7.4).
4. **A coluna Identidade usa primeira pessoa**, frase curta declarativa: `"Sou ..."` / `"Não sou mais ..."` — autoconceito do avatar (dado), não headline.
5. **Linguagem das células = VoC do mercado**, não tradução genérica. Reler S7.1 antes de cada matriz — usar pra **descrever**, não pra **vender**.
6. **Não duplicar entre matrizes.** Se duas ficarem idênticas, a clusterização do S11 está errada ou uma das subpersonas não justifica existência separada — voltar à persona profunda.
7. **Zero copy no doc.** Reler antes de entregar e cortar qualquer frase que pareça headline, hook, lead, CTA, slogan, ângulo de ad ou estrutura de campanha.

A Matriz é **derivação descritiva** — não carrega coluna Evidência por linha. A âncora vem do encadeamento declarado no header. A regra equivalente: cada célula precisa ser **rastreável** a um elemento da persona profunda ("essa célula veio de S?"). Se for invenção, sai. Se for copy disfarçada, também sai.

---

## Terceiro documento: Banco de Verbatims por Ângulo

A persona profunda guarda a fala literal dentro da coluna Evidência, espalhada por 11 seções; a matriz aponta só os códigos (`S4.2 [M]`, `LF8 #3`). Na hora de escrever batendo num ângulo específico, quem escreve teria que caçar a fala nas duas pontas. O banco vira o índice ao contrário: **organiza tudo por ângulo**, e debaixo de cada ângulo lista as falas literais que o sustentam — primeiro o que a persona profunda já condensou, depois **encorpando com o corpus cru** (que sempre tem mais fala por ângulo do que a persona profunda coube registrar). **Não é copy** — é munição indexada.

Molde exato (famílias, ordem, linha-meta de cada ângulo, blocos F e I): [`references/template-banco-verbatim.md`](references/template-banco-verbatim.md). **Ler antes de escrever.** As 9 famílias:

| Família | Vem de | Conteúdo |
|---|---|---|
| **A. Dores** | S2 + S4.1 | problemas estruturais e dor emocional |
| **B. Medos** | S4.3 + S10.5 + S10.c | medos verbalizados e silenciados (incl. objeção silenciada) |
| **C. Desejos** | S4.2 | manifestos / latentes / proibidos |
| **D. Objeções** | S10.a | as 7 camadas universais, forma literal |
| **E. Inimigos** | S8 | vilão primário + secundários + frase de batalha |
| **F. Identidade/Transformação** | S6 + S11 + col. Identidade da matriz | frase ANTES, DEPOIS, autoconceitos e falas que ancoram cada subpersona |
| **G. Jargão** | S7.1.4 | termos que provam pertencimento |
| **H. Gatilhos** | S7.5.b + S9 | o que faz comprar / o que faz fechar a aba |
| **I. Ponte LF8 → ângulos** | convergências da matriz | tabela-atalho da matriz pro banco |

**Anatomia de um bloco de ângulo** (replicar exatamente):

```
## A1 — "Não sei o caminho das pedras" (sei construir, não sei montar o negócio)
**Forte · 155 menções · S2, S4.1, S4.2, S5 · LF8 #6 Superioridade · Edson, Vânia, Marcelo**
*Linha de descrição opcional — o que é esse ângulo em 1 frase.*

- "fala literal do cliente, exatamente como ele escreveu" `[YT|8vskIQnTfxU|6]`
- "outra fala literal" `[YT|qyLm93QKMDA|2]`
```

A linha-meta em negrito segue sempre a ordem: **Intensidade · Frequência · Seções da persona profunda · LF8/Subpersonas**.

### Como montar o banco

1. **Reler a persona profunda**: o Mapa de Repetição é a **espinha** (temas dominantes viram os títulos dos ângulos); de cada seção, Intensidade, Frequência e falas da coluna Evidência; subpersonas (S11) e frases-identidade (S6).
2. **Reler a matriz**: desejos LF8 por subpersona, tabela de convergências e coluna Identidade (autoconceito em 1ª pessoa).
3. **Definir os ângulos e agrupar nas 9 famílias.** Cada ângulo recebe código (A1, B2, C4…) e **título na voz do cliente** (ex.: "E se eu construir e não vender?"). Os dominantes do Mapa de Repetição são obrigatórios; sem lastro no corpus, sem ângulo. Dentro de cada família, ordem por frequência decrescente.
4. **Encorpar com o corpus cru — minerar por palavra-chave.** Este passo é obrigatório; sem ele o banco vira só um recorte da persona profunda. **Não carregue o corpus inteiro no contexto** — faça `grep` por ângulo:

   ```bash
   # limites de cada fonte primeiro (pra atribuir cada fala à origem certa)
   grep -nE "^### \[" <pasta-do-bloco-1>/01-corpus-bruto.md

   # depois minere ângulo a ângulo
   grep -inE "não vender|liquidez|encalh|parado na mão" <pasta-do-bloco-1>/01-corpus-bruto.md | head -15
   ```

   Para cada ângulo, escolher **3–6 falas literais**, priorizando as de maior peso (likes/upvotes/recorrência) e as que mais soam como o cliente. Misturar a fala que a persona profunda já tinha com as novas do corpus.
5. **Atribuir a fonte de cada fala** com a mesma convenção do corpus e da persona profunda (`[YT|VideoID|likes]`, `[Reddit|sub|upvotes]`, `[REV|produto|estrelas]`, `[E#|id]`…). Peso quando existir; `|—|` quando a fonte não isolar.
6. **Montar a Seção I — Ponte LF8 → ângulos** a partir da tabela de convergências da matriz: pra cada desejo LF8 (e cobertura X/N subpersonas), quais ângulos do banco carregam o verbatim.
7. **Índice navegável + cabeçalho + rodapé**: índice por família no topo; cabeçalho com derivação, "pra que serve", "como ler" e **legenda das fontes** (ID curto → nome legível); rodapé com versão e ressalvas do corpus (ex.: monocanal, sem entrevista 1:1).

Se, por algum motivo, a matriz não existir (ex.: rodada anterior só gerou a persona profunda), dá pra montar com corpus + persona profunda — a Seção I e os autoconceitos (F3) ficam reduzidos; registrar nas lacunas.

---

## Fluxo de execução

1. **Inventário do corpus.** Rodar o script de inventário (ver "Scripts") no `01-corpus-bruto.md`. Atribuir IDs estáveis a cada material (tag do bloco; E#1, E#2 para entrevistas; review #1, #2...; nome de arquivo para material solto). Decidir COMPLETO/PARCIAL. Avisar se algo precisa de transcrição.

2. **Leitura ativa, material por material.** O corpus da pesquisa costuma ter 1500–3000 linhas: ler em lotes (por bloco `### [` ou por faixas de linha), nunca tudo de uma vez. Para cada lote, extrair cruamente para `notas-brutas.md` (na pasta de saída): cada elemento com **citação literal + ID do material + localização** (linha, timestamp, parágrafo) e a categoria provisória (dor, sintoma, desejo, medo, etc). Salvar o progresso a cada lote.

3. **Clusterização.** Agrupar elementos similares (ex: "não tenho tempo", "vivo correndo", "acordo cansado" → cluster "esgotamento por falta de tempo"). Cada cluster mantém TODOS os verbatims e fontes originais — clusterizar é agrupar, não compactar.

4. **Quantificação por cluster.** Contar menções em fontes distintas (use `contar_mencoes.py` quando o corpus tiver ≥10 materiais, e revise os matches), atribuir Frequência (Dominante/Secundária/Terciária/Pontual/Insuficiente) e Intensidade (Forte/Média/Fraca). Descartar clusters com Frequência = Insuficiente (1 menção) a menos que tenham coocorrência forte com outro cluster relevante.

5. **MAPA DE REPETIÇÃO.** Gerar a tabela top N (≥6 menções) ordenada por frequência decrescente. Classificar cada linha por categoria.

6. **Preenchimento seção por seção.** Seguir a ordem do template. Para cada seção:
   - Aplicar o prefixo obrigatório (quando houver)
   - Garantir evidência inline em cada linha de tabela de captura
   - Para S6 (Transformação): prosa curta antes/depois com frase-identidade fechando cada bloco
   - Para tabelas de síntese editorial (S8.b, S10.b, S10.c): derivar das tabelas de captura, sem inventar
   - Usar o mapa/dossiê da concorrência pra tickets e promessas do mercado (S7.5), vilões de categoria (S8) e desconfiança de mentor/método (S10.3/10.4) — sempre marcados como fato de mercado

7. **Persona em 1 parágrafo.** Escrever por último — é o resumo executivo que destila a persona-mãe.

8. **Sanity check da persona profunda.** Antes de seguir pra Matriz:
   - [ ] Toda linha de tabela de captura tem fonte + localização + citação literal?
   - [ ] Todos os prefixos obrigatórios estão aplicados?
   - [ ] S6 está em prosa, não em tabela?
   - [ ] S8.b, S10.b, S10.c estão SEM coluna Evidência?
   - [ ] S10.a tem TODAS as 7 camadas (mesmo que algumas com Insuficiente)?
   - [ ] S11 tem entre 8 e 15 subpersonas (ou 3-5 em modo PARCIAL com corpus pequeno) com a coluna "Diferenças-chave vs persona-mãe" preenchida?
   - [ ] MAPA DE REPETIÇÃO filtra por ≥6 menções?
   - [ ] Persona em 1 parágrafo cobre nome+idade+ocupação+contexto+renda+dor central+tentativas+reserva+ticket+janela de compra?
   - [ ] Nenhuma fala atribuída ao público veio da `02-pesquisa-lapidada.md` ou de copy de concorrente?
   - [ ] Modo PARCIAL: header marcado e bloco "Lacunas a fechar" no final?

9. **Gerar a Matriz de Benefícios.** Reler [`references/framework-matriz-beneficios.md`](references/framework-matriz-beneficios.md) e S11 + S4.2 + S4.3 + S7.1 + S1 da persona profunda recém-gerada. Para cada subpersona do S11:
   - Copiar Identificação, Deseja, Teme, Contexto (literal do S11)
   - Cruzar "Deseja" + "Teme" + contexto com o catálogo LF8 + 9 Secundários
   - Filtrar 3-5 desejos pungentes
   - Preencher a matriz: cada desejo vira uma linha; 4 colunas (Funcional → Dimensional → Emocional → Identidade) — cada célula é **descrição factual**, não copy
   - Ancorar cada célula numa cena/jargão/verbatim da persona profunda (S3, S5, S7.1, S7.4)
   - **NÃO** derivar headline-mãe, ângulos de ad, hook, CTA, briefing ou estrutura de campanha

   Fechar com "Convergências entre subpersonas" (tabela de cobertura). LF8 em ≥50% das subpersonas = desejos compartilhados do nicho; LF8 únicos = desejos exclusivos por subpersona.

10. **Sanity check da Matriz.**
    - [ ] Exatamente UMA matriz por subpersona do S11?
    - [ ] Cada matriz tem entre 3 e 5 desejos filtrados?
    - [ ] Cada matriz tem as 4 colunas (Funcional, Dimensional, Emocional, Identidade)?
    - [ ] Células concretas **e descritivas, não publicitárias**?
    - [ ] Coluna Identidade em primeira pessoa, frase curta declarativa?
    - [ ] Linguagem espelha a S7.1 da persona profunda, usada pra descrever?
    - [ ] Cada célula rastreável a um elemento da persona profunda?
    - [ ] Header declara `Derivado de: persona-profunda-<nicho>-v1.md`?
    - [ ] Tem "Convergências entre subpersonas" como tabela de cobertura?
    - [ ] **ZERO** headline, hook, lead, CTA, ângulo de ad, briefing-mãe ou estrutura de campanha?

11. **Gerar o Banco de Verbatims** (ver "Terceiro documento").

12. **Sanity check do Banco.**
    - [ ] Toda fala é literal (typos e tudo; cortes só com `[...]`) e tem tag de fonte?
    - [ ] Os ângulos dominantes do Mapa de Repetição estão todos lá?
    - [ ] Cada ângulo tem 3–6 falas e ao menos uma veio do corpus cru (não só da persona profunda)?
    - [ ] As 7 camadas de objeção (D1–D7) existem, mesmo com fala escassa?
    - [ ] A objeção silenciada está marcada como inferência, não verbatim?
    - [ ] Seção I (Ponte LF8 → ângulos) montada a partir das convergências da matriz?
    - [ ] Nenhuma headline, hook ou CTA? (Só as sínteses que a persona profunda já traz — frase de batalha S8, argumento pro stakeholder S10.7, frases-identidade S6 — marcadas como tal.)

13. **Releitura cética.** Reler os três documentos como um copywriter desconfiado perguntando "essa linha tem fonte real?". Se não souber responder com a referência na mão, voltar e corrigir.

14. **Entrega.** Modo briefing: devolver o resumo no formato do modo briefing. Modo direto: ver "Entrega ao aluno".

---

## Entrega ao aluno (modo direto)

Os arquivos têm os códigos e o rigor; o chat, não. Apresente assim, curto, sem nenhum código (S1, LF8, [M], etc.):

1. **Quem é o seu cliente** — 2–3 frases em português de gente, puxadas do "Persona em 1 parágrafo" (nome fictício, idade, momento de vida, o que trava ele).
2. **As 3 dores mais fortes** — cada uma com a frase exata que o público usa e quantas pessoas falaram disso ("apareceu em 42 comentários").
3. **As 3 desculpas pra não comprar** — em palavras simples ("acha caro", "não tem tempo", "já foi enganado antes"), com a frase real de cada uma.
4. **Os tipos de cliente** — um por linha: nome fictício + o que diferencia ele dos outros.
5. **O que ainda falta descobrir** (se for retrato inicial) — em no máximo 3 itens, dizendo que tipo de pesquisa resolveria ("rodar a pesquisa de mercado de novo incluindo fóruns onde se fala de preço de curso").
6. **Onde ficaram os arquivos** — os três caminhos, com uma linha de "pra que serve" cada:
   - retrato completo do cliente → base de tudo que você escrever
   - matriz de benefícios → o que cada tipo de cliente ganha, do prático até "quem ele passa a ser"
   - banco de frases → quando for escrever sobre um assunto (uma dor, uma desculpa), abra aqui e use as palavras dele

Feche dizendo o próximo passo: o tom de voz do especialista (bloco 3 do Alicerce do Copy) — ou, se ele rodou pela `/alicerce-copy`, que a sequência continua sozinha.

---

## O que NUNCA fazer

- **Nunca inventar** uma dor, desejo, medo, verbatim, ticket, símbolo de status. Sem evidência no corpus → `⚠ sem evidência suficiente — pesquisar mais`.
- **Nunca montar persona sem pesquisa.** Sem o corpus do bloco 1, a skill para.
- **Nunca parafrasear** uma citação "melhorando" o português. Verbatim é literal — preserva gírias, erros de digitação, vícios, palavrões.
- **Nunca misturar** problema (S2 estrutural) com sintoma (S3 manifestação) com dor (S4.1 emocional). Na dúvida, registrar nas duas seções com nota cruzada.
- **Nunca prosseguir** uma linha de captura sem citar fonte.
- **Nunca colocar evidência em S8.b, S10.b, S10.c.** São síntese editorial.
- **Nunca pular** uma das 7 camadas universais de objeção em S10.a. Sem evidência → Insuficiente, mas a camada existe.
- **Nunca clusterizar agressivamente** a ponto de perder verbatims — manter 2–3 por cluster.
- **Nunca tratar** a `02-pesquisa-lapidada.md` ou a copy de concorrente como fala do público.
- **Nunca usar** os documentos como narrativa de venda. São diagnóstico, não persuasão.
- **Nunca sobrescrever** uma versão anterior — gerar `-v2`.
- **Nunca usar jargão no chat** com o aluno (ver "Nomes que o aluno vê").

## Quando perguntar (só no modo direto)

Pergunte APENAS quando destrava, uma vez, com opções claras:
- Pesquisa encontrada em mais de um projeto → qual projeto
- Conflito alto entre fontes (metade diz X, metade o oposto) → qual segmento priorizar

Campo crítico sem evidência (renda, ticket máximo, o "depois" da S6) não vira pergunta: vira lacuna, nos dois modos. No modo briefing, nem as perguntas acima: tudo vira lacuna.

## Boas práticas

- **Lotes pequenos** em corpus grande: processar por bloco/faixa de linhas, salvar em `notas-brutas.md`, consolidar ao final.
- **Verbatims poderosos**: marcar com `★` os que parecem ouro de hook/headline.
- **Identidade-âncora** (autodescrição recorrente): tratar como dado da S1 OU como linha de S7.1, conforme seja factual ou retórica.
- **Coocorrência**: se uma dor sempre aparece junto com uma emoção, registrar na linha (`coocorre com: vergonha + identidade "pai falhando"`).
- **Campo sem evidência** → marcar `⚠ sem evidência suficiente` em vez de pular — é o sinal pro próximo ciclo de pesquisa.

---

## Scripts auxiliares

Dois scripts em `scripts/` (só Python padrão, sem instalar nada). **Use por padrão** quando o corpus tiver ≥10 materiais. Rodar da raiz do projeto. Os dois leem tanto o `01-corpus-bruto.md` (arquivo único com blocos `### [TAG | ...]`) quanto pastas de material solto — e aceitam vários caminhos de uma vez.

### `inventariar_corpus.py`
Gera o bloco "Corpus Analisado" pronto pra colar na persona profunda, com materiais por tipo e número de falas distintas (base da decisão COMPLETO/PARCIAL).

```bash
python3 .claude/skills/persona-profunda/scripts/inventariar_corpus.py \
  "<pasta-do-bloco-1>/01-corpus-bruto.md" --data AAAA-MM-DD
```

Material solto é classificado pelo prefixo do nome (`vsl_`, `yt_`, `reddit_`, `ig_`, `e1_`/`entrevista_`, `review_`/`depoimento_`, `ad_`/`anuncio_`, `survey_`/`form_`, `comentario_`/`dm_`, `call_`/`venda_`); o que não casar aparece como "Outros — RECLASSIFICAR".

### `contar_mencoes.py`
Recebe o corpus + um JSON de termos com sinônimos e conta **fontes distintas** onde cada cluster aparece (1 fonte = 1 menção), já classificando pelos thresholds e apontando arquivo:linha de cada ocorrência pra revisão.

```bash
python3 .claude/skills/persona-profunda/scripts/contar_mencoes.py \
  "<pasta-do-bloco-1>/01-corpus-bruto.md" --termos <pasta de saída>/termos.json
```

`--unidade auto` (padrão): no corpus com blocos, cada fala (linha) = 1 fonte; arquivo solto (entrevista, call) = 1 fonte. `--unidade fala` para exports em que cada linha é uma pessoa (formulário, lista de comentários). `--unidade bloco` para contar por vídeo/thread.

Formato de `termos.json` (salvar como arquivo de trabalho na pasta de saída):
```json
{
  "esgotamento por falta de tempo": ["sem tempo", "vivo correndo", "acordo cansado", "exausto"],
  "vergonha de pedir ajuda": ["tenho vergonha", "não consigo pedir", "constrangido"]
}
```

**Limitações:** os scripts contam texto. Ironia, negação e sentido figurado passam batido — **sempre revisar as linhas apontadas** antes de usar o número como Frequência final. Os blocos de concorrente/dados entram na contagem se casarem; descarte-os ao consolidar (não são fala do público). O script é assistente, não juiz.

---

## Referências

- [`references/template-persona-profunda.md`](references/template-persona-profunda.md) — Template da Persona Profunda (FONTE DE VERDADE do 1º documento). **Ler integralmente antes de gerar qualquer persona profunda.**
- [`references/framework-matriz-beneficios.md`](references/framework-matriz-beneficios.md) — Framework da Matriz de Benefícios (FONTE DE VERDADE do 2º documento): 5 camadas + LF8 + 9 Secundários + workflow em 3 passos + exemplo aplicado. **Ler integralmente antes de gerar qualquer matriz.**
- [`references/template-banco-verbatim.md`](references/template-banco-verbatim.md) — Molde do Banco de Verbatims por Ângulo (FONTE DE VERDADE do 3º documento). **Ler antes de montar o banco.**

---

**Filosofia:** copy boa não nasce da criatividade de quem escreve — nasce do reconhecimento de padrões na linguagem do mercado. A persona profunda torna esse reconhecimento auditável; a matriz transforma os padrões em benefícios por tipo de cliente; o banco devolve as palavras reais do público na hora de escrever. Frequência substitui opinião. Verbatim substitui paráfrase. Evidência substitui achismo.
