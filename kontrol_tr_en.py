# -*- coding: utf-8 -*-
"""Türkçe–İngilizce güvenlik eşitliği kontrolü.

Neden var: Türkçe kayıtlara sonradan eklenen bir kısıtlama (yaş sınırı,
kontrendikasyon, günlük üst sınır) İngilizce kayda yansımazsa İngilizce
sayfa Türkçeden daha az güvenli hâle gelir ve bu hiçbir yerde hata
vermez. 24 Kasım 2026'da 45 kaydın 33'ünde bu olmuştu.

Kullanım:  python3 kontrol_tr_en.py
Çıkış kodu 1 ise Türkçede olup İngilizcede karşılığı olmayan kısıtlama var.
Bulgular uyarıdır, kesin hüküm değil: kalıp eşleşmesiyle çalışır, elle
okunması gerekir.
"""
import json, re, sys, os, glob, importlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'en'))

# Türkçede aranan kısıtlama kalıpları -> İngilizcede beklenen karşılık
KURAL = [
    (r'kontrendike',              r'contraindicat|must not|never',        'kontrendikasyon'),
    (r'(\d+)\s*aydan küçük',      r'\d+\s*months',                        'ay sınırı'),
    (r'(\d+)\s*yaşından küçük',   r'under[ -]\d+|aged \d+|children',      'yaş sınırı'),
    (r'erkeklerde',               r'\bmen\b|\bmale',                      'erkek kısıtlaması'),
    (r'gebeli|hamileli',          r'pregnan|miscarriage',                 'gebelik'),
    (r'emzir',                    r'breastfeed|nursing|lactat',           'emzirme'),
    (r'günlük (?:üst sınır|toplam)', r'\ba day\b|daily|per day',          'günlük sınır'),
]


def kayitlar():
    """Yayında olan bütün kayıtları (çekirdek + tarihi gelmiş kuyruk) döndürür."""
    D = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))
    out = {p['id']: p for p in D['P']}
    bugun = datetime.date.today()
    # 27 Kasım 2026: kalıp 'k*.py' idi, yani toplu eklenen a001–a008 partileri
    # (64 kayıt) TR–EN güvenlik eşitliği denetiminden hiç geçmiyordu. Parti
    # 006'da iki eşitsizlik bu yüzden makineye görünmedi: yer fıstığında çalışma
    # dönemi TR'de yanlış EN'de doğru, chaliponga'da İngilizce sayfada yasal
    # bölüm hiç yok. Kuyruktaki bütün kayıt dosyaları taranıyor.
    for f in sorted(glob.glob(os.path.join(HERE, 'kuyruk', '[ak]*.py'))):
        mod = importlib.import_module('kuyruk.' + os.path.basename(f)[:-3])
        for q in getattr(mod, 'Q', []):
            if q['id'] in out:
                continue
            if datetime.date.fromisoformat(q['yayin']) <= bugun:
                out[q['id']] = q
    return out


def ingilizce():
    EN = {}
    for n in range(1, 9):
        EN.update(importlib.import_module(f'p{n}').EN)
    for p in kayitlar().values():          # kuyruk kayıtları İngilizcesini kendi taşıyor
        if 'en' in p:
            EN.setdefault(p['id'], p['en'])
    # build_en.py'deki birebir çeviri katmanı: asıl metnin üzerine yazar, burada da yazmalı
    from birebir import EN_FIX
    for i, f in EN_FIX.items():
        if i in EN:
            EN[i] = {**EN[i], **f}
    return EN


def main():
    EN, bulgu = ingilizce(), []
    for pid, p in sorted(kayitlar().items()):
        if pid not in EN:
            continue
        tr = ' '.join(str(p.get(k, '')) for k in ('haz', 'guvNot')).lower()
        en = ' '.join(str(EN[pid].get(k, '')) for k in ('safety', 'prep', 'part')).lower()
        for tr_rx, en_rx, ad in KURAL:
            m = re.search(tr_rx, tr)
            if m and not re.search(en_rx, en):
                detay = m.group(1) if m.groups() and m.group(1) else ''
                bulgu.append((pid, ad, detay))
        # Sayı eşitliği: Türkçe hazırlama/güvenlik metnindeki her miktar İngilizcede de geçmeli.
        # Ayraçlar yok sayılır, çünkü Türkçe 1,5 yazar, İngilizce 1.5 yazar.
        YAZI = {'one': '1', 'once': '1', 'two': '2', 'twice': '2', 'three': '3', 'thrice': '3',
                'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
                'ten': '10', 'eleven': '11', 'twelve': '12'}
        def sayi(t, ing=False):
            t = t or ''
            out = {x.replace(',', '').replace('.', '') for x in re.findall(r'\d[\d.,]*\d|\d', t)}
            if ing:   # İngilizce metin sayıyı yazıyla da yazabilir: "three times", "twice"
                out |= {YAZI[w] for w in re.findall(r'[a-z]+', t.lower()) if w in YAZI}
            return out
        for alan_tr, alan_en in (('haz', 'prep'), ('guvNot', 'safety')):
            eksik = sayi(str(p.get(alan_tr, ''))) - sayi(str(EN[pid].get(alan_en, '')), ing=True)
            if eksik:
                bulgu.append((pid, f'{alan_tr}: İngilizcede geçmeyen miktar', ', '.join(sorted(eksik)[:6])))
        # Uyarı işareti: Türkçedeki ⚠️ sayısı İngilizcede de olmalı.
        for alan_tr, alan_en in (('haz', 'prep'), ('guvNot', 'safety')):
            if str(p.get(alan_tr, '')).count('⚠️') > str(EN[pid].get(alan_en, '')).count('⚠️'):
                bulgu.append((pid, f'{alan_tr}: İngilizcede eksik ⚠️ uyarısı', ''))
    # 27 Kasım 2026: yasal durum eşitliği. extra.YASAL'da olup en/misc_en.py
    # YASAL_EN'de olmayan kayıtta İngilizce sayfada "Legal status" bölümü hiç
    # basılmıyor, rozet görünmüyor ve İngilizce katalog kartı data-durum
    # taşıdığı hâlde tabloda "No specific restriction" yazıyor. Parti 006'da
    # DMT içeren chaliponga böyle geçti: Türkçe sayfada "kısıtlı", İngilizce
    # sayfada hiçbir yasal uyarı yok. Metni insan yazar; eksikliği makine söyler.
    try:
        from extra import YASAL as _Y_TR
        _p = os.path.join(HERE, 'en')
        if _p not in sys.path: sys.path.insert(0, _p)
        from misc_en import YASAL_EN as _Y_EN
        for _pid in sorted(set(_Y_TR) - set(_Y_EN)):
            bulgu.append((_pid, 'yasal durum: extra.YASAL\'da var, en/misc_en.py YASAL_EN\'de yok '
                                '— İngilizce sayfada yasal bölüm hiç basılmaz', ''))
    except Exception as _e:
        print('uyarı: yasal durum eşitliği denetlenemedi:', _e)

    if not bulgu:
        print('Türkçe–İngilizce güvenlik eşitliği: eksik kısıtlama yok.')
        return 0
    print(f'Türkçede olup İngilizcede karşılığı bulunamayan kısıtlama: {len(bulgu)}\n')
    for pid, ad, detay in bulgu:
        print(f'  {pid:18s} {ad}{" " + detay if detay else ""}')
    print('\nHer biri elle okunmalı; kalıp eşleşmesi yanlış pozitif verebilir.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
