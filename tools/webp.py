"""img/*.jpg dosyalarının WebP kopyalarını üretir (yoksa ya da jpg daha yeniyse)."""
import os, sys
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = os.path.join(ROOT, 'img'); n = 0
for f in sorted(os.listdir(d)):
    if not f.endswith('.jpg'): continue
    src = os.path.join(d, f); dst = src[:-4] + '.webp'
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): continue
    Image.open(src).convert('RGB').save(dst, 'WEBP', quality=78, method=6); n += 1
print('webp', n)
