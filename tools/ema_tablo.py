#!/usr/bin/env python3
"""EMA'nın bitkisel ilaç tablosunu indirir ve kayıtlarımızla karşılaştırır.

Neden var: 24 Kasım 2026'da iki kayıtta "EMA bu tür için monograf kabul etmemiş"
yazıyordu, oysa monograf vardı (ıhlamur, karanfil). Bu tablo EMA'nın kendi günlük
çıktısı ve "Outcome of European assessment" sütunu tam bu soruyu yanıtlıyor:
monograf mı, kamuoyu açıklaması mı. Tür düzeyinde bakar — Tilia platyphyllos'un
monografı var, Tilia tomentosa'nın yok; ikisi ayrı satır.

Kullanım:
  python3 tools/ema_tablo.py indir     # tabloyu tazele (veri/onbellek/ema-herbal.xlsx)
  python3 tools/ema_tablo.py           # kayıtlarla karşılaştır, çelişkileri yaz
"""
import json, os, re, sys, subprocess
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
DOSYA = os.path.join(KOK, 'veri', 'onbellek', 'ema-herbal.xlsx')  # git'e girmez; tools/ema_tablo.py indir ile tazelenir
ADRES = 'https://www.ema.europa.eu/en/documents/report/medicines-output-herbal_medicines-report_en.xlsx'
UA = 'Mozilla/5.0 (compatible; bitkitabani/1.0; +https://bitkitabani.com)'

def indir():
    os.makedirs(os.path.dirname(DOSYA), exist_ok=True)
    for _ in range(4):   # EMA sık 429 veriyor, birkaç deneme gerekiyor
        r = subprocess.run(['curl', '-sL', '-m', '90', '-A', UA, '-o', DOSYA, '-w', '%{http_code}', ADRES],
                           capture_output=True, text=True)
        if r.stdout.strip() == '200' and os.path.getsize(DOSYA) > 50000:
            print('indirildi:', os.path.getsize(DOSYA), 'bayt'); return 0
        subprocess.run(['sleep', '25'])
    print('indirilemedi (EMA 429 veriyor olabilir); eski kopya kullanılacak'); return 1

def tablo():
    import openpyxl
    s = openpyxl.load_workbook(DOSYA, read_only=True).active
    satir = [r[:8] for r in s.iter_rows(min_row=9, values_only=True)]
    out = []
    for r in satir[1:]:
        if not r[3]: continue
        turler = [re.sub(r'\s+', ' ', t).strip() for t in str(r[3]).split(';')]
        out.append({'drog': r[0], 'turler': turler, 'sonuc': r[6] or ''})
    return out

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'indir': return indir()
    if not os.path.exists(DOSYA): return indir() or main()
    T = tablo()
    import kuyruk
    P = {p['id']: p for p in json.load(open(os.path.join(KOK, 'data.json')))['P']}
    P.update({q['id']: q for q in kuyruk.Q})
    cins = lambda t: ' '.join(re.sub(r'[×x]\s*', '', t).split()[:2]).lower()
    ema = {}
    for r in T:
        for t in r['turler']:
            ema.setdefault(cins(t), []).append((r['drog'], r['sonuc']))
    bulgu = 0
    for i, p in sorted(P.items()):
        metin = ' '.join(str(p.get(k, '')) for k in ('haz', 'guvNot', 'diger'))
        iddia_yok = re.search(r'EMA[^.]{0,80}(monograf[ıi] yok|monograf kabul etmemi)', metin)
        for t in re.split(r'[,;]', p.get('la', '')):
            k = cins(t)
            if k in ema:
                mono = [d for d, s in ema[k] if 'monograph' in s.lower()]
                if iddia_yok and mono:
                    print(f'{i}: "EMA monografı yok" deniyor ama EMA tablosunda VAR → {mono[0]} ({t.strip()})')
                    bulgu += 1
    print(f'{len(T)} EMA satırı okundu, {bulgu} çelişki')
    return 1 if bulgu else 0

if __name__ == '__main__':
    sys.exit(main())
