# Halk hekimliği hikâyeleri için kapak görselleri (1200×800): marka renkleri, kilim motifleri ve başlık.
# Her hikâyenin kapağı renk + motif + başlıkla diğerlerinden ayrılır. Var olanlar yeniden üretilmez (başlık değişirse silinip yeniden üretilir).
import os, sys, json, hashlib
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from halk import hikayeler
OUT = os.path.join(HERE, 'img', 'hikaye'); os.makedirs(OUT, exist_ok=True)
F = os.path.join(HERE, 'tools', 'fonts')
def font(n, s): return ImageFont.truetype(os.path.join(F, n), s)
RENK = ['#A3271B', '#2A3A6E', '#9C6A12', '#2E6A45', '#6E3F63', '#6B4A2E', '#2F5E62', '#8A3B1E', '#4B3F72', '#55622A']
KREM = '#F1EADD'
W, H = 1200, 800

def motif(d, kind, x, y, s, col, w=3):
    h = s / 2
    if kind == 0:   # baklava ve göz
        d.polygon([(x, y - h), (x + h, y), (x, y + h), (x - h, y)], outline=col, width=w)
        d.polygon([(x, y - h / 2.5), (x + h / 2.5, y), (x, y + h / 2.5), (x - h / 2.5, y)], fill=col)
    elif kind == 1:  # basamaklı haç
        a = s / 6
        for dx, dy in ((0, 0), (a, 0), (-a, 0), (0, a), (0, -a), (2 * a, 0), (-2 * a, 0), (0, 2 * a), (0, -2 * a)):
            d.rectangle([x + dx - a / 2, y + dy - a / 2, x + dx + a / 2, y + dy + a / 2], fill=col)
    elif kind == 2:  # koçboynuzu
        d.arc([x - h, y - h / 1.4, x, y + h / 1.4], 90, 270, fill=col, width=w + 1)
        d.arc([x, y - h / 1.4, x + h, y + h / 1.4], 270, 90, fill=col, width=w + 1)
        d.line([x, y - h, x, y + h], fill=col, width=w)
    elif kind == 3:  # yıldız (sekiz köşe)
        d.polygon([(x - h, y - h / 3), (x + h, y - h / 3), (x + h, y + h / 3), (x - h, y + h / 3)], outline=col, width=w)
        d.polygon([(x - h / 3, y - h), (x + h / 3, y - h), (x + h / 3, y + h), (x - h / 3, y + h)], outline=col, width=w)
    else:            # hayat ağacı
        d.line([x, y - h, x, y + h], fill=col, width=w + 1)
        for k in (-0.5, 0, 0.5):
            d.line([x, y + k * h, x - h / 1.6, y + k * h - h / 3], fill=col, width=w)
            d.line([x, y + k * h, x + h / 1.6, y + k * h - h / 3], fill=col, width=w)

def sar(d, metin, f, gen):
    sat, cur = [], ''
    for w_ in metin.split():
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=f) <= gen: cur = t
        else: sat.append(cur); cur = w_
    if cur: sat.append(cur)
    return sat

def kapak(h, i):
    hs = int(hashlib.md5(h['slug'].encode()).hexdigest(), 16)
    bg = RENK[i % len(RENK)]; kind = (hs >> 3) % 5; kind2 = (kind + 1 + (hs >> 7) % 4) % 5
    im = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(im)
    # büyük soluk motif (sağ alt), konumu hikâyeye göre değişir
    soluk = tuple(int(int(bg[j:j + 2], 16) * 0.78 + 0xF1 * 0.22) for j in (1, 3, 5))
    motif(d, kind, 930 + (hs % 120), 500 + (hs >> 11) % 120, 520, soluk, 14)
    # üst ve alt kilim şeritleri
    for y in (46, H - 46):
        for x in range(30, W, 60):
            motif(d, kind2 if (x // 60) % 2 else kind, x, y, 34, KREM, 3)
    d.line([0, 86, W, 86], fill=KREM, width=2); d.line([0, H - 86, W, H - 86], fill=KREM, width=2)
    ey = 'HALK HEKİMLİĞİNDEN' + (' · ' + h['yore'].upper() if h.get('yore') and len(h['yore']) < 40 else '')
    d.text((80, 140), ey, font=font('CourierPrime-Regular.ttf', 30), fill=KREM)
    bas = h['baslik'].rstrip('…')
    for sz in (78, 70, 62, 54, 48):
        f = font('Alegreya[wght].ttf', sz)
        try: f.set_variation_by_name('Bold')
        except Exception: pass
        L = sar(d, bas, f, W - 200)
        if len(L) * sz * 1.18 <= 400: break
    y = 210
    for l in L: d.text((80, y), l, font=f, fill=KREM); y += int(sz * 1.18)
    d.text((80, H - 160), 'Kaynak: ' + h['kisa'], font=font('AlegreyaSans-Italic.ttf', 28), fill=KREM)
    d.text((W - 80, H - 160), 'bitkitabani.com', font=font('AlegreyaSans-Bold.ttf', 30), fill=KREM, anchor='ra')
    return im

def main():
    H_ = hikayeler(); n = 0
    idx = os.path.join(OUT, 'basliklar.json')
    eski = json.load(open(idx, encoding='utf-8')) if os.path.exists(idx) else {}
    for i, h in enumerate(H_):
        p = os.path.join(OUT, h['slug'] + '.jpg')
        if os.path.exists(p) and eski.get(h['slug']) == h['baslik']: continue
        kapak(h, i).save(p, quality=86, optimize=True); n += 1
        eski[h['slug']] = h['baslik']
    canli = {h['slug'] for h in H_}
    for f in os.listdir(OUT):
        if f.endswith('.jpg') and f[:-4] not in canli: os.remove(os.path.join(OUT, f)); eski.pop(f[:-4], None)
    json.dump(eski, open(idx, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('kapak', n, 'yeni')

if __name__ == '__main__':
    main()
