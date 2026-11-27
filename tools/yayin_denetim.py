#!/usr/bin/env python3
"""Yayın kapısında koşan iddia denetimi: kayıttaki iddialar kaynakla tutuyor mu?

Neden var (25 Kasım 2026): kapı otomatik birleştiriyor, Eda doz ve
kontrendikasyon iddiasını doğrulayamıyor. "Dikkatli bakarım" bir mekanizma
değil. Bu betik yargı gerektirmeyen iddiaları makineyle sınar ve tutmazsa
birleştirmeyi durdurur.

  python3 tools/yayin_denetim.py              # main'e göre yeni/değişen kayıtlar
  python3 tools/yayin_denetim.py id1 id2      # verilen kayıtlar

Çıkış kodu 1 ise BİRLEŞTİRME.

Sınırı açık olsun: bu betik cümlenin doğru olduğunu kanıtlamaz. Yalnızca
kaynakla çelişen, kaynağı bulunmayan ve kendi ağzımızdan iddia kuran
cümleleri yakalar. Yeni bir arıza biçimini yakalamaz — onun için ikinci bir
göz gerekir.
"""
import json, os, re, subprocess, sys, unicodedata, urllib.parse

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
EMA_DIZIN = os.path.join(KOK, 'veri', 'onbellek', 'ema_index.json')
TITCK = os.path.join(KOK, 'veri', 'onbellek', 'titck')
UA = 'BitkiTabani/1.0 (https://bitkitabani.com)'

# Kendi ağzımızdan iddia kurulmaz; özne kaynaktır.
YASAK = [
    (r'\biyi gelir\b', 'kendi ağzımızdan "iyi gelir"'),
    (r'\btedavi eder\b', 'kendi ağzımızdan "tedavi eder"'),
    (r'\bşifa bulur\b', 'kendi ağzımızdan "şifa bulur"'),
    (r'\bkesinlikle (?:iyileştir|tedavi)', 'kesinlik iddiası'),
    (r'\bmucize\b', '"mucize"'),
    (r'\bkanıtlanmıştır\b(?!.{0,40}(?:derleme|çalışma|monograf))', 'kaynaksız "kanıtlanmıştır"'),
]
# Hayvan/tüp içi çalışmayı insanda kanıt gibi sunma riski
HAYVAN = re.compile(r'\b(sıçan|fare|tavşan|hayvan|in vitro|tüp içi|hücre kültür)', re.I)
INSAN = re.compile(r'\b(insanda|klinik|randomize|katılımcı|gönüllü|hasta)', re.I)


# 27 Kasım 2026: kesme işareti yanlış HATA üretiyordu. Künyede tipografik
# kesme (D’Addabbo), NCBI'de düz kesme (D'Addabbo) var. NFKD tipografik
# kesmeyi ayrıştırmıyor, ascii süzgeci onu atıyor: "daddabbo" ile "d'addabbo"
# karşılaştırılıyor ve tutmuyor. Yanlış HATA birleştirmeyi durdurduğu için
# kendisi bir arıza — her iki biçimi de baştan düşürüyoruz.
_KESME = str.maketrans('', '', "'\u2019\u2018\u02bc`\u00b4")


def sade(t):
    t = unicodedata.normalize('NFKD', t or '').encode('ascii', 'ignore').decode().lower()
    return t.translate(_KESME)


def kayitlar():
    import kuyruk as K
    d = json.load(open(os.path.join(KOK, 'data.json'), encoding='utf-8'))
    return {p['id']: p for p in d['P'] + K.Q}


def yeni_idler():
    """main'e göre eklenen kuyruk dosyalarındaki kayıt id'leri."""
    r = subprocess.run(['git', 'diff', '--name-only', 'origin/main...HEAD'],
                       capture_output=True, text=True, cwd=KOK)
    out = []
    for f in r.stdout.split():
        if f.startswith('kuyruk/') and f.endswith('.py'):
            yol = os.path.join(KOK, f)
            if os.path.exists(yol):
                out += re.findall(r"id='([a-z0-9]+)'", open(yol, encoding='utf-8').read())
    return sorted(set(out))


def ema_kontrol(p, hata):
    """"EMA monografı yok" diyorsak EMA'da gerçekten yok mu — TÜR düzeyinde."""
    if not os.path.exists(EMA_DIZIN): return
    metin = json.dumps(p, ensure_ascii=False)
    iddia_yok = re.search(r'(EMA|Avrupa İlaç Ajansı)[^.]{0,60}(monograf[ıi]? yok|monografı bulunm)', metin)
    tur = (p.get('taxon') or p.get('la') or '').strip()
    if not tur: return
    d = json.load(open(EMA_DIZIN, encoding='utf-8'))
    tam = [k for k in d.values()
           if tur.lower() in ((k.get('tur') or '') + ' ' + (k.get('latin') or '')).lower()
           and 'monograph' in (k.get('sonuc') or '').lower()]
    if iddia_yok and tam:
        hata.append(f'{p["id"]}: "EMA monografı yok" diyor ama EMA bu tür için monograf vermiş '
                    f'({tam[0].get("latin")}) — {tam[0].get("sayfa")}')
    # cins düzeyi tuzağı: EMA'da yalnız akraba tür varsa ve biz "var" diyorsak
    if p.get('ema') and not tam:
        cins = tur.split()[0].lower()
        akraba = [k for k in d.values() if cins in ((k.get('latin') or '') + ' ' + (k.get('tur') or '')).lower()]
        if akraba:
            hata.append(f'{p["id"]}: ema alanı dolu ama EMA\'da bu TÜR için monograf yok; '
                        f'yalnız akraba var ({akraba[0].get("latin")}). Bir türün monografı akrabasına ait değildir.')


