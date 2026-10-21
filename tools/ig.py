"""Instagram kaydırmalı postları: her gün bir bitki, 6 slayt (1080×1350 JPEG) ve açıklama metni.

build.py'den sonra çalışır: .cache/ig_input.json dosyasını okur, bugünün ve sonraki iki günün postunu
site/ig/<tarih>/ altına yazar (1.jpg … 6.jpg, post.json) ve site/ig/index.html önizleme sayfasını üretir.
Paylaşımı worker.js yapar (her akşam 19:00, IG_TOKEN gerekir).

Sıra: Türkiye’de en çok arandığını tahmin ettiğimiz bitkilerden başlar (IG_ORDER), sonra kataloğun geri kalanı.
Yüksek riskli ve Türkiye’de yasak/kısıtlı bitkiler Instagram’a konmaz. Kuyruktaki bitkiler yayın gününden önce paylaşılmaz.
"""
import json, os, re, sys, datetime, textwrap, html
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://bitkitabani.com'
IG_START = datetime.date(2026, 10, 21)   # ilk post günü; bundan sonraki her gün sıradaki bitki
IG_ORDER = ['zencefil', 'zerdecal', 'adacayi', 'ihlamur', 'papatya', 'isirgan', 'dagcayi', 'nane', 'kekik', 'biberiye', 'lavanta', 'corekotu',
            'atkestanesi', 'tarcin', 'ekinezya', 'ashwagandha', 'melisa', 'kantaron', 'ceviz', 'rezene', 'karanfil', 'aloe', 'incir', 'kusburnu',
            'feslegen', 'ginkgo', 'anason', 'sarimsak', 'keten', 'turunc', 'meyan', 'defne', 'kakule', 'enginar', 'devedikeni', 'hodan', 'kediotu',
            'goji', 'okaliptus', 'reishi', 'cemen', 'muskat', 'kimyon', 'gelincik', 'sumak', 'sogut', 'nar', 'pasiflora', 'zeytin', 'karabas', 'cay',
            'neem', 'hibiskus', 'graviola', 'keciboynuzu', 'mahlep', 'maca', 'yildizanason', 'mersin', 'gotukola', 'ebegumeci', 'tulsi', 'hatmi',
            'lotus', 'civanpercemi', 'hamamelis', 'murver', 'turnayemisi', 'alic', 'hayit', 'sakiz', 'kina', 'safran', 'sinameki', 'kizilcik', 'kapari',
            'karahindiba']
W, H = 1080, 1350
C = dict(paper=(241, 234, 221), sheet=(251, 246, 236), ink=(28, 33, 64), muted=(93, 88, 102), rule=(220, 207, 186), accent=(163, 39, 27),
         ochre=(185, 128, 26), indigo=(42, 58, 110), dusuk=(58, 116, 73), orta=(160, 102, 14), yuksek=(176, 42, 42))
REGC = dict(anadolu=(163, 39, 27), asya=(42, 58, 110), **{'and': (185, 128, 26)}, amazon=(46, 106, 69), kamerika=(122, 74, 110))

# ---------- yazı tipleri ----------
FD = os.path.join(ROOT, 'tools', 'fonts')
def _font(cands, size, wght=None):
    for c in cands:
        p = c if os.path.isabs(c) else os.path.join(FD, c)
        if os.path.exists(p):
            f = ImageFont.truetype(p, size)
            if wght:
                try: f.set_variation_by_axes([wght])
                except Exception: pass
            return f
    return ImageFont.load_default(size)
SERIF = ['Alegreya[wght].ttf', '/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf']
SERIF_I = ['Alegreya-Italic[wght].ttf', '/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf']
SANS = ['AlegreyaSans-Regular.ttf', '/usr/share/fonts/opentype/inter/Inter-Regular.otf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
SANS_B = ['AlegreyaSans-Bold.ttf', '/usr/share/fonts/opentype/inter/Inter-Bold.otf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']
MONO = ['CourierPrime-Regular.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf']
serif = lambda s, w=700: _font(SERIF, s, w)
serif_i = lambda s, w=400: _font(SERIF_I, s, w)
sans = lambda s: _font(SANS, s)
sans_b = lambda s: _font(SANS_B, s)
mono = lambda s: _font(MONO, s)

def up(t): return t.replace('i', 'İ').replace('ı', 'I').upper()

def wrap(d, text, font, width):
    lines = []
    for para in text.split('\n'):
        words, cur = para.split(), ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if d.textlength(t, font=font) <= width: cur = t
            else:
                if cur: lines.append(cur)
                cur = w
        lines.append(cur)
    return lines

def block(d, xy, text, fonts, width, max_h, fill, gap=1.38):
    """Metni sığdığı en büyük yazı boyutuyla yazar; kullanılan yüksekliği döndürür."""
    for f in fonts:
        lines = wrap(d, text, f, width); lh = int(f.size * gap)
        if len(lines) * lh <= max_h: break
    x, y = xy
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill); y += lh
    return y - xy[1]

