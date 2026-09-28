# Layouts de slide

Cada slide usa **um** layout. Cole o bloco no `<body>` do `assets/slide-base.html`. Troque os
textos entre colchetes e o contador (`03/08`).

**Fundo:** `escuro` · `escuro-2` · `claro` · `claro-2` — a classe vai no `<section>`, junto com a do
layout. Regra de ritmo: capa e CTA no fundo da marca (`escuro`); no meio, alterne claro e escuro, e
nunca 3 slides seguidos com o mesmo fundo. O slide que carrega a virada muda de fundo — a mudança
avisa o olho que algo mudou.

**Grifo** (`<span class="hl">`): no máximo um por slide, nas 2 a 4 palavras que carregam a ideia.

---

## capa — só no slide 1

```html
<section class="slide capa escuro">
  <p class="rot">[rótulo: o assunto em 2 palavras]</p>
  <h1 class="mt">[Título com <span class="hl">a parte que prende</span>]</h1>
  <p class="sub">[Subtítulo que abre a curiosidade]</p>
  <span class="seta">ARRASTA →</span>
  <div class="rodape"><span class="h"></span><span>01/08</span></div>
</section>
```

## texto — o layout de trabalho (um parágrafo, uma ideia)

```html
<section class="slide claro">
  <p class="rot">[rótulo opcional]</p>
  <h2 class="mt">[Frase principal do slide]</h2>
  <p class="mt">[Desenvolvimento em 1 a 3 frases.]</p>
  <div class="rodape"><span class="h"></span><span>02/08</span></div>
</section>
```

## numero — quando o slide é um dado

```html
<section class="slide escuro">
  <div class="num">[73%]</div>
  <h2 class="mt">[O que esse número quer dizer]</h2>
  <p class="mt">[Fonte, ano — ou de onde veio.]</p>
  <div class="rodape"><span class="h"></span><span>03/08</span></div>
</section>
```

## lista — no máximo 4 itens, cada um com 1 linha

```html
<section class="slide claro-2">
  <h2>[Título da lista]</h2>
  <ul class="lista">
    <li><span class="n">01</span>[Item]</li>
    <li><span class="n">02</span>[Item]</li>
    <li><span class="n">03</span>[Item]</li>
  </ul>
  <div class="rodape"><span class="h"></span><span>04/08</span></div>
</section>
```

## citacao — a frase exata do público (do banco de frases)

```html
<section class="slide citacao escuro-2">
  <blockquote>"[Frase literal do seu cliente]"</blockquote>
  <p class="quem">[quem fala assim — ex.: aluna, 34 anos, 2 filhos]</p>
  <div class="rodape"><span class="h"></span><span>05/08</span></div>
</section>
```

Frase inventada nunca vai numa citação: se não é literal do banco de frases, use o layout `texto`.

## vs — o jeito comum × o seu jeito

```html
<section class="slide claro">
  <h2>[Título da comparação]</h2>
  <div class="vs">
    <div class="a"><span class="rot">[Do jeito comum]</span><p>[como a maioria faz]</p></div>
    <div class="b"><span class="rot">[Do seu jeito]</span><p>[como você ensina]</p></div>
  </div>
  <div class="rodape"><span class="h"></span><span>06/08</span></div>
</section>
```

## foto — foto sua de fundo, texto embaixo

```html
<section class="slide com-foto escuro">
  <div class="foto" style="background-image:url('../imagens/[arquivo].jpg')"></div>
  <h2>[Frase curta]</h2>
  <p class="mt">[1 frase, opcional]</p>
  <div class="rodape"><span class="h"></span><span>07/08</span></div>
</section>
```

A sombra de baixo pra cima (`.foto::after`) garante leitura do texto. Se o `marca/DESIGN.md` proíbe
gradiente, troque por uma tarja sólida: `.com-foto h2{background:var(--marca-2);padding:12px 20px}`
no `slide-base.html` do carrossel.

## cta — só no último slide

```html
<section class="slide cta escuro">
  <h2>[Frase-ponte: liga o que a pessoa acabou de ler com a ação]</h2>
  <p class="mt">[O que ela ganha fazendo isso.]</p>
  <span class="botao">[AÇÃO — ex.: COMENTA "PLANO"]</span>
  <div class="rodape"><span class="h"></span><span>08/08</span></div>
</section>
```
