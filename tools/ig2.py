"""Instagram slaytları, 2. sürüm: dergi düzeni, büyük yazı, her slaytta tek fikir, sohbet dili.
tools/ig.py bu modüldeki slides2() ve caption2() işlevlerini kullanır."""
import os, re
from PIL import Image, ImageDraw, ImageFilter
import ig as base
from ig_metin import M

KAN = {'klinik': 'Kanıtı güçlü', 'sinirli': 'Kanıt sınırlı', 'geleneksel': 'Yalnızca geleneksel bilgi'}
def sentences(t): return [x.strip() for x in re.split(r'(?<=[.!?])\s+', t.strip()) if x.strip()]
def auto(p):
    """Elle yazılmış metni olmayan bitki için katalog verisinden sade bir metin."""
    k = p['kul'][0]; g = sentences(p['guvNot'])
    return dict(
        kapak=(f'{p["tr"]} neye iyi gelir?' if p['guv'] == 'dusuk' else 'Şifa mı, risk mi?'),
        kisaca=[('Nereden', ', '.join(x[0] for x in p['kul'][:2])), ('Geleneksel kullanım', sentences(k[1])[0][:90]), ('Kanıt', KAN.get(p['kanit'], ''))],
        hikaye=('Bunu çok kişi bilmiyor', p['ilginc']),
        gelenek=(k[0], ' '.join(sentences(k[1])[:2])),
        bilim=(KAN.get(p['kanit'], 'Bilim ne diyor?'), ' '.join(sentences(p['bilim'])[:2])),
        dikkat=g[:3] or ['Bilinen önemli bir risk yok'], dikkat_not='',
        nasil=('Daha fazlası sitede', 'Hazırlanışı, kaynakları ve ilaç etkileşimleri bitkitabani.com’da.'),
        kaydet='Kaydet, sonra lazım olur.', soru=f'{p["tr"]} hakkında ne biliyorsun?')
def text_for(p): return M.get(p['id']) or auto(p)

W, H = 1080, 1350
CREAM = (244, 238, 227); INK = (31, 43, 36); MUTED = (98, 104, 96); LEAF = (46, 92, 64); CLAY = (176, 74, 46); LINE = (214, 204, 186)
serif, serif_i, sans, sans_b = base.serif, base.serif_i, base.sans, base.sans_b
PAD = 96

def up(t): return t.replace('i', 'İ').replace('ı', 'I').upper()

def wrap_block(d, xy, text, fonts, width, max_h, fill, gap=1.3, align='left'):
    for f in fonts:
        lines = base.wrap(d, text, f, width); lh = int(f.size * gap)
        if len(lines) * lh <= max_h: break
    x, y = xy
    for ln in lines:
        lx = x if align == 'left' else x + (width - d.textlength(ln, font=f)) / 2
        d.text((lx, y), ln, font=f, fill=fill); y += lh
    return y - xy[1]

def photo(path, w, h, blur=0):
    if not path or not os.path.exists(path): return None
    src = Image.open(path).convert('RGB')
    s = max(w / src.width, h / src.height); src = src.resize((int(src.width * s + 1), int(src.height * s + 1)), Image.LANCZOS)
    l = (src.width - w) // 2; t = max(0, (src.height - h) // 3)
    im = src.crop((l, t, l + w, t + h))
    return im.filter(ImageFilter.GaussianBlur(blur)) if blur else im

def shade(im, top=0.0, bottom=0.78):
    g = Image.new('L', (1, H))
    for y in range(H): g.putpixel((0, y), int(255 * (top + (bottom - top) * (y / H) ** 1.6)))
    im.paste(Image.new('RGB', (W, H), (12, 18, 14)), (0, 0), g.resize((W, H)))
    return im

def chrome(d, n, total, dark=False):
    c = (236, 230, 218) if dark else MUTED
    d.text((PAD, H - 92), 'bitkitabani', font=serif(34, 700), fill=c)
    dx = W - PAD - total * 22
    for i in range(total):
        r = 6 if i == n - 1 else 4
        cx = dx + i * 22; cy = H - 74
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c if i == n - 1 else None, outline=c, width=2)

