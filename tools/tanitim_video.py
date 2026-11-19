# -*- coding: utf-8 -*-
"""Site özelliklerinin mobil ekran kaydı + seslendirme (tanıtım videosu).

Kullanım:  python3 tools/tanitim_video.py [kopruler|bitki-bul|hepsi]
Çıktı:     tanitim/<ad>.mp4  (1080x1920, 9:16)

Yöntem: yerel sunucuda site/ yayına alınır; Chromium telefon ekranı ölçüsünde
(360x640, 3x) açılır; her anlatım cümlesi bir "sahne"dir. Durağan sahne tek
kareden üretilir, kaydırmalı sahne JPEG kare dizisinden. Ses önce üretilir,
sahne süreleri cümlenin süresine göre belirlenir; böylece ses ile görüntü
kendiliğinden hizalanır.
"""
import asyncio, json, os, shutil, subprocess, sys, time, http.server, socketserver, threading

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(HERE, 'site')
OUT = os.path.join(HERE, 'tanitim')
TMP = os.path.join(OUT, '.tmp')
PORT = 8787
FPS = 24
GENISLIK, YUKSEKLIK, OLCEK = 360, 640, 3      # 360*3 = 1080, 640*3 = 1920
SES = os.environ.get('TANITIM_SES', 'tr-TR-EmelNeural')
ARA = 0.55                                     # cümleler arası sessizlik (sn)


# ---------------------------------------------------------------- ses
async def _tts(metin, yol):
    import edge_tts
    c = edge_tts.Communicate(metin, SES, rate='+6%')
    with open(yol, 'wb') as f:
        async for ch in c.stream():
            if ch['type'] == 'audio': f.write(ch['data'])


def _sure(yol):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                        '-of', 'default=nw=1:nk=1', yol], capture_output=True, text=True)
    return float(r.stdout.strip())


def seslendir(cumleler, klasor):
    """Her cümleyi seslendirir; [(wav, süre)] döner."""
    os.makedirs(klasor, exist_ok=True)
    cikti = []
    for i, c in enumerate(cumleler):
        mp3 = os.path.join(klasor, f'c{i}.mp3')
        wav = os.path.join(klasor, f'c{i}.wav')
        if not os.path.exists(wav):
            asyncio.run(_tts(c, mp3))
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', mp3, '-ac', '1', '-ar', '48000', wav], check=True)
        cikti.append((wav, _sure(wav)))
    return cikti


def ses_birlestir(parcalar, hedef):
    """Cümleler arasına ARA kadar sessizlik koyarak tek ses dosyası yapar."""
    sessiz = os.path.join(os.path.dirname(hedef), 'sessiz.wav')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i',
                    'anullsrc=r=48000:cl=mono', '-t', str(ARA), sessiz], check=True)
    liste = os.path.join(os.path.dirname(hedef), 'ses.txt')
    with open(liste, 'w') as f:
        for wav, _ in parcalar:
            f.write(f"file '{os.path.abspath(wav)}'\nfile '{os.path.abspath(sessiz)}'\n")
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
                    '-i', liste, '-c', 'copy', hedef], check=True)
    return hedef


