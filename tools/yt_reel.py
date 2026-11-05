"""Katalogdaki bütün bitkiler için seslendirmeli Reels: igout/yt/<id>/reel.mp4

YouTube Shorts akışını beslemek için. Çay tarifi olanlar zaten tools/cay_reel.py ile
üretiliyor; bu betik geri kalan bitkileri alır. Var olan dosyayı yeniden üretmez, bu yüzden
igmedia dalındaki eski dosyalar igout'a geri konduktan sonra çalıştırılmalı.

    python3 tools/yt_reel.py              # eksik olanlardan YT_REEL_LIMIT kadarını üret
    YT_REEL_LIMIT=0 python3 tools/yt_reel.py   # hepsini üret (uzun sürer)
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, ROOT)
import ig2, reel
from tarif import TARIFLER

LIMIT = int(os.environ.get('YT_REEL_LIMIT', '12'))


def main():
    data = json.load(open(os.path.join(ROOT, '.cache', 'ig_input.json'), encoding='utf-8'))
    P = {x['id']: x for x in data['p']}
    cayli = {t['bitki'] for t in TARIFLER}
    out_root = os.path.join(ROOT, 'igout', 'yt'); os.makedirs(out_root, exist_ok=True)
    ix = os.path.join(out_root, 'index.json')
    done = json.load(open(ix, encoding='utf-8')) if os.path.exists(ix) else {}

    # sıra: katalogdaki sıra (en çok aranandan başlıyor), çay tarifi olanlar hariç
    sira = [p['id'] for p in data['p'] if p['id'] not in cayli]
    eksik = [pid for pid in sira if not os.path.exists(os.path.join(out_root, pid, 'reel.mp4'))]
    print(f'{len(sira)} bitki, {len(sira) - len(eksik)} hazır, {len(eksik)} eksik')
    if LIMIT > 0: eksik = eksik[:LIMIT]

    for pid in eksik:
        p = P.get(pid)
        if not p: print('yt reel: yayında değil', pid); continue
        img = next((x for x in [os.path.join(ROOT, 'img', f'{pid}-1280.jpg'), os.path.join(ROOT, 'img', f'{pid}-960.jpg')] if os.path.exists(x)), None)
        if not img: print('yt reel: fotoğraf yok', pid); continue
        od = os.path.join(out_root, pid); os.makedirs(od, exist_ok=True)
        ok = reel.make(p, ig2.text_for(p), img, os.path.join(od, 'reel.mp4'))
        print('yt reel:', pid, 'ok' if ok else 'HATA')
        if ok:
            done[pid] = {'reel': f'https://bitkitabani.com/ig/yt/{pid}/reel.mp4',
                         'caption': ig2.caption2(p, 'Shorts'), 'tr': p['tr']}

    # dosyası silinmiş olanları indeksten düş
    for pid in list(done):
        if not os.path.exists(os.path.join(out_root, pid, 'reel.mp4')): done.pop(pid)
    json.dump(done, open(ix, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('yt indeks:', len(done), 'video')


if __name__ == '__main__':
    main()
