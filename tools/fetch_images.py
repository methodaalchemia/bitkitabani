"""Commons'tan seçili bitki fotoğraflarını indirir (500 ve 960 px), kredi bilgisini images.json'a yazar.
GitHub Actions'ta çalışır; yerelde de `python3 tools/fetch_images.py` ile çalıştırılabilir."""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from refs import FILES, POWO
import json as _j
_D = _j.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
# Yayın kuyruğundaki bitkilerin fotoğrafları da önceden hazırlanır
import kuyruk as _K
_have = {p['id'] for p in _D['P']}
for _q in _K.Q:
    if _q.get('foto'): FILES[_q['id']] = _q['foto']
    POWO.setdefault(_q['id'], _q['taxon'])
    if _q['id'] not in _have: _D['P'].append({'id': _q['id'], 'la': _q['la']})
# Komut satırında id verilirse yalnız onlar işlenir: 32 eksik görsel için
# bütün katalogu baştan doğrulamak gereksiz (24 Kasım 2026).
_SEC = [a for a in sys.argv[1:] if not a.startswith('-')]
if _SEC:
    _D['P'] = [p for p in _D['P'] if p['id'] in _SEC]
    FILES = {k: v for k, v in FILES.items() if k in _SEC}

BAD = re.compile(r'illustrat|drawing|k[öo]e?hler|medizinal-pflanzen|botanical (art|plate|print)|\bplate\b|tafel|lithograph|engraving|woodcut|painting|watercolou?r|herbari|exsiccat|\bmaps?\b|distribution|diagram|molecule|stamp|coin|logo|bottle|drink|beverage|powder|capsule|svg|specimen|museum|montage|collage|mhnt|landscape|panorama|habitat|forest|plantation|market|óleo|\\boil\\b|bowl|bottle', re.I)
GOOD = re.compile(r'flower|flor|blüte|fleur|fruit|fruto|frucht|leaf|leaves|hoja|blatt|blossom|close|macro|inflorescence|bloom|berries|berry', re.I)

# İlk görsel bitkinin kendisi olsun: ürün/baharat fotoğrafı (tohum, kuru meyve, kabuk,
# tane) geriye düşer. Metinde canlı bitkiyi anlatan bir sözcük de varsa ceza kalkar.
URUN = re.compile(r'\b(seeds?|dried|dry|pods?|beans?|spices?|powder|ground|grains?|kernels?|market|bazaar|isolated|white background|tohum|baharat)\b', re.I)
CANLI = re.compile(r'\b(plants?|trees?|shrubs?|fields?|flowers?|flowering|leaves|leaf|habit|bloom|blossom|in situ|wild|garden|cultivat\w*|farm|growing)\b', re.I)
# Elle reddedilen dosyalar: seçici bunları bir daha önermez (bitki değil ürün fotoğrafı).
RED = {
    'yildizanason': ['Dried Star Anise Fruit Seeds.jpg', 'Illicium verum20170511 7548.jpg', 'Illicium verum20170511 7552.jpg', 'Illicium verum20170511 7549.jpg', 'Illicium verum20170511 7551.jpg'],
    'kimyon': ['Seeds of Cumin.jpg', 'Dried cumin seeds.jpg', 'Jeragam.jpg'],  # Jeragam aslında rezene
    'fasulye': ['Pinto Beans Seeds.jpg', 'Black Turtle Bean.jpg', 'Haricot rouge cultivé au Bénin.jpg'],
    'kakule': ['Cardamom pods - Green BNC.jpg'],
}

UA = 'BitkiTabani/1.0 (https://bitkitabani.com; image sync)'
OUT = os.path.join(ROOT, 'img')
META = os.path.join(ROOT, 'images.json')
os.makedirs(OUT, exist_ok=True)
meta = json.load(open(META, encoding='utf-8')) if os.path.exists(META) else {}

_SON = [0.0]      # son isteğin zamanı; istekler arasına en az ARA kadar boşluk konur
ARA = 0.4

