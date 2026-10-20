import json, os, shutil, html, re, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
from refs import WIKI, POWO, NCCIH, EMA, OTHER, FILES
from extra import EK, KORUMA, YASAL, YASAL_AD, BR_GEO, ALT
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
    from zoneinfo import ZoneInfo
    LOCAL_DAY = datetime.datetime.now(ZoneInfo('Europe/Istanbul')).date()
except Exception:
    LOCAL_DAY = datetime.date.today()
AYLAR = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
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

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,500;0,700;0,800;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=Courier+Prime:wght@400;700&display=swap">'
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
    return f'''<div class="motif" aria-hidden="true"></div><div class="site-nav"><a class="logo" href="/">Bitki <em>Tabanı</em></a><nav>{a("/katalog/", "Katalog", "kat")}{a("/kopruler/", "Kültür köprüleri", "br")}{a("/hakkinda/", "Hakkında", "about")}</nav></div>'''

FOOT = '''<div class="motif indigo" aria-hidden="true"></div>
<footer class="site">
  <div>
    <h3>Bu site nedir</h3>
    <p>Bilgi ve merak için hazırlanmış bir derlemedir; tedavi önerisi değildir. Bir bitkiyi kullanmadan önce, özellikle ilaç kullanıyorsan, hamileysen ya da emziriyorsan bir hekime veya eczacıya danış.</p>
    <p>Fotoğraflar Wikimedia Commons’tan özgür lisanslarla alınmıştır; yazarı ve lisansı her bitkinin sayfasında yazılıdır.</p>
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
    return h + nav(cur) + body + FOOT + scripts + '\n</body>\n</html>\n'

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
    return f'<div class="ph loaded"><img src="/img/{p["id"]}-{size}.jpg" width="{w}" height="{h}" alt="{e(p["tr"])} ({e(short_la(p))}): {e(ALT.get(p["id"], "bitki"))}" {load} decoding="async"></div>'

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
    name = POWO.get(pid, short_la(p))
    if name:
        items.append(('Botanik kayıt', f'Kew Plants of the World Online: {name}', 'https://powo.science.kew.org/results?q=' + urllib.parse.quote(name)))
    return '<ol class="refs">' + ''.join(f'<li><span class="kind">{e(k)}</span><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' for k, t, u in items) + '</ol>'

def desc_for(p):
    first = p['kul'][0][1].split('. ')[0].rstrip('.')
    d = f'{p["tr"]} ({short_la(p)}): {first}. Bilimsel kanıt: {KANIT[p["kanit"]]["ad"].lower()}. Güvenlik notları ve kaynaklar.'
    return d if len(d) <= 160 else d[:157].rsplit(' ', 1)[0] + '…'

def card(p):
    s = ' '.join([p['tr'], p['la'], p['diger'], p['fam'], p['kisim'], p['haz'], p['bilim'], p['ilginc']] + [x for u in p['kul'] for x in u] + [KAT[k] for k in p['kat']])
    return f'''<a class="card" href="/{p["id"]}/" data-id="{p["id"]}" data-bolge="{" ".join(p["bolge"])}" data-kat="{" ".join(p["kat"])}" data-kanit="{p["kanit"]}" data-guv="{p["guv"]}" data-durum="{" ".join(([YASAL[p["id"]][0] if YASAL[p["id"]][0]=="yasak" else "kisitli"] if p["id"] in YASAL else []) + (["koruma"] if KORUMA.get(p["id"], {}).get("rozet") else []))}" data-s="{e(s)}">
  {ph(p, 500)}
  <div class="body">
    <div class="row"><span class="acc">{acc(p["no"])}</span><span class="regs">{"".join(dot(r) for r in p["bolge"])}</span></div>
    <h2>{e(p["tr"])}</h2>
    <div class="latin">{e(p["la"])}</div>
    <div class="fam" lang="la">{e(p["fam"])}</div>
    {tags(p)}
    <div class="foot"><span class="ev" aria-label="Kanıt düzeyi: {KANIT[p["kanit"]]["ad"]}">{pips(p["kanit"])} Kanıt: {KANIT[p["kanit"]]["ad"]}</span><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span></div>
  </div>
