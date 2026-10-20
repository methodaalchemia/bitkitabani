"""Commons'tan seçili bitki fotoğraflarını indirir (500 ve 960 px), kredi bilgisini images.json'a yazar.
GitHub Actions'ta çalışır; yerelde de `python3 tools/fetch_images.py` ile çalıştırılabilir."""
import json, os, re, sys, time, urllib.parse, urllib.request, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from refs import FILES, POWO
import json as _j
_D = _j.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
BAD = re.compile(r'illustrat|drawing|k[öo]e?hler|medizinal-pflanzen|botanical (art|plate|print)|\bplate\b|tafel|lithograph|engraving|woodcut|painting|watercolou?r|herbari|exsiccat|\bmaps?\b|distribution|diagram|molecule|stamp|coin|logo|bottle|drink|beverage|powder|capsule|svg|specimen|museum|montage|collage|mhnt|landscape|panorama|habitat|forest|plantation|market|óleo|\\boil\\b|bowl|bottle', re.I)
GOOD = re.compile(r'flower|flor|blüte|fleur|fruit|fruto|frucht|leaf|leaves|hoja|blatt|blossom|close|macro|inflorescence|bloom|berries|berry', re.I)

UA = 'BitkiTabani/1.0 (https://bitkitabani.com; image sync)'
OUT = os.path.join(ROOT, 'img')
META = os.path.join(ROOT, 'images.json')
os.makedirs(OUT, exist_ok=True)
meta = json.load(open(META, encoding='utf-8')) if os.path.exists(META) else {}

def get(url, binary=False):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            return data if binary else json.loads(data)
        except Exception as e:
            print('  tekrar', attempt + 1, e); time.sleep(3 * (attempt + 1))
    raise RuntimeError('indirilemedi: ' + url)

def clean(h):
    t = re.sub(r'<[^>]+>', ' ', h or '')
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()[:140]

def taxon_of(p):
    t = POWO.get(p['id']) or p['la'].split(',')[0].strip()
    return re.sub(r'\s+ve diğer.*$', '', t)

def auto_pick(taxon):
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
        score = (3 if src == 'qi' else 0) + (2 if GOOD.search(text) else 0) + (1 if (ii.get('height') or 0) >= (ii.get('width') or 1) else 0) - rank * 0.01
        scored.append((score, f))
    scored.sort(reverse=True)
    return scored[0][1] if scored else None

WANT = dict(FILES)
for p in _D['P']:
    if p['id'] in WANT: continue
    if meta.get(p['id'], {}).get('auto') and meta[p['id']].get('file'):
        WANT[p['id']] = meta[p['id']]['file']; continue
    f = auto_pick(taxon_of(p))
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

for pid in list(meta):
    if pid not in WANT: meta.pop(pid)
json.dump(meta, open(META, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
print('bitti; güncellenen:', changed, 'toplam:', len(meta))
