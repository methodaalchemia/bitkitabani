#!/usr/bin/env python3
"""Kardeş tür adaylarını eler: hangi aday kendi kaydını hak ediyor, hangisi paragraf olmalı.

Neden var (26 Kasım 2026, Eda'nın tespiti): aday listesi botanik kümelemeyle
kuruldu, kümeleme kardeş türleri kendiliğinden içine çekiyor. Mükerrer taraması
Latince adla çalıştığı için üç ayrı tür hiç alarm vermiyor — kayıtlar birbirinin
kopyası gibi okunsa bile. Parti 008'de üç ayrı "limon kokulu" tür yan yana geldi.

Ölçüt (Eda, 26 Kasım): bir aday şu üçünden en az birini geçmezse kendi kaydı
olmaz, akrabasının kaydında paragraf olur.
  1. Kendine ait monograf ya da kendine ait klinik literatür.
  2. Kendine ait kültürel hikâye — adı konmuş kullanım, adı konmuş kültürde.
  3. Okurun bilmesi gereken kendine ait ayrım (güvenlik farkı, karıştırma riski).

Bu betik yalnız 1. ölçütü makineyle sınar ve 2 ile 3'ün insan gözüyle
bakılacağı kısa listeyi çıkarır. Kümede olmak tek başına kusur değil:
kayısı, kiraz, vişne, erik aynı cinstendir ve ayrı yiyeceklerdir.

  python3 tools/kume_denetim.py                 # p009'dan sonrası
  python3 tools/kume_denetim.py --from p020
  python3 tools/kume_denetim.py --tsv > veri/kume_denetim.tsv
"""
import glob, json, os, re, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASLA = 'p009'
for i, a in enumerate(sys.argv):
    if a == '--from' and i + 1 < len(sys.argv): BASLA = sys.argv[i + 1]
TSV = '--tsv' in sys.argv

# ── katalogdaki kayıtlar: cins → [(id, Latince)] ──────────────────────────
sys.path.insert(0, KOK)
import kuyruk
KAYIT = []
# Katalog iki kaynaktan geliyor: data.json (yayımda olan kayıtlar) ve
# kuyruk.Q (toplu eklenenler). build.py de böyle birleştiriyor.
_d = json.load(open(os.path.join(KOK, 'data.json'), encoding='utf-8'))
BILGI = {}
for p in list(_d.get('P') or []) + list(kuyruk.Q):
    if not isinstance(p, dict) or not p.get('la'): continue
    KAYIT.append((p.get('id', ''), p['la']))
    BILGI[p.get('id', '')] = {'tr': p.get('tr', ''),
                              'bolge': set(p.get('bolge') or []),
                              'kat': set(p.get('kat') or [])}

def cins(latin):
    t = re.sub(r'^[×x]\s*', '', (latin or '').strip())
    g = t.split()[0] if t.split() else ''
    return g.rstrip(',')

KATALOG = {}
for kid, kla in KAYIT:
    KATALOG.setdefault(cins(kla), []).append((kid, kla))

def tur(latin):
    """'Eucalyptus citriodora Hook.' → 'eucalyptus citriodora'"""
    t = re.sub(r'^[×x]\s*', '', (latin or '').strip()).split()
    t = [w for w in t if not w.startswith('(')]
    return ' '.join(t[:2]).lower().rstrip('.,')

# ── EMA: monograf metinlerinden ikili adları çıkar ────────────────────────
EMA = {}
yol = os.path.join(KOK, 'veri', 'onbellek', 'ema_index.json')
if os.path.exists(yol):
    d = json.load(open(yol, encoding='utf-8'))
    for k, v in d.items():
        s = json.dumps(v, ensure_ascii=False)
        for b in re.findall(r'\b([A-Z][a-z]{3,})\s+(?:×\s*)?([a-z]{3,})\b', s):
            EMA.setdefault(' '.join(b).lower(), set()).add(k)

# ── TİTCK: monograf metinlerinde ikili ad aranır ──────────────────────────
TITCK = {}
for f in glob.glob(os.path.join(KOK, 'veri', 'onbellek', 'titck', '*.txt')):
    s = open(f, encoding='utf-8', errors='ignore').read()
    ad = os.path.basename(f)[:-4]
    for b in re.findall(r'\b([A-Z][a-z]{3,})\s+(?:×\s*)?([a-z]{3,})\b', s):
        TITCK.setdefault(' '.join(b).lower(), set()).add(ad)

# ── adaylar ───────────────────────────────────────────────────────────────
dosyalar = sorted(glob.glob(os.path.join(KOK, 'veri', 'parti', 'p*.txt')))
dosyalar = [f for f in dosyalar if os.path.basename(f)[:-4] >= BASLA]
aday = []
for f in dosyalar:
    parti = os.path.basename(f)[:-4]
    for satir in open(f, encoding='utf-8'):
        if satir.startswith('#') or '|' not in satir: continue
        p = [x.strip() for x in satir.split('|')]
        if len(p) < 3: continue
        aday.append({'parti': parti, 'id': p[0], 'la': p[1], 'tr': p[2],
                     'bolge': p[3] if len(p) > 3 else '',
                     'kat': p[4] if len(p) > 4 else ''})

