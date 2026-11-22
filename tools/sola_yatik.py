"""Masaüstünde (1440px) satırı kırılan ama kapsayıcısının %80'inden dar kalan metin bloklarını bulur.
Kullanım: python3 tools/sola_yatik.py  → bulunan sayfa sayısı 0 değilse çıkış kodu 1."""
import functools, http.server, threading, os, sys, json
from playwright.sync_api import sync_playwright
SITE = os.path.join(os.path.dirname(__file__), '..', 'site')
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
JS = r"""() => {
 const out = [];
 const sel = 'p, li, dd, blockquote, .lede, figcaption, h1, h2, h3, form, table';
 for (const el of document.querySelectorAll(sel)) {
   if (el.closest('header.site-nav, nav, footer, .menu-panel, .duzen-yan, svg, .chip, .pchips, .card, .hklist, .grid, .tarif-kart, button, .today, .sosyal, .alt-bar, .mobil-nav')) continue;
   const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden' || cs.position === 'absolute' || cs.position === 'fixed') continue;
   const r = el.getBoundingClientRect(); if (r.width < 50 || r.height < 1) continue;
   const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.4;
   if (r.height < lh * 1.8) continue;               // tek satır: sorun değil
   let par = el.parentElement;
   while (par && ['inline','contents'].includes(getComputedStyle(par).display)) par = par.parentElement;
   const pr = par.getBoundingClientRect(); const pcs = getComputedStyle(par);
   const inner = pr.width - parseFloat(pcs.paddingLeft) - parseFloat(pcs.paddingRight);
   if (pcs.display.includes('flex') && pcs.flexDirection.startsWith('row')) continue;
   if (pcs.columnCount !== 'auto' || pcs.columnWidth !== 'auto') continue;
   if (pcs.display.includes('grid') && pcs.gridTemplateColumns.split(' ').length > 1) continue;
   if (r.width < inner * 0.8) out.push({tag: el.tagName.toLowerCase(), cls: el.className, w: Math.round(r.width), pw: Math.round(inner), t: el.textContent.trim().slice(0, 60)});
 }
 return out;
}"""
def main():
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 8799), functools.partial(H, directory=SITE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    pages = []
    for root, _, files in os.walk(SITE):
        if 'index.html' in files:
            u = '/' + os.path.relpath(root, SITE).replace('\\', '/') + '/'
            pages.append(u.replace('/./', '/'))
    pages.sort(); bad = {}
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1440, 'height': 900})
        pg.route('**/*', lambda r: r.abort() if r.request.resource_type in ('image', 'media', 'font') else r.continue_())
        for i, u in enumerate(pages):
            try:
                pg.goto('http://127.0.0.1:8799' + u, wait_until='domcontentloaded', timeout=20000)
                pg.wait_for_timeout(60)
                r = pg.evaluate(JS)
                if r: bad[u] = r
            except Exception as ex:
                print('hata', u, ex)
        b.close()
    srv.shutdown()
    json.dump(bad, open('/tmp/sola_yatik.json', 'w'), ensure_ascii=False, indent=1)
    print(f'{len(pages)} sayfa tarandı, {len(bad)} sayfada sola yatık metin')
    return 1 if bad else 0
if __name__ == '__main__': sys.exit(main())
