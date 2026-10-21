"""Yayın kuyruğu: her gün bir yeni bitki.

Her kayıt 'yayin' tarihinde (Türkiye saatiyle gece yarısından sonraki ilk derlemede) siteye eklenir.
Biçim ve kurallar için kuyruk/README.md dosyasına bak. Yeni kayıtlar yeni bir kN.py dosyasına
eklenir ve aşağıdaki listeye yazılır; tarihler birbirini izlemeli, bir tarih iki kez kullanılmamalı.
"""
import importlib

FILES = ['k1', 'k2', 'k3']
Q = []
for _f in FILES:
    Q.extend(importlib.import_module(f'kuyruk.{_f}').Q)
Q.sort(key=lambda q: q['yayin'])

_ids = [q['id'] for q in Q]
assert len(_ids) == len(set(_ids)), 'kuyrukta tekrar eden id var'
_days = [q['yayin'] for q in Q]
assert len(_days) == len(set(_days)), 'aynı güne iki bitki yazılmış'
