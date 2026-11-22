"""Commons kategorisindeki adayların numaralı önizleme tablosu (elle seçim için)."""
import json, sys, io, urllib.parse, urllib.request
from PIL import Image, ImageDraw
UA = {'User-Agent': 'BitkiTabani/1.0 (https://bitkitabani.com; iletisim@bitkitabani.com)'}
def get(u, binary=False):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60) as r:
        b = r.read()
    return b if binary else json.loads(b)
for taxon in sys.argv[1:]:
    q = 'incategory:"' + taxon + '" filetype:bitmap'
    r = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&list=search&srnamespace=6&srlimit=40&srsearch=' + urllib.parse.quote(q))
    files = [h['title'][5:] for h in r.get('query', {}).get('search', [])]
    thumbs, names = [], []
    for f in files:
        try:
            j = get('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url|size|mime&iiurlwidth=240&titles=' + urllib.parse.quote('File:' + f))
            ii = (list(j['query']['pages'].values())[0].get('imageinfo') or [{}])[0]
            if ii.get('mime') != 'image/jpeg' or ii.get('width', 0) < 800: continue
            im = Image.open(io.BytesIO(get(ii['thumburl'], binary=True))).convert('RGB')
            im.thumbnail((240, 180)); thumbs.append(im); names.append(f)
        except Exception as e:
            print('hata', f, e)
        if len(thumbs) >= 24: break
    cols = 6; rows = (len(thumbs) + cols - 1) // cols or 1
    s = Image.new('RGB', (cols * 250, rows * 200), 'white'); d = ImageDraw.Draw(s)
    for n, im in enumerate(thumbs):
        x, y = (n % cols) * 250, (n // cols) * 200
        s.paste(im, (x, y)); d.rectangle([x, y, x + 30, y + 22], fill='black'); d.text((x + 4, y + 4), str(n), fill='white')
    slug = taxon.replace(' ', '_')
    s.save(f'aday/{slug}.png')
    json.dump(names, open(f'aday/{slug}.json', 'w'), ensure_ascii=False, indent=0)
    print(taxon, len(names))
