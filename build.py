import json, os, shutil, html, re, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
from refs import WIKI, POWO, NCCIH, EMA, OTHER, FILES, BAYTOP
from extra import EK, KORUMA, YASAL, YASAL_AD, BR_GEO, ALT
from etkilesim import ETK
from derin import D as DERIN
KAN_AD = {'klinik': 'Klinik kanıt', 'sinirli': 'Sınırlı kanıt', 'geleneksel': 'Yalnızca geleneksel', 'yok': 'Kanıt yok'}
AUTHOR = {'@type': 'Person', 'name': 'Edanaz Tınmazlar', 'url': 'https://bitkitabani.com/yontem/#hazirlayan', 'jobTitle': 'Sanatçı ve şifalı bitkiler uzmanı', 'sameAs': ['https://www.linkedin.com/in/edanaz-tinmazlar-%E6%B8%B8%E5%AD%90%E6%84%8F-588285110/', 'https://www.instagram.com/teda.naz/']}
SOCIAL = '<span class="social"><a href="https://www.linkedin.com/in/edanaz-tinmazlar-%E6%B8%B8%E5%AD%90%E6%84%8F-588285110/" rel="me noopener">LinkedIn</a> · <a href="https://www.instagram.com/teda.naz/" rel="me noopener">Instagram</a></span>'
BIO = 'Edanaz Tınmazlar, sanatçı ve şifalı bitkiler uzmanı. Beyaz yakalı hayatından şifa arayışına düştü ve kendini bitkilerin benzersiz dünyasını anlamaya çalışırken buldu. Dünyanın birçok ülkesinde gezip yaşadıktan sonra Türkiye’ye döndü; köklerini anlamayı ve anlatmayı kendine görev edindi.'
import mapgeo, math
IMG = json.load(open(os.path.join(HERE, 'images.json'), encoding='utf-8')) if os.path.exists(os.path.join(HERE, 'images.json')) else {}

BASE = 'https://bitkitabani.com'
OUT = os.path.join(HERE, 'site')
D = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))
REG, KAT, KANIT, GUV, P, BR, EXTRA = D['REG'], D['KAT'], D['KANIT'], D['GUV'], D['P'], D['BR'], D['EXTRA']
for i, p in enumerate(P): p['no'] = i + 1
GUV['yuksek'] = 'Yüksek risk'
byId = {p['id']: p for p in P}
TODAY = datetime.date.today().isoformat()
def _git_date():
    try:
        import subprocess
        out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', 'data.json', 'extra.py', 'refs.py', 'build.py'], cwd=HERE, capture_output=True, text=True, timeout=10).stdout.strip()
        return out or TODAY
    except Exception:
        return TODAY
CONTENT_DATE = _git_date()
try:
    _wr = re.sub(r'^\s*//.*$', '', open(os.path.join(HERE, 'wrangler.jsonc'), encoding='utf-8').read(), flags=re.M)
    GOOGLE_CLIENT_ID = json.loads(_wr).get('vars', {}).get('GOOGLE_CLIENT_ID', '')
except Exception:
    GOOGLE_CLIENT_ID = ''
try:
    from zoneinfo import ZoneInfo
    LOCAL_DAY = datetime.datetime.now(ZoneInfo('Europe/Istanbul')).date()
except Exception:
    LOCAL_DAY = datetime.date.today()
if os.environ.get('BT_DAY'): LOCAL_DAY = datetime.date.fromisoformat(os.environ['BT_DAY'])   # deneme için

# ---------- yayın kuyruğu: her gün bir yeni bitki (kuyruk/ klasörü) ----------
import kuyruk as _K
YENI, EN_NEW, ETK_EN_NEW, KUYRUK_LEFT = {}, {}, {}, []
for _q in _K.Q:
    _d = datetime.date.fromisoformat(_q['yayin'])
    if _q['id'] in byId: continue
    if _d > LOCAL_DAY: KUYRUK_LEFT.append(_q); continue
    _q = dict(_q); _id = _q['id']; YENI[_id] = _d
    EK[_id] = _q.pop('ek'); POWO[_id] = _q.pop('taxon')
    EN_NEW[_id] = _q.pop('en')
    if _q.get('etk_en'): ETK_EN_NEW[_id] = _q['etk_en']
    if _q.get('etk'): ETK[_id] = _q['etk']
    if _q.get('ema'): EMA[_id] = _q['ema']
    if _q.get('nccih'): NCCIH[_id] = _q['nccih']
    if _q.get('kaynak'): OTHER.setdefault(_id, []).extend(_q['kaynak'])
    if _q.get('koruma'): KORUMA[_id] = _q['koruma']
    if _q.get('yasal'): YASAL[_id] = _q['yasal']
    EXTRA[_id] = list(_q.get('rel', []))
    for _r in _q.get('rel', []):
        if _r in byId or _r in YENI: EXTRA.setdefault(_r, []).append(_id)
    for _k in ('etk', 'etk_en', 'ema', 'nccih', 'kaynak', 'koruma', 'yasal', 'rel', 'yayin', 'foto', 'ig'): _q.pop(_k, None)
    P.append(_q); byId[_id] = _q
