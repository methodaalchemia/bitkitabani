"""Dükkân: telifsiz tarihî levhalardan (Köhler 1887, Thomé 1885) basılabilir poster setleri.
Her bitki için 3 oranda yüksek çözünürlüklü JPG (ISO A-serisi, 4:5, 2:3), çerçeveli tanıtım görseli,
Etsy (İngilizce) ve Shopier (Türkçe) ilan metinleri. Setler için ayrıca set tanıtım görseli ve ilan.
GitHub Actions'ta elle çalışır; çıktı 'dukkan' dalına yazılır (geçmiş tutulmaz). python3 tools/dukkan.py"""
import json, os, re, sys, io, urllib.parse, zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, 'en'))
import tanima as T
OUT = os.path.join(ROOT, 'dukkan'); F = os.path.join(HERE, 'fonts')
PAPER, INK, MUTE = (243, 238, 227), (40, 44, 38), (110, 108, 98)

SETLER = [
 ('baharat', 'Kitchen Spices', 'Mutfak Baharatları', ['zencefil', 'tarcin', 'karanfil', 'kakule', 'muskat', 'safran']),
 ('cay', 'Herbal Tea Garden', 'Bitki Çayları', ['papatya', 'lavanta', 'melisa', 'rezene', 'anason', 'meyan']),
 ('rituel', 'Sacred & Ritual Plants', 'Kutsal ve Ritüel Bitkileri', ['koka', 'kakao', 'kinin', 'hashas', 'mapacho', 'guarana']),
]
ORANLAR = [('ISO_A4-A3-A2', 3508, 4961), ('4x5_8x10-16x20', 4800, 6000), ('2x3_12x18-24x36', 4800, 7200)]

def font(n, s): return ImageFont.truetype(os.path.join(F, n), s)
def levha(taxon):
    """Aynı türün Köhler ya da Thomé levhası: (dosya adı, orijinal url, seri adı)"""
    t = taxon.lower()
    for q, ok, seri in [('intitle:"Medizinal-Pflanzen" "' + taxon + '"', lambda x: t in x and 'medizinal-pflanzen' in x, "Köhler's Medizinal-Pflanzen, 1887"),
                        (taxon + ' Thomé', lambda x: ('illustration ' + t) in x, 'Thomé, Flora von Deutschland, 1885')]:
        r = T.get('https://commons.wikimedia.org/w/api.php?format=json&action=query&list=search&srnamespace=6&srlimit=8&srsearch=' + urllib.parse.quote(q))
        for h in r.get('query', {}).get('search', []):
            if ok(h['title'].lower()):
                j = T.get('https://commons.wikimedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url|size&titles=' + urllib.parse.quote(h['title']))
                ii = list(j['query']['pages'].values())[0]['imageinfo'][0]
                return h['title'][5:], ii['url'], seri
    return None

