# Metodologia de Extração de Tom de Voz

> Pipeline para transformar transcrições brutas de um especialista em um documento padronizado de Tom de Voz (ver `template-tom-de-voz.md`).
>
> Esta metodologia é **descritiva, não inventiva**: o objetivo é deixar a voz do especialista emergir da evidência, não impor um molde. Sempre que um copywriter consagrado já tem framework para a camada, usamos o framework dele com crédito. Onde não tem, descrevemos o heurístico explicitamente.
>
> **Princípio fundador:** se não tem evidência (citação direta), não entra no documento. Tudo o que sobra vai para `Backlog` e espera mais coleta. Nada inventado, nunca.

---

## 0. Pré-requisitos de Volume

> **Por quê:** abaixo de um piso mínimo, padrões aparentes são ruído amostral. Acima dele, a redundância natural da fala revela estrutura.

| Tipo de extração | Mínimo aceitável | Recomendado | Por quê |
|---|---|---|---|
| Demonstração / Piloto | 10 min OU ~1.500 palavras | — | Mostra o método funcionando, mas insuficiente para produção de copy |
| Rascunho operacional (v0.1) | 45 min OU ~7.000 palavras | 60 min / ~9.000 palavras | Já permite gerar copy de testes A/B |
| Documento calibrado (v1.0) | 3h OU ~25.000 palavras | 5h em ≥3 contextos distintos | Mínimo para sustentar lançamento ou VSL |
| Documento validado (v2.0+) | 8h+ em ≥4 contextos | + 1 entrevista direta | Padrão ouro |

**Diversidade de contexto importa mais que volume total.** 3h de uma única aula didática vale menos que 1h dividida em (1) aula técnica, (2) entrevista informal, (3) live respondendo objeções. Cada contexto revela uma camada da voz.

---

## 1. Fases do Pipeline

```
Fase 1 — Ingestão & Limpeza
     ↓
Fase 2 — Codificação Léxica          [@gary-halbert lidera]
     ↓
Fase 3 — Análise Sintática           [@gary-bencivenga + @bill-bernbach lideram]
     ↓
Fase 4 — Mapa de Crenças & Inimigos  [@eugene-schwartz + @todd-brown lideram]
     ↓
Fase 5 — Provas e Histórias          [@claude-hopkins lidera]
     ↓
Fase 6 — Síntese (preenchimento do template)  [a skill preenche]
     ↓
Fase 7 — Validação (Teste do Cego + Inverso)  [@claude-hopkins audita]
     ↓
Fase 8 — Aprovação                    [o especialista decide]
```

---

### Fase 1 — Ingestão & Limpeza

**Líder:** humano + ferramenta. Não é trabalho criativo.

**Inputs:** arquivos .txt/.srt/.vtt das transcrições.

**Outputs:**
- `transcricao-limpa-{id}.txt` — uma transcrição por arquivo, com mínima normalização (não removemos oralidade; ela é dado, não ruído)
- `inventario-fontes.md` — tabela: arquivo, duração estimada, contexto (aula/live/entrevista), data, palavras totais

**O que LIMPAR:**
- Marcadores automáticos do transcritor que não são fala ("[música]", "[inaudível]")
- Erros óbvios de transcrição que distorcem palavra (ex: "bação" no lugar de "bastão" — anotar em margem, manter original com `[sic: bastão]`)
- Cabeçalhos repetidos por segmentação automática

**O que NÃO LIMPAR (CRÍTICO):**
- Filler words ("tipo", "tá ligado", "meio que") — são marcadores de oralidade (§3.6 do template)
- Autocorreções em voz alta ("não, deixa eu falar de novo") — são padrões retóricos (§3.5)
- Repetições aparentes ("tudo, tudo, tudo, tudo") — são recursos de ênfase (§3.5)
- Frases torrenciais sem ponto final do transcritor — refletem cadência real

> **Heurística "Limpar tira voz":** se em dúvida sobre limpar, NÃO LIMPE. Voz mora justamente onde a transcrição parece "feia".

---

### Fase 2 — Codificação Léxica

**Líder:** @gary-halbert (vocabulário visceral) com check de @claude-hopkins (palavras que carregam prova).

**Output:** `codificacao-lexica-{especialista}.md` — três listas:
1. Candidatas a palavras-assinatura
2. Metáforas-mãe
3. Palavras-veto