for i, p in enumerate(P): p['no'] = i + 1
NEWEST = sorted(YENI, key=lambda k: YENI[k], reverse=True)
def is_new(pid, days=7): return pid in YENI and (LOCAL_DAY - YENI[pid]).days < days
AYLAR =['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
GUNLER = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
def tr_date(d): return f'{d.day} {AYLAR[d.month-1]} {d.year}, {GUNLER[d.weekday()]}'
def slug_of(br): return br['a'] + ('-' + br['b'] if br.get('b') else '')
e = lambda s: html.escape(str(s), quote=True)

def related(pid):
    s = list(EXTRA.get(pid, []))
    for b in BR:
        if b['a'] == pid and b.get('b'): s.append(b['b'])
        if b.get('b') == pid: s.append(b['a'])
    out = []
    for x in s:
        if x != pid and x in byId and x not in out: out.append(x)
    return out

acc = lambda n: f'BT-{n:03d}'
dot = lambda r: f'<span class="dot" style="background:var({REG[r]["c"]})" title="{e(REG[r]["ad"])}"></span>'
def pips(k):
    n = KANIT[k]['n']
    return '<span class="pips" aria-hidden="true">' + ''.join(f'<i class="{"on" if i <= n else ""}"></i>' for i in (1,2,3)) + '</span>'
short_la = lambda p: p['la'].split(',')[0].strip()

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,500;0,700;0,800;1,400&family=Alegreya+Sans:ital,wght@0,400;0,700;1,400&family=Courier+Prime&display=swap">'
FONTS = '<script>try{var t=localStorage.getItem("bt-theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>' + FONTS
FAV = '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">'

def head(title, desc, path, extra='', image=None):
    url = BASE + path
    image = image or BASE + '/img/kantaron-960.jpg'
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" type="application/rss+xml" title="Bitki Tabanı: günün bitkisi" href="/gunun-bitkisi/rss.xml"><link rel="alternate" type="application/rss+xml" title="Bitki Tabanı: yeni eklenen bitkiler" href="/yeni/rss.xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bitki Tabanı">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="tr_TR">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{image}">
<meta name="theme-color" content="#A3271B">
{FAV}
{FONTS}
<link rel="stylesheet" href="/assets/style.css">
{extra}
</head>
<body>
<div class="wrap{{narrow}}">
'''

def nav(cur):
    a = lambda href, label, key: f'<a href="{href}"{" aria-current=\"page\"" if cur == key else ""}>{label}</a>'
    return f'''<div class="motif" aria-hidden="true"></div><div class="site-nav"><a class="logo" href="/">Bitki <em>Tabanı</em></a><nav>{a("/katalog/", "Katalog", "kat")}{a("/yeni/", "Yeni", "yeni")}{a("/kopruler/", "Kültür köprüleri", "br")}{a("/hakkinda/", "Hakkında", "about")}{a("/hesap/", "Hesap", "acct")}<button type="button" class="themebtn" data-l="tr" aria-label="Açık ya da koyu tema">◐</button></nav></div>'''

FOOT = '''<div class="motif indigo" aria-hidden="true"></div>
<footer class="site">
  <div>
    <h3>Bu site nedir</h3>
    <p>Bilgi ve merak için hazırlanmış bir derlemedir; tedavi önerisi değildir. Bir bitkiyi kullanmadan önce, özellikle ilaç kullanıyorsan, hamileysen ya da emziriyorsan bir hekime veya eczacıya danış.</p>
    <p>Fotoğraflar Wikimedia Commons’tan özgür lisanslarla alınmıştır; yazarı ve lisansı her bitkinin sayfasında yazılıdır.</p>
    <p><a href="/yeni/">Yeni eklenenler</a> · <a href="https://www.instagram.com/bitkitabani/" rel="noopener">Instagram</a> · <a href="/yontem/">Yöntem</a> · <a href="/hesap/">Hesap</a> · <a href="/gizlilik/">Gizlilik</a> · <a href="mailto:iletisim@bitkitabani.com">İletişim</a></p>
  </div>
  <div class="legend">
    <h3>Kanıt düzeyi</h3>
    <div><span class="pips"><i class="on"></i><i class="on"></i><i class="on"></i></span> Klinik: kontrollü çalışmalar ya da onaylı ilaç</div>
    <div><span class="pips"><i class="on"></i><i class="on"></i><i></i></span> Sınırlı: küçük ya da az sayıda insan çalışması</div>
    <div><span class="pips"><i class="on"></i><i></i><i></i></span> Geleneksel: insan çalışması yok ya da çok az</div>
  </div>
  <div class="legend">
    <h3>Güvenlik</h3>
    <div><span class="sf dusuk">Genelde güvenli</span> ölçülü kullanımda</div>
    <div><span class="sf orta">Dikkat</span> etkileşim ya da doz riski</div>
    <div><span class="sf yuksek">Yüksek risk</span> zehirli ya da ciddi yan etkili</div>
    <div><span class="lg yasak">Türkiye’de yasak</span> ayrı bir etiketle gösterilir</div>
  </div>
</footer>
</div>
'''

def page(title, desc, path, body, cur, scripts='', narrow=False, extra='', image=None):
    h = head(title, desc, path, extra, image).replace('{narrow}', ' narrow' if narrow else '')
    return h + nav(cur) + body + FOOT + '<script src="/assets/theme.js" defer></script><script src="/assets/streak.js" defer></script><script src="/assets/sync.js" defer></script>' + scripts.replace('<script src="/assets/streak.js" defer></script>', '') + '\n</body>\n</html>\n'

def write(path, content):
    full = os.path.join(OUT, path.strip('/'), 'index.html') if not path.endswith('.html') and not '.' in path.split('/')[-1] else os.path.join(OUT, path.strip('/'))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(content)

def ph(p, size, eager=False):
    m = IMG.get(p['id'])
    if not m:
        return f'<div class="ph"><span class="ph-mark">{e(short_la(p))}</span></div>'
    w, h = (m['w'], m['h']) if size == 960 else (m.get('w500', 500), m.get('h500', 667))
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    src = f'<source type="image/webp" srcset="/img/{p["id"]}-{size}.webp">' if os.path.exists(os.path.join(HERE, 'img', f'{p["id"]}-{size}.webp')) else ''
    return f'<div class="ph loaded"><picture>{src}<img src="/img/{p["id"]}-{size}.jpg" width="{w}" height="{h}" alt="{e(p["tr"])} ({e(short_la(p))}): {e(ALT.get(p["id"], "bitki"))}" {load} decoding="async"></picture></div>'

def credit(p):
    m = IMG.get(p['id'])
    if not m: return ''
    lic = f'<a href="{e(m["licenseUrl"])}" target="_blank" rel="noopener">{e(m["license"])}</a>' if m.get('licenseUrl') else e(m.get('license', ''))
    parts = [x for x in [e(m.get('artist', '')), lic] if x]
    return 'Fotoğraf: ' + ' · '.join(parts) + f' · <a href="{e(m["page"])}" target="_blank" rel="noopener">Wikimedia Commons</a>'

def tags(p, small=False):
    out = []
    y = YASAL.get(p['id'])
    if y: out.append(f'<span class="lg {y[0]}">{YASAL_AD[y[0]]}</span>')
    k = KORUMA.get(p['id'])
    if k and k.get('rozet'): out.append(f'<span class="lg koruma">{e(k["rozet"])}</span>')
    return f'<div class="tags">{"".join(out)}</div>' if out else ''

def refs(p):
    pid = p['id']; items = []
    for label, url in EMA.get(pid, []):
        items.append(('EMA monografisi', f'{label}: Avrupa İlaç Ajansı bitkisel ilaç değerlendirmesi', url))
    if pid in NCCIH:
        items.append(('NCCIH', 'ABD Ulusal Tamamlayıcı ve Bütünleştirici Sağlık Merkezi: kullanım ve güvenlik özeti', f'https://www.nccih.nih.gov/health/{NCCIH[pid]}'))
    for label, url in OTHER.get(pid, []):
        kind = 'Resmî kaynak' if ('fda.gov' in url or 'unodc.org' in url or 'nobelprize.org' in url) else 'Araştırma'
        items.append((kind, label, url))
    if 'anadolu' in p['bolge'] and any('Anadolu' in w for w, _ in p['kul']):
        items.append(('Kitap', BAYTOP, ''))
    name = POWO.get(pid, short_la(p))
    if name:
        items.append(('Botanik kayıt', f'Kew Plants of the World Online: {name}', 'https://powo.science.kew.org/results?q=' + urllib.parse.quote(name)))
    return '<ol class="refs">' + ''.join((f'<li><span class="kind">{e(k)}</span><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' if u else f'<li><span class="kind">{e(k)}</span><cite>{e(t)}</cite></li>') for k, t, u in items) + '</ol>'

def desc_for(p):
    first = p['kul'][0][1].split('. ')[0].rstrip('.')
    d = f'{p["tr"]} ({short_la(p)}): {first}. Bilimsel kanıt: {KANIT[p["kanit"]]["ad"].lower()}. Güvenlik notları ve kaynaklar.'
    return d if len(d) <= 160 else d[:157].rsplit(' ', 1)[0] + '…'

def card(p):
    s = ' '.join([p['tr'], p['la'], p['diger'], p['fam'], p['kisim'], p['haz'], p['bilim'], p['ilginc']] + [x for u in p['kul'] for x in u] + [KAT[k] for k in p['kat']])
    return f'''<a class="card" href="/{p["id"]}/" data-id="{p["id"]}" data-bolge="{" ".join(p["bolge"])}" data-kat="{" ".join(p["kat"])}" data-kanit="{p["kanit"]}" data-guv="{p["guv"]}" data-durum="{" ".join(([YASAL[p["id"]][0] if YASAL[p["id"]][0]=="yasak" else "kisitli"] if p["id"] in YASAL else []) + (["koruma"] if KORUMA.get(p["id"], {}).get("rozet") else []))}" data-s="{e(s)}">
  {ph(p, 500)}
  <div class="body">
    <div class="row"><span class="acc">{acc(p["no"])}{'<span class="newb">Yeni</span>' if is_new(p["id"]) else ''}</span><span class="regs">{"".join(dot(r) for r in p["bolge"])}</span></div>
    <h2>{e(p["tr"])}</h2>
    <div class="latin">{e(p["la"])}</div>
    <div class="fam" lang="la">{e(p["fam"])}</div>
    {tags(p)}
    <div class="foot"><span class="ev" aria-label="Kanıt düzeyi: {KANIT[p["kanit"]]["ad"]}">{pips(p["kanit"])} Kanıt: {KANIT[p["kanit"]]["ad"]}</span><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span></div>
  </div>
</a>'''

import collections, re as _re
FAMC = collections.Counter(p['fam'] for p in P)
FAM_TR = {'Lamiaceae':'ballıbabagiller','Solanaceae':'patlıcangiller','Asteraceae':'papatyagiller','Rubiaceae':'kökboyasıgiller','Malvaceae':'ebegümecigiller','Fabaceae':'baklagiller',
          'Anacardiaceae':'sakızağacıgiller','Ranunculaceae':'düğünçiçeğigiller','Rosaceae':'gülgiller','Apiaceae':'maydanozgiller','Cactaceae':'kaktüsgiller','Euphorbiaceae':'sütleğengiller',
          'Lythraceae':'kınagiller','Arecaceae':'palmiyegiller'}
def fam_slug(f): return f.lower()
def fam_link(p):
    f = p['fam']
    return f'<a href="/familya/{fam_slug(f)}/" lang="la">{e(f)}</a>' if FAMC[f] >= 2 else f'<span lang="la">{e(f)}</span>'
DATE_TXT = tr_date(datetime.date.fromisoformat(CONTENT_DATE)).rsplit(',', 1)[0]
CONTACT = 'iletisim@bitkitabani.com'
def contrib(p):
    subj = urllib.parse.quote(f'Bitki Tabanı: {p["tr"]} için yöresel kullanım')
    body = urllib.parse.quote(f'Bitki: {p["tr"]} ({short_la(p)})\nYöre (il, ilçe, köy ya da topluluk): \nBitkinin oradaki adı: \nNasıl ve ne için kullanılır: \nBunu kimden ya da nereden öğrendin: \nAdının sitede yazılmasını ister misin (evet/hayır): \n')
    return f'<aside class="contrib"><h2>Yöresel bir kullanım biliyor musun?</h2><p>Annenden, köyünden ya da bir ustadan duyduğun bir kullanım buraya eklenebilir. Gelen her not okunur, kaynağıyla birlikte kontrol edildikten sonra eklenir.</p><p><a class="cta" href="mailto:{CONTACT}?subject={subj}&amp;body={body}">Not gönder →</a> <span class="muted-s">{CONTACT}</span></p></aside>'
def toc_and_ids(html):
    items = []
    def sub(m):
        t = m.group(1); sid = _re.sub(r'[^a-z0-9]+', '-', t.lower().translate(str.maketrans('çğıöşüâî', 'cgiosuai'))).strip('-')
        items.append((sid, t)); return f'<section class="sec" id="{sid}"><h2>{t}</h2>'
    html = _re.sub(r'<section class="sec"><h2>([^<]+)</h2>', sub, html)
    nav_ = '<nav class="toc" aria-label="Bu sayfada"><span class="eyebrow">Bu sayfada</span><ol>' + ''.join(f'<li><a href="#{s}">{t}</a></li>' for s, t in items) + '</ol></nav>'
    return html.replace('<!--TOC-->', nav_)

# ---------- bitki sayfaları ----------
for i, p in enumerate(P):
    pid = p['id']; rel = related(pid)
    prev, nxt = P[i-1], P[(i+1) % len(P)]
    title = (f'{p["tr"]}: nedir, etkileri ve zehirlilik riski' if p['guv'] == 'yuksek' else f'{p["tr"]}: faydaları, kullanımı ve yan etkileri')
    if len(title) < 44: title += ' | Bitki Tabanı'
    ld = {"@context":"https://schema.org","@type":"Article","headline":f'{p["tr"]} ({short_la(p)})',"inLanguage":"tr","about":{"@type":"Taxon","name":short_la(p),"alternateName":[p['tr']] + [x.strip() for x in p['diger'].split(',')][:4],"taxonRank":"species","parentTaxon":{"@type":"Taxon","name":p['fam'].split(' ')[0],"taxonRank":"family"}},"description":desc_for(p),"author":AUTHOR,"isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},"dateModified":(max(CONTENT_DATE, YENI[pid].isoformat()) if pid in YENI else CONTENT_DATE),**({"datePublished":YENI[pid].isoformat()} if pid in YENI else {}),"url":f'{BASE}/{pid}/',"image":(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None),"publisher":{"@type":"Organization","name":"Bitki Tabanı","url":BASE+"/","sameAs":["https://www.instagram.com/bitkitabani/"]}}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Katalog","item":BASE+"/katalog/"},{"@type":"ListItem","position":3,"name":p['tr'],"item":f'{BASE}/{pid}/'}]}
    uses = ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(t)}</p></div>' for w, t in p['kul'])
    relhtml = ''
    etkhtml = ''
    derhtml = ''; faqld = None
    trl = p['tr'].replace('I', 'ı').replace('İ', 'i')
    def _first(t): 
        s = t.split('. ')[0].rstrip('.'); return s + '.'
    regs_txt = ', '.join(REG[r]['ad'] for r in p['bolge'])
    q_nedir = (f'{p["tr"]} nedir?', f'{p["tr"]} ({short_la(p)}), {p["fam"]} familyasından bir bitkidir. Kullanıldığı gelenekler: {regs_txt}. Kullanılan kısmı: {p["kisim"].lower()}.')
    q_ne = (f'{p["tr"]} ne işe yarar?', f'Geleneksel kullanımı: {_first(p["kul"][0][1])} Bilimsel kanıt düzeyi: {KANIT[p["kanit"]]["ad"].lower()}. {_first(p["bilim"])}')
    q_guv = (f'{p["tr"]} güvenli mi?', f'Güvenlik etiketi: {GUV[p["guv"]].lower()}. {p["guvNot"]}' + (' Yasal durum: ' + YASAL_AD[YASAL[pid][0]] + '.' if pid in YASAL else ''))
    kisaca = [q_nedir, q_ne, q_guv]
    kisahtml = '<section class="kisaca" aria-label="Kısaca"><span class="eyebrow">Kısaca</span>' + ''.join(f'<div class="qa"><h2 class="q">{e(q)}</h2><p>{e(a)}</p></div>' for q, a in kisaca) + '</section>'
    if pid in DERIN:
        dd = DERIN[pid]
        rows_ = ''.join(f'<tr><th scope="row">{e(i)}</th><td><span class="kv {k}">{KAN_AD[k]}</span></td><td>{e(n)}</td></tr>' for i, k, n in dd['iddia'])
        derhtml += f'<section class="sec"><h2>Faydaları ne kadar kanıtlı?</h2><p class="muted-s">İnternette {e(p["tr"].replace("I","ı").replace("İ","i").lower())} için sık tekrarlanan iddialar ve bilimin bugün söyledikleri.</p><div class="tablewrap"><table class="cmp etk kanit"><thead><tr><th scope="col">İddia</th><th scope="col">Kanıt</th><th scope="col">Açıklama</th></tr></thead><tbody>{rows_}</tbody></table></div></section>'
        derhtml += '<section class="sec"><h2>Sık yapılan hatalar</h2><ul class="hatalar">' + ''.join(f'<li>{e(h)}</li>' for h in dd['hata']) + '</ul></section>'
        derhtml += '<section class="sec"><h2>Sık sorulanlar</h2><div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in dd['sss']) + '</div></section>'
        faqld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in dd['sss']]}
    if pid in ETK:
        rows_ = ''.join(f'<tr><th scope="row">{e(g)}</th><td>{e(w)}</td></tr>' for g, w in ETK[pid])
        etkhtml = f'<section class="sec"><h2>İlaç etkileşimleri</h2><div class="tablewrap"><table class="cmp etk"><thead><tr><th scope="col">İlaç ya da madde</th><th scope="col">Neden önemli</th></tr></thead><tbody>{rows_}</tbody></table></div><p class="muted-s">Bu liste eksiksiz değildir. Düzenli ilaç kullanıyorsan {e(p["tr"])} denemeden önce eczacına ya da hekimine sor.</p></section>'
    def _sim(q):
        return 2 * len(set(q['bolge']) & set(p['bolge'])) + len(set(q['kat']) & set(p['kat'])) + (2 if q['fam'] == p['fam'] else 0)
    similar = sorted((q for q in P if q['id'] != pid and q['id'] not in rel), key=lambda q: (-_sim(q), q['no']))[:3]
    simhtml = '<section class="sec"><h2>Benzer bitkiler</h2><div class="grid sim">' + ''.join(card(q) for q in similar) + '</div></section>'
    mybridges = [(i, x) for i, x in enumerate(BR, 1) if pid in (x['a'], x.get('b'))]
    brlinks = ''.join(f'<a class="cta" href="/kopruler/{slug_of(x)}/">Karşılaştırmayı oku: {e(x["t"])} →</a>' for i, x in mybridges)
    if rel:
        relhtml = '<section class="sec"><h2>Kültür köprüsü</h2><div class="related">' + ''.join(f'<a class="chip" href="/{r}/">{"".join(dot(x) for x in byId[r]["bolge"])}{e(byId[r]["tr"])}</a>' for r in rel) + '</div></section>'
    ek = EK.get(pid, {})
    kor = KORUMA.get(pid)
    y = YASAL.get(pid)
    yas = ''
    if y or (p.get('yasal') and pid not in ('sigla', 'palosanto', 'akadacayi', 'salep')):
        inner = ''
        if y: inner += f'<div class="callout yasal {y[0]}"><div class="lvl">{YASAL_AD[y[0]]}</div><p>{e(y[1])}</p></div>'
        if p.get('yasal') and pid not in ('sigla', 'palosanto', 'akadacayi', 'salep'): inner += f'<p><b>Diğer ülkeler:</b> {e(p["yasal"])}</p>'
        yas = f'<section class="sec"><h2>Yasal durum</h2>{inner}</section>'
    korhtml = ''
    if kor:
        rows = []
        if kor.get('iucn'): rows.append(f'<div><dt>IUCN Kırmızı Liste</dt><dd>{e(kor["iucn"])}</dd></div>')
        if kor.get('cites'): rows.append(f'<div><dt>CITES</dt><dd>{e(kor["cites"])}</dd></div>')
        alt = f'<div class="alt"><b>Sürdürülebilir alternatif:</b> {e(kor["alternatif"])}</div>' if kor.get('alternatif') else ''
        korhtml = f'<section class="sec"><h2>Koruma durumu</h2>{"<dl class=meta>" + "".join(rows) + "</dl>" if rows else ""}<p>{e(kor["not_"])}</p>{alt}</section>'
    dogada = ''
    if ek:
        dogada = f'''<section class="sec"><h2>Doğada</h2><dl class="meta wide">
      <div><dt>Nerede yetişir</dt><dd>{e(ek["yetisme"])}</dd></div>
      <div><dt>Toplama mevsimi</dt><dd>{e(ek["mevsim"])}</dd></div>
      <div><dt>Yöresel adlar</dt><dd>{e(ek["yoresel"])}</dd></div>
    </dl></section>
  <section class="sec"><h2>Karıştırma riski</h2><div class="callout orta"><p>{e(ek["karisma"])}</p></div></section>'''
    body = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/katalog/">Katalog</a><span>/</span><span>{e(p["tr"])}</span></nav>
<article class="sheet">
  <header class="sheet-head">
    <div class="titles">
      <span class="eyebrow">{acc(p["no"])} · {fam_link(p)}</span>
      <h1>{e(p["tr"])}</h1>
      <span class="latin">{e(p["la"])}</span>
      <div class="badges"><span class="ev">{pips(p["kanit"])} Kanıt: {KANIT[p["kanit"]]["ad"]}</span><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span>{tags(p).replace('<div class="tags">','').replace('</div>','')}</div>
      <p class="intro">{e(p["ilginc"])}</p>
      <dl class="meta">
    <div><dt>Diğer adlar</dt><dd>{e(p["diger"])}</dd></div>
    <div><dt>Kullanılan kısım</dt><dd>{e(p["kisim"])}</dd></div>
    <div><dt>Bölge</dt><dd>{"<br>".join(dot(r) + " " + e(REG[r]["ad"]) for r in p["bolge"])}</dd></div>
    <div><dt>Kullanım</dt><dd>{", ".join(KAT[k] for k in p["kat"])}</dd></div>
  </dl>
    </div>
    <figure class="photo">{ph(p, 960, eager=True)}<figcaption>{credit(p)}</figcaption></figure>
  </header>
  {kisahtml}
  <!--TOC-->
  <section class="sec"><h2>Geleneksel kullanım</h2><div class="uses">{uses}</div></section>
  {dogada}
  <section class="sec"><h2>Hazırlama</h2><p>{e(p["haz"])}</p></section>
  <section class="sec"><h2>Bilim ne diyor</h2><p>{e(p["bilim"])}</p></section>
  {derhtml}
  <section class="sec"><h2>Güvenlik</h2><div class="callout {p["guv"]}"><div class="lvl">{GUV[p["guv"]]}</div><p>{e(p["guvNot"])}</p></div></section>
  {etkhtml}
  {yas}
  {korhtml}
  {relhtml}
  {('<p class="brlinks">' + brlinks + '</p>') if brlinks else ''}
  {simhtml}
  {contrib(p)}
  <section class="sec"><h2>Kaynaklar</h2>{refs(p)}</section>
  <aside class="disclaimer" role="note"><b>Tıbbi tavsiye değildir.</b> Bu sayfa geleneksel kullanımları kültürel bir kayıt olarak anlatır ve bilimsel bilgiyi özetler; teşhis ya da tedavi önerisi değildir. {e(p["tr"])} ya da başka bir bitkiyi kullanmadan önce, özellikle ilaç kullanıyorsan, hamileysen, emziriyorsan ya da bir hastalığın varsa hekimine veya eczacına danış. Zehirlenme şüphesinde Ulusal Zehir Danışma Merkezi’ni (UZEM) <b>114</b> numaradan ara.</aside>
  <p class="updated">Hazırlayan: <a href="/yontem/#hazirlayan">Edanaz Tınmazlar</a> · {('Eklendi: <time datetime="' + YENI[pid].isoformat() + '">' + tr_date(YENI[pid]).rsplit(',', 1)[0] + '</time> · ') if pid in YENI else ''}Son gözden geçirme: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time></p>
  <p class="igcta">Her gün yeni bir bitki: <a href="https://www.instagram.com/bitkitabani/" rel="noopener">Instagram’da @bitkitabani</a></p>
  <div class="sheet-foot">
    <div class="learnbox"><button type="button" class="learn" id="learnBtn" data-id="{pid}" aria-pressed="false">Öğrendim olarak işaretle</button><span class="muted-s">Bu tarayıcıda saklanır. <a href="/hesap/">Google ile giriş yaparsan</a> bütün cihazlarında görünür.</span><span class="muted-s streak" id="streakNote"></span></div>
    <div class="pager"><a href="/{prev["id"]}/">← {e(prev["tr"])}</a><a href="/{nxt["id"]}/">{e(nxt["tr"])} →</a></div>
  </div>
</article>
'''
    body = toc_and_ids(body)
    allqa = kisaca + (DERIN[pid]['sss'] if pid in DERIN else [])
    faqld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in allqa]}
    crumbs = [crumbs, faqld]
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>'
    write(f'/{pid}/', page(title, desc_for(p), f'/{pid}/', body, 'plant', '<script src="/assets/streak.js" defer></script><script src="/assets/plant.js" defer></script>', narrow=True, extra=extra, image=(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None)))

