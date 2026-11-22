"""Seslendirmeli ve altyazılı Reels (9:16, ~25 sn).

Metin, bitkinin hazır Instagram metninden (ig_metin.py ya da otomatik metin) kurulur; Claude ya da elle yazım gerekmez.
Ses: Microsoft Edge'in Türkçe sinir ağı sesi (edge-tts, tr-TR-EmelNeural). Altyazı, sesin kelime zamanlamasından
üretilir ve videoya gömülür. edge-tts kurulu değilse ya da ulaşılamazsa video yine üretilir: altyazı tahmini
zamanlamayla gösterilir, arkada yalnızca ambiyans müziği çalar.
"""
import os, re, json, asyncio, shutil, subprocess, tempfile, random, time, hashlib, datetime
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(HERE, 'fonts')
# Ses sabittir: Emel. Eski sese (tr-TR-AhmetNeural) dönülmeyecek; bu yüzden
# ortam değişkeni yalnızca başka bir Emel varyantını seçebilir.
VOICE = os.environ.get('REEL_VOICE', 'tr-TR-EmelNeural')
if 'Emel' not in VOICE: VOICE = 'tr-TR-EmelNeural'
SW, SH, FPS, XF = 1080, 1920, 30, 0.45
GAP = 0.28   # cümleler arası sessizlik (sn)

def _sent(t): return [x.strip() for x in re.split(r'(?<=[.!?])\s+', (t or '').strip()) if x.strip()]
def _clean(t):
    t = re.sub(r'[\U0001F000-\U0001FFFF☀-➿️]', '', t or '')
    return re.sub(r'\s+', ' ', t).strip()
def _words(t): return len(t.split())

def script(p, m):
    """Konuşma metni: soru/kanca, az bilinen gerçek, gelenek, bilim, dikkat, kapanış. ~58 kelimeyi geçmez (~25-28 sn)."""
    hook = _clean(m.get('ilk') or m.get('kapak') or p['tr'])
    if not hook.lower().startswith(p['tr'].lower().split()[0]): hook = f"{p['tr']}: {hook}"
    parts = [hook]
    if m.get('hikaye'): parts += _sent(_clean(m['hikaye'][1]))[:2]
    if m.get('gelenek'): parts += _sent(_clean(m['gelenek'][1]))[:1]
    if m.get('bilim'):
        b = _sent(_clean(m['bilim'][1]))[:1]
        parts += b or [_clean(m['bilim'][0]) + '.']
    dk = [d for d in (m.get('dikkat') or []) if not d.startswith('Bilinen önemli')]
    if dk:
        dk = [d[0].lower() + d[1:] for d in dk[:2]]
        parts.append('Dikkat etmesi gerekenler: ' + ' ve '.join(dk).rstrip('.') + '.')
    end = 'Kaynaklarıyla birlikte tamamı Bitki Tabanı’nda.'
    out, n = [], _words(end)
    for s in parts:   # sırayla ekle, sınırı aşan cümleyi atla (kanca her zaman kalır)
        if not out or n + _words(s) <= 58: out.append(s); n += _words(s)
    return out + [end]

# ---------- ses ----------
async def _tts1(text, path):
    import edge_tts
    try: c = edge_tts.Communicate(text, VOICE, rate='+12%', boundary='WordBoundary')
    except TypeError: c = edge_tts.Communicate(text, VOICE, rate='+12%')
    words = []
    with open(path, 'wb') as f:
        async for ch in c.stream():
            if ch['type'] == 'audio': f.write(ch['data'])
            elif ch['type'] == 'WordBoundary': words.append([ch['offset'] / 1e7, (ch['offset'] + ch['duration']) / 1e7, ch['text']])
    return words

GEMINI_VOICE = os.environ.get('GEMINI_VOICE', 'Kore')
def _gemini1(text, path):
    """Gemini TTS: 24 kHz PCM döner; ffmpeg ile mp3'e çevrilir. Kelime zamanı vermez, süreye orantılı tahmin edilir."""
    import json as _j, base64, urllib.request, urllib.error
    key = os.environ.get('GEMINI_API_KEY')
    if not key: raise RuntimeError('GEMINI_API_KEY yok')
    # ⚠️ Metnin başına üslup yönergesi EKLENMEYECEK: Gemini onu da sesli okuyor
    # (19 Kasım 2026, reishi videosunda yönerge seslendirildi). Sadece okunacak metin gider.
    body = {'contents': [{'parts': [{'text': text}]}],
            'generationConfig': {'responseModalities': ['AUDIO'], 'speechConfig': {'voiceConfig': {'prebuiltVoiceConfig': {'voiceName': GEMINI_VOICE}}}}}
    req = urllib.request.Request('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent',
                                 data=_j.dumps(body).encode(), headers={'content-type': 'application/json', 'x-goog-api-key': key})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: j = _j.loads(r.read())
    except urllib.error.HTTPError as ex:   # kota mesajı gövdede: hangi sınıra takıldığımız görünsün
        try: govde = ex.read().decode('utf-8', 'replace')[:400]
        except Exception: govde = ''
        raise RuntimeError(f'HTTP {ex.code} {govde}') from None
    part = j['candidates'][0]['content']['parts'][0]['inlineData']
    pcm = path + '.pcm'; open(pcm, 'wb').write(base64.b64decode(part['data']))
    hiz = os.environ.get('GEMINI_RATE', '1.18')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 's16le', '-ar', '24000', '-ac', '1', '-i', pcm,
                    '-filter:a', f'atempo={hiz}', '-b:a', '128k', path], check=True)
    return _dur(path)

