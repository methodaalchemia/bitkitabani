#!/usr/bin/env python3
"""EMA bitkisel monograflarını yerele indirir ve çevrimdışı okunabilir hâle getirir.

Neden var (25 Kasım 2026): her yeni kayıtta endikasyon, dozaj, kontrendikasyon ve
etkileşim için EMA'ya tek tek gidiliyordu. Bir kayıt için 3–5 ağ turu, her turun
çıktısı bağlama giriyor. Monograflar yılda bir iki kez değişiyor; yerelde durup
betikle okunurlarsa o tur da, o bağlam da gitmiyor.

  python3 tools/ema_monograf.py indir   # ~250 monografı veri/onbellek/ema/ içine indirir
  python3 tools/ema_monograf.py         # PDF'leri okuyup veri/onbellek/ema_index.json üretir
  python3 tools/ema_monograf.py ara "Valeriana officinalis"   # tek türü yazdırır

Önbellek git'e girmez: belgeler EMA'nın, depo herkese açık, her an yeniden inebilir.
"""
import json, os, re, subprocess, sys, time

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ONBELLEK = os.path.join(KOK, 'veri', 'onbellek', 'ema')
XLSX = os.path.join(KOK, 'veri', 'onbellek', 'ema-herbal.xlsx')
DIZIN = os.path.join(KOK, 'veri', 'onbellek', 'ema_index.json')
KOK_ADRES = 'https://www.ema.europa.eu'
UA = 'Mozilla/5.0 (compatible; bitkitabani/1.0; +https://bitkitabani.com)'


def getir(adres, hedef=None, deneme=4):
    """curl ile çeker. EMA 429 veriyor, aralık açarak tekrar dener."""
    for i in range(deneme):
        k = ['curl', '-sL', '-m', '120', '-A', UA, '-w', '%{http_code}']
        k += ['-o', hedef] if hedef else ['-o', '-']
        k.append(adres)
        r = subprocess.run(k, capture_output=True, text=True, errors='replace')
        kod = r.stdout[-3:]
        if kod == '200':
            return True if hedef else r.stdout[:-3]
        time.sleep(8 * (i + 1))
    return None


def satirlar():
    """xlsx'ten (latin adı, sonuç, sayfa adresi) üçlüleri — her tür bir kez."""
    import openpyxl
    w = openpyxl.load_workbook(XLSX, read_only=True)
    r = [x for x in w.active.iter_rows(values_only=True)]
    b = [i for i, x in enumerate(r) if x and x[0] == 'Latin name'][0]
    gor, out = set(), []
    for x in r[b + 1:]:
        if not x or not x[12]: continue
        if x[12] in gor: continue
        gor.add(x[12])
        out.append({'latin': x[0], 'tur': x[3], 'alan': x[4], 'sonuc': x[6], 'sayfa': x[12]})
    return out


def en_son_monograf(html):
    """Sayfadaki monograf PDF'lerinden nihai ve en yüksek revizyonlu olanı seç.

    Taslak (draft) alınmaz: taslak metin bağlayıcı değil ve nihai metinden farklı
    dozaj verebiliyor. Revizyon numarası yoksa 0 sayılır.
    """
    aday = re.findall(r'href="(/en/documents/herbal-monograph/[^"]+\.pdf)"', html)
    nihai = [a for a in aday if '/final-' in a or a.split('/')[-1].startswith('final-')]
    if not nihai: return None
    def rev(a):
        m = re.search(r'revision-(\d+)', a)
        return int(m.group(1)) if m else 0
    return sorted(nihai, key=rev)[-1]


def indir():
    os.makedirs(ONBELLEK, exist_ok=True)
    kayit = satirlar()
    yeni = atla = yok = 0
    for i, s in enumerate(kayit, 1):
        ad = s['sayfa'].rstrip('/').split('/')[-1]
        pdf = os.path.join(ONBELLEK, ad + '.pdf')
        if os.path.exists(pdf) and os.path.getsize(pdf) > 20000:
            atla += 1; continue
        html = getir(s['sayfa'])
        if not html:
            print('sayfa alınamadı:', s['sayfa']); yok += 1; continue
        yol = en_son_monograf(html)
        if not yol:
            # Monograf yerine kamuoyu açıklaması olanlar burada normaldir.
            open(os.path.join(ONBELLEK, ad + '.yok'), 'w').write(s['sonuc'] or '')
            yok += 1; continue
        if getir(KOK_ADRES + yol, pdf):
            yeni += 1
            if yeni % 10 == 0: print(f'{i}/{len(kayit)} · indirilen {yeni}')
        else:
            print('pdf alınamadı:', yol); yok += 1
        time.sleep(1.2)
    print(f'bitti: {yeni} yeni, {atla} zaten vardı, {yok} monografsız/alınamadı')


BOLUM = [
    ('endikasyon',      r'4\.1[\.\s]*Therapeutic indications?'),
    ('dozaj',           r'4\.2[\.\s]*Posology'),
    ('kontrendikasyon', r'4\.3[\.\s]*Contraindications?'),
    ('uyari',           r'4\.4[\.\s]*Special warnings'),
    ('etkilesim',       r'4\.5[\.\s]*Interactions?'),
    ('gebelik',         r'4\.6[\.\s]*Fertility, pregnancy'),
    ('surus',           r'4\.7[\.\s]*Effects on ability'),
    ('yanetki',         r'4\.8[\.\s]*Undesirable effects'),
    ('asiridoz',        r'4\.9[\.\s]*Overdose'),
]


def ayikla(metin):
    """Monografın 4.x bölümlerini kesip sözlüğe koyar."""
    yer = []
    for ad, kalip in BOLUM:
        m = re.search(kalip, metin, re.I)
        if m: yer.append((m.start(), m.end(), ad))
    yer.sort()
    out = {}
    for n, (b, s, ad) in enumerate(yer):
        son = yer[n + 1][0] if n + 1 < len(yer) else min(len(metin), s + 6000)
        p = re.sub(r'\s+', ' ', metin[s:son]).strip()
        if p: out[ad] = p[:4000]
    return out


def dizinle():
    import subprocess as sp
    kayit = {k['sayfa'].rstrip('/').split('/')[-1]: k for k in satirlar()}
    dizin = {}
    for ad, s in kayit.items():
        pdf = os.path.join(ONBELLEK, ad + '.pdf')
        if not os.path.exists(pdf):
            dizin[ad] = {**s, 'monograf': False}
            continue
        r = sp.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True, errors='replace')
        dizin[ad] = {**s, 'monograf': True, **ayikla(r.stdout)}
    json.dump(dizin, open(DIZIN, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
    v = sum(1 for d in dizin.values() if d.get('monograf'))
    dz = sum(1 for d in dizin.values() if d.get('dozaj'))
    print(f'{len(dizin)} kayıt, {v} monograf okundu, {dz} tanesinde dozaj bölümü bulundu → {DIZIN}')


def ara(q):
    d = json.load(open(DIZIN, encoding='utf-8'))
    q = q.lower()
    for ad, k in d.items():
        if q in (k.get('tur') or '').lower() or q in (k.get('latin') or '').lower():
            print('=' * 70); print(ad, '·', k.get('latin'), '·', k.get('sonuc'))
            for a in ('endikasyon', 'dozaj', 'kontrendikasyon', 'uyari', 'etkilesim', 'gebelik'):
                if k.get(a): print(f'\n[{a}] {k[a][:900]}')


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else ''
    if a == 'indir': indir()
    elif a == 'ara': ara(' '.join(sys.argv[2:]))
    else: dizinle()
