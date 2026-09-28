# Info OS — Sistema Operacional do Infoproduto

Feito por [Heitor Toledo](https://instagram.com/oheitortoledo) pra quem vende infoproduto na internet.

Da pesquisa de mercado ao anúncio no ar: o Info OS é uma pasta com skills do Claude Code que montam o alicerce do copy, a identidade visual, a página de vendas, os criativos e o conteúdo do seu produto.

---

## Antes de começar

Você precisa ter:

1. O **Antigravity** (ou o VS Code) instalado
2. A extensão do **Claude Code** instalada nele, com login feito (plano Pro ou Max)
3. O **Git** instalado. Não sabe se tem? Faz a Opção 1: o Claude confere e instala pra você.

---

## Como instalar

### Opção 1 — Via prompt (mais fácil)

Abra o Claude Code na pasta onde você quer guardar o Info OS e cole este prompt:

```
Instala pra mim o Info OS: clona o repositório https://github.com/oheitortoledo/info-os-produto.git na pasta atual e depois confere e instala o que as skills precisam pra rodar (python3, yt-dlp, ffmpeg e o playwright com o chromium). Se faltar o git, instala ele primeiro. No final me diz o que foi instalado e o que ficou faltando.
```

O Claude faz tudo: baixa o Info OS, instala as ferramentas e te avisa o que ficou pendente.

Quando ele terminar, **abra a pasta `info-os-produto`** no Antigravity (menu **File → Open Folder**) e abra o Claude Code de novo lá dentro. O Info OS só funciona quando o Claude Code está aberto **dentro** da pasta dele.

---

### Opção 2 — Via terminal

**1. Baixe o Info OS**
```bash
git clone https://github.com/oheitortoledo/info-os-produto.git
cd info-os-produto
```

**2. Instale as ferramentas que as skills usam**

No Mac:
```bash
brew install yt-dlp ffmpeg
npm install playwright && npx playwright install chromium
```

No Windows:
```bash
pip install yt-dlp
winget install ffmpeg
npm install playwright && npx playwright install chromium
```

**3. Abra a pasta no Antigravity**

Menu **File → Open Folder** → escolha a pasta `info-os-produto`.

**4. Abra o Claude Code dentro dela** e comece pelo Alicerce:
```
/alicerce-copy
```

---

## Por onde começar

As skills têm uma ordem. Cada etapa usa o que a anterior produziu:

**1. Alicerce do Copy** — a base de onde sai toda copy
- `/alicerce-copy` — roda o Alicerce inteiro de uma vez (comece por aqui)
- `/pesquisa-mercado` — pesquisa do nicho: YouTube, Reddit, Google e concorrência
- `/mapa-concorrentes` — quem vende no seu nicho, o quê, por quanto e por qual caminho
- `/persona-profunda` — dores, desejos, objeções e as frases exatas do seu público
- `/tom-de-voz` — extrai a sua voz a partir de 30+ minutos seus falando

**2. Identidade visual**
- `/identidade-visual` — cores, fontes e regras da sua marca, salvas em `marca/DESIGN.md`

**3. Página de vendas**
- `/pagina-de-vendas` — pega uma página que você admira e escreve a sua em cima da estrutura dela
- `/design-paginas` — veste a página com a sua marca e entrega pronta pro computador e pro celular

**4. Criativos**
- `/biblioteca-anuncios-meta` — minera e guarda os anúncios dos concorrentes
- `/escrever-criativos-ultra-low-ticket` — pack de 12 anúncios pra produto de até R$ 10
- `/escrever-criativos-low-ticket` — pack de 12 anúncios pra produto acima de R$ 10 vendido na página
- `/escrever-criativos-vsl` — pack de 12 anúncios pra funil de aula ou vídeo gratuito

**5. Conteúdo**
- `/carrossel` — carrossel pro Instagram na sua voz e com a cara da sua marca

---

## Chaves de API (só pra biblioteca de anúncios)

A `/biblioteca-anuncios-meta` usa três serviços de fora. As outras skills não precisam de chave nenhuma.

| Chave | Pra que serve | Onde pegar |
|---|---|---|
| `APIFY_TOKEN` | minerar os anúncios (obrigatória) | [apify.com](https://apify.com) → Settings → API & Integrations |
| `ASSEMBLYAI_API_KEY` | transcrever a fala dos vídeos | [assemblyai.com](https://www.assemblyai.com) → Dashboard |
| `TWELVELABS_KEY` | analisar o visual dos vídeos (opcional) | [twelvelabs.io](https://www.twelvelabs.io) → API Keys |

Troque `cole_aqui` pela sua chave e rode no terminal.

No Mac:
```bash
echo 'export APIFY_TOKEN="cole_aqui"' >> ~/.zshrc
echo 'export ASSEMBLYAI_API_KEY="cole_aqui"' >> ~/.zshrc
echo 'export TWELVELABS_KEY="cole_aqui"' >> ~/.zshrc
```

No Windows:
```bash
setx APIFY_TOKEN "cole_aqui"
setx ASSEMBLYAI_API_KEY "cole_aqui"
setx TWELVELABS_KEY "cole_aqui"
```

Depois **feche e abra o Antigravity de novo** pra ele enxergar as chaves.

---

## O que vem no kit

- `.claude/skills/` — as skills listadas acima
- `_contexto/` — onde fica o contexto do seu negócio
- `marca/` — o guia de identidade visual da sua marca
- `conteudo/` — carrosséis, posts, roteiros e newsletters
- `infoproduto/` — tudo do seu produto: pesquisa, alicerce, página e criativos

---

## Ficou travado?

Cola o erro no próprio Claude Code e pede: **"deu esse erro, resolve pra mim"**. Na maioria das vezes ele resolve sozinho.
