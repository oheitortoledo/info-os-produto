# Coleta por concorrente — varrer as URLs, preencher as 4 dimensões

Este é o playbook da **Fase 2**. Objetivo: pra cada player, sair com **produtos, promessas, tickets e funil** preenchidos, cada dado com a URL de onde saiu.

Todo material cru (HTML baixado, listas de vídeos, descrições, anotações de coleta) vai em `<pasta de saída>/concorrentes/` — de preferência um arquivo por player (`concorrentes/<slug-do-player>.md`) com as URLs visitadas e o que cada uma mostrou. Isso é o que permite conferir e refazer depois.

## O checklist de URLs (não pular nenhuma que existir)

Um concorrente é um **conjunto de URLs**, cada uma revela uma dimensão diferente:

| URL | O que ela revela | Como achar |
|---|---|---|
| **Site institucional** | Posicionamento, autoridade, esteira geral | WebSearch `<nome> oficial` |
| **Landing de vendas** | Headline, promessa, bônus, garantia, prova social, CTA | Link da bio do IG, descrição de vídeo, anúncios |
| **Checkout / página de preço** | **Ticket** real, parcelamento, order bumps | Botão "quero comprar" da landing |
| **Produto na Hotmart / Kiwify / Eduzz / Hubla** | Ticket, estrutura do curso | Descrição de vídeo, WebSearch (ver contorno) |
| **Link da bio do Instagram** | O último passo do funil (pra onde ele manda o orgânico) | Perfil IG do criador |
| **Biblioteca de Anúncios da Meta** | Se roda tráfego pago, criativos, ângulos, volume | facebook.com/ads/library |
| **Reclame Aqui** | Reputação | reclameaqui.com.br |
| **Canal do YouTube (descrições)** | Links de oferta, iscas, parceiros | yt-dlp ou WebFetch |
| **"Falar com consultor" / WhatsApp** | Venda consultiva de produto caro | Landing (quando não tem preço público) |

Nem todo player tem todas. Mas se você só olhou a home, você tem ~20% do que precisa.

## 💰 Descoberta de preço via sitemap + slugs (o método que FUNCIONA)

Preço é a dimensão que mais falta por preguiça. O caminho confiável não é WebFetch na home — é **mapear o site inteiro e abrir as páginas de produto**. Faça com `curl` (pega o HTML cru e não gasta o limite do WebFetch). Funciona no terminal do Mac e no Git Bash do Windows:

```bash
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'
D=dominio-do-concorrente.com.br

# 1) robots + sitemap → lista TODAS as URLs do site
curl -sL -A "$UA" --max-time 12 "https://$D/robots.txt"
curl -sL -A "$UA" --max-time 12 "https://$D/sitemap.xml" | grep -oE '<loc>[^<]+</loc>' | sed 's/<[^>]*>//g'
# se for índice: repetir nos sub-sitemaps. Tentar também /sitemap_index.xml

# 2) abrir cada slug de PRODUTO/VENDA e caçar preço + link de checkout
for SLUG in oferta checkout inscricao matricula vendas mentoria curso planos precos <nomes-de-produto-do-sitemap>; do
  echo "== https://$D/$SLUG =="
  curl -sL -A "$UA" --max-time 15 "https://$D/$SLUG" 2>/dev/null \
    | grep -oE 'R\$ ?[0-9][0-9\.]*(,[0-9]{2})?|de R\$ ?[0-9\.,]*|[0-9]+x de R\$ ?[0-9\.,]*|pay\.hotmart\.com/[A-Za-z0-9?=&_-]+|kiwify[^"'"'"' ]*|<title>[^<]*</title>' | sort -u
done
```

Sem `curl` disponível: WebFetch direto em cada URL de produto do sitemap, com o prompt estruturado mais abaixo.

