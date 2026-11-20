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
            if not isinstance(slotlar, dict):
                bakilan += 1; eksik += 1; bildir(f'threads {gun}', 'gün kaydı sözlük değil'); continue
            for ad, v in slotlar.items():
                bakilan += 1
                if not isinstance(v, dict):
                    eksik += 1; bildir(f'threads {gun}:{ad}', 'slot sözlük değil: ' + type(v).__name__); continue
                if not v.get('image'): eksik += 1; bildir(f'threads {gun}:{ad}', 'image alanı boş')

    # 2) Instagram postları
    for pj in sorted(glob.glob(os.path.join(IGOUT, 'p', '*', 'post.json'))):
        j = json.load(open(pj, encoding='utf-8')); bakilan += 1
        n = os.path.basename(os.path.dirname(pj))
        if not (j.get('images') or []): eksik += 1; bildir(f'instagram p/{n} ({j.get("id")})', 'images boş')
        if not j.get('story'): print(f'  not: p/{n} hikâye görseli yok')

    # 3) Ek paylaşımlar (aylık, kampanya)
    # ek.json: {tarih: paylaşım}.  aylik.json: TEK paylaşım nesnesi — gezilecek
    # bir eşleme değil; ayırt etmeden dolaşılırsa değerler düz metin olarak gelir.
    for ad in ('ek.json', 'aylik.json'):
        f = os.path.join(IGOUT, ad)
        if not os.path.exists(f): continue
        d = json.load(open(f, encoding='utf-8'))
        if isinstance(d, dict) and ('image' in d or 'images' in d):
            kayitlar = [(d.get('ay') or d.get('id') or '-', d)]
        elif isinstance(d, dict):
            kayitlar = list(d.items())
        else:
            kayitlar = list(enumerate(d))
        for k, a in kayitlar:
            bakilan += 1
            if not isinstance(a, dict):
                eksik += 1; bildir(f'{ad}:{k}', 'kayıt sözlük değil: ' + type(a).__name__); continue
            if not (a.get('images') or a.get('image')): eksik += 1; bildir(f'{ad}:{k}', 'görsel yok')

    print(f'paylaşım kontrolü: {bakilan} paylaşım · görselsiz {eksik}')
    return 0


if __name__ == '__main__':
    # Bu betik yalnızca rapor verir. Beklenmedik bir hata yüzünden iş akışını
    # durdurup "Değişiklikleri kaydet" adımını atlatmamalı: hata bildirilir,
    # çıkış kodu 0 kalır.
    try:
        sys.exit(main())
    except Exception as e:
        print(('::error::paylaşım kontrolü çalışamadı: ' if CI else '  KONTROL HATASI: ')
              + f'{type(e).__name__}: {e}')
        sys.exit(0)
