#!/usr/bin/env python3
"""Bir parti bitki için görsel adaylarını tek bir HTML sayfasında toplar.

Neden var (25 Kasım 2026): kayıt başına en pahalı adım görsel seçimiydi —
küçük resimleri indirip kontak sayfası yapıp bakmak, ölçülen 45.000 tokenın
yaklaşık üçte biri. Seçimi insan yaparsa o maliyet sıfıra iner.

Betik Commons ve iNaturalist'te yalnız serbest lisanslı (CC0 / CC BY / CC BY-SA)
fotoğrafları arar, küçük resimleri sayfaya gömer ve her adaya bir numara verir.
Bakan kişi "yabanihunnap: 3" der, numaralar refs.py'ye yazılır.

  python3 tools/gorsel_adaylari.py p005
  python3 tools/gorsel_adaylari.py --tek yerbademi "Cyperus esculentus"

Çıktı: /tmp/.../gorsel_adaylari.html (Artifact ile yayımlanır).
"""
import base64, html, io, json, os, subprocess, sys, urllib.parse

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = 'BitkiTabani/1.0 (https://bitkitabani.com; iletisim@bitkitabani.com)'
SERBEST = {'cc0', 'cc-by', 'cc-by-sa'}


def al(adres):
    r = subprocess.run(['curl', '-sL', '-m', '60', '-A', UA, adres],
                       capture_output=True, text=True, errors='replace')
    try: return json.loads(r.stdout)
    except Exception: return None


def indir(adres):
    r = subprocess.run(['curl', '-sL', '-m', '60', '-A', UA, adres], capture_output=True)
    return r.stdout if r.stdout[:3] in (b'\xff\xd8\xff', b'\x89PN', b'RIF') else None


def commons(latin, adet=8):
    d = al('https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search'
           f'&gsrnamespace=6&gsrlimit={adet}&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=320'
           '&gsrsearch=' + urllib.parse.quote(latin))
    out = []
    for v in ((d or {}).get('query') or {}).get('pages', {}).values():
        ii = (v.get('imageinfo') or [{}])[0]
        em = ii.get('extmetadata') or {}
        lis = (em.get('LicenseShortName') or {}).get('value', '')
        if 'NC' in lis or 'ND' in lis: continue       # ticari olmayan / türetilemez alınmaz
        out.append({'kaynak': 'Commons', 'dosya': v['title'][5:],
                    'kucuk': ii.get('thumburl'), 'lisans': lis,
                    'yazar': html.unescape(((em.get('Artist') or {}).get('value', '') or ''))[:80],
                    'sayfa': ii.get('descriptionurl', '')})
    return out


def inat(latin, adet=6):
    d = al('https://api.inaturalist.org/v1/observations?per_page=%d&photo_license=%s&taxon_name=%s'
           % (adet, 'cc0,cc-by,cc-by-sa', urllib.parse.quote(latin)))
    out = []
    for o in (d or {}).get('results', []):
        ph = (o.get('photos') or [{}])[0]
        if (ph.get('license_code') or '') not in SERBEST: continue
        out.append({'kaynak': 'iNaturalist', 'dosya': str(ph.get('id')),
                    'kucuk': (ph.get('url') or '').replace('square', 'medium'),
                    'lisans': (ph.get('license_code') or '').upper(),
                    'yazar': (ph.get('attribution') or '')[:80],
                    'sayfa': f"https://www.inaturalist.org/observations/{o['id']}",
                    'tam': (ph.get('url') or '').replace('square', 'original')})
    return out


def kart(a, n):
    ham = indir(a['kucuk']) if a.get('kucuk') else None
    if not ham: return ''
    b64 = base64.b64encode(ham).decode()
    return (f'<figure><span class="no">{n}</span>'
            f'<img src="data:image/jpeg;base64,{b64}" alt="" loading="lazy">'
            f'<figcaption><b>{html.escape(a["kaynak"])}</b> · {html.escape(a["lisans"])}<br>'
            f'{html.escape(a["yazar"])}<br>'
            f'<a href="{html.escape(a["sayfa"])}" target="_blank" rel="noopener">kaynak sayfası</a>'
            f'</figcaption></figure>')


