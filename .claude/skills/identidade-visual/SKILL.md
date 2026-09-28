---
name: identidade-visual
description: Monta a identidade visual da marca do aluno e salva em marca/DESIGN.md — cores com papel (qual é a da marca, qual o destaque, quais os fundos), fontes, botões, cantos, o que nunca pode aparecer, e as regras dos anúncios em vídeo (texto na tela, legenda, tela final, área que o app cobre). É a fonte única de visual que a /design-paginas (página final) e as skills de criativo (edição dos anúncios) consultam — por isso roda DEPOIS do Alicerce do Copy e ANTES da página e dos criativos. Parte do que o aluno já tem (site ou página no ar, prints do Instagram, logo), OU de sites de referência que ele admira e quer usar como base da identidade dele (a skill lê cores, fontes e formas desses sites e adapta pra marca dele), OU, se ele não tem nada, propõe 3 direções a partir da Persona Profunda pra ele escolher. Uma parada (aprovar a prévia visual) e duas entregas — marca/DESIGN.md e marca/preview.html. Use SEMPRE que o usuário disser "identidade visual", "DESIGN.md", "design system", "minhas cores", "minha marca", "paleta", "que fonte eu uso", "a cara da minha marca", "não tenho identidade visual", "monta minha marca", "extrai o visual do meu site", "quero o visual desse site", "copia a identidade desse site", "quero uma marca parecida com essa", "usa esse site de referência", ou quando a /design-paginas ou uma skill de criativo não achar marca/DESIGN.md. NÃO faz logo nem página (→ /design-paginas).
---

# Identidade Visual

O Alicerce do Copy diz **o que** a marca fala. Esta skill decide **como ela aparece** — e grava num
lugar só (`marca/DESIGN.md`) pra que a página e os anúncios pareçam da mesma pessoa. Sem ele, cada
skill inventa um visual, e a pessoa que clica no anúncio chega numa página que parece de outro.

Dois princípios:

- **Registrar antes de inventar.** Se a marca já existe em algum lugar (site, Instagram, logo), o
  trabalho é ler e organizar o que está lá, não redesenhar. Marca que o público já reconhece vale
  mais que marca bonita nova. Se não existe, partir de uma referência que o aluno admira é melhor
  que partir do zero: ele já sabe que gosta.
- **Cada cor tem um papel.** Paleta não é lista de cores favoritas: é qual cor é a da marca, qual
  chama o clique, quais são os fundos. Cor sem papel não entra.

---

## Pra quem é esta skill

Quem usa **não é designer**. Por dentro, rigor total (códigos de cor, contraste medido, tokens com
nome). Por fora, português simples, uma coisa por vez, dizendo **o que está fazendo e por quê**.

