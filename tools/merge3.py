"""tools/new_plants3.py içeriğini data.json, extra.py, refs.py ve etkilesim.py'ye işler (bir kez çalıştırılır)."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, ROOT)
import new_plants3 as n
D = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
have = {p['id'] for p in D['P']}
EK, TAXON = {}, {}
for p in n.P3:
    if p['id'] in have: continue
    q = dict(p); EK[p['id']] = q.pop('ek'); TAXON[p['id']] = q.pop('taxon')
    D['P'].append(q)
for k, v in n.EXTRA3.items():
    D['EXTRA'].setdefault(k, [])
    for x in v:
        if x not in D['EXTRA'][k]: D['EXTRA'][k].append(x)
json.dump(D, open(os.path.join(ROOT, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(ROOT, 'extra.py'), 'a', encoding='utf-8') as f:
    f.write('\n# ---- 101–119 ----\nEK.update(' + repr(EK) + ')\nKORUMA.update(' + repr(n.KORUMA3) + ')\n')
with open(os.path.join(ROOT, 'refs.py'), 'a', encoding='utf-8') as f:
    f.write('\n# ---- 101–119 ----\nPOWO.update(' + repr(TAXON) + ')\nNCCIH.update(' + repr(n.NCCIH3) + ')\nEMA.update(' + repr(n.EMA3) + ')\n')
    f.write('for _k, _v in ' + repr({k: v for k, v in n.OTHER3.items() if v}) + '.items():\n    OTHER.setdefault(_k, []).extend(_v)\n')
with open(os.path.join(ROOT, 'etkilesim.py'), 'a', encoding='utf-8') as f:
    f.write('\n# ---- 101–119 ----\nETK.update(' + repr(n.ETK3) + ')\n')
print('bitki:', len(D['P']))
