#!/usr/bin/env python3
"""Aday listesindeki adları WCVP (POWO verisi, GBIF kopyası) ile karşılaştırır: kabul edilen ad, eş ad, bulunamadı.
Çıktı: veri/aday_adlar.tsv  (id, listedeki ad, durum, kabul edilen ad + yazar, familya)"""
import json, os, re, sys, glob, time, urllib.parse, urllib.request
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WCVP = 'f382f0ce-323a-4091-bb9f-add557f3a9a2'
UA = {'User-Agent': 'bitkitabani-powo/1.0 (+https://bitkitabani.com)'}
def al(u):
    for _ in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read())
        except Exception: time.sleep(2)
    return {}
sade = lambda x: re.sub(r'[×x]\s+', '', (x or '')).strip().lower()
out = open(os.path.join(KOK, 'veri', 'aday_adlar.tsv'), 'w', encoding='utf-8')
for f in sorted(glob.glob(os.path.join(KOK, 'veri', 'parti', 'p*.txt'))):
    for l in open(f, encoding='utf-8'):
        if l.startswith('#') or '|' not in l: continue
        pid, la = [x.strip() for x in l.split('|')[:2]]
        d = al('https://api.gbif.org/v1/species/search?datasetKey=' + WCVP + '&limit=20&q=' + urllib.parse.quote(la))
        r = [x for x in d.get('results', []) if sade(x.get('canonicalName')) == sade(la)]
        r.sort(key=lambda x: x.get('taxonomicStatus') != 'ACCEPTED')
        if not r: durum, kabul, fam = 'BULUNAMADI', '', ''
        else:
            x = r[0]; fam = x.get('family') or ''
            if x.get('taxonomicStatus') == 'ACCEPTED': durum, kabul = 'kabul', x.get('scientificName', '')
            else: durum, kabul = 'ESAD', x.get('accepted') or ''
        out.write('\t'.join([os.path.basename(f)[:4], pid, la, durum, kabul, fam]) + '\n'); out.flush()
