# Templates exatos dos dois documentos

Moldes de **dados brutos** (ver a REGRA-MÃE na SKILL.md: zero recomendação). O conteúdo entre `[...]` é placeholder. Adaptar os **grupos de vértice** ao nicho. Nada de leitura estratégica, oportunidades, SWOT ou matriz.

Os dois documentos abrem com a mesma **legenda de termos** — quem vai ler é especialista no assunto dele, não em marketing. Manter a legenda curta; tirar dela os termos que não aparecem no documento.

---

## Bloco comum — legenda de termos (vai logo abaixo do header de cada documento)

```markdown
<details open><summary><b>Legenda — o que cada termo quer dizer</b></summary>

- **Ticket** — preço do produto.
- **Esteira** — a lista de produtos que o concorrente vende, do mais barato ao mais caro.
- **Tripwire / produto de entrada** — produto barato que serve de porta de entrada.
- **High-ticket** — produto caro (mentoria, acompanhamento, grupo fechado).
- **Promessa / big idea** — a frase principal que o concorrente usa pra vender, copiada da página.
- **Vértice** — o tipo de promessa que ele vende. "Mesmo vértice" = vende a mesma coisa que você, pro mesmo público.
- **Funil** — o caminho que o cliente faz até comprar (ex: vídeo no Instagram → aula grátis → página de vendas → pagamento).
- **Landing / página de vendas** — página que apresenta e vende o produto.
- **Checkout** — página de pagamento.
- **Lead** — contato de quem deixou nome/e-mail/WhatsApp.
- **Upsell / order bump / OTO** — oferta extra na hora ou logo depois da compra.
- **Perpétuo / lançamento** — vende o ano todo / vende só em datas específicas.
- **Ancoragem** — o preço "de" riscado ao lado do preço "por".
- **`confirmado`** — preço lido numa página ou checkout no ar (com link). **`não público`** — o produto existe, mas o preço fica atrás de conversa, WhatsApp, lançamento ou página que não carrega sem navegador. **`não varrido`** — não foi coletado nesta rodada.

</details>
```

---

## TEMPLATE 1 — `mapa-concorrentes.md`

```markdown
# Mapa de Concorrentes — [Nicho]
> Produto · Promessa · Ticket · Atualizado [mês/ano] ([N]ª varredura)
> **DADOS BRUTOS para análise** — sem recomendação, sem interpretação, sem posicionamento. Só o que cada concorrente é, vende e cobra. Cada dado leva o link de onde saiu.

[LEGENDA DE TERMOS — bloco comum acima]

**Agrupamento por vértice** (o que o player *vende*, descritivo — não é ranking de ameaça):
- 🔴 **[Vértice A — mesmo vértice]** — [descrição do que vende]
- 🟡 **[Vértice B — adjacente]** — [...]
- 🟢 **Genéricos** — [não específico do público / ferramenta]
- ⚪ **Sem produto** — audiência no tema, sem oferta paga identificada

---

## [VÉRTICE A — o que vende]

### [Expert] — [Marca/Produto]
*[@handle](https://www.instagram.com/handle/) · [audiência] · [credencial factual curta]*
| Produto | Promessa | Ticket |
|---|---|---|
| [[Produto](https://url-da-pagina-do-produto) (o que inclui em 1 linha)] | "[big idea literal entre aspas]" | **R$X** (12x R$Y) (confirmado · [nome curto da fonte](https://url-completa-da-pagina)) |
| [[Produto 2](https://url)] | "[promessa]" | **não público** ([motivo: aplicação/WhatsApp/JS]) |

**Funil:** [captação → conversão, factual, com links]

[... repetir players do vértice ...]

### Cauda longa — [vértice] (passe raso)
| Concorrente | Produto | Promessa | Ticket |
|---|---|---|---|
| **[Nome]** ([@handle](https://www.instagram.com/handle/)) | [[produto](https://url)] | "[promessa]" | **não varrido** (Hotmart — pendência) |

---

## GENÉRICOS / FERRAMENTA (não específico do público)
| Concorrente | Produto | Nicho | Ticket |
|---|---|---|---|
| **[Nome]** | [[produto](https://url)] | [nicho genérico] | [ticket + fonte] |

---

## SEM PRODUTO — audiência no tema, sem oferta paga identificada
| Perfil | Audiência | Ângulo | Produto |
|---|---|---|---|
| **[Nome]** ([@handle](https://www.instagram.com/handle/)) | [audiência] | "[ângulo de conteúdo]" | nenhum identificado |

---

## MAPA DE PREÇOS — só o que foi confirmado em fonte viva
Ordenar por valor. Só entra o que foi lido numa página/checkout no ar (com fonte **clicável**).

| Player | Produto | Ticket confirmado | Fonte |
|---|---|---|---|
| [Player] | [produto] | R$X (12x R$Y) | [dominio.com/slug-da-pagina](https://dominio.com/slug-da-pagina) |

**Faixas (fatos):** entrada R$[X–Y] · principal R$[X–Y] · high-ticket R$[X+] · recorrência R$[X]/mês.

---

## PENDÊNCIAS DE COLETA
- [ ] **Atrás de aplicação/WhatsApp/lançamento:** [players] — fechar entrando como lead.
- [ ] **Não varridos nesta rodada:** [players] — abrir site/checkout/Hotmart.
- [ ] **Checkout Hotmart/Kiwify por JavaScript** (preço existe, não carrega sem navegador): [players + link do checkout] — abrir num navegador.
- [ ] **Biblioteca de Anúncios da Meta** (bloqueou leitura automática): [players + link da busca pronto] — abrir manual.
- [ ] **Reclame Aqui** (403): [players] — abrir manual.
- [ ] **Ferramentas que faltaram nesta rodada:** [ex: yt-dlp ausente — descrições de vídeo coletadas parcialmente via WebFetch].
- [ ] **Correções de dado:** [falsos positivos removidos, preços corrigidos, players fundidos].
```

