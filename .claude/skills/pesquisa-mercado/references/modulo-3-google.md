# Módulo 3 — Google (tamanho de mercado + ciência + autoridades)

**Tempo típico:** 10 min
**Ferramentas:** WebSearch + WebFetch (ferramentas do Claude, não precisam instalação — funciona igual em qualquer modo)
**Output:** SEÇÃO 4 do `01` + Apêndice B do `02`

## Princípio

Google traz a camada "institucional" que YouTube e Reddit não cobrem: tamanho de mercado (TAM), estudos revisados por pares, entrevistas com autoridades nomeadas, instituições oficiais, dados macroeconômicos.

Essa camada vira **munição de autoridade na copy**: números, quotes, estudos com fonte.

## 8 buscas em paralelo (template)

Rodar as 8 em UMA mensagem (paralelas).

**Os 8 vetores são FRAMES, não buscas fixas — traduzir cada um pro nicho antes de buscar.** Guia:

| Categoria do nicho | Como os vetores se traduzem |
|---|---|
| **Físico/esportivo/saúde** | epidemiologia de lesões, ciência do treino, volta pós-lesão, preparação física |
| **Profissional/B2B** (clínica, agência, SaaS) | dados setoriais (SEBRAE, conselhos, associações), margem/salário médio, mortalidade de negócios, gestão |
| **Hobby/aprendizado** (piano, idioma, desenho) | ciência do aprendizado, taxa de desistência, neurociência da prática, aprendizado adulto |
| **Ofício/carreira** (barbearia, confeitaria, programação) | mercado de trabalho, renda média, formalização, demanda regional |

### 3.1 — TAM / crescimento de mercado
```
estatísticas <nicho> brasil <ano atual> mercado crescimento <unidade do nicho>
```
Procurar: total de praticantes/consumidores, crescimento %, fontes oficiais (ministério, sindicato, associação).

### 3.2 — Problemas mais comuns do nicho (com dado)
```
<problema do nicho> mais comuns estudo <epidemiologia|pesquisa setorial> <categoria>
```
Procurar: revisões sistemáticas / artigos revisados (nicho físico/saúde) OU pesquisas setoriais e censos (nicho profissional), com % de prevalência.

### 3.3 — Ciência da prática / método validado
```
<nicho> ciência <metodologia específica> estudo
```
Procurar: TCCs/dissertações em repositórios universitários, revistas indexadas, SciELO.

### 3.4 — Subgrupos institucionais (categorias oficiais)
```
<nicho> <categoria etária ou demográfica> oficial
```
Procurar: federações, reguladores, categorias oficiais (= linguagem tribal do público).

### 3.5 — Recomeço / transição
```
"voltar" OR "recomeçar" OR "mudar de carreira" <nicho> depois <pausa|lesão|idade|demissão>
```
O frame é **o público em momento de virada**: volta após lesão (esporte), retomar depois de anos (hobby), transição de carreira (ofício), virada no negócio (B2B).

### 3.6 — Autoridades nomeadas
```
<figura top 1> <figura top 2> entrevista <tema> quote
```
Procurar: entrevistas em portais do nicho, quotes diretas em redes sociais. Ouro se vier de podcast transcrito.

### 3.7 — Benefício adjacente (vetor extra de venda)
```
<nicho> <benefício adjacente> benefícios estudo
```
Varia: saúde mental (esporte, hobby), renda extra/independência (ofício), tempo livre/família (negócio), status (carreira). Frequentemente vira o melhor diferencial de copy.

### 3.8 — Metodologia de referência / benchmark internacional
```
<nicho> <metodologia de referência> ciência método
```
Ex.: periodização (esporte), prática deliberada (aprendizado), framework de gestão (B2B), certificação internacional (ofício).

## Quando aprofundar com WebFetch

WebSearch traz snippet + URL. Abrir WebFetch quando:
- O snippet cita estudo importante sem o % específico
- A quote de autoridade vem parcial
- É site oficial de instituição relevante (quer os dados crus)
- É reportagem rica que merece extração estruturada

## Como registrar no `01` (SEÇÃO 4)

Cru, por vetor: dado/quote **literal** + URL completa. Tag `[Web | domínio | título | URL]`. Sem interpretação.

## O que gerar no Apêndice B do `02`

```markdown
# APÊNDICE B — Google (macro + ciência)

## B.1 — Tamanho de mercado (tabela: métrica | valor | fonte) + implicação
## B.2 — Problemas com base em dado (prevalência com fonte)
## B.3 — Categorias institucionais (vocabulário oficial + por que importa pra copy)
## B.4 — Ciência da prática (validado vs não validado; lacuna entre achismo e elite)
## B.5 — Quotes de figuras-âncora (literais)
## B.6 — Benefício adjacente (base pra usar com legitimidade na copy)
## B.7 — Recomeço / transição
## B.8 — Estatísticas-âncora prontas pra página de vendas (6-8 números/quotes)
## B.9 — Big idea v2 (refinada com macro)
## B.10 — Fontes consultadas (links markdown)
```

## Critério de qualidade

- 3+ fontes com dado verificável: estudos revisados (PMC, SciELO, periódicos) quando o nicho tem camada científica; senão, pesquisas setoriais (SEBRAE, IBGE, conselhos, associações)
- 1+ número macro de mercado
- 2+ quotes diretas de autoridade nomeada
- 1+ estatística "boa pra página de vendas" (que vire headline)

Se vier menos, refazer com ângulos diferentes. Se mesmo assim faltar, registrar nas lacunas.

## Anti-padrões

- ❌ 1 busca genérica gigante "<nicho> tudo"
- ❌ Aceitar dado sem fonte ("acredita-se que…")
- ❌ Não checar a data dos estudos
- ❌ Ignorar o benefício adjacente (3.7)
- ❌ Copiar as buscas do exemplo sem traduzir pro nicho (buscar "epidemiologia de lesão" pra curso de piano)
