---
name: alicerce-copy
description: Monta o ALICERCE DO COPY inteiro de uma vez — a base de onde sai toda copy (página, anúncio, email, roteiro). Faz uma entrevista curta e roda os três blocos, com agentes trabalhando em paralelo: (1) pesquisa de mercado + mapa da concorrência, (2) Persona Profunda, (3) tom de voz do especialista (a partir de 30+ minutos dele falando). No fim entrega um resumo em linguagem simples e o teste de voz pra validar. Use SEMPRE que o usuário disser "alicerce", "alicerce do copy", "monta meu alicerce", "roda o alicerce", "roda tudo", "pesquisa completa", "quero a base da minha copy", "começar a copy do zero", "entender meu mercado, meu cliente e minha voz", ou estiver começando um produto/oferta novo sem pesquisa. Cada bloco também tem skill própria pra refazer só uma parte: /pesquisa-mercado, /mapa-concorrentes, /persona-profunda, /tom-de-voz.
---

# Alicerce do Copy

## O que é, em uma frase

Antes de escrever qualquer copy, a gente precisa saber três coisas: **onde você está** (mercado e concorrência), **com quem você fala** (Persona Profunda) e **como você fala** (seu tom de voz). O Alicerce do Copy é o conjunto dessas pesquisas, documentado com prova — e toda skill de escrita daqui pra frente (como a `/pagina-de-vendas`) puxa dele.

## Como ela funciona

Você é o maestro. Quem pesquisa são agentes em segundo plano, cada um seguindo a skill do seu bloco. O aluno só age em dois momentos: **a entrevista** e **mandar os vídeos dele** pro tom de voz.

```
Entrevista (aluno) ─┬─► [agente] pesquisa de mercado  ─┐
                    ├─► [agente] mapa da concorrência ─┴─► [agente] persona profunda ─┐
                    └─► vídeos do aluno → transcrever → [agente] tom de voz ──────────┴─► Resumo + teste de voz (aluno)
```

A pesquisa de mercado e a concorrência demoram (pode passar de 30 minutos). O tom de voz acontece **enquanto elas rodam**, então o aluno não fica esperando à toa.

**Linguagem com o aluno:** português simples, "você", zero jargão (nada de "VoC", "corpus", "subpersona", "ToV", "funil de VSL" sem traduzir). Diga sempre o que está acontecendo e por quê em uma frase — ele está aprendendo o método enquanto usa.

---

## Passo 0 — Ler o que já existe

Antes de perguntar qualquer coisa:

1. Leia `_contexto/` (se o aluno já rodou o setup, boa parte da entrevista está respondida lá).
2. Procure alicerce anterior: `find infoproduto -type d -name "alicerce-do-copy" 2>/dev/null`. Se existir, pergunte se é pra **refazer tudo** (nova versão, `-v2`) ou **completar só o que falta** — e aí rode só os blocos vazios.

## Passo 1 — Entrevista (uma mensagem só)

Pergunte só o que o `_contexto/` não respondeu, tudo numa mensagem, numeradas:

1. **Qual o nicho e o produto?** Em uma frase: o que você vende, pra quem.
2. **Qual a promessa?** O resultado que a pessoa tem depois de comprar.
3. **Quem é o seu cliente ideal**, do jeito que você enxerga hoje? (vai ser testado pela pesquisa — pode chutar)
4. **Conhece concorrentes?** Nomes, @ ou sites. Se não souber, tudo bem, a gente acha.
5. **Qual o seu nome** do jeito que aparece pro público? (vai no documento de voz)

Tudo mora em `BASE` = `infoproduto/alicerce-do-copy`.

```bash
mkdir -p "<BASE>/pesquisa-de-mercado" "<BASE>/persona-profunda" "<BASE>/tom-de-voz"
```

Escreva o briefing em `<BASE>/briefing.md` (as respostas, com data). Ele é a fonte do que vai pros agentes e fica de registro.

## Passo 2 — Disparar o bloco 1 (dois agentes em paralelo)

Na **mesma mensagem**, lance dois agentes com a ferramenta `Agent` (`subagent_type: general-purpose`, `run_in_background: true`). Prompt de cada um:

```
Leia .claude/skills/<SKILL>/SKILL.md e siga em MODO BRIEFING (sem perguntas, sem abrir arquivos, sem lançar outros agentes).

BRIEFING
- Nicho: ...
- Produto: ...
- Promessa: ...
- Público (hipótese do aluno): ...
- Concorrentes conhecidos: ...
- PASTA DE SAÍDA: <BASE>/pesquisa-de-mercado/

Não apague nem sobrescreva arquivos da pasta: outro agente escreve nela ao mesmo tempo.
Ao terminar, devolva só o resumo que a skill pede pro modo briefing.
```

`<SKILL>` = `pesquisa-mercado` num, `mapa-concorrentes` no outro.

Avise o aluno, curto:

> "Coloquei dois pesquisadores pra rodar: um levantando o que o seu público fala e sente na internet, outro mapeando os concorrentes e quanto eles cobram. Isso leva um tempo. Enquanto isso, vamos pro seu tom de voz."

## Passo 3 — Tom de voz (com o aluno, enquanto o bloco 1 roda)

