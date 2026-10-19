import json, os, shutil, html, re, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
from refs import WIKI, POWO, NCCIH, EMA, OTHER, FILES
from extra import EK, KORUMA, YASAL, YASAL_AD
IMG = json.load(open(os.path.join(HERE, 'images.json'), encoding='utf-8')) if os.path.exists(os.path.join(HERE, 'images.json')) else {}

BASE = 'https://bitkitabani.com'
OUT = os.path.join(HERE, 'site')
D = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))
REG, KAT, KANIT, GUV, P, BR, EXTRA = D['REG'], D['KAT'], D['KANIT'], D['GUV'], D['P'], D['BR'], D['EXTRA']
for i, p in enumerate(P): p['no'] = i + 1
GUV['yuksek'] = 'Yüksek risk'
byId = {p['id']: p for p in P}
TODAY = datetime.date.today().isoformat()
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
    return f'''<div class="motif" aria-hidden="true"></div><div class="site-nav"><a class="logo" href="/">Bitki <em>Tabanı</em></a><nav>{a("/", "Katalog", "home")}{a("/kopruler/", "Kültür köprüleri", "br")}{a("/hakkinda/", "Hakkında", "about")}</nav></div>'''

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
    return f'<div class="ph loaded"><img src="/img/{p["id"]}-{size}.jpg" width="{w}" height="{h}" alt="{e(p["tr"])} ({e(short_la(p))})" {load} decoding="async"></div>'

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

# ---------- bitki sayfaları ----------
for i, p in enumerate(P):
    pid = p['id']; rel = related(pid)
    prev, nxt = P[i-1], P[(i+1) % len(P)]
    title = f'{p["tr"]} ({short_la(p)}): kullanımı, bilim ve güvenlik | Bitki Tabanı'
    ld = {"@context":"https://schema.org","@type":"Article","headline":f'{p["tr"]} ({short_la(p)})',"inLanguage":"tr","about":{"@type":"Thing","name":p['la'],"alternateName":p['tr']},"isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},"dateModified":TODAY,"url":f'{BASE}/{pid}/',"image":(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None),"publisher":{"@type":"Organization","name":"Bitki Tabanı","url":BASE+"/"}}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Katalog","item":BASE+"/"},{"@type":"ListItem","position":2,"name":p['tr'],"item":f'{BASE}/{pid}/'}]}
    uses = ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(t)}</p></div>' for w, t in p['kul'])
    relhtml = ''
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
<nav class="crumbs" aria-label="Konum"><a href="/">Katalog</a><span>/</span><span>{e(p["tr"])}</span></nav>
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
  <section class="sec"><h2>Kaynaklar</h2>{refs(p)}</section>
  <div class="sheet-foot">
    <button type="button" class="learn" id="learnBtn" data-id="{pid}" aria-pressed="false">Öğrendim olarak işaretle</button>
    <div class="pager"><a href="/{prev["id"]}/">← {e(prev["tr"])}</a><a href="/{nxt["id"]}/">{e(nxt["tr"])} →</a></div>
  </div>
