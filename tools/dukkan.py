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
    """Aynı türün Köhler ya da Thomé levhası; Commons'taki bütün kopyalar arasından en yüksek çözünürlüklüsü.
    Dönüş: (dosya adı, orijinal url, seri adı)"""
    t = taxon.lower()
    for sorgular, ok, seri in [
        (['"' + taxon + '" Medizinal-Pflanzen', '"' + taxon + '" Koehler1887', '"' + taxon + '" "Köhler\'s Medizinal-Pflanzen"'],
         lambda x: 'medizinal-pflanzen' in x or 'koehler' in x or 'köhler' in x, "Köhler's Medizinal-Pflanzen, 1887"),
        (['"' + taxon + '" Thomé', '"' + taxon + '" "Flora von Deutschland"'], lambda x: 'thom' in x or 'flora von deutschland' in x, 'Thomé, Flora von Deutschland, 1885')]:
        aday = {}
        for q in sorgular:
            url = ('https://commons.wikimedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=6&gsrlimit=20&gsrsearch=' + urllib.parse.quote(q)
                   + '&prop=imageinfo&iiprop=url|size|mime|extmetadata&iiextmetadatafilter=ObjectName|ImageDescription|Categories')
            for pg in T.get(url).get('query', {}).get('pages', {}).values():
                ii = (pg.get('imageinfo') or [{}])[0]; m = ii.get('extmetadata', {})
                if ii.get('mime') not in ('image/jpeg', 'image/png', 'image/tiff'): continue
                text = ' '.join([pg['title'], m.get('ObjectName', {}).get('value', ''), m.get('Categories', {}).get('value', ''), T.plain(m.get('ImageDescription', {}).get('value', ''))]).lower()
                if t in text and ok(text) and not re.search(r'herbari|specimen|photo|crop|detail|ausschnitt', pg['title'].lower()):
                    aday[pg['title']] = (ii.get('width', 0), ii['url'])
        if aday:
            f, (w, u) = max(aday.items(), key=lambda kv: kv[1][0])
            if f.lower().endswith(('.tif', '.tiff')): u = u.replace('/commons/', '/commons/thumb/', 1) + '/lossy-page1-3000px-' + f[5:].replace(' ', '_') + '.jpg'
            print('levha', taxon, w, 'px', f); return f[5:], u, seri
    return None