def _sessizlikler(path):
    """ffmpeg silencedetect: (başlangıç, bitiş) sessizlik aralıkları."""
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', 'silencedetect=noise=-33dB:d=0.22', '-f', 'null', '-'],
                       capture_output=True, text=True)
    out, bas = [], None
    for m in re.finditer(r'silence_(start|end): (-?[\d.]+)', r.stderr):
        if m.group(1) == 'start': bas = float(m.group(2))
        elif bas is not None: out.append((bas, float(m.group(2)))); bas = None
    return out

_SON_HIZA = None     # son hizalamanın en kötü sapması (ses kaydına yazılır)
_SON_YONTEM = None   # 'cumle' (her cümle ayrı istek) ya da 'tek-istek' (yedek yol)
TAM_HIZA = False     # yalnız o gün yayımlanacak video için True: cümle başına istek atılır.
                     # Gemini'nin ücretsiz katmanında günlük istek hakkı dar; koşu başına 4
                     # post üretiliyor, hepsine cümle başına istek atınca kota doluyor ve ses
                     # Emel'e düşüyordu (22 Kasım). Yayımlanacak tek videoya ayrılıyor.

def _edge_referans(sents, tmp):
    """Cümlelerin gerçek okunma süreleri ve kelime sınırları — hizalama referansı.

    Gemini TTS zaman bilgisi vermiyor; bu yüzden SES Gemini'nin, ZAMANLAMA bu referansın.
    Aynı metni edge-tts cümle cümle okur, kelime sınırlarını verir; sesi atılır, yalnız
    süreleri kullanılır. edge-tts ücretsiz ve kotasız olduğu için cümle başına istek
    sorun değil — Gemini'de olan oydu (tek istek zorunluluğu).
    """
    ref = []
    for i, c in enumerate(sents):
        yol = os.path.join(tmp, 'ref%d.mp3' % i)
        ws = asyncio.run(_tts1(c, yol))
        d = _dur(yol)
        if not ws or d <= 0: raise RuntimeError('referans ses alınamadı')
        ref.append((d, ws))
        try: os.remove(yol)
        except OSError: pass
    return ref


def _konusma_araligi(mp3):
    """Bir parçanın baş ve sondaki sessizliğini atar: gerçek konuşmanın başı ve sonu."""
    d = _dur(mp3)
    bas, son = 0.0, d
    for a, b in _sessizlikler(mp3):
        if a <= 0.05: bas = max(bas, b)
        if b >= d - 0.05: son = min(son, a)
    return (bas, son) if son - bas > 0.15 else (0.0, d)


def _konusma_saati(toplam, sessiz, hedef):
    """Konuşma-zamanı hedefini duvar saatine çevirir (aradaki duraklamaları atlayarak)."""
    t = k = 0.0
    for a, b in sessiz:
        if a <= t: continue
        if k + (a - t) >= hedef: return t + (hedef - k)
        k += a - t; t = b
    return min(toplam, t + (hedef - k))


