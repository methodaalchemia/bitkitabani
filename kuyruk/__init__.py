"""Yayın kuyruğu: her gün bir yeni bitki.

Her kayıt 'yayin' tarihinde (Türkiye saatiyle gece yarısından sonraki ilk derlemede) siteye eklenir.
Biçim ve kurallar için kuyruk/README.md dosyasına bak. Yeni kayıtlar yeni bir kN.py dosyasına
eklenir ve aşağıdaki listeye yazılır; tarihler birbirini izlemeli, bir tarih iki kez kullanılmamalı.
"""
import importlib

FILES = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9', 'k10', 'k11', 'k12', 'k13', 'k14', 'k15', 'k16', 'k17', 'k18', 'k19', 'k20', 'k21', 'k22', 'k23', 'k24', 'k25', 'k26', 'k27', 'k28', 'k29', 'k30', 'k31', 'k32', 'k33', 'k34', 'k35', 'k36', 'k37', 'k38', 'k39', 'k40', 'k41', 'k42', 'k43', 'k44', 'k45', 'k46', 'k47', 'k48', 'k49', 'k50', 'k51', 'k52', 'k53', 'k54', 'k55', 'k56', 'k57', 'k58', 'a003', 'a004']
Q = []
for _f in FILES:
    Q.extend(importlib.import_module(f'kuyruk.{_f}').Q)
Q.sort(key=lambda q: q['yayin'])

_ids = [q['id'] for q in Q]
assert len(_ids) == len(set(_ids)), 'kuyrukta tekrar eden id var'
# Aynı güne iki bitki yazılmaması kuralı yalnızca GELECEK tarihler içindir;
# 16 Kasım 2026'da bekleyen 104 kayıt tek seferde yayımlandı (aynı tarih),
# 19 Kasım 2026'da ise kuyruğun tamamı bir gün öne alındı; o gün iki bitki yayımlandı.
import datetime as _dt
# 'arsiv': True olan kayıtlar toplu eklenir (1000 bitki hedefi); günlük sıraya girmez, tarih kuralı onlara uygulanmaz.
_days = [q['yayin'] for q in Q if not q.get('arsiv') and _dt.date.fromisoformat(q['yayin']) > _dt.date(2026, 11, 19)]
assert len(_days) == len(set(_days)), 'aynı güne iki bitki yazılmış'
