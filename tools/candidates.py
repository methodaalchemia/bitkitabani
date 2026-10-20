"""Fotoğraf adayı toplama: tools/cand.txt içindeki her satır 'id | arama terimi'.
Her bitki için en çok 16 aday fotoğrafı 400 px olarak cand/<id>/ klasörüne indirir (yalnızca seçim yapmak için)."""
import json, os, re, sys, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.argv = [sys.argv[0]]
import importlib.util
spec = importlib.util.spec_from_file_location('fi_lib', os.path.join(ROOT, 'tools', 'fetch_images.py'))
src = open(os.path.join(ROOT, 'tools', 'fetch_images.py'), encoding='utf-8').read().split('WANT = dict(FILES)')[0]
ns = {'__file__': os.path.join(ROOT, 'tools', 'fetch_images.py')}
exec(src, ns)
get, BAD = ns['get'], ns['BAD']
out = os.path.join(ROOT, 'cand'); os.makedirs(out, exist_ok=True)
for line in open(os.path.join(ROOT, 'tools', 'cand.txt'), encoding='utf-8'):
    if '|' not in line or line.startswith('#'): continue
    pid, term = [x.strip() for x in line.split('|', 1)]
    d = os.path.join(out, pid); os.makedirs(d, exist_ok=True)
    titles = []
    for q in ['"' + term + '" incategory:Quality_images', '"' + term + '" filetype:bitmap -illustration -drawing -herbarium']:
        r = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&list=search&srnamespace=6&srlimit=30&srsearch=' + urllib.parse.quote(q))
        titles += [h['title'][5:] for h in r.get('query', {}).get('search', []) if h['title'][5:] not in titles]
    lst = []
    for f in titles:
        if len(lst) >= 12: break
        j = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url|mime|size|extmetadata&iiextmetadatafilter=Categories|ImageDescription&iiurlwidth=400&titles=' + urllib.parse.quote('File:' + f))
        ii = (list(j['query']['pages'].values())[0].get('imageinfo') or [{}])[0]
        if ii.get('mime') not in ('image/jpeg', 'image/webp') or (ii.get('width') or 0) < 800: continue
        m = ii.get('extmetadata', {})
        if BAD.search(' '.join([f, m.get('Categories', {}).get('value', ''), m.get('ImageDescription', {}).get('value', '')])): continue
        n = len(lst) + 1
        open(os.path.join(d, f'{n:02d}.jpg'), 'wb').write(get(ii['thumburl'], binary=True))
        lst.append({'n': n, 'file': f, 'w': ii.get('width'), 'h': ii.get('height')})
        print(pid, n, f)
    json.dump(lst, open(os.path.join(d, 'list.json'), 'w'), ensure_ascii=False, indent=1)