def get(url, binary=False):
    """Commons'tan indirir. 429'da uzun bekler.

    Wikimedia hız sınırı aştığımızda 429 döndürüyor ve kısa bir
    beklemeyle tekrar denemek sınırı daha da sıkıştırıyor. Bu yüzden
    429 ayrı ele alınıyor: sunucu Retry-After veriyorsa ona uyuluyor,
    vermiyorsa bekleme 30 saniyeden başlayıp ikiye katlanıyor. Diğer
    hatalarda kısa bekleme yeterli, çünkü onlar genellikle geçici ağ
    hatalarıdır.
    """
    bekle = 30
    for attempt in range(6):
        ara = ARA - (time.time() - _SON[0])
        if ara > 0:
            time.sleep(ara)
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            _SON[0] = time.time()
            return data if binary else json.loads(data)
        except urllib.error.HTTPError as e:
            _SON[0] = time.time()
            if e.code == 429:
                ra = e.headers.get('Retry-After')
                s_ = int(ra) if (ra or '').isdigit() else bekle
                print('  429, %d sn bekleniyor (deneme %d)' % (s_, attempt + 1))
                time.sleep(min(s_, 300)); bekle = min(bekle * 2, 300)
                continue
            print('  tekrar', attempt + 1, e); time.sleep(3 * (attempt + 1))
        except Exception as e:
            _SON[0] = time.time()
            print('  tekrar', attempt + 1, e); time.sleep(3 * (attempt + 1))
    raise RuntimeError('indirilemedi: ' + url)

def beyaz_fon(veri):
    """Görüntünün kenar piksellerinin ne kadarı düz beyaz: stüdyo/katalog fotoğrafını yakalar
    (beyaz zemin üzerinde tohum, sebze, meyve). 0–1 arası oran döner; ölçülemezse 0."""
    try:
        from PIL import Image
        import io
        im = Image.open(io.BytesIO(veri) if isinstance(veri, (bytes, bytearray)) else veri).convert('RGB')
        im.thumbnail((240, 240)); w, h = im.size; px = im.load()
        k = [px[x, y] for x in range(0, w, 2) for y in (0, 1, h - 1, h - 2)] + [px[x, y] for y in range(0, h, 2) for x in (0, 1, w - 1, w - 2)]
        return sum(1 for r, g, b in k if r > 228 and g > 228 and b > 228 and max(r, g, b) - min(r, g, b) < 22) / max(1, len(k))
    except Exception:
        return 0.0
BEYAZ_SINIR = 0.35   # kenarın üçte birinden fazlası düz beyazsa ilk görsel olmaz


def clean(h):
    t = re.sub(r'<[^>]+>', ' ', h or '')
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()[:140]

def taxon_of(p):
    t = POWO.get(p['id']) or p['la'].split(',')[0].strip()
    return re.sub(r'\s+ve diğer.*$', '', t)

def auto_pick(taxon, haric=(), siki=False):
    """Wikidata P18, sonra Commons 'Quality images' araması; yalnızca gerçek fotoğraflar."""
    cands = []
    try:
        r = get('https://www.wikidata.org/w/api.php?format=json&action=query&list=search&srlimit=1&srsearch=' + urllib.parse.quote('haswbstatement:"P225=' + taxon + '"'))
        hits = r.get('query', {}).get('search', [])
        if hits:
            c = get('https://www.wikidata.org/w/api.php?format=json&action=wbgetclaims&property=P18&entity=' + hits[0]['title'])
            cands += [('p18', x['mainsnak']['datavalue']['value']) for x in c.get('claims', {}).get('P18', []) if 'datavalue' in x['mainsnak']]
    except Exception as e:
        print('  wikidata hatası', e)
    for src, q in [('qi', '"' + taxon + '" incategory:Quality_images'), ('gen', '"' + taxon + '" filetype:bitmap -illustration -drawing -herbarium')]:
        try:
            r = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&list=search&srnamespace=6&srlimit=20&srsearch=' + urllib.parse.quote(q))
            cands += [(src, h['title'][5:]) for h in r.get('query', {}).get('search', [])]
        except Exception as e:
            print('  arama hatası', e)
    seen, scored = set(), []
    for rank, (src, f) in enumerate(cands):
        if f in seen: continue
        seen.add(f)
        j = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=mime|size|extmetadata&iiextmetadatafilter=Categories|ImageDescription&titles=' + urllib.parse.quote('File:' + f))
        page = list(j['query']['pages'].values())[0]
        ii = (page.get('imageinfo') or [{}])[0]
        if ii.get('mime') not in ('image/jpeg', 'image/webp') or (ii.get('width') or 0) < 800: continue
        m = ii.get('extmetadata', {})
        text = ' '.join([f, m.get('Categories', {}).get('value', ''), m.get('ImageDescription', {}).get('value', '')])
        if BAD.search(text): continue
        if taxon.split()[0].lower() not in text.lower(): continue
        canli = bool(CANLI.search(text))
        if siki and (not canli or URUN.search(f) or any(f.startswith(h.rsplit(' ',1)[0]) for h in haric if h[-4:]=='.jpg' and re.search(r'\d{8} \d+\.jpg$', h))): continue
        score = ((3 if src == 'qi' else 0) + (2 if GOOD.search(text) else 0) + (1 if (ii.get('height') or 0) >= (ii.get('width') or 1) else 0)
                 + (1 if canli else 0) - (4 if URUN.search(text) and not canli else 0) - rank * 0.01)
        scored.append((score, f))
    scored.sort(reverse=True)
    # Beyaz fonlu stüdyo fotoğrafı ilk görsel olmasın: sırayla küçük önizlemeye bakılır.
    for _, f in scored:
        if f in haric: continue
        try:
            j = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url&iiurlwidth=240&titles=' + urllib.parse.quote('File:' + f))
            ii = (list(j['query']['pages'].values())[0].get('imageinfo') or [{}])[0]
            if beyaz_fon(get(ii.get('thumburl') or ii['url'], binary=True)) > 0.12:
                print('  beyaz fon, geçildi:', f); continue
        except Exception as e:
            print('  önizleme alınamadı', f, e)
        return f
    return None