# ---------- familya sayfaları ----------
FAM_URLS = []
for f, n in sorted(FAMC.items()):
    if n < 2: continue
    ps = [p for p in P if p['fam'] == f]; trn = FAM_TR.get(f)
    others = ' · '.join(f'<a href="/familya/{fam_slug(g)}/" lang="la">{g}</a>' for g, m in sorted(FAMC.items()) if m >= 2 and g != f)
    fb = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/katalog/">Katalog</a><span>/</span><span lang="la">{f}</span></nav>
<header class="page-head"><span class="eyebrow">Familya · {n} bitki</span><h1 lang="la">{f}</h1><p>{(trn[0].upper() + trn[1:] + ' familyası. ') if trn else ''}Bitki Tabanı’nda bu familyadan {n} bitki var: {", ".join(e(p["tr"]) for p in ps)}. Aynı familyadaki bitkiler çoğu zaman benzer kimyasal bileşikler taşır.</p></header>
<div class="grid">{"".join(card(p) for p in ps)}</div>
<section class="sec"><h2>Diğer familyalar</h2><p class="famlist">{others}</p></section>'''
    url = f'/familya/{fam_slug(f)}/'; FAM_URLS.append(url)
    ldf = {"@context":"https://schema.org","@type":"CollectionPage","name":f,"url":BASE+url,"inLanguage":"tr","mainEntity":{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":k+1,"url":f'{BASE}/{p["id"]}/',"name":p['tr']} for k, p in enumerate(ps)]}}
    write(url, page(f'{f}{" (" + trn + ")" if trn else ""}: {n} şifalı bitki | Bitki Tabanı', f'{f} familyasından {n} şifalı ve ritüel bitkisi: ' + ', '.join(p['tr'] for p in ps)[:110] + '.', url, fb, 'kat',
          extra=f'<script type="application/ld+json">{json.dumps(ldf, ensure_ascii=False)}</script>'))

# ---------- mevsim (Anadolu'da şu an toplananlar) ----------
_AY = {m.lower(): i+1 for i, m in enumerate(AYLAR)}
def months_of(txt):
    t = txt.lower()
    if 'yıl boyu' in t or 'toplanmamalı' in t or 'önerilmez' in t or 'sonra sökülür' in t: return set()
    ms = set()
    for a, c in _re.findall(r'(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)\w*\s*[–-]\s*(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)', t):
        x, y = _AY[a], _AY[c]
        while True:
            ms.add(x)
            if x == y: break
            x = x % 12 + 1
    for m in _re.findall(r'(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)', t): ms.add(_AY[m])
    if 'sonbahar' in t: ms |= {9, 10, 11}
    if 'ilkbahar' in t or _re.search(r'(?<!son)bahar', t): ms |= {3, 4, 5}
    if _re.search(r'\byaz', t): ms |= {6, 7, 8}
    if _re.search(r'\bkış', t): ms |= {12, 1, 2}
    return ms
season = [p for p in P if 'anadolu' in p['bolge'] and p['guv'] != 'yuksek' and p['id'] not in YASAL and not p.get('yasal') and not KORUMA.get(p['id'], {}).get('rozet') and LOCAL_DAY.month in months_of(EK[p['id']]['mevsim'])]

# ---------- katalog ----------

def cnt(fn): return sum(1 for p in P if fn(p))
regs = [(k, v) for k, v in REG.items() if cnt(lambda p: k in p['bolge']) >= 3]
REG_LIST = ', '.join(v['ad'].split(' ve ')[0] for k, v in regs[:-1]) + ' ve ' + regs[-1][1]['ad']
durum = [('yasak', 'Türkiye’de yasak', lambda p: YASAL.get(p['id'], ('',))[0] == 'yasak'),
         ('kisitli', 'Türkiye’de kısıtlı veya lisanslı', lambda p: YASAL.get(p['id'], ('',))[0] in ('kisitli', 'lisansli')),
         ('koruma', 'Koruma gerektiren', lambda p: bool(KORUMA.get(p['id'], {}).get('rozet')))]
groups = [('bolge','Bölge',[(k,v['ad'],dot(k),cnt(lambda p,k=k: k in p['bolge'])) for k,v in regs]),
          ('kat','Kullanım',[(k,v,'',cnt(lambda p,k=k: k in p['kat'])) for k,v in KAT.items()]),
          ('kanit','Kanıt düzeyi',[(k,v['ad'],pips(k),cnt(lambda p,k=k: p['kanit']==k)) for k,v in KANIT.items()]),
          ('guv','Güvenlik',[(k,v,f'<span class="dot" style="background:var(--s-{k})"></span>',cnt(lambda p,k=k: p['guv']==k)) for k,v in GUV.items()]),
          ('durum','Yasal ve koruma',[(k,v,'',cnt(fn)) for k,v,fn in durum])]
filters = ''.join(f'<div class="fgroup"><span>{lab}</span><div class="chips">' + ''.join(f'<button type="button" class="chip" data-g="{g}" data-k="{k}" aria-pressed="false">{ic}{e(v)} <span class="n">{n}</span></button>' for k,v,ic,n in opts) + '</div></div>' for g,lab,opts in groups)
FEATURED = ['uzerlik','ayahuasca','salep','maca','kantaron','koka','kina','huito','safran','guarana','sigla','peyote']
learn_note = '<p class="hint" id="learnHint"><b>Öğrendiklerim</b> sayacı, bitki sayfalarının sonundaki “Öğrendim” düğmesiyle işaretlediğin bitkileri gösterir. Giriş yapmadan da çalışır; o zaman yalnızca bu tarayıcıda saklanır. <a href="/hesap/">Google ile giriş yaparsan</a> bütün cihazlarında görünür.</p>'
katalog = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Katalog</span></nav>
<header class="page-head"><span class="eyebrow">{len(P)} kayıt</span><h1>Bitki kataloğu</h1><p>Bütün bitkileri bölgeye, kullanıma, kanıt düzeyine, güvenliğe ve yasal duruma göre süz. Seçtiğin filtreler adres çubuğuna yazılır; bağlantıyı paylaşabilirsin.</p></header>
<div class="stats"><span><strong>{len(P)}</strong> bitki</span><span><strong>{len(regs)}</strong> bölge</span><span><strong>{len(BR)}</strong> kültür köprüsü</span><span>Öğrendiklerim <strong id="learnedCount">0</strong>/{len(P)} <span class="muted-s">(<a href="/hesap/">giriş yaparsan</a> her cihazda)</span></span></div>
{learn_note}
<section style="display:flex;flex-direction:column;gap:18px" aria-label="Katalog">
  <div class="controls">
    <label class="search" for="q">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="2" fill="none"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="q" type="search" placeholder="Bitki, Latince ad, kullanım ara… (ör. nazar, öksürük, tütsü)" autocomplete="off" aria-label="Bitki ara">
    </label>
    <details class="fbox" open><summary>Filtreler</summary><div class="fgroups">{filters}</div></details>
  </div>
  <div class="resultbar"><span id="count" aria-live="polite">{len(P)} / {len(P)} kayıt gösteriliyor</span><button class="linkbtn" id="reset" type="button" hidden>Filtreleri temizle</button></div>
  <div class="grid">{"".join(card(p) for p in P)}</div>
  <div class="empty" id="empty" hidden>Bu arama ve filtrelerle eşleşen bitki yok. Bir filtreyi kaldırmayı ya da farklı bir kelime denemeyi dene.</div>
</section>
'''
ld_kat = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Bitki kataloğu","url":BASE+"/katalog/","inLanguage":"tr","isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},
           "mainEntity":{"@type":"ItemList","numberOfItems":len(P),"itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{BASE}/{p["id"]}/',"name":p['tr']} for i,p in enumerate(P)]}},
          {"@context":"https://schema.org","@type":"Dataset","name":"Bitki Tabanı: şifalı ve ritüel bitkiler veri seti","description":f"Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika’dan {len(P)} şifalı ve ritüel bitkisinin geleneksel kullanımı, bilimsel kanıt düzeyi, güvenlik, koruma ve yasal durumu.","url":BASE+"/katalog/","inLanguage":"tr","creator":{"@type":"Organization","name":"Bitki Tabanı","url":BASE+"/"},"keywords":["şifalı bitkiler","etnobotanik","geleneksel tıp","Anadolu","Amazon","And Dağları"],"variableMeasured":["Geleneksel kullanım","Kanıt düzeyi","Güvenlik","Koruma durumu","Türkiye’de yasal durum"],"isAccessibleForFree":True}]
