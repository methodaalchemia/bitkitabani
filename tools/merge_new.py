"""tools/new_plants.py ve tools/refs2.py içeriğini data.json, extra.py ve refs.py'ye işler (bir kez çalıştırılır)."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, ROOT)
import new_plants as n, refs2 as r
D = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
have = {p['id'] for p in D['P']}
EK, TAXON = {}, {}
for p in n.P2:
    if p['id'] in have: continue
    q = dict(p); EK[p['id']] = q.pop('ek'); TAXON[p['id']] = q.pop('taxon')
    D['P'].append(q)
D['REG']['asya']['ad'] = 'Asya ve Sibirya'
geo = []
for a, b, t, d, pts in n.BR2:
    item = {'a': a, 't': t, 'd': d}
    if b: item['b'] = b
    if not any(x['a'] == a and x.get('b') == b for x in D['BR']):
        D['BR'].append(item); geo.append(pts)
D['EXTRA'].setdefault('tatula', []).extend(['toe', 'banotu'])
D['EXTRA'].setdefault('toe', []).append('tatula')
D['EXTRA'].setdefault('banotu', []).append('tatula')
D['EXTRA'].setdefault('muna', []).append('yarpuz')
D['EXTRA']['yarpuz'] = ['muna', 'nane']
D['EXTRA'].setdefault('safran', []).append('gucigdemi'); D['EXTRA']['gucigdemi'] = ['safran']
D['EXTRA']['civanpercemi'] = ['akadacayi']
json.dump(D, open(os.path.join(ROOT, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(ROOT, 'extra.py'), 'a', encoding='utf-8') as f:
    f.write('\n# ---- 51–100 ----\n')
    f.write('EK.update(' + repr(EK) + ')\n')
    f.write('KORUMA.update(' + repr(n.KORUMA2) + ')\n')
    f.write('YASAL.update(' + repr(n.YASAL2) + ')\n')
    f.write('BR_GEO.extend(' + repr(geo) + ')\n')
with open(os.path.join(ROOT, 'refs.py'), 'a', encoding='utf-8') as f:
    f.write('\n# ---- 51–100 ----\n')
    f.write('POWO.update(' + repr(TAXON) + ')\n')
    f.write('NCCIH.update(' + repr(r.NCCIH2) + ')\n')
    f.write('EMA.update(' + repr(r.EMA2) + ')\n')
    f.write('OTHER.update(' + repr(r.OTHER2) + ')\n')
print('bitki:', len(D['P']), 'köprü:', len(D['BR']), 'harita:', len(geo))
