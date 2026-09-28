---
name: biblioteca-anuncios-meta
description: Minera, disseca e GUARDA os anúncios de um concorrente da Biblioteca de Anúncios da Meta numa biblioteca permanente do seu produto (infoproduto/criativos/biblioteca-anuncios/) — vídeo, fala, visual e os 8 trabalhos de cada peça — pra não precisar minerar de novo. Na segunda rodada no mesmo link, só processa o que é NOVO, marca o que SAIU do ar sem apagar e recalcula há quantos dias cada anúncio está rodando (anúncio que roda há muito tempo está dando dinheiro). Você manda o LINK; nunca busca por palavra-chave. Use quando o usuário mandar um link da Biblioteca de Anúncios da Meta (facebook.com/ads/library) ou disser "minera os anúncios desse concorrente", "analisa os anúncios de fulano", "o que o mercado está anunciando", "quais anúncios estão rodando há mais tempo", "atualiza a biblioteca", "roda de novo o <concorrente>", "o que mudou nos anúncios do <concorrente>", ou quando a skill de escrever criativos precisar dos anúncios do nicho — nesse caso, LER a biblioteca antes de minerar.
---

# Biblioteca de Anúncios da Meta

**O que dizer ao aluno logo no começo (2 linhas, com estas ideias):**
> "Vou ver o que o seu mercado já está anunciando e há quanto tempo cada anúncio está no ar.
> Anúncio que roda há muito tempo quase sempre está dando dinheiro — é daí que a gente tira o que funciona."

A skill minera os anúncios de um concorrente e **guarda** cada um numa ficha permanente,
com o vídeo, a fala, o visual e a dissecação. Rodar de novo não refaz nada — só acrescenta
o que é novo e registra o que saiu do ar.

**Por que guardar muda o jogo:** a repetição mede a aposta do anunciante, nunca o
resultado. O que chega mais perto de resultado, sem acesso às métricas dele, é a
**longevidade**: anúncio de venda direta que roda há 60 dias está pagando a conta. Só dá
pra medir longevidade se alguém anotou quando a peça foi vista pela primeira e pela
última vez. A biblioteca anota.

## Como falar com o aluno

O aluno é especialista, não é gestor de tráfego. No chat, português simples, "você", sem
jargão. No arquivo, o rigor fica todo. Traduções pra usar no chat:

| No arquivo | No chat |
|---|---|
| os 8 trabalhos | as 8 partes do anúncio (formato, o que prende o olho, a primeira frase, o miolo, a chamada pra ação…) |
| longevidade | há quanto tempo o anúncio está no ar |
| variações agrupadas | versões do mesmo anúncio que a Meta junta (mesmo vídeo com texto ou título diferente) |
| minerar | buscar os anúncios |
| processar | baixar o vídeo, transcrever a fala e descrever o que aparece |
| leva | grupo de 5 anúncios |
| copy hook / visual hook | a primeira frase / o que prende o olho no começo |
| fala_suspeita | a transcrição saiu duvidosa (áudio ruim, música alta) |

## Configurar as chaves (uma vez só)

A skill usa três serviços de fora. Cada um dá uma **chave** (uma senha comprida que
identifica a sua conta). Você cria a conta, copia a chave e salva no seu computador.
**Não cole a chave aqui no chat** — salve direto no terminal, como abaixo.

| Serviço | Pra quê | Precisa? | Onde pegar a chave |
|---|---|---|---|
| **Apify** | buscar os anúncios na Biblioteca da Meta | **obrigatória** — sem ela não dá pra começar | crie a conta em apify.com → no painel, **Settings → API & Integrations** → copie o **Personal API token** |
| **AssemblyAI** | transcrever o que é falado no vídeo | recomendada — sem ela os vídeos ficam sem a fala | crie a conta em assemblyai.com → no painel, copie a **API Key** |
| **TwelveLabs** | descrever o que aparece no vídeo | opcional — sem ela eu tiro fotos do vídeo e olho uma por uma (funciona, só é mais lento) | crie a conta em twelvelabs.io → no painel, área **API Keys** |

**Como salvar** (troque `cole_aqui` pela sua chave, uma linha por chave que você tiver):