write('/katalog/', page(f'Bitki kataloğu: {len(P)} şifalı ve ritüel bitki | Bitki Tabanı', f'{len(P)} şifalı ve ritüel bitkiyi bölgeye, kullanıma, bilimsel kanıta, güvenliğe ve Türkiye’deki yasal duruma göre süz.', '/katalog/', katalog, 'kat', '<script src="/assets/catalog.js" defer></script>', extra=''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld_kat)))

# ---------- köprüler ----------
def mini(p):
    return f'<a class="mini" href="/{p["id"]}/"><span class="where">{"".join(dot(r) for r in p["bolge"])} {e(" · ".join(REG[r]["ad"] for r in p["bolge"]))}</span><b>{e(p["tr"])}</b><span class="latin">{e(p["la"])}</span></a>'
def bridge_map(only=None):
    x0 = mapgeo.project(-128, 0)[0]; x1 = mapgeo.project(128, 0)[0]
    y0 = mapgeo.project(0, 66)[1]; y1 = mapgeo.project(0, -42)[1]
    K = [0.10, 0.30, 0.20, 0.42, 0.14, 0.36, 0.24, 0.50, 0.06, 0.26, 0.46, 0.18, 0.34, 0.04, 0.22, 0.40]
    T = [0.50, 0.40, 0.60, 0.40, 0.66, 0.46, 0.55, 0.20, 0.62, 0.16, 0.72, 0.68, 0.88, 0.45, 0.25, 0.58]
    out = [f'<svg class="map{" focus" if only else ""}" viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}" role="img" aria-labelledby="mapTitle{only or ''}"><title id="mapTitle{only or ''}">Kültür köprüleri haritası: Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika arasındaki bitki bağlantıları</title>',
           f'<path class="land" d="{mapgeo.land_path()}"/>']
    for i, pts in enumerate(BR_GEO, 1):
        P0 = mapgeo.project(*pts[0][:2])
        g = [f'<g class="arc{" on" if only == i else ""}" data-i="{i}">']
        labels, mids = [], []
        for j, pt in enumerate(pts[1:]):
            P1 = mapgeo.project(*pt[:2])
            dx, dy = P1[0] - P0[0], P1[1] - P0[1]
            d = math.hypot(dx, dy) or 1
            nx, ny = -dy / d, dx / d
            if ny > 0: nx, ny = -nx, -ny          # yay hep kuzeye doğru kabarsın
            k = K[(i - 1) % len(K)] + 0.06 * j
            C = ((P0[0] + P1[0]) / 2 + nx * d * k, (P0[1] + P1[1]) / 2 + ny * d * k)
            g.append(f'<path class="line" d="M{P0[0]} {P0[1]} Q{C[0]:.1f} {C[1]:.1f} {P1[0]} {P1[1]}"/>')
            t = T[(i - 1) % len(T)]
            mids.append(((1-t)**2 * P0[0] + 2*(1-t)*t * C[0] + t*t * P1[0], (1-t)**2 * P0[1] + 2*(1-t)*t * C[1] + t*t * P1[1]))
        for pt in pts:
            x, y = mapgeo.project(*pt[:2])
            g.append(f'<circle class="end" cx="{x}" cy="{y}" r="4.5" style="fill:var({REG[pt[3]]["c"]})"/>')
            anchor = 'start' if (x < x0 + 140 or x > 420) and not x > x1 - 160 else 'end'
            dxl = -9 if anchor == 'end' else 9
            g.append(f'<text class="lbl" x="{x + dxl}" y="{y + 4}" text-anchor="{anchor}">{e(pt[2])}</text>')
        mx, my = mids[0]
        g.append(f'<a href="/kopruler/{slug_of(BR[i-1])}/" class="num" aria-label="Köprü {i}: {e(BR[i-1]["t"])}"><circle cx="{mx:.1f}" cy="{my:.1f}" r="11"/><text x="{mx:.1f}" y="{my + 4:.1f}" text-anchor="middle">{i}</text></a>')
        g.append('</g>')
        out.append(''.join(g))
    out.append('</svg>')
    return ''.join(out)

items = []
for i, b in enumerate(BR, 1):
    a = byId[b['a']]; c = byId.get(b.get('b')) if b.get('b') else None
    txt = f'<div class="txt"><h2><span class="bn">{i}</span><a href="/kopruler/{slug_of(b)}/">{e(b["t"])}</a></h2><p>{e(b["d"])}</p><p><a class="cta" href="/kopruler/{slug_of(b)}/">Karşılaştırmayı oku →</a></p></div>'
    items.append(f'<article class="bridge" id="kopru-{i}" data-i="{i}" tabindex="-1">{mini(a)}<span class="arrow" aria-hidden="true">↔</span>{mini(c)}{txt}</article>' if c else f'<article class="bridge single" id="kopru-{i}" data-i="{i}" tabindex="-1">{mini(a)}<span class="note">Aynı bitki, birden fazla kültür</span>{txt}</article>')
br = f'''<header class="page-head"><span class="eyebrow">{len(BR)} karşılaştırma</span><h1>Kültür köprüleri</h1><p>Birbirinden binlerce kilometre uzaktaki kültürler, çoğu zaman aynı molekülleri ya da aynı bitkiyi benzer dertlere kullanmış. Haritadaki her yay bir köprü; üzerine gel ya da aşağıdaki listeden birini seç.</p></header>
<figure class="mapwrap">{bridge_map()}<figcaption>Harita: Natural Earth (kamu malı), Natural Earth izdüşümü. Noktalar bölgeyi temsil eder, kesin toplama yerini değil.</figcaption></figure>
<div class="bridges">{"".join(items)}</div>'''
write('/kopruler/', page(f'Kültür köprüleri haritası: {len(BR)} bitki karşılaştırması | Bitki Tabanı', f'{REG_LIST} arasındaki {len(BR)} kültür köprüsü: üzerlik ve ayahuasca, efedra ve koka, salep ve maca gibi bitkileri yan yana karşılaştır.', '/kopruler/', br, 'br', '<script src="/assets/kopruler.js" defer></script>'))

# ---------- köprü karşılaştırma sayfaları ----------
def cmp_rows(ps):
    yas = lambda q: YASAL_AD[YASAL[q['id']][0]] if q['id'] in YASAL else 'Özel bir kısıt yok'
    rows = [('Latince adı', lambda q: f'<i>{e(q["la"])}</i>'), ('Familya', lambda q: e(q['fam'])), ('Bölge', lambda q: ', '.join(e(REG[r]['ad']) for r in q['bolge'])),
            ('Kullanılan kısım', lambda q: e(q['kisim'])), ('Kullanım', lambda q: ', '.join(KAT[k] for k in q['kat'])), ('Bilimsel kanıt', lambda q: KANIT[q['kanit']]['ad']),
            ('Güvenlik', lambda q: f'<span class="sf {q["guv"]}">{GUV[q["guv"]]}</span>'), ('Türkiye’de yasal durum', yas)]
    head = '<tr><th scope="col"></th>' + ''.join(f'<th scope="col"><a href="/{q["id"]}/">{e(q["tr"])}</a></th>' for q in ps) + '</tr>'
    body = ''.join('<tr><th scope="row">' + lab + '</th>' + ''.join(f'<td>{fn(q)}</td>' for q in ps) + '</tr>' for lab, fn in rows)
    return f'<div class="tablewrap"><table class="cmp"><thead>{head}</thead><tbody>{body}</tbody></table></div>'

