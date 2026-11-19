"""Bitkilerin Wikidata kimliklerini (Q numarası) toplar -> wikidata_kimlik.json

Şemadaki `about.Taxon.sameAs` için: bir arama motoru ya da dil modeli, sayfanın hangi
varlıktan söz ettiğini ancak dış kimliğe bağlıysa kesin olarak bilir. POWO/IPNI bağı
zaten var; bu dosya Wikidata ayağını tamamlar.

Bilimsel ada göre tam eşleşme arar (P225 = taksonun bilimsel adı). Bulunamazsa o adı atlar;
tahmin yapmaz. Bir kez bulunan kimlik dosyada kalır, tekrar sorgulanmaz.

⚠️ GitHub Actions'ta çalışır. Geliştirme konteynerinden wikidata.org'a erişim yok (403).
"""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CIKTI = os.path.join(ROOT, 'wikidata_kimlik.json')
UA = 'BitkiTabani/1.0 (https://bitkitabani.com; iletisim@bitkitabani.com)'


def sorgu(ad):
    u = ('https://www.wikidata.org/w/api.php?format=json&action=query&list=search&srlimit=1&srsearch='
         + urllib.parse.quote('haswbstatement:"P225=' + ad + '"'))
    r = urllib.request.Request(u, headers={'User-Agent': UA})
    with urllib.request.urlopen(r, timeout=25) as f:
        hits = json.load(f).get('query', {}).get('search', [])
    t = hits[0]['title'] if hits else ''
    return t if t.startswith('Q') and t[1:].isdigit() else ''


def main():
    adlar = sorted(json.load(open(os.path.join(ROOT, 'powo_kimlik.json'), encoding='utf-8')))
    eski = json.load(open(CIKTI, encoding='utf-8')) if os.path.exists(CIKTI) else {}
    yeni, hata = 0, 0
    for ad in adlar:
        if ad in eski:
            continue
        try:
            q = sorgu(ad)
        except Exception as ex:
            hata += 1
            print('  wikidata hatası', ad, ex)
            if hata > 10:
                print('wikidata: çok hata, bırakıldı'); break
            continue
        if q:
            eski[ad] = q; yeni += 1
        time.sleep(0.3)
    json.dump(dict(sorted(eski.items())), open(CIKTI, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'wikidata: {len(eski)} kimlik ({yeni} yeni), {len(adlar) - len(eski)} eşleşmeyen')


if __name__ == '__main__':
    main()