- **Mac** — no Terminal:
  ```bash
  echo 'export APIFY_TOKEN="cole_aqui"' >> ~/.zshrc
  echo 'export ASSEMBLYAI_API_KEY="cole_aqui"' >> ~/.zshrc
  echo 'export TWELVELABS_KEY="cole_aqui"' >> ~/.zshrc
  ```
- **Windows** — no PowerShell ou Prompt de Comando:
  ```
  setx APIFY_TOKEN "cole_aqui"
  setx ASSEMBLYAI_API_KEY "cole_aqui"
  setx TWELVELABS_KEY "cole_aqui"
  ```

Depois de salvar, **feche e abra o terminal e o Claude Code** — a chave só aparece em
janela nova. (Se você já tem a chave da AssemblyAI salva como `ASSEMBLYAI_KEY`, também
serve.)

**Custo, com honestidade:** os três cobram por uso. A Apify tem plano grátis com um
crédito mensal pequeno — cada busca gasta um pouco, e um concorrente com muitos anúncios
pode gastar boa parte do mês. AssemblyAI e TwelveLabs costumam dar crédito inicial ao
criar a conta. Os valores mudam: confira a página de preços de cada um antes de usar
muito. Por isso a skill guarda tudo — rodar de novo só busca o que é novo.

## Antes de tudo: checar chaves e programas

No início de **toda** rodada, da raiz do repo:

```bash
python3 .claude/skills/biblioteca-anuncios-meta/scripts/biblioteca.py checar
```

(No Windows, se `python3` não existir, use `python` ou `py` no lugar — em todos os comandos desta skill.)

Leia o resultado e diga ao aluno, em uma frase, **exatamente o que falta** e o que isso
muda. Nunca mostre erro técnico cru — traduza. Nunca imprima, repita ou peça o valor de
uma chave.

| O que falta | O que fazer |
|---|---|
| **Apify** | Pare. Mostre a linha da Apify da seção "Configurar as chaves" e espere ele salvar. Sem ela não há mineração. (Se ele já tem os vídeos baixados, dá pra seguir com o subcomando `arquivo`, peça por peça.) |
| **AssemblyAI** | Pode seguir, avisando: "vou guardar os anúncios, mas sem a fala transcrita — dá pra transcrever depois quando você criar a chave". Registre nas Pendências. |
| **TwelveLabs** | Siga, avisando: "sem a TwelveLabs, eu tiro fotos do vídeo a cada 2 segundos e descrevo olhando cada uma. Funciona, só demora mais." |
| **ffmpeg** | Instalar em 1 linha — Mac: `brew install ffmpeg` · Windows: `winget install ffmpeg` (depois, abrir terminal novo). Sem ele a skill segue: a fala ainda é transcrita (o vídeo inteiro vai pra AssemblyAI), mas sem fotos do vídeo e sem comprimir vídeo grande. Se faltar também a TwelveLabs, a análise visual fica de fora — registre. |
| **pacote `requests` do Python** | O script avisa sozinho. Mac: `python3 -m pip install requests` · Windows: `python -m pip install requests`. |

**Mac — chave salva mas o `checar` diz que falta:** o Claude Code foi aberto antes de
salvar. Peça pra fechar e abrir de novo. Se continuar, rode os comandos da skill como
`zsh -ic "python3 ..."`, que carrega o `~/.zshrc`.

Tudo o que ficou de fora numa rodada (sem fala, sem visual) vai para as **Pendências**
da ficha e do consolidado. Nada é inventado pra tapar buraco.

## Onde a biblioteca mora

Sempre em `infoproduto/criativos/biblioteca-anuncios/` (caminho a partir da raiz do
repo). Crie a pasta se não existir. Nunca grave na raiz do repo.

```
infoproduto/criativos/biblioteca-anuncios/
├── README.md                      índice de todos os anunciantes (regenerado a cada rodada)
└── <anunciante-slug>/
    ├── anunciante.md              ficha: link, página, oferta de destino, histórico de rodadas
    ├── dissecacao.md              consolidado: tabela geral + elementos repetidos + longevidade
    ├── anuncios.json              estado de cada peça (fonte da verdade do script — não editar à mão)
    ├── pecas/<id>.md              UMA ficha por anúncio
    ├── midia/<id>.mp4|.jpg        o criativo em si (fora do git)
    ├── _trabalho/<id>.json        saída crua do script (fala + visual), insumo da ficha
    └── _bruto/apify-AAAA-MM-DD.json   resposta crua da Apify de cada rodada
```

