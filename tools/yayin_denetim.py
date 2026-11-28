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
# 28 Kasım 2026 (p009 turu): bu iki yol depoda **yoktu** ve ema_kontrol ile
# titck_kontrol sessizce atlanıyordu — yani denetimin en önemli kolu, cins
# düzeyi monograf tuzağı, hiç koşmamıştı ve betik yine "0 hata" yazıyordu.
# Sessiz atlama, yanlış HATA kadar arızadır: kapı atlanan denetimi geçmiş
# sayıyor. Depoda duran gerçek kaynaklara düşülüyor ve atlanan her kol
# çıktıda ATLANDI diye **yüksek sesle** bildiriliyor.
EMA_DIZIN = os.path.join(KOK, 'veri', 'onbellek', 'ema_index.json')
EMA_YEDEK = os.path.join(KOK, 'ema_monograf.json')
TITCK = os.path.join(KOK, 'veri', 'onbellek', 'titck')
ATLANDI = []


def ema_dizin():
    """EMA dizinini döndür: önbellek varsa o, yoksa depodaki ema_monograf.json.

    İki dosyanın alan adları farklı; ema_monograf.json'da tür adı 'botanik',
    monograf adı 'latin', sayfa 'adres'. Ortak biçime çeviriyoruz.
    """
    for yol in (EMA_DIZIN, EMA_YEDEK):
        if os.path.exists(yol):
            d = json.load(open(yol, encoding='utf-8'))
            return {k: {'tur': v.get('tur') or v.get('botanik') or '',
                        'latin': v.get('latin') or '',
                        'sonuc': v.get('sonuc') or '',
                        'sayfa': v.get('sayfa') or v.get('adres') or ''}
                    for k, v in d.items()}
    return None
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
    """main'e göre eklenen kuyruk dosyalarındaki kayıt id'leri.

    28 Kasım 2026: yalnız `origin/main...HEAD` bakılıyordu. Kapı PR dalını
    `--no-commit` ile birleştirip denetimleri koştuğu için HEAD hâlâ
    origin/main'deydi: diff boş çıkıyor, betik "denetlenecek yeni kayıt yok"
    deyip **0 dönüyordu.** Sekiz kayıtlık bir parti denetlenmemiş hâlde
    temiz görünebilirdi. Çalışma ağacı ve indeks de artık okunuyor.
    """
    satirlar = []
    for arg in (['diff', '--name-only', 'origin/main...HEAD'],
                ['diff', '--name-only', '--cached'],
                ['diff', '--name-only']):
        r = subprocess.run(['git'] + arg, capture_output=True, text=True, cwd=KOK)
        satirlar += r.stdout.split()
    out = []
    for f in satirlar:
        if f.startswith('kuyruk/') and f.endswith('.py'):
            yol = os.path.join(KOK, f)
            if os.path.exists(yol):
                out += re.findall(r"id='([a-z0-9]+)'", open(yol, encoding='utf-8').read())
    return sorted(set(out))


