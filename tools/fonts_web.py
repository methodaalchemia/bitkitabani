# Site yazı tiplerini Google Fonts yerine siteden sunmak için: tools/fonts içindeki TTF'leri
# Latin + Türkçe karakterlerle sınırlayıp WOFF2'ye çevirir (assets/fonts). GitHub Actions'ta çalışır (brotli gerekir).
import os, shutil
from fontTools import subset
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(HERE, 'tools', 'fonts'), os.path.join(HERE, 'assets', 'fonts')
os.makedirs(OUT, exist_ok=True)
U = 'U+0000-00FF,U+0100-017F,U+2010-2027,U+2030-205E,U+20AC,U+2190-2193,U+2122,U+25C6,U+25D0,U+2600,U+263E'
for src, dst in [('Alegreya[wght].ttf', 'alegreya'), ('Alegreya-Italic[wght].ttf', 'alegreya-italic'), ('AlegreyaSans-Regular.ttf', 'alegreya-sans'),
                 ('AlegreyaSans-Bold.ttf', 'alegreya-sans-bold'), ('AlegreyaSans-Italic.ttf', 'alegreya-sans-italic'), ('CourierPrime-Regular.ttf', 'courier-prime')]:
    s, d = os.path.join(SRC, src), os.path.join(OUT, dst + '.woff2')
    if not os.path.exists(s) or os.path.exists(d): continue
    subset.main([s, f'--unicodes={U}', '--flavor=woff2', '--layout-features=kern,liga,lnum,onum,pnum,tnum', f'--output-file={d}'])
    print('font', dst, os.path.getsize(d))
if os.path.exists(os.path.join(SRC, 'OFL.txt')): shutil.copy(os.path.join(SRC, 'OFL.txt'), os.path.join(OUT, 'OFL.txt'))