</a>'''

# ---------- bitki sayfaları ----------
for i, p in enumerate(P):
    pid = p['id']; rel = related(pid)
    prev, nxt = P[i-1], P[(i+1) % len(P)]
    title = f'{p["tr"]} ({short_la(p)}): kullanımı, bilim ve güvenlik | Bitki Tabanı'
    ld = {"@context":"https://schema.org","@type":"Article","headline":f'{p["tr"]} ({short_la(p)})',"inLanguage":"tr","about":{"@type":"Taxon","name":short_la(p),"alternateName":[p['tr']] + [x.strip() for x in p['diger'].split(',')][:4],"taxonRank":"species","parentTaxon":{"@type":"Taxon","name":p['fam'].split(' ')[0],"taxonRank":"family"}},"description":desc_for(p),"author":{"@type":"Organization","name":"Bitki Tabanı"},"isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},"dateModified":CONTENT_DATE,"url":f'{BASE}/{pid}/',"image":(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None),"publisher":{"@type":"Organization","name":"Bitki Tabanı","url":BASE+"/"}}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Katalog","item":BASE+"/katalog/"},{"@type":"ListItem","position":3,"name":p['tr'],"item":f'{BASE}/{pid}/'}]}
    uses = ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(t)}</p></div>' for w, t in p['kul'])
    relhtml = ''
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
      <span class="eyebrow">{acc(p["no"])} · <span lang="la">{e(p["fam"])}</span></span>
      <h1>{e(p["tr"])}</h1>
      <span class="latin">{e(p["la"])}</span>
      <div class="badges"><span class="ev">{pips(p["kanit"])} Kanıt: {KANIT[p["kanit"]]["ad"]}</span><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span>{tags(p).replace('<div class="tags">','').replace('</div>','')}</div>
    </div>
    <figure class="photo">{ph(p, 960, eager=True)}<figcaption>{credit(p)}</figcaption></figure>
  </header>
  <dl class="meta">
    <div><dt>Diğer adlar</dt><dd>{e(p["diger"])}</dd></div>
    <div><dt>Kullanılan kısım</dt><dd>{e(p["kisim"])}</dd></div>
    <div><dt>Bölge</dt><dd>{"<br>".join(dot(r) + " " + e(REG[r]["ad"]) for r in p["bolge"])}</dd></div>
    <div><dt>Kullanım</dt><dd>{", ".join(KAT[k] for k in p["kat"])}</dd></div>
  </dl>
  <section class="sec"><h2>Geleneksel kullanım</h2><div class="uses">{uses}</div></section>
  {dogada}
  <section class="sec"><h2>Hazırlama</h2><p>{e(p["haz"])}</p></section>
  <section class="sec"><h2>Bilim ne diyor</h2><p>{e(p["bilim"])}</p></section>
  <section class="sec"><h2>Güvenlik</h2><div class="callout {p["guv"]}"><div class="lvl">{GUV[p["guv"]]}</div><p>{e(p["guvNot"])}</p></div></section>
  {yas}
  {korhtml}
  <p class="fact">{e(p["ilginc"])}</p>
  {relhtml}
  {('<p class="brlinks">' + brlinks + '</p>') if brlinks else ''}
  {simhtml}
  <section class="sec"><h2>Kaynaklar</h2>{refs(p)}</section>
  <aside class="disclaimer" role="note"><b>Tıbbi tavsiye değildir.</b> Bu sayfa geleneksel kullanımları kültürel bir kayıt olarak anlatır ve bilimsel bilgiyi özetler; teşhis ya da tedavi önerisi değildir. {e(p["tr"])} ya da başka bir bitkiyi kullanmadan önce, özellikle ilaç kullanıyorsan, hamileysen, emziriyorsan ya da bir hastalığın varsa hekimine veya eczacına danış. Zehirlenme şüphesinde Ulusal Zehir Danışma Merkezi’ni (UZEM) <b>114</b> numaradan ara.</aside>
  <div class="sheet-foot">
    <div class="learnbox"><button type="button" class="learn" id="learnBtn" data-id="{pid}" aria-pressed="false">Öğrendim olarak işaretle</button><span class="muted-s">Yalnızca bu tarayıcıda saklanır; başka cihazda görünmez.</span></div>
    <div class="pager"><a href="/{prev["id"]}/">← {e(prev["tr"])}</a><a href="/{nxt["id"]}/">{e(nxt["tr"])} →</a></div>
  </div>
</article>
'''
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>'
    write(f'/{pid}/', page(title, desc_for(p), f'/{pid}/', body, 'plant', '<script src="/assets/plant.js" defer></script>', narrow=True, extra=extra, image=(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None)))

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
learn_note = '<p class="hint" id="learnHint"><b>Öğrendiklerim</b> sayacı, bitki sayfalarının sonundaki “Öğrendim” düğmesiyle işaretlediğin bitkileri gösterir. Bu bilgi yalnızca şu an kullandığın tarayıcıda saklanır: başka bir cihazdan girersen, başka bir tarayıcı kullanırsan ya da tarayıcı verilerini silersen görünmez. Hesap ya da kayıt gerekmez.</p>'
katalog = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Katalog</span></nav>
<header class="page-head"><span class="eyebrow">{len(P)} kayıt</span><h1>Bitki kataloğu</h1><p>Bütün bitkileri bölgeye, kullanıma, kanıt düzeyine, güvenliğe ve yasal duruma göre süz. Seçtiğin filtreler adres çubuğuna yazılır; bağlantıyı paylaşabilirsin.</p></header>
<div class="stats"><span><strong>{len(P)}</strong> bitki</span><span><strong>{len(regs)}</strong> bölge</span><span><strong>{len(BR)}</strong> kültür köprüsü</span><span>Öğrendiklerim <strong id="learnedCount">0</strong>/{len(P)} <span class="muted-s">(bu tarayıcıda)</span></span></div>
{learn_note}
<section style="display:flex;flex-direction:column;gap:18px" aria-label="Katalog">
  <div class="controls">
    <label class="search" for="q">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="2" fill="none"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="q" type="search" placeholder="Bitki, Latince ad, kullanım ara… (ör. nazar, öksürük, tütsü)" autocomplete="off" aria-label="Bitki ara">
    </label>
    <div class="fgroups">{filters}</div>
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
<section class="sec"><h2>Diğer köprüler</h2><ul class="otherlist">{others}</ul></section>
<div class="sheet-foot"><a class="cta" href="/kopruler/">Bütün köprüler ve harita →</a><div class="pager"><a href="/kopruler/{slug_of(prev_)}/">← {e(prev_["t"])}</a><a href="/kopruler/{slug_of(next_)}/">{e(next_["t"])} →</a></div></div>
</article>'''
    ldb = [{"@context":"https://schema.org","@type":"Article","headline":br_['t'],"description":br_['d'],"inLanguage":"tr","url":f'{BASE}/kopruler/{slug}/',"dateModified":CONTENT_DATE,
            "about":[{"@type":"Taxon","name":short_la(q),"alternateName":q['tr']} for q in ps],"isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},
            "image":[f'{BASE}/img/{q["id"]}-960.jpg' for q in ps if q['id'] in IMG]},
           {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Kültür köprüleri","item":BASE+"/kopruler/"},{"@type":"ListItem","position":3,"name":br_['t'],"item":f'{BASE}/kopruler/{slug}/'}]}]
    desc = (f'{title_names}: ' + br_['d'])[:157]
    write(f'/kopruler/{slug}/', page(f'{br_["t"]}: {title_names} | Bitki Tabanı', desc, f'/kopruler/{slug}/', body, 'br', narrow=True,
          extra=''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ldb), image=(f'{BASE}/img/{a["id"]}-960.jpg' if a['id'] in IMG else None)))

# ---------- hakkında ----------
about = '''<header class="page-head"><span class="eyebrow">Hakkında</span><h1>Bitki Tabanı nedir?</h1></header>
<section class="sec"><p>Bitki Tabanı, farklı kültürlerde şifa ve ritüel için kullanılan bitkileri bir araya getiren bağımsız bir etnobotanik kayıt defteridir. Amacı merak uyandırmak ve geleneksel bilgiyi bugünkü bilimsel bilgiyle yan yana koymak.</p></section>
<section class="sec"><h2>Kayıtlar nasıl hazırlanıyor</h2><p>Her kayıt; geleneksel kullanımı, hazırlama biçimini, bilimin bugün ne söylediğini ve güvenlik notlarını içerir. Kanıt düzeyi Avrupa İlaç Ajansı (EMA/HMPC) monografileri, ABD NCCIH özetleri, Cochrane derlemeleri ve hakemli literatüre göre belirlenir. Kaynaklar her bitkinin sayfasının sonunda listelenir.</p></section>
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
def day_pick(d): return pool[(d - datetime.date(1970, 1, 1)).days % len(pool)]
today_p = day_pick(LOCAL_DAY)
LEDE = f'{REG_LIST}’dan {len(P)} şifalı ve ritüel bitkisi. Her kayıtta geleneksel kullanım, bilimin söyledikleri, güvenlik notu ve kaynaklar bir arada.'

