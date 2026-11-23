"""Bütün sayfaları site/_headers'taki CSP ile açar; CSP ihlali ve betik hatası olan sayfaları listeler.
Kullanım: python3 tools/csp_kontrol.py → sorun varsa çıkış kodu 1."""
import functools, http.server, threading, os, re, sys, collections
from playwright.sync_api import sync_playwright
SITE = os.path.join(os.path.dirname(__file__), '..', 'site')
CSP = re.search(r'Content-Security-Policy: (.+)', open(os.path.join(SITE, '_headers')).read()).group(1)
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def end_headers(self):
        if self.path.split('?')[0].endswith('/') or self.path.endswith('.html'):
            self.send_header('Content-Security-Policy', CSP)
        super().end_headers()
INIT = "window.__ihlal=[];document.addEventListener('securitypolicyviolation',e=>window.__ihlal.push(e.violatedDirective+' '+(e.blockedURI||'satır içi')+' '+(e.sample||'').slice(0,60)));"
def main():
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 8798), functools.partial(H, directory=SITE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    pages = sorted('/' + os.path.relpath(r, SITE).replace('\\', '/') + '/' for r, _, f in os.walk(SITE) if 'index.html' in f)
    pages = [p.replace('/./', '/') for p in pages]
    sorun = collections.defaultdict(list)
    with sync_playwright() as p:
        b = p.chromium.launch(); c = b.new_context(viewport={'width': 1280, 'height': 900}); c.add_init_script(INIT)
        pg = c.new_page(); hatalar = []
        pg.on('pageerror', lambda e: hatalar.append(str(e)[:120]))
        # dış adreslere gitme (analitik vb.): CSP kararı tarayıcıda verilir, ağ isteği gerekmez
        pg.route(re.compile(r'^https?://(?!127\.0\.0\.1)'), lambda r: r.abort())
        for u in pages:
            hatalar.clear()
            try:
                pg.goto('http://127.0.0.1:8798' + u, wait_until='load', timeout=20000); pg.wait_for_timeout(80)
                ih = pg.evaluate('window.__ihlal')
            except Exception as ex:
                ih = ['açılamadı ' + str(ex)[:80]]
            if ih or hatalar: sorun[u] = ih + ['HATA ' + h for h in hatalar]
        b.close()
    srv.shutdown()
    print(f'{len(pages)} sayfa tarandı, {len(sorun)} sayfada sorun')
    tur = collections.Counter(x for v in sorun.values() for x in v)
    for k, n in tur.most_common(15): print(n, k)
    return 1 if sorun else 0
if __name__ == '__main__': sys.exit(main())