**Git:** `midia/`, `_bruto/` e `_trabalho/` não se versionam (vídeo pesa e não é seu).
O `.gitignore` da raiz do Info OS já deixa estas pastas de fora do git. Se o aluno apagou o arquivo ou as linhas, recoloque:

```
infoproduto/criativos/biblioteca-anuncios/**/midia/
infoproduto/criativos/biblioteca-anuncios/**/_bruto/
infoproduto/criativos/biblioteca-anuncios/**/_trabalho/
```

`pecas/`, `dissecacao.md`, `anunciante.md`, `anuncios.json` e o README **se versionam** —
são o conhecimento.

`<anunciante-slug>`: nome da página em minúsculas, sem acento, com hífen
(`cozinha-de-domingo`). Um anunciante = uma pasta, mesmo que tenha vários links.

## Pipeline

O script faz a parte mecânica. A dissecação é trabalho seu. Da raiz do repo:

```bash
S=.claude/skills/biblioteca-anuncios-meta/scripts/biblioteca.py
B=infoproduto/criativos/biblioteca-anuncios
python3 $S checar
python3 $S minerar   --link '<LINK>' --dest "$B/<anunciante-slug>"
python3 $S processar --dest "$B/<anunciante-slug>" --ids ID1,ID2,ID3
python3 $S arquivo   --dest "$B/<anunciante-slug>" --id <ID> --arquivo video.mp4   # vídeo já baixado
python3 $S status    --dest "$B/<anunciante-slug>"
python3 $S marcar    --dest "$B/<anunciante-slug>" --ids ID1,ID2                   # depois de escrever as fichas
```

No Windows (PowerShell), escreva os caminhos por extenso em vez de usar `S=`/`B=`, entre
aspas duplas.

**O link:** o aluno manda o link da página do concorrente na Biblioteca de Anúncios
(`facebook.com/ads/library/?...`). **Nunca busque por palavra-chave.** Se ele não tem o
link, ensine: abrir facebook.com/ads/library, escolher país Brasil e "Todos os anúncios",
digitar o nome do concorrente, clicar na página dele e copiar o endereço da barra do
navegador.

### 0 · Antes de minerar: a biblioteca já tem esse anunciante?

Procure a pasta do anunciante. Se existir, mostre o `status` (última rodada, quantas
peças, quantas processadas) e pergunte: **usar o que já está guardado ou atualizar?**
Se a última rodada tem menos de 7 dias e o aluno não pediu atualização, use o que está
guardado. Buscar de novo gasta crédito da Apify.

### 1 · Minerar e comparar

`minerar` traz os dados dos anúncios (rápido, sem baixar vídeo) e junta com o
`anuncios.json`:

- **NOVA** — nunca vista. Entra com `processado: false`.
- **CONTINUA** — já estava e segue ativa. Atualiza `ultima_vez` e o link da mídia (o link expira).
- **SAIU** — estava ativa e não voltou. **Nada é apagado.** A ficha fica, com a data em que foi vista pela última vez.

Apresente ao aluno a tabela da rodada: novas, continuam, saíram — e, pra cada peça, há
quantos dias está no ar e quantas versões a Meta juntou.

**Se a Apify recusar por limite do mês:** diga em uma frase que o crédito do mês acabou
e ofereça as saídas: (a) esperar o ciclo renovar (a data aparece no painel da Apify, em
Billing/Usage); (b) adicionar crédito na conta; (c) coleta manual pela página da
Biblioteca com Playwright (só se ele topar instalar: `pip install playwright` e
`playwright install chromium`) — extraia do DOM ID, data de início e URL do vídeo, grave
com a função `juntar()` do script (`metodo="playwright"`) e **declare o método** no
`anunciante.md`.

### 2 · Processar em levas de 5 — só as peças que ainda não foram processadas

