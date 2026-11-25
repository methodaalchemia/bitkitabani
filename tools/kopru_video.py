# -*- coding: utf-8 -*-
"""Köprü videosu — 1920x1080 yatay uzun video üretimi.

Zamanlama kopru_ses.py'nin ölçtüğü sürelerden gelir; bu dosya yalnız görüntü
kurar ve birleştirir. Altyazı videoya gömülmez, ayrı .srt olarak yüklenir.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 30
ACILIS, KAPANIS = 3.0, 3.5

PAPER = (241, 234, 221)
INK = (28, 33, 64)
ACCENT = (163, 39, 27)
INDIGO = (42, 58, 110)
OCHRE = (185, 128, 26)
MUTED = (93, 88, 102)

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(KOK, 'tools', 'fonts')


def f(ad, boy):
    return ImageFont.truetype(os.path.join(FONTS, ad), boy)


SERIF = 'Alegreya[wght].ttf'
SANS = 'AlegreyaSans-Regular.ttf'
SANS_B = 'AlegreyaSans-Bold.ttf'


def _gren(img, guc=5):
    import random
    g = Image.new('L', (W // 2, H // 2))
    g.putdata([random.randint(128 - guc, 128 + guc) for _ in range((W // 2) * (H // 2))])
    g = g.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.4))
    return Image.blend(img, Image.merge('RGB', (g, g, g)), 0.055)


def _sar(cizici, metin, font, en):
    satir, out = [], []
    for k in metin.split():
        d = ' '.join(satir + [k])
        if cizici.textlength(d, font=font) <= en or not satir:
            satir.append(k)
        else:
            out.append(' '.join(satir)); satir = [k]
    if satir: out.append(' '.join(satir))
    return out


def _kapla(yol, en, boy, cipa='orta', yakin=1.0):
    """Kırparak kaplar. cipa ile aynı fotoğraftan farklı kadraj alınabilir."""
    im = Image.open(yol).convert('RGB')
    o = max(en / im.width, boy / im.height) * yakin
    im = im.resize((max(en, int(im.width * o)), max(boy, int(im.height * o))), Image.LANCZOS)
    fx = {'orta': .5, 'sol': .18, 'sag': .82}.get(cipa, .5)
    fy = {'orta': .5, 'ust': .2, 'alt': .8}.get(cipa, .5)
    x = int((im.width - en) * fx); y = int((im.height - boy) * fy)
    return im.crop((x, y, x + en, y + boy))


def _beyazi_kagit(im, esik=238):
    """Taranmış levhanın beyaz zeminini kağıt rengine çevirir (kutu izi kalmasın)."""
    im = im.convert('RGB')
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            if r > esik and g > esik and b > esik:
                px[x, y] = PAPER
    return im


def _sigdir(yol, kutu_en, kutu_boy, zemin=PAPER):
    """Kırpmadan, kağıt zemine oturtur (botanik levha gibi bütün görünmesi gerekenler)."""
    im = _beyazi_kagit(Image.open(yol)).convert('RGBA')
    o = min(kutu_en / im.width, kutu_boy / im.height)
    im = im.resize((int(im.width * o), int(im.height * o)), Image.LANCZOS)
    zem = Image.new('RGBA', (W, H), zemin + (255,))
    zem.alpha_composite(im, ((W - im.width) // 2, (H - 300 - im.height) // 2 + 20))
    return zem.convert('RGB')


def _etiket(d, metin, renk=INDIGO):
    fo = f(SANS_B, 32)
    w = d.textlength(metin.upper(), font=fo)
    d.rounded_rectangle((64, 56, 64 + w + 56, 56 + 56), 28, fill=renk)
    d.text((64 + 28, 56 + 28), metin.upper(), font=fo, fill=PAPER, anchor='lm')


def _kunye(d, metin, koyu=True):
    """Künye görünmek zorunda (CC BY 4.0). Açık zeminde koyu, koyu zeminde açık."""
    if not metin: return
    d.text((W - 64, H - 30), metin, font=f(SANS, 26),
           fill=MUTED if koyu else (245, 240, 230), anchor='rs')


def sahne_gorsel(sahne, zaman_sahne, varlik):
    """Sahne için 1920x1080 taban görüntüsü üretir."""
    g = sahne['gorsel']; tip = g['tip']
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)

    if tip in ('foto', 'cizim', 'harita', 'motif'):
        if tip == 'harita':
            yol = varlik['harita-and'] if g.get('kirp') == 'and' else varlik['harita']
        elif tip == 'motif':
            yol = varlik['motif']
        else:
            yol = os.path.join(KOK, g['yol'])
        if tip == 'cizim':
            img = _sigdir(yol, W - 820, H - 268); d = ImageDraw.Draw(img)
        elif tip in ('motif', 'harita'):
            # kağıt zemin üstünde ortalanmış, kırpılmadan
            im = Image.open(yol).convert('RGBA')
            o = min((W - 320) / im.width, (H - 340) / im.height)
            im = im.resize((int(im.width * o), int(im.height * o)), Image.LANCZOS)
            zem = Image.new('RGBA', (W, H), PAPER + (255,))
            zem.alpha_composite(im, ((W - im.width) // 2, (H - im.height) // 2 - 40))
            img = zem.convert('RGB'); d = ImageDraw.Draw(img)
        else:
            img = _kapla(yol, W, H, g.get('kirp', 'orta'), g.get('yakin', 1.0)); d = ImageDraw.Draw(img)
            # alt bant
            bant = Image.new('RGBA', (W, 300), PAPER + (238,))
            img.paste(Image.alpha_composite(
                img.crop((0, H - 300, W, H)).convert('RGBA'), bant).convert('RGB'), (0, H - 300))

    elif tip == 'kutular':
        for i, k in enumerate(g['kutular']):
            y = 300 + i * 190
            d.rounded_rectangle((200, y, W - 200, y + 150), 18, fill=(255, 255, 255), outline=ACCENT, width=4)
            d.text((248, y + 75), k, font=f(SANS_B, 52), fill=INK, anchor='lm')

    elif tip == 'kaynaklar':
        fo, fn = f(SANS_B, 40), f(SANS, 33)
        d.text((160, 230), 'KAYNAKLAR', font=fo, fill=ACCENT)
        y = 310
        for i, k in enumerate(varlik['kaynaklar'], 1):
            d.text((160, y), f'{i}.', font=f(SANS_B, 33), fill=INDIGO)
            for s in _sar(d, k, fn, W - 460):
                d.text((215, y), s, font=fn, fill=INK); y += 44
            y += 22

    # üst etiket
    _etiket(d, sahne['bolum'])

    # ekrandaki yazı
    yazi = sahne.get('yazi') or []
    if yazi:
        if tip == 'foto':
            y = H - 300 + 56
            for i, s in enumerate(yazi):
                fo = f(SANS_B, 66) if i == 0 else f(SANS, 50)
                d.text((100, y), s, font=fo, fill=INK if i == 0 else MUTED)
                y += 84 if i == 0 else 64
        else:
            y = H - 190
            for i, s in enumerate(yazi):
                fo = f(SANS_B, 58) if i == 0 else f(SANS, 46)
                d.text((W // 2, y), s, font=fo, fill=INK if i == 0 else MUTED, anchor='mm')
                y += 72

    # uyarı kutusu
    if sahne.get('uyari'):
        fo = f(SANS_B, 50)
        w = d.textlength(sahne['uyari'], font=fo)
        x0 = (W - w - 80) // 2
        d.rounded_rectangle((x0, 150, x0 + w + 80, 150 + 96), 14, fill=ACCENT)
        d.text((x0 + 40, 150 + 48), sahne['uyari'], font=fo, fill=PAPER, anchor='lm')

    _kunye(d, sahne.get('kunye'), koyu=(tip != 'foto') or True)
    return _gren(img)


def kart(ust, alt, dip=None):
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)
    logo = os.path.join(KOK, 'assets', 'logo-512.png')
    if os.path.exists(logo):
        lg = Image.open(logo).convert('RGBA'); lg.thumbnail((190, 190), Image.LANCZOS)
        img.paste(lg, ((W - lg.width) // 2, 250), lg)
    d.text((W // 2, 505), ust, font=f(SERIF, 96), fill=INK, anchor='mm')
    d.text((W // 2, 600), alt, font=f(SANS, 50), fill=ACCENT, anchor='mm')
    if dip:
        for i, s in enumerate(dip):
            d.text((W // 2, 730 + i * 52), s, font=f(SANS, 36), fill=MUTED, anchor='mm')
    return _gren(img)


def parca(png, sure, hedef, zoom=True):
    vf = (f"zoompan=z='min(zoom+0.00035,1.07)':d=1:x='iw/2-(iw/zoom/2)':"
          f"y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}" if zoom else f"fps={FPS}")
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', str(FPS),
                    '-i', png, '-t', f'{sure:.3f}',
                    '-vf', vf + ',format=yuv420p', '-c:v', 'libx264', '-crf', '19',
                    '-preset', 'medium', '-r', str(FPS), hedef], check=True)
    return hedef


def main(slug='sedef'):
    cik = os.path.join(KOK, 'kopru-video', slug)
    sen = json.load(open(os.path.join(KOK, 'tools/kopru_senaryo', slug + '.json'), encoding='utf-8'))
    zam = json.load(open(os.path.join(cik, 'zaman.json'), encoding='utf-8'))
    kare = os.path.join(cik, 'kare'); os.makedirs(kare, exist_ok=True)
    varlik = {'harita': os.path.join(cik, 'yakala', 'harita.png'),
              'harita-and': os.path.join(cik, 'yakala', 'harita-and.png'),
              'motif': os.path.join(cik, 'yakala', 'motif.png'),
              'kaynaklar': sen['kaynaklar']}

    parcalar = []
    # açılış
    p = os.path.join(kare, 'acilis.png')
    kart('Bitki Tabanı', 'Şifalı ve ritüel bitkiler',
         ['Kültür köprüsü 2', sen['kayit']]).save(p)
    parcalar.append(parca(p, ACILIS, os.path.join(kare, 'acilis.mp4'), zoom=False))

    for s in zam['sahneler']:
        sahne = sen['sahneler'][s['no']]
        png = os.path.join(kare, f"s{s['no']:02d}.png")
        sahne_gorsel(sahne, s, varlik).save(png)
        z = sahne['gorsel']['tip'] == 'foto'
        parcalar.append(parca(png, s['sure'], os.path.join(kare, f"s{s['no']:02d}.mp4"), zoom=z))

    # kapanış
    p = os.path.join(kare, 'kapanis.png')
    kart('Bitki Tabanı', 'bitkitabani.com',
         ['250+ şifalı ve ritüel bitki', 'Bilgi amaçlıdır, tedavi önerisi değildir.']).save(p)
    parcalar.append(parca(p, KAPANIS, os.path.join(kare, 'kapanis.mp4'), zoom=False))

    # ses: başa ve sona sessizlik
    ses = os.path.join(cik, f'{slug}.mp3')
    ses2 = os.path.join(cik, f'{slug}.tam.mp3')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', ses, '-af',
                    f'adelay={int(ACILIS*1000)}|{int(ACILIS*1000)},'
                    f'apad=pad_dur={KAPANIS}', '-c:a', 'libmp3lame', '-b:a', '160k', ses2], check=True)

    liste = os.path.join(kare, 'liste.txt')
    with open(liste, 'w') as fh:
        for x in parcalar: fh.write(f"file '{x}'\n")
    sessiz = os.path.join(cik, '_sessiz.mp4')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', liste,
                    '-c', 'copy', sessiz], check=True)
    hedef = os.path.join(cik, f'{slug}-1080p.mp4')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', sessiz, '-i', ses2,
                    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k',
                    '-movflags', '+faststart', hedef], check=True)

    # srt'yi açılış kadar kaydır
    kay = os.path.join(cik, f'{slug}.tr.srt')
    import re
    def ts(m):
        h, mi, s, ms = int(m[1]), int(m[2]), int(m[3]), int(m[4])
        t = h * 3600 + mi * 60 + s + ms / 1000 + ACILIS
        return f'{int(t//3600):02d}:{int(t%3600//60):02d}:{int(t%60):02d},{int(round(t%1*1000)):03d}'
    met = open(kay, encoding='utf-8').read()
    met = re.sub(r'(\d{2}):(\d{2}):(\d{2}),(\d{3})', lambda m: ts(m), met)
    open(os.path.join(cik, f'{slug}.tr.kaydirilmis.srt'), 'w', encoding='utf-8').write(met)
    print('video:', hedef)
    return hedef


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'sedef')
