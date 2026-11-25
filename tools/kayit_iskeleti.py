#!/usr/bin/env python3
"""Yeni bir bitki kaydı için kaynaklı iskelet ve araştırma özeti üretir.

Neden var (25 Kasım 2026): her kayıt için aynı beş tur ağa çıkılıyordu — Kew/GBIF'te
ad doğrulama, EMA'da monograf var mı, TİTCK'te uyarı var mı, PubMed'de künye
doğrulama. Her turun çıktısı bağlama giriyordu. Bu betik turları kendisi atar,
yalnız sonucu yazar; metni yazan insan ya da model ağa hiç çıkmaz.

  python3 tools/kayit_iskeleti.py beyazpelin "Artemisia herba-alba"
  python3 tools/kayit_iskeleti.py --parti p005        # bir partinin sekizi birden

Üretilen şey **taslaktır, yayın değildir.** Yalnız kaynağı olan alanlar doldurulur;
gerisi boş bırakılır. Betik cümle uydurmaz — EMA ve TİTCK metinlerini olduğu gibi
alıntılar, Türkçe metni yazan onları okuyup kendi cümlesini kurar.
"""
import json, os, re, subprocess, sys, time, urllib.parse

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
EMA_DIZIN = os.path.join(KOK, 'veri', 'onbellek', 'ema_index.json')
TITCK = os.path.join(KOK, 'veri', 'onbellek', 'titck')
FAM_TR = os.path.join(KOK, 'veri', 'familya_tr.json')
UA = 'BitkiTabani/1.0 (https://bitkitabani.com; iletisim@bitkitabani.com)'


def al(adres):
    r = subprocess.run(['curl', '-sL', '-m', '60', '-A', UA, adres],
                       capture_output=True, text=True, errors='replace')
    try: return json.loads(r.stdout)
    except Exception: return None


# ── 1. Ad ve familya: GBIF (Kew/WCVP kopyası) ────────────────────────────────
def ad_dogrula(latin):
    d = al('https://api.gbif.org/v1/species/match?strict=false&name=' + urllib.parse.quote(latin))
    if not d or d.get('matchType') == 'NONE':
        return {'uyari': f'GBIF {latin} adını tanımadı — ad elle doğrulanmalı'}
    return {
        'kabul_ad': d.get('canonicalName'), 'yazar': d.get('scientificName'),
        'familya': d.get('family'), 'cins': d.get('genus'),
        'durum': d.get('status'), 'guven': d.get('confidence'),
        'gbif': f"https://www.gbif.org/species/{d.get('usageKey')}",
    }


# ── 2. EMA: yerel monograf dizininden tür eşlemesi ──────────────────────────
def ema_bul(tur):
    if not os.path.exists(EMA_DIZIN):
        return [{'uyari': 'ema_index.json yok — önce tools/ema_monograf.py çalıştır'}]
    d = json.load(open(EMA_DIZIN, encoding='utf-8'))
    cins = tur.split()[0].lower()
    out = []
    for ad, k in d.items():
        alan = ((k.get('tur') or '') + ' ' + (k.get('latin') or '')).lower()
        if tur.lower() in alan or (cins and cins in alan):
            out.append(k | {'slug': ad})
    return out


# ── 3. TİTCK: yerel monograf metinlerinde cins/tür araması ──────────────────
def titck_bul(tur):
    if not os.path.isdir(TITCK): return []
    cins = tur.split()[0]
    out = []
    for f in sorted(os.listdir(TITCK)):
        if not f.endswith('.txt'): continue
        m = open(os.path.join(TITCK, f), encoding='utf-8', errors='replace').read()
        if cins.lower() in m.lower():
            # Tam tür geçiyorsa güçlü, yalnız cins geçiyorsa kontrol gerektirir
            out.append({'dosya': f[:-4], 'tam_tur': tur.lower() in m.lower(),
                        'parca': re.sub(r'\s+', ' ', m[max(0, m.lower().find(cins.lower()) - 200):][:700])})
    return out


# ── 4. PubMed: doğrulanmış künyeler (uydurma atıf olmasın diye) ─────────────
def pubmed(tur, adet=4):
    """Derleme ve klinik çalışmaları ayrı ayrı arar.

    Kayıtlarımızın atıf yaptığı şey bunlar; düz arama laboratuvar ve ziraat
    yazılarıyla doluyor. Sonuçlar 'tur' alanıyla gelir, hangi havuzdan geldiği
    yazılır — kanıt düzeyini yazan buna bakar.
    """
    ids, nereden = [], {}
    for etiket, suz in (('derleme', 'AND (review[pt] OR systematic[sb] OR meta-analysis[pt])'),
                        ('klinik',  'AND (clinical trial[pt] OR randomized controlled trial[pt])'),
                        ('genel',   '')):
        q = f'"{tur}"[Title/Abstract] {suz}'.strip()
        r = al('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json'
               f'&sort=relevance&retmax={adet}&term=' + urllib.parse.quote(q))
        for i in (((r or {}).get('esearchresult') or {}).get('idlist') or []):
            if i not in nereden: nereden[i] = etiket; ids.append(i)
        time.sleep(0.4)
    if not ids: return []
    time.sleep(0.4)
    d = al('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=' + ','.join(ids))
    r = (d or {}).get('result') or {}
    out = []
    for i in ids:
        k = r.get(i) or {}
        if not k: continue
        yz = (k.get('authors') or [{}])[0].get('name', '')
        out.append({'pmid': i, 'ilk_yazar': yz, 'yil': (k.get('pubdate') or '')[:4],
                    'baslik': k.get('title', ''), 'dergi': k.get('source', ''),
                    'havuz': nereden.get(i, ''),
                    'url': f'https://pubmed.ncbi.nlm.nih.gov/{i}/'})
    return out


