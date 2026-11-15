#!/usr/bin/env python3
"""EMA bitkisel monograflarından kanıt düzeyi ve güvenlik bölümlerini çıkarır.

Monografın kendisi, sitenin dört katmanından ikisini doğrudan veriyor:

- **Kanıt düzeyi.** EMA monografı endikasyonu iki başlıktan birine
  koyuyor: *well-established use* (iyi bilinen kullanım — klinik kanıta
  dayanır) ya da *traditional use* (geleneksel kullanım — yalnızca otuz
  yıllık kullanım geçmişine dayanır, klinik kanıt aranmaz). Bu ayrım
  sitenin "klinik / sınırlı / geleneksel" ölçeğinin karşılığı ve
  yorumla değil kaynakla belirleniyor.
- **Güvenlik.** Kontrendikasyon, etkileşim, gebelik-emzirme ve istenmeyen
  etki bölümleri monografta ayrı ayrı yazılı.

Çıktı: ``ema_icerik.json``. Metin kopyalanmaz — çıkarılan bölümler kayıt
yazarken okunmak için, sayfaya olduğu gibi aktarılmaz.

Çalıştırma:  python3 tools/ema_cek.py [slug ...]
"""
import collections
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KOK, 'ema_icerik.json')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                    'Chrome/120 Safari/537.36'}

# Monograftaki başlıklar ve karşılıkları
BOLUM = [
    ('endikasyon', r'4\.1\.?\s*Therapeutic indications?'),
    ('dozaj', r'4\.2\.?\s*Posology'),
    ('kontrendikasyon', r'4\.3\.?\s*Contraindications?'),
    ('uyari', r'4\.4\.?\s*Special warnings'),
    ('etkilesim', r'4\.5\.?\s*Interactions?'),
    ('gebelik', r'4\.6\.?\s*Fertility, pregnancy'),
    ('istenmeyen', r'4\.8\.?\s*Undesirable effects?'),
    ('doz_asimi', r'4\.9\.?\s*Overdose'),
]


def al(u, ikili=False):
    d = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
    return d if ikili else d.decode('utf-8', 'replace')


def monograf_pdf(slug):
    """Monograf sayfasındaki nihai AB monografı PDF'inin adresi."""
    h = al(f'https://www.ema.europa.eu/en/medicines/herbal/{slug}')
    yol = re.findall(r'href="(/en/documents/herbal-monograph/[^"]*\.pdf)"', h)
    nihai = [p for p in yol if 'final-european-union' in p or 'final-community' in p]
    if not nihai:
        nihai = [p for p in yol if 'draft' not in p] or yol
    if not nihai:
        return None
    # en son sürüm: "revision-N" varsa en büyüğü
    def rev(p):
        m = re.search(r'revision-(\d+)', p)
        return int(m.group(1)) if m else 0
    return 'https://www.ema.europa.eu' + sorted(nihai, key=rev)[-1]


HAM = os.path.join(KOK, '.ema_ham')


def metin(pdf_adres, slug=None):
    """Monografın düz metni. Bölme mantığı değiştiğinde yeniden indirmemek
    için ham metin .ema_ham/ klasörüne saklanır."""
    if slug:
        os.makedirs(HAM, exist_ok=True)
        yol_ham = os.path.join(HAM, slug + '.txt')
        if os.path.exists(yol_ham):
            return open(yol_ham, encoding='utf-8').read()
    d = al(pdf_adres, ikili=True)
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
        f.write(d)
        yol = f.name
    try:
        t = subprocess.run(['pdftotext', '-layout', yol, '-'],
                           capture_output=True, text=True, timeout=120).stdout
        if slug:
            open(os.path.join(HAM, slug + '.txt'), 'w', encoding='utf-8').write(t)
        return t
    finally:
        os.unlink(yol)


def kolon_sinirlari(t):
    """Monografın iki kolonunun metindeki sütun konumu.

    ``pdftotext -layout`` kolonları aynı satırda yan yana bırakıyor:
    solda *Well-established use*, sağda *Traditional use*. Başlık
    satırındaki "Traditional use" ifadesinin konumu sınırı veriyor.
    Birden çok sayfada tekrarlandığı için en sık görülen konum alınır.
    """
    yer = [m.start() - m.string.rfind('\n', 0, m.start()) - 1
           for m in re.finditer(r'Traditional use', t)]
    yer = [y for y in yer if y > 10]
    if not yer:
        return None
    return collections.Counter(yer).most_common(1)[0][0]


def _bol(ln, sinir):
    """Satırı kolon sınırından böler, kelimeyi ortadan kesmeden.

    Gövde metni kolon sınırının bir iki karakter solundan başlayabiliyor;
    sınır kelimenin ortasına düşerse en yakın boşluğa kaydırılır
    ("active substance" -> "active ubstance" hatası böyle çıkıyordu).
    """
    k = sinir
    if 0 < k < len(ln) and not ln[k - 1].isspace() and not ln[k].isspace():
        sol_bosluk = ln.rfind(' ', 0, k)
        sag_bosluk = ln.find(' ', k)
        aday = [x for x in (sol_bosluk, sag_bosluk) if x != -1]
        if aday:
            k = min(aday, key=lambda x: abs(x - sinir))
    return ln[:k], ln[k:]


