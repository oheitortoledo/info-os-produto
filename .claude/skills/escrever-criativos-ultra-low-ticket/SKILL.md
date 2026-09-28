---
name: escrever-criativos-ultra-low-ticket
description: Escreve um pack de 12 anúncios em vídeo (roteiros prontos pra gravar e editar) para produto ULTRA LOW TICKET, até R$ 10, vendido direto na página (anúncio → página de vendas → checkout). Cinco etapas com parada entre cada uma — mercado e formato (anúncios dos concorrentes + catálogo de 50 formatos) → pessoas (Persona Profunda) → 28 ganchos pra você escolher → roteiros → checagem final contra a página — e entrega tudo num arquivo em infoproduto/criativos/packs/. Use SEMPRE que o usuário disser "anúncio", "criativo", "roteiro de anúncio", "gancho", "pack de criativos", "próximo pack", "lote de anúncios", "vídeo pra tráfego pago", "anúncio de 7 reais", "produto de 7/9/10 reais", "ultra low ticket", "front barato", ou quando o destino do clique for uma página com checkout e o preço for até R$ 10. Precisa do Alicerce do Copy (sem ele, manda rodar /alicerce-copy). Acima de R$ 10 → escrever-criativos-low-ticket; aula ou VSL gratuita → escrever-criativos-vsl; lançamento: em breve. NÃO sobe campanha.
---

# Escrever criativos — Ultra Low Ticket (até R$ 10)

**O macro está na base compartilhada.** Leia antes de começar, nesta ordem:

1. `.claude/skills/_base-criativos/PROCESSO.md` — o que conferir antes, as 5 etapas, as paradas, o arquivo do pack
2. `.claude/skills/_base-criativos/REGRAS-ESCRITA.md` — a régua de toda fala, o tom de voz e a medição em código
3. `.claude/skills/_base-criativos/MODELO-ENTREGA.md` — como o pack fica escrito
4. `.claude/skills/_base-criativos/ANGULOS.md` — os 17 ângulos
5. `.claude/skills/_base-criativos/formatos/README.md` — o catálogo (fichas sob demanda)
6. `.claude/skills/_base-criativos/NOMENCLATURA.md` — o nome de cada criativo

Este arquivo só traz **o que é próprio do ultra low ticket**. Onde contradiz a base, vale este.
Todos os caminhos são relativos à raiz do Info OS.

---

## Pra quem é esta skill (vale pra sessão inteira)

Quem usa **não é copywriter nem gestor de tráfego**. É o especialista montando o próprio produto e
aprendendo o método agora. Duas regras:

1. **Por dentro, rigor total.** Os códigos (S4.1, P2, H07, [CPA], [PACK], [HIPÓTESE]), a régua de
   escrita, a medição em código, a nota única `[validar]` — tudo fica nos arquivos, nada afrouxado.
2. **Por fora, português simples.** No chat, trate por "você", uma coisa por vez, e diga em uma
   frase **o que está fazendo e por quê**. Palavra técnica só com tradução, na primeira vez que
   aparecer:

| Termo (nos arquivos) | Como explicar na primeira vez |
|---|---|
| criativo | cada anúncio (vídeo ou imagem) |
| pack | o lote de 12 anúncios que você grava de uma vez |
| gancho | os 3 primeiros segundos: a frase e a imagem que fazem a pessoa parar de rolar |
| ângulo | a porta de entrada do argumento (um erro, um segredo, uma promessa…) |
| formato | a "embalagem" do vídeo (caixinha de pergunta, tela dividida, fala enquanto faz…) |
| CTA | o pedido de clique no fim ("clica em Saiba Mais") |
| message match | o anúncio promete exatamente o que a página mostra logo que abre |
| primeira dobra | o que aparece na página antes de rolar |
| portão | a checagem final antes de ir pra gravação |
| UGC | vídeo com cara de gravado por um cliente comum, não por marca |
| POV | "ponto de vista": o vídeo mostra a cena como se fosse você vivendo |
| CPA | quanto custou, em anúncio, cada venda |
| Persona Profunda | o retrato completo do seu cliente (do seu Alicerce do Copy) |
| subpersona / S11 | os tipos de cliente que você tem |
| verbatim | a frase exata que seu cliente usa |

