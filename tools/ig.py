"""Instagram kaydırmalı postları: her gün bir bitki, 6 slayt (1080×1350 JPEG) ve açıklama metni.

build.py'den sonra çalışır: .cache/ig_input.json dosyasını okur, sıradaki 14 postu (paylaşılmış post sayısından başlayarak)
site/ig/p/<n>/ altına yazar (1.jpg … 6.jpg, post.json) ve site/ig/index.html önizleme sayfasını üretir.
Paylaşımı worker.js yapar: açılış günü 12 post yarım saat arayla, sonra her akşam 19:00'da bir post (IG_TOKEN gerekir).

Sıra: Türkiye’de en çok arandığını tahmin ettiğimiz bitkilerden başlar (IG_ORDER), sonra kataloğun geri kalanı.
Yüksek riskli ve Türkiye’de yasak/kısıtlı bitkiler Instagram’a konmaz. Kuyruktaki bitkiler yayın gününden önce paylaşılmaz.
"""
import json, os, re, sys, datetime, textwrap, html
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://bitkitabani.com'
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
    d.text((80, H - 74), 'Kaydır', font=mono(30), fill=C['accent'])
    ax = 80 + d.textlength('Kaydır', font=mono(30)) + 14; ay = H - 56
    d.line([(ax, ay), (ax + 34, ay)], fill=C['accent'], width=3); d.polygon([(ax + 34, ay - 8), (ax + 46, ay), (ax + 34, ay + 8)], fill=C['accent'])
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

LAUNCH = 12                               # açılışta aynı gün paylaşılan post sayısı (4 sıra)
EARLIEST = datetime.date(2026, 10, 21)    # açılışın en erken günü; kuyruktaki bitkiler buna göre yerleştirilir

def sequence(data):
    """Post sırası: n. post hangi bitki? Sabit ve tekrar üretilebilir.
    Kuyruktaki bir bitki, açılış en erken gün yapılsa bile yayın gününden önce sıraya gelmeyecek kadar geride durur."""
    P = {p['id']: p for p in data['p']}
    rel = {q[0]: datetime.date.fromisoformat(q[1]) for q in data['kuyruk']}
    allowed = lambda pid: pid in P and P[pid]['guv'] != 'yuksek' and P[pid]['yasal'] not in ('yasak', 'kisitli')
    order = IG_ORDER + [p['id'] for p in data['p'] if p['id'] not in IG_ORDER] + [q[0] for q in data['kuyruk'] if q[0] not in IG_ORDER]
    order = [x for x in dict.fromkeys(order) if allowed(x) or (x in rel and x not in P)]
    min_i = lambda x: (LAUNCH - 1 + max(0, (rel[x] - EARLIEST).days)) if x in rel else 0
    seq, pending, i = [], list(order), 0
    while pending:
        pick = next((x for x in pending if min_i(x) <= i), None) or pending[0]
        seq.append(pick); pending.remove(pick); i += 1
    # İlk iki post (zencefil, zerdeçal) eski stilde çıktı; açılışın sonunda (13. ve 14. sıra) yeni stille yeniden paylaşılır.
    return seq[:LAUNCH] + REPOST + seq[LAUNCH:]

REPOST = ['zencefil', 'zerdecal']

def posted_count():
    """Kaç post paylaşıldığını sitenin kendisinden öğren (GitHub Actions’ta çalışır).
    Öğrenilemezse None döner ve hiçbir şey üretilmez; yanlış sıradan post üretmekten iyidir."""
    if os.environ.get('IG_N'): return int(os.environ['IG_N'])   # yerelde deneme için
    try:
        import urllib.request
        with urllib.request.urlopen(urllib.request.Request(BASE + '/api/ig-durum', headers={'User-Agent': 'BitkiTabani-build'}), timeout=20) as r:
            return int(json.loads(r.read()).get('sayi') or 0)
    except Exception as e:
        print('ig: paylaşım durumu alınamadı, postlar üretilmedi:', e); return None

