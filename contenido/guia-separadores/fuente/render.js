const { chromium } = require('playwright');
(async () => {
  const dir = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + dir + '/guia.html'); await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: dir + '/guia.pdf', width: '1080px', height: '1350px', printBackground: true });
  const secs = await p.$$('section');
  for (let i = 0; i < secs.length; i++) await secs[i].screenshot({ path: `${dir}/pagina-${i+1}.png` });
  await b.close();
})();