</article>
'''
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>'
    write(f'/{pid}/', page(title, desc_for(p), f'/{pid}/', body, 'plant', '<script src="/assets/plant.js" defer></script>', narrow=True, extra=extra, image=(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None)))

# ---------- katalog ----------
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

def cnt(fn): return sum(1 for p in P if fn(p))
regs = [(k, v) for k, v in REG.items() if cnt(lambda p: k in p['bolge']) >= 3]
durum = [('yasak', 'Türkiye’de yasak', lambda p: YASAL.get(p['id'], ('',))[0] == 'yasak'),
         ('kisitli', 'Türkiye’de kısıtlı veya lisanslı', lambda p: YASAL.get(p['id'], ('',))[0] in ('kisitli', 'lisansli')),
         ('koruma', 'Koruma gerektiren', lambda p: bool(KORUMA.get(p['id'], {}).get('rozet')))]
groups = [('bolge','Bölge',[(k,v['ad'],dot(k),cnt(lambda p,k=k: k in p['bolge'])) for k,v in regs]),
          ('kat','Kullanım',[(k,v,'',cnt(lambda p,k=k: k in p['kat'])) for k,v in KAT.items()]),
          ('kanit','Kanıt düzeyi',[(k,v['ad'],pips(k),cnt(lambda p,k=k: p['kanit']==k)) for k,v in KANIT.items()]),
          ('guv','Güvenlik',[(k,v,f'<span class="dot" style="background:var(--s-{k})"></span>',cnt(lambda p,k=k: p['guv']==k)) for k,v in GUV.items()]),
          ('durum','Yasal ve koruma',[(k,v,'',cnt(fn)) for k,v,fn in durum])]
filters = ''.join(f'<div class="fgroup"><span>{lab}</span><div class="chips">' + ''.join(f'<button type="button" class="chip" data-g="{g}" data-k="{k}" aria-pressed="false">{ic}{e(v)} <span class="n">{n}</span></button>' for k,v,ic,n in opts) + '</div></div>' for g,lab,opts in groups)
home = f'''
<header class="top">
  <div class="brand">
    <span class="eyebrow">Etnobotanik kayıt defteri</span>
    <h1 class="wordmark">Bitki <em>Tabanı</em></h1>
    <p class="lede">Anadolu’dan And Dağları’na, Amazon’dan Sibirya’ya {len(P)} şifalı ve ritüel bitkisi. Her kayıtta geleneksel kullanım, bilimin söyledikleri, güvenlik notu ve kaynaklar bir arada.</p>
  </div>
  <a class="today" id="today" href="/{P[1]["id"]}/"><span class="eyebrow">Bugünün bitkisi</span><b id="todayName">{e(P[1]["tr"])}</b><i id="todayLatin">{e(P[1]["la"])}</i></a>
</header>
<div class="stats"><span><strong>{len(P)}</strong> bitki</span><span><strong>{len(regs)}</strong> bölge</span><span><strong>{len(BR)}</strong> kültür köprüsü</span><span title="Okuduğun bitkileri sayfalarındaki “Öğrendim” düğmesiyle işaretle">Öğrendiklerim <strong id="learnedCount">0</strong>/{len(P)}</span></div>
<p class="hint">Okuduğun bitkileri, sayfalarının sonundaki <b>Öğrendim</b> düğmesiyle işaretleyebilirsin. İlerlemen yalnızca bu tarayıcıda saklanır; hesap gerekmez.</p>
<section style="display:flex;flex-direction:column;gap:18px" aria-label="Katalog">
  <div class="controls">
    <label class="search" for="q">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="2" fill="none"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="q" type="search" placeholder="Bitki, Latince ad, kullanım ara… (ör. nazar, öksürük, tütsü)" autocomplete="off">
    </label>
    <div class="fgroups">{filters}</div>
  </div>
  <div class="resultbar"><span id="count">{len(P)} / {len(P)} kayıt gösteriliyor</span><button class="linkbtn" id="reset" type="button" hidden>Filtreleri temizle</button></div>
  <div class="grid">{"".join(card(p) for p in P)}</div>
  <div class="empty" id="empty" hidden>Bu arama ve filtrelerle eşleşen bitki yok. Bir filtreyi kaldırmayı ya da farklı bir kelime denemeyi dene.</div>