def card(n, total):
    im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
    chrome(d, n, total); return im, d

def eyebrow(d, y, t, col=CLAY):
    d.text((PAD, y), up(t), font=sans_b(32), fill=col); return y + 64

def slides2(p, img_path, label):
    m = text_for(p); T = 8; out = []
    # 1. kapak: tam fotoğraf, büyük soru
    im = photo(img_path, W, H) or Image.new('RGB', (W, H), LEAF)
    im = shade(im, 0.05, 0.86); d = ImageDraw.Draw(im)
    if label.startswith('Yeni'):
        f = sans_b(28); tw = d.textlength(up('Yeni eklendi'), font=f)
        d.rounded_rectangle([PAD, 90, PAD + tw + 40, 146], radius=28, fill=CREAM); d.text((PAD + 20, 102), up('Yeni eklendi'), font=f, fill=CLAY)
    d.text((PAD, 760), up(p['tr']), font=sans_b(40), fill=(240, 226, 196))
    wrap_block(d, (PAD, 820), m['kapak'], [serif(108, 800), serif(96, 800), serif(84, 800)], W - 2 * PAD, 340, (255, 255, 255), gap=1.06)
    d.text((PAD, H - 92), 'bitkitabani', font=serif(34, 700), fill=(236, 230, 218))
    t = 'kaydır'; f = sans_b(30); tx = W - PAD - d.textlength(t, font=f) - 56
    d.text((tx, H - 92), t, font=f, fill=(236, 230, 218))
    ax, ay = W - PAD - 44, H - 74
    d.line([(ax, ay), (ax + 40, ay)], fill=(236, 230, 218), width=4); d.polygon([(ax + 40, ay - 10), (ax + 54, ay), (ax + 40, ay + 10)], fill=(236, 230, 218))
    out.append(im)
    # 2. kısaca
    im, d = card(2, T); y = eyebrow(d, 150, 'Kısaca')
    d.text((PAD, y), p['tr'], font=serif(96, 800), fill=INK); y += 112
    d.text((PAD, y), p['la'], font=serif_i(44), fill=MUTED); y += 110
    for k, v in m['kisaca']:
        d.line([(PAD, y), (W - PAD, y)], fill=LINE, width=2); y += 30
        d.text((PAD, y), up(k), font=sans_b(28), fill=LEAF); y += 46
        y += wrap_block(d, (PAD, y), v, [sans(50), sans(44), sans(40)], W - 2 * PAD, 140, INK, gap=1.25) + 24
    out.append(im)
    # 3. hikâye: bulanık fotoğraf üstünde
    im = photo(img_path, W, H, blur=18) or Image.new('RGB', (W, H), LEAF)
    im = shade(im, 0.55, 0.75); d = ImageDraw.Draw(im); chrome(d, 3, T, dark=True)
    y = eyebrow(d, 360, 'Biliyor muydun?', (240, 226, 196))
    h = wrap_block(d, (PAD, y), m['hikaye'][0], [serif(92, 800), serif(80, 800), serif(70, 800)], W - 2 * PAD, 320, (255, 255, 255), gap=1.08)
    wrap_block(d, (PAD, y + h + 40), m['hikaye'][1], [sans(48), sans(44), sans(40)], W - 2 * PAD, 420, (236, 230, 218), gap=1.38)
    out.append(im)
    # 4. gelenek, 5. bilim
    for n, key, eb in ((4, 'gelenek', 'Gelenek'), (5, 'bilim', 'Bilim ne diyor?')):
        def draw(d, y0):
            y = eyebrow(d, y0, eb, LEAF if key == 'bilim' else CLAY)
            h = wrap_block(d, (PAD, y), m[key][0], [serif(88, 800), serif(76, 800), serif(66, 800)], W - 2 * PAD, 300, INK, gap=1.1)
            return y + h + 44 + wrap_block(d, (PAD, y + h + 44), m[key][1], [sans(54), sans(50), sans(46), sans(42), sans(38)], W - 2 * PAD, 700, INK, gap=1.4) - y0
        im, d = card(n, T)
        hh = draw(ImageDraw.Draw(Image.new('RGB', (W, H))), 0)
        draw(d, max(150, (H - 120 - hh) // 2 - 20))
        out.append(im)
    # 6. dikkat
    im, d = card(6, T); y = eyebrow(d, max(150, 470 - 70 * len(m['dikkat'])), 'Dikkat', CLAY)
    d.text((PAD, y), 'Önce hekimine sor:' if p['id'] in M else 'Bilmen gerekenler:', font=serif(80, 800), fill=INK); y += 140
    for it in m['dikkat']:
        d.ellipse([PAD, y + 22, PAD + 18, y + 40], fill=CLAY)
        y += wrap_block(d, (PAD + 44, y), it, [sans(50), sans(44)], W - 2 * PAD - 44, 140, INK, gap=1.3) + 26
    if m.get('dikkat_not'):
        y += 30; d.line([(PAD, y), (W - PAD, y)], fill=LINE, width=2); y += 34
        wrap_block(d, (PAD, y), m['dikkat_not'], [sans(46), sans(42)], W - 2 * PAD, 200, LEAF, gap=1.3)
    out.append(im)
    # 7. nasıl
    im = Image.new('RGB', (W, H), LEAF); d = ImageDraw.Draw(im); chrome(d, 7, T, dark=True)
    y = eyebrow(d, 380, 'Nasıl kullanılır?', (240, 226, 196))
    h = wrap_block(d, (PAD, y), m['nasil'][0], [serif(96, 800), serif(84, 800)], W - 2 * PAD, 240, (255, 255, 255), gap=1.08)
    wrap_block(d, (PAD, y + h + 44), m['nasil'][1], [sans(54), sans(48), sans(44)], W - 2 * PAD, 520, (236, 230, 218), gap=1.4)
    out.append(im)
    # 8. kapanış
    im, d = card(8, T)
    ph = photo(img_path, 300, 300)
    if ph:
        mask = Image.new('L', (300, 300), 0); ImageDraw.Draw(mask).ellipse([0, 0, 300, 300], fill=255); im.paste(ph, ((W - 300) // 2, 170), mask)
    y = 530
    y += wrap_block(d, (PAD, y), m['kaydet'], [serif(80, 800), serif(70, 800)], W - 2 * PAD, 220, INK, gap=1.1, align='center') + 40
    y += wrap_block(d, (PAD, y), 'Her gün yeni bir bitki için takip et.', [sans(46)], W - 2 * PAD, 120, INK, align='center') + 50
    t = f'bitkitabani.com/{p["id"]}'; f = sans_b(40); d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=CLAY); y += 64
    t = 'Kaynaklar ve fazlası sitede'; f = sans(36); d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=MUTED)
    wrap_block(d, (PAD, H - 230), 'Bilgi amaçlıdır, tıbbi tavsiye değildir.' + (f' Fotoğraf: {p["foto"][:60]}' if p.get('foto') else ''), [sans(26)], W - 2 * PAD, 100, MUTED, align='center')
    out.append(im)
    return out

def caption2(p, label):
    m = text_for(p)
    first = f'{p["tr"]}: {m["kapak"][0].lower() + m["kapak"][1:]} {m.get("emoji", "🌿")}'
    lines = ([('🆕 Bugün Bitki Tabanı’na eklendi.'), ''] if label.startswith('Yeni') else []) + [
        first, '', m['bilim'][0] + '. ' + m['bilim'][1].split('. ')[0].rstrip('.') + '.', '',
        'Kaydırarak oku: nereden geliyor, bilim ne diyor, kimler dikkat etmeli.', '',
        m['soru'] + ' Yorumlara yaz 👇', '',
        f'Kaynaklarıyla tamamı: bitkitabani.com/{p["id"]} (bağlantı profilde)', '',
        ' '.join(m.get('etiket') or [base.hashtag(p['tr']), '#şifalıbitkiler', '#bitkiçayı', '#doğalyaşam', '#etnobotanik'])]
    return '\n'.join(lines)[:2150]

def alts2(p):
    """Her slayt için alternatif metin (görme engelliler ve Instagram araması için)."""
    m = text_for(p)
    return [f'{p["tr"]} ({p["la"]}) fotoğrafı. {m["kapak"]}',
            f'{p["tr"]} kısaca: ' + '; '.join(f'{a}: {b}' for a, b in m['kisaca']),
            f'{m["hikaye"][0]}. {m["hikaye"][1]}', f'Gelenek: {m["gelenek"][0]}. {m["gelenek"][1]}',
            f'Bilim ne diyor: {m["bilim"][0]}. {m["bilim"][1]}', 'Dikkat: ' + '; '.join(m['dikkat']) + '. ' + m.get('dikkat_not', ''),
            f'{m["nasil"][0]}: {m["nasil"][1]}', f'{m["kaydet"]} Her gün yeni bir bitki: bitkitabani.com/{p["id"]}']

def story(p, cover):
    """Hikâye görseli (1080×1920): bulanık arka plan üstünde kapak slaydı ve 'yeni gönderi' notu."""
    SW, SH = 1080, 1920
    bg = cover.resize((int(SH * cover.width / cover.height), SH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(30))
    l = (bg.width - SW) // 2; bg = bg.crop((l, 0, l + SW, SH))
    bg.paste(Image.new('RGB', (SW, SH), (12, 18, 14)), (0, 0), Image.new('L', (SW, SH), 110))
    card = cover.resize((864, 1080), Image.LANCZOS); bg.paste(card, ((SW - 864) // 2, 380))
    d = ImageDraw.Draw(bg)
    t = up('Yeni gönderi'); f = sans_b(40); d.text(((SW - d.textlength(t, font=f)) / 2, 270), t, font=f, fill=(240, 226, 196))
    t = 'Profilde, kaydırarak oku'; f = sans(44); d.text(((SW - d.textlength(t, font=f)) / 2, 1520), t, font=f, fill=(255, 255, 255))
    t = '@bitkitabani'; f = serif(52, 800); d.text(((SW - d.textlength(t, font=f)) / 2, 1600), t, font=f, fill=(255, 255, 255))
    return bg

def reel(ims, img_path=None, out='reel.mp4', sec=3.0):
    """Slaytlardan 9:16 sessiz kısa video (Reels). ffmpeg yoksa False döner."""
    import shutil, subprocess, tempfile
    if not shutil.which('ffmpeg'): return False
    SW, SH = 1080, 1920
    base_bg = photo(img_path, SW, SH, blur=30) or Image.new('RGB', (SW, SH), LEAF)
    base_bg.paste(Image.new('RGB', (SW, SH), (12, 18, 14)), (0, 0), Image.new('L', (SW, SH), 120))
    tmp = tempfile.mkdtemp()
    lst = []
    for i, im in enumerate(ims):
        fr = base_bg.copy(); fr.paste(im, (0, (SH - H) // 2))
        pth = os.path.join(tmp, f'{i}.png'); fr.save(pth); lst.append(pth)
    with open(os.path.join(tmp, 'l.txt'), 'w') as f:
        for i, pth in enumerate(lst): f.write(f"file '{pth}'\nduration {sec + (1 if i in (0, len(lst) - 1) else 0)}\n")
        f.write(f"file '{lst[-1]}'\n")
    r = subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', os.path.join(tmp, 'l.txt'),
                        '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest',
                        '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-c:a', 'aac', '-b:a', '64k',
                        '-movflags', '+faststart', out], capture_output=True, text=True)
    shutil.rmtree(tmp, ignore_errors=True)
    if r.returncode != 0: print('reel hatası:', r.stderr[:300]); return False
    return True