**Notas de preenchimento do mapa:**
- **SEMPRE linkar o @ do Instagram** como `[@handle](https://www.instagram.com/handle/)` — na linha sob o `###` e dentro da célula do nome nas tabelas compactas. Handle não confirmado → `@?` + pendência (não inventar).
- **Todo ticket confirmado carrega a fonte, e a fonte é SEMPRE um link clicável** — markdown `[texto](https://url-completa)`, nunca URL solta nem caminho relativo (`/oferta/`, `home`, `descrição de vídeo`). Quem lê clica pra conferir; fonte não clicável é dado morto.
  - **A URL é a página exata onde o número foi lido**, não a home do domínio.
  - **Texto do link:** o slug legível (`dominio.com.br/oferta/`) ou o nome curto da página (`página de oferta R$297`). Nunca "aqui", "link", "fonte".
  - **Vale pra TODA fonte de dado**, não só preço: promessa literal, garantia, número de alunos, checkout, matéria, ficha de app.
  - **Checkout também é fonte clicável:** `[pay.hotmart.com/K00000000X](https://pay.hotmart.com/K00000000X)`.
  - **Sem URL pública?** Então é `não público` / `não varrido` + pendência. Nunca um número solto e nunca um link inventado.
  - **Produto sem preço também leva link** — é por ele que a pendência se fecha.
- Marcar `*(novo)*` nos players que apareceram nesta varredura e não estavam na anterior (rodadas `-v2` em diante).
- **Zero recomendação.** Sem "onde você entra", sem oportunidades, sem leitura estratégica. Se sobrou opinião, corte.

---

## TEMPLATE 2 — `dossie-concorrencia.md`

```markdown
# Dossiê de Concorrência — [Nicho]
**Projeto:** [produto do aluno ou nome do cliente] · **Data:** [mês/ano] · **Rodada:** [N]ª
> **DADOS BRUTOS para análise.** Fichas factuais — identidade, esteira, preços, promessa literal, funil, reputação. Sem SWOT, sem matriz, sem oportunidades, sem recomendação. Cada dado leva o link de onde saiu.

[LEGENDA DE TERMOS — bloco comum acima]

---

## PANORAMA FACTUAL DO MERCADO

[Como o mercado se organiza por vértice — descritivo. Ex: "quatro grupos pelo que cada player vende: ..."]

**Faixas de ticket confirmadas (fonte viva):** [recorrência R$X/mês · cursos R$Y–Z · high-ticket R$W]. [Nota factual sobre o que ficou atrás de aplicação/WhatsApp.]

**Modelos de funil observados:** [ex: 5 de 8 vendem por lançamento com aula grátis; 2 vendem direto na página; 1 só por WhatsApp — com os players entre parênteses].

*(Nada de "conclusão" ou "onde você entra".)*

---

# FICHA 01 — [MARCA/PRODUTO]

| Campo | Dado |
|---|---|
| **Expert** | [nome + credencial factual] |
| **Instagram** | [@handle](https://www.instagram.com/handle/) · [audiência] |
| **Outros canais** | [YouTube/TikTok com link + audiência, se houver] |
| **Produto-âncora** | [nome] |
| **Modelo** | [lançamento / perpétuo / evento / assinatura / aplicação] |

**Esteira/oferta com preços:**
| Produto | Preço | Fonte |
|---|---|---|
| [Produto] | **R$X** (12x R$Y) (confirmado) | [slug-legível](https://url-exata) |
| [Produto] | não público ([motivo]) | [página do produto](https://url) |

**Big Idea (literal):** "[promessa literal da página, entre aspas]." ([fonte](https://url))
**Método:** [os passos/pilares do método, se explícitos na página — com fonte].
**Garantia / bônus / prova social:** [fatos da página, com fonte].
**Funil:** [captação → nutrição → oferta, factual — o que usa, com links (bio, isca, anúncios)].
**Anúncios pagos:** [o que a Biblioteca mostrou, ou "não verificado — [link da busca](https://www.facebook.com/ads/library/?...)"].
**Reputação:** [fatos do Reclame Aqui/reviews com link, ou "não coletada"].

---

# FICHA 02 — [...]
[repetir pros players prioritários — top 4-6]

---

## PENDÊNCIAS DE COLETA
- [ ] [Preço `não público` de X — como fechar: entrar como lead / abrir checkout no navegador]
- [ ] [Reclame Aqui de Y — abrir manual (403)]
- [ ] [Biblioteca de Anúncios de Z — abrir manual: link]
- [ ] [Ferramentas que faltaram e o que ficou de fora]
- [ ] [Correções de dado aplicadas]
```

**Notas de preenchimento do dossiê:**
- Fichas fundas só pros players do mesmo vértice + os maiores + os que o aluno citou. Menores ficam só no mapa.
- **Esteira COM PREÇOS reais** é o coração da ficha — cada preço com fonte. Varra o site (ver `coleta-por-concorrente.md`); não deixe preço em branco por preguiça.
- **Zero interpretação.** Sem forças/fraquezas, sem matriz de estrelas, sem oportunidades, sem "você pode...". Descreva o concorrente; não aconselhe.
