"""Tanıma görselleri: her bitki için Commons'tan üç görsel seçer: botanik çizim, çiçekli hâli, kurutulmuş (drog) hâli.
Bitki sayfasındaki "Nasıl tanınır?" bölümünde ve Reels'te kullanılır. img/tanima/<id>-<tür>.jpg ve img/tanima/meta.json.
Bir kez bulunan görsel bir daha aranmaz; bulunamayan tür 'yok' diye işaretlenir (meta.json'dan silinirse yeniden aranır).
Çizim standardı: yalnızca Köhler (1887) ya da Thomé (1885), aynı tür. Elle seçim: ELLE sözlüğüne {'bitki:tür': 'Commons dosya adı'} eklenir.
GitHub Actions'ta derlemeden önce çalışır: python3 tools/tanima.py [bitki_id ...]"""
import json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
OUT = os.path.join(ROOT, 'img', 'tanima'); META = os.path.join(OUT, 'meta.json')
UA = 'BitkiTabani/1.0 (https://bitkitabani.com; identification images)'
TURLER = ['cizim', 'cicek', 'kuru']
AD = {'cizim': 'Botanik çizim', 'cicek': 'Çiçekli hâli', 'kuru': 'Kurutulmuş hâli'}
ELLE = {}   # örn. 'zencefil:kuru': 'Dried ginger.jpg'

PLATE = r'köhler|kohler|koehler|thomé|thome|illustrat|\bplate\b|tafel|lithograph|engraving|drawing|botanical|flora von|medizinal|sowerby|curtis|blackwell|fuchs'
Q = {   # arama ifadesi, metinde aranan, metinde olmaması gereken
 'cizim': ('"{t}" (Köhler OR illustration OR plate OR Tafel OR Thomé OR botanical)', PLATE, r'herbari|specimen|photo of|stamp|coin|map'),
 'cicek': ('"{t}" (flower OR flowers OR inflorescence OR Blüte OR fleur OR blossom) filetype:bitmap', r'flower|blüte|fleur|flor\b|flores|inflorescen|blossom|bloom|anthes', PLATE + r'|herbari|specimen|stamp|map|dried|droge'),
 'kuru': ('"{t}" (dried OR droge OR Droge OR getrocknet OR séché OR seco OR "dry" OR drug OR herba OR radix OR rhizoma OR semen OR folium OR flos) filetype:bitmap', r'dried|droge|drug\b|getrocknet|séch|seco|secad|\bdry\b|herba|radix|rhizoma|semen|folium|flos|cortex|fructus|spice|tea\b', PLATE + r'|herbari|specimen|stamp|map|fresh plant|in situ'),
}

def get(url, binary=False):
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=50) as r: d = r.read()
            return d if binary else json.loads(d)
        except Exception as e:
            print('  tekrar', a + 1, str(e)[:80]); time.sleep(2 * (a + 1))
    raise RuntimeError('alınamadı')

def plain(h): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()

def ara(taxon, tur, main_file):
    q, need, bad = Q[tur]; genus = taxon.split()[0].lower()
    url = ('https://commons.wikimedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=6&gsrlimit=30&gsrsearch='
           + urllib.parse.quote(q.format(t=taxon)) + '&prop=imageinfo&iiprop=mime|size|url|extmetadata&iiurlwidth=1280'
           + '&iiextmetadatafilter=Categories|ImageDescription|Artist|LicenseShortName|ObjectName')
    pages = list(get(url).get('query', {}).get('pages', {}).values())
    best = None
    for pg in sorted(pages, key=lambda x: x.get('index', 99)):
        t = pg['title'][5:]; ii = (pg.get('imageinfo') or [{}])[0]; m = ii.get('extmetadata', {})
        if t == main_file or ii.get('mime') not in ('image/jpeg', 'image/png'): continue
        if (ii.get('width') or 0) < 700 or (ii.get('height') or 0) < 700: continue
        lic = m.get('LicenseShortName', {}).get('value', '')
        if not re.search(r'CC|Public domain|PD|No restrictions', lic, re.I): continue
        text = ' '.join([t, m.get('ObjectName', {}).get('value', ''), m.get('Categories', {}).get('value', ''), plain(m.get('ImageDescription', {}).get('value', ''))]).lower()
        if genus not in text or not re.search(need, text, re.I) or re.search(bad, text, re.I): continue
        score = (3 if taxon.lower() in text else 0) + (2 if 'quality' in text else 0) + (2 if tur == 'cizim' and re.search(r'köhler|kohler|koehler|thomé', text) else 0) - pg.get('index', 0) * 0.05
        if not best or score > best[0]:
            best = (score, t, ii.get('thumburl') or ii.get('url'), (plain(m.get('Artist', {}).get('value', '')) or 'Wikimedia Commons')[:60], lic)
    return best

