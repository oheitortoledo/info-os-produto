---
name: carrossel
description: Cria carrossel pro Instagram (1080×1350, e versão TikTok se quiser) que fala com o SEU cliente, na SUA voz e com a cara da SUA marca — a pauta sai da Persona Profunda (as dores, as crenças e as frases exatas do público), o texto passa pelo seu tom de voz e o visual usa o marca/DESIGN.md. Texto aprovado ANTES do visual. Quatro paradas — pauta → espinha e capa → texto slide a slide + legenda → slide 1 renderizado — e entrega os PNGs prontos pra postar em conteudo/carrosseis/. Use SEMPRE que o usuário disser "carrossel", "carousel", "slides pro Instagram", "post em carrossel", "faz um carrossel sobre", "transforma isso em carrossel", "conteúdo pro feed", "o que eu posto", "ideia de post", "pauta de conteúdo", ou mandar um tema, texto, link ou vídeo pedindo pra virar carrossel. Precisa do Alicerce do Copy (pauta e linguagem) e roda melhor com o tom de voz e a identidade visual. NÃO posta nem agenda.
---

# Carrossel

O carrossel do Info OS não nasce de "um tema legal": nasce **do que o seu cliente sente, pensa e fala**
— que já está mapeado na Persona Profunda. É isso que faz a pessoa parar no feed e pensar "isso é
comigo". O texto sai na **sua** voz (tom de voz) e o visual com a **sua** marca (DESIGN.md), pra que
o carrossel, a página e o anúncio pareçam da mesma pessoa.

**Texto primeiro, visual depois.** O texto é aprovado inteiro antes de qualquer slide ser desenhado.
Mexer no texto depois do visual custa refazer slide.

---

## Pra quem é esta skill

Quem usa é o especialista, não um social media. Por dentro, rigor total (fonte de cada ideia na
Persona Profunda, régua de palavras medida em código, render conferido). Por fora, português
simples, uma coisa por vez, dizendo **o que está fazendo e por quê**.

| Termo (nos arquivos) | Como falar com o aluno |
|---|---|
| pauta | o assunto do carrossel e o ângulo |
| espinha | o caminho do carrossel, do primeiro ao último slide |
| capa | o slide 1: o que faz a pessoa parar de rolar |
| virada | o slide em que a pessoa entende algo que não entendia |
| CTA | o pedido do último slide (comentar, salvar, clicar no link) |
| Persona Profunda / S4, S5, S7… | o retrato do seu cliente (códigos só nos arquivos) |

---

## Etapa 0 — Conferir

Rode na raiz do Info OS:

```bash
find infoproduto/alicerce-do-copy marca conteudo/carrosseis -maxdepth 3 -type f -name "*.md" 2>/dev/null
```

1. **Persona Profunda** (`infoproduto/alicerce-do-copy/persona-profunda/persona-profunda-*.md`) e o
   banco de frases (`banco-verbatim-*.md`) — **obrigatórios**. Sem eles, **pare**:
   > "Antes do conteúdo, a gente precisa do seu Alicerce do Copy — é dele que sai do que o seu
   > cliente reclama, no que ele acredita e as palavras que ele usa. Sem isso eu escrevo carrossel
   > genérico, igual ao de todo mundo. Roda o `/alicerce-copy` e volta aqui."
2. **Tom de voz** (`infoproduto/alicerce-do-copy/tom-de-voz/tom-de-voz-*.md`) — se existir, o texto
   passa por ele. Se não, siga e avise numa linha que o texto vai sair neutro até ele rodar `/tom-de-voz`.
3. **Identidade visual** (`marca/DESIGN.md`) — necessária na Etapa 4. Se não existir, dá pra fazer as
   etapas de texto; antes do visual, mande rodar `/identidade-visual`.
4. **Carrosséis anteriores** (`conteudo/carrosseis/`) — leia os títulos pra não repetir pauta.
5. **Perfil** — o @ do Instagram (vai no rodapé dos slides). Se não estiver no `marca/DESIGN.md` nem
   no `_contexto/`, pergunte uma vez e anote no `marca/DESIGN.md`.

Havendo `-v2`, `-v3` de qualquer documento, use a versão mais alta.

---

## Etapa 1 — Pauta (parada)

**Se o aluno trouxe o tema** (texto, link, vídeo, ideia): leia o material (link → abra a página; vídeo
→ transcrição; Instagram bloqueia leitura, peça o texto colado) e ache **onde ele encosta na Persona
Profunda**: qual dor, crença, objeção ou desejo do cliente esse tema toca. Tema que não encosta em
nada da persona vira carrossel pra ninguém — diga isso e proponha o ângulo que encosta.