def kolonla(parca, sinir):
    """Bir bölümün metnini (iyi bilinen kullanım, geleneksel kullanım) diye böler."""
    if not sinir:
        return None, parca
    sol, sag = [], []
    for ln in parca.split('\n'):
        if re.search(r'Well-established use\s+Traditional use', ln):
            continue
        s_, g_ = (x.strip() for x in _bol(ln, sinir))
        if s_:
            sol.append(s_)
        if g_:
            sag.append(g_)
    temiz = lambda xs: re.sub(r'\s+', ' ', ' '.join(xs)).strip()
    return temiz(sol), temiz(sag)


def bolumler(t, sinir):
    """Monograf metnini 4.x başlıklarına, her bölümü de iki kolona böler."""
    yer = []
    for ad, kal in BOLUM:
        m = re.search(kal, t, re.I)
        if m:
            yer.append((m.start(), m.end(), ad))
    yer.sort()
    out = {}
    for i, (b, e, ad) in enumerate(yer):
        son = yer[i + 1][0] if i + 1 < len(yer) else min(len(t), e + 6000)
        parca = t[e:son]
        # sayfa altlığı ve dipnotlar bölüm metnine karışıyor, atılır
        parca = re.sub(r'(?m)^(European Union herbal monograph|EMA/HMPC/|Page \d+|\d+\s*$).*$',
                       '', parca)
        iyi, gel = kolonla(parca, sinir)
        out[ad] = {'iyi_bilinen': (iyi or None), 'geleneksel': (gel or None)}
    return out


# Monograf sayfalarının dipnot ve kalıp metni. Kolon bölmesinde boş
# kolona sızabiliyor, bu yüzden endikasyon sayılmaz.
KALIP = (
    'declaration of the active substance',
    'complies with the Ph. Eur',
    'quality guidance',
    'in accordance with relevant herbal',
    'Not applicable',
)


def endikasyon_var(metin_):
    """Kolondaki metin gerçekten bir endikasyon mu, dipnot mu?

    EMA endikasyonları iki kalıptan biriyle yazıyor: geleneksel kullanımda
    "Traditional herbal medicinal product for ...", iyi bilinen kullanımda
    "Herbal medicinal product ...". Sayfa dipnotları ve kalıp cümleler bu
    kalıpları taşımadığı için ayıklanır.
    """
    if not metin_:
        return False
    t = metin_
    for k in KALIP:
        t = t.replace(k, '')
    return bool(re.search(r'[Hh]erbal medicinal product|Indication\s*\d\)'
                          r'|is indicated|used (?:as|for|to|in)', t))


def kanit_duzeyi(bolum):
    """Monografın endikasyonları hangi kategoride — kaynaktan, yorumsuz.

    EMA endikasyonu iki kategoriden birine koyuyor: *well-established use*
    klinik kanıta dayanır, *traditional use* yalnızca uzun kullanım
    geçmişine. 4.1 bölümünün sol kolonunda gerçek bir endikasyon varsa
    monografta klinik kanıta dayanan en az bir endikasyon var demektir.
    """
    e = (bolum or {}).get('endikasyon') or {}
    iyi, gel = endikasyon_var(e.get('iyi_bilinen')), endikasyon_var(e.get('geleneksel'))
    if iyi and gel:
        return 'ikisi birlikte'
    if iyi:
        return 'iyi bilinen kullanım'
    if gel:
        return 'geleneksel kullanım'
    return None


def main():
    out = {}
    if os.path.exists(CIKTI):
        out = json.load(open(CIKTI, encoding='utf-8'))
    istenen = sys.argv[1:]
    if not istenen:
        parti = json.load(open(os.path.join(
            os.path.dirname(KOK), 'parti70.json'), encoding='utf-8')) \
            if os.path.exists(os.path.join(os.path.dirname(KOK), 'parti70.json')) else None
        if parti is None:
            print('slug verilmedi ve parti dosyası yok'); return
        istenen = [e['slug'] for o in parti for e in o['ema']]
    istenen = [s for s in dict.fromkeys(istenen) if s not in out]
    print(len(istenen), 'monograf çekilecek')
    for i, slug in enumerate(istenen, 1):
        try:
            p = monograf_pdf(slug)
            if not p:
                out[slug] = {'hata': 'monograf PDF bağlantısı yok'}
                print(f'{i:3d}/{len(istenen)} {slug:42s} PDF YOK')
            else:
                t = metin(p, slug)
                sinir = kolon_sinirlari(t)
                bol = bolumler(t, sinir)
                out[slug] = {'pdf': p, 'kanit': kanit_duzeyi(bol),
                             'bolum': bol, 'uzunluk': len(t)}
                print(f'{i:3d}/{len(istenen)} {slug:42s} '
                      f'{out[slug]["kanit"] or "BELİRSİZ"}')
        except Exception as ex:
            out[slug] = {'hata': str(ex)[:120]}
            print(f'{i:3d}/{len(istenen)} {slug:42s} HATA {ex}')
        json.dump(out, open(CIKTI, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1, sort_keys=True)
        time.sleep(0.5)
    iyi = sum(1 for v in out.values() if v.get('bolum'))
    print(f'\n{iyi}/{len(out)} monografın bölümleri çıkarıldı')


if __name__ == '__main__':
    main()
