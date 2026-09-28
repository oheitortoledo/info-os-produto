---
name: tom-de-voz
description: Extrai o TOM DE VOZ do especialista a partir de 30+ minutos dele falando (aula, live, YouTube, podcast, call) e entrega o documento de voz que toda copy passa a consultar: palavras-assinatura, vetos, jeito de abrir e fechar, crenças, inimigos, histórias, tom emocional, régua de 7 notas pra aprovar texto e biblioteca de frases prontas. Transcreve sozinho: link do YouTube (pode ser NÃO LISTADO), arquivo de vídeo/áudio (AssemblyAI) ou transcrição pronta. Tudo com citação literal. Bloco 3 do Alicerce do Copy (a /alicerce-copy roda junto). Use SEMPRE que o usuário disser "tom de voz", "minha voz", "como eu falo", "quero que a copy soe como eu", "a copy não parece comigo", "extrair minha voz", "transcreve minhas aulas", "guia de voz", ou mandar vídeos/aulas dele pedindo pra entender o estilo. NÃO é a voz do público (/persona-profunda) nem identidade visual (/identidade-visual).
---

# Tom de Voz do Especialista

## O que ela entrega

Um documento que responde: **como essa pessoa fala, de verdade?** Qualquer texto escrito depois (anúncio, página, email, roteiro) passa por ele antes de sair. É o que impede a copy de soar como "mais um do nicho".

A regra que sustenta tudo: **se não tem citação da fala dele, não entra.** O que foi visto uma vez só vai pro Backlog, esperando mais material. A voz tem que emergir da fala, nunca do molde.

## Pra quem é

O aluno é o próprio especialista (ou está fazendo pro especialista que ele atende). Não é copywriter. Na conversa, português simples e zero jargão — nada de "ToV", "anáfora", "tricolon", "n-grama". Diga "suas expressões que se repetem", "o jeito que você abre um assunto", "as frases que você repete como lei". No documento, o rigor técnico fica.

---

## Dois modos

- **Modo briefing (chamada pela `/alicerce-copy` como subagente):** o prompt traz um bloco `BRIEFING` com nome do especialista, nicho, a pasta onde as transcrições JÁ estão e a pasta de saída. Não pergunte nada, não abra arquivo. Rode do Passo 3 ao 6 e devolva um resumo curto: arquivos gerados · volume analisado · maturidade · top 5 palavras-assinatura · top 3 vetos · tese central · tamanho do Backlog.
- **Modo direto (o aluno chamou `/tom-de-voz`):** siga do Passo 1 ao 7.

---

## Passo 1 — Pedir o material

Diga o que é e por quê, curto:

> "Pra eu pegar o seu jeito de falar, preciso de **pelo menos 30 minutos de você falando** — aula, live, vídeo do YouTube, podcast, reunião gravada, qualquer coisa. Quanto mais natural, melhor.
>
> **Dica que faz diferença:** misture contextos. 15 min de aula + 15 min de live respondendo pergunta vale mais que 30 min de uma aula só, porque cada situação mostra um lado da sua fala.
>
> Pode me mandar de 3 jeitos:
> 1. **Link do YouTube** — o mais fácil. Se o vídeo não é público, suba como **não listado** (só quem tem o link vê) e me mande o link.
> 2. **Arquivo de vídeo ou áudio** — eu transcrevo pela AssemblyAI (precisa de uma chave grátis, te ensino em 1 minuto).
> 3. **Transcrição pronta** (.txt, .srt, .vtt) — se você já tem."

**Não serve:** vídeo em que ele **lê roteiro** (voz lida não é voz falada), vídeo onde quem mais fala é outra pessoa, anúncio muito editado. Se o aluno mandar isso, explique e peça outro.

### Se ele escolher arquivo (AssemblyAI)

Só se ainda não tiver a chave configurada (`echo $ASSEMBLYAI_API_KEY`):

1. Criar conta grátis em **assemblyai.com** e copiar a **API Key** no painel.
2. Rodar no terminal — Mac: `export ASSEMBLYAI_API_KEY=cole_aqui` · Windows: `setx ASSEMBLYAI_API_KEY cole_aqui` (e fechar/abrir o terminal).

Se ele travar aqui, ofereça o caminho do YouTube não listado — não depende de chave nenhuma.

---

## Passo 2 — Transcrever

Pasta de saída: `infoproduto/alicerce-do-copy/tom-de-voz/`.

```bash
python3 .claude/skills/tom-de-voz/scripts/transcrever.py <link-ou-arquivo> [<outro> ...] --out infoproduto/alicerce-do-copy/tom-de-voz/transcricoes
```

O script devolve palavras e minutos por fonte e avisa se passou do mínimo.

- **Falta yt-dlp:** peça pra instalar (`pip install yt-dlp`, ou `brew install yt-dlp` no Mac) e rode de novo.
- **Vídeo sem legenda em português:** peça o arquivo e vá pela AssemblyAI.
- **Mais de uma voz** (a AssemblyAI marca `[Falante A]`, `[Falante B]`): leia um trecho, identifique qual é o especialista, e passe o outro em `--ignorar` no Passo 3. Só a voz dele entra.
- **Abaixo de 30 min:** diga quanto falta e peça mais. Com 10–29 min, só siga se ele insistir, e marque o documento como **Piloto — não usar em copy de produção**.

---

## Passo 3 — Medir (a parte contável)

```bash
python3 .claude/skills/tom-de-voz/scripts/medir_voz.py <pasta>/transcricoes > <pasta>/medicao-voz.md
```

Ele devolve volume, ritmo de frase, vícios de fala por 1.000 palavras com a política pro texto escrito, expressões repetidas **e em quantos arquivos cada uma aparece**, e as aberturas de frase mais comuns.