def _araliklar(sents, toplam, sessiz, ref):
    """Cümle sınırlarını seçer.

    Önceden "en uzun n-1 sessizlik" alınıyordu; cümle içindeki doğal duraklama cümle sonu
    sanılınca kesim kayıyor, sahne ve altyazı sesten ayrılıyordu (19-21 Kasım: reishi,
    çemen, muskat). Artık her sınırın BEKLENEN yeri referans sürelerden ölçeklenerek
    bulunuyor, sonra yalnızca o civardaki gerçek sessizliğe oturtuluyor. Yakınında
    sessizlik yoksa beklenen yerde kesiliyor — uzaktaki yanlış sessizliğe atlamıyor.
    """
    n = len(sents)
    if n == 1: return [(0.0, toplam)], 0.0
    sure = [d for d, _ in ref] if ref else [max(1.0, _estimate(c)[1]) for c in sents]
    S = sum(sure) or 1.0
    # Duraklamalar toplam süreye dahil; oranı doğrudan toplam süreye uygularsak her sınır
    # biraz daha ileri kayıyordu. Beklenen yer KONUŞMA zamanında hesaplanıp duvar saatine
    # çevriliyor, böylece aradaki duraklamalar sınırı ötelemiyor.
    kon = max(0.1, toplam - sum(max(0.0, b - a) for a, b in sessiz))
    bek, t = [], 0.0
    for k in sure[:-1]:
        t += k; bek.append(_konusma_saati(toplam, sessiz, kon * t / S))
    pencere = max(0.8, toplam / n * 0.35)
    secim, onceki, kalan = [], 0.0, sorted(sessiz)
    for b in bek:
        uygun = [(a, c) for a, c in kalan if a > onceki + 0.15 and abs((a + c) / 2 - b) <= pencere]
        if uygun:
            a, c = min(uygun, key=lambda x: abs((x[0] + x[1]) / 2 - b))
            kalan = [x for x in kalan if x[0] > a]
        else:
            a = c = min(max(b, onceki + 0.15), toplam - 0.1)
        secim.append((a, c)); onceki = c
    araliklar, onceki = [], 0.0
    for a, c in secim: araliklar.append((onceki, a)); onceki = c
    araliklar.append((onceki, toplam))
    sapma = max(abs((a + c) / 2 - b) for (a, c), b in zip(secim, bek)) / toplam
    return araliklar, sapma


def _gemini_cumle(sents, tmp):
    """Her cümleyi AYRI istekle seslendirir — tercih edilen yol.

    Gemini zaman bilgisi vermiyor. Tek istekte seslendirilince cümleleri sessizliklerden
    kesmek gerekiyordu ve kesim yeri tahmindi; altyazı sesten kayıyordu (19-22 Kasım:
    reishi, çemen, muskat, kimyon). Cümle başına istek bu tahmini tamamen kaldırır:
    her cümlenin süresi ölçülür.

    Maliyet: ig.py koşu başına 4 post üretiyor, cümle de ~6, yani ~24 istek. Tek istekli
    yol (_gemini_hepsi) kota hatasında yedek olarak duruyor.
    """
    global _SON_YONTEM, _SON_HIZA
    try:
        ref = _edge_referans(sents, tmp)
    except Exception as ex:
        print('reel: kelime zamanı referansı alınamadı, süre tahminine düşülüyor:', str(ex)[:120]); ref = None
    out = []
    for i, c in enumerate(sents):
        mp3 = os.path.join(tmp, 'c%d.mp3' % i)
        if i: time.sleep(1.5)        # dakikalık istek sınırına çarpmamak için
        _gemini1(c, mp3)
        d = _dur(mp3)
        if d <= 0: raise RuntimeError('boş ses: cümle %d' % (i + 1))
        sb, ss = _konusma_araligi(mp3)
        if ss - sb > 0.3 and (sb > 0.05 or ss < d - 0.05):   # baş/son sessizliği at: araları GAP belirlesin
            kes = os.path.join(tmp, 'k%d.mp3' % i)
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '%.3f' % max(0.0, sb - 0.06),
                            '-to', '%.3f' % min(d, ss + 0.08), '-i', mp3, '-b:a', '128k', kes], check=True)
            mp3, d = kes, _dur(kes)
            sb, ss = _konusma_araligi(mp3)
        if ref:
            _, ws = ref[i]
            rb, rs = ws[0][0], ws[-1][1]
            k = (ss - sb) / max(0.1, rs - rb)
            ws = [[sb + (x - rb) * k, sb + (y - rb) * k, w] for x, y, w in ws]
        else:
            ws, est = _estimate(c)
            k = (ss - sb) / max(0.1, est)
            ws = [[sb + x * k, sb + y * k, w] for x, y, w in ws]
        out.append((mp3, d, ws))
    _SON_YONTEM, _SON_HIZA = 'cumle', 0.0      # cümle sınırı tahmin değil: sapma yok
    return out


