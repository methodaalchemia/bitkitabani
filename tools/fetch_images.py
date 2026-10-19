"""Commons'tan seçili bitki fotoğraflarını indirir (500 ve 960 px), kredi bilgisini images.json'a yazar.
GitHub Actions'ta çalışır; yerelde de `python3 tools/fetch_images.py` ile çalıştırılabilir."""
import json, os, re, sys, time, urllib.parse, urllib.request, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from refs import FILES

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

changed = 0
for pid, fname in FILES.items():
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
    if pid not in FILES: meta.pop(pid)
json.dump(meta, open(META, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
print('bitti; güncellenen:', changed, 'toplam:', len(meta))
