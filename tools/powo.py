#!/usr/bin/env python3
"""POWO kalıcı kayıt adreslerini toplar.

Künyelerde POWO'ya arama sorgusu adresiyle (``/results?q=...``) bağlanmak
iki sorun doğuruyor: adres bir kayda değil bir aramaya işaret ediyor, ve
arama sonucu zamanla değişebiliyor. POWO'nun kendi arama API'si her ad
için kalıcı bir IPNI kimliği (``urn:lsid:ipni.org:names:...``) veriyor;
bu araç o kimlikleri ``powo_kimlik.json`` dosyasına yazıyor, derleme de
oradan ``/taxon/<kimlik>`` adresini kuruyor.

Çalıştırma:  python3 tools/powo.py
"""
import json
import os
import sys
import time
import re
import urllib.parse
import urllib.request

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
ONBELLEK = os.path.join(KOK, 'powo_kimlik.json')
UA = {'User-Agent': 'bitkitabani-powo/1.0 (+https://bitkitabani.com)'}


def adlar():
    """Künyelerde POWO'ya bağlanan bütün botanik adlar.

    Yayındaki kayıtlar data.json'da, bekleyenler kuyrukta. Derleme
    ikisini birleştirdiği için burada da ikisi birlikte taranıyor;
    yoksa kuyruktaki bitkiler yayına girdiği gün arama adresiyle
    çıkar.
    """
    from refs import POWO
    import kuyruk
    d = json.load(open(os.path.join(KOK, 'data.json'), encoding='utf-8'))
    out = {}
    for p in d['P']:
        ad = POWO.get(p['id']) or p['la'].split(',')[0].strip()
        if ad:
            out.setdefault(ad, []).append(p['id'])
    for q in kuyruk.Q:
        ad = (q.get('taxon') or q['la'].split(',')[0]).strip()
        if ad:
            out.setdefault(ad, []).append(q['id'])
    # familya sayfalarındaki familya adları da POWO'ya bağlanıyor
    try:
        import familya
        for f in familya.FAM_BILGI:
            out.setdefault(f, []).append('familya:' + f)
    except Exception:
        pass
    return out


WCVP = 'f382f0ce-323a-4091-bb9f-add557f3a9a2'  # Kew WCVP, POWO'nun veri seti


def gbif_yazar(ad):
    """Kabul edilen adın yazar kısaltmasını GBIF'in WCVP kopyasından alır.

    IPNI aynı ada birkaç kayıt döndürdüğünde (eşadlılık) hangisinin
    doğru olduğunu ad değil yazar belirliyor. POWO'nun verisi GBIF'te
    WCVP veri seti olarak duruyor; oradaki ACCEPTED kaydın yazarı
    IPNI adaylarını teke indiriyor.
    """
    u = ('https://api.gbif.org/v1/species/search?datasetKey=' + WCVP
         + '&rank=SPECIES&status=ACCEPTED&limit=20&q=' + urllib.parse.quote(ad))
    try:
        d = json.loads(urllib.request.urlopen(
            urllib.request.Request(u, headers=UA), timeout=60).read())
    except Exception:
        return None
    sade = lambda x: re.sub(r'[×x]\s*', '', (x or '')).replace('  ', ' ').strip().lower()
    for r in d.get('results', []):
        tam = r.get('scientificName') or ''
        kanon = r.get('canonicalName') or ' '.join(tam.split()[:2])
        if sade(kanon) != sade(ad):
            continue
        yazar = tam[len(kanon):].strip() if tam.startswith(kanon) else None
        if not yazar:
            # "Rosa ×damascena Herrm." gibi: kanon ×'siz dönebiliyor
            parca = tam.split()
            yazar = ' '.join(parca[2:]) if len(parca) > 2 else None
        if yazar:
            return yazar.strip()
    return None


