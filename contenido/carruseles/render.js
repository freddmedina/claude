// Convierte los HTML generados por generar.py en PNG 1080x1350.
const path = require('path');
const { chromium } = require(path.join(require('child_process').execSync('npm root -g').toString().trim(), 'playwright'));
const lista = require('./_html/lista.json');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const s of lista) {
    await page.goto('file://' + s.html);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: s.png });
  }
  await browser.close();
  console.log('ok', lista.length);
})();
