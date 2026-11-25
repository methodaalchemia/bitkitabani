#!/usr/bin/env python3
"""Latince bitki adlarını çevrimdışı çözer — Kew WCVP'nin tam kopyasından.

Neden var (25 Kasım 2026): her kayıt için ad doğrulamaya ağa çıkılıyordu.
Kew'in Dünya Damarlı Bitkiler Kontrol Listesi (WCVP) tek dosya hâlinde
indirilebiliyor: 1.448.984 ad ve 1.995.338 yayılış kaydı. Artık ad çözümü,
familya, eş ad ve "Türkiye'de yetişir mi" sorusu ağa hiç çıkmadan yanıtlanıyor.

  python3 tools/ad_bul.py "Ziziphus lotus"
  python3 tools/ad_bul.py --parti p006        # bir partinin hepsi birden
  python3 tools/ad_bul.py --dizin             # aramayı hızlandıran dizini kurar

Veri: veri/onbellek/wcvp/ (git'e girmez; Kew'in, yeniden inebilir).
Kaynak: https://sftp.kew.org/pub/data-repositories/WCVP/
"""
import csv, json, os, pickle, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WCVP = os.path.join(KOK, 'veri', 'onbellek', 'wcvp')
TAKSON = os.path.join(WCVP, 'wcvp_taxon.csv')
DAGILIM = os.path.join(WCVP, 'wcvp_distribution.csv')
DIZIN = os.path.join(WCVP, 'ad_dizin.pkl')
csv.field_size_limit(10_000_000)


def dizin_kur():
    """Adları ve yayılışı belleğe alınabilir tek bir dosyaya indirger.

    Ham CSV 1,4 milyon satır; her sorguda baştan taranması gereksiz. Dizin
    yalnız gereken altı alanı tutar, yaklaşık 200 MB yerine ~90 MB yer kaplar.
    """
    ad, kimlik = {}, {}
    with open(TAKSON, encoding='utf-8', errors='replace') as f:
        for r in csv.DictReader(f, delimiter='|'):
            k = r['taxonid']
            # Not: sütun adı Kew'in dosyasında "scientfiic" diye yazılmış (yazım hatası onlarda).
            kayit = (r['scientfiicname'], r['scientfiicnameauthorship'], r['family'],
                     r['taxonomicstatus'], r['acceptednameusageid'], r['taxonrank'])
            kimlik[k] = kayit
            ad.setdefault(r['scientfiicname'].lower(), []).append(k)
    dag = {}
    with open(DAGILIM, encoding='utf-8', errors='replace') as f:
        for r in csv.DictReader(f, delimiter='|'):
            dag.setdefault(r['coreid'], []).append((r['locality'], r['establishmentmeans']))
    with open(DIZIN, 'wb') as f:
        pickle.dump({'ad': ad, 'kimlik': kimlik, 'dag': dag}, f, protocol=5)
    print(f'dizin kuruldu: {len(kimlik)} ad, {len(dag)} taksonun yayılışı → {DIZIN}')


_D = None
def yukle():
    global _D
    if _D is None:
        if not os.path.exists(DIZIN): dizin_kur()
        _D = pickle.load(open(DIZIN, 'rb'))
    return _D


def gbif(latin):
    """WCVP yalnız damarlı bitkileri kapsar. Mantar, liken, alg ve kara yosunu
    orada yoktur — onlar için GBIF'e tek sorgu. Dönen 'alem' alanı aynı zamanda
    "bu bitki değil" bilgisini verir."""
    import json as _j, subprocess as _sp, urllib.parse as _u
    r = _sp.run(['curl', '-sL', '-m', '45', '-A', 'BitkiTabani/1.0 (https://bitkitabani.com)',
                 'https://api.gbif.org/v1/species/match?strict=false&name=' + _u.quote(latin)],
                capture_output=True, text=True, errors='replace')
    try: d = _j.loads(r.stdout)
    except Exception: d = None
    if not d or d.get('matchType') == 'NONE':
        return {'bulunamadi': latin}
    o = {'sorgu': latin, 'ad': d.get('canonicalName') or latin,
         'yazar': d.get('scientificName', ''), 'familya': d.get('family', ''),
         'durum': d.get('status', ''), 'rank': d.get('rank', ''),
         'alem': d.get('kingdom', ''), 'kaynak': 'GBIF', 'taxonid': str(d.get('usageKey', '')),
         'eslesme_sayisi': 1, 'yayilis': [], 'turkiyede': None}
    if (d.get('status') or '').upper() == 'SYNONYM' and d.get('species'):
        o['kabul_ad'] = d['species']; o['kabul_yazar'] = ''
    return o