# ---------------------------------------------------------------- sunucu
class _Sessiz(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


def sunucu_baslat():
    import functools
    isleyici = functools.partial(_Sessiz, directory=SITE)
    socketserver.TCPServer.allow_reuse_address = True
    sunucu = socketserver.TCPServer(('127.0.0.1', PORT), isleyici)
    threading.Thread(target=sunucu.serve_forever, daemon=True).start()
    return sunucu


# ---------------------------------------------------------------- kare çekimi
DOKUNMA_CSS = """
#bt-dokun{position:fixed;z-index:99999;width:56px;height:56px;margin:-28px 0 0 -28px;border-radius:50%;
 background:rgba(37,99,235,.28);border:2px solid rgba(37,99,235,.75);pointer-events:none;transition:none}
*{scroll-behavior:auto !important}
"""


class Cekim:
    def __init__(self, sayfa, klasor):
        self.s, self.k, self.n = sayfa, klasor, 0
        os.makedirs(klasor, exist_ok=True)

    def kare(self):
        self.n += 1
        self.s.screenshot(path=os.path.join(self.k, f'{self.n:05d}.jpg'), type='jpeg', quality=92)

    def bekle(self, sn):
        for _ in range(max(1, round(sn * FPS))): self.kare()

    def kaydir(self, hedef, sn):
        """Yumuşak (ease-in-out) kaydırma; süre boyunca kare çeker."""
        bas = self.s.evaluate('window.scrollY')
        n = max(2, round(sn * FPS))
        for i in range(1, n + 1):
            t = i / n
            e = 3 * t * t - 2 * t * t * t
            self.s.evaluate(f'window.scrollTo(0, {bas} + ({hedef} - {bas}) * {e})')
            self.kare()

    def kaydir_ogeye(self, secici, sn, pay=90):
        y = self.s.evaluate("""(s)=>{const el=document.querySelector(s);
            return el ? el.getBoundingClientRect().top + window.scrollY : window.scrollY;}""", secici)
        self.kaydir(max(0, y - pay), sn)

    def sahne(self, sure, eylem):
        """Eylemi çalıştırır, sahnenin kalan süresini durağan kareyle doldurur."""
        n0 = self.n
        eylem()
        kalan = sure - (self.n - n0) / FPS
        if kalan > 0.04: self.bekle(kalan)

    def dokun(self, secici, sn_once=0.45):
        """Dokunma halkasını gösterir, kare çeker, sonra tıklar."""
        el = self.s.query_selector(secici)
        if not el: raise RuntimeError('öge yok: ' + secici)
        el.scroll_into_view_if_needed()
        self.bekle(0.15)
        k = el.bounding_box()
        self.s.evaluate("""([x,y])=>{let d=document.getElementById('bt-dokun');
            if(!d){d=document.createElement('div');d.id='bt-dokun';document.body.appendChild(d);}
            d.style.left=x+'px';d.style.top=y+'px';d.style.opacity='1';}""",
                        [k['x'] + k['width'] / 2, k['y'] + k['height'] / 2])
        self.bekle(sn_once)
        self.s.evaluate("()=>{const d=document.getElementById('bt-dokun'); if(d) d.style.opacity='0';}")
        el.click()
        self.s.wait_for_timeout(350)


# ---------------------------------------------------------------- video
def video_yap(klasor, ses, hedef):
    ham = os.path.join(os.path.dirname(klasor), 'ham.mp4')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-framerate', str(FPS),
                    '-i', os.path.join(klasor, '%05d.jpg'),
                    '-vf', f'scale={GENISLIK*OLCEK}:{YUKSEKLIK*OLCEK}:flags=lanczos,format=yuv420p',
                    '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-r', str(FPS), ham], check=True)
    gecici = hedef + '.parca.mp4'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', ham, '-i', ses,
                    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k',
                    '-shortest', gecici], check=True)
    os.replace(gecici, hedef)
    return hedef


# ---------------------------------------------------------------- senaryolar
KOPRULER = [
    'Bitki Tabanı’nda kültür köprüleri, birbirinden binlerce kilometre uzaktaki halkların aynı bitkiyi ya da aynı molekülü neden benzer dertlere kullandığını gösteriyor.',
    'Haritadaki her yay bir köprü. Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika arasında on altı bağlantı var.',
    'Listeden ilkini açıyoruz: üzerlik ve ayahuasca sarmaşığı.',
    'İkisi de harmin ve harmalin taşıyor. Anadolu’da bu alkaloitler nazar dumanında yanıyor, Amazon’da tören içeceğinin omurgasını oluşturuyor.',
    'Yan yana tablo familyayı, kullanılan kısmı, bilimsel kanıt düzeyini, güvenliği ve Türkiye’deki yasal durumu birlikte veriyor.',
    'Aşağıda her kültür kendi anlatısıyla, kaynaklarıyla birlikte okunuyor.',
]

BITKI_BUL = [
    'Bana uygun bitki hangisi? Bitki Tabanı’nın üç soruluk bitki bulucusu.',
    'Önce derdini seçiyorsun: uyku, öksürük, mide, kaygı, eklem ağrısı.',
    'İkinci soru hamilelik ve emzirme.',
    'Üçüncü soru düzenli kullandığın ilaçlar. Riskli eşleşmeler listeden kendiliğinden eleniyor.',
    'Sonuçlar, bilimsel kanıtı en güçlü olandan başlayarak sıralanıyor.',
    'Hiçbiri tıbbi tavsiye değil: her kayıt kendi kaynaklarıyla birlikte açılıyor.',
]


