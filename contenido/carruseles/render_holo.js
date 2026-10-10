// Renderiza los slides de generar_holo.py: un PNG fijo y un MP4 de 6 s en loop por slide.
// Uso: node render_holo.js [solo-png]
const path = require('path');
const { spawn } = require('child_process');
const { chromium } = require(path.join(require('child_process').execSync('npm root -g').toString().trim(), 'playwright'));
const lista = require('./_html/lista_holo.json');

const FPS = 24, SEG = 6, N = FPS * SEG;
const soloPng = process.argv[2] === 'solo-png';

function ffmpeg(out) {
  const p = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium', '-movflags', '+faststart', out]);
  const done = new Promise((ok, ko) => p.on('close', c => c === 0 ? ok() : ko(new Error('ffmpeg ' + c))));
  return { stdin: p.stdin, done };
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const s of lista) {
    await page.goto('file://' + s.html);
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => setT(0.15));
    await page.screenshot({ path: s.png });
    if (soloPng) continue;
    const enc = ffmpeg(s.mp4);
    for (let f = 0; f < N; f++) {
      await page.evaluate(t => setT(t), f / N);
      const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
      if (!enc.stdin.write(buf)) await new Promise(r => enc.stdin.once('drain', r));
    }
    enc.stdin.end();
    await enc.done;
    console.log('ok', path.basename(path.dirname(s.mp4)), path.basename(s.mp4));
  }
  await browser.close();
})();