def coz(latin):
    d = yukle()
    anahtar = latin.strip().lower()
    def dene(a):
        return d['ad'].get(a)
    ids = dene(anahtar)
    if not ids:
        # Tür altı ek olmadan dene (ör. "Thymus vulgaris L." → "Thymus vulgaris")
        anahtar = ' '.join(latin.split()[:2]).lower()
        ids = dene(anahtar)
    if not ids:
        # Melez işareti: WCVP kültür bitkilerinin çoğunu melez olarak yazıyor
        # (Citrus × limon, Musa × paradisiaca, Chrysanthemum × morifolium).
        # Bizdeki listelerde işaret yok; iki yönde de dene.
        par = anahtar.split()
        if len(par) >= 2 and '×' not in anahtar:
            ids = dene(f'{par[0]} × {par[1]}') or dene(f'{par[0]} x {par[1]}')
        if not ids and '×' in anahtar:
            ids = dene(anahtar.replace('× ', '').replace('×', ''))
    if not ids: return gbif(latin)
    # Aynı ad birden çok kayıtla eşleşebilir (eş adlar, gayrimeşru adlar).
    # Sıra: kabul edilen ad > kabul adı aynı cinste olan eş ad > kalanı.
    # Bu olmadan "Sorghum bicolor" gayrimeşru bir kayda düşüp
    # Hyparrhenia dichroa'ya yönleniyordu.
    cins_sorgu = anahtar.split()[0]
    def oncelik(x):
        _ad, _yz, _fm, _dr, _kb, _rk = d['kimlik'][x]
        if _dr.lower() == 'accepted': return 0
        if _kb and _kb in d['kimlik'] and d['kimlik'][_kb][0].lower().startswith(cins_sorgu): return 1
        if 'illegitimate' in _dr.lower() or 'invalid' in _dr.lower(): return 3
        return 2
    ids = sorted(ids, key=oncelik)
    k = ids[0]
    ad, yazar, fam, durum, kabul_id, rank = d['kimlik'][k]
    sonuc = {'sorgu': latin, 'ad': ad, 'yazar': yazar, 'familya': fam,
             'durum': durum, 'rank': rank, 'taxonid': k, 'eslesme_sayisi': len(ids)}
    if durum.lower() != 'accepted' and kabul_id and kabul_id in d['kimlik']:
        kad, kyazar, kfam, _, _, _ = d['kimlik'][kabul_id]
        sonuc['kabul_ad'] = kad
        sonuc['kabul_yazar'] = kyazar
        sonuc['familya'] = kfam or fam
        k = kabul_id
    yer = d['dag'].get(k, [])
    sonuc['yayilis'] = sorted({a for a, _ in yer})
    sonuc['turkiyede'] = any('Turkey' in a for a, _ in yer)
    return sonuc


def yaz(s):
    if s.get('bulunamadi'):
        print(f'⚠️  WCVP {s["bulunamadi"]} adını tanımadı — elle doğrula'); return
    fam_tr = json.load(open(os.path.join(KOK, 'veri', 'familya_tr.json'), encoding='utf-8')).get(s['familya'], '')
    print(f'{s["sorgu"]}')
    if s.get('kabul_ad'):
        print(f'  ⚠️  {s["durum"]} — kabul edilen ad: {s["kabul_ad"]} {s["kabul_yazar"]}')
    else:
        print(f'  {s["ad"]} {s["yazar"]}  [{s["durum"]}, {s["rank"]}]')
    if s.get('alem') and s['alem'] != 'Plantae':
        print(f'  ⚠️  ALEM: {s["alem"]} — damarlı bitki değil (kaynak GBIF)')
    print(f'  familya : {s["familya"]}' + (f' ({fam_tr})' if fam_tr else '  ← Türkçesi tabloda yok'))
    y = s['yayilis']
    print(f'  yayılış : {len(y)} bölge' + (f' — {", ".join(y[:10])}' + ('…' if len(y) > 10 else '') if y else ' (kayıt yok)'))
    # WCVP yayılışı doğal ve yabanileşmiş alanları verir, tarımını değil.
    # "hayır" demek "Türkiye'de yetiştirilmiyor" demek değildir — buğday da
    # listede Türkiye'yi doğal alan olarak taşımaz.
    print(f'  Türkiye : {"evet" if s["turkiyede"] else "hayır (doğal yayılış; tarımı ayrı)"}')
    if s['eslesme_sayisi'] > 1:
        print(f'  ⚠️  bu ad {s["eslesme_sayisi"]} kayıtla eşleşti — eş adlı taksonlar olabilir')


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else ''
    if a == '--dizin': dizin_kur()
    elif a == '--parti':
        f = os.path.join(KOK, 'veri', 'parti', sys.argv[2] + '.txt')
        for s in open(f, encoding='utf-8'):
            if s.startswith('#') or '|' not in s: continue
            p = [x.strip() for x in s.split('|')]
            print(f'--- {p[0]}'); yaz(coz(p[1])); print()
    elif a: yaz(coz(' '.join(sys.argv[1:])))
    else: print(__doc__)
