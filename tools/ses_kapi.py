"""Video yayın kapısı: seslendirmenin hangi sayfadan geldiğini dosyadan doğrular.

Kapı üç dosyaya dayanır (tools/reel.py):
  <video>.ses.json  — ses üretilmeden ÖNCE yazılır: slug, adres, metnin özeti
  <video>.ses.txt   — seslendirilen metnin kendisi (ses yalnızca bu dosyadan üretilir)
  <video>.ses.mp3   — seslendirmenin tamamı, metnin yanında

Çalıştırma:
    python3 tools/ses_kapi.py            # igout'u tara, geçmeyenleri indeksten düşür
    python3 tools/ses_kapi.py --rapor    # yalnızca rapor, dosyaya dokunma

Kapıdan önce üretilmiş videolar için kayıt, üretim sırasında yazılan <video>.json'daki
metinden geriye dönük kurulur ve `geriye_donuk` işaretlenir: o metnin sesle birebir
aynı olduğu kanıtlanamaz, bu yüzden rapor onları ayrıca sayar.
"""
import os, sys, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import reel

IGOUT = os.path.join(ROOT, 'igout')


def slug_of(video):
    """igout/p/41/reel.mp4 -> post.json'daki id · igout/cay/adacayi/reel.mp4 -> klasör adı"""
    d = os.path.dirname(video)
    post = os.path.join(d, 'post.json')
    if os.path.exists(post):
        try: return json.load(open(post, encoding='utf-8')).get('id')
        except Exception: return None
    return os.path.basename(d)


def geriye_donuk(video, slug):
    """Kapıdan önce üretilmiş video: üretim anındaki metinden kayıt kur."""
    yan = os.path.splitext(video)[0] + '.json'
    if not os.path.exists(yan): return False
    try: j = json.load(open(yan, encoding='utf-8'))
    except Exception: return False
    sents = j.get('metin') or []
    if not sents: return False
    data = os.path.join(ROOT, '.cache', 'ig_input.json')
    tr = ''
    if os.path.exists(data):
        try: tr = next((x['tr'] for x in json.load(open(data, encoding='utf-8'))['p'] if x['id'] == slug), '')
        except Exception: tr = ''
    reel.ses_kaydi({'id': slug, 'tr': tr}, sents, video, sesli=bool(j.get('sesli')),
                   not_='kapıdan önce üretildi; kayıt <video>.json metninden kuruldu')
    reel.kayda_ekle(video, geriye_donuk=True)
    ses = os.path.splitext(video)[0] + '.ses.mp3'
    if j.get('sesli') and not os.path.exists(ses):
        # ses ayrı dosya olarak saklanmıyordu: videonun kendi ses yolundan çıkarılır
        import subprocess
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', video, '-vn', '-b:a', '128k', ses])
    return True


def main():
    rapor_sadece = '--rapor' in sys.argv
    videolar = sorted(glob.glob(os.path.join(IGOUT, '*', '*', 'reel.mp4')))
    gecen, kuruldu, dusen = [], [], []
    for v in videolar:
        slug = slug_of(v)
        if not slug: dusen.append((v, 'slug bulunamadı')); continue
        if not os.path.exists(os.path.splitext(v)[0] + '.ses.json'):
            if geriye_donuk(v, slug): kuruldu.append(slug)
        tamam, sebep = reel.kapi(v, slug)
        (gecen if tamam else dusen).append((slug, sebep))
    print(f'ses kapısı: {len(videolar)} video · {len(gecen)} geçti · {len(dusen)} durduruldu · {len(kuruldu)} kayıt geriye dönük kuruldu')
    ci = bool(os.environ.get('GITHUB_ACTIONS'))
    for slug, sebep in dusen:
        print(('::error::ses kapısı durdurdu: ' if ci else '  DURDU: ') + f'{slug} — {sebep}')
    if kuruldu: print('  geriye dönük kayıt (ses–metin eşleşmesi kanıtlanamaz):', ', '.join(kuruldu))

    if not rapor_sadece and dusen:
        kotu = {s for s, _ in dusen}
        for ad in ('cay', 'yt'):
            ix = os.path.join(IGOUT, ad, 'index.json')
            if not os.path.exists(ix): continue
            d = json.load(open(ix, encoding='utf-8'))
            kalan = {k: v for k, v in d.items() if k not in kotu}
            if len(kalan) != len(d):
                json.dump(kalan, open(ix, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
                print(f'  {ad}/index.json: {len(d) - len(kalan)} video indeksten düştü')
        for pj in glob.glob(os.path.join(IGOUT, 'p', '*', 'post.json')):
            j = json.load(open(pj, encoding='utf-8'))
            if j.get('reel') and j.get('id') in kotu:
                j.pop('reel', None); j.pop('ses', None)
                json.dump(j, open(pj, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
                print('  post.json: reel kaldırıldı —', j.get('id'))
    # Hat yalnızca kapıyı geçemeyen video için durur: o video indeksten düşer, geri kalan akar.
    # Adım kırmızıya boyanmasın diye 0 dönülür; durdurulanlar ::error:: ile görünür.
    return 2 if ('--kati' in sys.argv and dusen) else 0


if __name__ == '__main__':
    sys.exit(main())