Número não é conclusão. É o ponto de partida pra você ler a transcrição com olho treinado. Duas armadilhas:
- **Assunto do dia não é assinatura.** "Máximo de oxigênio" 13 vezes numa aula de cardio é tema, não voz. Assinatura aparece em **contextos diferentes**.
- **Legenda automática erra palavra.** Antes de promover um termo esquisito a assinatura, confira se não é erro de transcrição. Quando for, cite com `[sic: forma correta]`.

---

## Passo 4 — Ler e extrair (Fases 1–5 da metodologia)

Leia `references/metodologia.md` inteiro antes de começar — ele tem os critérios numéricos de cada fase. Resumo do que você faz lendo as transcrições:

1. **Limpeza mínima** — tira `[música]` e cabeçalho. **Não tira** "tipo", "né", repetição, autocorreção: isso é voz. Na dúvida, não limpe.
2. **Palavras** — assinatura (3+ vezes em contextos distintos, ou 1 vez estruturando um conceito que ele reusa), metáforas-mãe, jargão que ele usa sem explicar × jargão que ele traduz, vetos.
3. **Frase** — como ele abre um assunto, como faz transição, como fecha. Padrão em 30%+ das vezes = dominante; 10–29% = variação; <10% = Backlog.
4. **Crenças e inimigos** — a tese central (tem que criar atrito com o mercado; "saúde é importante" não é tese), as crenças que derivam dela ("por isso que…"), o que ele ataca, e os vilões (pessoa, sistema, mito, comportamento — procure "esses caras que…", "tem uma galera que…").
5. **Provas e histórias** — histórias que ele repete ou conta completas pra argumentar, o tipo de prova que ele puxa primeiro e o que guarda pro fim.

**Disciplina que decide a qualidade:** se você se pegar *deduzindo* em vez de *citando*, pare. Aquilo vai pro Backlog. Documento completo e inventado é pior que documento curto e verdadeiro — a copy vai herdar a invenção.

---

## Passo 5 — Escrever o documento

Preencha `references/template-tom-de-voz.md` seção por seção e salve em `<pasta>/tom-de-voz-<nome>-v1.md`. Versão nova = `-v2`, nunca sobrescrever.

- **Toda afirmação com citação** entre aspas, do arquivo de origem. O Apêndice (§12) guarda as citações brutas.
- **Maturidade honesta** nos Metadados, pela régua da metodologia: 30–59 min = **Rascunho (v0.1)**, bom pra anúncio e post em teste; 60 min+ em 2+ contextos = **Rascunho forte**; **Calibrado** só depois do teste do Passo 7 aprovado com 3h+. Diga quais contextos faltam.
- **§14 Biblioteca pronta** — aberturas, fechamentos, pares ❌ genérico / ✅ como ele diria, frases-lei. Use frase literal sempre que der. É a seção que ele vai usar todo dia.
- **TL;DR por último**, no topo.

Se o projeto já tem a persona profunda (`*alicerce-do-copy/persona-profunda/persona-profunda-*.md`), cruze os inimigos e crenças dele com o vilão e as crenças do público: onde batem é munição de copy; onde divergem, registre no Backlog (ele pode estar falando de um jeito que o público não reconhece).

---

## Passo 6 — O teste de voz

Salve `<pasta>/teste-de-voz.md` com **um mesmo texto curto em duas versões** (um gancho de anúncio de 3–4 frases, ou um post curto, sobre um tema que apareceu na fala dele):

- **Versão A** — genérica do nicho, como qualquer um escreveria.
- **Versão B** — usando só o documento de voz.

Embaralhe a ordem (não diga qual é qual) e embaixo coloque as 3 perguntas do Passo 7. Se as duas versões ficarem parecidas até pra você, o documento está capturando o óbvio do nicho e não a pessoa: volte ao Passo 4 com olhar mais crítico nas palavras e nas crenças.

---

## Passo 7 — Validar com ele (modo direto)

Abra o documento e mostre o teste ao aluno, em linguagem simples:

> "Pronto. Antes de você usar, um teste rápido: qual dessas duas soa como você?
> 1. Qual das duas você diria?
> 2. Tem alguma palavra ali que você **nunca** usaria?
> 3. Falta alguma expressão que você fala o tempo todo e eu não peguei?"

As respostas dele são evidência direta — a mais forte que existe (veto declarado, assinatura confirmada). Aplique no documento, registre no Changelog e suba a versão (`-v1` → `-v1.1`). Se ele não reconhecer a versão B, o problema quase sempre é o ritmo da frase, não o vocabulário: releia a Fase 3.

Feche dizendo, curto:
1. **Sua voz em uma frase** (o TL;DR).
2. **O que eu ainda não sei** — os maiores itens do Backlog e que tipo de vídeo resolveria (ex.: "falta você respondendo objeção ao vivo — uma live de perguntas resolve").
3. **Como usar:** toda copy que sair daqui em diante passa pela régua de 7 notas (§11) antes de ir pro ar.

---

## Erros que estragam o documento

**Descrever o nicho em vez da pessoa.** "Usa linguagem acessível e didática" serve pra qualquer professor. Se o item não serve só pra ele, não é voz.

**Promover tema a assinatura.** Palavra que só aparece na aula sobre aquele assunto é conteúdo.

**Limpar a oralidade.** Tirar "né", "tipo", "então" e a frase que ele reformula no meio. É exatamente aí que a voz mora.

**Inventar pra completar.** Seção vazia com "sem evidência — Backlog" é resposta certa. Seção cheia de dedução é o erro que chega publicado.

**Analisar a voz errada.** Entrevistador, co-apresentador, trecho lido de roteiro. Só a fala espontânea do especialista.
