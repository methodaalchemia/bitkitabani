"""Çay tarifi olan bütün bitkiler için seslendirmeli Reels: igout/cay/<id>/reel.mp4 (bitkitabani.com/ig/cay/<id>/reel.mp4).
tools/ig.py'den sonra çalışır; tarif.py'deki bitkileri alır.

Hizalama: altyazı zamanları artık üretilen sesin kendisinden okunuyor
(reel._ses_hizasi), TTS motorunun kelime zamanı vermesine gerek yok. Video
başına tek Gemini isteği yetiyor. Koşu başına sayılı video yenilenir: önce hiç
videosu olmayanlar (bugün yayımlanacak olanlar), sonra kaydında `ses-hizasi`
bulunmayan eskiler."""
import os, sys, json, shutil, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, ROOT)
import ig2, reel
from tarif import TARIFLER

BUTCE = int(os.environ.get('CAY_HIZA_BUTCE', '12'))   # koşu başına yeniden üretilecek video sayısı (video başına 1 Gemini isteği)
# Altyazısı tahmin değil ölçüm olan yöntemler. 'edge-kelime' edge-tts'in
# WordBoundary olayından geliyor; Gemini kotası dolduğunda ses oraya düşüyor
# ve o yol da gerçek kelime zamanı veriyor, yani video geri alınmamalı.
SAGLAM = ('cumle', 'ses-hizasi', 'edge-kelime')


def _yontem(od):
    """Videonun ses kaydındaki hizalama yöntemi; kayıt yoksa None."""
    try:
        with open(os.path.join(od, 'reel.ses.json'), encoding='utf-8') as f:
            return json.load(f).get('yontem')
    except Exception:
        return None


def main():
    data = json.load(open(os.path.join(ROOT, '.cache', 'ig_input.json'), encoding='utf-8'))
    P = {x['id']: x for x in data['p']}
    out_root = os.path.join(ROOT, 'igout', 'cay'); os.makedirs(out_root, exist_ok=True)
    pidler = sorted({t['bitki'] for t in TARIFLER})

    # Bütçe sırası: önce videosu olmayanlar, sonra hizası tahmin olan eskiler.
    yeni, eski = [], []
    for pid in pidler:
        od = os.path.join(out_root, pid)
        if not os.path.exists(os.path.join(od, 'reel.mp4')): yeni.append(pid)
        elif _yontem(od) not in SAGLAM: eski.append(pid)
    tam_hiza = set((yeni + eski)[:BUTCE])
    print('cay reel: cümle-başına hizalama →', ', '.join(sorted(tam_hiza)) or '(yok)',
          '· yeni %d, düzeltilecek eski %d' % (len(yeni), len(eski)))

    done = {}
    for pid in pidler:
        p = P.get(pid)
        if not p: print('cay reel: yayında değil', pid); continue
        img = next((x for x in [os.path.join(ROOT, 'img', f'{pid}-1280.jpg'), os.path.join(ROOT, 'img', f'{pid}-960.jpg')] if os.path.exists(x)), None)
        od = os.path.join(out_root, pid); os.makedirs(od, exist_ok=True)
        hedef = os.path.join(od, 'reel.mp4')
        # Bütçeye giren eski video yeniden üretilir; girmeyen varsa olduğu gibi kalır.
        yenile = pid in tam_hiza and os.path.exists(hedef)
        reel.TAM_HIZA = False   # cümle başına istek gerekmiyor; hizalama sesten okunuyor
        if os.path.exists(hedef) and not yenile:
            ok = True
        else:
            # Var olan videoyu yenilerken önce yedekle: üretim tutmazsa eskisi geri
            # konur, yoksa video index.json'dan düşer ve yayın kuyruğundan kaybolur.
            yedek = []
            if yenile:
                for ad in ('reel.mp4', 'reel.json', 'reel.ses.json', 'reel.ses.txt', 'reel.ses.mp3'):
                    y = os.path.join(od, ad)
                    if os.path.exists(y): shutil.copy2(y, y + '.yedek'); yedek.append(y)
            ok = reel.make(p, ig2.text_for(p), img, hedef)
            if yenile and (not ok or _yontem(od) not in SAGLAM):
                for y in yedek: shutil.copy2(y + '.yedek', y)
                ok = True
                print('cay reel: %s yenilenemedi, eski video geri kondu' % pid)
            for y in yedek:
                if os.path.exists(y + '.yedek'): os.remove(y + '.yedek')
        if ok:   # yayın kapısı: ses kaydındaki slug videonun konusuyla aynı mı
            ok, sebep = reel.kapi(hedef, pid)
            if not ok: print('cay reel: KAPI DURDURDU —', pid, '—', sebep)
        print('cay reel:', pid, 'hazır' if ok else 'HATA', '· hiza=%s' % (_yontem(od) or 'tahmin'))
        if ok:
            # Yöresel ad başlık testine girsin: YouTube'da yöresel adla arayan
            # bulduğunu sonuna kadar izliyor (24 Kasım veri notu).
            yor = re.split(r'[,;]', str(p.get('diger') or ''))[0].strip()
            if yor.lower() == p['tr'].lower() or len(yor) < 3: yor = ''
            done[pid] = {'reel': f'https://bitkitabani.com/ig/cay/{pid}/reel.mp4', 'caption': ig2.caption2(p, 'Çay tarifi'),
                         'tr': p['tr'], 'yoresel': yor,
                         'tarif': next(t['slug'] for t in TARIFLER if t['bitki'] == pid)}
    json.dump(done, open(os.path.join(out_root, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    kalan = sum(1 for pid in pidler if _yontem(os.path.join(out_root, pid)) not in SAGLAM)
    print('cay reel: %d video hazır · hizası hâlâ tahmin olan: %d' % (len(done), kalan))


if __name__ == '__main__':
    main()
