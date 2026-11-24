#!/usr/bin/env python3
"""Toplu kayıt dosyası denetimi: python3 tools/arsiv_denetle.py kuyruk/aNNN.py"""
import sys, os, re, json, importlib.util
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOLGE = {'anadolu','avrupa','asya','afrika','kamerika','amazon','and','okyanusya'}
KAT = {'sifa','besin','ritual','zehir','tutsu'}
EN = ['name','other','part','uses','prep','science','safety','fact','season','habitat','local']
YASAK = ('wikipedia.', 'wikimedia.', 'wiki', 'webmd.', 'healthline.', 'blogspot.', 'wordpress.', 'medium.com', 'amazon.', 'verywell', 'drugs.com', 'rxlist', 'researchgate.net', 'scribd.', 'libgen', 'sci-hub', 'academia.edu')
def main(f):
    sp = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    mevcut = set(open(os.path.join(KOK, 'veri', 'mevcut_id.txt')).read().split())
    part = {}
    pf = os.path.join(KOK, 'veri', 'parti', 'p' + re.sub(r'\D', '', os.path.basename(f)) + '.txt')
    if os.path.exists(pf):
        part = {l.split('|')[0].strip() for l in open(pf) if '|' in l}
    hata = []
    for q in m.Q:
        i = q.get('id', '?')
        def h(s): hata.append(f'{i}: {s}')
        for k in ['yayin','id','foto','tr','la','fam','diger','bolge','kat','kisim','taxon','kul','haz','bilim','kanit','guv','guvNot','ilginc','ek','kaynak','rel','en']:
            if k not in q: h(f'eksik alan {k}')
        if q.get('arsiv') is not True: h('arsiv: True yok')
        if part and i not in part: h('id parti dosyasında yok')
        if i in mevcut: h('id katalogda zaten var')
        if not set(q.get('bolge', [])) <= BOLGE or not q.get('bolge'): h('bolge geçersiz')
        if not set(q.get('kat', [])) <= KAT or not q.get('kat'): h('kat geçersiz')
        if q.get('kanit') not in ('klinik','sinirli','geleneksel'): h('kanit geçersiz')
        if q.get('guv') not in ('dusuk','orta','yuksek'): h('guv geçersiz')
        if q.get('guv') in ('orta','yuksek') and not (q.get('etk') and q.get('etk_en')): h('etk / etk_en zorunlu')
        if q.get('etk') and len(q.get('etk', [])) != len(q.get('etk_en', [])): h('etk ve etk_en sayısı farklı')
        if len(q.get('kul', [])) < 2: h('kul en az 2 bölüm olmalı')
        if len(q.get('kaynak', [])) + len(q.get('ema', [])) + (1 if q.get('nccih') else 0) < 3: h('en az 3 kaynak gerekli')
        for kk in q.get('kaynak', []) + q.get('ema', []):
            if not (isinstance(kk, (list, tuple)) and len(kk) == 2 and str(kk[1]).startswith('https://')): h(f'kaynak biçimi bozuk: {kk!r:.80}'); continue
            if any(y in kk[1].lower() for y in YASAK): h(f'yasak kaynak: {kk[1]}')
        for r in q.get('rel', []):
            if r not in mevcut: h(f'rel katalogda yok: {r}')
        ek = q.get('ek', {})
        for k in ('mevsim','yetisme','yoresel'):
            if not ek.get(k): h(f'ek.{k} eksik')
        en = q.get('en', {})
        for k in EN:
            if not en.get(k): h(f'en.{k} eksik')
        if bool(ek.get('karisma')) != bool(en.get('confusion')): h('karisma / confusion eşleşmiyor')
        if len(en.get('uses', [])) != len(q.get('kul', [])): h('kul ve en.uses bölüm sayısı farklı')
        for a, b in [('haz','prep'),('bilim','science'),('guvNot','safety'),('ilginc','fact')]:
            ta, tb = str(q.get(a, '')), str(en.get(b, ''))
            if ta and tb and not (0.7 <= len(tb) / max(1, len(ta)) <= 1.45): h(f'{a}/{b} uzunluk oranı {len(tb)/len(ta):.2f} (birebir çeviri değil mi?)')
            if ta.count('**') != tb.count('**'): h(f'{a}/{b} kalın vurgu sayısı farklı')
            na = set(re.findall(r'\d+', ta)); nb = set(re.findall(r'\d+', tb))
            if len(na - nb) > 2: h(f'{a}/{b} Türkçedeki sayılar İngilizcede yok: {sorted(na - nb)[:6]}')
        for k in ('diger','ilginc'):
            if '**' in str(q.get(k, '')): h(f'{k} içinde ** olmamalı')
        tum = json.dumps(q, ensure_ascii=False)
        if re.search(r'\[\d+\]', tum): h('metinde [n] numarası var')
        if re.search(r'mucize|şifa deposu', tum, re.I): h('yasak ifade (mucize / şifa deposu)')
        if len(tum) < 6000: h(f'kayıt çok kısa ({len(tum)} karakter; hedef 9-14 bin)')
        if q.get('guv') == 'yuksek' and not re.search(r'114|112', q.get('guvNot', '')): h('yüksek riskte 114/112 uyarısı yok')
    ids = [q.get('id') for q in m.Q]
    if len(ids) != len(set(ids)): hata.append('dosyada tekrar eden id')
    print('\n'.join(hata) if hata else f'tamam: {len(m.Q)} kayıt, hata yok')
    return 1 if hata else 0
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
