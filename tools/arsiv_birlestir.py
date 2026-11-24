#!/usr/bin/env python3
"""Biten toplu kayıt dosyalarını (kuyruk/aNNN.py) kuyruğa bağlar.
Yalnızca tools/arsiv_denetle.py denetiminden hatasız geçen dosyalar eklenir; yayin tarihi bugüne çekilir.
Çalıştırma: python3 tools/arsiv_birlestir.py"""
import glob, os, re, subprocess, sys, datetime
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
init = os.path.join(KOK, 'kuyruk', '__init__.py'); s = open(init, encoding='utf-8').read()
m = re.search(r"FILES = \[(.*?)\]", s); var = re.findall(r"'(\w+)'", m.group(1))
bugun = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).date().isoformat()
yeni = []
for f in sorted(glob.glob(os.path.join(KOK, 'kuyruk', 'a[0-9]*.py'))):
    ad = os.path.basename(f)[:-3]
    if ad in var: continue
    r = subprocess.run([sys.executable, os.path.join(KOK, 'tools', 'arsiv_denetle.py'), f], capture_output=True, text=True)
    if r.returncode != 0:
        print('BEKLİYOR', ad, '\n  ' + r.stdout.strip().replace('\n', '\n  ')[:1500]); continue
    t = open(f, encoding='utf-8').read()
    t2 = re.sub(r"(['\"]yayin['\"]\s*:\s*['\"])\d{4}-\d\d-\d\d", r"\g<1>" + bugun, t)
    if t2 != t: open(f, 'w', encoding='utf-8').write(t2)
    yeni.append(ad); print('eklendi', ad, r.stdout.strip())
if yeni:
    s = s.replace(m.group(0), "FILES = [" + ', '.join(repr(x) for x in var + yeni) + "]")
    open(init, 'w', encoding='utf-8').write(s)
print(len(yeni), 'dosya eklendi')