**Se ele não trouxe tema** ("o que eu posto?"): proponha **5 pautas**, cada uma saindo de um lugar
diferente da Persona Profunda:

| Porta | De onde sai | Exemplo de ângulo |
|---|---|---|
| a dor | S4.1 — o que dói | "por que você faz tudo certo e ainda assim…" |
| o pensamento escondido | S5 — o que ele pensa e não fala | dar voz ao que ele tem vergonha de admitir |
| o culpado | S8 — o que ele acha que atrapalha | confirmar ou desmontar o culpado |
| a desculpa | S10 — as objeções | desarmar a desculpa mais comum, sem vender |
| o assunto do momento | S7.2 — tópicos que prendem | o que o público está discutindo agora |

Cada pauta com: o ângulo em uma frase · a porta (e a seção de origem, no arquivo) · a frase literal
do público que prova que a dor existe.

**Parada:** "Qual dessas pautas? Pode juntar duas ou mudar o ângulo."

---

## Etapa 2 — Espinha e capa (parada)

Monte e mostre:

- **A tese:** o que o carrossel defende, em uma frase. Se o aluno disse a opinião dele, é ela —
  nunca amacie.
- **A tensão:** o que está errado, surpreende ou incomoda.
- **O porquê:** a causa real (é aqui que entra o seu método, sem nome de produto).
- **As provas:** 2 ou 3 — dado com fonte, caso real, exemplo específico, a frase do público.
- **A virada:** o que muda pra quem leu.
- **O pedido (CTA):** um só. Opções: salvar, compartilhar, comentar uma palavra, clicar no link da
  bio (pra página ou aula). Pergunte qual, se ele não disse.
