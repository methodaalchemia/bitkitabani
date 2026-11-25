"""Commons dışı kaynaklardan (şimdilik iNaturalist) görsel indirir.

refs.DIS'teki her kayıt için fotoğrafı indirir, 500/960/1280 boylarını üretir ve
images.json'a künyesini yazar. Zaten doğru künyeyle duranı atlar, ağa çıkmaz.

Neden ayrı: fetch_images.py Commons API'sine bağlı — dosya adıyla arar, lisansı
oradan okur. Commons'ta fotoğrafı olmayan bitkiler için (Amazon türlerinin çoğu)
o yol kapalı. Bu betik künyeyi refs.DIS'ten alır, yalnız dosyayı indirir.
"""
import io, json, os, sys
from PIL import Image

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
from refs import DIS

import urllib.request
BASLIK = {'User-Agent': 'BitkiTabani/1.0 (https://bitkitabani.com; iletisim@bitkitabani.com)'}
META = os.path.join(KOK, 'images.json')
meta = json.load(open(META, encoding='utf-8')) if os.path.exists(META) else {}
IMG = os.path.join(KOK, 'img')
BOY = (500, 960, 1280)

degisen = 0
for pid, k in DIS.items():
    var = meta.get(pid, {})
    tam = all(os.path.exists(os.path.join(IMG, f'{pid}-{b}.jpg')) for b in BOY)
    if tam and var.get('page') == k['page']:
        continue
    print('indiriliyor:', pid, k['page'])
    ham = urllib.request.urlopen(urllib.request.Request(k['url'], headers=BASLIK), timeout=90).read()
    im = Image.open(io.BytesIO(ham)).convert('RGB')
    yeni = {a: k[a] for a in ('page', 'kaynak', 'artist', 'license', 'licenseUrl')}
    for a in ('not', 'notEn'):
        if k.get(a): yeni[a] = k[a]
    yeni['auto'] = False
    yeni['file'] = os.path.basename(k['url'])
    for b in BOY:
        o = im.copy()
        o.thumbnail((b, b * 4))
        o.save(os.path.join(IMG, f'{pid}-{b}.jpg'), quality=86, optimize=True)
        if b == 500: yeni['w500'], yeni['h500'] = o.size
        if b == 960: yeni['w'], yeni['h'] = o.size
        if b == 1280: yeni['b1280'] = yeni['file']
    meta[pid] = yeni
    degisen += 1

if degisen:
    json.dump(meta, open(META, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
print(f'{len(DIS)} dış görsel, {degisen} güncellendi')
