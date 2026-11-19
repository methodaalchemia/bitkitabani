"""Her paylaşımda görsel var mı? Üretilen igout planını denetler.

19 Kasım: bağlantılı bitkisi olmayan bir sembol gönderisi (bukağı) Threads'e
görselsiz çıktı. Bu betik, yayına girecek bütün planı tarar ve görselsiz
kalan her slotu adıyla bildirir; iş akışında derlemeden sonra çalışır.

    python3 tools/paylasim_kontrol.py          # rapor; görselsiz varsa ::error::
"""
import os, sys, json, glob

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
IGOUT = os.path.join(ROOT, 'igout')
CI = bool(os.environ.get('GITHUB_ACTIONS'))


def bildir(nerede, neden):
    print(('::error::görselsiz paylaşım: ' if CI else '  GÖRSELSİZ: ') + f'{nerede} — {neden}')


def main():
    eksik, bakilan = 0, 0

    # 1) Threads günlük metinleri
    tj = os.path.join(IGOUT, 'threads.json')
    if os.path.exists(tj):
        plan = json.load(open(tj, encoding='utf-8'))
        for gun, slotlar in sorted(plan.items()):
            for ad, v in slotlar.items():
                bakilan += 1
                if not v.get('image'): eksik += 1; bildir(f'threads {gun}:{ad}', 'image alanı boş')

    # 2) Instagram postları
    for pj in sorted(glob.glob(os.path.join(IGOUT, 'p', '*', 'post.json'))):
        j = json.load(open(pj, encoding='utf-8')); bakilan += 1
        n = os.path.basename(os.path.dirname(pj))
        if not (j.get('images') or []): eksik += 1; bildir(f'instagram p/{n} ({j.get("id")})', 'images boş')
        if not j.get('story'): print(f'  not: p/{n} hikâye görseli yok')

    # 3) Ek paylaşımlar (aylık, kampanya)
    for ad in ('ek.json', 'aylik.json'):
        f = os.path.join(IGOUT, ad)
        if not os.path.exists(f): continue
        d = json.load(open(f, encoding='utf-8'))
        for k, a in (d.items() if isinstance(d, dict) else enumerate(d)):
            bakilan += 1
            if not (a.get('images') or a.get('image')): eksik += 1; bildir(f'{ad}:{k}', 'görsel yok')

    print(f'paylaşım kontrolü: {bakilan} paylaşım · görselsiz {eksik}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
