#!/usr/bin/env python3
"""Kaydın mekanik alanlarını yazar, yargı gerektirenleri boş bırakır.

Eda'nın sorusu (25 Kasım 2026): "Yazı hep aynı formda ilerlemiyor mu, neden
onu da otomatikleştiremiyoruz?" — Formu evet, yargıyı hayır.

Otomatik yazılanlar, hepsi doğrulanabilir olgular:
  la, taxon, fam        Kew WCVP'den, Türkçe familya adı kendi tablomuzdan
  kanit                 EMA sonucuna göre 'monograf' ya da 'geleneksel'
  ek.yetisme            WCVP yayılış listesinden
  ek.mevsim             Türkiye'de yetişmiyorsa standart cümle
  ek.yoresel            Türkçe adı yoksa standart cümle
  ek.karisma            aynı cinsten kayıt varsa tür-düzeyi uyarısı
  diger                 monograf durumu cümlesi
  haz, bilim            monograf/klinik çalışma yoksa açılış cümlesi
  kaynak                WCVP + seçilen PubMed künyeleri
  rel                   aynı cinsten mevcut kayıtlar
  en.*                  yukarıdakilerin birebir İngilizcesi

Boş bırakılanlar — kaynak okunmadan yazılamaz:
  kul, bilim gövdesi, guvNot gövdesi, ilginc, kisim, kat, bolge

Mekanik kısmı yazmak kaydın yaklaşık üçte biri. Geri kalanı okumaktan,
hangi kaynağın ne kadar güçlü olduğuna karar vermekten ve cümleyi o güce
göre kurmaktan ibaret; onu betik yapamaz. 25 Kasım'da adım başlıklarını
mekanik üretme denemesi "Yaprakları çıkarıp ya da süzüp iç" adımını
"Yaprakları iç" diye özetlemişti — yanlış talimat. Aynı risk burada daha
büyük: doz ve kontrendikasyon.

  python3 tools/kayit_taslak.py yerbademi "Cyperus esculentus" > /tmp/t.py
"""
import importlib.util, json, os, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
_s = importlib.util.spec_from_file_location('ad_bul', os.path.join(KOK, 'tools', 'ad_bul.py'))
ad_bul = importlib.util.module_from_spec(_s); _s.loader.exec_module(ad_bul)
_s2 = importlib.util.spec_from_file_location('kayit_iskeleti', os.path.join(KOK, 'tools', 'kayit_iskeleti.py'))
isk = importlib.util.module_from_spec(_s2); _s2.loader.exec_module(isk)

BOS = "'',  # ← KAYNAK OKUNMADAN YAZILMAZ"


def ayni_cins(tur):
    import kuyruk as K
    d = json.load(open(os.path.join(KOK, 'data.json'), encoding='utf-8'))
    c = tur.split()[0].lower()
    return [p for p in d['P'] + K.Q
            if c in (p.get('taxon') or p.get('la') or '').lower()]


def q(x):
    return "'" + str(x).replace('\\', '\\\\').replace("'", "\\'") + "'"