def poster(plate, w, h, la, tr, en, seri):
    c = Image.new('RGB', (w, h), PAPER); d = ImageDraw.Draw(c); m = int(w * 0.07)
    d.rectangle([m // 2, m // 2, w - m // 2, h - m // 2], outline=(196, 186, 165), width=max(3, w // 900))
    cap = int(h * 0.15); box = (w - 2 * m, h - 2 * m - cap)
    sc = min(box[0] / plate.width, box[1] / plate.height); p = plate.resize((int(plate.width * sc), int(plate.height * sc)), Image.LANCZOS)   # küçükse büyüt
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

_AYI = {m: i + 1 for i, m in enumerate(['ocak', 'şubat', 'mart', 'nisan', 'mayıs', 'haziran', 'temmuz', 'ağustos', 'eylül', 'ekim', 'kasım', 'aralık'])}
def months_of(txt):
    t = txt.lower()
    if 'yıl boyu' in t or 'toplanmamalı' in t or 'önerilmez' in t or 'sonra sökülür' in t: return set()
    ms = set()
    for a, c in re.findall(r'(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)\w*\s*[–-]\s*(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)', t):
        x, y = _AYI[a], _AYI[c]
        while True:
            ms.add(x)
            if x == y: break
            x = x % 12 + 1
    for m in re.findall(r'(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)', t): ms.add(_AYI[m])
    if 'sonbahar' in t: ms |= {9, 10, 11}
    if 'ilkbahar' in t or re.search(r'(?<!son)bahar', t): ms |= {3, 4, 5}
    if re.search(r'\byaz', t): ms |= {6, 7, 8}
    if re.search(r'\bkış', t): ms |= {12, 1, 2}
    return ms

def notion_paketi(D, EN, POWO):
    """Notion'a içe aktarılabilir 'Şifalı Bitki Defteri' (TR) ve 'Herbal Plant Journal' (EN) paketleri (Import → Markdown & CSV)."""
    import csv
    from extra import EK, KORUMA, YASAL
    data = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
    KAT, KANIT, GUV = data['KAT'], data['KANIT'], dict(data['GUV'], yuksek='Yüksek risk')
    AY = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
    ndir = os.path.join(OUT, 'notion'); os.makedirs(ndir, exist_ok=True)
    P = data['P']
    for dil in ('tr', 'en'):
        ad = 'Şifalı Bitki Defteri' if dil == 'tr' else 'Herbal Plant Journal'
        zp = os.path.join(ndir, ('Sifali-Bitki-Defteri' if dil == 'tr' else 'Herbal-Plant-Journal') + '.zip')
        with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
            buf = io.StringIO(); w = csv.writer(buf)
            if dil == 'tr':
                w.writerow(['Bitki', 'Latince', 'Aile', 'Diğer adlar', 'Kullanılan kısım', 'Kategori', 'Kanıt düzeyi', 'Güvenlik', 'Güvenlik notu', 'Hazırlama', 'Toplama mevsimi', 'Yöresel adlar', 'Geleneksel kullanım', 'Kaynaklı sayfa', 'Evde var', 'Denedim'])
                for p in P:
                    ek = EK.get(p['id'], {})
                    w.writerow([p['tr'], p['la'], p['fam'], p['diger'], p['kisim'], ', '.join(KAT[k] for k in p['kat']), KANIT[p['kanit']]['ad'], GUV[p['guv']], p['guvNot'], p['haz'],
                                ek.get('mevsim', ''), ek.get('yoresel', ''), ' | '.join(f'{a}: {b}' for a, b in p['kul']), f"https://bitkitabani.com/{p['id']}/", 'No', 'No'])
            else:
                w.writerow(['Plant', 'Latin name', 'Family', 'Part used', 'Traditional uses', 'Preparation', 'Science', 'Safety', 'Harvest season', 'Habitat', 'Fun fact', 'Source page', 'In my pantry', 'Tried'])
                for p in P:
                    e = EN.get(p['id']) or {}
                    if not e.get('name'): continue
                    w.writerow([e['name'], p['la'], p['fam'], e.get('part', ''), ' | '.join(f'{a}: {b}' for a, b in e.get('uses', [])), e.get('prep', ''), e.get('science', ''), e.get('safety', ''),
                                e.get('season', ''), e.get('habitat', ''), e.get('fact', ''), f"https://bitkitabani.com/en/{p['id']}/", 'No', 'No'])
            z.writestr(f'{ad}/' + ('Bitkiler.csv' if dil == 'tr' else 'Plants.csv'), '\ufeff' + buf.getvalue())
            buf = io.StringIO(); w = csv.writer(buf)
            w.writerow(['Tarih', 'Bitki', 'Ne yaptım (topladım, kuruttum, demledim…)', 'Nerede', 'Notlar'] if dil == 'tr' else ['Date', 'Plant', 'What I did (gathered, dried, brewed…)', 'Where', 'Notes'])
            z.writestr(f'{ad}/' + ('Kayıtlarım.csv' if dil == 'tr' else 'My log.csv'), '\ufeff' + buf.getvalue())
            if dil == 'tr':
                buf = io.StringIO(); w = csv.writer(buf); w.writerow(['Ay', 'Toplanabilecek bitkiler (kaynak: Bitki Tabanı)'])
                for i, a in enumerate(AY):
                    w.writerow([a, ', '.join(p['tr'] for p in P if p['guv'] != 'yuksek' and p['id'] not in YASAL and not p.get('yasal') and not KORUMA.get(p['id'], {}).get('rozet') and (i + 1) in months_of(EK.get(p['id'], {}).get('mevsim', '')))])
                z.writestr(f'{ad}/Toplama Takvimi.csv', '\ufeff' + buf.getvalue())
            giris = ({'tr': f"# {ad}\n\n{len(P)} şifalı ve ritüel bitki: geleneksel kullanım, bilimsel kanıt düzeyi, güvenlik ve kaynaklar.\n\n"
                      "## Nasıl kullanılır\n- **Bitkiler**: Evde olanları ve denediklerini işaretle; Kategori ve Güvenlik sütunlarına göre filtrele.\n"
                      "- **Toplama Takvimi**: Hangi ay neyin toplanabileceğini gör.\n- **Kayıtlarım**: Topladığın, kuruttuğun ve demlediğin her şeyi not et.\n\n"
                      "> Bu defter bilgi amaçlıdır, tıbbi tavsiye değildir. Hamilelik, emzirme, çocuklar ve ilaç kullananlar için her bitkinin güvenlik notuna bak; bitkisel bir ürüne başlamadan önce hekimine ya da eczacına danış.\n\n"
                      "Kaynaklar ve güncellemeler: https://bitkitabani.com"},
                     {'en': f"# {ad}\n\nMedicinal and ritual plants with traditional uses, level of scientific evidence, safety notes and sources.\n\n"
                      "## How to use\n- **Plants**: tick what is in your pantry and what you have tried; filter by safety.\n- **My log**: note what you gather, dry and brew.\n\n"
                      "> For information only, not medical advice. Check the safety notes, especially in pregnancy, breastfeeding, for children and with medication.\n\nSources and updates: https://bitkitabani.com/en/"})[0 if dil == 'tr' else 1][dil]
            z.writestr(f'{ad}.md', giris)
    print('notion paketleri hazır')

def main():
    from refs import POWO
    D = {p['id']: p for p in json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))['P']}
    EN = {}
    for m in ('p1', 'p2', 'p3', 'p4'):
        try: EN.update(__import__(m).EN)
        except Exception as e: print('en', m, e)
    import kuyruk as K
    for q in K.Q: D.setdefault(q['id'], {'id': q['id'], 'tr': q['tr'], 'la': q['la']}); POWO.setdefault(q['id'], q.get('taxon')); EN.setdefault(q['id'], q.get('en') or {})
    os.makedirs(OUT, exist_ok=True); rapor = []
    for sid, set_en, set_tr, ids in SETLER:
        sdir = os.path.join(OUT, sid); os.makedirs(sdir, exist_ok=True); onizleme, adlar = [], []
        for pid in ids:
          try:
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
          except Exception as ex: rapor.append(f'{pid}: HATA {str(ex)[:120]}')
        if onizleme:
            mockup(onizleme[:3], os.path.join(sdir, f'set_{sid}_tanitim_1.jpg')); mockup(onizleme[3:6] or onizleme[:3], os.path.join(sdir, f'set_{sid}_tanitim_2.jpg'))
            json.dump(ilan(None, None, None, '', '', n=len(adlar), set_en=set_en, set_tr=set_tr, adlar=adlar), open(os.path.join(sdir, 'set_ilan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    try: notion_paketi(D, EN, POWO)
    except Exception as ex: rapor.append('notion HATA ' + str(ex)[:150])
    open(os.path.join(OUT, 'RAPOR.txt'), 'w', encoding='utf-8').write('\n'.join(rapor)); print('\n'.join(rapor))

if __name__ == '__main__':
    import traceback
    try: main()
    except Exception:
        os.makedirs(OUT, exist_ok=True); open(os.path.join(OUT, 'HATA.txt'), 'w').write(traceback.format_exc()); print(traceback.format_exc())