def motif(d, y, color, h=22):
    x = 0
    while x < W + 40:
        cx = x + 20; cy = y + h // 2
        d.polygon([(cx, cy - h // 2), (cx + h // 2, cy), (cx, cy + h // 2), (cx - h // 2, cy)], outline=color, width=3)
        d.polygon([(cx, cy - 5), (cx + 5, cy), (cx, cy + 5), (cx - 5, cy)], fill=color)
        x += 48

def frame(p, n, total):
    im = Image.new('RGB', (W, H), C['paper']); d = ImageDraw.Draw(im)
    motif(d, 34, C['accent'])
    d.text((80, 96), f'BİTKİ TABANI · BT-{p["no"]:03d}', font=mono(28), fill=C['muted'])
    t = f'{n}/{total}'; d.text((W - 80 - d.textlength(t, font=mono(28)), 96), t, font=mono(28), fill=C['muted'])
    d.line([(80, H - 120), (W - 80, H - 120)], fill=C['rule'], width=2)
    d.text((80, H - 96), p['tr'], font=serif(34), fill=C['ink'])
    u = 'bitkitabani.com'; d.text((W - 80 - d.textlength(u, font=mono(28)), H - 90), u, font=mono(28), fill=C['accent'])
    return im, d

def heading(d, y, eyebrow, title, color=None):
    d.text((80, y), up(eyebrow), font=sans_b(30), fill=color or C['accent'])
    y += 52
    h = block(d, (80, y), title, [serif(76), serif(64), serif(56)], W - 160, 220, C['ink'], gap=1.12)
    return y + h + 28

def cover(p, photo, total, label):
    im = Image.new('RGB', (W, H), C['paper']); d = ImageDraw.Draw(im)
    ph_h = 900
    if photo and os.path.exists(photo):
        src = Image.open(photo).convert('RGB')
        s = max(W / src.width, ph_h / src.height); src = src.resize((int(src.width * s + 1), int(src.height * s + 1)), Image.LANCZOS)
        l = (src.width - W) // 2; t = max(0, (src.height - ph_h) // 3)
        im.paste(src.crop((l, t, l + W, t + ph_h)), (0, 0))
    else:
        d.rectangle([0, 0, W, ph_h], fill=C['sheet'])
        d.text((80, ph_h // 2 - 40), p['la'], font=serif_i(60), fill=C['muted'])
    d.rectangle([0, ph_h, W, ph_h + 10], fill=REGC.get(p['bolge'][0], C['accent']))
    lab = up(label); f = sans_b(28); tw = d.textlength(lab, font=f)
    d.rounded_rectangle([60, 56, 60 + tw + 44, 56 + 58], radius=29, fill=C['paper'])
    d.text((82, 68), lab, font=f, fill=C['accent'])
    y = ph_h + 44
    h = block(d, (80, y), p['tr'], [serif(112, 800), serif(96, 800), serif(80, 800)], W - 160, 150, C['ink'], gap=1.05)
    y += h + 18
    d.text((80, y), p['la'], font=serif_i(46), fill=C['muted']); y += 80
    x = 80
    for r in p['bolge']:
        name = R[r]; f = sans_b(28); tw = d.textlength(name, font=f)
        d.ellipse([x, y + 8, x + 22, y + 30], fill=REGC.get(r, C['accent'])); d.text((x + 32, y + 2), name, font=f, fill=C['ink']); x += tw + 70
    d.text((80, H - 74), 'Kaydır →', font=mono(30), fill=C['accent'])
    u = 'bitkitabani.com'; d.text((W - 80 - d.textlength(u, font=mono(28)), H - 72), u, font=mono(28), fill=C['muted'])
    return im

def slides(p, photo, label):
    T = 6; out = [cover(p, photo, T, label)]
    im, d = frame(p, 2, T)
    d.text((80, 200), up('Biliyor muydun?'), font=sans_b(30), fill=C['accent'])
    d.text((70, 230), '“', font=serif(200, 700), fill=C['rule'])
    block(d, (80, 430), p['ilginc'], [serif(74, 600), serif(66, 600), serif(58, 600), serif(50, 600), serif(44, 600)], W - 160, H - 430 - 170, C['ink'], gap=1.25)
    out.append(im)
    im, d = frame(p, 3, T); y = heading(d, 190, 'Geleneksel kullanım', 'Kim, nasıl kullanmış?')
    for where, txt in p['kul'][:2]:
        d.text((80, y), where, font=sans_b(40), fill=C['indigo']); y += 60
        y += block(d, (80, y), txt, [sans(46), sans(42), sans(38), sans(34), sans(30)], W - 160, 400, C['ink'], gap=1.4) + 40
    out.append(im)
    im, d = frame(p, 4, T); y = heading(d, 190, 'Bilim ne diyor?', f'Kanıt: {K[p["kanit"]]}')
    n = {'klinik': 3, 'sinirli': 2, 'geleneksel': 1}.get(p['kanit'], 1)
    for i in range(3):
        d.ellipse([80 + i * 46, y, 80 + i * 46 + 30, y + 30], fill=C['ink'] if i < n else None, outline=C['ink'], width=3)
    y += 64
    block(d, (80, y), p['bilim'], [sans(50), sans(46), sans(42), sans(38), sans(35), sans(32), sans(29)], W - 160, H - 150 - y - 40, C['ink'], gap=1.42)
    out.append(im)
    im, d = frame(p, 5, T); col = C.get(p['guv'], C['orta']); y = heading(d, 190, 'Güvenlik', G[p['guv']], col)
    hh = block(d, (122, y), p['guvNot'], [sans(50), sans(46), sans(42), sans(38), sans(35), sans(32), sans(29)], W - 202, H - 190 - y, C['ink'], gap=1.42)
    d.rectangle([80, y + 6, 92, y + hh - 14], fill=col)
    out.append(im)
    im, d = frame(p, 6, T)
    y = heading(d, 230, 'Devamı sitede', 'Kaynaklarıyla birlikte tamamı')
    d.text((80, y + 10), f'bitkitabani.com/{p["id"]}', font=serif(64, 700), fill=C['accent']); y += 120
    d.text((80, y), 'Bağlantı profilde.', font=sans(40), fill=C['muted']); y += 110
    for t in ['Kaydet: sonra okumak için', 'Paylaş: bu bitkiyi seven birine', 'Takip et: her gün yeni bir bitki']:
        d.text((80, y), '◆', font=sans(34), fill=C['ochre']); d.text((130, y - 4), t, font=sans(40), fill=C['ink']); y += 72
    y += 40
    block(d, (80, y), 'Bitki Tabanı geleneksel kullanımları kültürel bir kayıt olarak anlatır ve bilimsel bilgiyi özetler. Tıbbi tavsiye değildir; bir bitkiyi tedavi amacıyla kullanmadan önce hekimine ya da eczacına danış.', [sans(30), sans(27)], W - 160, 220, C['muted'], gap=1.4)
    if p.get('foto'): d.text((80, H - 160), 'Fotoğraf: ' + p['foto'][:70], font=sans(22), fill=C['muted'])
    out.append(im)
    return out

TAG = {'anadolu': '#anadolu', 'asya': '#asya', 'and': '#andlar', 'amazon': '#amazon', 'kamerika': '#kuzeyamerika'}
def hashtag(s):
    s = s.replace('İ', 'i').replace('I', 'ı').lower()
    return '#' + re.sub(r'[^a-zçğıöşü0-9]', '', s)
def first_sentence(t):
    m = re.match(r'(.+?[.!?])(\s|$)', t.strip()); return m.group(1) if m else t
def caption(p, label):
    k = p['kul'][0]
    lines = [f'{p["tr"]} ({p["la"]})', '', p['ilginc'], '',
             f'🌿 Gelenek: {k[1]}', '', f'🔬 Bilim: {first_sentence(p["bilim"])} (Kanıt düzeyi: {K[p["kanit"]].lower()})', '',
             f'⚠️ Güvenlik: {first_sentence(p["guvNot"])}', '',
             f'Kaynaklarıyla birlikte tamamı: bitkitabani.com/{p["id"]} (bağlantı profilde)', '',
             'Tıbbi tavsiye değildir. Bir bitkiyi tedavi için kullanmadan önce hekimine ya da eczacına danış.', '',
             ' '.join([hashtag(p['tr']), '#şifalıbitkiler', '#bitkiler', '#etnobotanik', '#doğa', '#bitkiçayı', '#halkhekimliği', '#botanik'] + [TAG[r] for r in p['bolge'] if r in TAG])]
    if label.startswith('Yeni'): lines.insert(0, '🆕 Bugün Bitki Tabanı’na eklendi.\n')
    return '\n'.join(lines)[:2150]

def schedule(data, upto):
    P = {p['id']: p for p in data['p']}
    rel = {q[0]: datetime.date.fromisoformat(q[1]) for q in data['kuyruk']}
    ok = lambda pid, d: pid in P and P[pid]['guv'] != 'yuksek' and P[pid]['yasal'] not in ('yasak', 'kisitli') and rel.get(pid, datetime.date.min) <= d
    order = IG_ORDER + [p['id'] for p in data['p'] if p['id'] not in IG_ORDER] + [q[0] for q in data['kuyruk'] if q[0] not in IG_ORDER]
    done, plan, d = set(), {}, IG_START
    while d <= upto:
        pick = next((x for x in order if x not in done and ok(x, d)), None)
        if pick is None: done = set(); pick = next((x for x in order if ok(x, d)), None)   # liste bitince başa dön
        plan[d] = pick; done.add(pick); d += datetime.timedelta(days=1)
    return plan

def main():
    data = json.load(open(os.path.join(ROOT, '.cache', 'ig_input.json'), encoding='utf-8'))
    global K, G, R
    K, G, R = data['kanit'], data['guv'], data['reg']
    day = datetime.date.fromisoformat(data['day'])
    days = [day + datetime.timedelta(days=i) for i in range(3)]
    plan = schedule(data, days[-1])
    P = {p['id']: p for p in data['p']}
    out_root = os.path.join(ROOT, 'site', 'ig'); os.makedirs(out_root, exist_ok=True)
    cards = ''
    for d in days:
        if d < IG_START: continue
        pid = plan[d]; p = P[pid]
        label = 'Yeni eklendi' if data['yeni'].get(pid) == d.isoformat() else 'Şifalı bitkiler'
        od = os.path.join(out_root, d.isoformat()); os.makedirs(od, exist_ok=True)
        ims = slides(p, os.path.join(ROOT, 'img', f'{pid}-960.jpg') if p['img'] else None, label)
        urls = []
        for i, im in enumerate(ims, 1):
            im.save(os.path.join(od, f'{i}.jpg'), 'JPEG', quality=88, optimize=True, progressive=False)
            urls.append(f'{BASE}/ig/{d.isoformat()}/{i}.jpg')
        cap = caption(p, label)
        json.dump({'date': d.isoformat(), 'id': pid, 'caption': cap, 'images': urls}, open(os.path.join(od, 'post.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        thumbs = ''.join(f'<a href="{d.isoformat()}/{i}.jpg" download><img src="{d.isoformat()}/{i}.jpg" alt="Slayt {i}" width="216" height="270" loading="lazy"></a>' for i in range(1, len(ims) + 1))
        cards += f'''<section class="post"><h2>{d.day}.{d.month:02d}.{d.year} · {html.escape(p["tr"])}</h2><p class="when">{"Bugün" if d == day else "Sonraki"} · her akşam 19:00’da kendiliğinden paylaşılır.</p><div class="strip">{thumbs}</div>
<textarea readonly rows="10">{html.escape(cap)}</textarea><button type="button" onclick="navigator.clipboard.writeText(this.previousElementSibling.value);this.textContent='Kopyalandı'">Açıklamayı kopyala</button></section>'''
        print('ig:', d, pid, label)
    page = f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow"><title>Instagram postları | Bitki Tabanı</title>
<style>body{{margin:0;padding:16px;background:#F1EADD;color:#1C2140;font-family:system-ui,sans-serif;max-width:1180px;margin:auto}}h1{{font-family:Georgia,serif}}.post{{background:#FBF6EC;border:1px solid #DCCFBA;border-radius:12px;padding:16px;margin:0 0 24px}}.when{{color:#5D5866;margin-top:0}}.strip{{display:flex;gap:8px;overflow-x:auto;padding-bottom:8px}}.strip img{{width:216px;height:auto;border-radius:6px;display:block}}textarea{{width:100%;font:inherit;margin:12px 0 8px;border:1px solid #DCCFBA;border-radius:8px;padding:8px;background:#fff;color:inherit}}button{{font:inherit;padding:8px 14px;border-radius:8px;border:1px solid #A3271B;background:#A3271B;color:#fff}}@media (prefers-color-scheme:dark){{body{{background:#15131E;color:#F0E7D8}}.post{{background:#1E1A29;border-color:#3A3247}}textarea{{background:#15131E}}}}</style></head>
<body><h1>Instagram postları</h1><p>Bugünün ve sonraki iki günün kaydırmalı postları. Görsele dokununca indirilir. Otomatik paylaşım açıkken bir şey yapmana gerek yok.</p>{cards}</body></html>'''
    open(os.path.join(out_root, 'index.html'), 'w', encoding='utf-8').write(page)

if __name__ == '__main__':
    main()