def _gemini_hepsi(sents, tmp):
    """Bütün metni TEK istekte seslendirir (ücretsiz katman günlük hakkı cümle başına
    istek atmaya yetmiyor), sonra cümleleri referans zamanlamaya göre keser."""
    global _SON_HIZA, _SON_YONTEM
    tam = os.path.join(tmp, 'gem-tam.mp3')
    _gemini1('\n'.join(sents), tam)   # yalnızca okunacak cümleler; yönerge yok (sesli okunuyordu)
    toplam = _dur(tam)
    if toplam <= 0: raise RuntimeError('boş ses')
    ic = [(a, b) for a, b in _sessizlikler(tam) if a > 0.25 and b < toplam - 0.25]
    try:
        ref = _edge_referans(sents, tmp)
    except Exception as ex:
        print('reel: hizalama referansı alınamadı, süre tahminine düşülüyor:', str(ex)[:120]); ref = None
    araliklar, _SON_HIZA = _araliklar(sents, toplam, ic, ref)
    _SON_YONTEM = 'tek-istek'
    out = []
    for i, ((a, b), c) in enumerate(zip(araliklar, sents)):
        mp3 = os.path.join(tmp, 's%d.mp3' % i)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '%.3f' % a, '-to', '%.3f' % b, '-i', tam, '-b:a', '128k', mp3], check=True)
        d = _dur(mp3)
        if ref:
            # Referansın dosya süresine göre ölçeklemek yanlıştı: hem referansın hem parçanın
            # baş/son sessizlik payı sayıya giriyor, kelimeler video boyunca giderek geç
            # düşüyordu ("yazı geç kalıyor, ses daha hızlı gidiyor"). Artık iki tarafın da
            # KONUŞMA aralığı eşleniyor: ilk kelime konuşmanın başına, son kelime sonuna oturur.
            _, ws = ref[i]
            rb, rs = ws[0][0], ws[-1][1]
            sb, ss = _konusma_araligi(mp3)
            k = (ss - sb) / max(0.1, rs - rb)
            ws = [[sb + (x - rb) * k, sb + (y - rb) * k, w] for x, y, w in ws]
        else:
            ws, est = _estimate(c); k = max(0.05, d - 0.12) / max(0.1, est)
            ws = [[x * k, y * k, w] for x, y, w in ws]
        out.append((mp3, d, ws))
    return out


def _dur(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], capture_output=True, text=True)
    try: return float(r.stdout.strip())
    except ValueError: return 0.0

def _estimate(s):
    ws = s.split(); tot = 0.30 * len(ws) + 0.15 * len(re.findall(r'[,;:]', s)) + 0.2
    w8 = [len(w) + 2 for w in ws]; t, out = 0.1, []
    for w, k in zip(ws, w8):
        d = tot * k / sum(w8); out.append([t, t + d * 0.92, w]); t += d
    return out, tot + 0.1

# ---------- ses kaydı ve yayın kapısı ----------
# 19 Kasım 2026: bir videonun seslendirmesi yanlış metinden üretildi ve bu gözden kaçtı.
# Kapı, elle kontrole değil dosyalara dayanır:
#   1. Ses üretilmeden ÖNCE metnin hangi sayfadan geldiği (slug/adres) <video>.ses.json'a yazılır.
#   2. Okunacak metin <video>.ses.txt'ye düz metin olarak kaydedilir; seslendirme YALNIZCA bu
#      dosyadan okunur, böylece metin ile ses aynı işin çıktısı olur.
#   3. Yayından önce kapi() çalışır: kayıttaki slug videonun konusuyla aynı değilse hat durur.

YONERGE_IZI = ('ses tonu', 'üslupla', 'üslupta', 'seslendir', 'aşağıdaki metni', 'oku:', 'voice:', 'style:', 'instruction')

def _kucuk(t): return (t or '').replace('I', 'ı').replace('İ', 'i').lower()
def _taban(out): return os.path.splitext(out)[0]
def _ozet(metin): return hashlib.sha256(metin.encode('utf-8')).hexdigest()[:16]