for i, br_ in enumerate(BR, 1):
    slug = slug_of(br_); a = byId[br_['a']]; c = byId.get(br_.get('b')) if br_.get('b') else None
    ps = [a] + ([c] if c else [])
    title_names = f'{a["tr"]} ve {c["tr"]}' if c else a['tr']
    blocks = ''
    for q in ps:
        uses = ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(t)}</p></div>' for w, t in q['kul'])
        blocks += f'<section class="sec"><h2>{e(q["tr"])}</h2><div class="uses">{uses}</div><p><b>Bilim:</b> {e(q["bilim"])}</p><p><b>Güvenlik:</b> {e(q["guvNot"])}</p><p><a class="cta" href="/{q["id"]}/">{e(q["tr"])} sayfasının tamamı →</a></p></section>'
    others = ''.join(f'<li><a href="/kopruler/{slug_of(x)}/">{e(x["t"])}</a></li>' for x in BR if x is not br_)
    prev_, next_ = BR[i-2], BR[i % len(BR)]
    body = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/kopruler/">Kültür köprüleri</a><span>/</span><span>{e(br_["t"])}</span></nav>
<article class="sheet">
<header class="page-head"><span class="eyebrow">Kültür köprüsü {i} · {e(title_names)}</span><h1>{e(br_["t"])}</h1><p>{e(br_["d"])}</p></header>
<figure class="mapwrap">{bridge_map(only=i)}<figcaption>Harita: Natural Earth (kamu malı). Noktalar bölgeyi temsil eder, kesin toplama yerini değil.</figcaption></figure>
<section class="sec"><h2>Yan yana</h2>{cmp_rows(ps)}</section>
{blocks}
<aside class="disclaimer" role="note"><b>Tıbbi tavsiye değildir.</b> Bu sayfa geleneksel kullanımları kültürel bir kayıt olarak karşılaştırır; teşhis ya da tedavi önerisi değildir. Herhangi bir bitkiyi kullanmadan önce hekimine ya da eczacına danış. Zehirlenme şüphesinde Ulusal Zehir Danışma Merkezi’ni (UZEM) <b>114</b> numaradan ara.</aside>
<p class="updated">Son gözden geçirme: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time></p>
<section class="sec"><h2>Diğer köprüler</h2><ul class="otherlist">{others}</ul></section>
<div class="sheet-foot"><a class="cta" href="/kopruler/">Bütün köprüler ve harita →</a><div class="pager"><a href="/kopruler/{slug_of(prev_)}/">← {e(prev_["t"])}</a><a href="/kopruler/{slug_of(next_)}/">{e(next_["t"])} →</a></div></div>
</article>'''
    ldb = [{"@context":"https://schema.org","@type":"Article","author":AUTHOR,"headline":br_['t'],"description":br_['d'],"inLanguage":"tr","url":f'{BASE}/kopruler/{slug}/',"dateModified":CONTENT_DATE,
            "about":[{"@type":"Taxon","name":short_la(q),"alternateName":q['tr']} for q in ps],"isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},
            "image":[f'{BASE}/img/{q["id"]}-960.jpg' for q in ps if q['id'] in IMG]},
           {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Kültür köprüleri","item":BASE+"/kopruler/"},{"@type":"ListItem","position":3,"name":br_['t'],"item":f'{BASE}/kopruler/{slug}/'}]}]
    desc = (f'{title_names}: ' + br_['d'])[:157]
    write(f'/kopruler/{slug}/', page(f'{br_["t"]}: {title_names} | Bitki Tabanı', desc, f'/kopruler/{slug}/', body, 'br', narrow=True,
          extra=''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ldb), image=(f'{BASE}/img/{a["id"]}-960.jpg' if a['id'] in IMG else None)))

# ---------- hakkında ----------
about = '''<header class="page-head"><span class="eyebrow">Hakkında</span><h1>Bitki Tabanı nedir?</h1></header>
<section class="sec"><p>Bitki Tabanı, farklı kültürlerde şifa ve ritüel için kullanılan bitkileri bir araya getiren bağımsız bir etnobotanik kayıt defteridir. Amacı merak uyandırmak ve geleneksel bilgiyi bugünkü bilimsel bilgiyle yan yana koymak.</p></section>
<section class="sec"><h2>Kim hazırlıyor</h2><p>''' + BIO + '''</p><p>''' + SOCIAL + ''' · <a href="/yontem/">Kayıtları nasıl hazırladığını oku →</a></p></section>
<section class="sec"><h2>Ticari değil</h2><p>Bitki Tabanı hiçbir ürün, bitki, takviye ya da tören satmaz; inziva veya ayahuasca seremonisi düzenlemez, bunlara yönlendirmez ve reklam almaz. Kayıtlarda adı geçen hiçbir marka ya da satıcıyla bağı yoktur.</p></section>
<section class="sec"><h2>İletişim</h2><p>Bir hata gördüysen ya da yöresel bir kullanım biliyorsan <a href="mailto:iletisim@bitkitabani.com">iletisim@bitkitabani.com</a> adresine yaz.</p></section>
<section class="sec"><h2>Kayıtlar nasıl hazırlanıyor</h2><p>Ayrıntılı kurallar <a href="/yontem/">Yöntem</a> sayfasında. Her kayıt; geleneksel kullanımı, hazırlama biçimini, bilimin bugün ne söylediğini ve güvenlik notlarını içerir. Kanıt düzeyi Avrupa İlaç Ajansı (EMA/HMPC) monografileri, ABD NCCIH özetleri, Cochrane derlemeleri ve hakemli literatüre göre belirlenir. Kaynaklar her bitkinin sayfasının sonunda listelenir.</p></section>
<section class="sec"><h2>Önemli not</h2><p>Bu site tıbbi tavsiye vermez. Burada anlatılan geleneksel kullanımlar bir öneri değil, kültürel bir kayıttır. Zehirli ve yasal kısıtlı bitkiler, tarihleri ve riskleri anlaşılsın diye yer alır. Herhangi bir bitkiyi kullanmadan önce bir hekime ya da eczacıya danış.</p></section>
<section class="sec"><h2>Yerel bilgiye saygı</h2><p>Kayıtlardaki geleneksel bilgi, onu kuşaklar boyunca koruyan toplulukların mirasıdır. Bitki Tabanı bu bilginin kaynağını görünür kılmayı ve aşırı toplanan türler konusunda farkındalık yaratmayı amaçlar.</p></section>
<section class="sec"><h2>Renklerimiz ve motifimiz</h2><p>Sitenin renkleri, Anadolu ile Amazon ve And Dağları’nın ortak boya geleneklerinden geliyor. Motif ise Anadolu kilimlerindeki göz ve baklava desenini, Shipibo halkının kené çizgileri ve And dokumalarının basamaklı baklavasıyla birleştiriyor.</p>
<div class="palette">
<div class="swatch"><i style="background:var(--accent)"></i><b>Kırmızı</b><span>Anadolu’da kök boya ve kırmız böceği (“kırmızı” kelimesi buradan gelir); And’larda koşnil, Amazon’da achiote.</span></div>
<div class="swatch"><i style="background:var(--indigo)"></i><b>Çivit</b><span>Anadolu kilimlerinin çivit mavisi; Amazon’da huito meyvesiyle yapılan lacivert beden boyası.</span></div>
<div class="swatch"><i style="background:var(--ochre)"></i><b>Safran</b><span>Anadolu’da safran ve cehri sarısı; And dokumalarının toprak sarısı tonları.</span></div>
<div class="swatch"><i style="background:var(--paper);border:1px solid var(--rule)"></i><b>Yün</b><span>Boyanmamış yünün doğal rengi; iki coğrafyada da dokumanın zemini.</span></div>
</div></section>
<section class="sec"><h2>Görseller</h2><p>Fotoğraflar Wikimedia Commons’tan özgür lisanslarla kullanılır. Hepsi aynı dikey kadrajda, bitkiyi tanıtan kısma yakın çekimdir; yazar ve lisans bilgisi her fotoğrafın altında yazar.</p></section>'''
write('/hakkinda/', page('Hakkında | Bitki Tabanı', 'Bitki Tabanı’nın amacı, kayıtların nasıl hazırlandığı ve kaynak yaklaşımı.', '/hakkinda/', about, 'about', narrow=True))


# ---------- fotoğraf seçim sayfası (gizli) ----------
def taxon_of(p):
    t = POWO.get(p['id']) or short_la(p)
    t = re.sub(r'\s+ve diğer.*$', '', t)
    return 'Amanita muscaria' if p['id'] == 'sinekmantari' else t
order = sorted(P, key=lambda p: (p['id'] in FILES, p['no']))
def pickrow(p):
    m = IMG.get(p['id'], {})
    durum = 'Elle seçildi' if p['id'] in FILES else ('Otomatik seçildi, onay bekliyor' if m else 'Fotoğraf yok')
    return f'<section class="pick-row" data-id="{p["id"]}" data-taxon="{e(taxon_of(p))}"><h2>{acc(p["no"])} · {e(p["tr"])} <span class="latin">{e(taxon_of(p))}</span> <span class="lg">{durum}</span></h2><div class="cands"><p class="muted">Adaylar yükleniyor…</p></div></section>'
rows = ''.join(pickrow(p) for p in order)
secim = f'''<header class="page-head"><span class="eyebrow">Yalnızca yönetici için</span><h1>Fotoğraf seçimi</h1><p>Otomatik seçilen fotoğraflar en üstte. Beğenmediğin bitki için daha iyi bir yakın çekime tıkla; beğendiklerine dokunmana gerek yok. Seçimlerin bu tarayıcıda saklanır. Bitince alttaki listeyi kopyalayıp Claude’a gönder.</p></header>
{rows}
<div class="result-box"><div class="row"><span id="done"></span><button type="button" id="copy">Listeyi kopyala</button><span id="copied"></span></div><textarea id="result" readonly aria-label="Seçim listesi"></textarea></div>'''
write('/secim/', page('Fotoğraf seçimi | Bitki Tabanı', 'Fotoğraf seçimi', '/secim/', secim, '', '<script src="/assets/photo.js" defer></script><script src="/assets/secim.js" defer></script>', extra='<meta name="robots" content="noindex, nofollow">'))


# ---------- ana sayfa ----------
pool = [p for p in P if p['guv'] != 'yuksek']
def day_pick(d):
    pl = [p for p in pool if YENI.get(p['id'], datetime.date.min) <= d]
    return pl[(d - datetime.date(1970, 1, 1)).days % len(pl)]
today_p = day_pick(LOCAL_DAY)
LEDE = f'{REG_LIST}’dan {len(P)} şifalı ve ritüel bitkisi. Her kayıtta geleneksel kullanım, bilimin söyledikleri, güvenlik notu ve kaynaklar bir arada.'

REG_TXT = {'anadolu':'Nazar tütsüsünden kına gecesine, Anadolu’nun şifa ve ritüel otları.','asya':'İskit tütsülerinden Sibirya şamanlarına, bozkırın ve taygaların bitkileri.',
           'and':'Koka yaprağından kantuta çiçeğine, And Dağları’nın kutsal bitkileri.','amazon':'Ayahuasca sarmaşığından huito boyasına, yağmur ormanının öğretmen bitkileri.',
           'kamerika':'Ak adaçayından peyoteye, Kuzey Amerika yerli halklarının bitkileri.'}
regcards = ''.join(f'<a class="regcard" href="/katalog/?bolge={k}"><span class="where">{dot(k)} {e(v["ad"])}</span><b>{cnt(lambda p,k=k: k in p["bolge"])} bitki</b><span>{e(REG_TXT.get(k,""))}</span></a>' for k,v in regs)

# ---------- her gün yeni bitki: ana sayfa bandı ----------
IG_URL = 'https://www.instagram.com/bitkitabani/'
NEXT_Q = min(KUYRUK_LEFT, key=lambda q: q['yayin']) if KUYRUK_LEFT else None
def teaser():
    if not NEXT_Q: return ''
    nd = datetime.date.fromisoformat(NEXT_Q['yayin'])
    when = 'Yarın' if (nd - LOCAL_DAY).days == 1 else tr_date(nd).rsplit(',', 1)[0]
    return f'<p class="teaser"><b>{when}:</b> {e(REG[NEXT_Q["bolge"][0]]["ad"])} bölgesinden yeni bir bitki geliyor.</p>'
def newband():
    if not NEWEST: return ''
    np_ = byId[NEWEST[0]]; d0 = YENI[np_['id']]
    lab = 'Bugün eklendi' if d0 == LOCAL_DAY else 'Dün eklendi' if (LOCAL_DAY - d0).days == 1 else 'Son eklenen · ' + tr_date(d0).rsplit(',', 1)[0]
    prev = ''.join(f'<li><a href="/{i}/">{e(byId[i]["tr"])}</a> <span class="mono-d">{YENI[i].day} {AYLAR[YENI[i].month-1]}</span></li>' for i in NEWEST[1:5])
    return f"""<section class="newband" aria-labelledby="nbh">
  <a class="nb-main" href="/{np_["id"]}/">{ph(np_, 500)}<span class="nb-txt"><span class="eyebrow">{lab}</span><b id="nbh">{e(np_["tr"])}</b><i>{e(short_la(np_))}</i><span class="nb-fact">{e(np_["ilginc"])}</span><span class="cta small">Sayfayı oku →</span></span></a>
  <div class="nb-side"><p class="nb-say"><b>Her gün yeni bir bitki.</b> Katalog her gece bir kayıt büyüyor.</p>{teaser()}{('<ul class="nb-list">' + prev + '</ul>') if prev else ''}<p class="nb-links"><a href="/yeni/">Bütün yeni eklenenler →</a><a href="{IG_URL}" rel="noopener">Instagram’da her gün →</a><a href="/yeni/rss.xml">RSS</a></p></div>
</section>"""
home = f'''
<header class="top">
  <div class="brand">
    <span class="eyebrow">Etnobotanik kayıt defteri</span>
    <h1 class="wordmark">Bitki <em>Tabanı</em></h1>
    <p class="lede">{LEDE}</p>
    <p><a class="cta" href="/katalog/">Kataloğa git →</a></p>
  </div>
  <div class="todaybox"><a class="today" id="today" href="/{today_p["id"]}/" data-pool="{e(json.dumps([[p["id"], p["tr"], p["la"]] for p in pool], ensure_ascii=False))}"><span class="eyebrow">Bugünün bitkisi</span><b id="todayName">{e(today_p["tr"])}</b><i id="todayLatin">{e(today_p["la"])}</i></a><a class="cta small" href="/oyun/">Günün bilmecesini çöz →</a><a class="cta small" href="/gunun-bitkisi/">Geçmiş günlerin bitkileri →</a><p class="streak" id="streak" hidden></p></div>