- **Quantos slides:** de 6 a 10. Padrão: 8.
- **3 capas** — título (até 12 palavras) + subtítulo (até 18), cada uma com um jeito diferente de
  prender: a frase do público, a contradição, a promessa específica. Nunca descritiva ("5 dicas
  de X"); sempre com ângulo.

**Parada:** "Qual capa? E o caminho está certo ou quer mudar alguma coisa?"

---

## Etapa 3 — Texto (parada)

Escreva o carrossel inteiro em `conteudo/carrosseis/<AAAA-MM-DD>-<tema-curto>/texto.md`:

```markdown
# <título da capa>
**Pauta:** <ângulo> · **Porta:** <S4.1 / S5 / S8 / S10 / S7.2> · **CTA:** <…>
**Tom de voz:** <arquivo usado | ainda não extraído>

## Slide 01 · capa
> <título>
> <subtítulo>
<!-- fonte: S5.2 · "frase literal do banco" -->

## Slide 02 · texto
> <frase principal>
> <desenvolvimento>
<!-- fonte: … -->
…
## Slide 08 · cta
> <frase-ponte>
> <o que ela ganha>
> <AÇÃO>

## Legenda
<gancho nos primeiros 125 caracteres — é o que aparece antes do "mais">
<2 ou 3 parágrafos curtos>
<o mesmo CTA do último slide>
<5 a 10 hashtags do nicho>

## Nota única
- [validar] <todo número, caso ou depoimento não confirmado>
```

O que vai no slide fica nas linhas com `> `. O layout de cada slide (`capa`, `texto`, `numero`,
`lista`, `citacao`, `vs`, `foto`, `cta` — ver `references/layouts.md`) vai no título da seção.

**O caminho:**
- **Slide 1 — capa:** a escolhida na Etapa 2.
- **Slide 2 — o gancho:** a situação ou o dado que cria a tensão, na língua do cliente. Termina
  deixando uma pergunta aberta.
- **Slides do meio — o porquê e as provas:** uma ideia por slide, cada um acrescentando uma camada
  (não repetindo o anterior com outras palavras). Use a `citacao` quando tiver a frase literal do
  público: é o slide que faz a pessoa se reconhecer.
- **Penúltimo — a virada:** o que muda pra quem leu. Não é resumo.
- **Último — o pedido:** frase-ponte que liga o que ela leu à ação, e a ação.

**As regras do texto:**
1. **Uma ideia por slide.** Se precisa de "e também", são dois slides.
2. **A palavra é do cliente.** As palavras de carga vêm da S7.1 e do banco de frases. Termo que o
   seu público não usa (jargão do seu mercado) → troque pelo que ele usa.
3. **Frase de leitura, não de fala.** Carrossel é lido: frases completas, com artigo, que fluem com
   "porque", "só que", "por isso", "então". Duas frases curtas valem mais que uma longa com vírgula.
4. **Cada slide puxa o próximo** pela tensão (uma pergunta aberta, um "mas"), nunca por aviso
   ("continua no próximo", "arrasta pra ver").
5. **Específico ou nada.** Dado vem com fonte e ano; exemplo tem nome e situação. Se trocar o tema
   do carrossel e o texto continuar servindo, está genérico: reescreva.
6. **Nada inventado.** Número, caso, depoimento ou print que não está confirmado vai pra nota
   única como `[validar]`. Citação só com frase literal do banco de frases.
7. **Sem vender produto.** Carrossel é conteúdo: o método aparece, o produto não. A venda, se o CTA
   for pro link, acontece na página.
8. **Sem os vícios de texto de IA:** abertura de apresentação ("hoje vou falar sobre…"), fechamento
   de agradecimento ("espero que tenha ajudado"), frases de efeito vazias ("e isso muda tudo"),
   jargão de palestra ("mindset", "potencializar", "ecossistema").
9. **A voz é a sua.** Com tom de voz: palavras-assinatura entram, palavras-veto nunca, e o texto
   inteiro passa pela régua de 7 notas (§11) — média ≥ 7,5, nenhum eixo abaixo de 6 — antes de
   ser mostrado. A nota fica no `texto.md`, não no chat.

**Meça antes de mostrar:**

```bash
python3 .claude/skills/carrossel/scripts/medir_texto.py conteudo/carrosseis/<pasta>/texto.md
```

Reprovou → corte ou divida o slide e meça de novo.

Mostre no chat o texto de todos os slides e a legenda (não só o caminho do arquivo).

**Parada:** "Esse é o texto. Revisa slide a slide — depois que aprovar, eu passo pro visual e o texto
não muda mais."

---

## Etapa 4 — Visual (parada no slide 1)

Com o texto aprovado e o `marca/DESIGN.md` existindo:

1. Copie `assets/slide-base.html` uma vez, troque os tokens do `:root` pelos do DESIGN.md (cores,
   fontes, caixa do título, raio), o link do Google Fonts e o `--handle`. Esse é o molde deste
   carrossel.
2. Crie um arquivo por slide em `<pasta>/slides/slide-NN.html`, colando o layout de
   `references/layouts.md` que o `texto.md` indica e o texto **exatamente como aprovado**.
3. **Ritmo:** capa e CTA no fundo da marca; no meio, alterne claro e escuro, nunca 3 iguais
   seguidos; o slide da virada muda de fundo. Um grifo por slide no máximo.
4. **Fotos** (opcional): as do aluno vão em `<pasta>/imagens/` e entram pelo layout `foto`.
   Carrossel sem foto funciona — o layout carrega. Nunca use foto de banco que finja ser dele ou
   de aluno.
5. **Renderize só a capa:**
   ```bash
   node .claude/skills/carrossel/scripts/renderizar.cjs conteudo/carrosseis/<pasta> slide-01
   ```
   (Precisa do Playwright: se der "não encontrado", rode uma vez na raiz do Info OS
   `npm install playwright && npx playwright install chromium`.)

**Parada:** mostre o PNG da capa. "Essa é a capa. Gostou do visual? Se sim, eu faço o resto."

Aprovada → renderize todos (sem o segundo argumento). O script avisa texto estourado, fonte que não
carregou e imagem quebrada: corrija e rode de novo até sair "Tudo certo". Olhe os PNGs antes de
entregar. Ajuste pedido num slide → edite só aquele HTML e renderize só ele.

**Versão TikTok** (pergunte no fim): os mesmos slides em 1080×1920. Ajuste no molde `html,body` e
`.slide` pra `height:1920px`, aumente o `padding-bottom` pra 320px (a interface do TikTok cobre a
parte de baixo) e rode com `--tiktok` — os PNGs saem em `png-tiktok/`.

---

## Etapa 5 — Entregar

```
conteudo/carrosseis/<AAAA-MM-DD>-<tema-curto>/
├── texto.md        ← texto aprovado + legenda + nota única
├── imagens/        ← fotos do aluno (se houver)
├── slides/         ← slide-01.html … (editáveis)
├── png/            ← slide-01.png … (pra postar)
└── png-tiktok/     ← se pediu
```

Abra a pasta `png/` (`open` no Mac, `start` no Windows) e diga, curto: quantos slides, a legenda
pronta pra copiar e o que está na nota única pra confirmar antes de postar.

---

## Erros que estragam o carrossel

**Tema que não encosta na persona.** Fica bonito e ninguém se reconhece.

**Parede de texto.** Slide com 80 palavras não é lido. A régua existe por isso.

**Capa descritiva.** "5 dicas de X" não para ninguém. A capa precisa de uma tensão.

**Mexer no texto no visual.** O texto aprovado é o que vai pro slide, palavra por palavra.

**Citação inventada.** Aspas são promessa de que alguém falou aquilo.

**Vender no carrossel.** O conteúdo que vende produto perde o alcance e a confiança que o
conteúdo existe pra construir.