---

## Status das regras deste funil — leia antes de usar

**Não existe manual de copy consagrado pra ultra low ticket.** As regras abaixo foram montadas a
partir de evidência real, e cada uma diz de onde veio:

- **[CPA]** — medido em anúncios que rodaram, com custo por compra: os 10 criativos de maior
  investimento de um produto de culinária vendido a R$ 7 (ago/2026). É evidência de UM produto,
  UMA pessoa gravando e UM preço — e a venda foi atribuída pela própria Meta. Serve de ponto de
  partida, não de lei pro seu nicho.
- **[PACK]** — prática observada num pack real de 10 peças escrito pra esse mesmo produto. É
  escolha de quem escreveu, **ainda sem resultado lido**.
- **[HIPÓTESE]** — raciocínio, sem dado. Serve pra testar, não pra travar.

Regra marcada [HIPÓTESE] nunca é usada pra reprovar gancho do usuário. Ao fim de cada pack que
rodar, o resultado por criativo volta pro **Registro de calibração** no fim deste arquivo: regra
que se confirmou no nicho dele sobe de nível, regra que falhou sai.

---

## LEI MÁXIMA — todo criativo de ultra low ticket

1. **O destino é a página de vendas com checkout.** Nunca aula, grupo ou isca gratuita.
2. **O preço aparece em toda peça, por extenso na fala e grande na tela.** [CPA: preço no gancho
   em 10/10 dos criativos que mais gastaram, incluindo o de melhor CPA] [PACK: 9/10 — uma peça não diz preço]
3. **O CTA nomeia o botão real do anúncio** ("clica em Saiba Mais"). [CPA: 9/10] [PACK: 9/10 — uma peça diz "clica no link"]
4. **A promessa e o preço do anúncio estão na primeira dobra da página.** Se a pessoa precisa
   rolar pra achar o preço que viu no vídeo, o clique morre.

Peça que viola qualquer um dos quatro volta antes de chegar ao usuário.

---

## O que muda no processo

### Antes da etapa 1 — conferir e perguntar o que faltar
Primeiro rode a conferência de `PROCESSO.md` (alicerce, página, biblioteca, tom de voz,
nomenclatura). Sem Persona Profunda, **pare** e mande rodar `/alicerce-copy`. Depois pergunte,
numa mensagem só, só o que os arquivos não responderam:

- **Produto e página de destino.** Leia a `pagina.html` da `/pagina-de-vendas`
  (`infoproduto/funil/pagina-de-vendas/<produto>*/pagina.html`) e/ou a URL no ar: headline, preço,
  o que aparece antes de rolar, o rodapé legal. Sem página, não há message match — pare e peça
  (ou sugira `/pagina-de-vendas`).
- **Preço ou preços em teste** (ex.: 7/9/10). Vira a regra de GRAVAÇÃO do pack.
- **Número do pack e último `NUM` da oferta** — em `infoproduto/criativos/nomenclatura.md`. O pack
  continua a sequência; nunca recomeça do `001`. Primeiro pack e sem arquivo → ajude a escolher o
  código de 3 letras (`NOMENCLATURA.md`) e crie o arquivo.
- **Tamanho do pack: sempre 12** (4 pessoas × 3 criativos — regra da base). No ultra low, o volume
  de criativo novo costuma ser o gargalo: uma referência de tráfego usada na prática pede em torno
  de 20 criativos novos por semana nesse tipo de oferta. Diga isso como referência, não como
  obrigação: "este pack tem 12; se a sua campanha pedir mais volume, o próximo pack cobre".
- **Quem grava e com o quê.** No ultra low o volume é a regra mais cara de cumprir: prefira
  formatos de dificuldade 1–2 que você grava sozinho, do celular.

