# -*- coding: utf-8 -*-
"""Motif SVG'lerinden paylaşım önizlemesi (og:image) PNG'si üretir.

Neden ayrı bir araç: og:image SVG kabul etmiyor — Facebook, X, WhatsApp ve
Telegram SVG'yi işlemez, önizleme hiç çıkmaz. PNG gerekli. Ama derlemenin
kendisine tarayıcı bağımlılığı eklenmesin diye (site'ı GitHub Actions da
derliyor) PNG'ler burada bir kez üretilip `img/motif/` altına depoya
yazılıyor; build.py onları `img/` kopyasıyla birlikte siteye taşıyor.

Çizim deterministik (random.Random(slug)), bu yüzden yeniden çalıştırmak
aynı dosyayı üretir. Yalnız motif eklenince ya da çizim değişince çalıştır:

    python3 build.py && python3 tools/motif_png.py
"""
import os, sys, glob
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(HERE, 'site', 'img', 'motif')      # build.py üretiyor
HEDEF = os.path.join(HERE, 'img', 'motif')               # depoya yazılıyor
EN, BOY = 1200, 630                                      # og:image ölçüsü
KAGIT = '#F1EADD'                                        # --paper

if not os.path.isdir(KAYNAK):
    sys.exit('önce `python3 build.py` çalıştır: ' + KAYNAK + ' yok')
os.makedirs(HEDEF, exist_ok=True)
dosyalar = sorted(glob.glob(os.path.join(KAYNAK, '*.svg')))

# SVG dosya olarak değil, gömülü veriliyor: Chromium about:blank kaynaklı bir
# sayfanın file:// alt kaynağını yüklemiyor, çıktı boş kalıyor.
SAYFA = '''<!doctype html><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;width:{en}px;height:{boy}px;background:{kagit};
  display:flex;align-items:center;justify-content:center;overflow:hidden}}
svg{{width:{kare}px;height:{kare}px;display:block}}
</style>{svg}'''

with sync_playwright() as p:
    tar = p.chromium.launch()
    sf = tar.new_page(viewport={'width': EN, 'height': BOY}, device_scale_factor=1)
    for yol in dosyalar:
        slug = os.path.splitext(os.path.basename(yol))[0]
        svg = open(yol, encoding='utf-8').read().split('?>', 1)[-1]
        sf.set_content(SAYFA.format(en=EN, boy=BOY, kagit=KAGIT, kare=int(BOY * 0.78),
                                    svg=svg))
        sf.wait_for_timeout(60)
        sf.screenshot(path=os.path.join(HEDEF, slug + '.png'))
    tar.close()
print('üretilen PNG:', len(dosyalar), '->', HEDEF)
