"""Çay tarifi olan bütün bitkiler için seslendirmeli Reels: igout/cay/<id>/reel.mp4 (bitkitabani.com/ig/cay/<id>/reel.mp4).
tools/ig.py'den sonra çalışır; tarif.py'deki bitkileri alır."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, ROOT)
import ig2, reel
from tarif import TARIFLER

def main():
    data = json.load(open(os.path.join(ROOT, '.cache', 'ig_input.json'), encoding='utf-8'))
    P = {x['id']: x for x in data['p']}
    out_root = os.path.join(ROOT, 'igout', 'cay'); os.makedirs(out_root, exist_ok=True)
    done = {}
    for pid in sorted({t['bitki'] for t in TARIFLER}):
        p = P.get(pid)
        if not p: print('cay reel: yayında değil', pid); continue
        img = next((x for x in [os.path.join(ROOT, 'img', f'{pid}-1280.jpg'), os.path.join(ROOT, 'img', f'{pid}-960.jpg')] if os.path.exists(x)), None)
        od = os.path.join(out_root, pid); os.makedirs(od, exist_ok=True)
        ok = reel.make(p, ig2.text_for(p), img, os.path.join(od, 'reel.mp4'))
        print('cay reel:', pid, 'ok' if ok else 'HATA')
        if ok: done[pid] = {'reel': f'https://bitkitabani.com/ig/cay/{pid}/reel.mp4', 'caption': ig2.caption2(p, 'Çay tarifi'), 'tr': p['tr'], 'tarif': next(t['slug'] for t in TARIFLER if t['bitki'] == pid)}
    json.dump(done, open(os.path.join(out_root, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