sayac = {}
for a in aday: sayac[cins(a['la'])] = sayac.get(cins(a['la']), 0) + 1

satirlar, ozet = [], {'AYRI': 0, 'GÖZDEN GEÇİR': 0, 'TEK': 0}
for a in aday:
    g = cins(a['la']); t = tur(a['la'])
    akraba = KATALOG.get(g, [])
    kume = sayac.get(g, 1)
    if kume < 2 and not akraba:
        ozet['TEK'] += 1; continue           # kümede değil, soru yok

    e_tur = sorted(EMA.get(t, ()))
    t_tur = sorted(TITCK.get(t, ()))
    # akrabanın monografı bu adayı da kapsıyor mu
    paylasilan = []
    for kid, kla in akraba:
        kt = tur(kla)
        ortak = (set(EMA.get(kt, ())) & set(e_tur)) | (set(TITCK.get(kt, ())) & set(t_tur))
        if ortak: paylasilan.append(f"{kid}:{','.join(sorted(ortak))}")

    if (e_tur or t_tur) and not paylasilan:
        karar = 'AYRI'                       # kendi monografı var, paylaşmıyor
    elif akraba:
        karar = 'GÖZDEN GEÇİR'               # kendi dayanağı yok, akrabası yayında
    else:
        karar = 'AYRI'                       # cinsinin ilki; kayıt açılır
    # ── İkinci katman ──────────────────────────────────────────────────
    # 1. ölçüt tek başına çok kaba: pırasa, lahana, tarhun ve köygöçüren de
    # "kendi monografı yok" diye işaretleniyor, oysa hepsi ayrı kayıt olmayı
    # hak ediyor. Gerçek yakın-kopya üç işareti birden taşıyor: Türkçe adı
    # akrabanın adının önüne sıfat eklenmiş hali, aynı bölge, aynı kategori.
    isaret = []
    if karar == 'GÖZDEN GEÇİR':
        a_bol = set(x.strip() for x in a['bolge'].split(',') if x.strip())
        a_kat = set(x.strip() for x in a['kat'].split(',') if x.strip())
        for kid, _kla in akraba:
            b = BILGI.get(kid) or {}
            ktr = (b.get('tr') or '').lower()
            atr = a['tr'].lower()
            ad_turevi = bool(ktr) and ktr in atr and atr != ktr
            ayni_bolge = bool(a_bol & (b.get('bolge') or set()))
            ayni_kat = bool(a_kat) and a_kat == (b.get('kat') or set())
            if ad_turevi and ayni_bolge and ayni_kat:
                isaret.append(f'{kid}:ad+bölge+kategori'); break
            if ad_turevi and (ayni_bolge or ayni_kat):
                isaret.append(f'{kid}:ad+' + ('bölge' if ayni_bolge else 'kategori'))
        if isaret:
            karar = 'YAKIN KOPYA'
    ozet[karar] = ozet.get(karar, 0) + 1
    satirlar.append({**a, 'cins': g, 'kume': kume, 'karar': karar,
                     'ema': ';'.join(e_tur), 'titck': ';'.join(t_tur),
                     'akraba': ';'.join(k for k, _ in akraba), 'isaret': ';'.join(isaret),
                     'paylasilan': ';'.join(paylasilan)})

if TSV:
    print('parti\tid\tlatince\tturkce\tcins\tkume\tkarar\tema\ttitck\tkatalogdaki_akraba\tpaylasilan_monograf\tisaret')
    for s in satirlar:
        print('\t'.join([s['parti'], s['id'], s['la'], s['tr'], s['cins'], str(s['kume']),
                         s['karar'], s['ema'], s['titck'], s['akraba'], s['paylasilan'], s['isaret']]))
else:
    yk = [x for x in satirlar if x['karar'] == 'YAKIN KOPYA']
    gg = [x for x in satirlar if x['karar'] == 'GÖZDEN GEÇİR']
    print(f"{BASLA}'dan sonrası: {len(aday)} aday · kümede olmayan {ozet['TEK']} "
          f"· kendi dayanağı olan {ozet['AYRI']} · yakın kopya {len(yk)} · bakılacak {len(gg)}\n")
    print(f'YAKIN KOPYA ({len(yk)}) — kendi monografı yok, akrabası katalogda,')
    print('adı akrabanın adının türevi, bölge ya da kategori de aynı:\n')
    for x in sorted(yk, key=lambda z: (z['cins'], z['la'])):
        print(f"  {x['parti']}  {x['tr']:26s} {x['la']:34s} → {x['isaret']}")
    print(f'\nBAKILACAK ({len(gg)}) — monografı yok ama adı, bölgesi ya da kategorisi ayrı;')
    print('2. ve 3. ölçüt (kültürel hikâye, güvenlik ayrımı) insan gözü ister.')