### Etapa 1 · Mercado e formato — o que olhar a mais
- **O próprio histórico pesa mais que o mercado.** No ultra low quase ninguém do nicho vende a
  R$ 10, então a biblioteca de concorrentes costuma ter pouco comparável (no caso observado, 1
  anunciante de 8 tinha oferta parecida). Se o usuário já anunciou, os anúncios dele com CPA são a
  primeira fonte; a biblioteca, a segunda. Se nunca anunciou, a biblioteca é a fonte, e isso fica
  declarado.
- **Os esqueletos de gancho que rodaram no caso observado** (use como hipótese de partida, com as
  palavras do nicho do usuário): preço-primeiro ("R$ 7 é o preço do meu curso de…", o de melhor
  CPA), acusação de golpe ("tem gente falando que meu curso de 7 reais é golpe", CPA entre 1,3× e
  2,3× o melhor) e pergunta de seguidor em caixinha (CPA cerca de 1,7× o melhor). [CPA]
- **Formatos de ação contínua funcionaram aqui**: 5 dos 10 criativos observados são fala durante
  uma tarefa, e o de melhor CPA é a especialista fazendo a tarefa do próprio curso enquanto fala.
  [CPA] → no catálogo: Fala e Faz (F13), Trivial (F44).

### Etapa 2 · Pessoas — o recorte do ultra low
A pessoa do ultra low não está decidindo se o problema vale a pena resolver; está decidindo se
**vale arriscar R$ 7 pra ver**. Pra cada ficha de pessoa, acrescente:
- **O "por que não" dela a R$ 7** — quase sempre desconfiança do barato ("é golpe", "vai ser
  coisa básica", "o que dá pra ensinar por sete reais?"). Procure na S10 (objeções) e no banco de
  frases. No caso observado, 5 dos 10 criativos que mais gastaram abrem justamente respondendo à
  acusação de golpe. [CPA]
- **Com o que ela compara os R$ 7** — o objeto do dia a dia que vira âncora (o refrigerante no
  restaurante, o café, o lanche). [PACK: 3 peças]

### Etapa 3 · Ganchos — regras próprias
- **O preço é a notícia.** No ultra low, o preço baixo é o fato mais surpreendente do anúncio, e
  por isso pode abrir a peça — ao contrário do low ticket, onde preço na abertura vira promoção.
  Os três esqueletos observados colocam o preço em jogo nos primeiros segundos; o que varia é QUEM
  põe: o próprio especialista, terceiros acusando, ou um seguidor perguntando. [CPA]
- **Divida a bateria**: pelo menos metade dos ganchos com o preço na primeira frase; o resto abre
  por dor, desejo ou curiosidade e traz o preço no corpo. Nenhum gancho observado que rodou abria
  sem preço — a outra metade é justamente o teste que falta. [HIPÓTESE]
- **Preço escrito no frame 0** quando o gancho abre com preço: o único criativo observado com o
  preço fixo na tela desde o primeiro segundo é o de melhor CPA. [CPA — 1 peça, sinal fraco]

### Etapa 4 · Roteiros — regras próprias
- **Toda peça desarma a desconfiança do barato uma vez**, com UMA destas: a razão do preço
  ("eu quero que o máximo de gente possível aprenda isso"), o conteúdo concreto que a pessoa leva
  (módulos e entregas com nome, não "vários conteúdos"), ou prova de aluno. [CPA: razão do preço em
  5/10, incluindo o melhor CPA; prova de aluno em 6/10] [PACK: 2 peças]
- **O que a pessoa leva é dito com nome.** Três entregas concretas e nomeadas vendem mais que a
  categoria genérica ("entrada, prato e sobremesa", "várias planilhas"). [PACK: 2 peças —
  HIPÓTESE quanto a resultado]
- **Âncora de preço** com um objeto do cotidiano é bem-vinda ("é menos que um refrigerante no
  restaurante"); âncora de preço cheio inventada ("custava R$ 397") só com o preço cheio real e
  declarado na página. [PACK]
- **Curto.** Alvo de 25 a 45 segundos de fala. O melhor CPA observado tem 36s; o que mais explica e
  menos pressiona (45s, sem urgência, sem prova) teve o pior retorno. [CPA — correlação, não causa]
- **Motivo de agora** (por que comprar hoje) está em 8/10 dos criativos observados, sempre como
  incerteza ("não sei por quanto tempo vai estar nesse preço") ou subida de preço. Use **só se for
  verdade** — num teste de preço 7/9/10, o preço de fato muda. Prazo inventado vai pra nota única
  como `[validar]`. [CPA + PACK]
- **Desqualificador leve.** Ao contrário do low ticket, clique errado a R$ 7 custa pouco; basta a
  peça falar com quem já faz a coisa. Não gaste frase dizendo pra quem não é. [HIPÓTESE]
- **A voz é a sua.** Se existe o documento de tom de voz, a fala do especialista usa as suas
  palavras-assinatura, evita as proibidas e passa pela régua de 7 notas (§11) — ver
  `REGRAS-ESCRITA.md`. Ultra low é impulso: soar como você (e não como "anúncio") é parte do que
  desarma a desconfiança. [HIPÓTESE]

### Etapa 5 · Portão — itens a mais
- [ ] Preço em toda peça, por extenso na fala e com a regra de edição "preço grande na tela".
- [ ] Se há teste de preço, o pack traz nas INSTRUÇÕES a regra de gravação ("só a frase do valor,
      em N valores") e as peças escrevem o preço como `7/9/10 reais`.
- [ ] Faixa de preço fixa (ex.: "7 Reais essa semana"), quando usada, está nas OBSERVAÇÕES com as
      N variações escritas.
- [ ] Toda urgência é verdadeira ou está na nota única.
- [ ] A página mostra o mesmo preço do anúncio na primeira dobra — pra cada variação de preço
      testada, existe a página correspondente (ex.: `/7`, `/9`, `/10`). Se não existir, diga em
      vermelho no topo da nota: **sem a página do preço, o criativo daquele preço não pode rodar.**
- [ ] O rodapé da página tem a identificação de quem vende (CNPJ e razão social, ou os dados que a
      sua plataforma de venda exige) e um contato — página sem isso costuma ter anúncio reprovado
      na Meta. No wireframe da `/pagina-de-vendas`, é a `.nota` do rodapé: se ainda está como
      pendência, entra na nota única.
- [ ] Toda peça tem nome no padrão `[OFERTA]_Pack[N]_[FORMATO]_[NUM]`, sem número repetido; cada
      troca de preço é `_V1`, `_V2`… do mesmo número, com o preço de cada versão nas OBSERVAÇÕES.
      Ao fechar, atualizar o último `NUM` em `infoproduto/criativos/nomenclatura.md`.
- [ ] 12 roteiros = 4 pessoas × 3, com formato e ângulo distintos dentro de cada pessoa.

---

## Registro de calibração — o seu

Aqui você registra o que aprendeu com os seus packs. É isto que transforma as regras acima de
"funcionou num produto de culinária" em "funciona no **meu** nicho".

**Como ler o resultado:** depois de 3 a 7 dias no ar, abra o Gerenciador de Anúncios, filtre pelo
pack (o nome de cada anúncio é o nome do criativo) e anote por criativo: gasto, compras e custo
por compra. Cruze com o bastidor do pack (pessoa · ângulo · formato · gancho) pra ver o que se
repete nos que venderam mais barato. Uma peça só é sinal fraco; o mesmo padrão em 3+ peças é
sinal de verdade.

**Como registrar:** uma linha por mudança — data · regra · o que mudou (subiu de nível, caiu,
nova) · fonte (qual pack, quais criativos, quantas vendas).

| Data | Regra | O que mudou | Fonte |
|---|---|---|---|
| | | | |