def ema_kontrol(p, hata):
    """"EMA monografı yok" diyorsak EMA'da gerçekten yok mu — TÜR düzeyinde."""
    d = ema_dizin()
    if d is None:
        ATLANDI.append('EMA tür düzeyi monograf denetimi — ne veri/onbellek/ema_index.json '
                       'ne ema_monograf.json bulundu')
        return
    metin = json.dumps(p, ensure_ascii=False)
    iddia_yok = re.search(r'(EMA|Avrupa İlaç Ajansı)[^.]{0,60}(monograf[ıi]? yok|monografı bulunm)', metin)
    tur = (p.get('taxon') or p.get('la') or '').strip()
    if not tur: return
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
    """TİTCK metinlerinde yalnız cins geçiyorsa işaretle — insan baksın.

    27 Kasım 2026 (akşam turu): bu denetim sabah turunda iki kola
    daraltılmıştı — (a) kaydın monografa fiilen atıf yapması, (b) monografın
    cinsi çapraz duyarlılık gerekçesiyle sayması. **Daraltma geri alındı**,
    çünkü ikinci göz denetiminde ölçüldü ki daraltma kendi gerekçesini
    susturuyor.

    huacatay (*Tagetes minuta*) için eski hâl 3 uyarı veriyordu, daraltılmış
    hâl 0. Oysa TİTCK'in `dulavratotu` monografı birebir şöyle diyor:
    "Asteraceae familyası bitkilerine (… ve **Tagetes L.** cinslerine ait
    türler) karşı aşırı duyarlılık görülebilir. **Anafilaktik şok
    görülebilir.**" `enginar` monografı da Tagetes'i adıyla sayıyor.
    huacatay'ın `guvNot` alanında ise "duyarl", "alerj" ve "anafila"
    sözcüklerinin **hiçbiri geçmiyor** (sayım 0/0/0); alan tamamen
    fototoksisite üzerine. Kol (b)'nin muafiyet listesi "compositae" ve
    "familyas" sözcüklerini o **fototoksisite** cümlesinde bulup uyarıyı
    susturuyordu — bir fototoksisite cümlesi bir anafilaksi boşluğunu
    kapatıyordu. Kuyruk genelinde muafiyet 250 kaydın 66'sını (%26) toptan
    muaf kılıyor ve "aşırı duyarl" tek başına yetiyor.

    Kol (a) de ölçüldü: kuyruktaki 99 TİTCK monograf atıfının yalnız 3'ünü
    saptıyor. Önbellek dosya adları ASCII'leştirilmiş ("seytanpencesi"),
    kayıt metni aksanlı ("şeytanpençesi") ve karşılaştırma `sade()`'den
    geçmiyor.

    Korunan düzeltme: cins adı **sözcük sınırıyla** aranıyor. Alt dizgi
    araması 29 doğrulanmış yanlış pozitif üretiyordu — "Rosa" (gül)
    "Rosaceae" içinde, "Ananas" (comosus) "Fragaria × ananassa" içinde
    eşleşiyordu.

    Denetim gürültülü ama fail-loud: kararı ikinci göz verir. Doğru bir
    çapraz duyarlılık saptayıcısı yazılana kadar bu hâlde bırakıldı;
    tasarım notu `claude/yayin-gunlugu.md` içinde.
    """
    tur = (p.get('taxon') or p.get('la') or '').strip()
    if not tur: return

    # Tür düzeyi kol: TİTCK listesinde bu TÜR için monograf var mı? Bu kol
    # PDF önbelleği olmadan da koşar, çünkü titck.py listenin kendisidir.
    try:
        import titck as _T
        adlar = [a for a, _y in _T.M.values()]
    except Exception as e:
        ATLANDI.append(f'TİTCK tür düzeyi monograf denetimi — titck.py okunamadı ({e})')
        adlar = None
    if adlar is not None:
        metin = json.dumps(p, ensure_ascii=False)
        iddia_yok = re.search(r'(TİTCK|TITCK)[^.]{0,80}(monograf[ıi]? yok|monografı bulunm)', metin)
        tam = [a for a in adlar if tur.lower() in sade(a) or sade(tur) in sade(a)]
        if iddia_yok and tam:
            uyari.append(f'{p["id"]}: "TİTCK monografı yok" diyor ama TİTCK listesinde bu tür var '
                         f'({tam[0]}) — tür düzeyinde bakılsın')

    if not os.path.isdir(TITCK):
        ATLANDI.append(f'TİTCK cins düzeyi çapraz duyarlılık denetimi — {TITCK} yok '
                       '(monograf metinleri indirilmemiş; tools/titck_indir.py)')
        return
    cins = tur.split()[0]
    cins_kalip = re.compile(r'\b' + re.escape(cins.lower()) + r'\b')
    for f in sorted(os.listdir(TITCK)):
        if not f.endswith('.txt'): continue
        m = open(os.path.join(TITCK, f), encoding='utf-8', errors='replace').read().lower()
        if cins_kalip.search(m) and tur.lower() not in m:
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
        print('denetlenecek yeni kayıt yok')
        print('⚠ Bu, denetimin GEÇTİĞİ anlamına gelmez — hiç koşmadı anlamına gelir.')
        print('  Birleştirilecek bir parti varsa kayıt id\'lerini argüman olarak ver:')
        print('  python3 tools/yayin_denetim.py <id> <id> ...')
        return 0
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
    atlanan = list(dict.fromkeys(ATLANDI))   # kayıt başına yinelenmesin
    for a in atlanan:
        print('ATLANDI', a)
    print(f'\n{len(idler)} kayıt denetlendi · {len(hata)} hata · {len(uyari)} uyarı'
          + (f' · {len(atlanan)} denetim kolu ATLANDI' if atlanan else ''))
    if atlanan:
        print('→ Atlanan kol koşmadı; o konuda "temiz" denemez. İkinci göz elle baksın.')
    if hata:
        print('→ HATA varken BİRLEŞTİRME.')
    if uyari:
        print('→ Uyarılar insan gözü ister; emin değilsen birleştirme.')
    return 1 if hata else 0


if __name__ == '__main__':
    sys.exit(main([a for a in sys.argv[1:] if not a.startswith('-')]))