#### Heurísticas para palavras-assinatura

| Heurística | Critério numérico | Justificativa |
|---|---|---|
| H1 — Frequência mínima | Aparece **3+ vezes** no corpus em **contextos distintos** | Repetição em UM bloco é ênfase pontual. Em múltiplos blocos = assinatura. |
| H2 — Função estruturante | Aparece **1 vez** mas o termo organiza um modelo mental que ele reusa | Captura termos cunhados pelo especialista (ex: uma metáfora-mãe que ele introduz e volta depois). |
| H3 — Densidade fora da norma | Frequência por 1.000 palavras é **>3x** a média do português coloquial | Detecta termos sem-saliência semântica mas com saliência estatística (ex: "meio que" muito acima da norma). |
| H4 — Marcação afetiva | Termo carrega carga emocional do especialista (xingamento, ênfase, gíria identitária) | Mesmo que apareça 2 vezes, se vier acompanhado de ênfase ("PRA CARALHO"), é assinatura. |

**Falsos positivos comuns (descartar):**
- Conectores genéricos do português ("e", "ou", "porque") — só entram se usados de forma anômala
- Termos do nicho usados por qualquer um do nicho (ex: "treino" para preparador físico) — só entram se a forma de usar for marcada
- Repetições causadas pelo tema do dia (ex: ele falou da palavra X 10 vezes porque o tópico era X)

#### Heurísticas para metáforas-mãe

> Critério: a mesma imagem retorna **em contextos diferentes** para explicar **conceitos diferentes**. Se "chapéuzinho" explica especialização de agente E delimitação de tarefa E foco mental, é metáfora-mãe. Se aparece só uma vez para uma coisa, é enfeite.

#### Heurísticas para palavras-veto

Duas vias:
- **Veto declarado:** o especialista explicita ("eu odeio quando falam X"). Forte.
- **Veto descoberto:** termo padrão do nicho que ele **nunca** usa em N horas de transcrição. Médio. Confirmar com o especialista antes de tratar como regra.

---

### Fase 3 — Análise Sintática

**Líderes:** @gary-bencivenga (ritmo, bullets, fascination structure) + @bill-bernbach (preservação da voz autêntica) + @gary-halbert (cadência conversacional).

**Output:** `padroes-sintaticos-{especialista}.md`

#### O que medir

| Métrica | Como medir | Útil para |
|---|---|---|
| Mediana de palavras/frase | Tokenizar por pontuação real, contar palavras, mediana | Distinguir "longo" de "curto" objetivamente |
| % de frases curtas (<12), médias (12-25), longas (>25) | Histograma | Identificar se o ritmo é staccato, balanceado ou torrencial |
| Pergunta retórica por minuto | Contar "?" que não esperam resposta | Marcar densidade de engajamento conversacional |
| % de aberturas com conector | Quantas frases começam com "Então", "Aí", "Só que", etc. | Detectar padrão de transição que precisa entrar no copy |
| Anáforas | Identificar repetições de 2+ palavras em início de frases consecutivas | Recurso retórico para preservar |

**Heurística 30%:** se uma estrutura sintática (abertura, transição, fechamento) aparece em **30%+ das ocorrências** daquela função no corpus, é **dominante**. Entra no template como padrão obrigatório no copy.

**Heurística 10%:** se aparece em **10-29%**, é **secundário**. Entra como variação opcional.

**Heurística <10%:** é **idiossincrasia ocasional**. Vai para backlog, não para o documento.

#### Como mapear marcadores de oralidade

1. Listar todos os filler words observados ("tipo", "tá ligado", "meio que", "vamos dizer assim", "mano", "ó")
2. Para cada um: contar ocorrências por 1.000 palavras
3. Decidir política de copy escrito:
   - Frequência alta (>5 por 1.000): MANTER em copy informal (posts, emails, scripts de áudio); reduzir para 30-50% em copy formal (VSL escrita, sales page)
   - Frequência média (2-5 por 1.000): MANTER em copy informal; reduzir para 10-20% em formal
   - Frequência baixa (<2): usar pontualmente para dar sabor