</section>
'''
ldsite = {"@context":"https://schema.org","@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/","inLanguage":"tr"}
write('/index.html', page('Bitki Tabanı: şifalı ve ritüel bitkiler veri tabanı', f'Anadolu’dan And Dağları’na {len(P)} şifalı ve ritüel bitkisi: geleneksel kullanım, bilimsel kanıt, güvenlik notları ve kaynaklar.', '/', home, 'home', '<script src="/assets/catalog.js" defer></script>', extra=f'<script type="application/ld+json">{json.dumps(ldsite, ensure_ascii=False)}</script>'))

# ---------- köprüler ----------
def mini(p):
    return f'<a class="mini" href="/{p["id"]}/"><span class="where">{"".join(dot(r) for r in p["bolge"])} {e(" · ".join(REG[r]["ad"] for r in p["bolge"]))}</span><b>{e(p["tr"])}</b><span class="latin">{e(p["la"])}</span></a>'
items = []
for b in BR:
    a = byId[b['a']]; c = byId.get(b.get('b')) if b.get('b') else None
    txt = f'<div class="txt"><h2>{e(b["t"])}</h2><p>{e(b["d"])}</p></div>'
    items.append(f'<article class="bridge">{mini(a)}<span class="arrow" aria-hidden="true">↔</span>{mini(c)}{txt}</article>' if c else f'<article class="bridge single">{mini(a)}<span class="note">Aynı bitki, birden fazla kültür</span>{txt}</article>')
br = f'''<header class="page-head"><span class="eyebrow">{len(BR)} karşılaştırma</span><h1>Kültür köprüleri</h1><p>Birbirinden binlerce kilometre uzaktaki kültürler, çoğu zaman aynı molekülleri ya da aynı bitkiyi benzer dertlere kullanmış. Bu sayfa o kesişimleri bir araya getiriyor.</p></header><div class="bridges">{"".join(items)}</div>'''
write('/kopruler/', page('Kültür köprüleri: Anadolu, And ve Amazon bitkileri | Bitki Tabanı', 'Anadolu ile And Dağları ve Amazon’un bitki geleneklerini karşılaştıran kültür köprüleri: üzerlik ve ayahuasca, sedef otu ve ruda, sığla ve palo santo.', '/kopruler/', br, 'br'))

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
    return 'Amanita muscaria' if p['id'] == 'sinekmantari' else t
rows = ''.join(f'<section class="pick-row" data-id="{p["id"]}" data-taxon="{e(taxon_of(p))}"><h2>{acc(p["no"])} · {e(p["tr"])} <span class="latin">{e(taxon_of(p))}</span></h2><div class="cands"><p class="muted">Adaylar yükleniyor…</p></div></section>' for p in P)
secim = f'''<header class="page-head"><span class="eyebrow">Yalnızca yönetici için</span><h1>Fotoğraf seçimi</h1><p>Her bitki için bitkiyi en iyi tanıtan yakın çekime tıkla. Seçimlerin bu tarayıcıda saklanır. Bitince alttaki listeyi kopyalayıp Claude’a gönder.</p></header>
{rows}
<div class="result-box"><div class="row"><span id="done"></span><button type="button" id="copy">Listeyi kopyala</button><span id="copied"></span></div><textarea id="result" readonly aria-label="Seçim listesi"></textarea></div>'''
write('/secim/', page('Fotoğraf seçimi | Bitki Tabanı', 'Fotoğraf seçimi', '/secim/', secim, '', '<script src="/assets/photo.js" defer></script><script src="/assets/secim.js" defer></script>', extra='<meta name="robots" content="noindex, nofollow">'))

# ---------- 404, robots, sitemap, favicon ----------
nf = '<header class="page-head"><span class="eyebrow">404</span><h1>Bu sayfa bulunamadı</h1><p>Aradığın kayıt taşınmış ya da hiç olmamış olabilir. <a href="/">Kataloğa dön</a> ve oradan ara.</p></header>'
open(os.path.join(OUT,'404.html'),'w',encoding='utf-8').write(page('Sayfa bulunamadı | Bitki Tabanı','Sayfa bulunamadı.','/404.html',nf,'', narrow=True))
open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nDisallow: /secim/\n\nSitemap: {BASE}/sitemap.xml\n')
urls = ['/', '/kopruler/', '/hakkinda/'] + [f'/{p["id"]}/' for p in P]
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls) + '</urlset>\n')
os.makedirs(os.path.join(OUT,'assets'), exist_ok=True)
for f in os.listdir(os.path.join(HERE, 'assets')):
    shutil.copy(os.path.join(HERE, 'assets', f), os.path.join(OUT, 'assets', f))
if os.path.isdir(os.path.join(HERE, 'img')):
    shutil.copytree(os.path.join(HERE, 'img'), os.path.join(OUT, 'img'), dirs_exist_ok=True)
print('ok', len(urls), 'sayfa')