def poster(plate, w, h, la, tr, en, seri):
    c = Image.new('RGB', (w, h), PAPER); d = ImageDraw.Draw(c); m = int(w * 0.07)
    d.rectangle([m // 2, m // 2, w - m // 2, h - m // 2], outline=(196, 186, 165), width=max(3, w // 900))
    cap = int(h * 0.15); box = (w - 2 * m, h - 2 * m - cap)
    p = plate.copy(); p.thumbnail(box, Image.LANCZOS)
    c.paste(p, ((w - p.width) // 2, m + (box[1] - p.height) // 2))
    y = h - m - cap + int(cap * 0.12)
    for txt, f, col in [(la, font('Alegreya-Italic[wght].ttf', int(w * 0.045)), INK),
                        (f'{tr}  ·  {en}', font('AlegreyaSans-Regular.ttf', int(w * 0.024)), MUTE),
                        (seri, font('AlegreyaSans-Italic.ttf', int(w * 0.015)), MUTE)]:
        tw = d.textlength(txt, font=f); d.text(((w - tw) / 2, y), txt, font=f, fill=col); y += int(f.size * 1.45)
    return c

def mockup(posters, path, size=2000):
    """Duvarda çerçeveli poster(ler): basit, ışık düşen bir tanıtım görseli."""
    W = H = size; bg = Image.new('RGB', (W, H), (226, 220, 208)); g = ImageDraw.Draw(bg)
    for y in range(H): g.line([(0, y), (W, y)], fill=tuple(int(v * (1.02 - 0.12 * y / H)) for v in (232, 226, 214)))
    n = len(posters); fw = int(W * (0.56 if n == 1 else 0.86 / n - 0.02)); gap = int(W * 0.03)
    x0 = (W - (fw * n + gap * (n - 1))) // 2
    for k, p in enumerate(posters):
        fh = int(fw * p.height / p.width); x = x0 + k * (fw + gap); y = (H - fh) // 2 - int(H * 0.02)
        sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rectangle([x + 14, y + 22, x + fw + 14, y + fh + 22], fill=120)
        bg.paste((40, 34, 28), (0, 0), sh.filter(ImageFilter.GaussianBlur(18)))
        fr = max(10, fw // 28); ImageDraw.Draw(bg).rectangle([x - fr, y - fr, x + fw + fr, y + fh + fr], fill=(52, 40, 30))
        bg.paste(p.resize((fw, fh), Image.LANCZOS), (x, y))
    bg.save(path, 'JPEG', quality=88)

def ilan(en, tr, la, fact, seri, n=1, set_en=None, set_tr=None, adlar=None):
    if n == 1:
        t_en = f'{en} Vintage Botanical Print, {la}, Antique {seri.split(",")[0]} Plate, Printable Herbal Wall Art'[:140]
        t_tr = f'{tr} ({la}) Antika Botanik Poster, İndirilebilir Duvar Sanatı'
    else:
        t_en = f'Set of {n} Vintage Botanical Prints, {set_en}, Antique Medicinal Plant Illustrations, Printable Wall Art'[:140]
        t_tr = f'{set_tr}: {n}\'lü Antika Botanik Poster Seti, İndirilebilir'
    tags = ['vintage botanical', 'botanical print', 'printable wall art', 'herbal print', 'antique plant art', 'kitchen wall art',
            'medicinal plant', 'digital download', 'botanical poster', 'herbalist gift', 'cottagecore decor', (en or set_en).lower()[:20], 'apothecary print']
    sizes = 'ISO A-series (A4, A3, A2), 4:5 (8x10, 11x14*, 16x20), 2:3 (12x18, 16x24, 24x36). High resolution 300 dpi JPG.'
    body_en = (f'{"A curated set of " + str(n) + " antique plates: " + ", ".join(adlar) + "." if n > 1 else en + " (" + la + "), from " + seri + "."}\n\n'
               + (f'Did you know? {fact}\n\n' if fact else '') +
               f'INSTANT DIGITAL DOWNLOAD. No physical item is shipped.\nSizes: {sizes}\n\n'
               'Restored from public-domain 19th-century plates, re-composed on warm paper with the Latin, Turkish and English names. '
               'Print at home, at a local print shop or online.\n\nFrom Bitki Tabanı (bitkitabani.com), a non-commercial, source-based encyclopedia of medicinal and ritual plants.')
    body_tr = (f'{"Özenle seçilmiş " + str(n) + " antika levha: " + ", ".join(adlar) + "." if n > 1 else tr + " (" + la + "), " + seri + " levhasından."}\n\n'
               'DİJİTAL ÜRÜNDÜR, kargo gönderilmez. 300 dpi JPG; A4, A3, A2, 30×40, 40×50, 50×70 cm baskıya uygun.\n'
               'Telifsiz 19. yüzyıl levhaları sıcak kâğıt zemin üzerinde Latince, Türkçe ve İngilizce adlarla yeniden düzenlendi.\n\nBitki Tabanı · bitkitabani.com')
    return {'etsy': {'title': t_en, 'tags': tags, 'description': body_en, 'price_usd': 4.5 if n == 1 else 14},
            'shopier': {'title': t_tr, 'description': body_tr, 'price_try': 120 if n == 1 else 390}}

def main():
    from refs import POWO
    D = {p['id']: p for p in json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))['P']}
    EN = {}
    for m in ('p1', 'p2', 'p3', 'p4'):
        try: EN.update(__import__(m).EN)
        except Exception as e: print('en', m, e)
    os.makedirs(OUT, exist_ok=True); rapor = []
    for sid, set_en, set_tr, ids in SETLER:
        sdir = os.path.join(OUT, sid); os.makedirs(sdir, exist_ok=True); onizleme, adlar = [], []
        for pid in ids:
            p = D[pid]; taxon = POWO.get(pid) or p['la'].split(',')[0]; en = EN.get(pid, {}).get('name', p['tr']).split(',')[0].strip().title()
            lv = levha(taxon)
            if not lv: rapor.append(f'{pid}: levha yok'); continue
            plate = Image.open(io.BytesIO(T.get(lv[1], binary=True))).convert('RGB')
            pdir = os.path.join(sdir, pid); os.makedirs(pdir, exist_ok=True)
            files = []
            for ad, w, h in ORANLAR:
                fn = os.path.join(pdir, f'{pid}_{ad}.jpg'); poster(plate, w, h, taxon, p['tr'], en, lv[2]).save(fn, 'JPEG', quality=90, dpi=(300, 300)); files.append(fn)
            onz = poster(plate, 1200, 1500, taxon, p['tr'], en, lv[2]); onizleme.append(onz)
            mockup([onz], os.path.join(pdir, f'{pid}_tanitim.jpg'))
            with zipfile.ZipFile(os.path.join(pdir, f'{pid}_indir.zip'), 'w', zipfile.ZIP_STORED) as z:
                for fn in files: z.write(fn, os.path.basename(fn))
                z.writestr('LISANS.txt', f'Kaynak levha: {lv[0]} ({lv[2]}), kamu malı (public domain).\nDüzenleme: Bitki Tabanı, bitkitabani.com. Kişisel kullanım içindir.')
            json.dump(ilan(en, p['tr'], taxon, EN.get(pid, {}).get('fact', ''), lv[2]), open(os.path.join(pdir, 'ilan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            adlar.append(en); rapor.append(f'{pid}: {lv[0]}')
        if onizleme:
            mockup(onizleme[:3], os.path.join(sdir, f'set_{sid}_tanitim_1.jpg')); mockup(onizleme[3:6] or onizleme[:3], os.path.join(sdir, f'set_{sid}_tanitim_2.jpg'))
            json.dump(ilan(None, None, None, '', '', n=len(adlar), set_en=set_en, set_tr=set_tr, adlar=adlar), open(os.path.join(sdir, 'set_ilan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(os.path.join(OUT, 'RAPOR.txt'), 'w', encoding='utf-8').write('\n'.join(rapor)); print('\n'.join(rapor))

if __name__ == '__main__':
    main()