def taslak(pid, tur, tr_ad=''):
    w = ad_bul.coz(tur)
    if w.get('bulunamadi'):
        print(f'# ⚠️  {tur} hiçbir kaynakta bulunamadı — ad elle doğrulanmalı'); return
    ema = isk.ema_bul(tur)
    monograf = [e for e in ema if 'monograph' in (e.get('sonuc') or '').lower()
                and tur.lower() in ((e.get('tur') or '') + ' ' + (e.get('latin') or '')).lower()]
    fam = w['familya']
    fam_tr = json.load(open(os.path.join(KOK, 'veri', 'familya_tr.json'), encoding='utf-8')).get(fam, '')
    akraba = [p for p in ayni_cins(tur) if p['id'] != pid]
    kabul = w.get('kabul_ad') or w['ad']
    yazar = (w.get('kabul_yazar') or w.get('yazar') or '').strip()
    y = w['yayilis']

    mono_tr = ('Bu tür için Avrupa İlaç Ajansı monografı vardır.' if monograf else
               '**Bu türün ne Avrupa İlaç Ajansı’nda ne TİTCK’de monografı vardır.**')
    mono_en = ('The European Medicines Agency has a monograph for this species.' if monograf else
               '**Neither the European Medicines Agency nor the Turkish agency '
               'has a monograph for this species.**')
    L = []
    A = L.append
    A('    dict(')
    A("        yayin='',  # ← parti tarihi")
    A('        arsiv=True,')
    A(f'        id={q(pid)},')
    A("        foto='',")
    A(f'        tr={q(tr_ad or pid)},')
    A(f'        la={q((kabul + " " + yazar).strip())},')
    A(f'        taxon={q(kabul)},')
    A(f'        fam={q(fam + (f" ({fam_tr})" if fam_tr else ""))},')
    if not fam_tr:
        A(f'        # ⚠️  {fam} familyasının Türkçe adı veri/familya_tr.json’da yok')
    A(f'        diger={BOS}  # yöresel/yabancı adlar + şu cümle: {mono_tr}')
    A(f'        kisim={BOS}')
    A('        kat=[],    # ← sifa / ritual / tutsu / besin / zehir')
    A('        bolge=[],  # ← anadolu / asya / and / amazon / kamerika / avrupa / afrika / okyanusya')
    A('        kul=[],    # ← [başlık, metin] çiftleri; KAYNAK OKUNMADAN YAZILMAZ')
    A(f'        haz={BOS}  # monograf yoksa: “Resmî bir monografta kabul edilmiş doz yoktur.”')
    A(f'        bilim={BOS}')
    A(f"        kanit={q('monograf' if monograf else 'geleneksel')},")
    A("        guv='',    # ← dusuk / orta / yuksek")
    A(f'        guvNot={BOS}')
    A(f'        ilginc={BOS}')
    A('        ek=dict(')
    if w.get('turkiyede') is False:
        A("            mevsim='Dayanak alınan kaynaklarda Türkiye için bir toplama '")
        A("                   'takvimi yoktur; bitki Türkiye’de doğal olarak yetişmez.',")
        A("            yoresel='Türkçede yerleşik bir yöresel adı yok.',")
    else:
        A(f'            mevsim={BOS}')
        A(f'            yoresel={BOS}')
    if y:
        ilk = ', '.join(y[:10]) + ('…' if len(y) > 10 else '')
        A(f"            yetisme='Kew’in kayıtlarına göre yayılışı {len(y)} bölgeyi kapsar: {ilk}. '")
        A("                    '',  # ← habitatı bir cümleyle ekle")
    else:
        A(f'            yetisme={BOS}')
    if akraba:
        ad = ', '.join(f"{p.get('tr','?')} (*{p.get('taxon') or p.get('la')}*)" for p in akraba[:3])
        A(f"            karisma='{ad} ile aynı cinstendir ama ayrı türdür; bir türün '")
        A("                    'monografı ve kısıtlamaları akrabasına ait değildir.',")
    else:
        A("            karisma='',")
    A('        ),')
    A('        kaynak=[')
    A(f"            ['{kabul} {yazar}, World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',")
    A("             'https://powo.science.kew.org/'],")
    for k in isk.pubmed(tur)[:5]:
        A(f"            # [{k['havuz']}] {k['ilk_yazar']} {k['yil']} — {k['baslik'][:70]}")
        A(f"            #  {k['url']}")
    A('        ],')
    A(f"        rel={[p['id'] for p in akraba[:3]]!r},")
    A('        en=dict(')
    A(f'            name={BOS}')
    A(f'            other={BOS}  # + {mono_en}')
    A(f'            part={BOS}')
    A('            uses=[],')
    A(f'            prep={BOS}')
    A(f'            science={BOS}')
    A(f'            safety={BOS}')
    A(f'            fact={BOS}')
    if w.get('turkiyede') is False:
        A("            season='The sources relied on here give no collection calendar '")
        A("                   'for Turkey; the plant does not grow there naturally.',")
        A("            local='It has no established Turkish local name.',")
    A(f'            habitat={BOS}')
    A(f'            confusion={BOS}')
    A('        ),')
    A('    ),')
    print('\n'.join(L))


if __name__ == '__main__':
    if len(sys.argv) > 2: taslak(sys.argv[1], ' '.join(sys.argv[2:]))
    else: print(__doc__)