> **Por quê reduzir, não eliminar:** copy escrito sem nenhum marcador soa estéril e quebra a ilusão de voz. Copy escrito com marcadores na frequência da fala soa transcrição mal-editada. A regra é proporcional: copy escrito = ~30% da densidade oral.

---

### Fase 4 — Mapa de Crenças & Inimigos

**Líderes:** @eugene-schwartz (Breakthrough Advertising — awareness stages e core beliefs) + @todd-brown (E5 Method, especialmente "Established Beliefs of the market") + @michael-masterson (Inimigo Comum).

**Output:** `mapa-crencas-{especialista}.md`

#### Como extrair a tese central

Procurar nas transcrições por:
- Afirmações universais ("a verdade é que...", "ninguém te conta que...", "no fim das contas...")
- Frases que fecham um bloco de explicação (geralmente é onde o especialista resume sua posição)
- Repetição da mesma ideia com palavras diferentes em contextos distintos (= ideia-pilar)

A tese central deve ser **falsificável e polêmica**. Se for "saúde é importante", você não capturou nada. Tese real cria atrito com o mercado.

#### Como extrair crenças derivadas

Crença derivada = "Se a tese central é verdade, então X também é". Procurar em frases que começam com:
- "Por isso que..."
- "Aí é por isso que..."
- "É por isso que eu falo que..."
- "O que acontece é que..." (frequentemente introduz consequência derivada)

#### Como extrair inimigos

Quatro tipos a procurar:

| Tipo | Sinais | Exemplo de extração |
|---|---|---|
| Vilão-pessoa | Categoria nomeada de profissional/figura | "esses caras que falam X" |
| Vilão-sistema | Instituição/setor criticado | "a indústria X" |
| Vilão-mito | Crença popular que ele rejeita | "essa história de que..." |
| Vilão-comportamento | Hábito ou postura criticada | "quem fica fazendo Y" |

> **Diretriz @todd-brown:** o especialista quase sempre tem inimigo claro, mas raramente o nomeia diretamente — chega lá por descrição. Procurar por padrões "esses caras que…", "o pessoal que…", "tem uma galera que…" + crítica subsequente.

---

### Fase 5 — Provas e Histórias

**Líder:** @claude-hopkins (Scientific Advertising — toda alegação precisa de evidência rastreável).

**Output:** `provas-historias-{especialista}.md`

#### Inventário de histórias-âncora

Critério para uma história entrar como âncora:
- Aparece em **2+ transcrições distintas** OU
- Aparece **1 vez** mas com estrutura completa (situação→conflito→resolução→lição) e o especialista a usa para argumentar (não só ilustrar)

Documentar para cada uma:
- **Apelido** curto (ex: "Cliente que mudou de 90kg em 6 meses")
- **Resumo** em 1-2 linhas
- **Função argumentativa** (prova de transformação / prova de método / contra-exemplo / etc.)
- **Citação** com timestamp

#### Hierarquia de provas

Identificar a **ordem em que o especialista invoca prova**:
1. O que ele puxa primeiro quando começa a argumentar? (= prova mais barata para ele)
2. O que ele guarda para o fechamento? (= prova mais pesada)
3. Que tipo de prova ele NÃO usa? (= sinal de identidade — ex: especialista que nunca cita estudo)

Isso vai informar a sequência de prova no copy.

---

### Fase 6 — Síntese (Preenchimento do Template)

**Quem faz:** a skill, preenchendo o template.

Preencher `template-tom-de-voz.md` seção por seção, **com citação para cada afirmação**. Qualquer seção sem evidência fica vazia e vai para o Backlog (§13 do template).

**Regra de auto-disciplina:** ao tentar preencher uma seção, se você se pega "deduzindo" em vez de citando, pare. Marque a seção como `Backlog — falta evidência` e siga em frente. Tentar "completar" sem dado é o que destrói a confiabilidade do documento.

**Versão de saída desta fase:** `v0.1 — Rascunho`.

---

### Fase 7 — Validação

**Auditor:** @claude-hopkins (Hopkins audit aplicado à voz, mínimo 85/100).

#### Teste do Cego

1. Pegar um copy curto (200-400 palavras) já produzido para outro especialista do mesmo nicho.
2. Reescrever esse copy usando exclusivamente o documento de ToV recém-criado.
3. Mostrar a versão reescrita a alguém que conhece o especialista, sem dizer que é gerado.
4. **PASS:** a pessoa reconhece o autor sem hesitar.
5. **FAIL:** a pessoa hesita, diz "parece, mas..." ou identifica autor errado.

