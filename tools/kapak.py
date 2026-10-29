# Halk hekimliği hikâyeleri için kapak görselleri (1200×800): marka renkleri, kilim motifleri ve başlık.
# Her hikâyenin kapağı renk + motif + başlıkla diğerlerinden ayrılır. Var olanlar yeniden üretilmez (başlık değişirse silinip yeniden üretilir).
import os, sys, json, hashlib
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from halk import hikayeler
from yazilar import YAZILAR
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

IMG = json.load(open(os.path.join(HERE, 'images.json'), encoding='utf-8'))
GDIR = os.path.join(HERE, 'img', 'hikaye-gorsel')
GK = json.load(open(os.path.join(GDIR, 'kaynak.json'), encoding='utf-8')) if os.path.exists(os.path.join(GDIR, 'kaynak.json')) else {}
def gorsel(g):
    """(dosya, künye) — önce hikâyeye özel Commons görseli, sonra katalogdaki bitki fotoğrafı."""
    if not g: return None, ''
    if g in GK and os.path.exists(os.path.join(GDIR, g + '.jpg')):
        k = GK[g]; return os.path.join(GDIR, g + '.jpg'), f"{k['artist']}, {k['license']}"
    f = os.path.join(HERE, 'img', g + '-1280.jpg')
    if os.path.exists(f):
        k = IMG.get(g, {}); return f, (f"{k.get('artist', '')}, {k.get('license', '')}".strip(', ') if k else '')
    return None, ''

PW = 470   # fotoğraf şeridinin genişliği
def kapak(h, i):
    hs = int(hashlib.md5(h['slug'].encode()).hexdigest(), 16)
    bg = RENK[i % len(RENK)]; kind = (hs >> 3) % 5; kind2 = (kind + 1 + (hs >> 7) % 4) % 5
    im = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(im)
    gf, kunye = gorsel(h.get('gorsel'))
    tw = W - (PW if gf else 0)
    soluk = tuple(int(int(bg[j:j + 2], 16) * 0.78 + 0xF1 * 0.22) for j in (1, 3, 5))
    motif(d, kind, tw - 160 + (hs % 80), 520 + (hs >> 11) % 100, 420, soluk, 12)
    if gf:
        ph = Image.open(gf).convert('RGB')
        r = max(PW / ph.width, H / ph.height); ph = ph.resize((int(ph.width * r) + 1, int(ph.height * r) + 1))
        ox = (ph.width - PW) * ((hs >> 5) % 3) // 2; oy = (ph.height - H) // 2
        ph = ph.crop((ox, oy, ox + PW, oy + H))
        if (hs >> 9) % 2: ph = ph.transpose(Image.FLIP_LEFT_RIGHT)
        im.paste(ph, (tw, 0))
        # fotoğrafla renk alanı arasında dikey kilim şeridi
        d.rectangle([tw - 34, 0, tw, H], fill=bg)
        for y in range(20, H, 46): motif(d, kind2 if (y // 46) % 2 else kind, tw - 17, y, 26, KREM, 2)
        if kunye:
            fk = font('AlegreyaSans-Italic.ttf', 18); t = 'Görsel: ' + kunye[:60]
            x1 = W - 14; x0 = x1 - d.textlength(t, font=fk) - 16
            d.rectangle([x0, H - 40, x1, H - 12], fill=(0, 0, 0)); d.text((x1 - 8, H - 26), t, font=fk, fill=KREM, anchor='rm')
    for y in (46, H - 46):
        for x in range(30, tw - 40, 60):
            motif(d, kind2 if (x // 60) % 2 else kind, x, y, 34, KREM, 3)
    d.line([0, 86, tw - 34, 86], fill=KREM, width=2); d.line([0, H - 86, tw - 34, H - 86], fill=KREM, width=2)
    ey = h.get('ust') or 'HALK HEKİMLİĞİNDEN'
    d.text((70, 140), ey, font=font('CourierPrime-Regular.ttf', 28), fill=KREM)
    bas = h['baslik'].rstrip('…'); gen = tw - 34 - 140
    for sz in (96, 86, 76, 68, 60, 52, 46):
        f = font('Alegreya[wght].ttf', sz)
        try: f.set_variation_by_name('Bold')
        except Exception: pass
        L = sar(d, bas, f, gen)
        if len(L) * sz * 1.12 <= 400 and all(d.textlength(l, font=f) <= gen for l in L): break
    y = 200 + max(0, (400 - len(L) * int(sz * 1.12)) // 2)
    for l in L: d.text((70, y), l, font=f, fill=KREM); y += int(sz * 1.12)
    if h.get('yore') and len(h['yore']) < 34: d.text((70, H - 150), h['yore'], font=font('AlegreyaSans-Bold.ttf', 30), fill=KREM)
    d.text((70, H - 112), 'bitkitabani.com', font=font('AlegreyaSans-Italic.ttf', 24), fill=KREM)
    return im

def main():
    H_ = hikayeler() + [dict(slug='yazi-' + y['slug'], baslik=y['baslik'], kisa='Edanaz Tınmazlar · ' + str(len(y['kaynaklar'])) + ' kaynak', ust='YAZI · ' + y['tarih'][:4]) for y in YAZILAR]; n = 0
    idx = os.path.join(OUT, 'basliklar.json')
    eski = json.load(open(idx, encoding='utf-8')) if os.path.exists(idx) else {}
    for i, h in enumerate(H_):
        p = os.path.join(OUT, h['slug'] + '.jpg')
        imza = h['baslik'] + '|' + str(h.get('gorsel')) + '|v2'
        if os.path.exists(p) and eski.get(h['slug']) == imza: continue
        kapak(h, i).save(p, quality=86, optimize=True); n += 1
        eski[h['slug']] = imza
    canli = {h['slug'] for h in H_}
    for f in os.listdir(OUT):
        if f.endswith('.jpg') and f[:-4] not in canli: os.remove(os.path.join(OUT, f)); eski.pop(f[:-4], None)
    json.dump(eski, open(idx, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('kapak', n, 'yeni')

if __name__ == '__main__':
    main()