**⚠️ Anote a URL EXATA de cada número que capturar.** No documento final toda fonte vira link clicável, então guarde a URL completa da página onde o preço apareceu — não o domínio, não o slug relativo. Um preço achado em `/melhoroferta/` sai da coleta como `https://dominio.com.br/melhoroferta/`.

**Ordem de ataque por player:** bio do Instagram → site próprio → `sitemap.xml`/`robots.txt` → slugs de produto → checkout. O sitemap quase sempre entrega os slugs de venda que não aparecem no menu (é comum o preço estar numa página tipo `/venda-2` ou `/cap-xyz` que só o sitemap revela).

**Plataformas de checkout** onde o preço mora: Hotmart, Kiwify, Eduzz, Hubla, Cademi, Ticto, Stripe (checkout próprio), Sympla (eventos). Procure `pay.hotmart.com/...`, `.../checkout`, links de "comprar".

**Ancoragem:** o grep pega `de R$X` (riscado) e o `por R$Y` real na mesma página. Registre os dois (ex: "R$1.497,99 de R$2.997,99").

**⚠️ Checkouts Hotmart/Kiwify carregam o preço por JavaScript** — `curl` pega a casca, não o preço. Se o preço não sair, o produto **existe** mas o número exige **abrir o checkout num navegador** → registrar como pendência (`não capturável estático`, não `não público`). Sites terceiros às vezes têm o número — WebSearch `"<produto>" preço R$`.

**Landings de infoproduto caem MUITO** (DNS/SSL/403). Tente `http://` e `https://`; se cair, WebSearch o nome do produto (o snippet do Google costuma ter o preço), mesmo com o domínio fora do ar.

**Correção vale ouro:** ao abrir o site real, você corrige preço chutado ou desatualizado (é comum um preço "conhecido" de R$99 estar, no site vivo, R$1.497). Sempre confie no checkout, nunca na memória nem em post antigo.

> **⚠️ Operacional — NÃO faça um subagente por concorrente.** Subagentes tendem a abrir outros subagentes, estouram o limite e voltam com erro de limite / zero dado. Faça a coleta **você mesmo com `curl`/WebFetch**, sequencial ou em poucos lotes. Se usar subagente, no máximo ~3 e com "VOCÊ MESMO pesquisa, NÃO use a ferramenta Agent" escrito no prompt. (Se esta skill já está rodando como subagente da `/alicerce-copy`, não abra nenhum.)

## Descoberta de canal no YouTube

**Com yt-dlp:**

```bash
cd "<pasta de saída>/concorrentes"

# Tentar handles plausíveis
for HANDLE in <handle1> <handle2>; do
  cnt=$(yt-dlp "https://www.youtube.com/@$HANDLE/videos" --flat-playlist --print id --no-warnings --playlist-end 3 2>/dev/null | wc -l)
  echo "@$HANDLE → $cnt vídeos"
done

# Se o handle falhar (0 vídeos), busca reversa por nome
yt-dlp "ytsearch5:<nome do concorrente> <nicho>" --flat-playlist --no-warnings \
  --print "%(channel)s | %(channel_id)s | %(title)s" 2>/dev/null
```

**Sem yt-dlp (modo degradado):** WebSearch `site:youtube.com "<nome do concorrente>"` e `site:youtube.com <nicho> curso`, depois WebFetch na página do canal ou do vídeo pedindo título, descrição e links. Registre nas pendências que a varredura do YouTube foi parcial.

**Nº de seguidores / audiência:** não confie no YouTube pra isso (o yt-dlp costuma devolver o campo vazio). **A fonte primária de audiência é o Instagram** — WebSearch/WebFetch do perfil (`instagram.com/<handle>`) ou busca `"<nome>" seguidores instagram`. O YouTube serve pra descobrir os vídeos e as descrições, não pra contar público.

**Registre o @handle exato + a URL do perfil** (`https://www.instagram.com/<handle>/`) de cada player — ele vira link clicável no documento. Confirme o handle no perfil real, não chute a partir do nome. Se não conseguir confirmar, marque `@?` e registre como pendência — não invente handle.