1. Proponha a leva: as NOVAS primeiro, em ordem de longevidade (a mais antiga ainda
   ativa é a mais valiosa). O aluno pode escolher outras.
2. `processar` baixa a mídia pra `midia/`, transcreve e faz a análise visual. Download
   falhou por link expirado → minere de novo (só os dados) e reprocesse.
3. Escreva a ficha de cada peça (§3) e rode `marcar`.
4. Entregue a leva e **pergunte: "Quer que eu processe mais 5?"** — e pare até a resposta.

O script lista em `ficou_de_fora` o que não deu pra fazer por falta de chave ou programa.
Isso vai pra Pendências da ficha, com a frase do que faltou.

**Regras da fala (invioláveis):**
- `fala_suspeita` (confiança < 0,62 mesmo depois da segunda tentativa automática) não é
  evidência: disseque pelo visual e pelo texto na tela e declare a limitação na ficha.
- Erros previsíveis de transcrição: números, preços (centavo fantasma), nomes próprios do
  nicho, palavras técnicas ("TDF" por "PDF"). Liste os suspeitos na ficha — **nunca
  corrija por conta própria**.
- `sem_chave` → a ficha sai sem transcrição, marcada em Pendências. Nunca invente transcrição.

**Regras do visual:**
- A fala vem da AssemblyAI; a TwelveLabs entrega **só** o visual. Ela resume — nunca a
  use como fonte de fala.
- **Armadilha conhecida:** quando o vídeo tem legenda karaokê, a TwelveLabs costuma
  despejar a legenda inteira em TEXTO NA TELA. Se o "texto na tela" repete a fala palavra
  por palavra, é legenda — mova pra LEGENDA e deixe em TEXTO NA TELA só o que é fixo
  (faixa, título, sticker, endcard).
- Fallback por frames (`visual.metodo` começa com "frames"): **olhe** os frames
  listados e preencha a mesma estrutura (ABERTURA · ESTRUTURA VISUAL · SPOKESPERSON ·
  TEXTO NA TELA · LEGENDA · VISUAL). Declare o método na ficha.
- `visual.metodo` = "sem análise visual" (sem TwelveLabs e sem ffmpeg) → disseque pela
  fala e pelo texto do feed, declare na ficha, e sugira instalar o ffmpeg.
- Anúncio de imagem: olhe o arquivo em `midia/` e disseque pelo estático.

### 3 · A ficha da peça — `pecas/<id>.md`

```markdown
# <id> · <formato> · <duração>s

| Campo | Valor |
|---|---|
| Anunciante | … |
| Início (Meta) | AAAA-MM-DD |
| Visto de / até | AAAA-MM-DD → AAAA-MM-DD (N dias) · status: ativo/saiu |
| Variações agrupadas | n |
| Destino | URL (e se é página de vendas, captura, VSL, grupo) |
| Mídia | midia/<id>.mp4 |
| Fala | AssemblyAI · confiança 0,xx  (ou: sem transcrição — motivo) |
| Visual | TwelveLabs pegasus1.5 / frames / sem análise visual — motivo |

## Os 8 trabalhos
| # | Trabalho | Registro |
|---|---|---|
| 1 | Formato | rótulo do catálogo de formatos, se houver um que case (ver abaixo) |
| 2 | Visual hook | o que segura o olho nos 3 primeiros segundos |
| 3 | Copy hook | a primeira fala verbatim + o esqueleto com slots |
| 4 | Body — introdução | como associa a ideia ao mecanismo/nome de atração |
| 5 | Body — explicação | a cadeia do porquê |
| 6 | Body — conclusão | como fecha e apresenta o destino |
| 7 | CTA — introdução | o comando + o que promete |
| 8 | CTA — motivo de agora | a urgência e o motivo dela |

**Transversais:** benefício principal (como dito, com unidade de tempo) · spokesperson ·
trend topic · preço dito no anúncio? (como: cheio, parcela, comparação) · ângulo.

## Visual
<a análise visual, já corrigida da armadilha da legenda>

## Transcrição
<a fala completa>

## Pendências
<falas suspeitas, o que não deu pra ver, o que foi inferido, o que ficou de fora por falta de chave/programa>
```