PAGE_CSS = 'body{margin:0;padding:16px;background:#F1EADD;color:#1C2140;font-family:system-ui,sans-serif;max-width:1180px;margin:auto}h1{font-family:Georgia,serif}.post{background:#FBF6EC;border:1px solid #DCCFBA;border-radius:12px;padding:16px;margin:0 0 24px}.when{color:#5D5866;margin-top:0}.strip{display:flex;gap:8px;overflow-x:auto;padding-bottom:8px}.strip img{width:216px;height:auto;border-radius:6px;display:block}textarea{width:100%;font:inherit;margin:12px 0 8px;border:1px solid #DCCFBA;border-radius:8px;padding:8px;background:#fff;color:inherit}button{font:inherit;padding:8px 14px;border-radius:8px;border:1px solid #A3271B;background:#A3271B;color:#fff}@media (prefers-color-scheme:dark){body{background:#15131E;color:#F0E7D8}.post{background:#1E1A29;border-color:#3A3247}textarea{background:#15131E}}'

PAUSED = False   # True yapılırsa post dosyası üretilmez ve worker paylaşamaz

def threads_plan(data, day, days=4):
    """Threads için günde iki ek metin: sabah 'Biliyor muydunuz?', öğleden sonra rehber/tarif/karşılaştırma."""
    sys.path.insert(0, ROOT)
    from rehber import KONULAR
    from tarif import TARIFLER
    from karsilastirma import KARS
    P = {p['id']: p for p in data['p']}
    img = lambda i: f'https://bitkitabani.com/img/{i}-960.jpg' if i in P and P[i]['img'] else None
    pool = sorted([p for p in data['p'] if p['guv'] != 'yuksek' and not p['yasal'] and p['img'] and len(p['ilginc']) < 330], key=lambda p: p['no'])
    extra = []
    for k in KONULAR:
        ids = [x for x, _ in k['bitkiler'] if x in P]
        if len(ids) >= 2: extra.append(dict(text=f"{k['baslik']}\n\n{k['ozet']}\n\nRehberin tamamı: bitkitabani.com/rehber/{k['slug']}/", image=img(ids[0])))
    for t in TARIFLER:
        if t['bitki'] in P: extra.append(dict(text=f"{t['ad']} nasıl yapılır? ☕\n\n{t['kisa']}\n\nÖlçüler, demleme süresi ve kimlerin dikkat etmesi gerektiği: bitkitabani.com/tarif/{t['slug']}/", image=img(t['bitki'])))
    for c in KARS:
        if c['a'] in P and c['b'] in P: extra.append(dict(text=f"{c['baslik']}\n\n{c['sonuc']}\n\nKarşılaştırmanın tamamı: bitkitabani.com/karsilastirma/{c['a']}-ve-{c['b']}/", image=img(c['a'])))
    # rehber, tarif ve karşılaştırmalar karışık sırayla gelsin
    extra = [x for i, x in sorted(enumerate(extra), key=lambda t: (t[0] * 7) % max(1, len(extra)))]
    out = {}
    for d in range(days):
        dd = day + datetime.timedelta(days=d); k = dd.toordinal()
        p = pool[(k * 37) % len(pool)]
        fact = f"Biliyor muydunuz? 🌿\n\n{p['ilginc']}\n\n{p['tr']} ({p['la']}) hakkında daha fazlası: bitkitabani.com/{p['id']}/"
        out[dd.isoformat()] = {'sabah': dict(text=fact[:495], image=img(p['id'])), 'ogle': dict(text=extra[k % len(extra)]['text'][:495], image=extra[k % len(extra)]['image'])}
    return out