def ara(ad, yazar=None):
    """Adın kalıcı IPNI kimliğini döndürür.

    POWO'nun kendi arama API'si buradan 403 veriyor (bot koruması), ama
    POWO kayıtları IPNI kimlik uzayını kullanıyor: IPNI'nin ``inPowo``
    alanı o adın POWO'da bir kaydı olup olmadığını söylüyor. Kabul
    ölçütü dar tutuldu — ad birebir eşleşmeli, rütbe beklenen rütbe
    olmalı ve kayıt POWO'da bulunmalı. İki aday kalırsa (eşadlılık)
    hiçbiri seçilmez: yanlış bir kalıcı adres, arama adresinden daha
    kötüdür.
    """
    tek = len(ad.split()) == 1
    familya = tek and ad.endswith(('ceae', 'inae'))
    if familya:
        bekle, suzgec = ('fam.',), '&f=f_familial'
    elif tek:
        bekle, suzgec = ('gen.',), '&f=f_generic'
    else:
        bekle, suzgec = ('spec.', 'subsp.', 'var.', 'f.'), ''
    # IPNI melez adlarını "Mentha x piperita" biçiminde tutuyor; sitedeki
    # "Mentha × piperita" yazımı doğrudan eşleşmiyor, biçimler denenir.
    denemeler = [ad]
    if '×' in ad or ' x ' in ad:
        yalin = re.sub(r'\s*[×x]\s*', ' ', ad).strip()
        denemeler = [ad.replace('×', 'x'), ad.replace('× ', '×'), yalin, ad]
    elif len(ad.split()) == 2 and not tek:
        denemeler = [ad, ad.replace(' ', ' × ', 1), ad.replace(' ', ' x ', 1)]
    sonuc = []
    for deneme in denemeler:
        u = ('https://www.ipni.org/api/1/search?perPage=50' + suzgec
             + '&q=' + urllib.parse.quote(deneme))
        try:
            d = json.loads(urllib.request.urlopen(
                urllib.request.Request(u, headers=UA), timeout=60).read())
        except Exception as ex:
            return None, f'istek: {ex}'
        sonuc = d.get('results') or []
        if sonuc:
            break
        time.sleep(0.4)
    d = {'results': sonuc}
    esle = lambda x: re.sub(r'\s*[×x]\s*', ' ', (x or '')).strip().lower()
    hedef = esle(ad)
    aday = []
    for r in (d.get('results') or []):
        if esle(r.get('name')) != hedef:
            continue
        # Familya kayıtlarında inPowo alanı false dönüyor, ama POWO'da
        # familya sayfası var (Rosaceae 30000200-2 ile doğrulandı), bu
        # yüzden familyada bu koşul uygulanmıyor.
        if not familya and not r.get('inPowo'):
            continue
        if r.get('rank') not in bekle:
            continue
        kimlik = (r.get('url') or '').rsplit('/', 1)[-1]
        if not kimlik:
            continue
        aday.append({'kimlik': kimlik, 'ad': r.get('name'),
                     'yazar': r.get('authors'), 'rutbe': r.get('rank'),
                     'familya': r.get('family')})
    if not aday:
        return None, 'POWO kaydı olan birebir eşleşme yok'
    if len(aday) > 1 and yazar:
        kis = lambda x: re.sub(r'[^a-z]', '', (x or '').lower())
        tam = [a for a in aday if kis(a['yazar']) == kis(yazar)]
        if len(tam) == 1:
            tam[0]['yazar_kaynagi'] = 'GBIF/WCVP'
            return tam[0], None
    if len(aday) > 1:
        return None, 'eşadlı: ' + ', '.join(
            f'{a["kimlik"]} ({a["yazar"]})' for a in aday[:4])
    return aday[0], None


def main():
    onbellek = {}
    if os.path.exists(ONBELLEK):
        onbellek = json.load(open(ONBELLEK, encoding='utf-8'))
    hepsi = adlar()
    print(len(hepsi), 'botanik ad')
    eksik = [a for a in hepsi if not (onbellek.get(a) or {}).get('kimlik')]
    print(len(eksik), 'çözülmemiş')
    for i, ad in enumerate(sorted(eksik), 1):
        kayit, hata = ara(ad)
        if not kayit and hata and hata.startswith('eşadlı'):
            yz = gbif_yazar(ad)
            if yz:
                kayit, hata = ara(ad, yazar=yz)
        if kayit:
            onbellek[ad] = kayit
            print(f'{i:3d}/{len(eksik)}  {ad}  ->  {kayit["kimlik"]}')
        else:
            onbellek.setdefault(ad, {})['hata'] = hata
            print(f'{i:3d}/{len(eksik)}  {ad}  ->  ÇÖZÜLEMEDİ: {hata}')
        if i % 5 == 0:
            json.dump(onbellek, open(ONBELLEK, 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1, sort_keys=True)
        time.sleep(0.6)
    json.dump(onbellek, open(ONBELLEK, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1, sort_keys=True)
    cozulen = sum(1 for v in onbellek.values() if v.get('kimlik'))
    print(f'\n{cozulen}/{len(hepsi)} ad kalıcı kimliğe bağlandı')


if __name__ == '__main__':
    main()
