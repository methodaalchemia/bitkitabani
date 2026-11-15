#!/usr/bin/env python3
"""DergiPark'ın doğrudan PDF bağlantılarını makale adresine çevirir.

`/download/article-file/NNN` bir makaleye değil bir dosyaya işaret ediyor:
künye üstverisi yok, bağlantı da okuyucuyu doğrudan PDF'e atıyor. Ama
dosyanın HTTP başlığındaki ``content-disposition`` alanı makalenin
başlığını ve köşeli parantez içinde makale kimliğini taşıyor
(``...[#1067778]-2231021.pdf``), bazılarında da DOI'yi
(``10.17099-jffiu.98238-176576.pdf``).

Yol: başlığı oku, Crossref'te ara, başlık birebir örtüşüyorsa DOI'yi al.
DOI hem kalıcı hem APA'nın istediği bağlantı. DOI bulunamazsa makale
kimliği ve başlık yazdırılır, adres elle bulunur.

Çalıştırma:  python3 tools/dergipark_link.py
"""
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                    'Chrome/120 Safari/537.36'}
CIKTI = os.path.join(KOK, 'dergipark_adres.json')


def sade(x):
    """Karşılaştırma için başlığı sadeleştirir: harf dışı her şey atılır."""
    x = unicodedata.normalize('NFKD', (x or '').lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in x if not unicodedata.combining(c)))


def basliklar():
    """Derlenmiş sitedeki doğrudan PDF bağlantıları."""
    import glob
    out = set()
    for f in glob.glob(os.path.join(KOK, 'site', '**', '*.html'), recursive=True):
        h = open(f, encoding='utf-8').read()
        out |= set(re.findall(
            r'https://dergipark\.org\.tr/\w+/download/article-file/\d+', h))
    return sorted(out)


def dosya_adi(u):
    """PDF'in content-disposition başlığından adını okur."""
    try:
        r = urllib.request.urlopen(
            urllib.request.Request(u, headers=UA, method='HEAD'), timeout=60)
        cd = r.headers.get('content-disposition') or ''
    except Exception:
        return None
    m = re.search(r"filename\*=utf-8''([^;]+)", cd)
    if m:
        return urllib.parse.unquote(m.group(1))
    m = re.search(r'filename="?([^";]+)', cd)
    return m.group(1) if m else None


def coz(ad):
    """Dosya adından (başlık, makale kimliği, doi) üçlüsü."""
    if not ad:
        return None, None, None
    ad = re.sub(r'\.pdf$', '', ad)
    doi = None
    m = re.match(r'^(10\.\d{4,5})-([^-]+)-\d+$', ad)
    if m:
        doi = f'{m.group(1)}/{m.group(2)}'
        return None, None, doi
    kimlik = None
    m = re.search(r'\[#(\d+)\]', ad)
    if m:
        kimlik = m.group(1)
        ad = ad[:m.start()]
    ad = re.sub(r'-\d+$', '', ad).strip()
    # DergiPark iki dilli başlıkları " - " ile birleştiriyor; ilki özgün dil
    baslik = ad.split(' - ')[0].strip()
    return baslik or None, kimlik, None


def doi_acilir(doi):
    """DOI gerçekten bir sayfaya çözülüyor mu?

    Crossref kaydı olan bir DOI her zaman açılmıyor: eski DergiPark
    kayıtlarının bir bölümünde DOI tescil edilmiş ama hedefi yok ve
    doi.org 404 döndürüyor. Doğrulamadan kabul edilirse çalışan bir PDF
    bağlantısı kırık bir DOI ile değiştirilmiş olur — bu araç bir kez
    bunu yaptı, üç bağlantı kırıldı. Bu yüzden kabul şartı Crossref'te
    bulunmak değil, doi.org'un açılması.
    """
    try:
        r = urllib.request.urlopen(urllib.request.Request(
            'https://doi.org/' + doi, headers=UA), timeout=50)
        return r.status == 200
    except urllib.error.HTTPError:
        return False
    except Exception:
        return None  # ağ sorunu: karar verilemedi


def crossref_doi(baslik):
    """Başlık birebir örtüşen Crossref kaydının DOI'si."""
    u = ('https://api.crossref.org/works?rows=5&select=DOI,title&query.bibliographic='
         + urllib.parse.quote(baslik[:300]))
    try:
        d = json.loads(urllib.request.urlopen(
            urllib.request.Request(u, headers=UA), timeout=60).read())
    except Exception:
        return None
    hedef = sade(baslik)
    for it in d.get('message', {}).get('items', []):
        for t in (it.get('title') or []):
            s = sade(t)
            # iki dilli başlıklarda biri diğerini içerebilir
            if s and (s == hedef or (len(hedef) > 25 and hedef in s)):
                return it.get('DOI')
    return None


def main():
    out = {}
    if os.path.exists(CIKTI):
        out = json.load(open(CIKTI, encoding='utf-8'))
    hepsi = basliklar()
    print(len(hepsi), 'doğrudan PDF bağlantısı')
    for i, u in enumerate(hepsi, 1):
        if out.get(u, {}).get('adres'):
            continue
        ad = dosya_adi(u)
        baslik, kimlik, doi = coz(ad)
        if not doi and baslik:
            doi = crossref_doi(baslik)
        kayit = {'baslik': baslik, 'makale_id': kimlik, 'doi': doi}
        kayit['adres'] = None
        if doi:
            acilir = doi_acilir(doi)
            if acilir:
                kayit['adres'] = 'https://doi.org/' + doi
            elif acilir is False:
                kayit['doi_404'] = doi
                kayit['not'] = ('Crossref DOI verdi ama doi.org 404 döndürüyor; '
                                'doğrudan PDF bağlantısında kalıyor.')
            else:
                kayit['not'] = 'DOI doğrulanamadı (ağ); yeniden çalıştırılmalı.'
        out[u] = kayit
        isaret = kayit['adres'] or f'ÇÖZÜLEMEDİ (makale #{kimlik})'
        print(f'{i:3d}/{len(hepsi)}  {u.rsplit("/", 1)[-1]:9s} {isaret}')
        if baslik and not doi:
            print(f'          başlık: {baslik[:95]}')
        json.dump(out, open(CIKTI, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1, sort_keys=True)
        time.sleep(0.8)
    n = sum(1 for v in out.values() if v.get('adres'))
    print(f'\n{n}/{len(hepsi)} bağlantı DOI adresine çevrilebilir')


if __name__ == '__main__':
    main()
