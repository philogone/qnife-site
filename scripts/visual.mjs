// Garde-fou visuel : compare le site construit (dist/) aux captures de référence (tests/visual/).
//   npm run build && npm run visual            -> échoue si l'écart dépasse la tolérance
//   npm run build && npm run visual:update     -> régénère les références (changement de design voulu)
// Animations coupées (prefers-reduced-motion) pour des captures stables.
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import puppeteer from 'puppeteer-core';
import pixelmatch from 'pixelmatch';
import { PNG } from 'pngjs';

const ROOT = path.resolve(import.meta.dirname, '..');
const DIST = path.join(ROOT, 'dist');
const GOLD = path.join(ROOT, 'tests', 'visual');
const OUT = path.join(ROOT, 'tests', 'visual', '.actual');
const UPDATE = process.argv.includes('--update');
const TOLERANCE = 0.004; // 0,4 % de pixels différents
const PAGES = ['/', '/couteaux/', '/atelier/', '/sur-mesure/', '/contact/', '/mentions-legales/', '/404.html'];
const VIEWPORTS = [{ name: 'mobile', width: 375, height: 812, mobile: true }, { name: 'bureau', width: 1440, height: 900, mobile: false }];
const CHROME = process.env.CHROME_PATH || [
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].find((p) => fs.existsSync(p));
if (!CHROME) { console.error('Chrome introuvable : définir CHROME_PATH.'); process.exit(2); }
if (!fs.existsSync(DIST)) { console.error('dist/ absent : lancer npm run build.'); process.exit(2); }

const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.webp': 'image/webp', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.png': 'image/png', '.txt': 'text/plain', '.xml': 'application/xml' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p.endsWith('/')) p += 'index.html';
  const f = path.join(DIST, p);
  if (!f.startsWith(DIST) || !fs.existsSync(f)) { res.writeHead(404); res.end('404'); return; }
  res.writeHead(200, { 'content-type': MIME[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}`;

fs.mkdirSync(GOLD, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });
const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });
let failed = 0;
for (const vp of VIEWPORTS) {
  const page = await browser.newPage();
  await page.setViewport({ width: vp.width, height: vp.height, deviceScaleFactor: 1, isMobile: vp.mobile });
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
  for (const route of PAGES) {
    const name = `${route === '/' ? 'accueil' : route.replace(/[\/.]/g, '_').replace(/^_|_$/g, '')}-${vp.name}.png`;
    await page.goto(base + route, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.querySelectorAll('img').forEach((i) => (i.loading = 'eager')));
    await page.evaluate(() => Promise.all([...document.images].map((i) => i.decode().catch(() => {}))));
    await new Promise((r) => setTimeout(r, 300));
    const shot = await page.screenshot({ fullPage: true });
    const goldFile = path.join(GOLD, name);
    if (UPDATE || !fs.existsSync(goldFile)) { fs.writeFileSync(goldFile, shot); console.log('référence écrite :', name); continue; }
    const a = PNG.sync.read(fs.readFileSync(goldFile));
    const b = PNG.sync.read(shot);
    if (a.width !== b.width || a.height !== b.height) { failed++; fs.writeFileSync(path.join(OUT, name), shot); console.log(`ÉCART ${name} : taille ${a.width}x${a.height} -> ${b.width}x${b.height}`); continue; }
    const diff = new PNG({ width: a.width, height: a.height });
    const n = pixelmatch(a.data, b.data, diff.data, a.width, a.height, { threshold: 0.1 });
    const ratio = n / (a.width * a.height);
    if (ratio > TOLERANCE) { failed++; fs.writeFileSync(path.join(OUT, name), PNG.sync.write(diff)); console.log(`ÉCART ${name} : ${(ratio * 100).toFixed(2)} % de pixels (voir tests/visual/.actual/)`); }
    else console.log(`ok ${name} (${(ratio * 100).toFixed(3)} %)`);
  }
  await page.close();
}
await browser.close();
server.close();
if (failed) { console.error(`\n${failed} page(s) ont changé. Si c'est voulu : npm run visual:update.`); process.exit(1); }
console.log(UPDATE ? '\nRéférences mises à jour.' : '\nDesign identique aux références.');