AYDA = ['Ocak’ta', 'Şubat’ta', 'Mart’ta', 'Nisan’da', 'Mayıs’ta', 'Haziran’da', 'Temmuz’da', 'Ağustos’ta', 'Eylül’de', 'Ekim’de', 'Kasım’da', 'Aralık’ta']
def aylik(data, day, out_root):
    """Ayın ilk günü Instagram ve Threads için 'Bu ay doğada' postu (toplama takvimine yönlendirir)."""
    m = day.month; ids = data.get('takvim', {}).get(str(m)) or data.get('takvim', {}).get(m) or []
    P = {p['id']: p for p in data['p']}
    ps = [P[i] for i in ids if i in P][:10]
    if len(ps) < 3: return
    im = Image.new('RGB', (W, H), C['paper']); d = ImageDraw.Draw(im)
    motif(d, 34, C['accent'])
    d.text((80, 96), 'BİTKİ TABANI · TOPLAMA TAKVİMİ', font=mono(28), fill=C['muted'])
    y = heading(d, 170, 'Bu ay doğada', f'{AYDA[m-1]} hangi şifalı bitkiler toplanır?')
    d.text((80, y), 'Anadolu’da bu ay toplama mevsimi olan bitkiler:', font=sans(36), fill=C['muted']); y += 80
    col = (W - 160) // 2
    for i, p in enumerate(ps):
        x = 80 + (i % 2) * col; yy = y + (i // 2) * 112
        d.text((x, yy), p['tr'], font=serif(44), fill=C['ink'])
        d.text((x, yy + 50), p['la'][:26], font=serif_i(28), fill=C['muted'])
    d.line([(80, H - 120), (W - 80, H - 120)], fill=C['rule'], width=2)
    d.text((80, H - 96), 'Ay ay bütün takvim', font=serif(34), fill=C['ink'])
    u = 'bitkitabani.com/toplama-takvimi'; d.text((W - 80 - d.textlength(u, font=mono(28)), H - 90), u, font=mono(28), fill=C['accent'])
    os.makedirs(os.path.join(out_root, 'aylik'), exist_ok=True)
    key = day.strftime('%Y-%m')
    im.save(os.path.join(out_root, 'aylik', key + '.jpg'), quality=90)
    names = ', '.join(p['tr'] for p in ps)
    cap = (f'{AYDA[m-1]} doğada neler var? 🌿\n\nAnadolu’da bu ay toplama mevsimi olan şifalı bitkiler: {names}.\n\n'
           'Toplarken yalnızca kesin tanıdığınız bitkileri, yol kenarından ve ilaçlanmış alanlardan uzakta toplayın; bitkinin tamamını değil, bir kısmını alın ki yeniden büyüyebilsin.\n\n'
           'Bu ay siz hangisini topluyorsunuz? Yorumlarda buluşalım. 👇\n\nAy ay bütün takvim: bitkitabani.com/toplama-takvimi (bağlantı profilde)\n\n'
           '#şifalıbitkiler #toplamatakvimi #doğa #etnobotanik #bitkiçayı')
    th = f'{AYDA[m-1]} doğada neler var? 🌿\n\nAnadolu’da bu ay toplama mevsimi olan şifalı bitkiler: {names}.\n\nAy ay bütün takvim: bitkitabani.com/toplama-takvimi/'
    json.dump({'ay': key, 'image': f'{BASE}/ig/aylik/{key}.jpg', 'caption': cap, 'threads': th[:495],
               'alt': f'{AYDA[m-1]} toplanan şifalı bitkilerin listesi: {names}.'}, open(os.path.join(out_root, 'aylik.json'), 'w', encoding='utf-8'), ensure_ascii=False)

def ek_postlar(data, day, out_root, days=7):
    """Haftalık ek postlar (Instagram + Threads, öğlen): Pazartesi 'Doğru mu, efsane mi?', Çarşamba 'Bunu karıştırmayın', Cuma 'Bu hangi bitki?'."""
    import ig2
    P = {p['id']: p for p in data['p']}
    ok = lambda p: p['img'] and p['guv'] != 'yuksek' and not p['yasal']
    claims = [(pid, c) for pid in sorted(data.get('derin', {})) if pid in P and ok(P[pid]) for c in data['derin'][pid]]
    kar = [(pid, t) for pid, t in sorted(data.get('karisma', {}).items()) if pid in P and ok(P[pid]) and re.search(r'karıştırıl|karıştırma|ile karış|sanıl|diye satıl', t) and not re.search(r'zor karış|karışmaz|karıştırılmaz', t)]
    pop = {x: i for i, x in enumerate(IG_ORDER)}
    kar.sort(key=lambda x: pop.get(x[0], 999))
    quiz = [p for p in sorted(data['p'], key=lambda p: (pop.get(p['id'], 999), p['no'])) if ok(p)]
    imgp = lambda pid: os.path.join(ROOT, 'img', f'{pid}-960.jpg')
    def photo_slide(pid, eyebrow, title, sub=None):
        im = ig2.photo(imgp(pid), W, H) or Image.new('RGB', (W, H), C['ink'])
        im = ig2.shade(im, 0.08, 0.88); d = ImageDraw.Draw(im)
        d.text((ig2.PAD, 700), up(eyebrow), font=sans_b(38), fill=(240, 226, 196))
        y = 760 + ig2.wrap_block(d, (ig2.PAD, 760), title, [serif(96, 800), serif(84, 800), serif(72, 800), serif(62, 800)], W - 2 * ig2.PAD, 420, (255, 255, 255), gap=1.06)
        if sub: ig2.wrap_block(d, (ig2.PAD, min(y + 24, H - 250)), sub, [sans(46), sans(40), sans(36)], W - 2 * ig2.PAD, 160, (236, 230, 218))
        d.text((ig2.PAD, H - 92), 'bitkitabani', font=serif(34, 700), fill=(236, 230, 218))
        return im
    def paper_slide(p, eyebrow, title, body, n, total):
        im, d = frame(p, n, total)
        y = heading(d, 190, eyebrow, title)
        block(d, (80, y + 20), body, [sans(62), sans(56), sans(50), sans(44), sans(38)], W - 160, H - y - 230, C['ink'], gap=1.34)
        return im
    def cta_slide(p, n, total):
        return paper_slide(p, 'Devamı sitede', f'{p["tr"]} hakkında bilmeniz gerekenler', f'Bilimin söyledikleri, kimlerin dikkat etmesi gerektiği, ilaç etkileşimleri ve kaynaklar: bitkitabani.com/{p["id"]}\n\nKaydedin, lazım olunca bulun. 🔖', n, total)
    out = {}
    for dd in (day + datetime.timedelta(days=i) for i in range(days)):
        wd, wk = dd.weekday(), dd.isocalendar()[1] + dd.year * 53
        if wd == 0 and claims:
            pid, (iddia, k, note) = claims[(wk * 7) % len(claims)]; p = P[pid]; tur = 'efsane'
            verdict = data['kanad'].get(k, k)
            ims = [photo_slide(pid, f'{p["tr"]} · Doğru mu, efsane mi?', f'“{iddia}”', 'Sizce doğru mu? Kaydırın. 👉'),
                   paper_slide(p, 'Bilim ne diyor?', verdict, f'İddia: “{iddia}”\n\n{note}', 2, 3), cta_slide(p, 3, 3)]
            cap = (f'“{p["tr"]}: {iddia[0].lower() + iddia[1:]}.” Doğru mu, efsane mi? 🤔\n\nBilimin cevabı: {verdict.lower()}. {note}\n\n'
                   f'Bu iddiayı daha önce duymuş muydunuz? Yorumlarda buluşalım. 👇\n\nKaynaklarıyla birlikte tamamı: bitkitabani.com/{pid} (bağlantı profilde)\n\nBilgilendirme amaçlıdır; tıbbi tavsiye yerine geçmez.\n\n#doğrumuefsanemi #şifalıbitkiler #{re.sub(r"[^a-zçğıöşü]", "", p["tr"].lower())} #bilim')
        elif wd == 2 and kar:
            pid, t = kar[wk % min(len(kar), 40)]; p = P[pid]; tur = 'karisma'
            ims = [photo_slide(pid, 'Bunu karıştırmayın', p['tr'], f'{p["la"]} · Nasıl ayırt edilir? Kaydırın. 👉'),
                   paper_slide(p, 'Karıştırma riski', f'{p["tr"]} nasıl tanınır?', t, 2, 3), cta_slide(p, 3, 3)]
            cap = (f'{p["tr"]}: bunu karıştırmayın! ⚠️\n\n{t}\n\nToplarken ya da satın alırken Latince adına ({p["la"]}) bakmak en güvenli yoldur.\n\n'
                   f'Siz hiç karıştırdınız mı? Yorumlarda buluşalım. 👇\n\nTamamı: bitkitabani.com/{pid} (bağlantı profilde)\n\n#karıştırmayın #şifalıbitkiler #{re.sub(r"[^a-zçğıöşü]", "", p["tr"].lower())} #doğa')
        elif wd == 4 and quiz:
            p = quiz[(wk * 3) % min(len(quiz), 60)]; pid = p['id']; tur = 'bilmece'
            hint = f'İpucu: {p["fam"]} familyasından; kullanılan kısmı {p.get("kisim", "").lower() or "bilinmiyor"}.' if p.get('kisim') else f'İpucu: {p["fam"]} familyasından.'
            ims = [photo_slide(pid, 'Bu hangi bitki?', 'Bu hangi bitki?', hint + ' Tahmininizi yorumlara yazın, sonra kaydırın. 👉'),
                   paper_slide(p, 'Cevap', p['tr'], f'{p["la"]}\n\n{p["ilginc"]}', 2, 3), cta_slide(p, 3, 3)]
            cap = (f'Bu hangi bitki? 🌿\n\n{hint}\n\nÖnce tahmininizi yorumlara yazın, cevap ikinci slaytta. 👇\n\n'
                   f'Her gün yeni bir bilmece: bitkitabani.com/oyun (bağlantı profilde)\n\n#buhangibitki #bilmece #şifalıbitkiler #doğa')
        else:
            continue
        key = dd.isoformat(); od = os.path.join(out_root, 'ek', key); os.makedirs(od, exist_ok=True)
        urls = []
        for i, im in enumerate(ims, 1):
            im.convert('RGB').save(os.path.join(od, f'{i}.jpg'), 'JPEG', quality=84, optimize=True); urls.append(f'{BASE}/ig/ek/{key}/{i}.jpg')
        th = cap.split('\n\n#')[0].replace(' (bağlantı profilde)', '/')
        out[key] = {'tur': tur, 'id': pid, 'images': urls, 'caption': cap, 'threads': th[:495], 'alts': [f'{p["tr"]} ({p["la"]}) fotoğrafı.', '', '']}
    json.dump(out, open(os.path.join(out_root, 'ek.json'), 'w', encoding='utf-8'), ensure_ascii=False)

def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    global ig2
    import ig2
    data = json.load(open(os.path.join(ROOT, '.cache', 'ig_input.json'), encoding='utf-8'))
    global K, G, R
    K, G, R = data['kanit'], data['guv'], data['reg']
    day = datetime.date.fromisoformat(data['day'])
    P = {p['id']: p for p in data['p']}
    seq = sequence(data)
    n0 = posted_count()
    import shutil
    old = os.path.join(ROOT, 'site', 'ig')            # eski yer; dosyalar artık igmedia dalında
    if os.path.isdir(old): shutil.rmtree(old)
    if n0 is None: return
    out_root = os.path.join(ROOT, 'igout')
    if os.path.isdir(out_root): shutil.rmtree(out_root)
    os.makedirs(out_root)
    json.dump({'n': n0, 'day': day.isoformat()}, open(os.path.join(out_root, 'state.json'), 'w'))
    try: json.dump(threads_plan(data, day), open(os.path.join(out_root, 'threads.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    except Exception as ex: print('threads planı yazılamadı:', ex)
    try: ek_postlar(data, day, out_root)
    except Exception as ex: print('ek postlar yazılamadı:', ex)
    try: aylik(data, day, out_root)
    except Exception as ex: print('aylık post yazılamadı:', ex)
    cards = []
    if PAUSED:
        open(os.path.join(out_root, 'index.html'), 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><p>Instagram paylaşımı şu an durduruldu.</p>')
        print('ig: durduruldu'); return
    for n in range(max(0, n0 - 1), n0 + (LAUNCH + 4 if n0 < LAUNCH + len(REPOST) else 3)):   # bir önceki de dursun (telafi gerekirse)
        pid = seq[n % len(seq)]                  # liste bitince başa döner
        if pid not in P:
            print('ig: henüz yayında değil, atlandı:', n, pid); continue
        p = P[pid]
        yd = data['yeni'].get(pid)
        label = 'Yeni eklendi' if yd and (day - datetime.date.fromisoformat(yd)).days < 7 else 'Şifalı bitkiler'
        od = os.path.join(out_root, 'p', str(n)); os.makedirs(od, exist_ok=True)
        ims = ig2.slides2(p, os.path.join(ROOT, 'img', f'{pid}-960.jpg') if p['img'] else None, label)
        urls = []
        for i, im in enumerate(ims, 1):
            im.save(os.path.join(od, f'{i}.jpg'), 'JPEG', quality=82, optimize=True, progressive=False)
            urls.append(f'{BASE}/ig/p/{n}/{i}.jpg')
        cap = ig2.caption2(p, label)
        extra = {}
        if n >= LAUNCH + len(REPOST):                     # günlük postlarda hikâye ve deneme Reels
            ig2.story(p, ims[0]).save(os.path.join(od, 'story.jpg'), 'JPEG', quality=85)
            extra['story'] = f'{BASE}/ig/p/{n}/story.jpg'
            if ig2.reel(ims, img_path=os.path.join(ROOT, 'img', f'{pid}-960.jpg') if p['img'] else None, out=os.path.join(od, 'reel.mp4'), p=p):
                extra['reel'] = f'{BASE}/ig/p/{n}/reel.mp4'
        json.dump({'n': n, 'id': pid, 'caption': cap, 'images': urls, 'alts': ig2.alts2(p), **extra}, open(os.path.join(od, 'post.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        thumbs = ''.join(f'<a href="p/{n}/{i}.jpg" download><img src="p/{n}/{i}.jpg" alt="Slayt {i}" width="216" height="270" loading="lazy"></a>' for i in range(1, len(ims) + 1))
        when = f'Açılış postu {n - 1}/{LAUNCH}' if 2 <= n < LAUNCH + len(REPOST) else ('Sıradaki' if n == n0 else 'Sonra')
        cards.append(f'<section class="post"><h2>{n + 1}. post: {html.escape(p["tr"])}</h2><p class="when">{when}</p><div class="strip">{thumbs}</div>'
                     f'<textarea readonly rows="10">{html.escape(cap)}</textarea>'
                     '<button type="button" onclick="navigator.clipboard.writeText(this.previousElementSibling.value);this.textContent=\'Kopyalandı\'">Açıklamayı kopyala</button></section>')
        print('ig:', n, pid, label)
    intro = (f'Açılışta {LAUNCH} post yarım saat arayla paylaşılır (profilde 4 sıra); sonra her akşam 19:00’da bir post.' if n0 < LAUNCH + len(REPOST)
             else f'Şimdiye kadar {n0} post paylaşıldı. Her akşam 19:00’da sıradaki paylaşılır.')
    page = ('<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="robots" content="noindex, nofollow"><title>Instagram postları | Bitki Tabanı</title><style>' + PAGE_CSS + '</style></head>'
            f'<body><h1>Instagram postları</h1><p>{intro} Görsele dokununca indirilir.</p>' + ''.join(cards) + '</body></html>')
    open(os.path.join(out_root, 'index.html'), 'w', encoding='utf-8').write(page)

if __name__ == '__main__':
    main()
