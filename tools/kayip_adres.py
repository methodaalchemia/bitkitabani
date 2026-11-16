#!/usr/bin/env python3
"""Bir zamanlar yayında olup bugün 404 veren adresleri bulur.

Google bir adresi dizine aldıktan sonra uzun süre tekrar ziyaret ediyor.
Sayfa aradan kalkmışsa her ziyaret bir "404" uyarısı doğuruyor ve uyarılar
günler sonra, damla damla geliyor — yani Search Console sorunu haftalar
sonra haber veriyor. Bu araç aynı şeyi depodan, anında çıkarıyor:
geçmişte `site/` klasöründe bulunmuş her adresi bugünküyle karşılaştırıp
aradaki farkı üç kümeye ayırıyor.

1. **Kendiliğinden dönecek.** Yayın tarihi ileride olan kuyruk ve kavram
   sayfaları. Bunlar bir kez canlıya sızmış (5 Kasım'daki `BT_DAY`
   kazası) ve geri çekilmiş; tarihleri gelince dönecekler. Yönlendirme
   gerekmez, hatta yanlış olur.
2. **Yönlendirmesi var.** `_redirects` karşılıyor, sorun yok.
3. **Açıkta.** Ne dönecek ne yönlendiriliyor — gerçek 404. Düzeltilmesi
   gereken küme budur.

Çalıştırma:  python3 tools/kayip_adres.py [--gun 30]
Çıkış kodu açıkta adres varsa 1, yoksa 0.
"""
import argparse
import os
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)


def ko(komut):
    return subprocess.run(komut, shell=True, capture_output=True, text=True,
                          cwd=KOK).stdout


def sayfalar(commit):
    """Bir commit'teki site adreslerinin kümesi."""
    out = set()
    for x in ko(f'git ls-tree -r --name-only {commit} site').split('\n'):
        if x.endswith('index.html'):
            out.add('/' + x[len('site/'):-len('index.html')])
    return out


def bekleyenler():
    """Yayın tarihi ileride olduğu için henüz üretilmeyen sayfaların son eki."""
    bek = set()
    try:
        import kuyruk
        bek |= {q['id'] for q in kuyruk.Q}
    except Exception as ex:
        print('kuyruk okunamadı:', ex)
    try:
        import kavramlar
        bek |= {k['slug'] for k in kavramlar.KAVRAMLAR}
        # İngilizce kavram sayfaları ayrı slug taşıyor: en/kavram_en.py
        # Türkçe slug'ı anahtar, İngilizce slug'ı değerin içinde tutuyor.
        try:
            sys.path.insert(0, os.path.join(KOK, 'en'))
            import kavram_en
            for ad in dir(kavram_en):
                o = getattr(kavram_en, ad)
                if not isinstance(o, dict):
                    continue
                for v in o.values():
                    if isinstance(v, dict) and v.get('slug'):
                        bek.add(v['slug'])
        except Exception as ex:
            print('İngilizce kavramlar okunamadı:', ex)
    except Exception as ex:
        print('kavramlar okunamadı:', ex)
    return bek


def canli_404(yol, alan='https://bitkitabani.com'):
    """Adres canlıda gerçekten 404 mü?

    Depo geçmişi tek başına yetmiyor: `site/` klasöründe üretilmeyen ama
    canlıda duran sayfalar var (örnek: /ig/, Worker'a ayrıca yüklenmiş
    noindex bir önizleme sayfası). Böyle bir adrese yönlendirme eklemek
    çalışan sayfayı kırar. Bu yüzden açıkta görünen her adres canlıya
    sorulur. Ağ hatasında None döner — karar verilmez.
    """
    import urllib.error
    import urllib.parse
    import urllib.request
    u = alan + urllib.parse.quote(yol, safe='/')
    try:
        r = urllib.request.urlopen(urllib.request.Request(
            u, headers={'User-Agent': 'bitkitabani-kayip-adres/1.0'}), timeout=30)
        return r.status == 404
    except urllib.error.HTTPError as e:
        return e.code == 404
    except Exception:
        return None


def yonlendirmeler():
    yol = os.path.join(KOK, 'site', '_redirects')
    if not os.path.exists(yol):
        return set()
    return {l.split()[0] for l in open(yol, encoding='utf-8')
            if l.strip() and not l.startswith('#')}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gun', type=int, default=40,
                    help='kaç günlük geçmiş taransın (varsayılan 40)')
    a = ap.parse_args()
    ko('git config core.quotePath false')
    commitler = ko(f"git log --since='{a.gun} days ago' --format=%H").split()
    if not commitler:
        print('tarihe uyan commit yok'); return 0
    print(f'{len(commitler)} commit taranıyor')
    bugun = sayfalar('HEAD')
    gormus = set()
    for c in commitler:
        gormus |= sayfalar(c)
    kayip = sorted(gormus - bugun)
    bek, yon = bekleyenler(), yonlendirmeler()

    donecek, yonlu, acik = [], [], []
    for y in kayip:
        son = y.strip('/').split('/')[-1]
        if son in bek:
            donecek.append(y)
        elif y in yon or y.replace(' ', '%20') in yon:
            yonlu.append(y)
        else:
            acik.append(y)

    print(f'\nbugün {len(bugun)} sayfa; geçmişte görülüp bugün olmayan {len(kayip)}')
    print(f'  kendiliğinden dönecek (yayın tarihi ileride) : {len(donecek)}')
    print(f'  yönlendirmesi var                            : {len(yonlu)}')
    print(f'  AÇIKTA (gerçek 404)                          : {len(acik)}')
    if acik:
        print('\n  açıktakiler canlıya soruluyor...')
    gercek, yanlis_alarm, bilinmeyen = [], [], []
    for y in acik:
        d = canli_404(y)
        (gercek if d else (bilinmeyen if d is None else yanlis_alarm)).append(y)
    for y in gercek:
        print('      404 :', y)
    for y in yanlis_alarm:
        print('      canlıda duruyor, yönlendirme EKLEME:', y)
    for y in bilinmeyen:
        print('      canlıya sorulamadı (ağ):', y)
    acik = gercek
    if acik:
        print('\nBu adresler için site/_redirects\'e 301 eklenmeli '
              '(build.py içindeki _ESKI_ADRES listesi).')
    return 1 if acik else 0


if __name__ == '__main__':
    sys.exit(main())