def mevcut_mu(tur):
    """Latince ada göre mükerrer taraması — kural: önce Latince ad, metin benzerliği değil."""
    import kuyruk as K
    d = json.load(open(os.path.join(KOK, 'data.json'), encoding='utf-8'))
    t = tur.split()[0].lower()
    return [p['id'] for p in d['P'] + K.Q
            if t in ((p.get('taxon') or p.get('la') or '')).lower()]


def iskelet(pid, tur, ek=None):
    ek = ek or {}
    ad = ad_dogrula(tur)
    fam = ad.get('familya') or ''
    fam_tr = json.load(open(FAM_TR, encoding='utf-8')).get(fam, '')
    ema = ema_bul(tur)
    return {
        'id': pid, 'tur_sorgu': tur,
        'ad': ad,
        'familya_tr': f'{fam} ({fam_tr})' if fam_tr else fam + '  ← Türkçe familya adı veri/familya_tr.json’da yok',
        'mukerrer_adaylari': mevcut_mu(tur),
        'ema': ema,
        'titck': titck_bul(tur),
        'pubmed': pubmed(tur),
        'parti': ek,
    }


def yaz(k):
    a = k['ad']
    print('=' * 72)
    print(f"{k['id']}  ·  {k['tur_sorgu']}")
    print('-' * 72)
    if a.get('uyari'): print('⚠️ ', a['uyari'])
    else: print(f"kabul ad : {a['yazar']}  [{a['durum']}, güven {a['guven']}]\nfamilya  : {k['familya_tr']}\ngbif     : {a['gbif']}")
    if k['mukerrer_adaylari']:
        print('⚠️  aynı cinsten kayıt var:', ', '.join(k['mukerrer_adaylari']), '— tür düzeyinde kontrol et')
    print(f"\nEMA  : {len(k['ema'])} eşleşme")
    for e in k['ema'][:4]:
        if e.get('uyari'): print('  ⚠️ ', e['uyari']); continue
        print(f"  · {e.get('latin')} — {e.get('sonuc')}")
        print(f"    {e.get('sayfa')}")
        for alan in ('endikasyon', 'dozaj', 'kontrendikasyon', 'uyari', 'etkilesim', 'gebelik'):
            if e.get(alan): print(f"    [{alan}] {e[alan][:400]}")
    print(f"\nTİTCK: {len(k['titck'])} dosyada cins geçiyor")
    for t in k['titck'][:4]:
        print(f"  · {t['dosya']} {'(tam tür)' if t['tam_tur'] else '(yalnız cins — kontrol et)'}")
        print(f"    {t['parca'][:300]}")
    print(f"\nPubMed: {len(k['pubmed'])} künye (NCBI’den doğrulandı)")
    for p in k['pubmed']:
        print(f"  · [{p['havuz']}] {p['ilk_yazar']} {p['yil']}. {p['baslik'][:88]} — {p['dergi']} · {p['url']}")
    print("""
TASLAK ALANLAR — yalnız kaynağı olanlar doludur, gerisini yazan doldurur:
  la / taxon / fam  : yukarıdaki GBIF satırından
  ema               : yukarıdaki EMA eşleşmesinden (tür düzeyinde doğrula)
  kanit             : EMA sonucu 'monograph' ise 'monograf', değilse 'geleneksel'
  kul/bilim/guvNot/haz/diger : KAYNAK OKUNMADAN YAZILMAZ
""")


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--parti':
        f = os.path.join(KOK, 'veri', 'parti', sys.argv[2] + '.txt')
        for s in open(f, encoding='utf-8'):
            if s.startswith('#') or '|' not in s: continue
            p = [x.strip() for x in s.split('|')]
            yaz(iskelet(p[0], p[1], {'onerilen_tr': p[2], 'bolge': p[3], 'kat': p[4]}))
            time.sleep(1)
    elif len(sys.argv) > 2:
        yaz(iskelet(sys.argv[1], ' '.join(sys.argv[2:])))
    else:
        print(__doc__)