REG_TXT = {'anadolu':'Nazar tütsüsünden kına gecesine, Anadolu’nun şifa ve ritüel otları.','asya':'İskit tütsülerinden Sibirya şamanlarına, bozkırın ve taygaların bitkileri.',
           'and':'Koka yaprağından kantuta çiçeğine, And Dağları’nın kutsal bitkileri.','amazon':'Ayahuasca sarmaşığından huito boyasına, yağmur ormanının öğretmen bitkileri.',
           'kamerika':'Ak adaçayından peyoteye, Kuzey Amerika yerli halklarının bitkileri.'}
regcards = ''.join(f'<a class="regcard" href="/katalog/?bolge={k}"><span class="where">{dot(k)} {e(v["ad"])}</span><b>{cnt(lambda p,k=k: k in p["bolge"])} bitki</b><span>{e(REG_TXT.get(k,""))}</span></a>' for k,v in regs)
home = f'''
<header class="top">
  <div class="brand">
    <span class="eyebrow">Etnobotanik kayıt defteri</span>
    <h1 class="wordmark">Bitki <em>Tabanı</em></h1>
    <p class="lede">{LEDE}</p>
    <p><a class="cta" href="/katalog/">Kataloğa git →</a></p>
  </div>
  <div class="todaybox"><a class="today" id="today" href="/{today_p["id"]}/" data-pool="{e(json.dumps([[p["id"], p["tr"], p["la"]] for p in pool], ensure_ascii=False))}"><span class="eyebrow">Bugünün bitkisi</span><b id="todayName">{e(today_p["tr"])}</b><i id="todayLatin">{e(today_p["la"])}</i></a><a class="cta small" href="/gunun-bitkisi/">Geçmiş günlerin bitkileri →</a></div>
</header>
<section class="sec"><h2>Bölgelere göre</h2><div class="regs-grid">{regcards}</div></section>
<section class="sec"><h2>Öne çıkanlar</h2><div class="grid">{"".join(card(byId[i]) for i in FEATURED if i in byId)}</div><p><a class="cta" href="/katalog/">Bütün {len(P)} bitkiyi gör →</a></p></section>
<section class="sec"><h2>Kültür köprüleri</h2><p>Birbirinden binlerce kilometre uzaktaki kültürler, çoğu zaman aynı molekülleri ya da aynı bitkiyi benzer dertlere kullanmış. {len(BR)} köprüyü haritada gör.</p><div class="mapwrap">{bridge_map()}</div><p><a class="cta" href="/kopruler/">Bütün köprüleri ve karşılaştırmaları gör →</a></p></section>
'''
ldsite = {"@context":"https://schema.org","@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/","inLanguage":"tr","description":"Şifalı ve ritüel bitkiler için Türkçe etnobotanik kayıt defteri."}
write('/index.html', page('Bitki Tabanı: şifalı ve ritüel bitkiler veri tabanı', f'{REG_LIST}’dan {len(P)} şifalı ve ritüel bitkisi: geleneksel kullanım, bilimsel kanıt, güvenlik ve kaynaklar.', '/', home, 'home', '<script src="/assets/home.js" defer></script>', extra=f'<script type="application/ld+json">{json.dumps(ldsite, ensure_ascii=False)}</script>'))