def ses_kaydi(p, sents, out, sesli=None, not_=''):
    """Seslendirmeden ÖNCE çağrılır: metnin kaynağını ve kendisini diske yazar."""
    t = _taban(out); metin = '\n'.join(sents)
    open(t + '.ses.txt', 'w', encoding='utf-8').write(metin + '\n')
    k = {'slug': p['id'], 'adres': 'https://bitkitabani.com/%s/' % p['id'], 'tr': p.get('tr', ''),
         'metin_dosyasi': os.path.basename(t) + '.ses.txt', 'ozet': _ozet(metin),
         'yazilma': datetime.datetime.now().isoformat(timespec='seconds')}
    if sesli is not None: k['sesli'] = bool(sesli)
    if not_: k['not'] = not_
    json.dump(k, open(t + '.ses.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return k

def okunacak(out):
    """Seslendirilecek cümleler yalnızca kayıttan okunur (tek kaynak)."""
    return [x.strip() for x in open(_taban(out) + '.ses.txt', encoding='utf-8').read().split('\n') if x.strip()]

def kayda_ekle(out, **alanlar):
    t = _taban(out) + '.ses.json'
    k = json.load(open(t, encoding='utf-8')); k.update(alanlar)
    json.dump(k, open(t, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return k

def _ses_sakla(segs, tmp, hedef):
    """Seslendirmenin tamamı metnin yanında dursun diye tek mp3'e birleştirilir."""
    parcalar = [s[2] for s in segs if s[2] and os.path.exists(s[2])]
    if not parcalar: return False
    lst = os.path.join(tmp, 'ses-liste.txt')
    open(lst, 'w', encoding='utf-8').write(''.join("file '%s'\n" % x for x in parcalar))
    for kodek in (['-c', 'copy'], ['-c:a', 'libmp3lame', '-b:a', '128k']):   # kopyalama tutmazsa yeniden kodla
        r = subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst] + kodek + [hedef])
        if r.returncode == 0 and os.path.exists(hedef) and _dur(hedef) > 0: return True
    print('reel: seslendirme tek dosyada saklanamadı')
    return False

def kapi(out, slug):
    """Yayın öncesi tek kontrol. (tamam, sebep) döner; tamam değilse video yayımlanmaz."""
    t = _taban(out)
    if not os.path.exists(out): return False, 'video yok'
    try: k = json.load(open(t + '.ses.json', encoding='utf-8'))
    except Exception: return False, 'ses kaydı yok'
    if not k.get('slug'): return False, 'ses kaydında slug yok'
    if k['slug'] != slug: return False, 'ses kaydı %s, video %s' % (k['slug'], slug)
    # Seslendirme alınamadıysa video yayımlanmaz. Önceden sessiz video kapıdan geçiyordu;
    # tek ses motoru kaldığı için (bkz. voice(), REEL_GEMINI) bir edge-tts kesintisi
    # doğrudan sessiz Reels demek olurdu. Eda'nın kararı, 21 Kasım 2026.
    if k.get('sesli') is False: return False, 'ses üretilemedi (sessiz video)'
    try: metin = open(t + '.ses.txt', encoding='utf-8').read().strip()
    except Exception: return False, 'metin dosyası yok'
    if not metin: return False, 'metin boş'
    if k.get('ozet') and k['ozet'] != _ozet(metin): return False, 'metin kayıttan sonra değişmiş'
    ad = _kucuk(k.get('tr') or '').split()
    if ad and ad[0] not in _kucuk(metin): return False, 'metinde "%s" geçmiyor' % ad[0]
    dusuk = _kucuk(metin)
    for iz in YONERGE_IZI:
        if iz in dusuk: return False, 'metinde yönerge izi: "%s"' % iz
    ses = t + '.ses.mp3'
    if not os.path.exists(ses) or _dur(ses) <= 0: return False, 'ses dosyası yok'
    return True, 'tamam'


def voice(sents, tmp, gem=None):
    global _SON_HIZA, _SON_YONTEM
    _SON_HIZA = _SON_YONTEM = None      # her video kendi değerini yazsın (22 Kasım: üç kayıtta aynı hiza)
    """Her cümle ayrı seslendirilir: [(başlangıç, süre, mp3 ya da None, kelimeler)] ve sesli mi?"""
    if gem is None: gem = bool(os.environ.get('GEMINI_API_KEY'))
    if gem:
        yollar = (_gemini_cumle, _gemini_hepsi) if TAM_HIZA else (_gemini_hepsi,)
        for yol in yollar:   # önce cümle başına istek; kota dolarsa tek istek
            hata = ''
            for bekle in ((0,) if yol is _gemini_cumle else (0, 20, 40)):   # cümle yolu tekrar denenmez: kotayı tüketir
                if bekle: time.sleep(bekle)
                try:
                    parcalar = yol(sents, tmp)
                    segs, t = [], 0.15
                    for d, (mp3, dur, ws) in zip(sents, parcalar):
                        segs.append((t, dur, mp3, [[a + t, b + t, w] for a, b, w in ws])); t += dur + GAP
                    print('reel: ses yolu =', _SON_YONTEM)
                    return segs, True, t
                except Exception as ex:
                    hata = str(ex)[:300]
                    if '429' not in hata: break
            print('reel: %s yolu olmadı: %s' % (yol.__name__, hata))
        print('reel: Gemini sesi alınamadı, video Edge sesiyle yapılıyor')
        return voice(sents, tmp, gem=False)
    segs, t, ok = [], 0.15, True
    for i, s in enumerate(sents):
        mp3, ws, d = os.path.join(tmp, f's{i}.mp3'), None, 0
        if ok:
            try:
                ws = asyncio.run(_tts1(s, mp3))
                d = _dur(mp3)
                if not ws or d <= 0: raise RuntimeError('boş ses')
            except Exception as e:
                print('reel: ses alınamadı, altyazılı sessiz video:', str(e)[:120]); ok = False
        if not ok: ws, d = _estimate(s); mp3 = None
        segs.append((t, d, mp3, [[a + t, b + t, w] for a, b, w in ws])); t += d + GAP
    return segs, ok, t

# ---------- altyazı ----------
def _ts(x): x = max(0, x); return f'{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}'
def ass(segs, path, skip_last=True):
    head = ('[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 0\n\n[V4+ Styles]\n'
            'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
            'Style: Cap,Alegreya Sans,124,&H00FFFFFF,&H00FFFFFF,&H00141812,&H64000000,-1,0,0,0,100,100,0,0,1,9,4,2,70,70,560,1\n\n'
            '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
    ev = []
    for si, (_, _, _, ws) in enumerate(segs[:-1] if skip_last else segs):
        ch, chunks = [], []
        for w in ws:   # en çok 3 kelime ya da ~16 harf; noktalamada böl
            ch.append(w)
            if len(ch) >= 3 or sum(len(x[2]) for x in ch) > 15 or re.search(r'[.,;:?!]$', w[2]): chunks.append(ch); ch = []
        if ch: chunks.append(ch)
        for k, c in enumerate(chunks):
            st, en = c[0][0], (chunks[k + 1][0][0] if k + 1 < len(chunks) else c[-1][1] + 0.25)
            txt = ' '.join(x[2] for x in c).replace('{', '(').replace('}', ')')
            ev.append(f'Dialogue: 0,{_ts(st)},{_ts(en)},Cap,,0,0,0,,{{\\fad(60,40)\\fscx92\\fscy92\\t(0,120,\\fscx100\\fscy100)}}{txt}')
    open(path, 'w', encoding='utf-8').write(head + '\n'.join(ev) + '\n')


# ---------- görüntü ----------
def _font(name, size):
    from PIL import ImageFont
    return ImageFont.truetype(os.path.join(FONTS, name), size)
def _cover(src, w, h):
    s = max(w / src.width, h / src.height); im = src.resize((int(src.width * s + 1), int(src.height * s + 1)), Image.LANCZOS)
    l, t = (im.width - w) // 2, max(0, (im.height - h) // 3); return im.crop((l, t, l + w, t + h))
def _up(t): return t.replace('i', 'İ').replace('ı', 'I').upper()

def frames(p, photos, tmp, credits=''):
    """Her fotoğraf 2 kat çözünürlükte (kaydırma için), sabit üst/alt katman ve kapanış kartı."""
    srcs = [Image.open(x).convert('RGB') for x in photos if x and os.path.exists(x)] or [Image.new('RGB', (SW, SH), (46, 92, 64))]
    bps = []
    for k, src in enumerate(srcs):
        bp = os.path.join(tmp, f'big{k}.jpg'); _cover(src, SW * 2, SH * 2).save(bp, quality=88); bps.append(bp)
    ov = Image.new('RGBA', (SW, SH), (0, 0, 0, 0)); g = Image.new('L', (1, SH))
    for y in range(SH):
        a = 150 * max(0, 1 - y / 420) ** 1.6 + 175 * max(0, (y - SH * 0.45) / (SH * 0.55)) ** 1.4
        g.putpixel((0, y), int(min(220, a)))
    ov.paste(Image.new('RGBA', (SW, SH), (10, 16, 12, 255)), (0, 0), g.resize((SW, SH)))
    d = ImageDraw.Draw(ov)
    _gen = SW - 160   # uzun adlar taşmasın: önce küçült, gerekirse alt satıra sar
    def _yaz(x, y, metin, dosya, boy, renk, kucuk=None, satir=2):
        for b in range(boy, (kucuk or boy) - 1, -4):
            f = _font(dosya, b)
            L, cur = [], ''
            for w in metin.split():
                t = (cur + ' ' + w).strip()
                if not cur or d.textlength(t, font=f) <= _gen: cur = t
                else: L.append(cur); cur = w
            if cur: L.append(cur)
            if len(L) <= satir and all(d.textlength(l, font=f) <= _gen for l in L): break
        for l in L[:satir]: d.text((x, y), l, font=f, fill=renk); y += int(b * 1.12)
        return y
    _y = _yaz(80, 110, _up(p['tr']), 'AlegreyaSans-Bold.ttf', 58, (255, 255, 255), 40)
    _yaz(80, max(182, _y + 6), p['la'], 'AlegreyaSans-Italic.ttf', 40, (236, 226, 205), 28)
    d.text((80, SH - 150), 'bitkitabani.com', font=_font('AlegreyaSans-Bold.ttf', 42), fill=(240, 226, 196))
    if credits: d.text((80, SH - 88), ('Fotoğraflar: ' + credits)[:110], font=_font('AlegreyaSans-Regular.ttf', 22), fill=(220, 214, 200))
    op = os.path.join(tmp, 'ov.png'); ov.save(op)
    end = _cover(srcs[0], SW, SH).filter(ImageFilter.GaussianBlur(28)); end.paste(Image.new('RGB', (SW, SH), (12, 18, 14)), (0, 0), Image.new('L', (SW, SH), 150))
    d = ImageDraw.Draw(end); f1, f2 = _font('AlegreyaSans-Bold.ttf', 84), _font('AlegreyaSans-Bold.ttf', 64)
    y = 720
    for ln in ['Kaynaklarıyla', 'birlikte tamamı', 'sitede']: d.text((80, y), ln, font=f1, fill=(255, 255, 255)); y += 100
    d.text((80, y + 40), 'bitkitabani.com', font=f2, fill=(240, 226, 196))
    d.text((80, y + 130), 'Her gün yeni bir bitki · @bitkitabani', font=_font('AlegreyaSans-Regular.ttf', 38), fill=(236, 230, 218))
    ep = os.path.join(tmp, 'end.png'); end.save(ep)
    return bps, op, ep

# her sahnede görüntü sağdan sola kayar (kamera sağa ilerler), hafif yakınlaşmayla
MOVE = ("1.18+0.06*on/{N}", "(iw-iw/zoom)*(0.5+0.5*sin(PI*on/{N}-PI/2))", "ih/2-(ih/zoom/2)")
# sinematik görünüm: sıcak renk, hafif kontrast, vinyet, ince film greni, yumuşak keskinlik
GRADE = ("eq=contrast=1.06:saturation=1.14:gamma=0.98,colorbalance=rs=0.04:gs=0.01:bs=-0.05:rm=0.03:bm=-0.03,"
         "vignette=angle=PI/4.6:mode=forward,unsharp=5:5:0.4,noise=alls=5:allf=t+u")

def _ambient(seed, total):
    rr = random.Random(seed)
    ch = rr.choice([(110, 220, 261.63, 329.63), (73.42, 146.83, 220, 293.66), (82.41, 164.81, 246.94, 329.63), (98, 196, 246.94, 293.66)])
    e = '+'.join(f'{a:.3f}*sin(2*PI*{f}*t)*(0.65+0.35*sin(2*PI*{m:.3f}*t+{ph}))' for f, a, m, ph in
                 [(ch[0], .10, .07, 0), (ch[1], .07, .11, 1), (ch[2], .05, .13, 2), (ch[3], .04, .09, 3)])
    return (f"aevalsrc='{e}|{e}':s=44100:d={total:.2f},lowpass=f=1400,aecho=0.8:0.6:420|830:0.22|0.15,"
            f"afade=t=in:d=1.5,afade=t=out:st={max(0, total - 2):.2f}:d=2")

def make(p, m, img_path, out, photos=None):
    if not shutil.which('ffmpeg'): return False
    tmp = tempfile.mkdtemp()
    try:
        sents = script(p, m)
        ses_kaydi(p, sents, out)          # ses üretilmeden ÖNCE: metin ve kaynağı diske yazılır
        sents = okunacak(out)             # seslendirme yalnızca o dosyadan okunur
        segs, spoken, total = voice(sents, tmp)
        _ses_sakla(segs, tmp, _taban(out) + '.ses.mp3')
        kayda_ekle(out, sesli=bool(spoken), ses_dosyasi=os.path.basename(_taban(out)) + '.ses.mp3', sure=round(total, 1),
                   **({'hiza': round(_SON_HIZA, 4)} if _SON_HIZA is not None else {}),
                   **({'yontem': _SON_YONTEM} if _SON_YONTEM else {}))
        total += 0.5
        credits = ''
        if photos is None:   # ana fotoğraf + varsa tools/tanima.py'nin seçtiği çiçekli hâl, çizim, kurutulmuş hâl
            photos, cr = [img_path], []
            tdir = os.path.join(ROOT, 'img', 'tanima'); tm = os.path.join(tdir, 'meta.json')
            meta = json.load(open(tm, encoding='utf-8')) if os.path.exists(tm) else {}
            for tur in ('cicek', 'cizim', 'kuru'):
                x = meta.get(f"{p['id']}:{tur}"); f = os.path.join(tdir, f"{p['id']}-{tur}.jpg")
                if isinstance(x, dict) and os.path.exists(f): photos.append(f); cr.append(f"{x.get('artist', '')} ({x.get('license', '')})")
            credits = '; '.join(dict.fromkeys(cr))
        bps, op, ep = frames(p, photos, tmp, credits)
        sub = os.path.join(tmp, 'cap.ass'); ass(segs, sub)
        # sahneler: her cümle bir hareket; son cümle kapanış kartı
        cuts = [s[0] for s in segs] + [total]
        scenes = [(cuts[0] if i == 0 else cuts[i], cuts[i + 1]) for i in range(len(segs))]
        scenes[0] = (0, scenes[0][1])
        args = ['ffmpeg', '-y', '-loglevel', 'error']; fl = []
        for i, (a, b) in enumerate(scenes):
            dur = (b - a) + (XF if i < len(scenes) - 1 else 0); N = max(2, int(dur * FPS))
            last = i == len(scenes) - 1
            args += ['-i', ep if last else bps[i % len(bps)]]
            if last: fl.append(f"[{i}:v]scale={SW}:{SH},zoompan=z='1+0.03*on/{N}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={N}:s={SW}x{SH}:fps={FPS},setsar=1,format=yuv420p[v{i}]")
            else:
                z, x, y = (s.format(N=N) for s in MOVE)
                fl.append(f"[{i}:v]zoompan=z='{z}':x='{x}':y='{y}':d={N}:s={SW}x{SH}:fps={FPS},setsar=1,{GRADE},format=yuv420p[v{i}]")
        cur, off = 'v0', scenes[0][1] - scenes[0][0]
        for i in range(1, len(scenes)):
            o = f'x{i}'; fl.append(f"[{cur}][v{i}]xfade=transition={'slideleft' if i < len(scenes) - 1 else 'fade'}:duration={XF}:offset={off:.2f}[{o}]"); cur = o; off += scenes[i][1] - scenes[i][0]
        n = len(scenes); args += ['-i', op]
        subf = sub.replace('\\', '/').replace(':', '\\:'); fdir = FONTS.replace('\\', '/').replace(':', '\\:')
        fl.append(f"[{cur}][{n}:v]overlay=0:0:enable='lt(t,{scenes[-1][0]:.2f})'[ov];[ov]subtitles='{subf}':fontsdir='{fdir}',format=yuv420p[vout]")
        # ses: cümleler kendi zamanlarında + kısık ambiyans
        ai = n + 1; mix = []
        for (st, d, mp3, _) in segs:
            if mp3:
                args += ['-i', mp3]; ms = int(st * 1000)
                fl.append(f"[{ai}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{ai}]"); mix.append(f'[a{ai}]'); ai += 1
        args += ['-f', 'lavfi', '-i', _ambient(p['id'], total)]
        fl.append(f"[{ai}:a]volume={0.35 if spoken else 1.4}[amb]"); mix.append('[amb]')
        fl.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=longest,atrim=0:{total:.2f},alimiter=limit=0.95[aout]")
        args += ['-filter_complex', ';'.join(fl), '-map', '[vout]', '-map', '[aout]', '-t', f'{total:.2f}',
                 '-c:v', 'libx264', '-preset', 'medium', '-crf', '22', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', out]
        r = subprocess.run(args, capture_output=True, text=True)
        if r.returncode != 0: print('reel hatası:', r.stderr[-600:]); return False
        json.dump({'sesli': spoken, 'metin': sents, 'sure': round(total, 1), 'slug': p['id']},
                  open(os.path.splitext(out)[0] + '.json', 'w', encoding='utf-8'), ensure_ascii=False)
        tamam, sebep = kapi(out, p['id'])   # yayın kapısı: geçmezse video bırakılmaz
        if not tamam:
            print('reel: KAPI DURDURDU —', p['id'], '—', sebep)
            for x in (out, _taban(out) + '.ses.mp3'):
                if os.path.exists(x): os.remove(x)
            return False
        return True
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == '__main__':   # deneme: python3 tools/reel.py zencefil out.mp4
    import sys
    sys.path.insert(0, HERE); import ig2
    data = json.load(open(os.path.join(ROOT, '.cache', 'ig_input.json'), encoding='utf-8'))
    P = {x['id']: x for x in data['p']}; pid = sys.argv[1] if len(sys.argv) > 1 else 'zencefil'
    img = next((x for x in [os.path.join(ROOT, 'img', f'{pid}-1280.jpg'), os.path.join(ROOT, 'img', f'{pid}-960.jpg')] if os.path.exists(x)), None)
    print(script(P[pid], ig2.text_for(P[pid])))
    print('ok' if make(P[pid], ig2.text_for(P[pid]), img, sys.argv[2] if len(sys.argv) > 2 else 'reel_deneme.mp4') else 'HATA')