## Extrair as descrições dos vídeos (onde moram os links de oferta)

**O ouro do funil está na descrição.** É onde o concorrente bota o link da landing, o cupom, a isca, o WhatsApp, os parceiros.

```bash
# Top 15 vídeos do canal
yt-dlp "https://www.youtube.com/channel/<CHANNEL_ID>/videos" --flat-playlist --no-warnings --playlist-end 15 \
  --print "%(id)s | %(view_count)s | %(title)s" 2>/dev/null > canal-<slug>.txt

# Descrição completa de um vídeo (repetir pros relevantes)
yt-dlp "https://youtube.com/watch?v=<ID>" --skip-download --no-warnings \
  --print "%(title)s" --print "%(view_count)s views" --print "%(description)s" 2>/dev/null > video-<ID>.txt
```

Sem yt-dlp: WebFetch em `https://www.youtube.com/watch?v=<ID>` pedindo "título, descrição completa e todos os links da descrição".

Em nicho **técnico/B2B** os vídeos têm poucos comentários — priorizar a **descrição** (sempre tem CTA e link).

**Canal dominado por Shorts?** Shorts costumam vir com descrição vazia — o CTA está no vídeo falado ou na bio. Vá direto pro **link da bio do Instagram** pra achar a oferta e o funil.

## WebFetch estruturado na landing (extrai as 4 dimensões de uma vez)

Pra cada landing/checkout encontrado:

```
WebFetch(
  url: <landing>,
  prompt: "Extraia em detalhes, literalmente como aparece na página:
  (1) HEADLINE e sub-headline principal (a promessa/big idea — copie a frase entre aspas);
  (2) PREÇO de cada produto/plano, com ancoragem (R$X de R$Y) e parcelamento;
  (3) O QUE ESTÁ INCLUÍDO — módulos, nº de aulas, bônus (com valor individual se houver), comunidade, mentoria;
  (4) GARANTIA (dias);
  (5) PÚBLICO declarado — a quem é vendido, com as palavras da página;
  (6) PROVA SOCIAL — números, depoimentos, cases com valores;
  (7) FUNIL — como se compra (checkout direto? formulário? falar com consultor? WhatsApp? evento?);
  (8) CTAs e upsells/order bumps mencionados, com os links.
  Se algum item não aparecer, diga 'não informado'."
)
```

Esse prompt único cobre produto (3), promessa (1), ticket (2) e funil (7). Salve o retorno em `concorrentes/<slug-do-player>.md` com a URL no topo.

## Contorno da Hotmart (obrigatório)

URLs `hotmart.com/pt-br/marketplace/produtos/...` retornam a página genérica de cadastro, **não** o produto. WebFetch direto não funciona. Buscar em sites terceiros:

```
WebSearch ("<criador>" curso "<nicho>" preço "R$")
WebSearch ("<nome do produto>" hotmart preço)
WebSearch ("<criador>" curso site:mundodecursos.com OR site:cursosverificados.com)
```

**Expectativa realista:** o contorno recupera bem a **existência e a estrutura** do produto — o **preço quase nunca vem** pra produto pequeno da Hotmart. O normal é: descobre-se que o produto existe, o preço fica `não público`, e a forma de fechar é **entrar como lead** (abrir o checkout num navegador, comprar o produto de entrada, ou WhatsApp). Isso não é falha da coleta — é o padrão da cauda longa.

## Biblioteca de Anúncios da Meta (o funil pago)

Se o concorrente anuncia, a Biblioteca revela o funil de captação e os ângulos que ele está testando:

```
WebFetch("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=<nome do concorrente>", prompt: "Liste os anúncios ativos: texto principal, o que oferecem, pra onde mandam (landing, WhatsApp, formulário), e desde quando rodam.")
```

