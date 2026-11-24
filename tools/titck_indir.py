#!/usr/bin/env python3
"""TİTCK monograflarını bir kere indirir, yerelde önbelleğe alır, kayıtlarımızla karşılaştırır.

Neden var: TİTCK monografları yılda bir değişiyor; her seferinde siteye gitmenin anlamı yok.
PDF'ler ve metinleri `veri/onbellek/titck/` altında kalır (git'e girmez — belgeler TİTCK'in,
depo herkese açık). Depoya yalnız çıkan bulgu girer: hangi kayıtta hangi uyarı eksik.

  python3 tools/titck_indir.py indir    # 143 monografı indir (bir kere; ~3 dk)
  python3 tools/titck_indir.py          # önbellekten karşılaştır, eksikleri yaz (ağa çıkmaz)
"""
import json, os, re, subprocess, sys, time
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
ONB = os.path.join(KOK, 'veri', 'onbellek', 'titck')
RAPOR = os.path.join(KOK, 'veri', 'titck_eksik.json')
# Her uyarı için: TİTCK metninde aranan kalıp, bizim metinde karşılık sayılan kalıp.
# İkincisi geniş tutulur — aynı şeyi başka sözcükle yazmışsak eksik saymayalım.
ANAHTAR = [
    ('hamilelik',       r'hamile|gebe',                 r'hamile|gebe'),
    ('emzirme',         r'emzir|laktasyon',             r'emzir|laktasyon|süt veren'),
    ('yaş sınırı',      r'\d+\s*yaş',                   r'\d+\s*yaş|çocuk|ergen|bebek'),
    ('kanser',          r'kanser',                      r'kanser|tümör|östrojen'),
    ('karaciğer',       r'karaciğer',                   r'karaciğer|hepat'),
    ('böbrek',          r'böbrek',                      r'böbrek|renal|idrar yolu'),
    ('tiroit',          r'tiroit|tiroid',               r'tiroit|tiroid|guatr'),
    ('diyabet',         r'diyabet|hipoglisem',          r'diyabet|şeker|kan şekeri|hipoglisem|insülin'),
    ('tansiyon',        r'tansiyon|hipertansi',         r'tansiyon|hipertansi|kan basınc'),
    ('glokom',          r'glokom',                      r'glokom|göz tansiyon'),
    ('ameliyat',        r'ameliyat|cerrahi',            r'ameliyat|cerrahi|operasyon|anestezi'),
    ('kısırlık',        r'infertil|kısır',              r'infertil|kısır|doğurganl'),
    ('kan sulandırıcı', r'antikoagül|varfarin',         r'antikoagül|varfarin|kan sulandır|pıhtıla|kanama'),
]

def indir():
    import titck
    os.makedirs(ONB, exist_ok=True)
    yeni = hata = 0
    for i, (la, yol) in sorted(titck.M.items()):
        pdf = os.path.join(ONB, i + '.pdf')
        if os.path.exists(pdf) and os.path.getsize(pdf) > 10000:
            continue
        ok = False
        for _ in range(3):
            r = subprocess.run(['curl', '-sS', '-m', '90', '-o', pdf, titck.B + yol], capture_output=True)
            if os.path.exists(pdf) and os.path.getsize(pdf) > 10000: ok = True; break
            time.sleep(4)
        if ok: yeni += 1
        else: hata += 1; print('inemedi:', i)
        time.sleep(0.4)
    for f in sorted(os.listdir(ONB)):
        if f.endswith('.pdf'):
            t = os.path.join(ONB, f[:-4] + '.txt')
            if not os.path.exists(t):
                subprocess.run(['pdftotext', '-layout', os.path.join(ONB, f), t], capture_output=True)
    print(f'{yeni} yeni indirildi, {hata} inemedi, önbellek: {ONB}')
    return 0

def metin(i):
    p = os.path.join(ONB, i + '.txt')
    if not os.path.exists(p): return ''
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'GÜVENL[İI]L[İI]KLE(.*?)LİTERATÜR', t, re.S) or re.search(r'GÜVENL[İI]L[İI]KLE(.*)', t, re.S)
    return ' '.join((m.group(1) if m else t).split()).lower()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'indir': return indir()
    if not os.path.isdir(ONB):
        print('önbellek yok; önce: python3 tools/titck_indir.py indir'); return 1
    import kuyruk
    P = {p['id']: p for p in json.load(open(os.path.join(KOK, 'data.json')))['P']}
    P.update({q['id']: q for q in kuyruk.Q})
    rapor, bakilan = {}, 0
    for i in sorted(P):
        t = metin(i)
        if not t: continue
        bakilan += 1
        biz = ' '.join(str(P[i].get(k, '')) for k in ('guvNot', 'haz', 'etk')).lower()
        eksik = [ad for ad, rx_t, rx_b in ANAHTAR if re.search(rx_t, t) and not re.search(rx_b, biz)]
        if eksik: rapor[i] = eksik
    json.dump(rapor, open(RAPOR, 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    print(f'{bakilan} monograf okundu (ağa çıkılmadı), {len(rapor)} kayıtta eksik uyarı')
    for i, v in sorted(rapor.items(), key=lambda x: -len(x[1]))[:20]:
        print(f'  {i:18s} {", ".join(v)}')
    if len(rapor) > 20: print(f'  … toplam {len(rapor)}; tamamı {os.path.relpath(RAPOR, KOK)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
