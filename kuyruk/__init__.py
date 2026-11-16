"""Yayın kuyruğu: her gün bir yeni bitki.

Her kayıt 'yayin' tarihinde (Türkiye saatiyle gece yarısından sonraki ilk derlemede) siteye eklenir.
Biçim ve kurallar için kuyruk/README.md dosyasına bak. Yeni kayıtlar yeni bir kN.py dosyasına
eklenir ve aşağıdaki listeye yazılır; tarihler birbirini izlemeli, bir tarih iki kez kullanılmamalı.
"""
import importlib

FILES = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9', 'k10', 'k11', 'k12', 'k13', 'k14', 'k15', 'k16', 'k17', 'k18', 'k19', 'k20', 'k21', 'k22', 'k23', 'k24', 'k25', 'k26', 'k27', 'k28', 'k29', 'k30', 'k31', 'k32', 'k33', 'k34', 'k35', 'k36', 'k37', 'k38', 'k39', 'k40', 'k41', 'k42', 'k43', 'k44']
Q = []
for _f in FILES:
    Q.extend(importlib.import_module(f'kuyruk.{_f}').Q)
Q.sort(key=lambda q: q['yayin'])

_ids = [q['id'] for q in Q]
assert len(_ids) == len(set(_ids)), 'kuyrukta tekrar eden id var'
# Aynı güne iki bitki yazılmaması kuralı yalnızca GELECEK tarihler içindir;
# 16 Kasım 2026'da bekleyen 104 kayıt tek seferde yayımlandı (aynı tarih).
import datetime as _dt
_days = [q['yayin'] for q in Q if _dt.date.fromisoformat(q['yayin']) > _dt.date(2026, 11, 16)]
assert len(_days) == len(set(_days)), 'aynı güne iki bitki yazılmış'