def senaryo_kopruler(c, d):
    c.sahne(d[0], lambda: None)                                  # başlık ve giriş
    c.sahne(d[1], lambda: (c.kaydir(430, d[1] * 0.45),           # harita
                           c.kaydir(960, d[1] * 0.45)))          # köprü listesi
    c.sahne(d[2], lambda: c.dokun('p a[href="/kopruler/uzerlik-ayahuasca/"]'))
    c.sahne(d[3], lambda: (c.bekle(0.6), c.kaydir_ogeye('figure.brshot, figure', d[3] - 1.2)))
    c.sahne(d[4], lambda: c.kaydir_ogeye('table', d[4] - 0.3))
    c.sahne(d[5], lambda: (c.kaydir(2000, d[5] * 0.5), c.kaydir(2900, d[5] * 0.45)))


def senaryo_bitki_bul(c, d):
    c.sahne(d[0], lambda: None)                                  # başlık
    c.sahne(d[1], lambda: (c.kaydir_ogeye('.bbk', max(0.8, d[1] - 1.6), pay=70),
                           c.dokun('.bbk a[data-k="uyku"]')))
    c.sahne(d[2], lambda: (c.kaydir_ogeye('section[data-s="2"]', 0.8, pay=120),
                           c.dokun('button[data-h="0"]')))
    c.sahne(d[3], lambda: (c.kaydir_ogeye('section[data-s="3"]', 0.8, pay=110),
                           c.dokun('button[data-g="yok"]'),
                           c.bekle(0.35),
                           c.dokun('button.bbgo')))
    c.sahne(d[4], lambda: (c.bekle(0.5), c.kaydir_ogeye('.bbres', max(0.8, d[4] - 1.3), pay=110)))
    c.sahne(d[5], lambda: c.kaydir(c.s.evaluate('window.scrollY') + 1100, d[5] * 0.8))


ISLER = {
    'kopruler': ('/kopruler/', KOPRULER, senaryo_kopruler),
    'bitki-bul': ('/bitki-bul/', BITKI_BUL, senaryo_bitki_bul),
}


def uret(ad, sunucu_hazir=True):
    yol, cumleler, senaryo = ISLER[ad]
    is_tmp = os.path.join(TMP, ad)
    shutil.rmtree(os.path.join(is_tmp, 'kare'), ignore_errors=True)
    os.makedirs(is_tmp, exist_ok=True)
    print(f'{ad}: ses üretiliyor ({len(cumleler)} cümle)')
    parcalar = seslendir(cumleler, os.path.join(is_tmp, 'ses'))
    sahne = [s + ARA for _, s in parcalar]
    ses = ses_birlestir(parcalar, os.path.join(is_tmp, 'anlatim.wav'))
    print(f'{ad}: sahne süreleri', [round(s, 1) for s in sahne])

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--force-color-profile=srgb'])
        ctx = b.new_context(viewport={'width': GENISLIK, 'height': YUKSEKLIK},
                            device_scale_factor=OLCEK, is_mobile=True, has_touch=True,
                            locale='tr-TR', reduced_motion='reduce')
        sayfa = ctx.new_page()
        sayfa.add_style_tag  # (stil sayfa açıldıktan sonra eklenir)
        sayfa.goto(f'http://127.0.0.1:{PORT}{yol}', wait_until='load')
        sayfa.add_style_tag(content=DOKUNMA_CSS)
        sayfa.wait_for_timeout(700)
        c = Cekim(sayfa, os.path.join(is_tmp, 'kare'))
        senaryo(c, sahne)
        b.close()
    print(f'{ad}: {c.n} kare')
    os.makedirs(OUT, exist_ok=True)
    hedef = os.path.join(OUT, ad + '.mp4')
    video_yap(os.path.join(is_tmp, 'kare'), ses, hedef)
    print(f'{ad}: {hedef} · {round(os.path.getsize(hedef)/1e6,1)} MB · {round(_sure(hedef),1)} sn')
    return hedef


if __name__ == '__main__':
    hangi = (sys.argv[1] if len(sys.argv) > 1 else 'hepsi')
    adlar = list(ISLER) if hangi == 'hepsi' else [hangi]
    s = sunucu_baslat()
    try:
        for a in adlar: uret(a)
    finally:
        s.shutdown()