def cizim(taxon):
    """Standart çizim: yalnızca aynı türün Köhler's Medizinal-Pflanzen (1887) levhası, yoksa Thomé, Flora von Deutschland (1885).
    Akraba tür levhası kullanılmaz (tanımada yanıltır); ikisi de yoksa çizim yok."""
    t = taxon.lower()
    for q, need in [('intitle:"Medizinal-Pflanzen" "' + taxon + '"', lambda x: t in x and 'medizinal-pflanzen' in x),
                    (taxon + ' Thomé', lambda x: ('illustration ' + t) in x)]:
        r = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&list=search&srnamespace=6&srlimit=8&srsearch=' + urllib.parse.quote(q))
        for h in r.get('query', {}).get('search', []):
            if need(h['title'].lower()): return tek(taxon, h['title'][5:])
    return None

def tek(taxon, f):   # elle seçilen dosya
    j = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1280&iiextmetadatafilter=Artist|LicenseShortName&titles=' + urllib.parse.quote('File:' + f))
    ii = list(j['query']['pages'].values())[0]['imageinfo'][0]; m = ii.get('extmetadata', {})
    return (9, f, ii.get('thumburl') or ii['url'], (plain(m.get('Artist', {}).get('value', '')) or 'Wikimedia Commons')[:60], m.get('LicenseShortName', {}).get('value', ''))

def main(only=None):
    from refs import FILES, POWO
    import kuyruk as K
    D = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
    plants = [(p['id'], p['la']) for p in D['P']] + [(q['id'], q['la']) for q in K.Q if q['id'] not in {p['id'] for p in D['P']}]
    for q in K.Q: POWO.setdefault(q['id'], q.get('taxon'))
    os.makedirs(OUT, exist_ok=True)
    meta = json.load(open(META, encoding='utf-8')) if os.path.exists(META) else {}
    n = 0
    for pid, la in plants:
        if only and pid not in only: continue
        taxon = re.sub(r'\s+ve diğer.*$', '', (POWO.get(pid) or la.split(',')[0]).strip())
        for tur in TURLER:
            key = f'{pid}:{tur}'; fn = f'{pid}-{tur}.jpg'
            if key in meta and (meta[key] == 'yok' or os.path.exists(os.path.join(OUT, fn))) and key not in ELLE: continue
            try:
                b = tek(taxon, ELLE[key]) if key in ELLE else (cizim(taxon) if tur == 'cizim' else ara(taxon, tur, FILES.get(pid, '')))
                if not b: meta[key] = 'yok'; print('tanıma:', key, 'bulunamadı'); continue
                from PIL import Image
                import io
                im = Image.open(io.BytesIO(get(b[2], binary=True))).convert('RGB')
                im.thumbnail((1280, 1280)); im.save(os.path.join(OUT, fn), 'JPEG', quality=84, optimize=True)
                meta[key] = {'file': b[1], 'artist': b[3], 'license': b[4], 'page': 'https://commons.wikimedia.org/wiki/File:' + urllib.parse.quote(b[1].replace(' ', '_'))}
                print('tanıma:', key, '←', b[1]); n += 1
            except Exception as e:
                print('tanıma hatası:', key, str(e)[:120])
            time.sleep(0.3)
        json.dump(meta, open(META, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('tanıma: yeni görsel', n)

if __name__ == '__main__':
    main(set(sys.argv[1:]) or None)
