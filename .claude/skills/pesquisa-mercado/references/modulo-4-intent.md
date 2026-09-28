# Módulo 4 — Intent search (o público buscando solução)

**Tempo típico:** 15 min
**Ferramentas:** WebSearch + `scripts/pesquisa.py yt-intent` (yt-dlp)
**Output:** SEÇÃO 4 do `01` (resultados crus) + Apêndice C do `02`

## Princípio

Os módulos 1-3 olham o nicho **de fora pra dentro** (pesquisador analisando). Este olha **de dentro pra fora**: com as palavras que o **público digitaria** quando procura solução.

Isso revela:
- **O que o público ENCONTRA quando busca** (= concorrência real de atenção)
- **O vocabulário que ele absorve** como linguagem do nicho
- **Gaps de produto** confirmados pela SERP (= mar azul real)
- **Quem domina a primeira página** (= quem leva a venda hoje)

## Construindo as buscas do público

Personificar **6 estados emocionais**. Os estados são universais; a forma muda por nicho:

| Estado emocional | Tipo de busca | Exemplo nicho físico (jiu-jitsu) | Exemplo nicho B2B (clínica veterinária) |
|---|---|---|---|
| Dor principal / sintoma | "como evitar/resolver X" | "como evitar lesão de joelho no jiu jitsu" | "clínica veterinária dando prejuízo o que fazer" |
| Objeção à solução óbvia | "X atrapalha Y?" | "musculação atrapalha o jiu jitsu deixa travado" | "vale a pena contratar gestor pra clínica pequena" |
| Praticidade / restrição | "X em casa / sem Y / com pouco Z" | "preparação física pra jiu jitsu em casa sem academia" | "como divulgar clínica veterinária sem gastar muito" |
| Recomeço / transição | "voltar/começar depois de Z" | "voltar pro jiu jitsu depois dos 40 anos" | "abrir clínica veterinária depois dos 40 vale a pena" |
| Resultado / performance | "como conseguir mais X" | "como aguentar mais rounds no jiu jitsu fôlego" | "como aumentar faturamento da clínica veterinária" |
| Identidade / estágio de vida | busca com idade/papel declarado | "treino pra durar mais no jiu jitsu master" | "veterinário recém-formado abrir clínica própria" |

Características das buscas do público:
- Linguagem coloquial, não técnica
- Palavras emocionais ("destravar", "se quebrar", "atrapalhar")
- Pode ter erro de grafia/acento, como o público real
- Perguntas, não comandos

## Comandos

### 6 buscas no Google (WebSearch, em paralelo, numa mensagem só)

Uma por estado emocional.

### 6 buscas no YouTube (em paralelo)

```bash
python3 .claude/skills/pesquisa-mercado/scripts/pesquisa.py yt-intent --out "<W>/avatar_search" \
  --q "<busca 1>" --q "<busca 2>" --q "<busca 3>" --q "<busca 4>" --q "<busca 5>" --q "<busca 6>"
```

Imprime, por busca, os 8 vídeos mais vistos entre os 15 primeiros resultados: `[views v] canal — título`.
(Aqui é `ytsearch` de relevância de propósito: queremos o que o YouTube **mostra** pra quem digita isso, não o mais visto do ano.)

**Modo degradado:** trocar pelo WebSearch `site:youtube.com <busca>` e anotar título/canal/views que aparecerem nos snippets.

## Análise

Pra cada busca, anotar:
1. **Top 5 resultados** (quem aparece, que tipo de conteúdo)
2. **Tipo de fonte dominante** (blog de loja, mídia, criador independente, fórum…)
3. **Quem vende produto** vs quem só publica conteúdo
4. **Views dos vídeos com TÍTULO PERFEITO** (se baixas = gap de distribuição)

## O que gerar no Apêndice C do `02`

```markdown
# APÊNDICE C — Intent search (Google + YouTube com a lente do público)

## C.1 — As buscas do público (tabela: estado emocional | busca)
## C.2 — O QUE O PÚBLICO ENCONTRA (tipo de conteúdo dominante + "quem domina por busca")
## C.3 — Achado estratégico #1: produto já ocupado? (mar azul confirmado ou refutado)
## C.4 — Concorrente de referência do nicho (a partir dos top resultados) → vira insumo do Módulo 5
## C.5 — Linguagem da SERP que o público absorve (termo | origem | uso na copy)
## C.6 — Gap visual no YouTube (título perfeito vs views baixas)
## C.7 — Padrões NOVOS desta rodada
## C.8 — Implicações pra estratégia do produto (5-7 conclusões)
## C.9 — Onde a SERP REFUTA hipóteses anteriores
## C.10 — Fontes consultadas
```

## O insight mais valioso deste módulo

Vídeo com **TÍTULO PERFEITO PRO PÚBLICO + views ridículas** (443, 845, 5,6 mil) é sinal de **gap de distribuição**, não de tema sem interesse. Quem chegar bem estruturado, com tráfego pago e produto sólido, **ocupa esse vácuo**. Sinal número 1 de mar azul. Anotar sempre.

## Anti-padrões

- ❌ Escrever as buscas como pesquisador (formal, técnica)
- ❌ Só Google, sem YouTube (perde metade do que o público vê)
- ❌ Não verificar se um concorrente domina a primeira página
- ❌ Não notar o gap quando aparece (vídeo bom + views baixas)
