"""Seslendirmeli ve altyazılı Reels (9:16, ~25 sn).

Metin, bitkinin hazır Instagram metninden (ig_metin.py ya da otomatik metin) kurulur; Claude ya da elle yazım gerekmez.
Ses: Microsoft Edge'in Türkçe sinir ağı sesi (edge-tts, tr-TR-EmelNeural). Altyazı, sesin kelime zamanlamasından
üretilir ve videoya gömülür. edge-tts kurulu değilse ya da ulaşılamazsa video yine üretilir: altyazı tahmini
zamanlamayla gösterilir, arkada yalnızca ambiyans müziği çalar.
"""
import os, re, json, asyncio, shutil, subprocess, tempfile, random
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(HERE, 'fonts')
VOICE = os.environ.get('REEL_VOICE', 'tr-TR-EmelNeural')
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
    try: c = edge_tts.Communicate(text, VOICE, rate='+5%', boundary='WordBoundary')
    except TypeError: c = edge_tts.Communicate(text, VOICE, rate='+5%')
    words = []
    with open(path, 'wb') as f:
        async for ch in c.stream():
            if ch['type'] == 'audio': f.write(ch['data'])
            elif ch['type'] == 'WordBoundary': words.append([ch['offset'] / 1e7, (ch['offset'] + ch['duration']) / 1e7, ch['text']])
    return words

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

def voice(sents, tmp):
    """Her cümle ayrı seslendirilir: [(başlangıç, süre, mp3 ya da None, kelimeler)] ve sesli mi?"""
    segs, t, ok = [], 0.15, True
    for i, s in enumerate(sents):
        mp3, ws, d = os.path.join(tmp, f's{i}.mp3'), None, 0
        if ok:
            try:
                ws = asyncio.run(_tts1(s, mp3)); d = _dur(mp3)
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
    d.text((80, 110), _up(p['tr']), font=_font('AlegreyaSans-Bold.ttf', 58), fill=(255, 255, 255))
    d.text((80, 182), p['la'], font=_font('AlegreyaSans-Italic.ttf', 40), fill=(236, 226, 205))
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
MOVE = ("1.22+0.04*on/{N}", "(iw-iw/zoom)*on/{N}", "ih/2-(ih/zoom/2)")

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
        segs, spoken, total = voice(sents, tmp)
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
                fl.append(f"[{i}:v]zoompan=z='{z}':x='{x}':y='{y}':d={N}:s={SW}x{SH}:fps={FPS},setsar=1,format=yuv420p[v{i}]")
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
        json.dump({'sesli': spoken, 'metin': sents, 'sure': round(total, 1)}, open(os.path.splitext(out)[0] + '.json', 'w', encoding='utf-8'), ensure_ascii=False)
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