| Termo (nos arquivos) | Como falar com o aluno |
|---|---|
| DESIGN.md | o documento da identidade visual da sua marca |
| token | uma cor ou fonte da marca, com nome e papel |
| paleta | as cores da marca |
| hex (#1f3b57) | o código da cor |
| contraste | se o texto dá pra ler em cima daquela cor |
| primary / acento | a cor da marca / a cor do botão e do destaque |
| safe zone | a parte do vídeo que o app não cobre |

---

## Etapa 0 — Conferir e perguntar

Rode na raiz do Info OS:

```bash
find marca infoproduto/alicerce-do-copy -type f 2>/dev/null
```

- **Já existe `marca/DESIGN.md`:** pergunte se é pra **revisar** (ajustar o que existe) ou
  **refazer**. Revisar é o padrão. Refazer → a versão antiga vira `marca/DESIGN-v1.md`.
- **Persona Profunda** (`infoproduto/alicerce-do-copy/persona-profunda/persona-profunda-*.md`):
  recomendada. É dela que sai quem vai ver a marca (S1), em que ela confia e do que desconfia (S9),
  e onde presta atenção (S7). Sem ela, siga, mas a Etapa 2 fica mais pobre — avise numa linha.
- **Tom de voz** (`infoproduto/alicerce-do-copy/tom-de-voz/tom-de-voz-*.md`): se existir, o visual
  conversa com a voz (voz seca e direta não combina com visual fofo).

Depois, **uma mensagem só** perguntando o que ele já tem:

> "Pra montar a identidade da sua marca, eu parto do que você já usa. Me manda o que tiver:
> 1. o link do seu site ou de alguma página sua no ar;
> 2. prints do seu Instagram (o perfil e 2 ou 3 posts que você acha que têm a sua cara);
> 3. o seu logo, se tiver;
> 4. **sites que você admira e queria que a sua marca parecesse** — pode ser de qualquer
>    mercado. Eu leio as cores, as fontes e o jeito deles e adapto pra você;
> 5. em 3 palavras, como a sua marca deve parecer;
> 6. alguma cor, fonte ou estilo que você NÃO quer de jeito nenhum.
> Não tem nada disso? Tudo bem — me responde só a 5 e a 6 que eu te proponho 3 caminhos."

---

## Etapa 1 — Ler o que existe

**Site ou página no ar** — o script lê as cores e as fontes que o site usa de verdade:

```bash
python3 .claude/skills/identidade-visual/scripts/extrair_site.py <url> --saida marca/_leitura-site.json
```

(No Windows, `python` no lugar de `python3`.) A cor que aparece muitas vezes é a da marca; a que
aparece uma vez é detalhe. Site montado todo por JavaScript volta quase vazio — aí vá pelos prints.
O Instagram bloqueia leitura direta: sempre por print.

**Prints e logo** — olhe cada imagem e anote as cores dominantes, a de destaque e o tipo de letra.
Cor tirada de print é aproximada (a tela e a compressão mexem nela): marque no DESIGN.md como
`# estimada do print` e peça confirmação. Se ele tiver o código exato (do Canva, do designer),
vale o código dele.

**Sites de referência** (os que ele admira) — o mesmo script, um por site:

```bash
python3 .claude/skills/identidade-visual/scripts/extrair_site.py <url-da-referencia> --saida marca/_referencia-<nome>.json
```

Além do script, abra a página e olhe como ela usa o que o script achou: qual cor está no fundo do
topo, qual está no botão, se os títulos são em caixa alta, se tem borda ou sombra, cantos redondos
ou retos, como são as fotos. O script dá os códigos; o olhar dá os papéis. Se a página não abrir
(site por JavaScript, bloqueio), peça um print inteiro dela.

**Não tem nada** — pule pra Etapa 2 com as 3 direções.

**Escreva no rascunho** (`marca/_leitura.md`, arquivo de trabalho) o que achou, com a fonte de cada
coisa: `#1d4d2e — site, 120×, fundo do topo` · `#d4a647 — print do post 2, botão`.

---

## Etapa 2 — Decidir o sistema

### Se a marca já existe
Organize o que achou em papéis — não troque cor que o público já reconhece. Complete só o que
falta (ex.: tinha cor da marca e não tinha destaque) e diga o porquê de cada complemento.

### Se veio de site de referência
Pegue o **sistema** da referência — a paleta com os papéis, o par de fontes, as formas, o jeito das
fotos e dos fundos — e vista a marca dele com isso. Regras:

- **O que se leva:** cores, papéis das cores, tipo de fonte, cantos, bordas, ritmo de fundos,
  tratamento de foto. Isso é estilo, e estilo não tem dono.
- **O que NUNCA se leva:** logo, nome, ilustração, foto, ícone desenhado sob medida, textos e
  qualquer elemento que identifique a outra marca. A pessoa que conhece a referência tem que achar
  "parecido", nunca "é a mesma empresa".
- **Fonte paga ou exclusiva** (a referência usa uma fonte própria, que não está no Google Fonts):
  troque pela gratuita mais próxima e diga qual trocou por qual.
- **Mais de uma referência:** pergunte qual é a base e o que ele quer de cada uma ("as cores deste,
  as fontes daquele"). Sem resposta, a base é a primeira e as outras só complementam o que falta.
- **Ele já tem marca e mandou referência:** as cores dele ficam (o público já reconhece) e a
  referência entra nas fontes, formas e ritmo — a não ser que ele diga que quer trocar tudo.
- **Adaptar ao público dele:** se a referência é de outro mercado, confira com a Persona Profunda.
  Visual de marca de moda pode passar futilidade pra um público que desconfia de promessa fácil —
  avise e sugira o ajuste, mas a decisão é dele.
- **Contraste:** a referência pode ter combinação que reprova na medição. Corrija na marca dele.

Na seção 8 do DESIGN.md ("De onde veio"), registre cada referência com a URL e o que foi tirado
dela.

### Se não existe nada — 3 direções
Proponha **3 direções** diferentes entre si, cada uma amarrada à persona e às 3 palavras dele:

- **Nome curto** da direção + a frase de por que ela fala com esse público (fonte: S1, S7, S9).
- Paleta com papéis, par de fontes, jeito do botão e dos cantos.

Ex.: pra um público que desconfia de promessa fácil (S9.2), uma direção sóbria e "de ofício" tende
a passar mais confiança que uma colorida de guru. A decisão é do aluno.

### O que o sistema precisa ter (nas duas situações)

**Cores — um papel por cor:**

| Papel | Pra quê |
|---|---|
| `marca` (primary) | a cor que as pessoas associam a você: topo da página, tela final do anúncio |
| `marca-2` | escura alternativa: dobra de compra, rodapé |
| `acento` | o destaque: botão, grifo, número grande, selo — **uma cor só** |
| `claro` / `claro-2` | fundos de leitura, alternados |
| `texto` / `apagado` | texto corrido e texto secundário |
| `alerta` (opcional) | o ✕ do "antes", erro |

**Contraste medido, não no olho.** Texto sobre fundo precisa de contraste de pelo menos 4,5 (texto
comum) e 3 (título grande e botão). Meça as combinações que vão existir — texto em `claro`, texto
claro em `marca`, texto do botão em `acento`:

```bash
python3 -c "
def l(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
import sys
a,b=sys.argv[1],sys.argv[2]; x,y=sorted([l(a),l(b)],reverse=True)
print(f'{a} × {b}: {(x+.05)/(y+.05):.2f}')
" "#1b1b1b" "#f3eee4"
```

Combinação reprovada: escureça ou clareie a cor do texto, não a da marca.

**Fontes — do Google Fonts** (gratuitas, funcionam na página e no editor de vídeo):
- **título** — com personalidade; se for condensada, em caixa alta;
- **texto** — legível em tamanho pequeno;
- **rótulo** (opcional) — pra etiquetas e botões, costuma ser uma mono.
Evite as genéricas (Inter, Roboto, Arial, Poppins) como fonte de título: deixam a marca igual a
todo mundo. A marca é dele — se ele insistir, vale a dele.

**Formas:** raio dos cards e fotos, raio do botão (pílula ou retangular), borda ou sem borda, com
sombra ou plano, com gradiente ou sem.

**Anúncios em vídeo** — é aqui que o criativo e a página ficam parecidos:
- **Texto na tela (gancho):** fonte de título, caixa, cor, e como fica legível em cima de vídeo
  (tarja na cor `acento`, contorno ou sombra).
- **Legenda:** fonte de texto, cor, tamanho relativo, posição.
- **Tela final / convite:** fundo `marca`, texto `claro`, seta ou destaque em `acento`.
- **Área livre:** a interface do Reels e do Stories cobre cerca de 14% em cima e 35% embaixo —
  texto importante fica fora dessas faixas.
- **Preço na tela** (só ultra low ticket): tamanho e cor.

**Nunca:** a lista do que a marca proíbe (o que ele pediu na pergunta 5 + o que o sistema decidiu:
"sem sombra", "sem gradiente", "`acento` nunca vira fundo de dobra inteira").

---

## Etapa 3 — Prévia e aprovação (a única parada)

Copie `assets/preview-base.html` para `marca/preview.html`, troque os valores do `:root`, o link de
fontes e os textos [entre colchetes] por frases reais (a headline pode sair da Persona Profunda; o
CTA, do que ele vende). **Se forem 3 direções, gere 3 prévias** (`marca/preview-a.html`, `-b`, `-c`).

Abra no navegador (`open` no Mac, `start "" "<arquivo>"` no Windows) e mostre em chat, curto:
as cores com o papel de cada uma, as fontes, o que ficou de fora e por quê, e as combinações de
contraste medidas. Pergunte:

> "É essa a cara da sua marca? Pode mudar qualquer cor ou fonte — me diz o que e eu ajusto a prévia."

Ajuste até ele aprovar. Com 3 direções, ele escolhe uma (ou mistura) e as outras prévias são apagadas.

---

## Etapa 4 — Escrever o marca/DESIGN.md

Formato: cabeçalho YAML com os tokens (é o que as outras skills leem) e o texto explicando como usar.

```markdown
---
name: "<marca>"
colors:
  marca: "#1f3b57"        # primary — de onde veio (site 120× / print / escolhida)
  marca-2: "#16293d"
  acento: "#e0a93b"
  claro: "#f3eee4"
  claro-2: "#fbf8f2"
  texto: "#1b1b1b"
  apagado: "#5d6b75"
typography:
  titulo: { fontFamily: "Anton", caixa: "alta", lineHeight: 1.04 }
  texto: { fontFamily: "DM Sans", tamanhoBase: "17px", lineHeight: 1.6 }
  rotulo: { fontFamily: "DM Mono", caixa: "alta", letterSpacing: "0.15em" }
rounded: { card: "12px", botao: "999px" }
---

## 1. Atmosfera
Em 3 a 5 linhas: como a marca deve parecer e por quê (a quem ela fala, do que esse público desconfia).

## 2. Cores e papéis
Tabela: token · código · papel · onde usa · onde NUNCA usa. + contrastes medidos.

## 3. Fontes
Qual é pra quê, tamanhos de referência, caixa, link do Google Fonts.

## 4. Componentes
Botão (principal, em fundo claro, secundário), card, foto (tratamento), selo/grifo se houver.

## 5. Página
Fundo do topo, alternância de fundos, dobra de compra, tratamento de foto.

## 6. Anúncios em vídeo
Texto na tela, legenda, tela final, área livre, preço na tela (se ultra low).

## 7. Nunca
A lista do que a marca proíbe.

## 8. De onde veio
Fontes da leitura (site, prints, sites de referência com URL e o que foi tirado de cada um,
escolhas do aluno) e data.
```

Apague os arquivos de trabalho (`marca/_leitura.md`, `marca/_leitura-site.json`,
`marca/_referencia-*.json`) só depois de o
DESIGN.md registrar a origem de cada cor na seção 8.

---

## Etapa 5 — Entregar

Mensagem curta:
1. **A marca em uma frase** e onde estão os dois arquivos (`marca/DESIGN.md` e `marca/preview.html`).
2. **O que ficou pra confirmar** — cor estimada de print, fonte que ele não tem certeza.
3. **O que usa isso daqui pra frente:** "A `/design-paginas` veste a sua página com essa identidade,
   e as skills de criativo usam as regras de vídeo nas instruções de edição. Mudou a marca? Roda
   esta skill de novo e tudo que vier depois já sai com a versão nova."

---

## Erros que estragam a identidade

**Levar a marca junto com o estilo.** Logo, ilustração exclusiva ou foto de referência na marca do
aluno é cópia, e pode dar problema. Da referência vem o sistema, não os elementos.

**Redesenhar marca que já existe.** O público reconhece a cor de sempre; trocar sem motivo custa
reconhecimento.

**Duas cores de destaque.** Se botão e grifo têm cores diferentes, nenhum dos dois chama o clique.

**Contraste no olho.** Mostarda em creme parece legível no monitor e some no celular no sol.

**Cor de print tratada como exata.** Marque como estimada e peça o código.

**Esquecer o vídeo.** Identidade que só serve pra página faz o anúncio parecer de outra marca.