**A Biblioteca costuma bloquear leitura automática** (página pesada de JavaScript / conexão recusada). Isso é o **esperado**, não exceção: tente **uma vez**; se não vier, registre como pendência com o **link da busca pronto** (a URL acima, com o nome preenchido) pra abrir manualmente. O link em si já é dado útil. Não gaste tentativas.

## Reclame Aqui (reputação)

Pros players do mesmo vértice, sempre checar:

```
WebSearch ("<marca/produto>" reclame aqui reclamações)
WebFetch("https://www.reclameaqui.com.br/empresa/<slug>/", prompt: "Nota, volume de reclamações, e os 3-5 temas mais recorrentes (ex: propaganda enganosa, não entrega, reembolso, atendimento).")
```

**O Reclame Aqui quase sempre devolve `403`** (bloqueia bot). O caminho que funciona é o **WebSearch dos títulos de reclamação** (que já mostram os temas recorrentes). Tente o fetch uma vez; se der 403, use o WebSearch e registre "abrir Reclame Aqui manual pra nota/volume" como pendência. Registre só os fatos — o que isso significa fica pro passo seguinte.

## Quando a landing cai (certificado/DNS/fora do ar)

**Isso é frequente, não raro.** `ENOTFOUND` (DNS), erro de SSL, `403` (bloqueio a bot). Numa varredura típica, boa parte das landings vai falhar. **Não insista:** uma tentativa por URL, depois fallback.

Fallback em ordem:
1. **WebSearch** pelo nome do produto/criador (preço e oferta aparecem em outro site com frequência)
2. **Link da bio do Instagram** — landings de último passo vivem lá
3. **Wayback Machine** — `https://web.archive.org/web/<url-original>` (se usar, marque o dado como "arquivado em [data]")
4. **Biblioteca de Anúncios** — às vezes mostra prévia da oferta

## Preencher as 4 dimensões — o que "bom" parece

**PRODUTOS** — a esteira toda, do tripwire ao high-ticket:
> Imersão R$67 (tripwire) → Formação R$1.897 → Curso de escala R$2.390–3.497 → Mentoria 1:1 ~R$30.000

**PROMESSAS** — a frase literal, entre aspas:
> "Construir imóveis para vender, sem terreno e sem capital próprio, mantendo seu emprego"

**TICKETS** — cada produto, com ancoragem e parcelamento:
> R$1.897 (de R$2.897, 12x R$189) · high-ticket `não público` (atrás de "falar com consultor")

**FUNIL** — a mecânica de captação → conversão:
> Orgânico dominante (IG/TikTok/YouTube) → lista de espera WhatsApp → masterclass grátis → página com escassez (contador) → checkout

## Anti-padrões

- ❌ Olhar só a home (perde preço, esteira e funil)
- ❌ Tratar todo canal grande como mesmo vértice (ignora tipologia)
- ❌ Não buscar Hotmart/Kiwify (deixa de mapear concorrente digital real)
- ❌ Pular a descrição dos vídeos (perde os links de oferta)
- ❌ Aceitar `não público` sem registrar como pendência acionável
- ❌ Inventar preço quando não achou — melhor `não público` honesto
- ❌ Pular Reclame Aqui dos players do mesmo vértice
- ❌ Travar porque uma ferramenta faltou — siga em modo degradado e registre

## Notas de terminal

- **Mac (zsh):** não usar `status`, `path`, `result`, `cdpath` como nome de variável (são reservadas). Usar `http_code`, `cnt`, `rc`, `outdir`.
- **Windows:** o Claude Code roda os comandos no Git Bash — `curl`, `grep` e `sed` funcionam igual. Caminhos com espaço sempre entre aspas.
- IDs do YouTube que começam com hífen quebram alguns comandos — usar `--` antes do argumento.
- `yt-dlp` não instalado? Mac: `brew install yt-dlp` (ou `pip3 install yt-dlp`) · Windows: `winget install yt-dlp`. Não é obrigatório.