# ---------- günün bitkisi arşivi ----------
days = [LOCAL_DAY - datetime.timedelta(days=n) for n in range(14)]
tp = today_p
past = ''.join(f'<li><span class="mono-d">{tr_date(d)}</span><a href="/{day_pick(d)["id"]}/">{e(day_pick(d)["tr"])}</a> <i class="latin">{e(short_la(day_pick(d)))}</i></li>' for d in days[1:])
gb = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Günün bitkisi</span></nav>
<header class="page-head"><span class="eyebrow">{tr_date(LOCAL_DAY)}</span><h1>Günün bitkisi: {e(tp["tr"])}</h1><p>Her gün katalogdan bir bitki öne çıkıyor. Ölümcül zehirli ya da yüksek riskli bitkiler bu döngüye alınmaz.</p></header>
<div class="grid sim">{card(tp)}</div>
<section class="sec"><h2>Bugün okumak için</h2><p>{e(tp["kul"][0][1])}</p><p class="fact">{e(tp["ilginc"])}</p><p><a class="cta" href="/{tp["id"]}/">{e(tp["tr"])} sayfasının tamamı →</a></p></section>
<section class="sec"><h2>Son iki hafta</h2><ul class="daylist">{past}</ul></section>
'''
write('/gunun-bitkisi/', page(f'Günün bitkisi: {tp["tr"]} | Bitki Tabanı', f'Bugünün bitkisi {tp["tr"]} ({short_la(tp)}) ve son iki haftanın bitkileri.', '/gunun-bitkisi/', gb, '', narrow=True,
      image=(f'{BASE}/img/{tp["id"]}-960.jpg' if tp['id'] in IMG else None)))

# ---------- 404, robots, sitemap, favicon ----------
nf = '<header class="page-head"><span class="eyebrow">404</span><h1>Bu sayfa bulunamadı</h1><p>Aradığın kayıt taşınmış ya da hiç olmamış olabilir. <a href="/">Kataloğa dön</a> ve oradan ara.</p></header>'
open(os.path.join(OUT,'404.html'),'w',encoding='utf-8').write(page('Sayfa bulunamadı | Bitki Tabanı','Sayfa bulunamadı.','/404.html',nf,'', narrow=True))
open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nDisallow: /secim/\nDisallow: /*?\n\nSitemap: {BASE}/sitemap.xml\n')
urls = ['/', '/katalog/', '/kopruler/', '/gunun-bitkisi/', '/hakkinda/'] + [f'/kopruler/{slug_of(x)}/' for x in BR] + [f'/{p["id"]}/' for p in P]
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{(LOCAL_DAY.isoformat() if u in ('/', '/gunun-bitkisi/') else CONTENT_DATE)}</lastmod></url>\n' for u in urls) + '</urlset>\n')
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
''')
print('ok', len(urls), 'sayfa')