</header>
{newband()}
<section class="sec"><h2>Bölgelere göre</h2><div class="regs-grid">{regcards}</div></section>
{f'<section class="sec"><h2>Şu an mevsiminde</h2><p>{AYLAR[LOCAL_DAY.month-1]} ayında Anadolu’da toplama mevsimi olan bitkiler. Koruma altındaki ve yasal kısıtlı türler bu listeye alınmaz.</p><div class="grid">' + "".join(card(p) for p in season[:8]) + '</div></section>' if season else ''}
<section class="sec"><h2>Nereden başlamalı?</h2><p>{len(P)} bitki çok gelebilir. Siteyi tanımak için bu beşiyle başla:</p><ol class="start">
<li><a href="/papatya/"><b>Papatya</b></a>: herkesin bildiği bir çayın arkasındaki bilim; “Faydaları ne kadar kanıtlı?” tablosunu da gösterir.</li>
<li><a href="/kantaron/"><b>Sarı kantaron</b></a>: kanıtı güçlü ama ilaç etkileşimleri ciddi; bir bitkinin neden hem şifa hem risk olabildiğini anlatır.</li>
<li><a href="/uzerlik/"><b>Üzerlik</b></a>: nazar dumanından ayahuascaya uzanan bir kültür köprüsü.</li>
<li><a href="/salep/"><b>Salep</b></a>: sevdiğimiz bir içeceğin yabani orkidelere bedeli.</li>
<li><a href="/koka/"><b>Koka</b></a>: And’larda kutsal bir yaprak, başka yerde yasak bir madde.</li>
</ol></section>
<section class="sec"><h2>Öne çıkanlar</h2><div class="grid">{"".join(card(byId[i]) for i in FEATURED if i in byId)}</div><p><a class="cta" href="/katalog/">Bütün {len(P)} bitkiyi gör →</a></p></section>
<section class="sec"><h2>Kültür köprüleri</h2><p>Birbirinden binlerce kilometre uzaktaki kültürler, çoğu zaman aynı molekülleri ya da aynı bitkiyi benzer dertlere kullanmış. {len(BR)} köprüyü haritada gör.</p><div class="mapwrap">{bridge_map()}</div><p><a class="cta" href="/kopruler/">Bütün köprüleri ve karşılaştırmaları gör →</a></p></section>
'''
ldsite = {"@context":"https://schema.org","@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/","inLanguage":"tr","description":"Şifalı ve ritüel bitkiler için Türkçe etnobotanik kayıt defteri."}
write('/index.html', page('Bitki Tabanı: şifalı ve ritüel bitkiler veri tabanı', f'{REG_LIST}’dan {len(P)} şifalı ve ritüel bitkisi: geleneksel kullanım, bilimsel kanıt, güvenlik ve kaynaklar.', '/', home, 'home', '<script src="/assets/streak.js" defer></script><script src="/assets/home.js" defer></script>', extra=f'<script type="application/ld+json">{json.dumps(ldsite, ensure_ascii=False)}</script>'))


# ---------- /yeni/: her gün eklenen bitkiler ----------
nl = ''.join(f'<li><span class="mono-d">{tr_date(YENI[i])}</span><a href="/{i}/">{e(byId[i]["tr"])}</a> <i class="latin">{e(short_la(byId[i]))}</i></li>' for i in NEWEST)
yn = f"""
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Yeni eklenenler</span></nav>
<header class="page-head"><span class="eyebrow">Her gün yeni bir bitki</span><h1>Yeni eklenenler</h1><p>Bitki Tabanı her gece yarısı bir kayıt büyüyor. Her yeni bitki öteki kayıtlar gibi geleneksel kullanım, bilimsel kanıt, güvenlik notu ve kaynaklarla gelir. Şu an katalogda {len(P)} bitki var.</p></header>
{teaser()}
{('<div class="grid">' + ''.join(card(byId[i]) for i in NEWEST[:12]) + '</div>') if NEWEST else '<p>İlk yeni bitki bu gece geliyor.</p>'}
<section class="sec"><h2>Takip et</h2><p><a class="cta" href="{IG_URL}" rel="noopener">Instagram’da her gün bir bitki →</a></p><p><a class="cta" href="/yeni/rss.xml">RSS ile takip et →</a> <span class="muted-s">Bir RSS okuyucusu her yeni bitkiyi getirir; bildirim ya da e-posta yok.</span></p></section>
{('<section class="sec"><h2>Bütün liste</h2><ul class="daylist">' + nl + '</ul></section>') if nl else ''}
"""
write('/yeni/', page(f'Yeni eklenen bitkiler | Bitki Tabanı', f'Bitki Tabanı’na her gün yeni bir şifalı ya da ritüel bitki ekleniyor. Son eklenenler ve tarihleri.', '/yeni/', yn, 'yeni', image=(f'{BASE}/img/{NEWEST[0]}-960.jpg' if NEWEST and NEWEST[0] in IMG else None)))
from email.utils import format_datetime as _fd
_it = ''
for i in NEWEST[:30]:
    q = byId[i]; d = YENI[i]; dt = datetime.datetime(d.year, d.month, d.day, 0, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=3)))
    _it += f'<item><title>Yeni bitki: {e(q["tr"])} ({e(short_la(q))})</title><link>{BASE}/{i}/</link><guid>{BASE}/{i}/</guid><pubDate>{_fd(dt)}</pubDate><description>{e(q["ilginc"])} {e(q["kul"][0][1])}</description></item>'
open(os.path.join(OUT, 'yeni', 'rss.xml'), 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Bitki Tabanı: yeni eklenen bitkiler</title><link>{BASE}/yeni/</link><description>Her gün kataloğa eklenen yeni bitki.</description><language>tr</language>{_it}</channel></rss>')

# ---------- günün bitkisi arşivi ----------
days = [LOCAL_DAY - datetime.timedelta(days=n) for n in range(14)]
tp = today_p
past = ''.join(f'<li><span class="mono-d">{tr_date(d)}</span><a href="/{day_pick(d)["id"]}/">{e(day_pick(d)["tr"])}</a> <i class="latin">{e(short_la(day_pick(d)))}</i></li>' for d in days[1:])
gb = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Günün bitkisi</span></nav>
<header class="page-head"><span class="eyebrow">{tr_date(LOCAL_DAY)}</span><h1>Günün bitkisi: {e(tp["tr"])}</h1><p>Her gün katalogdan bir bitki öne çıkıyor. Ölümcül zehirli ya da yüksek riskli bitkiler bu döngüye alınmaz.</p></header>
<div class="grid sim">{card(tp)}</div>
<section class="sec"><h2>Bugün okumak için</h2><p>{e(tp["kul"][0][1])}</p><p class="fact">{e(tp["ilginc"])}</p><p><a class="cta" href="/{tp["id"]}/">{e(tp["tr"])} sayfasının tamamı →</a></p></section>
<section class="sec"><h2>Her gün</h2><p><a class="cta" href="/oyun/">Günün bilmecesini çöz →</a></p><p><a class="cta" href="/gunun-bitkisi/rss.xml">RSS ile takip et →</a> <span class="muted-s">Bir RSS okuyucusu (Feedly, NetNewsWire gibi) her sabah yeni bitkiyi getirir; bildirim ya da e-posta yok.</span></p></section>
<section class="sec"><h2>Son iki hafta</h2><ul class="daylist">{past}</ul></section>
'''
write('/gunun-bitkisi/', page(f'Günün bitkisi: {tp["tr"]} | Bitki Tabanı', f'Bugünün bitkisi {tp["tr"]} ({short_la(tp)}) ve son iki haftanın bitkileri.', '/gunun-bitkisi/', gb, '', narrow=True,
      image=(f'{BASE}/img/{tp["id"]}-960.jpg' if tp['id'] in IMG else None)))

# ---------- RSS ----------
from email.utils import format_datetime
items = ''
for d in days:
    q = day_pick(d); dt = datetime.datetime(d.year, d.month, d.day, 0, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=3)))
    items += f'<item><title>{e(tr_date(d))}: {e(q["tr"])} ({e(short_la(q))})</title><link>{BASE}/{q["id"]}/</link><guid isPermaLink="false">{BASE}/gunun-bitkisi/#{d.isoformat()}</guid><pubDate>{format_datetime(dt)}</pubDate><description>{e(q["kul"][0][1])} {e(q["ilginc"])}</description></item>'
