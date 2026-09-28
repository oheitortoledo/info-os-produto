#!/usr/bin/env node
/*
  Renderiza os slides de um carrossel em PNG e confere se algum texto estourou.

  Uso (na raiz do Info OS):
    node .claude/skills/carrossel/scripts/renderizar.cjs <pasta-do-carrossel> [slide-01]

  Lê <pasta>/slides/slide-*.html e salva <pasta>/png/slide-*.png.
  Com o segundo argumento, renderiza só aquele slide (ex.: slide-01 pra aprovar a capa).

  Tamanho: 1080×1350 (feed do Instagram, 4:5). Com --tiktok, 1080×1920 e salva em png-tiktok/.

  O que confere em cada slide:
    - texto que passou da borda (o conteúdo é mais alto que o slide) → corte no texto
    - fonte que não carregou (o slide caiu na fonte reserva)
    - imagem quebrada
*/
const path = require('path');
const fs = require('fs');

function carregarPlaywright() {
  const tentativas = [
    () => require('playwright'),
    () => require(path.join(process.cwd(), 'node_modules/playwright')),
  ];
  for (const t of tentativas) { try { return t(); } catch (_) {} }
  console.error('Playwright não encontrado. Na raiz do Info OS, rode: npm install playwright && npx playwright install chromium');
  process.exit(1);
}

(async () => {
  const args = process.argv.slice(2);
  const tiktok = args.includes('--tiktok');
  const [pasta, so] = args.filter(a => !a.startsWith('--'));
  if (!pasta) { console.error('uso: node renderizar.cjs <pasta-do-carrossel> [slide-01] [--tiktok]'); process.exit(1); }
  const dirSlides = path.join(pasta, 'slides');
  const dirSaida = path.join(pasta, tiktok ? 'png-tiktok' : 'png');
  const altura = tiktok ? 1920 : 1350;
  if (!fs.existsSync(dirSlides)) { console.error(`não achei ${dirSlides}`); process.exit(1); }
  fs.mkdirSync(dirSaida, { recursive: true });

  let arquivos = fs.readdirSync(dirSlides).filter(f => /^slide-\d+\.html$/.test(f)).sort();
  if (so) arquivos = arquivos.filter(f => f.startsWith(so));
  if (!arquivos.length) { console.error('nenhum slide encontrado'); process.exit(1); }

  const { chromium } = carregarPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: altura } });
  let problemas = 0;

  for (const f of arquivos) {
    await page.goto('file://' + path.resolve(dirSlides, f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const rel = await page.evaluate(async (alt) => {
      const s = document.querySelector('.slide') || document.body;
      const estouros = [];
      const limite = s.getBoundingClientRect();
      s.querySelectorAll('h1,h2,p,li,blockquote,.num,.botao').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.bottom > limite.bottom + 1 || r.right > limite.right + 1 || r.top < limite.top - 1)
          estouros.push((el.textContent || '').trim().slice(0, 40));
      });
      if (s.scrollHeight > alt + 1) estouros.push(`conteúdo com ${s.scrollHeight}px de altura (máx ${alt})`);
      const usadas = new Set();
      s.querySelectorAll('*').forEach(el => usadas.add(getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim()));
      const faltando = [...usadas].filter(ff => ff && !/^(Impact|Menlo|Georgia|-apple-system|sans-serif|serif|monospace)$/i.test(ff) && !document.fonts.check(`32px "${ff}"`));
      const quebradas = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.split('/').pop());
      for (const el of document.querySelectorAll('.foto')) {
        const m = getComputedStyle(el).backgroundImage.match(/url\("?(.*?)"?\)/);
        if (!m) continue;
        const ok = await new Promise(res => { const img = new Image(); img.onload = () => res(img.naturalWidth > 0); img.onerror = () => res(false); img.src = m[1]; });
        if (!ok) quebradas.push(decodeURIComponent(m[1].split('/').pop()));
      }
      return { estouros, faltando, quebradas };
    }, altura);
    const png = path.join(dirSaida, f.replace('.html', '.png'));
    await page.screenshot({ path: png, clip: { x: 0, y: 0, width: 1080, height: altura } });
    const avisos = [];
    if (rel.estouros.length) avisos.push(`texto estourou: ${rel.estouros.join(' | ')}`);
    if (rel.faltando.length) avisos.push(`fonte não carregou: ${rel.faltando.join(', ')}`);
    if (rel.quebradas.length) avisos.push(`imagem quebrada: ${rel.quebradas.join(', ')}`);
    problemas += avisos.length;
    console.log(`${f} → ${path.relative(process.cwd(), png)}${avisos.length ? '\n   ⚠ ' + avisos.join('\n   ⚠ ') : '  ok'}`);
  }
  await browser.close();
  console.log(problemas ? `\n${problemas} problema(s). Corrija o HTML e rode de novo.` : '\nTudo certo.');
  process.exit(problemas ? 2 : 0);
})();