Se FAIL → voltar para Fase 2 ou 3 (geralmente o problema é sintaxe, não vocabulário).

#### Teste do Inverso

1. Pegar o mesmo conteúdo do passo anterior.
2. Gerar uma versão **genérica do nicho** (sem usar o ToV).
3. Comparar lado a lado.
4. **PASS:** as diferenças entre versão ToV e versão genérica são óbvias mesmo para leigo.
5. **FAIL:** as duas versões parecem intercambiáveis.

Se FAIL → o ToV está capturando obviedades do nicho, não a voz específica. Voltar para Fases 2 e 4 com olhar mais crítico.

#### Hopkins audit aplicado

Rodar a rubric da §11 do template em pelo menos 3 copies-teste. Aprovação:
- Média >= 7.5
- Nenhum eixo abaixo de 6
- Os 7 eixos cobertos em todos os copies

---

### Fase 8 — Aprovação

**Decisor:** o próprio especialista (é a voz dele).

| Estado de aprovação | Critério | Próximo passo |
|---|---|---|
| **Rascunho (v0.1)** | Fases 1-6 concluídas, Fase 7 não rodada | Uso interno, A/B testing apenas |
| **Calibrado (v1.0)** | Fase 7 com PASS em Teste do Cego e Inverso | Liberado para campanha de tráfego pago |
| **Validado (v2.0)** | v1.0 + revisão de pelo menos 3 copies aprovados em produção + idealmente revisão direta com o especialista | Liberado para VSL, lançamento, conteúdo de marca |

---

## 2. Tratamento de Ruído em Transcrições

Problemas frequentes e como tratar:

| Problema | Decisão |
|---|---|
| Erro de transcrição muda o sentido ("bação" no lugar de "bastão") | Anotar `[sic: forma correta]` na transcrição limpa; descartar a palavra como candidata a assinatura |
| Múltiplas vozes na transcrição (entrevistador + especialista) | Separar antes de codificar; só o especialista alimenta o ToV |
| Frases que o transcritor cortou no meio | Marcar `[corte]`; não usar para análise sintática de comprimento |
| Especialista lê algo (texto não-original) | Excluir do corpus; voz lida ≠ voz falada |
| Especialista cita outro autor | Não confundir citação com fala dele; marcar e excluir do corpus de assinatura |

---

## 3. Quando Iterar (Recoleta)

Sinais de que o ToV precisa de mais material:

- Backlog (§13 do template) maior que 10 itens
- Teste do Cego com FAIL
- Cobertura de contexto enviesada (só aulas, sem entrevista; só Q&A, sem aula técnica)
- Especialista lançando produto novo ou mudando posicionamento (ToV antigo pode estar desatualizado)

---

## 4. Quem Faz o Quê (Mapa de Líderes por Fase)

| Fase | Líder primário | Apoio | Auditor |
|---|---|---|---|
| 1. Ingestão | humano/ferramenta | — | — |
| 2. Codificação Léxica | @gary-halbert | @claude-hopkins | — |
| 3. Análise Sintática | @gary-bencivenga | @bill-bernbach, @gary-halbert | — |
| 4. Mapa de Crenças | @eugene-schwartz | @todd-brown, @michael-masterson | — |
| 5. Provas e Histórias | @claude-hopkins | @gary-halbert | — |
| 6. Síntese | a skill | (todos) | — |
| 7. Validação | @claude-hopkins | — | o especialista |
| 8. Aprovação | o especialista | — | — |

---

## 5. Critério de Aprovação Final (TL;DR)

Para um documento de ToV ser declarado **Calibrado (v1.0)**:

1. Volume >= 3h em >=3 contextos distintos
2. Todas as 13 seções do template preenchidas OU explicitamente marcadas como "sem evidência suficiente" no Backlog
3. Cada afirmação no documento ancorada em pelo menos 1 citação direta (apêndice §12 do template)
4. Teste do Cego: PASS
5. Teste do Inverso: PASS
6. Rubric §11 média >= 7.5 em 3 copies-teste, nenhum eixo abaixo de 6
7. Hopkins audit >= 85/100