def titck_kontrol(p, uyari):
    """TİTCK metinlerinde yalnız cins geçiyorsa işaretle — insan baksın."""
    if not os.path.isdir(TITCK): return
    tur = (p.get('taxon') or p.get('la') or '').strip()
    if not tur: return
    cins = tur.split()[0]
    for f in sorted(os.listdir(TITCK)):
        if not f.endswith('.txt'): continue
        m = open(os.path.join(TITCK, f), encoding='utf-8', errors='replace').read().lower()
        if cins.lower() in m and tur.lower() not in m:
            uyari.append(f'{p["id"]}: TİTCK "{f[:-4]}" monografında yalnız CİNS geçiyor, tür geçmiyor — '
                         f'o monografın kısıtlamaları bu türe uygulanamaz')


def kaynak_kontrol(p, hata):
    """PubMed künyeleri gerçekten var mı, ilk yazar ve yıl tutuyor mu."""
    for ad, url in (p.get('kaynak') or []):
        m = re.search(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)', url or '')
        if not m: continue
        pmid = m.group(1)
        # NCBI hız sınırı veriyor; tek denemede "bulunamadı" demek yanlış HATA üretir
        # ve yanlış HATA birleştirmeyi durdurduğu için kendisi bir arıza biçimidir.
        import time as _t
        k = None
        for _d in range(3):
            r = subprocess.run(['curl', '-sL', '-m', '45', '-A', UA,
                                'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
                                f'?db=pubmed&retmode=json&id={pmid}'], capture_output=True, text=True)
            try:
                k = json.loads(r.stdout)['result'][pmid]
                if k.get('title') or k.get('authors'): break
                k = None
            except Exception:
                k = None
            _t.sleep(3 * (_d + 1))
        if not k:
            hata.append(f'{p["id"]}: PMID {pmid} NCBI\'de doğrulanamadı (üç deneme) — {ad[:60]}')
            continue
        yil = (k.get('pubdate') or '')[:4]
        yazar = sade((k.get('authors') or [{}])[0].get('name', '')).split()[0] if k.get('authors') else ''
        if yil and yil not in ad:
            hata.append(f'{p["id"]}: PMID {pmid} yılı {yil}, künyede yok — {ad[:60]}')
        if yazar and yazar not in sade(ad):
            hata.append(f'{p["id"]}: PMID {pmid} ilk yazarı "{yazar}", künyede geçmiyor — {ad[:60]}')


def dil_kontrol(p, hata, uyari):
    metin = ' '.join(str(v) for v in p.values() if isinstance(v, str))
    for kalip, ad in YASAK:
        if re.search(kalip, metin, re.I):
            hata.append(f'{p["id"]}: yasak kalıp — {ad}')
    bilim = p.get('bilim') or ''
    if bilim and HAYVAN.search(bilim) is None and INSAN.search(bilim) is None and len(bilim) > 200:
        uyari.append(f'{p["id"]}: bilim bölümünde çalışmanın türü (insan / hayvan / tüp içi) belirtilmemiş olabilir')
    haz = p.get('haz') or ''
    if re.search(r'\d+\s*(mg|g|ml|damla)', haz) and (p.get('kanit') == 'geleneksel') and not p.get('ema'):
        uyari.append(f'{p["id"]}: haz alanında doz var ama monograf yok ve kanıt "geleneksel" — dozun kaynağı nedir?')


def main(idler):
    K = kayitlar()
    hata, uyari = [], []
    if not idler: idler = yeni_idler()
    if not idler:
        print('denetlenecek yeni kayıt yok'); return 0
    for i in idler:
        p = K.get(i)
        if not p:
            hata.append(f'{i}: kayıt bulunamadı'); continue
        ema_kontrol(p, hata)
        titck_kontrol(p, uyari)
        kaynak_kontrol(p, hata)
        dil_kontrol(p, hata, uyari)
    for u in uyari: print('UYARI  ', u)
    for h in hata: print('HATA   ', h)
    print(f'\n{len(idler)} kayıt denetlendi · {len(hata)} hata · {len(uyari)} uyarı')
    if hata:
        print('→ HATA varken BİRLEŞTİRME.')
    if uyari:
        print('→ Uyarılar insan gözü ister; emin değilsen birleştirme.')
    return 1 if hata else 0


if __name__ == '__main__':
    sys.exit(main([a for a in sys.argv[1:] if not a.startswith('-')]))