def sayfa(gruplar):
    g = []
    for pid, latin, adaylar in gruplar:
        kartlar, n = [], 0
        for a in adaylar:
            n += 1
            k = kart(a, n)
            if k: kartlar.append(k)
            else: n -= 1
        g.append(f'<section><h2>{html.escape(pid)}'
                 f'<em>{html.escape(latin)}</em></h2><div class="grid">{"".join(kartlar)}</div></section>')
    return ''.join(g)


ŞABLON = '''<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Görsel Adayları</title><style>
:root{--bg:#fbfaf7;--fg:#211d17;--ln:#ddd6c7;--mut:#6b6354;--ac:#5d6f3f}
:root:not([data-theme="light"]){}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17150f;--fg:#ece6d8;--ln:#39342a;--mut:#9c9382;--ac:#9db673}}
:root[data-theme="dark"]{--bg:#17150f;--fg:#ece6d8;--ln:#39342a;--mut:#9c9382;--ac:#9db673}
*{box-sizing:border-box}
body{margin:0;padding:0 16px 64px;background:var(--bg);color:var(--fg);
font:16px/1.55 ui-serif,Georgia,serif;-webkit-text-size-adjust:100%}
header{max-width:1100px;margin:0 auto;padding:40px 0 8px;border-bottom:1px solid var(--ln)}
h1{font-size:1.6rem;margin:0 0 6px}
p.lead{color:var(--mut);margin:0;font-size:.95rem}
section{max-width:1100px;margin:0 auto;padding:28px 0;border-bottom:1px solid var(--ln)}
h2{font-size:1.15rem;margin:0 0 14px;display:flex;flex-wrap:wrap;gap:10px;align-items:baseline}
h2 em{font-style:italic;font-weight:400;color:var(--mut);font-size:.92rem}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(210px,1fr))}
figure{margin:0;border:1px solid var(--ln);border-radius:8px;overflow:hidden;position:relative;background:transparent}
figure img{display:block;width:100%;height:190px;object-fit:cover}
.no{position:absolute;top:8px;left:8px;background:var(--ac);color:#fff;font:600 13px/1 ui-sans-serif,system-ui;
padding:6px 9px;border-radius:5px}
figcaption{padding:9px 10px;font:12px/1.45 ui-sans-serif,system-ui;color:var(--mut);word-break:break-word}
figcaption a{color:var(--ac)}
</style></head><body>
<header><h1>Görsel adayları</h1>
<p class="lead">Her bitki için serbest lisanslı adaylar. Beğendiğinin numarasını yaz —
“yabanihunnap: 3” gibi. Yalnız CC0, CC BY ve CC BY-SA var; ticari olmayan lisans alınmadı.</p></header>
__ICERIK__
</body></html>'''


def uret(cift, cikti):
    gruplar = []
    for pid, latin in cift:
        a = commons(latin) + inat(latin)
        gruplar.append((pid, latin, a))
        print(f'{pid}: {len(a)} aday')
    io.open(cikti, 'w', encoding='utf-8').write(ŞABLON.replace('__ICERIK__', sayfa(gruplar)))
    print('yazıldı:', cikti, os.path.getsize(cikti) // 1024, 'KB')


if __name__ == '__main__':
    cikti = os.environ.get('CIKTI', '/tmp/claude-0/gorsel_adaylari.html')
    if len(sys.argv) > 3 and sys.argv[1] == '--tek':
        uret([(sys.argv[2], ' '.join(sys.argv[3:]))], cikti)
    elif len(sys.argv) > 1:
        f = os.path.join(KOK, 'veri', 'parti', sys.argv[1] + '.txt')
        c = []
        for s in open(f, encoding='utf-8'):
            if s.startswith('#') or '|' not in s: continue
            p = [x.strip() for x in s.split('|')]
            c.append((p[0], p[1]))
        uret(c, cikti)
    else:
        print(__doc__)