**Trend topic — 5 regras:** (1) é o tópico de interesse DITO NO GANCHO, com as
palavras ditas, nunca um rótulo seu; (2) ≠ promessa — desejo explícito é benefício;
(3) segue o nível de consciência; (4) gancho pode não ter — registre "sem trend topic" e
o que ocupa o lugar; (5) nome de atração no gancho → trend topic é o nome como dito.

**Formato:** use o nome do catálogo de formatos das skills de escrita
(`.claude/skills/_base-criativos/formatos/README.md` e as fichas `Fnn-*.md` da mesma
pasta) quando um deles descrever a peça, pra que a biblioteca e a escrita falem a mesma
língua. Nenhum casa → rótulo seu, e anote como candidato a formato novo no
`dissecacao.md`. Se a pasta do catálogo não existir no repo, use rótulo descritivo e
avise que a classificação ficou sem o catálogo.

**Agrupamento:** arquivo de vídeo diferente = peça distinta. Duplicata = transcrição
≥93% igual. Variação de gancho = corpo ≥82% igual e abertura (~18% iniciais) <65%
parecida. O texto do feed é metadado — a copy que importa é o que o vídeo fala e mostra.

### 4 · Regenerar o consolidado — `dissecacao.md` e `README.md`

A cada rodada, reescreva o `dissecacao.md` do anunciante a partir das fichas:

1. **Tabela geral** — peça · formato · copy hook resumido · duração · dias no ar · status. Ordenada por dias no ar.
2. **Longevidade** — as peças que rodam há mais tempo, separadas em ativas e que já saíram.
   Advertência: *longevidade é o melhor sinal disponível de que a peça paga a conta, e
   ainda assim não é prova — o anunciante pode estar rodando no prejuízo.*
3. **Elementos repetidos com contagem** (n/N) — formatos, esqueletos de gancho, motivos
   de agora, provas, benefícios, preço no anúncio. Duas colunas de contagem: sobre as
   **ativas agora** e sobre **todo o histórico**. Advertência no topo: *repetição mede a
   APOSTA do anunciante, nunca o resultado.*
4. **O que mudou desde a última rodada** — o que entrou, o que saiu, e o que isso sugere
   (ex.: saiu todo o lote de ilustração e ficou só o de comida real).
5. **Pendências** — peças não processadas, falas suspeitas, downloads que falharam, o que
   ficou de fora por falta de chave ou programa. Número exato.

E o `README.md` da biblioteca: uma linha por anunciante (link, última rodada, ativas /
total, processadas / total, a peça mais longeva).

O `anunciante.md` guarda o que não muda a cada rodada: link(s) da biblioteca, nome da
página, a oferta de destino (headline, preço, garantia, mecanismo — lida na página) e o
histórico de rodadas com o método de cada uma.

**Ao entregar pro aluno**, resuma em linguagem simples: quantos anúncios achou, quais
estão no ar há mais tempo (e por que isso importa), o que se repete entre eles, e o que
ficou pendente.

## Como as outras skills usam a biblioteca

A skill `escrever-criativos-ultra-low-ticket` (e qualquer outra de escrever criativo)
**lê a biblioteca, não minera**: na etapa 1 (mercado e formato) ela abre
`infoproduto/criativos/biblioteca-anuncios/` — o `README.md` pra ver os anunciantes, e o
`dissecacao.md` de cada um pra longevidade, formatos e elementos repetidos. Se a
biblioteca não tem o concorrente, ou a última rodada é velha pra decisão em jogo, ela
sugere rodar esta skill — nunca minera por conta própria.

## Regras que não podem ser violadas

- O link do aluno é a fonte. Zero busca por palavra-chave.
- Nada é apagado da biblioteca — o que sai do ar muda de status.
- Nada inventado: transcrição, número, contagem, data. Falhou → declara.
- Contagem sempre com denominador (7/20, não "a maioria").
- Leva máxima de 5, com pergunta entre levas.
- Chave nunca aparece em tela, log ou arquivo — nem é pedida no chat.
- Falta de chave ou programa se explica em português, com o que fazer; nunca erro técnico cru.