os.makedirs(os.path.join(OUT, 'gunun-bitkisi'), exist_ok=True)
open(os.path.join(OUT, 'gunun-bitkisi', 'rss.xml'), 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Bitki Tabanı: günün bitkisi</title><link>{BASE}/gunun-bitkisi/</link><description>Her gün bir şifalı ya da ritüel bitkisi.</description><language>tr</language>{items}</channel></rss>')

# ---------- günün bilmecesi ----------
def mask(txt, p):
    words = set()
    for src in [p['tr'], p['diger'], p['la'].split()[0]]:
        for w in _re.split(r'[\s,;/()]+', src):
            w = w.strip('.’\'"')
            if len(w) >= 3 and w.lower() not in ('ve', 'otu', 'ağacı', 'kökü', 'çiçeği', 'yaprağı', 'tohumu'): words.add(w)
    for w in sorted(words, key=len, reverse=True):
        txt = _re.sub(r'(?i)\b' + _re.escape(w) + r'\w*', '＿＿＿', txt)
        txt = _re.sub(r'\b' + _re.escape(w.replace('i', 'İ').replace('ı', 'I').upper()[:1] + w[1:]) + r'\w*', '＿＿＿', txt)
    return txt
gp = []
for q in P:
    c = [['Bölge ve kullanım', ', '.join(REG[r]['ad'] for r in q['bolge']) + ' · ' + ', '.join(KAT[k] for k in q['kat'])],
         ['Kullanılan kısım', q['kisim']],
         ['Familya', q['fam'] + (f' ({FAM_TR[q["fam"]]})' if q['fam'] in FAM_TR else '')],
         ['Geleneksel kullanım', mask(q['kul'][0][0] + ': ' + q['kul'][0][1], q)],
         ['İlginç bilgi', mask(q['ilginc'], q)]]
    if q['id'] in IMG: c.append(['img', f'/img/{q["id"]}-500.jpg'])
    gp.append({'id': q['id'], 'tr': q['tr'], 'la': short_la(q), 'fam': q['fam'], 'bolge': q['bolge'], 'c': c})
opts = ''.join(f'<option value="{e(q["tr"])}">' for q in sorted(P, key=lambda q: q['tr']))
oy = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Günün bilmecesi</span></nav>
<header class="page-head"><span class="eyebrow">Her gün yeni bir bitki</span><h1>Günün bilmecesi</h1><p>Katalogdaki {len(P)} bitkiden biri saklı. İlk ipucuyla tahmin et; her yanlış tahminde yeni bir ipucu açılır. Altı hakkın var. Sarı kare, tahminin bölge ya da familya olarak yakın olduğunu gösterir.</p></header>
<div id="game">
<div class="gprog" id="gprog" aria-live="polite"></div>
<ol class="clues" id="clues"><li class="clue"><p>Bilmece yükleniyor… JavaScript kapalıysa <a href="/gunun-bitkisi/">günün bitkisine</a> bakabilirsin.</p></li></ol>
<form id="guessForm" class="guess" autocomplete="off"><label for="guessInput" class="eyebrow">Tahminin</label><div class="row"><input id="guessInput" list="plantNames" placeholder="Bitki adı yaz, listeden seç" required><button type="submit" class="learn">Tahmin et</button></div><p class="muted-s"><span id="left"></span> <span id="gameMsg" role="status"></span></p><datalist id="plantNames">{opts}</datalist></form>
<ul class="guesses" id="guesses"></ul>
<div class="gameend" id="gameEnd" hidden></div>
</div>
<p class="muted-s">Tahminlerin ve serin yalnızca bu tarayıcıda saklanır.</p>
<script type="application/json" id="gameData">{json.dumps({"p": gp, "ay": AYLAR}, ensure_ascii=False)}</script>'''
write('/oyun/', page('Günün bilmecesi: bitkiyi ipuçlarından bul | Bitki Tabanı', f'Her gün katalogdaki {len(P)} şifalı ve ritüel bitkisinden biri saklı. İpuçlarından bul, sonucunu paylaş.', '/oyun/', oy, '', '<script src="/assets/streak.js" defer></script><script src="/assets/oyun.js" defer></script>', narrow=True))

# ---------- hesap ve gizlilik ----------
hz = f'''
<header class="page-head"><span class="eyebrow">Hesap</span><h1>İlerlemeni sakla</h1><p>Google hesabınla giriş yaparsan öğrendiğin bitkiler, serin ve bilmece sonuçların hesabında saklanır; telefonda da bilgisayarda da aynısını görürsün. Giriş yapmadan da her şey çalışır, yalnızca bu tarayıcıda kalır.</p></header>
<div id="acct" data-client="{e(GOOGLE_CLIENT_ID)}">
<div class="stats"><span>Öğrendiklerim <strong id="stLearned">0</strong></span><span>Seri <strong id="stStreak">0</strong> gün</span><span>Bilmece <strong id="stGames">0</strong> gün</span></div>
<section class="sec" id="acctOut"><h2>Giriş</h2>{'<div id="gbtn"></div>' if GOOGLE_CLIENT_ID else '<p>Google ile giriş çok yakında açılacak.</p>'}<p class="muted-s">Yalnızca Google hesap kimlik numaran saklanır; e-postan, adın ve fotoğrafın saklanmaz. Ayrıntılar <a href="/gizlilik/">gizlilik</a> sayfasında.</p></section>
<section class="sec" id="acctIn" hidden><h2>Giriş yapıldı</h2><p>İlerlemen bu hesapla eşitleniyor.</p><p class="btnrow"><button type="button" class="learn" id="logout">Çıkış yap</button> <button type="button" class="learn danger" id="del">Hesabımdaki veriyi sil</button></p></section>
<p class="muted-s" id="acctMsg" role="status"></p>
</div>'''
write('/hesap/', page('Hesap | Bitki Tabanı', 'Google ile giriş yaparak öğrendiğin bitkileri, serini ve bilmece sonuçlarını bütün cihazlarında sakla.', '/hesap/', hz, 'acct', '<script src="/assets/hesap.js" defer></script>', narrow=True,
      extra='<meta name="robots" content="noindex, follow">'))
gz = '''
<header class="page-head"><span class="eyebrow">Gizlilik</span><h1>Hangi bilgileri saklıyoruz?</h1><p>Kısaca: çok az. Bitki Tabanı reklam göstermez, seni siteler arasında izlemez ve kimseye veri satmaz.</p></header>
<section class="sec"><h2>Ziyaret sayıları</h2><p>Kaç kişinin hangi sayfayı okuduğunu görmek için Cloudflare Web Analytics kullanıyoruz. Bu araç çerez yazmaz, seni tanımlamaz ve siteler arasında izlemez; yalnızca toplu sayılar (ör. bir sayfanın kaç kez görüntülendiği, ziyaretçilerin hangi ülkeden geldiği) tutar.</p></section>
<section class="sec"><h2>Giriş yapmazsan</h2><p>Öğrendiğin bitkiler, serin ve bilmece tahminlerin yalnızca kendi tarayıcının hafızasında (localStorage) durur. Bize hiçbir şey gelmez. Tarayıcı verilerini silersen bunlar da silinir.</p></section>
<section class="sec"><h2>Google ile giriş yaparsan</h2><p>Google bize senin adına bir kimlik belgesi gönderir. Bunun içinden yalnızca Google hesap kimlik numaranı (rastgele görünen bir sayı) saklarız. E-posta adresin, adın ve profil fotoğrafın saklanmaz.</p><p>Bu numarayla birlikte şunları saklarız: öğrendim olarak işaretlediğin bitkiler, serinin günleri ve bilmece tahminlerin. Oturumunu hatırlamak için tarayıcına yalnızca bu iş için kullanılan, 180 gün geçerli bir çerez yazılır.</p><p>Veriler Cloudflare’in sunucularında tutulur. Google ile girişte Google’ın kendi <a href="https://policies.google.com/privacy?hl=tr" rel="noopener">gizlilik politikası</a> geçerlidir.</p></section>
<section class="sec"><h2>Silme</h2><p><a href="/hesap/">Hesap</a> sayfasındaki “Hesabımdaki veriyi sil” düğmesi saklanan bütün ilerlemeni hemen siler. Google hesabından da Bitki Tabanı’nın erişimini dilediğin zaman kaldırabilirsin.</p></section>
<section class="sec"><h2>Haklarına dair</h2><p>6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında verilerin hakkında bilgi isteme, düzeltme ve silme hakların vardır. Yukarıdaki silme düğmesi bu hakkı tek tıkla kullanmanı sağlar.</p></section>
'''
write('/gizlilik/', page('Gizlilik | Bitki Tabanı', 'Bitki Tabanı hangi bilgileri saklar: giriş yapmazsan hiçbirini; Google ile girişte yalnızca hesap kimlik numaranı ve ilerlemeni.', '/gizlilik/', gz, '', narrow=True))

# ---------- yöntem ----------
yt = """
<header class="page-head"><span class="eyebrow">Yöntem</span><h1>Kayıtları nasıl hazırlıyoruz?</h1><p>Bitki Tabanı bağımsız, ticari olmayan bir projedir. Her kayıt aynı kurallarla hazırlanır; bu sayfa o kuralları açıkça yazar ki neye ne kadar güvenebileceğini bil.</p></header>
<section class="sec" id="hazirlayan"><h2>Kim hazırlıyor</h2><p>""" + BIO + """</p><p>""" + SOCIAL + """</p><p>Bitki Tabanı’ndaki her kayıt onun tarafından hazırlanır ve aşağıdaki kurallarla kaynaklara dayandırılır.</p></section>
<section class="sec"><h2>Hangi kaynakları kullanıyoruz</h2><ol class="srclist">
<li><b>Resmî bitkisel ilaç değerlendirmeleri:</b> Avrupa İlaç Ajansı Bitkisel Ürünler Komitesi (EMA/HMPC) monografları ve ABD Ulusal Tamamlayıcı ve Bütünleştirici Sağlık Merkezi (NCCIH) özetleri.</li>
<li><b>Sistematik derlemeler ve klinik çalışmalar:</b> Cochrane derlemeleri ve PubMed’de dizinlenen hakemli dergiler.</li>
<li><b>Bitki adı ve sınıflandırma:</b> Kew Kraliyet Botanik Bahçeleri’nin Plants of the World Online (POWO) veri tabanı.</li>
<li><b>Koruma ve ticaret:</b> IUCN Kırmızı Liste ve CITES.</li>
<li><b>Yasal durum:</b> resmî mevzuat ve BM Uyuşturucu ve Suç Ofisi (UNODC) yayınları.</li>
<li><b>Geleneksel kullanım:</b> etnobotanik saha çalışmaları ve akademik kitaplar; Anadolu için Turhan Baytop’un <i>Türkiye’de Bitkiler ile Tedavi</i> kitabı temel başvuru kaynağıdır.</li>
</ol><p>Vikipedi, haber siteleri, aktar ve takviye satıcılarının sayfaları kaynak olarak kullanılmaz.</p></section>
<section class="sec"><h2>Kanıt düzeyleri</h2><dl class="meta wide">
<div><dt>Klinik</dt><dd>Kontrollü insan çalışmaları ya da resmî olarak onaylanmış bir ilaç kullanımı var.</dd></div>
<div><dt>Sınırlı</dt><dd>Küçük ya da az sayıda insan çalışması var; sonuçlar umut verici ama kesin değil.</dd></div>
<div><dt>Geleneksel</dt><dd>Kullanım kültürel olarak belgelenmiş, ama insan çalışması yok ya da çok az. Bu, bitkinin işe yaramadığı anlamına gelmez; yalnızca bilimin henüz bilmediğini söyler.</dd></div>
</dl></section>
<section class="sec"><h2>Güvenlik etiketleri</h2><dl class="meta wide">
<div><dt>Genelde güvenli</dt><dd>Ölçülü ve geleneksel biçimde kullanıldığında ciddi yan etki bildirilmemiş.</dd></div>
<div><dt>Dikkat</dt><dd>İlaç etkileşimi, doz ya da belirli gruplar (hamileler, çocuklar, kronik hastalar) için risk var.</dd></div>
<div><dt>Yüksek risk</dt><dd>Zehirli ya da ciddi yan etkileri olan bitkiler. Kültürel ve tarihî önemleri için yer alırlar; kullanım önerisi değildir.</dd></div>
</dl><p>Yasal durum, güvenlik etiketinden ayrı gösterilir: bir bitki yasak olmadan zehirli, zehirli olmadan yasak olabilir.</p></section>
<section class="sec"><h2>Geleneksel bilgiye yaklaşım</h2><p>Geleneksel kullanımlar, onları yaşatan toplulukların adıyla ve bağlamıyla anlatılır; “Amazon yerlileri” gibi genellemeler yerine Shipibo, Huichol gibi somut adlar kullanılır. Kutsal ve törensel kullanımlar bir tavsiye olarak değil, kültürel bir kayıt olarak yazılır.</p></section>
<section class="sec"><h2>Nasıl doğrulanıyor</h2><p>Her kayıt bir kişi tarafından hazırlanır; şu an bağımsız bir uzman ya da eczacı kayıtları gözden geçirmiyor. Bu yüzden her iddia, sayfanın altında listelenen kaynağa bağlanır ve okuyan herkes onu kendisi kontrol edebilir. Tıbbi bilgiler resmî değerlendirmelerden (EMA, NCCIH) ve sistematik derlemelerden alınır; kaynağı olmayan sağlık iddiası yazılmaz. Bir eczacı ya da farmakognozi uzmanı gözden geçirmeye katılırsa adı bu sayfada ve ilgili kayıtlarda belirtilecek.</p></section>
<section class="sec"><h2>Güncelleme ve düzeltme</h2><p>Her sayfanın altında son gözden geçirme tarihi yazar. Bir hata görürsen ya da yöresel bir kullanım biliyorsan <a href="mailto:iletisim@bitkitabani.com">iletisim@bitkitabani.com</a> adresine yaz; düzeltmeler kaynağıyla birlikte kontrol edilip eklenir.</p></section>
<section class="sec"><h2>Bağımsızlık</h2><p>Bitki Tabanı ürün satmaz, reklam almaz, satış ortaklığı (affiliate) bağlantısı kullanmaz ve hiçbir şirketten destek almaz.</p></section>
"""
write('/yontem/', page('Yöntem: kayıtları nasıl hazırlıyoruz | Bitki Tabanı', 'Bitki Tabanı hangi kaynakları kullanır, kanıt düzeylerini ve güvenlik etiketlerini nasıl belirler, hataları nasıl düzeltir.', '/yontem/', yt, 'about', narrow=True))

# ---------- 404, robots, sitemap, favicon ----------
nf = '<header class="page-head"><span class="eyebrow">404</span><h1>Bu sayfa bulunamadı</h1><p>Aradığın kayıt taşınmış ya da adres yanlış yazılmış olabilir.</p></header><section class="sec" id="nfs" hidden><h2>Bunu mu arıyordun?</h2><ul class="otherlist" id="nfList"></ul></section><p><a class="cta" id="nfSearch" href="/katalog/">Katalogda ara →</a></p>' + f'<script type="application/json" id="nfData">{json.dumps([[p["id"], p["tr"], p["la"]] for p in P] + [["kopruler/" + slug_of(x), x["t"], ""] for x in BR], ensure_ascii=False)}</script><script src="/assets/404.js" defer></script>'
open(os.path.join(OUT,'404.html'),'w',encoding='utf-8').write(page('Sayfa bulunamadı | Bitki Tabanı','Sayfa bulunamadı.','/404.html',nf,'', narrow=True))
_rules = 'Allow: /\nDisallow: /secim/\nDisallow: /api/\nDisallow: /hesap/\nDisallow: /*?\n'
_ai = ['Googlebot', 'Google-Extended', 'Bingbot', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'Perplexity-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'Applebot', 'Applebot-Extended', 'DuckAssistBot', 'meta-externalagent', 'CCBot']
open(os.path.join(OUT,'robots.txt'),'w').write('# Bitki Tabanı arama motorlarına ve yapay zekâ asistanlarına açıktır; alıntı yaparken kaynak göster.\n# Özet: ' + BASE + '/llms.txt\n\n' + ''.join(f'User-agent: {a}\n' for a in _ai) + _rules + '\nUser-agent: *\n' + _rules + f'\nSitemap: {BASE}/sitemap.xml\n')
import build_en
EN_URLS = build_en.run(globals())
urls = ['/', '/katalog/', '/kopruler/', '/gunun-bitkisi/', '/yeni/', '/oyun/', '/hakkinda/', '/yontem/', '/gizlilik/'] + [f'/kopruler/{slug_of(x)}/' for x in BR] + FAM_URLS + [f'/{p["id"]}/' for p in P] + EN_URLS
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{(LOCAL_DAY.isoformat() if u in ('/', '/gunun-bitkisi/', '/oyun/', '/yeni/', '/katalog/', '/en/', '/en/catalog/') else max(CONTENT_DATE, YENI[u.strip('/').split('/')[-1]].isoformat()) if u.strip('/').split('/')[-1] in YENI else CONTENT_DATE)}</lastmod></url>\n' for u in urls) + '</urlset>\n')
# ---------- llms.txt: yapay zekâ asistanları için özet ve tam metin ----------
def _md_plant(p, full=False):
    pid = p['id']; L = [f'## {p["tr"]} ({short_la(p)})', '', f'URL: {BASE}/{pid}/', f'Familya: {p["fam"]} · Bölge: {", ".join(REG[r]["ad"] for r in p["bolge"])} · Kullanılan kısım: {p["kisim"]}',
        f'Bilimsel kanıt: {KANIT[p["kanit"]]["ad"]} · Güvenlik: {GUV[p["guv"]]}' + (f' · Türkiye’de: {YASAL_AD[YASAL[pid][0]]}' if pid in YASAL else ''), '']
    if not full:
        return L[:4] + ['']
    L += ['### Geleneksel kullanım'] + [f'- {w}: {t}' for w, t in p['kul']] + ['', '### Hazırlama', p['haz'], '', '### Bilim ne diyor', p['bilim'], '', '### Güvenlik', p['guvNot'], '']
    if pid in ETK: L += ['### İlaç etkileşimleri'] + [f'- {g}: {w}' for g, w in ETK[pid]] + ['']
    if pid in DERIN: L += ['### İddialar ve kanıt'] + [f'- {i}: {KAN_AD[k]}. {n}' for i, k, n in DERIN[pid]['iddia']] + ['']
    ek = EK.get(pid, {})
    if ek: L += ['### Doğada', f'Nerede yetişir: {ek.get("yetisme","")}', f'Toplama mevsimi: {ek.get("mevsim","")}', f'Yöresel adlar: {ek.get("yoresel","")}', f'Karıştırma riski: {ek.get("karisma","")}', '']
    L += ['### İlginç bilgi', p['ilginc'], '']
    return L
_head = ['# Bitki Tabanı', '', f'> Şifalı ve ritüel bitkiler için Türkçe, kaynaklı ve ticari olmayan bir etnobotanik veri tabanı: {len(P)} bitki; Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika. Her kayıtta geleneksel kullanım, bilimsel kanıt düzeyi, güvenlik ve ilaç etkileşimleri, Türkiye’deki yasal durum ve kaynaklar yer alır. Hazırlayan: Edanaz Tınmazlar. Tıbbi tavsiye değildir.', '',
         'Alıntı yaparken lütfen bitkinin sayfasını kaynak olarak göster.', '', '## Sayfalar', f'- [Katalog]({BASE}/katalog/): bütün bitkiler, bölge, kullanım, kanıt ve güvenliğe göre', f'- [Kültür köprüleri]({BASE}/kopruler/): farklı kültürlerde benzer kullanılan bitkilerin karşılaştırması',
         f'- [Yöntem]({BASE}/yontem/): kaynaklar, kanıt düzeyleri ve güvenlik etiketleri nasıl belirlenir', f'- [Tam metin]({BASE}/llms-full.txt): bütün kayıtların düz metin hâli', f'- [English edition]({BASE}/en/): the same database in English', '', '## Bitkiler']
open(os.path.join(OUT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(_head + [f'- [{p["tr"]} ({short_la(p)})]({BASE}/{p["id"]}/): {GUV[p["guv"]]}, kanıt: {KANIT[p["kanit"]]["ad"].lower()}' for p in P]) + '\n\n## Kültür köprüleri\n' + '\n'.join(f'- [{x["t"]}]({BASE}/kopruler/{slug_of(x)}/): {x["d"]}' for x in BR) + '\n')
open(os.path.join(OUT, 'llms-full.txt'), 'w', encoding='utf-8').write('\n'.join(_head[:5] + ['Tıbbi tavsiye değildir. Zehirlenme şüphesinde Türkiye’de Ulusal Zehir Danışma Merkezi: 114.', ''] + [l for p in P for l in _md_plant(p, True)]))

os.makedirs(os.path.join(OUT,'assets'), exist_ok=True)
for f in os.listdir(os.path.join(HERE, 'assets')):
    shutil.copy(os.path.join(HERE, 'assets', f), os.path.join(OUT, 'assets', f))
if os.path.isdir(os.path.join(HERE, 'img')):
    shutil.copytree(os.path.join(HERE, 'img'), os.path.join(OUT, 'img'), dirs_exist_ok=True)
open(os.path.join(OUT, '_headers'), 'w').write('''/*
  Cache-Control: public, max-age=0, must-revalidate
/assets/*
  Cache-Control: public, max-age=3600
/img/*
  Cache-Control: public, max-age=2592000
/robots.txt
  Content-Type: text/plain; charset=utf-8
/llms.txt
  Content-Type: text/plain; charset=utf-8
/llms-full.txt
  Content-Type: text/plain; charset=utf-8
''')
# ---------- Instagram postları için veri (tools/ig.py okur; yayımlanmaz) ----------
os.makedirs(os.path.join(HERE, '.cache'), exist_ok=True)
json.dump({'day': LOCAL_DAY.isoformat(), 'yeni': {k: v.isoformat() for k, v in YENI.items()},
           'kuyruk': [[q['id'], q['yayin']] for q in _K.Q],
           'kanit': {k: v['ad'] for k, v in KANIT.items()}, 'guv': GUV, 'reg': {k: v['ad'] for k, v in REG.items()},
           'p': [dict(id=p['id'], no=p['no'], tr=p['tr'], la=short_la(p), fam=p['fam'], bolge=p['bolge'], kat=p['kat'], kul=p['kul'], bilim=p['bilim'], kanit=p['kanit'],
                      guv=p['guv'], guvNot=p['guvNot'], ilginc=p['ilginc'], yasal=(YASAL[p['id']][0] if p['id'] in YASAL else None), img=(p['id'] in IMG),
                      foto=((IMG[p['id']].get('artist') or '') + (' · ' + IMG[p['id']].get('license', '') if IMG[p['id']].get('license') else '')) if p['id'] in IMG else '') for p in P]},
          open(os.path.join(HERE, '.cache', 'ig_input.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('ok', len(urls), 'sayfa')

