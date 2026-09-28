#!/usr/bin/env node
/*
  Renderiza uma página HTML em desktop (1280) e mobile (390) e confere o básico.

  Uso:
    node render_check.cjs <arquivo.html> <pasta-de-saida>

  Saída na pasta:
    desk-0.png, desk-1.png…  → página inteira de desktop fatiada em blocos de 1800px
    mob-0.png,  mob-1.png…   → página inteira de mobile fatiada em blocos de 1800px
    mob-hero.png             → primeira tela do celular (390×800), como a pessoa vê ao chegar
  E imprime um relatório: rolagem lateral, imagens quebradas ou esticadas, fontes carregadas.

  Por que fatiar: página de vendas passa de 10.000px, e um PNG desse tamanho some quando
  vira miniatura. Blocos de 1800px dá pra ler cada dobra.

  Por que esconder `position:fixed` no print de página inteira: no fullPage, barra fixa de CTA
  aparece no meio da página, num lugar onde ela nunca fica de verdade. O relatório diz se existe
  elemento fixo, pra testar o comportamento dele rolando (não pelo print).
*/
const path = require('path');
const os = require('os');
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
  const [arquivo, saida] = process.argv.slice(2);
  if (!arquivo || !saida) { console.error('uso: node render_check.cjs <arquivo.html> <pasta-de-saida>'); process.exit(1); }
  const url = 'file://' + path.resolve(arquivo);
  fs.mkdirSync(saida, { recursive: true });
  const { chromium } = carregarPlaywright();
  const browser = await chromium.launch();

  for (const [nome, w, h] of [['desk', 1280, 900], ['mob', 390, 800]]) {
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    await page.goto(url, { waitUntil: 'networkidle' });

    if (nome === 'mob') await page.screenshot({ path: path.join(saida, 'mob-hero.png') });

    // força tudo que depende de rolagem a aparecer: animação de entrada e lazy-load
    await page.evaluate(() => {
      document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager');
      document.querySelectorAll('*').forEach(e => {
        const c = e.classList;
        ['rv', 'reveal', 'fade', 'fade-up', 'animate'].forEach(k => { if (c.contains(k)) c.add('in', 'visible', 'is-visible'); });
      });
    });
    await page.evaluate(async () => {
      for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); }
      window.scrollTo(0, 0);
    });
    await page.waitForTimeout(1000);

    const rel = await page.evaluate(() => {
      const fixos = [...document.querySelectorAll('body *')].filter(e => getComputedStyle(e).position === 'fixed');
      const imgs = [...document.images].map(i => {
        const r = i.getBoundingClientRect();
        const natural = i.naturalWidth ? i.naturalWidth / i.naturalHeight : null;
        const fit = getComputedStyle(i).objectFit;
        const tela = r.height ? r.width / r.height : null;
        // caso 1: sem object-fit, a proporção na tela não bate com a da foto
        // caso 2: com aspect-ratio no CSS, a caixa saiu com outra proporção (ex.: faltou height:auto)
        const ar = getComputedStyle(i).aspectRatio;
        const m = ar && ar !== 'auto' ? ar.match(/([\d.]+)\s*\/\s*([\d.]+)/) : null;
        const declarado = m ? +m[1] / +m[2] : null;
        const esticada = (natural && tela && fit !== 'cover' && fit !== 'contain' && Math.abs(natural - tela) / natural > 0.05)
          || (declarado && tela && Math.abs(declarado - tela) / declarado > 0.05);
        return { src: i.getAttribute('src'), quebrada: !i.complete || i.naturalWidth === 0, esticada };
      });
      return {
        rolagemLateral: document.documentElement.scrollWidth - window.innerWidth,
        altura: document.body.scrollHeight,
        fixos: fixos.map(e => e.className || e.tagName),
        imgsQuebradas: imgs.filter(i => i.quebrada).map(i => i.src),
        imgsEsticadas: imgs.filter(i => i.esticada).map(i => i.src),
        fontes: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/"/g, '')),
      };
    });
    rel.fontes = [...new Set(rel.fontes)];
    console.log(`\n[${nome} ${w}px] altura ${rel.altura}px`);
    console.log(`  rolagem lateral: ${rel.rolagemLateral > 0 ? 'SIM, ' + rel.rolagemLateral + 'px (corrigir)' : 'não'}`);
    console.log(`  imagens quebradas: ${rel.imgsQuebradas.length ? rel.imgsQuebradas.join(', ') : 'nenhuma'}`);
    console.log(`  imagens esticadas: ${rel.imgsEsticadas.length ? rel.imgsEsticadas.join(', ') + ' (falta height:auto ou object-fit)' : 'nenhuma'}`);
    console.log(`  fontes carregadas: ${rel.fontes.join(', ') || 'nenhuma web font'}`);
    if (rel.fixos.length) console.log(`  elementos fixos (escondidos no print, testar rolando): ${rel.fixos.join(', ')}`);

    await page.evaluate(() => document.querySelectorAll('body *').forEach(e => {
      if (getComputedStyle(e).position === 'fixed') e.style.visibility = 'hidden';
    }));
    const fatia = 1800;
    for (let i = 0, y = 0; y < rel.altura; i++, y += fatia) {
      await page.screenshot({ path: path.join(saida, `${nome}-${i}.png`), fullPage: true,
        clip: { x: 0, y, width: w, height: Math.min(fatia, rel.altura - y) } });
    }
    await page.close();
  }
  await browser.close();
  console.log(`\nprints em ${path.resolve(saida)}`);
})();