WANT = dict(FILES)
for p in _D['P']:
    if p['id'] in WANT: continue
    _kucuk = os.path.join(OUT, f"{p['id']}-500.jpg")
    _haric = ()
    if meta.get(p['id'], {}).get('auto') and meta[p['id']].get('file'):
        _f = meta[p['id']]['file']
        if (os.path.exists(_kucuk) and beyaz_fon(_kucuk) > BEYAZ_SINIR) or _f in RED.get(p['id'], ()) \
                or (URUN.search(_f) and not CANLI.search(_f)):
            print('ilk görsel bitki değil ya da beyaz fonlu, yeniden seçiliyor:', p['id'], _f)
            _haric = tuple(RED.get(p['id'], ())) + (_f,)
        else:
            WANT[p['id']] = meta[p['id']]['file']; continue
    f = auto_pick(taxon_of(p), _haric or tuple(RED.get(p['id'], ())), siki=p['id'] in RED)
    print('otomatik seçim:', p['id'], '→', f)
    if f: WANT[p['id']] = f; meta.setdefault(p['id'], {})['auto'] = True

changed = 0
for pid, fname in WANT.items():
    big = os.path.join(OUT, f'{pid}-960.jpg'); small = os.path.join(OUT, f'{pid}-500.jpg')
    if meta.get(pid, {}).get('file') == fname and os.path.exists(big) and os.path.exists(small):
        continue
    print('indiriliyor:', pid, fname)
    q = ('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo'
         '&iiprop=url|size|extmetadata&iiextmetadatafilter=Artist|LicenseShortName|LicenseUrl'
         '&titles=' + urllib.parse.quote('File:' + fname))
    for w in (960, 500):
        j = get(q + f'&iiurlwidth={w}')
        page = list(j['query']['pages'].values())[0]
        ii = page['imageinfo'][0]
        data = get(ii.get('thumburl') or ii['url'], binary=True)
        open(big if w == 960 else small, 'wb').write(data)
        if w == 960:
            m = ii.get('extmetadata', {})
            meta[pid] = {
                'auto': pid not in FILES,
                'file': fname,
                'page': ii.get('descriptionurl'),
                'w': ii.get('thumbwidth') or ii.get('width'), 'h': ii.get('thumbheight') or ii.get('height'),
                'artist': clean(m.get('Artist', {}).get('value')),
                'license': clean(m.get('LicenseShortName', {}).get('value')),
                'licenseUrl': (m.get('LicenseUrl', {}) or {}).get('value', ''),
            }
        else:
            meta[pid]['w500'] = ii.get('thumbwidth') or ii.get('width')
            meta[pid]['h500'] = ii.get('thumbheight') or ii.get('height')
        time.sleep(1)
    changed += 1

# Paylaşım önizlemesi ve Google Discover için 1280 px sürüm (Discover en az 1200 px ister)
for pid, fname in WANT.items():
    big = os.path.join(OUT, f'{pid}-1280.jpg')
    if os.path.exists(big) and meta.get(pid, {}).get('b1280') == fname: continue
    try:
        j = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url|size&iiurlwidth=1280&titles=' + urllib.parse.quote('File:' + fname))
        ii = list(j['query']['pages'].values())[0]['imageinfo'][0]
        if (ii.get('thumbwidth') or ii.get('width') or 0) < 1200: continue
        open(big, 'wb').write(get(ii.get('thumburl') or ii['url'], binary=True))
        meta.setdefault(pid, {})['b1280'] = fname
        print('1280:', pid); time.sleep(1)
    except Exception as e:
        print('1280 alınamadı:', pid, e)

for pid in list(meta):
    if pid not in WANT: meta.pop(pid)
json.dump(meta, open(META, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
print('bitti; güncellenen:', changed, 'toplam:', len(meta))