Siga os **Passos 1 e 2** de `.claude/skills/tom-de-voz/SKILL.md` aqui na conversa: pedir 30+ min de fala dele e transcrever pra `<BASE>/tom-de-voz/transcricoes/`. Essa parte precisa do aluno, por isso não vai pra agente.

Com o mínimo atingido, lance o agente de voz em segundo plano:

```
Leia .claude/skills/tom-de-voz/SKILL.md e siga em MODO BRIEFING (sem perguntas, sem abrir arquivos, sem lançar outros agentes).

BRIEFING
- Especialista: ...
- Nicho: ...
- TRANSCRIÇÕES (já prontas): <BASE>/tom-de-voz/transcricoes/
- Falante a ignorar (se houver): ...
- PASTA DE SAÍDA: <BASE>/tom-de-voz/

Rode os Passos 3 a 6. Devolva só o resumo do modo briefing.
```

**Se o aluno não tem os vídeos agora:** não trave o alicerce. Siga sem o bloco 3 e, no fim, diga que ele pode rodar `/tom-de-voz` quando tiver o material.

## Passo 4 — Persona Profunda (quando os DOIS agentes do bloco 1 voltarem)

Não lance antes: a Persona Profunda é construída **em cima** da pesquisa — ela analisa o material que o bloco 1 levantou e transforma nas 11 seções da persona, na matriz de benefícios e no banco de frases. Não pede nada ao aluno.

Quando os dois resumos chegarem, confira que existem `01-corpus-bruto.md` e `mapa-concorrentes.md` na pasta. Se algum agente falhou, conte ao aluno o que faltou e rode de novo só aquele. Depois lance:

```
Leia .claude/skills/persona-profunda/SKILL.md e siga em MODO BRIEFING (sem perguntas, sem abrir arquivos, sem lançar outros agentes).

BRIEFING
- Nicho: ...
- Produto: ...
- PASTA DO BLOCO 1: <BASE>/pesquisa-de-mercado/
- PASTA DE SAÍDA: <BASE>/persona-profunda/

Devolva só o resumo do modo briefing.
```

Avise o aluno numa linha: "A pesquisa voltou. Agora estou montando a sua Persona Profunda — o retrato do seu cliente, com as dores, os medos e as frases exatas dele."

## Passo 5 — Fechar (quando Persona Profunda e tom de voz voltarem)

### 5.a — Conferir

Antes de mostrar qualquer coisa, abra os documentos principais e confira por amostragem: 3 linhas aleatórias da Persona Profunda e 3 afirmações do tom de voz têm **citação literal com fonte**? Se não têm, o agente inventou — mande refazer aquela parte. É o controle de qualidade que o aluno não sabe fazer.

### 5.b — Resumo do alicerce

Escreva `<BASE>/README.md` — **uma página**, pra ser a porta de entrada do alicerce:

```markdown
# Alicerce do Copy — <produto>
Gerado em <data>. Briefing: briefing.md

## O mercado em 5 linhas
## Seus concorrentes: quem são e quanto cobram (faixa de preço)
## Seu cliente (Persona Profunda)
- Quem é:
- As 3 dores mais fortes (com a frase dele):
- O que ele pensa e não fala:
- As 3 desculpas pra não comprar:
- Os tipos de cliente que você tem:
## Sua voz
- Em uma frase:
- Palavras suas: · Nunca diga:
## O que ainda falta (lacunas de todos os blocos, do mais importante pro menos)
## Arquivos
| Bloco | Arquivo | Pra que serve |
```

Tudo que entra aqui sai dos documentos dos blocos. Nada novo.

### 5.c — Entregar ao aluno

Abra o README (`open` no Mac, `start` no Windows) e fale, curto:

1. **O que descobrimos** — 3 a 5 achados que ele provavelmente não sabia (o mais surpreendente primeiro).
2. **O teste de voz** — mostre o `tom-de-voz/teste-de-voz.md` e faça as 3 perguntas do Passo 7 da `/tom-de-voz`. Aplique as respostas no documento de voz.
3. **O que falta** — as lacunas que mais pesam, e o que resolve cada uma.
4. **Próximo passo:** "Com o alicerce pronto, falta só uma coisa antes de escrever: a cara da sua marca — cores, fontes, o jeito dos botões e do texto nos anúncios. É o `/identidade-visual`, e ele usa o que a gente acabou de descobrir sobre o seu cliente. Depois disso vem a página de vendas (`/pagina-de-vendas`) e os anúncios." Se `marca/DESIGN.md` já existir, pule a identidade e ofereça direto a `/pagina-de-vendas`.

---

## Regras do maestro

- **Nunca escreva o conteúdo dos blocos você mesmo.** Quem pesquisa é o agente, seguindo a skill. Você coordena, confere e resume.
- **Nunca invente pra tapar buraco.** Bloco que falhou volta como lacuna no README, não como texto plausível.
- **Não deixe o aluno esperando calado.** Enquanto os agentes rodam, avance no tom de voz. Se não há nada pra fazer, diga o que está rodando e que você avisa quando voltar.
- **Um produto por vez.** O Info OS é feito pra um produto só. Se o aluno citar dois, faça o alicerce do principal e registre o outro no `briefing.md` pra depois — a Persona Profunda de um produto nunca pode vazar pro outro.
