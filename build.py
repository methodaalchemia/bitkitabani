import json, os, shutil, html, re, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
from refs import WIKI, POWO, NCCIH, EMA, OTHER, FILES, BAYTOP
from extra import EK, KORUMA, YASAL, YASAL_AD, BR_GEO, ALT
from etkilesim import ETK
from derin import D as DERIN
from gozden import KISI as GZ_KISI, SAYFALAR as GZ
KAN_AD = {'klinik': 'Klinik kanıt', 'sinirli': 'Sınırlı kanıt', 'geleneksel': 'Yalnızca geleneksel', 'yok': 'Kanıt yok'}
AUTHOR = {'@type': 'Person', 'name': 'Edanaz Tınmazlar', 'alternateName': 'Edanaz Tinmazlar', 'url': 'https://bitkitabani.com/yontem/#hazirlayan', 'jobTitle': 'Sanatçı ve şifalı bitkiler uzmanı', 'sameAs': ['https://www.linkedin.com/in/edanaz-tinmazlar-%E6%B8%B8%E5%AD%90%E6%84%8F-588285110/', 'https://www.instagram.com/teda.naz/']}
SOCIAL = '<span class="social"><a href="https://www.linkedin.com/in/edanaz-tinmazlar-%E6%B8%B8%E5%AD%90%E6%84%8F-588285110/" rel="me noopener">LinkedIn</a> · <a href="https://www.instagram.com/teda.naz/" rel="me noopener">Instagram</a></span>'
BIO = 'Edanaz Tınmazlar, sanatçı; şifalı ve ritüel bitkiler üzerine araştırıyor ve yazıyor. Beyaz yakalı hayatından şifa arayışına düştü ve kendini bitkilerin benzersiz dünyasını anlamaya çalışırken buldu. Dünyanın birçok ülkesinde gezip yaşadıktan sonra Türkiye’ye döndü; köklerini anlamayı ve anlatmayı kendine görev edindi.'
import mapgeo, math
IMG = json.load(open(os.path.join(HERE, 'images.json'), encoding='utf-8')) if os.path.exists(os.path.join(HERE, 'images.json')) else {}

BASE = 'https://bitkitabani.com'
OUT = os.path.join(HERE, 'site')
shutil.rmtree(OUT, ignore_errors=True)   # her derleme temiz başlar: kaldırılan sayfalar yayında kalmasın
D = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))
REG, KAT, KANIT, GUV, P, BR, EXTRA = D['REG'], D['KAT'], D['KANIT'], D['GUV'], D['P'], D['BR'], D['EXTRA']
for i, p in enumerate(P): p['no'] = i + 1
GUV['yuksek'] = 'Yüksek risk'
byId = {p['id']: p for p in P}
INAT = json.load(open(os.path.join(HERE, 'inat.json'), encoding='utf-8')) if os.path.exists(os.path.join(HERE, 'inat.json')) else {}
AYLAR = ['ocak', 'şubat', 'mart', 'nisan', 'mayıs', 'haziran', 'temmuz', 'ağustos', 'eylül', 'ekim', 'kasım', 'aralık']
def inat_satir(pid):
    x = INAT.get(pid) or {}
    if not x.get('toplam') or x['toplam'] < 5: return ''
    ay = x['ay']; m = max(ay); yog = [i for i in range(12) if ay[i] >= m * 0.5]
    bar = ''.join(f'<span title="{AYLAR[i].capitalize()}: {ay[i]}" style="height:{max(2, round(28 * ay[i] / m))}px"></span>' for i in range(12))
    return (f'<div><dt>Türkiye’de gözlem</dt><dd><span class="inat-bar" aria-hidden="true">{bar}</span> {x["toplam"]} doğrulanmış gözlem; en çok {AYLAR[yog[0]]}–{AYLAR[yog[-1]]} aylarında. '
            f'<a href="https://www.inaturalist.org/observations?taxon_id={x["taxon_id"]}&amp;place_id=7183&amp;quality_grade=research" rel="noopener">iNaturalist</a></dd></div>')
_TM = os.path.join(HERE, 'img', 'tanima', 'meta.json')
TANIMA = json.load(open(_TM, encoding='utf-8')) if os.path.exists(_TM) else {}
TANIMA_AD = {'cizim': 'Botanik çizim', 'cicek': 'Çiçekli hâli', 'kuru': 'Kurutulmuş hâli'}
def tanima_html(pid, h2=True):
    figs = []
    for t in ('cizim', 'cicek', 'kuru'):
        x = TANIMA.get(f'{pid}:{t}')
        if isinstance(x, dict) and os.path.exists(os.path.join(HERE, 'img', 'tanima', f'{pid}-{t}.jpg')):
            figs.append(f'<figure class="tn-{t}"><img src="/img/tanima/{pid}-{t}.jpg" alt="{TANIMA_AD[t]}" loading="lazy" width="400" height="500"><figcaption><b>{TANIMA_AD[t]}</b><br><a href="{x["page"]}" rel="noopener">{e(x.get("artist", ""))}</a> · {e(x.get("license", ""))}</figcaption></figure>')
    if not figs: return ''
    return (f'<section class="sec" id="tanima"><h2>Nasıl tanınır?</h2>' if h2 else '') + f'<div class="tanima">{"".join(figs)}</div>' + ('</section>' if h2 else '')
# kaynaklı halk hekimliği kayıtları (halk.py): bitki sayfasının geleneksel kullanım bölümüne ve kaynaklarına eklenir
from halk import site_kul as _site_kul
from ege import EGE, KAYNAK as EGE_KAYNAK
def ege_html(pid, ad):
    x = EGE.get(pid)
    if not x: return ''
    c = []
    if x.get('genel'):
        sira, kay, yay = x['genel']
        c.append(f'Türkiye’de 1928–2014 arasında yapılmış etnobotanik çalışmalarda en sık kaydedilen {sira}. bitki: {yay} yayında {kay} kullanım kaydı.')
    if x.get('kul'): c.append(f'Tıbbi kullanımı {x["lit"]} yayında kayıtlı. En sık geçen amaçlar (yayın sayısı): {x["kul"]}.')
    if x.get('alan'):
        c.append('Halk arasında en sık kullanılan bitkiler sıralamasında: ' + '; '.join(f'{a} için {i}. sırada ({cs} çalışma)' for a, i, k, cs in x['alan']) + '.')
    if x.get('adlar'): c.append(f'Kayıtlı yöresel adları (çalışma sayısı): {x["adlar"]}.')
    if x.get('yaraotu'): c.append(f'{x["yaraotu"]}’da “yara otu” adıyla anılıyor.')
    return ('<aside class="ege"><h3>Türkiye’deki halk kayıtları</h3>' + ''.join(f'<p>{e(t)}</p>' for t in c) +
            f'<p class="muted-s">Bunlar halk arasında kayıtlı kullanımlardır, etkinlik kanıtı değildir. Kaynak: <a href="{EGE_KAYNAK[1]}" target="_blank" rel="noopener">Türkiye’nin Etnobotanik Veritabanı (Ege Üniversitesi, 2020)</a>; 930 çalışmadan 81.526 kayıt.</p></aside>')
_hk, _hs = _site_kul()
for _i, _u in _hk.items():
    if _i in byId: byId[_i]['kul'] = [list(x) for x in byId[_i]['kul']] + [list(x) for x in _u]
for _i, _s in _hs.items():
    for _x in _s:
        if _x not in OTHER.get(_i, []): OTHER.setdefault(_i, []).append(_x)
TODAY =datetime.date.today().isoformat()
def _git_date():
    try:
        import subprocess
        out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', 'data.json', 'extra.py', 'refs.py', 'build.py'], cwd=HERE, capture_output=True, text=True, timeout=10).stdout.strip()
        return out or TODAY
    except Exception:
        return TODAY
CONTENT_DATE = _git_date()
try:
    _wr = re.sub(r'^\s*//.*$', '', open(os.path.join(HERE, 'wrangler.jsonc'), encoding='utf-8').read(), flags=re.M)
    GOOGLE_CLIENT_ID = json.loads(_wr).get('vars', {}).get('GOOGLE_CLIENT_ID', '')
except Exception:
    GOOGLE_CLIENT_ID = ''
try:
    from zoneinfo import ZoneInfo
    LOCAL_DAY = datetime.datetime.now(ZoneInfo('Europe/Istanbul')).date()
except Exception:
    LOCAL_DAY = datetime.date.today()
if os.environ.get('BT_DAY'): LOCAL_DAY = datetime.date.fromisoformat(os.environ['BT_DAY'])   # deneme için

# ---------- yayın kuyruğu: her gün bir yeni bitki (kuyruk/ klasörü) ----------
import kuyruk as _K
YENI, EN_NEW, ETK_EN_NEW, KUYRUK_LEFT = {}, {}, {}, []
for _q in _K.Q:
    _d = datetime.date.fromisoformat(_q['yayin'])
    if _q['id'] in byId: continue
    if _d > LOCAL_DAY: KUYRUK_LEFT.append(_q); continue
    _q = dict(_q); _id = _q['id']; YENI[_id] = _d
    EK[_id] = _q.pop('ek'); POWO[_id] = _q.pop('taxon')
    EN_NEW[_id] = _q.pop('en')
    if _q.get('etk_en'): ETK_EN_NEW[_id] = _q['etk_en']
    if _q.get('etk'): ETK[_id] = _q['etk']
    if _q.get('ema'): EMA[_id] = _q['ema']
    if _q.get('nccih'): NCCIH[_id] = _q['nccih']
    if _q.get('kaynak'): OTHER.setdefault(_id, []).extend(_q['kaynak'])
    if _q.get('koruma'): KORUMA[_id] = _q['koruma']
    if _q.get('yasal'): YASAL[_id] = _q['yasal']
    EXTRA[_id] = list(_q.get('rel', []))
    for _r in _q.get('rel', []):
        if _r in byId or _r in YENI: EXTRA.setdefault(_r, []).append(_id)
    for _k in ('etk', 'etk_en', 'ema', 'nccih', 'kaynak', 'koruma', 'yasal', 'rel', 'yayin', 'foto', 'ig'): _q.pop(_k, None)
    P.append(_q); byId[_id] = _q
for i, p in enumerate(P): p['no'] = i + 1
NEWEST = sorted(YENI, key=lambda k: YENI[k], reverse=True)
def is_new(pid, days=7): return pid in YENI and (LOCAL_DAY - YENI[pid]).days < days
AYLAR =['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
GUNLER = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
def tr_date(d): return f'{d.day} {AYLAR[d.month-1]} {d.year}, {GUNLER[d.weekday()]}'
def slug_of(br): return br['a'] + ('-' + br['b'] if br.get('b') else '')
e = lambda s: html.escape(str(s), quote=True)

# ---------- simgeler (basit çizgi simgeleri) ----------
IC = {'share': 'M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7 M12 3v13 M7 8l5-5 5 5', 'link': 'M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1 M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1',
      'print': 'M6 9V3h12v6 M6 18H4v-7h16v7h-2 M6 14h12v7H6z', 'chat': 'M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.9A8 8 0 1 1 21 12z',
      'uyku': 'M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z', 'oksuruk': 'M3 8h11a3 3 0 1 0-3-3 M3 12h15a3 3 0 1 1-3 3 M3 16h7', 'bogaz-agrisi': 'M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z',
      'mide-hazimsizlik': 'M5 19c0-8 5-14 14-14 0 9-6 14-14 14z M5 19l8-8', 'bulanti': 'M3 9c3-3 6 3 9 0s6 3 9 0 M3 15c3-3 6 3 9 0s6 3 9 0', 'soguk-alginligi': 'M12 2v20 M3.5 7l17 10 M20.5 7l-17 10',
      'kaygi-stres': 'M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z', 'eklem-agrisi': 'M8 8l8 8 M5 9a2 2 0 1 1 1.5-3.5A2 2 0 1 1 9 4 M19 15a2 2 0 1 1-1.5 3.5A2 2 0 1 1 15 20',
      'kabizlik': 'M12 4v14 M7 13l5 5 5-5', 'idrar-yolu': 'M8 4s4 5 4 8a4 4 0 0 1-8 0c0-3 4-8 4-8z M16 10s3 3.5 3 6a3 3 0 0 1-6 0c0-2.5 3-6 3-6z', 'kolesterol-tansiyon': 'M3 12h4l2-5 4 10 2-5h6',
      'cilt-yara': 'M8 3l13 13-5 5L3 8z M10 10l4 4', 'bacak-damar': 'M8 3c0 6 4 6 4 12s-2 6-2 6 M16 3c0 4-3 6-3 9', 'adet': 'M12 3a9 9 0 1 0 0 18 9 9 0 1 0 0-18z M12 3v18',
      'prostat': 'M12 3l7 3v6c0 5-3 8-7 9-4-1-7-4-7-9V6z', 'hafiza': 'M12 3v4 M12 17v4 M3 12h4 M17 12h4 M6 6l2.5 2.5 M15.5 15.5L18 18 M6 18l2.5-2.5 M15.5 8.5L18 6',
      'etk': 'M8 16l8-8a3.5 3.5 0 0 1 5 5l-8 8a3.5 3.5 0 0 1-5-5z M12 12l4 4', 'gebe': 'M12 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4z M12 9v4c3 0 4 2 4 4s-2 4-4 4 M12 13v8',
      'tarif': 'M5 10h12v5a5 5 0 0 1-5 5h-2a5 5 0 0 1-5-5z M17 11h2a2 2 0 0 1 0 4h-2 M9 3c0 2 2 2 2 4 M13 3c0 2 2 2 2 4', 'takvim': 'M4 6h16v14H4z M4 10h16 M8 3v5 M16 3v5',
      'adlar': 'M4 5h16 M4 10h10 M4 15h16 M4 20h8', 'kars': 'M8 4v16 M16 4v16 M4 8h8 M12 16h8'}
def ico(n, cls='ico'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{IC[n]}"/></svg>' if n in IC else ''

# ---------- paylaş / yazdır çubuğu ----------
def sharebar(title, path):
    u = urllib.parse.quote(BASE + path, safe=''); t = urllib.parse.quote(title, safe='')
    wa = _icon('whatsapp', '') if os.path.exists(os.path.join(HERE, 'assets', 'icons', 'whatsapp.svg')) else ico('chat')
    return f'''<div class="sharebar noprint" data-url="{BASE}{path}" data-title="{e(title)}"><button type="button" class="sb-share" title="Paylaş" aria-label="Paylaş">{ico('share')}</button><a class="sb-wa" href="https://wa.me/?text={t}%20{u}" rel="noopener" target="_blank" title="WhatsApp’ta paylaş" aria-label="WhatsApp’ta paylaş">{wa}</a><button type="button" class="sb-copy" title="Bağlantıyı kopyala" aria-label="Bağlantıyı kopyala">{ico('link')}</button><button type="button" class="sb-print" title="Yazdır" aria-label="Yazdır">{ico('print')}</button><span class="sb-msg muted-s" role="status"></span></div>'''

# ---------- bülten kayıt kutusu ----------
def abone(kaynak, baslik='Ücretsiz e-posta kursu: Şifalı bitkilere başlangıç', alt='7 gün boyunca her sabah kısa, görsel bir ders: kanıtı okumak, doğru demlemek, güvenli kullanmak, doğada toplamak. Sonra her pazar haftanın bitkileri. Yazdırılabilir “Bitki–ilaç etkileşimi kartı” da hediye.', kurs=True):
    return f'''<section class="abone" aria-labelledby="ab-{kaynak[:20]}"><h2 id="ab-{kaynak[:20]}">{baslik}</h2><p>{alt}</p>
<form class="abone-form" data-kaynak="{e(kaynak)}"{' data-kurs="1"' if kurs else ''} novalidate><label class="vh" for="ab-e-{kaynak[:20]}">E-posta adresi</label><div class="row"><input id="ab-e-{kaynak[:20]}" type="email" name="email" placeholder="e-posta adresin" autocomplete="email" required><button type="submit" class="learn">{'Kursa başla' if kurs else 'Kaydol'}</button></div>
<input type="text" name="hp" tabindex="-1" autocomplete="off" class="vh" aria-hidden="true">
<label class="chk"><input type="checkbox" name="riza" required><span>{'E-posta adresimin 7 günlük kurs ve ardından haftalık bülten için saklanmasına ve bana e-posta gönderilmesine izin veriyorum.' if kurs else 'E-posta adresimin haftalık bülten için saklanmasına ve bana e-posta gönderilmesine izin veriyorum.'} <a href="/gizlilik/#bulten">Ayrıntılar</a></span></label>
<label class="chk"><input type="checkbox" name="duyuru"><span>İsteğe bağlı: Bitki Tabanı’nın atölye, doğa yürüyüşü ve gezi gibi duyurularını da almak istiyorum.</span></label>
<p class="muted-s abone-msg" role="status"></p></form><p class="tg-cta"><a class="cta" href="https://t.me/bitkitabani" rel="noopener" target="_blank">Telegram kanalında her akşam bir bitki →</a> <span class="muted-s">Bildirimle gelir, e-posta gerekmez.</span></p></section>'''

# ---------- rehber, tarif ve karşılaştırma bağlantıları (bitki sayfalarına da eklenir) ----------
from rehber import KONULAR
if 'pasiflora' not in byId:   # çarkıfelek kataloğa girene kadar rehber metinlerinde anılmaz
    for _k in KONULAR:
        for _f in ('ozet', 'aciklama'):
            if isinstance(_k.get(_f), str): _k[_f] = _k[_f].replace('Kediotu, melisa ve çarkıfelek', 'Kediotu ve melisa').replace(', çarkıfelek ve ashwagandha', ' ve ashwagandha')
from tarif import TARIFLER
# --- yöre haritası: saha çalışmalarında bitkilerin kaydedildiği iller ---
import trmap as _TM
from yore import CALISMALAR as _YC, KAYIT as _YK, DETAY as _YD
_YCAL = {c['id']: c for c in _YC}
YORE_BITKI = {}   # bitki id → [çalışma]
YORE_IL = {}      # il → {'cal': [çalışma], 'bitki': {bitki id: [çalışma]}}
for _cid, _pid in _YK:
    if _pid not in byId: continue
    _c = _YCAL[_cid]
    YORE_BITKI.setdefault(_pid, []).append(_c)
    _d = YORE_IL.setdefault(_c['il'], {'cal': [], 'bitki': {}})
    if _c not in _d['cal']: _d['cal'].append(_c)
    _d['bitki'].setdefault(_pid, []).append(_c)
def _ilslug(il): return re.sub(r'[^a-z0-9]+', '-', il.lower().translate(str.maketrans('çğıöşüâîİ', 'cgiosuaii')).replace('i̇', 'i')).strip('-')
YORE_SAYFA = {il for il, d in YORE_IL.items() if len(d['bitki']) >= 8}   # az kayıtlı iller ince sayfa olmasın diye yayınlanmaz
def _ydet(c, pid):
    d = _YD.get(f"{c['id']}:{pid}")
    if not d: return ''
    return ' (' + '; '.join(x for x in [('yöresel adları: ' + e(d['ad'])) if d.get('ad') else '', ('kullanım: ' + e(d['kul'])) if d.get('kul') else ''] if x) + ')'
def _cal_ref(c): return f'<a href="{c["url"]}" target="_blank" rel="noopener">{e(c["yazar"])}, {c["yil"]}</a>'
def yore_html(pid):
    L = YORE_BITKI.get(pid)
    if not L: return ''
    by = {}
    for c in L: by.setdefault(c['il'], []).append(c)
    items = []
    for il in sorted(by, key=_trkey0):
        ad = f'<a href="/yore/{_ilslug(il)}/">{e(il)}</a>' if il in YORE_SAYFA else e(il)
        items.append(f'<li><b>{ad}</b>' + (' (' + ', '.join(e(c['ilce']) for c in by[il] if c['ilce']) + ')' if any(c['ilce'] for c in by[il]) else '') + ' · ' + '; '.join(_cal_ref(c) + _ydet(c, pid) for c in by[il]) + '</li>')
    return (f'<aside class="yore-k"><h3>Saha çalışmalarında kaydedildiği yöreler</h3><ul>{"".join(items)}</ul>'
            f'<p class="muted-s"><a href="/yoreler/">Bütün yöreler haritada →</a></p></aside>')
def halk_kutu(pid, ad):
    a, b = ege_html(pid, ad), yore_html(pid)
    if a and b:   # tek kutu: önce veritabanı sayıları, sonra yöreler
        b = b.replace('<aside class="yore-k"><h3>Saha çalışmalarında kaydedildiği yöreler</h3>', '<h4>Saha çalışmalarında kaydedildiği yöreler</h4>').replace('</aside>', '')
        return a.replace('<p class="muted-s">Bunlar halk', b + '<p class="muted-s">Bunlar halk', 1)
    return a or b
def _trkey0(w):
    T = 'abcçdefgğhıijklmnoöprsştuüvyz'
    return [(-1 if c == ' ' else T.index(c) if c in T else 100 + ord(c)) for c in w.replace('I', 'ı').replace('İ', 'i').lower()]
def tr_haritasi(vurgu=None):
    out = [f'<svg class="trmap" viewBox="{" ".join(map(str, _TM.VIEW))}" role="img" aria-label="Türkiye yöre haritası: saha çalışması olan iller renkli">']
    for il, d in _TM.IL.items():
        n = len(YORE_IL.get(il, {}).get('bitki', {}))
        cls = 'il' + (' var' if n else '') + (' on' if il == vurgu else '')
        if n:
            href = f'/yore/{_ilslug(il)}/' if il in YORE_SAYFA else f'/yoreler/#il-{_ilslug(il)}'
            out.append(f'<a href="{href}" aria-label="{e(il)}: {n} bitki"><path class="{cls}" d="{d}"><title>{e(il)}: {n} bitki</title></path></a>')
        else:
            out.append(f'<path class="{cls}" d="{d}"><title>{e(il)}</title></path>')
    for c in _YC:
        x, y = _TM.P(c['lon'], c['lat'])
        out.append(f'<circle class="nokta" cx="{x:.0f}" cy="{y:.0f}" r="6"><title>{e(c["il"])}{" · " + e(c["ilce"]) if c["ilce"] else ""}: {e(c["baslik"])}</title></circle>')
    return ''.join(out) + '</svg>'
def _il_bolum(il, d, baslik_tag='h2'):
    bl = sorted(d['bitki'], key=lambda q: _trkey0(byId[q]['tr']))
    chips = ''.join(f'<a class="chip" href="/{q}/">{e(byId[q]["tr"])}</a>' for q in bl)
    cal = ''.join(f'<li>{e(c["ilce"] + ": ") if c["ilce"] else ""}<a href="{c["url"]}" target="_blank" rel="noopener">{e(c["baslik"])}</a> · {e(c["yazar"])}, <i>{e(c["dergi"])}</i>, {c["yil"]}</li>' for c in d['cal'])
    return f'<{baslik_tag}>{e(il)} <small class="muted-s">· {len(bl)} bitki</small></{baslik_tag}><div class="related">{chips}</div><p class="muted-s">Kaynak saha çalışmaları:</p><ul class="srclist">{cal}</ul>'
from karsilastirma import KARS
from motifler import MOTIFLER, TEMALAR, ESKI as MOTIF_ESKI
from yazilar import YAZILAR
from kavramlar import KAVRAMLAR
KAV = sorted([k for k in KAVRAMLAR if datetime.date.fromisoformat(k['yayin']) <= LOCAL_DAY and k['bitki'] in byId], key=lambda k: k['yayin'])
KAV_TODAY = KAV[-1] if KAV else None
GLINKS = {}
def _glinks():
    for k in KONULAR:
        if sum(1 for x, _ in k['bitkiler'] if x in byId) < 2: continue
        for pid, _ in k['bitkiler']:
            if pid in byId: GLINKS.setdefault(pid, []).append((f'/rehber/{k["slug"]}/', 'Rehber: ' + k['kisa']))
    for t in TARIFLER:
        if t['bitki'] in byId: GLINKS.setdefault(t['bitki'], []).append((f'/tarif/{t["slug"]}/', 'Tarif: ' + t['ad']))
    for mo in MOTIFLER:
        for x, _ in mo['bitkiler']:
            if x in byId: GLINKS.setdefault(x, []).append((f'/semboller/{mo["slug"]}/', 'Sembol: ' + mo['ad']))
    for c in KARS:
        if c['a'] in byId and c['b'] in byId:
            for x in (c['a'], c['b']): GLINKS.setdefault(x, []).append((f'/karsilastirma/{c["a"]}-ve-{c["b"]}/', c['baslik']))
_glinks()

def related(pid):
    s = list(EXTRA.get(pid, []))
    for b in BR:
        if b['a'] == pid and b.get('b'): s.append(b['b'])
        if b.get('b') == pid: s.append(b['a'])
    out = []
    for x in s:
        if x != pid and x in byId and x not in out: out.append(x)
    return out

acc = lambda n: f'BT-{n:03d}'
dot = lambda r: f'<span class="dot" style="background:var({REG[r]["c"]})" title="{e(REG[r]["ad"])}"></span>'
def pips(k):
    n = KANIT[k]['n']
    return '<span class="pips" aria-hidden="true">' + ''.join(f'<i class="{"on" if i <= n else ""}"></i>' for i in (1,2,3)) + '</span>'
short_la = lambda p: p['la'].split(',')[0].strip()

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,500;0,700;0,800;1,400&family=Alegreya+Sans:ital,wght@0,400;0,700;1,400&family=Courier+Prime&display=swap">'
FONTS = '<script>try{var t=localStorage.getItem("bt-theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>' + FONTS
if os.path.exists(os.path.join(HERE, 'assets', 'fonts', 'alegreya.woff2')):   # yazı tipleri siteden: Google'a bağlantı yok, daha hızlı açılış
    _ff = [('Alegreya', 'alegreya', '400 900', 'normal'), ('Alegreya', 'alegreya-italic', '400 900', 'italic'), ('Alegreya Sans', 'alegreya-sans', '400', 'normal'),
           ('Alegreya Sans', 'alegreya-sans-bold', '700', 'normal'), ('Alegreya Sans', 'alegreya-sans-italic', '400', 'italic'), ('Courier Prime', 'courier-prime', '400', 'normal')]
    FONTS = ('<script>try{var t=localStorage.getItem("bt-theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>'
             '<link rel="preload" href="/assets/fonts/alegreya-sans.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/alegreya.woff2" as="font" type="font/woff2" crossorigin>'
             '<style>' + ''.join(f'@font-face{{font-family:"{fam}";src:url(/assets/fonts/{f}.woff2) format("woff2");font-weight:{w};font-style:{st};font-display:swap}}' for fam, f, w, st in _ff
                                 if os.path.exists(os.path.join(HERE, 'assets', 'fonts', f + '.woff2'))) + '</style>')
FAV = '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">'

def head(title, desc, path, extra='', image=None):
    url = BASE + path
    image = image or BASE + '/assets/logo-512.png'
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-BMP0ECQ163"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'G-BMP0ECQ163');
</script>
<meta name="robots" content="max-image-preview:large, max-snippet:-1">
<meta name="p:domain_verify" content="e3e9bfbe0eae8412bc7dead5c2e3540e"/><meta name="yandex-verification" content="47d7313e57781f89"/>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" type="application/rss+xml" title="Bitki Tabanı: günün bitkisi" href="/gunun-bitkisi/rss.xml"><link rel="alternate" type="application/rss+xml" title="Bitki Tabanı: yeni eklenen bitkiler" href="/yeni/rss.xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bitki Tabanı">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="tr_TR">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{image}">
<meta name="theme-color" content="#A3271B">
{FAV}
{FONTS}
<link rel="stylesheet" href="/assets/style.css">
{extra}
</head>
<body>
<div class="wrap{{narrow}}">
'''

MENU = [('Bitkiler', [('/katalog/', 'Katalog', 'kat'), ('/toplama-takvimi/', 'Doğada bu ay', 'toplama'), ('/yoreler/', 'Yöreler ve yöresel adlar', 'yore'), ('/yeni/', 'Yeni eklenenler', 'yeni')]),
        ('Şifa', [('/rehber/', 'Derde göre bitkiler', 'rehber'), ('/tarif/', 'Çay tarifleri', 'tarif'), ('/karsilastirma/', 'Karşılaştırmalar', 'kars'), ('/rehber/ilac-etkilesimi/', 'İlaç etkileşimi', 'etk')]),
        ('Kültür', [('/kavram/', 'Kavramlar', 'kavram'), ('/semboller/', 'Semboller', 'sembol'), ('/kopruler/', 'Kültür köprüleri', 'br'), ('/hikaye/', 'Halk hekimliğinden', 'hikaye'), ('/yazilar/', 'Yazılar', 'yazi'), ('/takvim/', 'Ritüel takvimi', 'takvim')]),
        ('Bitki Tabanı', [('/hakkinda/', 'Hakkında', 'about'), ('/yontem/', 'Yöntem ve kaynaklar', 'yontem'), ('/bulten/', 'Bülten ve e-posta kursu', 'bulten'), ('/kartlar/', 'Yazdırılabilir kartlar', 'kartlar'), ('/hesap/', 'Hesabım', 'acct'), ('mailto:iletisim@bitkitabani.com', 'İletişim', 'mail')])]
MENU_HUB = {'Bitkiler': '/katalog/', 'Şifa': '/rehber/', 'Kültür': '/kultur/'}
_TABICO = {'ara': '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>', 'kat': '<path d="M12 21V9"/><path d="M12 13c-4 0-6-3-6-7 4 0 6 3 6 7z"/><path d="M12 11c3 0 5-2 5-5-3 0-5 2-5 5z"/>',
           'rehber': '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>', 'kultur': '<path d="M12 3l2.5 5.5L20 9l-4 4 1 6-5-3-5 3 1-6-4-4 5.5-.5z"/>', 'gun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5L19 19M5 19l1.5-1.5M17.5 6.5L19 5"/>'}
def tabbar(cur):
    it = [('/#ara', 'Ara', 'ara'), ('/katalog/', 'Bitkiler', 'kat'), ('/rehber/', 'Şifa', 'rehber'), ('/kultur/', 'Kültür', 'kultur')]
    return '<nav class="tabbar" aria-label="Ana bölümler">' + ''.join(f'<a href="{h}"' + (' aria-current="page"' if cur == k else '') + f'><svg viewBox="0 0 24 24" aria-hidden="true">{_TABICO[k]}</svg><span>{l}</span></a>' for h, l, k in it) + '</nav>'
def nav(cur):
    a = lambda href, label, key: f'<a href="{href}"{" aria-current=\"page\"" if cur == key else ""}{" rel=\"noopener\"" if href.startswith("http") else ""}>{label}</a>'
    groups = ''.join(f'<div class="mgrp"><b>' + (f'<a href="{MENU_HUB[g]}">{g} →</a>' if g in MENU_HUB else g) + '</b>' + ''.join(a(h, l, k) for h, l, k in items) + '</div>' for g, items in MENU)
    return f'''<div class="motif" aria-hidden="true"></div><div class="site-nav"><a class="logo" href="/">Bitki <em>Tabanı</em></a><nav class="topnav" aria-label="Ana bölümler">{a("/katalog/", "Bitkiler", "kat")}{a("/rehber/", "Şifa", "rehber")}{a("/kultur/", "Kültür", "kultur")}</nav><div class="navr"><button type="button" class="themebtn" data-l="tr" aria-label="Açık ya da koyu tema">◐</button><details class="menu"><summary aria-label="Menü"><span class="burger" aria-hidden="true"></span><span class="mlab">Menü</span></summary><nav class="menu-panel" aria-label="Site menüsü">{groups}<div class="mgrp lang"><!--LANG--></div></nav></details></div></div>''' + tabbar(cur)

FOOT = '''<div class="motif indigo" aria-hidden="true"></div>
<footer class="site">
  <!--FOOTNAV-->
  <div>
    <h3>Bu site nedir</h3>
    <p>Bilgi ve merak için hazırlanmış bir derlemedir; tedavi önerisi değildir. Bir bitkiyi kullanmadan önce, özellikle ilaç kullanıyorsan, hamileysen ya da emziriyorsan bir hekime veya eczacıya danış.</p>
    <p>Fotoğraflar Wikimedia Commons’tan özgür lisanslarla alınmıştır; yazarı ve lisansı her bitkinin sayfasında yazılıdır.</p>
  </div>
  <div class="legend">
    <h3>Kanıt düzeyi</h3>
    <div><span class="pips"><i class="on"></i><i class="on"></i><i class="on"></i></span> Klinik: kontrollü çalışmalar ya da onaylı ilaç</div>
    <div><span class="pips"><i class="on"></i><i class="on"></i><i></i></span> Sınırlı: küçük ya da az sayıda insan çalışması</div>
    <div><span class="pips"><i class="on"></i><i></i><i></i></span> Geleneksel: insan çalışması yok ya da çok az</div>
  </div>
  <div class="legend">
    <h3>Güvenlik</h3>
    <div><span class="sf dusuk">Genelde güvenli</span> ölçülü kullanımda</div>
    <div><span class="sf orta">Dikkat</span> etkileşim ya da doz riski</div>
    <div><span class="sf yuksek">Yüksek risk</span> zehirli ya da ciddi yan etkili</div>
    <div><span class="lg yasak">Türkiye’de yasak</span> ayrı bir etiketle gösterilir</div>
  </div>
</footer>
</div>
'''

FOOTNAV = '<nav class="footnav" aria-label="Site haritası">' + ''.join(f'<div><h3>{g}</h3><ul>' + ''.join(f'<li><a href="{h}"' + (' rel="noopener"' if h.startswith('http') else '') + f'>{l}</a></li>' for h, l, k in items) + '</ul></div>' for g, items in MENU) + '</nav>'
SOSYAL = [('instagram', 'Instagram', 'https://www.instagram.com/bitkitabani/'), ('threads', 'Threads', 'https://www.threads.net/@bitkitabani'),
          ('facebook', 'Facebook', 'https://www.facebook.com/profile.php?id=61595314033889'), ('pinterest', 'Pinterest', 'https://www.pinterest.com/bitkitabani/'), ('telegram', 'Telegram', 'https://t.me/bitkitabani'), ('rss', 'RSS', '/yeni/rss.xml')]
def _icon(n, label):
    f = os.path.join(HERE, 'assets', 'icons', n + '.svg')
    if os.path.exists(f):
        svg = re.sub(r'<title>.*?</title>', '', open(f, encoding='utf-8').read())
        return svg.replace('<svg ', '<svg aria-hidden="true" focusable="false" fill="currentColor" width="22" height="22" ', 1)
    return f'<span class="sicon-t">{label}</span>'
FOOTNAV += '<div class="sosyal" aria-label="Sosyal medya">' + ''.join(f'<a href="{u}" title="{l}" aria-label="Bitki Tabanı {l}"' + (' rel="noopener" target="_blank"' if u.startswith('http') else '') + f'>{_icon(n, l)}</a>' for n, l, u in SOSYAL) + '</div>'
FOOT = FOOT.replace('<!--FOOTNAV-->', FOOTNAV)
def page(title, desc, path, body, cur, scripts='', narrow=False, extra='', image=None):
    h = head(title, desc, path, extra, image).replace('{narrow}', ' narrow' if narrow else '')
    return h + nav(cur) + body + FOOT + '<script src="/assets/theme.js" defer></script><script src="/assets/streak.js" defer></script><script src="/assets/sync.js" defer></script>' + ('<script src="/assets/bulten.js" defer></script>' if 'abone-form' in body and 'bulten.js' not in scripts else '') + scripts.replace('<script src="/assets/streak.js" defer></script>', '') + '\n</body>\n</html>\n'

_BIG = re.compile(re.escape(BASE) + r'/img/([a-z0-9]+)-960\.jpg')
def _big(m):   # paylaşım önizlemesi ve Google Discover için 1280 px görsel (varsa)
    return f'{BASE}/img/{m.group(1)}-1280.jpg' if os.path.exists(os.path.join(HERE, 'img', f'{m.group(1)}-1280.jpg')) else m.group(0)
def write(path, content):
    content = _BIG.sub(_big, content)
    if path.strip('/') in byId or (path.startswith('/yazilar/') and path.count('/') > 2) or path.startswith('/rehber/') and path != '/rehber/':   # tekil içerik sayfaları
        content = content.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">', 1)
    full = os.path.join(OUT, path.strip('/'), 'index.html') if not path.endswith('.html') and not '.' in path.split('/')[-1] else os.path.join(OUT, path.strip('/'))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(content)

_AVG_F = os.path.join(HERE, '.cache', 'avgcolor.json')
try: _AVGC = json.load(open(_AVG_F))
except Exception: _AVGC = {}
def _avg(pid):   # fotoğraf yüklenene kadar kutuda fotoğrafın ortalama rengi görünsün
    if pid not in _AVGC:
        try:
            from PIL import Image
            im = Image.open(os.path.join(HERE, 'img', f'{pid}-500.jpg')).convert('RGB').resize((1, 1), Image.LANCZOS)
            _AVGC[pid] = '#%02x%02x%02x' % im.getpixel((0, 0))
            os.makedirs(os.path.dirname(_AVG_F), exist_ok=True); json.dump(_AVGC, open(_AVG_F, 'w'))
        except Exception: return ''
    return f' style="background:{_AVGC[pid]}"'
def ph(p, size, eager=False):
    m = IMG.get(p['id'])
    if not m:
        return f'<div class="ph"><span class="ph-mark">{e(short_la(p))}</span></div>'
    w, h = (m['w'], m['h']) if size == 960 else (m.get('w500', 500), m.get('h500', 667))
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    src = f'<source type="image/webp" srcset="/img/{p["id"]}-{size}.webp">' if os.path.exists(os.path.join(HERE, 'img', f'{p["id"]}-{size}.webp')) else ''
    return f'<div class="ph loaded"{_avg(p["id"])}><picture>{src}<img src="/img/{p["id"]}-{size}.jpg" width="{w}" height="{h}" alt="{e(p["tr"])} ({e(short_la(p))}): {e(ALT.get(p["id"], "bitki"))}" {load} decoding="async"></picture></div>'

def galeri(p):
    """Bitki sayfasının üst görseli: ana fotoğraf + tanıma görselleri (çizim, çiçekli, kurutulmuş).
    Telefonda yatay kaydırmalı, geniş ekranda büyük ana fotoğraf ve yanında küçük ızgara."""
    pid = p['id']; ek = []
    for t in ('cizim', 'cicek', 'kuru'):
        x = TANIMA.get(f'{pid}:{t}')
        if isinstance(x, dict) and os.path.exists(os.path.join(HERE, 'img', 'tanima', f'{pid}-{t}.jpg')): ek.append((t, x))
    ana = f'<figure class="g-ana">{ph(p, 960, eager=True)}<figcaption>{credit(p)}</figcaption></figure>'
    if not ek: return f'<figure class="photo">{ph(p, 960, eager=True)}<figcaption>{credit(p)}</figcaption></figure>'
    sl = ''.join(f'<figure class="g-{t}"><div class="ph loaded"><img src="/img/tanima/{pid}-{t}.jpg" alt="{e(p["tr"])}: {TANIMA_AD[t].lower()}" loading="lazy" decoding="async"></div>'
                 f'<figcaption><b>{TANIMA_AD[t]}</b> · {e(x.get("artist", ""))} · {e(x.get("license", ""))} · <a href="{x["page"]}" target="_blank" rel="noopener">Commons</a></figcaption></figure>' for t, x in ek)
    dots = ''.join(f'<button type="button" aria-label="{l}"></button>' for l in ['Fotoğraf'] + [TANIMA_AD[t] for t, _ in ek])
    return f'<div class="photo galeri" data-n="{len(ek) + 1}"><div class="g-track">{ana}{sl}</div><div class="g-dots" aria-hidden="true">{dots}</div></div>'

def credit(p):
    m = IMG.get(p['id'])
    if not m: return ''
    lic = f'<a href="{e(m["licenseUrl"])}" target="_blank" rel="noopener">{e(m["license"])}</a>' if m.get('licenseUrl') else e(m.get('license', ''))
    parts = [x for x in [e(m.get('artist', '')), lic] if x]
    return 'Fotoğraf: ' + ' · '.join(parts) + f' · <a href="{e(m["page"])}" target="_blank" rel="noopener">Wikimedia Commons</a>'

def tags(p, small=False):
    out = []
    y = YASAL.get(p['id'])
    if y: out.append(f'<span class="lg {y[0]}">{YASAL_AD[y[0]]}</span>')
    k = KORUMA.get(p['id'])
    if k and k.get('rozet'): out.append(f'<span class="lg koruma">{e(k["rozet"])}</span>')
    return f'<div class="tags">{"".join(out)}</div>' if out else ''

def refs(p):
    pid = p['id']; items = []
    for label, url in EMA.get(pid, []):
        items.append(('EMA monografisi', f'{label}: Avrupa İlaç Ajansı bitkisel ilaç değerlendirmesi', url))
    if pid in NCCIH:
        items.append(('NCCIH', 'ABD Ulusal Tamamlayıcı ve Bütünleştirici Sağlık Merkezi: kullanım ve güvenlik özeti', f'https://www.nccih.nih.gov/health/{NCCIH[pid]}'))
    for label, url in OTHER.get(pid, []):
        kind = 'Resmî kaynak' if ('fda.gov' in url or 'unodc.org' in url or 'nobelprize.org' in url) else 'Araştırma'
        items.append((kind, label, url))
    if 'anadolu' in p['bolge'] and any('Anadolu' in w for w, _ in p['kul']):
        items.append(('Kitap', BAYTOP, ''))
    name = POWO.get(pid, short_la(p))
    if name:
        items.append(('Botanik kayıt', f'Kew Plants of the World Online: {name}', 'https://powo.science.kew.org/results?q=' + urllib.parse.quote(name)))
    return '<ol class="refs">' + ''.join((f'<li><span class="kind">{e(k)}</span><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' if u else f'<li><span class="kind">{e(k)}</span><cite>{e(t)}</cite></li>') for k, t, u in items) + '</ol>'

KANIT_ICIN = {'kantaron': 'depresyonda', 'lavanta': 'kaygıda (kapsül)', 'hayit': 'adet öncesi sendromda', 'hashas': 'ağrıda (morfin)', 'kinin': 'sıtmada',
              'nane': 'huzursuz bağırsakta', 'sarimsak': 'tansiyon ve kolesterolde', 'keten': 'kabızlıkta', 'gucigdemi': 'gut ve FMF’de (kolşisin)', 'efedra': 'bronş açmada (efedrin)',
              'kenevir': 'kemoterapi bulantısı ve epilepside', 'sinameki': 'kısa süreli kabızlıkta', 'atkestanesi': 'toplardamar yetmezliğinde', 'ceviz': 'kolesterolde',
              'turnayemisi': 'idrar yolu enfeksiyonunu önlemede', 'mayiselmasi': 'kemoterapide (etoposid)'}
def kan_txt(p): return KANIT[p["kanit"]]["ad"] + (' · ' + KANIT_ICIN[p['id']] if p['kanit'] == 'klinik' and p['id'] in KANIT_ICIN else '')
def desc_for(p):
    """Arama sonucu açıklaması: doğal cümle; önce kanıt, sonra güvenlik. Kesme işareti (…) olmadan ≤160 karakter."""
    k = p['kanit']
    if k == 'klinik': kc = (KANIT_ICIN[p['id']][0].upper() + KANIT_ICIN[p['id']][1:] + ' klinik kanıtı var') if p['id'] in KANIT_ICIN else 'Kontrollü insan çalışmalarıyla desteklenen bir kullanımı var'
    elif k == 'sinirli': kc = 'Umut verici ama sınırlı insan çalışmaları var'
    else: kc = 'Kullanımı daha çok geleneğe dayanıyor'
    g = p['guv']
    gc = ('zehirli ya da yüksek riskli, kullanım önerisi değildir' if g == 'yuksek' else
          ('ilaç etkileşimleri nedeniyle dikkat ister' if p['id'] in ETK else 'bazı gruplar için dikkat ister') if g == 'orta' else 'ölçülü kullanımda genelde güvenli')
    bas = f'{p["tr"]} ({short_la(p)}) ne işe yarar? {kc}; {gc}.'
    for son in (' Geleneksel kullanımı, kanıtı ve kaynakları.', ' Kanıtı ve kaynakları.', ''):
        if len(bas + son) <= 160: return bas + son
    return f'{p["tr"]} ne işe yarar? {kc}; {gc}.'[:160]

KISIM = [('yaprak', 'Yaprak', r'yaprak'), ('cicek', 'Çiçek', r'çiçek'), ('kok', 'Kök ve yumru', r'kök|rizom|yumru|soğan'), ('tohum', 'Tohum ve meyve', r'tohum|meyve|bakla|kozalak|tane'),
         ('kabuk', 'Kabuk ve odun', r'kabuk|odun|gövde'), ('herba', 'Toprak üstü kısımlar', r'toprak üstü|dal|herba|bütün bitki'), ('recine', 'Reçine, yağ ve özsu', r'reçine|yağ|sakız|özsu|lateks|jel|süt'), ('mantar', 'Mantar', r'mantar|şapka|miselyum')]
def kisim_of(p): return ' '.join(k for k, _, rx in KISIM if re.search(rx, p['kisim'].lower()))
def ay_of(p): return ' '.join(f'a{m}' for m in sorted(months_of(EK.get(p['id'], {}).get('mevsim', '')))) if 'months_of' in globals() else ''
def card(p):
    s = ' '.join([p['tr'], p['la'], p['diger'], p['fam'], p['kisim'], p['haz'], p['bilim'], p['ilginc']] + [x for u in p['kul'] for x in u] + [KAT[k] for k in p['kat']])
    return f'''<a class="card" href="/{p["id"]}/" data-id="{p["id"]}" data-bolge="{" ".join(p["bolge"])}" data-kat="{" ".join(p["kat"])}" data-kanit="{p["kanit"]}" data-no="{p["no"]}" data-ad="{e(p["tr"])}" data-guv="{p["guv"]}" data-kisim="{kisim_of(p)}" data-ay="{ay_of(p)}" data-durum="{" ".join(([YASAL[p["id"]][0] if YASAL[p["id"]][0]=="yasak" else "kisitli"] if p["id"] in YASAL else []) + (["zehir"] if "zehir" in p["kat"] else []) + (["koruma"] if KORUMA.get(p["id"], {}).get("rozet") else []))}" data-s="{e(s)}">
  {ph(p, 500)}
  <div class="body">
    <div class="row"><span class="acc">{acc(p["no"])}{'<span class="newb">Yeni</span>' if is_new(p["id"]) else ''}</span><span class="regs">{"".join(dot(r) for r in p["bolge"])}</span></div>
    <h2>{e(p["tr"])}</h2>
    <div class="latin">{e(p["la"])}</div>
    <div class="fam" lang="la">{e(p["fam"])}</div>
    {tags(p)}
    <div class="foot"><span class="ev" aria-label="Kanıt düzeyi: {kan_txt(p)}">{pips(p["kanit"])} Kanıt: {kan_txt(p)}</span><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span></div>
  </div>
</a>'''

import collections, re as _re
FAMC = collections.Counter(p['fam'] for p in P)
FAM_TR = {'Lamiaceae':'ballıbabagiller','Solanaceae':'patlıcangiller','Asteraceae':'papatyagiller','Rubiaceae':'kökboyasıgiller','Malvaceae':'ebegümecigiller','Fabaceae':'baklagiller',
          'Anacardiaceae':'sakızağacıgiller','Ranunculaceae':'düğünçiçeğigiller','Rosaceae':'gülgiller','Apiaceae':'maydanozgiller','Cactaceae':'kaktüsgiller','Euphorbiaceae':'sütleğengiller',
          'Lythraceae':'kınagiller','Arecaceae':'palmiyegiller'}
def fam_slug(f): return f.lower()
def fam_link(p):
    f = p['fam']
    return f'<a href="/familya/{fam_slug(f)}/" lang="la">{e(f)}</a>' if FAMC[f] >= 2 else f'<span lang="la">{e(f)}</span>'
DATE_TXT = tr_date(datetime.date.fromisoformat(CONTENT_DATE)).rsplit(',', 1)[0]
CONTACT = 'iletisim@bitkitabani.com'
def contrib(p):
    subj = urllib.parse.quote(f'Bitki Tabanı: {p["tr"]} için yöresel kullanım')
    body = urllib.parse.quote(f'Bitki: {p["tr"]} ({short_la(p)})\nYöre (il, ilçe, köy ya da topluluk): \nBitkinin oradaki adı: \nNasıl ve ne için kullanılır: \nBunu kimden ya da nereden öğrendin: \nAdının sitede yazılmasını ister misin (evet/hayır): \n')
    return (f'<aside class="contrib" id="katki"><h2>Yöresel bir ad ya da kullanım biliyor musun?</h2><p>Annenden, köyünden ya da bir ustadan duyduğun bir adı ya da kullanımı yaz. Her not okunur; uygun bulunanlar “Okurlardan” başlığıyla, yöresiyle birlikte bu sayfaya eklenir.</p>'
            f'<form class="katki-form" data-bitki="{p["id"]}"><label>Ne paylaşıyorsun? <select name="tur"><option value="ad">Yöresel ad</option><option value="kullanim" selected>Yöresel kullanım</option><option value="duzeltme">Düzeltme</option></select></label>'
            f'<label>Notun <textarea name="metin" rows="3" maxlength="600" required placeholder="Örn. Bizim köyde kurutulup kışın çay olarak içilir."></textarea></label>'
            f'<label>Yöre (il, ilçe, köy ya da topluluk) <input name="yore" maxlength="80"></label>'
            f'<label>Bunu kimden ya da nereden öğrendin? <input name="kaynak" maxlength="200"></label>'
            f'<label>Adın (sitede yazılsın istersen) <input name="ad" maxlength="60"></label><input name="hp" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">'
            f'<button type="submit" class="cta">Gönder</button> <span class="katki-durum muted-s" role="status"></span></form>'
            f'<p class="muted-s">E-postayla da yazabilirsin: <a href="mailto:{CONTACT}?subject={subj}&amp;body={body}">{CONTACT}</a></p></aside>')
def toc_and_ids(html):
    items = []
    def sub(m):
        t = m.group(2); sid = m.group(1) or _re.sub(r'[^a-z0-9]+', '-', t.lower().translate(str.maketrans('çğıöşüâî', 'cgiosuai'))).strip('-')
        items.append((sid, t)); return f'<section class="sec" id="{sid}"><h2>{t}</h2>'
    html = _re.sub(r'<section class="sec"(?: id="([^"]+)")?><h2>([^<]+)</h2>', sub, html)
    nav_ = '<details class="toc"><summary><span class="eyebrow">Bu sayfada</span> ' + str(len(items)) + ' bölüm</summary><nav aria-label="Bu sayfada"><ol>' + ''.join(f'<li><a href="#{s}">{t}</a></li>' for s, t in items) + '</ol></nav></details>'
    return html.replace('<!--TOC-->', nav_)

# ---------- bitki sayfaları ----------
for i, p in enumerate(P):
    pid = p['id']; rel = related(pid)
    prev, nxt = P[i-1], P[(i+1) % len(P)]
    title = (f'{p["tr"]}: nedir, etkileri ve zehirlilik riski' if p['guv'] == 'yuksek' else f'{p["tr"]} nedir, ne işe yarar? Faydaları ve zararları')
    if len(title) < 44: title += ' | Bitki Tabanı'
    ld = {"@context":"https://schema.org","@type":"Article","headline":f'{p["tr"]} ({short_la(p)})',"inLanguage":"tr","about":{"@type":"Taxon","name":short_la(p),"alternateName":[p['tr']] + [x.strip() for x in p['diger'].split(',')][:4],"taxonRank":"species","parentTaxon":{"@type":"Taxon","name":p['fam'].split(' ')[0],"taxonRank":"family"}},"description":desc_for(p),"author":AUTHOR,"isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},"dateModified":(max(CONTENT_DATE, YENI[pid].isoformat()) if pid in YENI else CONTENT_DATE),**({"datePublished":YENI[pid].isoformat()} if pid in YENI else {}),**({"reviewedBy":{"@type":"Person","name":GZ_KISI['ad'],"jobTitle":GZ_KISI.get('unvan','Eczacı')},"lastReviewed":GZ[pid]} if GZ_KISI and pid in GZ else {}),"url":f'{BASE}/{pid}/',"image":(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None),"publisher":{"@type":"Organization","name":"Bitki Tabanı","url":BASE+"/","logo":BASE+"/assets/logo-512.png","sameAs":["https://www.instagram.com/bitkitabani/","https://www.threads.net/@bitkitabani","https://www.facebook.com/profile.php?id=61595314033889","https://www.pinterest.com/bitkitabani/","https://t.me/bitkitabani"]}}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Katalog","item":BASE+"/katalog/"},{"@type":"ListItem","position":3,"name":p['tr'],"item":f'{BASE}/{pid}/'}]}
    uses = ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(t)}</p></div>' for w, t in p['kul'])
    relhtml = ''
    etkhtml = ''
    derhtml = ''; faqld = None
    trl = p['tr'].replace('I', 'ı').replace('İ', 'i')
    def _first(t): 
        s = t.split('. ')[0].rstrip('.'); return s + '.'
    regs_txt = ', '.join(REG[r]['ad'] for r in p['bolge'])
    _kis = p["kisim"].lower(); _fam = p["fam"].split(" ")[0]
    q_nedir = (f'{p["tr"]} nedir?', f'{p["tr"]} ({short_la(p)}), {_fam} familyasından bir bitkidir. {regs_txt} geleneklerinde en çok {_kis} kullanılır.')
    q_ne = (f'{p["tr"]} ne işe yarar?', f'Bilimsel kanıt düzeyi {KANIT[p["kanit"]]["ad"].lower()}. {_first(p["bilim"])} Geleneksel kullanımları aşağıda, yöresiyle birlikte anlatılıyor.')
    q_guv = (f'{p["tr"]} zararlı mı, kimler kullanmamalı?' if p['guv'] != 'yuksek' else f'{p["tr"]} güvenli mi?', f'Güvenlik düzeyi: {GUV[p["guv"]].lower()}. {_first(p["guvNot"])}' + (' Yasal durum: ' + YASAL_AD[YASAL[pid][0]] + '.' if pid in YASAL else '') + ' Ayrıntılar “Güvenlik” bölümünde.')
    kisaca = [q_nedir, q_ne, q_guv]
    kisahtml = '<details class="kisaca"><summary><span class="eyebrow">30 saniyede</span> ' + e(p['tr']) + ' nedir, ne işe yarar?</summary>' + ''.join(f'<div class="qa"><h2 class="q">{e(q)}</h2><p>{e(a)}</p></div>' for q, a in kisaca) + '</details>'
    if pid in DERIN:
        dd = DERIN[pid]
        rows_ = ''.join(f'<tr><th scope="row">{e(i)}</th><td><span class="kv {k}">{KAN_AD[k]}</span></td><td>{e(n)}</td></tr>' for i, k, n in dd['iddia'])
        derhtml += f'<section class="sec"><h2>Faydaları ne kadar kanıtlı?</h2><p class="muted-s">İnternette {e(p["tr"].replace("I","ı").replace("İ","i").lower())} için sık tekrarlanan iddialar ve bilimin bugün söyledikleri.</p><div class="tablewrap"><table class="cmp etk kanit"><thead><tr><th scope="col">İddia</th><th scope="col">Kanıt</th><th scope="col">Açıklama</th></tr></thead><tbody>{rows_}</tbody></table></div></section>'
        derhtml += '<section class="sec"><h2>Sık yapılan hatalar</h2><ul class="hatalar">' + ''.join(f'<li>{e(h)}</li>' for h in dd['hata']) + '</ul></section>'
        derhtml += '<section class="sec"><h2>Sık sorulanlar</h2><div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in dd['sss']) + '</div></section>'
        faqld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in dd['sss']]}
    if pid in ETK:
        rows_ = ''.join(f'<tr><th scope="row">{e(g)}</th><td>{e(w)}</td></tr>' for g, w in ETK[pid])
        etkhtml = f'<section class="sec" id="etk"><h2>İlaç etkileşimleri</h2><div class="tablewrap"><table class="cmp etk"><thead><tr><th scope="col">İlaç ya da madde</th><th scope="col">Neden önemli</th></tr></thead><tbody>{rows_}</tbody></table></div><p class="muted-s">Bu liste eksiksiz değildir. Düzenli ilaç kullanıyorsan {e(p["tr"])} denemeden önce eczacına ya da hekimine sor.</p></section>'
    _gp = {k['slug'] for k in KONULAR if any(x == pid for x, _ in k['bitkiler'])}
    def _sim(q):
        _gq = {k['slug'] for k in KONULAR if any(x == q['id'] for x, _ in k['bitkiler'])}
        return 4 * len(_gp & _gq) + 2 * len(set(q['kat']) & set(p['kat'])) + (2 if q['fam'] == p['fam'] else 0) + len(set(q['bolge']) & set(p['bolge']))
    similar = sorted((q for q in P if q['id'] != pid and q['id'] not in rel), key=lambda q: (-_sim(q), q['no']))[:3]
    _rg = [k for k in KONULAR if any(x == pid for x, _ in k['bitkiler']) and sum(1 for y, _ in k['bitkiler'] if y in byId) >= 2]
    simhtml = (('<p class="brlinks">Bu bitki şu rehberlerde: ' + ' · '.join(f'<a href="/rehber/{k["slug"]}/">{e(k["kisa"])}</a>' for k in _rg) + '</p>') if _rg else '') + '<section class="sec"><h2>Benzer bitkiler</h2><p class="muted-s">Aynı derde kullanılan ya da aynı familyadan bitkiler.</p><div class="grid sim">' + ''.join(card(q) for q in similar) + '</div></section>'
    mybridges = [(i, x) for i, x in enumerate(BR, 1) if pid in (x['a'], x.get('b'))]
    brlinks = ''.join(f'<a class="cta" href="/kopruler/{slug_of(x)}/">Karşılaştırmayı oku: {e(x["t"])} →</a>' for i, x in mybridges)
    brlinks += ''.join(f'<a class="cta" href="{u}">{e(t)} →</a>' for u, t in GLINKS.get(pid, []))
    if rel:
        relhtml = '<section class="sec"><h2>Kültür köprüsü</h2><div class="related">' + ''.join(f'<a class="chip" href="/{r}/">{"".join(dot(x) for x in byId[r]["bolge"])}{e(byId[r]["tr"])}</a>' for r in rel) + '</div></section>'
    ek = EK.get(pid, {})
    kor = KORUMA.get(pid)
    y = YASAL.get(pid)
    yas = ''
    if y or (p.get('yasal') and pid not in ('sigla', 'palosanto', 'akadacayi', 'salep')):
        inner = ''
        if y: inner += f'<div class="callout yasal {y[0]}"><div class="lvl">{YASAL_AD[y[0]]}</div><p>{e(y[1])}</p></div>'
        if p.get('yasal') and pid not in ('sigla', 'palosanto', 'akadacayi', 'salep'): inner += f'<p><b>Diğer ülkeler:</b> {e(p["yasal"])}</p>'
        yas = f'<section class="sec"><h2>Yasal durum</h2>{inner}</section>'
    korhtml = ''
    if kor:
        rows = []
        if kor.get('iucn'): rows.append(f'<div><dt>IUCN Kırmızı Liste</dt><dd>{e(kor["iucn"])}</dd></div>')
        if kor.get('cites'): rows.append(f'<div><dt>CITES</dt><dd>{e(kor["cites"])}</dd></div>')
        alt = f'<div class="alt"><b>Sürdürülebilir alternatif:</b> {e(kor["alternatif"])}</div>' if kor.get('alternatif') else ''
        korhtml = f'<section class="sec"><h2>Koruma durumu</h2>{"<dl class=meta>" + "".join(rows) + "</dl>" if rows else ""}<p>{e(kor["not_"])}</p>{alt}</section>'
    dogada = ''
    if ek:
        dogada = f'''<section class="sec"><h2>Doğada</h2><dl class="meta wide">
      <div><dt>Nerede yetişir</dt><dd>{e(ek["yetisme"])}</dd></div>
      <div><dt>Toplama mevsimi</dt><dd>{e(ek["mevsim"])}</dd></div>
      <div><dt>Yöresel adlar</dt><dd>{e(ek["yoresel"])}</dd></div>
      {inat_satir(pid)}
    </dl></section>
  <section class="sec"><h2>Karıştırma riski</h2><div class="callout orta"><p>{e(ek["karisma"])}</p></div></section>'''
    body = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/katalog/">Katalog</a><span>/</span><span>{e(p["tr"])}</span></nav>
<article class="sheet">
  <header class="sheet-head">
    <div class="titles">
      <span class="eyebrow">{acc(p["no"])} · {fam_link(p)}</span>
      <h1>{e(p["tr"])}</h1>
      <span class="latin">{e(p["la"])}</span>
      <div class="badges"><span class="ev">{pips(p["kanit"])} Kanıt: {kan_txt(p)}</span><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span>{tags(p).replace('<div class="tags">','').replace('</div>','')}</div>
      <p class="intro">{e(p["ilginc"])}</p>
      <dl class="meta">
    <div><dt>Diğer adlar</dt><dd>{e(p["diger"])}</dd></div>
    <div><dt>Kullanılan kısım</dt><dd>{e(p["kisim"])}</dd></div>
    <div><dt>Bölge</dt><dd>{"<br>".join(dot(r) + " " + e(REG[r]["ad"]) for r in p["bolge"])}</dd></div>
    <div><dt>Kullanım</dt><dd>{", ".join(KAT[k] for k in p["kat"])}</dd></div>
  </dl>
    </div>
    {galeri(p)}
  </header>
  {sharebar(p['tr'] + ': ne işe yarar, kanıtı ve güvenliği', '/' + pid + '/')}
  {kisahtml}
  <!--TOC-->
  <section class="sec"><h2>Geleneksel kullanım</h2><div class="uses">{uses}</div>{halk_kutu(pid, p["tr"])}</section>
  {dogada}
  <section class="sec"><h2>Hazırlama</h2><p>{e(p["haz"])}</p></section>
  <section class="sec"><h2>Bilim ne diyor</h2><p>{e(p["bilim"])}</p></section>
  {derhtml}
  <section class="sec"><h2>Güvenlik</h2><div class="callout {p["guv"]}"><div class="lvl">{GUV[p["guv"]]}</div><p>{e(p["guvNot"])}</p></div><div class="safelinks"><a href="{('#etk' if pid in ETK else '/rehber/ilac-etkilesimi/?q=' + urllib.parse.quote(p["tr"]))}">{ico('etk','ico-s')}<span>{'Bu bitkinin ilaç etkileşimleri' if pid in ETK else 'İlaç kullanıyorsan: etkileşim aracı'}</span></a><a href="/rehber/hamilelik-emzirme/">{ico('gebe','ico-s')}<span>Hamilelik ve emzirme</span></a></div></section>
  {etkhtml}
  {yas}
  {korhtml}
  {relhtml}
  {('<p class="brlinks">' + brlinks + '</p>') if brlinks else ''}
  {abone('bitki:' + pid)}
  {simhtml}
  {contrib(p)}
  <section class="sec"><h2>Kaynaklar</h2>{refs(p)}</section>
  <aside class="disclaimer" role="note"><b>Tıbbi tavsiye değildir.</b> Bu sayfa geleneksel kullanımları kültürel bir kayıt olarak anlatır ve bilimsel bilgiyi özetler; teşhis ya da tedavi önerisi değildir. {e(p["tr"])} ya da başka bir bitkiyi kullanmadan önce, özellikle ilaç kullanıyorsan, hamileysen, emziriyorsan ya da bir hastalığın varsa hekimine veya eczacına danış. Zehirlenme şüphesinde Ulusal Zehir Danışma Merkezi’ni (UZEM) <b>114</b> numaradan ara.</aside>
  <p class="updated">Hazırlayan: <a href="/yontem/#hazirlayan">Edanaz Tınmazlar</a> · {('Gözden geçiren: <a href="/yontem/#gozden">' + e(GZ_KISI['ad']) + '</a> (<time datetime="' + GZ[pid] + '">' + tr_date(datetime.date.fromisoformat(GZ[pid])).rsplit(',', 1)[0] + '</time>) · ') if GZ_KISI and pid in GZ else ''}{('Eklendi: <time datetime="' + YENI[pid].isoformat() + '">' + tr_date(YENI[pid]).rsplit(',', 1)[0] + '</time> · ') if pid in YENI else ''}Son gözden geçirme: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time></p>
  <p class="igcta">Her gün yeni bir bitki: <a href="https://www.instagram.com/bitkitabani/" rel="noopener">Instagram’da @bitkitabani</a></p>
  <div class="sheet-foot">
    <div class="learnbox"><button type="button" class="learn" id="learnBtn" data-id="{pid}" aria-pressed="false">Öğrendim olarak işaretle</button><span class="muted-s">Bu tarayıcıda saklanır. <a href="/hesap/">Google ile giriş yaparsan</a> bütün cihazlarında görünür.</span><span class="muted-s streak" id="streakNote"></span></div>
    <div class="pager"><a href="/{prev["id"]}/">← {e(prev["tr"])}</a><a href="/{nxt["id"]}/">{e(nxt["tr"])} →</a></div>
  </div>
</article>
'''
    body = toc_and_ids(body)
    allqa = kisaca + (DERIN[pid]['sss'] if pid in DERIN else [])
    faqld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in allqa]}
    crumbs = [crumbs, faqld]
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>'
    write(f'/{pid}/', page(title, desc_for(p), f'/{pid}/', body, 'plant', '<script src="/assets/streak.js" defer></script><script src="/assets/plant.js" defer></script><script src="/assets/katki.js" defer></script>', narrow=True, extra=extra, image=(f'{BASE}/img/{pid}-960.jpg' if pid in IMG else None)))

# ---------- familya sayfaları ----------
FAM_URLS = []
for f, n in sorted(FAMC.items()):
    if n < 2: continue
    ps = [p for p in P if p['fam'] == f]; trn = FAM_TR.get(f)
    others = ' · '.join(f'<a href="/familya/{fam_slug(g)}/" lang="la">{g}</a>' for g, m in sorted(FAMC.items()) if m >= 2 and g != f)
    fb = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/katalog/">Katalog</a><span>/</span><span lang="la">{f}</span></nav>
<header class="page-head"><span class="eyebrow">Familya · {n} bitki</span><h1 lang="la">{f}</h1><p>{(trn[0].upper() + trn[1:] + ' familyası. ') if trn else ''}Bitki Tabanı’nda bu familyadan {n} bitki var: {", ".join(e(p["tr"]) for p in ps)}. Aynı familyadaki bitkiler çoğu zaman benzer kimyasal bileşikler taşır.</p></header>
<div class="grid">{"".join(card(p) for p in ps)}</div>
<section class="sec"><h2>Diğer familyalar</h2><p class="famlist">{others}</p></section>'''
    url = f'/familya/{fam_slug(f)}/'; FAM_URLS.append(url)
    ldf = {"@context":"https://schema.org","@type":"CollectionPage","name":f,"url":BASE+url,"inLanguage":"tr","mainEntity":{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":k+1,"url":f'{BASE}/{p["id"]}/',"name":p['tr']} for k, p in enumerate(ps)]}}
    write(url, page(f'{f}{" (" + trn + ")" if trn else ""}: {n} şifalı bitki | Bitki Tabanı', f'{f} familyasından {n} şifalı ve ritüel bitkisi: ' + ', '.join(p['tr'] for p in ps)[:110] + '.', url, fb, 'kat',
          extra=f'<script type="application/ld+json">{json.dumps(ldf, ensure_ascii=False)}</script>'))

# ---------- mevsim (Anadolu'da şu an toplananlar) ----------
_AY = {m.lower(): i+1 for i, m in enumerate(AYLAR)}
def months_of(txt):
    t = txt.lower()
    if 'yıl boyu' in t or 'toplanmamalı' in t or 'önerilmez' in t or 'sonra sökülür' in t: return set()
    ms = set()
    for a, c in _re.findall(r'(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)\w*\s*[–-]\s*(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)', t):
        x, y = _AY[a], _AY[c]
        while True:
            ms.add(x)
            if x == y: break
            x = x % 12 + 1
    for m in _re.findall(r'(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)', t): ms.add(_AY[m])
    if 'sonbahar' in t: ms |= {9, 10, 11}
    if 'ilkbahar' in t or _re.search(r'(?<!son)bahar', t): ms |= {3, 4, 5}
    if _re.search(r'\byaz', t): ms |= {6, 7, 8}
    if _re.search(r'\bkış', t): ms |= {12, 1, 2}
    return ms
season = [p for p in P if 'anadolu' in p['bolge'] and p['guv'] != 'yuksek' and p['id'] not in YASAL and not p.get('yasal') and not KORUMA.get(p['id'], {}).get('rozet') and LOCAL_DAY.month in months_of(EK[p['id']]['mevsim'])]

# ---------- katalog ----------

def cnt(fn): return sum(1 for p in P if fn(p))
regs = [(k, v) for k, v in REG.items() if cnt(lambda p: k in p['bolge']) >= 3]
REG_LIST = ', '.join(v['ad'].split(' ve ')[0] for k, v in regs[:-1]) + ' ve ' + regs[-1][1]['ad']
durum = [('yasak', 'Türkiye’de yasak', lambda p: YASAL.get(p['id'], ('',))[0] == 'yasak'),
         ('kisitli', 'Türkiye’de kısıtlı veya lisanslı', lambda p: YASAL.get(p['id'], ('',))[0] in ('kisitli', 'lisansli')),
         ('koruma', 'Koruma gerektiren', lambda p: bool(KORUMA.get(p['id'], {}).get('rozet'))),
         ('zehir', 'Zehirli', lambda p: 'zehir' in p['kat'])]
groups = [('bolge','Bölge',[(k,v['ad'],dot(k),cnt(lambda p,k=k: k in p['bolge'])) for k,v in regs]),
          ('kat','Kullanım',[(k,v,'',cnt(lambda p,k=k: k in p['kat'])) for k,v in KAT.items() if k != 'zehir']),
          ('kanit','Kanıt düzeyi',[(k,v['ad'],pips(k),cnt(lambda p,k=k: p['kanit']==k)) for k,v in KANIT.items()]),
          ('guv','Güvenlik',[(k,v,f'<span class="dot" style="background:var(--s-{k})"></span>',cnt(lambda p,k=k: p['guv']==k)) for k,v in GUV.items()]),
          ('durum','Zehir, yasal durum ve koruma',[(k,v,'',cnt(fn)) for k,v,fn in durum]),
          ('kisim','Kullanılan kısım',[(k,v,'',cnt(lambda p,k=k: k in kisim_of(p).split())) for k,v,_ in KISIM]),
          ('ay','Toplama ayı',[(f'a{m}',AYLAR[m-1],'',cnt(lambda p,m=m: f'a{m}' in ay_of(p).split())) for m in range(1, 13)])]
filters = ''.join(f'<div class="fgroup"><span>{lab}</span><div class="chips">' + ''.join(f'<button type="button" class="chip" data-g="{g}" data-k="{k}" aria-pressed="false">{ic}{e(v)} <span class="n">{n}</span></button>' for k,v,ic,n in opts) + '</div></div>' for g,lab,opts in groups)
FEATURED = ['uzerlik','ayahuasca','salep','maca','kantaron','koka','kina','huito','safran','guarana','sigla','peyote']
learn_note = '<p class="hint" id="learnHint"><b>Öğrendiklerim</b> sayacı, bitki sayfalarının sonundaki “Öğrendim” düğmesiyle işaretlediğin bitkileri gösterir. Giriş yapmadan da çalışır; o zaman yalnızca bu tarayıcıda saklanır. <a href="/hesap/">Google ile giriş yaparsan</a> bütün cihazlarında görünür.</p>'
katalog = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Katalog</span></nav>
<header class="page-head"><span class="eyebrow">{len(P)} kayıt</span><h1>Bitki kataloğu</h1><p>Bütün bitkileri bölgeye, kullanıma, kanıt düzeyine, güvenliğe ve yasal duruma göre süz. Seçtiğin filtreler adres çubuğuna yazılır; bağlantıyı paylaşabilirsin.</p></header>
<section style="display:flex;flex-direction:column;gap:18px" aria-label="Katalog">
  <div class="controls">
    <label class="search" for="q">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="2" fill="none"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="q" type="search" placeholder="Bitki, Latince ad, kullanım ara… (ör. nazar, öksürük, tütsü)" autocomplete="off" aria-label="Bitki ara">
    </label>
    <details class="fbox"><summary>Filtreler <span class="fcount" hidden></span></summary><div class="fgroups">{filters}</div></details>
  </div>
  <div class="resultbar"><span id="count" aria-live="polite">{len(P)} / {len(P)} kayıt gösteriliyor</span><button class="linkbtn" id="reset" type="button" hidden>Filtreleri temizle</button><label class="sortsel">Sırala <select id="sort"><option value="no">Katalog sırası</option><option value="az">A’dan Z’ye</option><option value="kanit">Kanıtı en güçlü</option></select></label></div>
  <div class="grid">{"".join(card(p) for p in P)}</div>
  <div class="empty" id="empty" hidden>Bu arama ve filtrelerle eşleşen bitki yok. Bir filtreyi kaldırmayı ya da farklı bir kelime denemeyi dene.</div>
</section>
<details class="kstats"><summary>İstatistikler ve öğrendiklerim</summary><div class="stats"><span><strong>{len(P)}</strong> bitki</span><span><strong>{len(regs)}</strong> bölge</span><span><strong>{len(BR)}</strong> kültür köprüsü</span><span>Öğrendiklerim <strong id="learnedCount">0</strong>/{len(P)} <span class="muted-s">(<a href="/hesap/">giriş yaparsan</a> her cihazda)</span></span></div>
{learn_note}</details>
'''
ld_kat = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Bitki kataloğu","url":BASE+"/katalog/","inLanguage":"tr","isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},
           "mainEntity":{"@type":"ItemList","numberOfItems":len(P),"itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{BASE}/{p["id"]}/',"name":p['tr']} for i,p in enumerate(P)]}},
          {"@context":"https://schema.org","@type":"Dataset","name":"Bitki Tabanı: şifalı ve ritüel bitkiler veri seti","description":f"Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika’dan {len(P)} şifalı ve ritüel bitkisinin geleneksel kullanımı, bilimsel kanıt düzeyi, güvenlik, koruma ve yasal durumu.","url":BASE+"/katalog/","inLanguage":"tr","creator":{"@type":"Organization","name":"Bitki Tabanı","url":BASE+"/"},"keywords":["şifalı bitkiler","etnobotanik","geleneksel tıp","Anadolu","Amazon","And Dağları"],"variableMeasured":["Geleneksel kullanım","Kanıt düzeyi","Güvenlik","Koruma durumu","Türkiye’de yasal durum"],"isAccessibleForFree":True}]
write('/katalog/', page(f'Bitki kataloğu: {len(P)} şifalı ve ritüel bitki | Bitki Tabanı', f'{len(P)} şifalı ve ritüel bitkiyi bölgeye, kullanıma, bilimsel kanıta, güvenliğe ve Türkiye’deki yasal duruma göre süz.', '/katalog/', katalog, 'kat', '<script src="/assets/catalog.js" defer></script>', extra=''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld_kat)))

# ---------- köprüler ----------
def mini(p):
    return f'<a class="mini" href="/{p["id"]}/"><span class="where">{"".join(dot(r) for r in p["bolge"])} {e(" · ".join(REG[r]["ad"] for r in p["bolge"]))}</span><b>{e(p["tr"])}</b><span class="latin">{e(p["la"])}</span></a>'
def bridge_map(only=None):
    x0 = mapgeo.project(-128, 0)[0]; x1 = mapgeo.project(128, 0)[0]
    y0 = mapgeo.project(0, 66)[1]; y1 = mapgeo.project(0, -42)[1]
    K = [0.10, 0.30, 0.20, 0.42, 0.14, 0.36, 0.24, 0.50, 0.06, 0.26, 0.46, 0.18, 0.34, 0.04, 0.22, 0.40]
    T = [0.50, 0.40, 0.60, 0.40, 0.66, 0.46, 0.55, 0.20, 0.62, 0.16, 0.72, 0.68, 0.88, 0.45, 0.25, 0.58]
    out = [f'<svg class="map{" focus" if only else ""}" viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}" role="img" aria-labelledby="mapTitle{only or ''}"><title id="mapTitle{only or ''}">Kültür köprüleri haritası: Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika arasındaki bitki bağlantıları</title>',
           f'<path class="land" d="{mapgeo.land_path()}"/>']
    for i, pts in enumerate(BR_GEO, 1):
        P0 = mapgeo.project(*pts[0][:2])
        g = [f'<g class="arc{" on" if only == i else ""}" data-i="{i}">']
        labels, mids = [], []
        for j, pt in enumerate(pts[1:]):
            P1 = mapgeo.project(*pt[:2])
            dx, dy = P1[0] - P0[0], P1[1] - P0[1]
            d = math.hypot(dx, dy) or 1
            nx, ny = -dy / d, dx / d
            if ny > 0: nx, ny = -nx, -ny          # yay hep kuzeye doğru kabarsın
            k = K[(i - 1) % len(K)] + 0.06 * j
            C = ((P0[0] + P1[0]) / 2 + nx * d * k, (P0[1] + P1[1]) / 2 + ny * d * k)
            g.append(f'<path class="line" d="M{P0[0]} {P0[1]} Q{C[0]:.1f} {C[1]:.1f} {P1[0]} {P1[1]}"/>')
            t = T[(i - 1) % len(T)]
            mids.append(((1-t)**2 * P0[0] + 2*(1-t)*t * C[0] + t*t * P1[0], (1-t)**2 * P0[1] + 2*(1-t)*t * C[1] + t*t * P1[1]))
        for pt in pts:
            x, y = mapgeo.project(*pt[:2])
            g.append(f'<circle class="end" cx="{x}" cy="{y}" r="4.5" style="fill:var({REG[pt[3]]["c"]})"/>')
            anchor = 'start' if (x < x0 + 140 or x > 420) and not x > x1 - 160 else 'end'
            dxl = -9 if anchor == 'end' else 9
            g.append(f'<text class="lbl" x="{x + dxl}" y="{y + 4}" text-anchor="{anchor}">{e(pt[2])}</text>')
        mx, my = mids[0]
        g.append(f'<a href="/kopruler/{slug_of(BR[i-1])}/" class="num" aria-label="Köprü {i}: {e(BR[i-1]["t"])}"><circle cx="{mx:.1f}" cy="{my:.1f}" r="11"/><text x="{mx:.1f}" y="{my + 4:.1f}" text-anchor="middle">{i}</text></a>')
        g.append('</g>')
        out.append(''.join(g))
    out.append('</svg>')
    return ''.join(out)

items = []
for i, b in enumerate(BR, 1):
    a = byId[b['a']]; c = byId.get(b.get('b')) if b.get('b') else None
    txt = f'<div class="txt"><h2><span class="bn">{i}</span><a href="/kopruler/{slug_of(b)}/">{e(b["t"])}</a></h2><p>{e(b["d"])}</p><p><a class="cta" href="/kopruler/{slug_of(b)}/">Karşılaştırmayı oku →</a></p></div>'
    items.append(f'<article class="bridge" id="kopru-{i}" data-i="{i}" tabindex="-1">{mini(a)}<span class="arrow" aria-hidden="true">↔</span>{mini(c)}{txt}</article>' if c else f'<article class="bridge single" id="kopru-{i}" data-i="{i}" tabindex="-1">{mini(a)}<span class="note">Aynı bitki, birden fazla kültür</span>{txt}</article>')
br = f'''<header class="page-head"><span class="eyebrow">{len(BR)} karşılaştırma</span><h1>Kültür köprüleri</h1><p>Birbirinden binlerce kilometre uzaktaki kültürler, çoğu zaman aynı molekülleri ya da aynı bitkiyi benzer dertlere kullanmış. Haritadaki her yay bir köprü; üzerine gel ya da aşağıdaki listeden birini seç.</p></header>
<figure class="mapwrap">{bridge_map()}<figcaption>Harita: Natural Earth (kamu malı), Natural Earth izdüşümü. Noktalar bölgeyi temsil eder, kesin toplama yerini değil.</figcaption></figure>
<div class="bridges">{"".join(items)}</div>'''
write('/kopruler/', page(f'Kültür köprüleri haritası: {len(BR)} bitki karşılaştırması | Bitki Tabanı', f'{REG_LIST} arasındaki {len(BR)} kültür köprüsü: üzerlik ve ayahuasca, efedra ve koka, salep ve maca gibi bitkileri yan yana karşılaştır.', '/kopruler/', br, 'br', '<script src="/assets/kopruler.js" defer></script>'))

# ---------- köprü karşılaştırma sayfaları ----------
def cmp_rows(ps):
    yas = lambda q: YASAL_AD[YASAL[q['id']][0]] if q['id'] in YASAL else 'Özel bir kısıt yok'
    rows = [('Latince adı', lambda q: f'<i>{e(q["la"])}</i>'), ('Familya', lambda q: e(q['fam'])), ('Bölge', lambda q: ', '.join(e(REG[r]['ad']) for r in q['bolge'])),
            ('Kullanılan kısım', lambda q: e(q['kisim'])), ('Kullanım', lambda q: ', '.join(KAT[k] for k in q['kat'])), ('Bilimsel kanıt', lambda q: KANIT[q['kanit']]['ad']),
            ('Güvenlik', lambda q: f'<span class="sf {q["guv"]}">{GUV[q["guv"]]}</span>'), ('Türkiye’de yasal durum', yas)]
    head = '<tr><th scope="col"></th>' + ''.join(f'<th scope="col"><a href="/{q["id"]}/">{e(q["tr"])}</a></th>' for q in ps) + '</tr>'
    body = ''.join('<tr><th scope="row">' + lab + '</th>' + ''.join(f'<td>{fn(q)}</td>' for q in ps) + '</tr>' for lab, fn in rows)
    return f'<div class="tablewrap"><table class="cmp"><thead>{head}</thead><tbody>{body}</tbody></table></div>'

for i, br_ in enumerate(BR, 1):
    slug = slug_of(br_); a = byId[br_['a']]; c = byId.get(br_.get('b')) if br_.get('b') else None
    ps = [a] + ([c] if c else [])
    title_names = f'{a["tr"]} ve {c["tr"]}' if c else a['tr']
    blocks = ''
    for q in ps:
        uses = ''.join(f'<div class="use"><div class="who">{e(w)}</div><p>{e(t)}</p></div>' for w, t in q['kul'])
        blocks += f'<section class="sec"><h2>{e(q["tr"])}</h2><div class="uses">{uses}</div><p><b>Bilim:</b> {e(q["bilim"])}</p><p><b>Güvenlik:</b> {e(q["guvNot"])}</p><p><a class="cta" href="/{q["id"]}/">{e(q["tr"])} sayfasının tamamı →</a></p></section>'
    others = ''.join(f'<li><a href="/kopruler/{slug_of(x)}/">{e(x["t"])}</a></li>' for x in BR if x is not br_)
    prev_, next_ = BR[i-2], BR[i % len(BR)]
    body = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/kopruler/">Kültür köprüleri</a><span>/</span><span>{e(br_["t"])}</span></nav>
<article class="sheet">
<header class="page-head"><span class="eyebrow">Kültür köprüsü {i} · {e(title_names)}</span><h1>{e(br_["t"])}</h1><p>{e(br_["d"])}</p></header>
<figure class="mapwrap">{bridge_map(only=i)}<figcaption>Harita: Natural Earth (kamu malı). Noktalar bölgeyi temsil eder, kesin toplama yerini değil.</figcaption></figure>
<section class="sec"><h2>Yan yana</h2>{cmp_rows(ps)}</section>
{blocks}
<aside class="disclaimer" role="note"><b>Tıbbi tavsiye değildir.</b> Bu sayfa geleneksel kullanımları kültürel bir kayıt olarak karşılaştırır; teşhis ya da tedavi önerisi değildir. Herhangi bir bitkiyi kullanmadan önce hekimine ya da eczacına danış. Zehirlenme şüphesinde Ulusal Zehir Danışma Merkezi’ni (UZEM) <b>114</b> numaradan ara.</aside>
<p class="updated">Son gözden geçirme: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time></p>
<section class="sec"><h2>Diğer köprüler</h2><ul class="otherlist">{others}</ul></section>
<div class="sheet-foot"><a class="cta" href="/kopruler/">Bütün köprüler ve harita →</a><div class="pager"><a href="/kopruler/{slug_of(prev_)}/">← {e(prev_["t"])}</a><a href="/kopruler/{slug_of(next_)}/">{e(next_["t"])} →</a></div></div>
</article>'''
    ldb = [{"@context":"https://schema.org","@type":"Article","author":AUTHOR,"headline":br_['t'],"description":br_['d'],"inLanguage":"tr","url":f'{BASE}/kopruler/{slug}/',"dateModified":CONTENT_DATE,
            "about":[{"@type":"Taxon","name":short_la(q),"alternateName":q['tr']} for q in ps],"isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},
            "image":[f'{BASE}/img/{q["id"]}-960.jpg' for q in ps if q['id'] in IMG]},
           {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Kültür köprüleri","item":BASE+"/kopruler/"},{"@type":"ListItem","position":3,"name":br_['t'],"item":f'{BASE}/kopruler/{slug}/'}]}]
    desc = (f'{title_names}: ' + br_['d'])[:157]
    write(f'/kopruler/{slug}/', page(f'{br_["t"]}: {title_names} | Bitki Tabanı', desc, f'/kopruler/{slug}/', body, 'br', narrow=True,
          extra=''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ldb), image=(f'{BASE}/img/{a["id"]}-960.jpg' if a['id'] in IMG else None)))

# ---------- hakkında ----------
about = '''<header class="page-head"><span class="eyebrow">Hakkında</span><h1>Bitki Tabanı nedir?</h1></header>
<section class="sec"><p>Bitki Tabanı, farklı kültürlerde şifa ve ritüel için kullanılan bitkileri bir araya getiren bağımsız bir etnobotanik kayıt defteridir. Amacı merak uyandırmak ve geleneksel bilgiyi bugünkü bilimsel bilgiyle yan yana koymak.</p></section>
<section class="sec"><h2>Kim hazırlıyor</h2><p>''' + BIO + '''</p><p>''' + SOCIAL + ''' · <a href="/yontem/">Kayıtları nasıl hazırladığını oku →</a></p></section>
<section class="sec"><h2>Bağımsız</h2><p>Bitki Tabanı’nın bilgi içeriği hiçbir satıcıdan ve şirketten bağımsızdır: bitki, takviye ya da tören satmaz; inziva veya ayahuasca seremonisi düzenlemez, bunlara yönlendirmez ve reklam almaz. İleride düzenlenebilecek atölye ve doğa yürüyüşleri ayrıca duyurulur; sitedeki bilgiyi etkilemez. Kayıtlarda adı geçen hiçbir marka ya da satıcıyla bağı yoktur.</p></section>
<section class="sec"><h2>İletişim</h2><p>Bir hata gördüysen ya da yöresel bir kullanım biliyorsan <a href="mailto:iletisim@bitkitabani.com">iletisim@bitkitabani.com</a> adresine yaz.</p></section>
<section class="sec"><h2>Kayıtlar nasıl hazırlanıyor</h2><p>Ayrıntılı kurallar <a href="/yontem/">Yöntem</a> sayfasında. Her kayıt; geleneksel kullanımı, hazırlama biçimini, bilimin bugün ne söylediğini ve güvenlik notlarını içerir. Kanıt düzeyi Avrupa İlaç Ajansı (EMA/HMPC) monografileri, ABD NCCIH özetleri, Cochrane derlemeleri ve hakemli literatüre göre belirlenir. Kaynaklar her bitkinin sayfasının sonunda listelenir.</p></section>
<section class="sec"><h2>Önemli not</h2><p>Bu site tıbbi tavsiye vermez. Burada anlatılan geleneksel kullanımlar bir öneri değil, kültürel bir kayıttır. Zehirli ve yasal kısıtlı bitkiler, tarihleri ve riskleri anlaşılsın diye yer alır. Herhangi bir bitkiyi kullanmadan önce bir hekime ya da eczacıya danış.</p></section>
<section class="sec"><h2>Yerel bilgiye saygı</h2><p>Kayıtlardaki geleneksel bilgi, onu kuşaklar boyunca koruyan toplulukların mirasıdır. Bitki Tabanı bu bilginin kaynağını görünür kılmayı ve aşırı toplanan türler konusunda farkındalık yaratmayı amaçlar.</p></section>
<section class="sec"><h2>Renklerimiz ve motifimiz</h2><p>Sitenin renkleri, Anadolu ile Amazon ve And Dağları’nın ortak boya geleneklerinden geliyor. Motif ise Anadolu kilimlerindeki göz ve baklava desenini, Shipibo halkının kené çizgileri ve And dokumalarının basamaklı baklavasıyla birleştiriyor.</p>
<div class="palette">
<div class="swatch"><i style="background:var(--accent)"></i><b>Kırmızı</b><span>Anadolu’da kök boya ve kırmız böceği (“kırmızı” kelimesi buradan gelir); And’larda koşnil, Amazon’da achiote.</span></div>
<div class="swatch"><i style="background:var(--indigo)"></i><b>Çivit</b><span>Anadolu kilimlerinin çivit mavisi; Amazon’da huito meyvesiyle yapılan lacivert beden boyası.</span></div>
<div class="swatch"><i style="background:var(--ochre)"></i><b>Safran</b><span>Anadolu’da safran ve cehri sarısı; And dokumalarının toprak sarısı tonları.</span></div>
<div class="swatch"><i style="background:var(--paper);border:1px solid var(--rule)"></i><b>Yün</b><span>Boyanmamış yünün doğal rengi; iki coğrafyada da dokumanın zemini.</span></div>
</div></section>
<section class="sec"><h2>Görseller</h2><p>Fotoğraflar Wikimedia Commons’tan özgür lisanslarla kullanılır. Hepsi aynı dikey kadrajda, bitkiyi tanıtan kısma yakın çekimdir; yazar ve lisans bilgisi her fotoğrafın altında yazar.</p></section>'''
write('/hakkinda/', page('Hakkında | Bitki Tabanı', 'Bitki Tabanı’nın amacı, kayıtların nasıl hazırlandığı ve kaynak yaklaşımı.', '/hakkinda/', about, 'about', narrow=True))


# ---------- fotoğraf seçim sayfası (gizli) ----------
def taxon_of(p):
    t = POWO.get(p['id']) or short_la(p)
    t = re.sub(r'\s+ve diğer.*$', '', t)
    return 'Amanita muscaria' if p['id'] == 'sinekmantari' else t
order = sorted(P, key=lambda p: (p['id'] in FILES, p['no']))
def pickrow(p):
    m = IMG.get(p['id'], {})
    durum = 'Elle seçildi' if p['id'] in FILES else ('Otomatik seçildi, onay bekliyor' if m else 'Fotoğraf yok')
    return f'<section class="pick-row" data-id="{p["id"]}" data-taxon="{e(taxon_of(p))}"><h2>{acc(p["no"])} · {e(p["tr"])} <span class="latin">{e(taxon_of(p))}</span> <span class="lg">{durum}</span></h2><div class="cands"><p class="muted">Adaylar yükleniyor…</p></div></section>'
rows = ''.join(pickrow(p) for p in order)
secim = f'''<header class="page-head"><span class="eyebrow">Yalnızca yönetici için</span><h1>Fotoğraf seçimi</h1><p>Otomatik seçilen fotoğraflar en üstte. Beğenmediğin bitki için daha iyi bir yakın çekime tıkla; beğendiklerine dokunmana gerek yok. Seçimlerin bu tarayıcıda saklanır. Bitince alttaki listeyi kopyalayıp Claude’a gönder.</p></header>
{rows}
<div class="result-box"><div class="row"><span id="done"></span><button type="button" id="copy">Listeyi kopyala</button><span id="copied"></span></div><textarea id="result" readonly aria-label="Seçim listesi"></textarea></div>'''
write('/secim/', page('Fotoğraf seçimi | Bitki Tabanı', 'Fotoğraf seçimi', '/secim/', secim, '', '<script src="/assets/photo.js" defer></script><script src="/assets/secim.js" defer></script>', extra='<meta name="robots" content="noindex, nofollow">'))


# ---------- ana sayfa ----------
pool = [p for p in P if p['guv'] != 'yuksek']
def day_pick(d):
    pl = [p for p in pool if YENI.get(p['id'], datetime.date.min) <= d]
    return pl[(d - datetime.date(1970, 1, 1)).days % len(pl)]
today_p = day_pick(LOCAL_DAY)
LEDE = f'{REG_LIST}’dan {len(P)} şifalı ve ritüel bitkisi. Her kayıtta geleneksel kullanım, bilimin söyledikleri, güvenlik notu ve kaynaklar bir arada.'

REG_TXT = {'anadolu':'Nazar tütsüsünden kına gecesine, Anadolu’nun şifa ve ritüel otları.','asya':'İskit tütsülerinden Sibirya şamanlarına, bozkırın ve taygaların bitkileri.',
           'and':'Koka yaprağından kantuta çiçeğine, And Dağları’nın kutsal bitkileri.','amazon':'Ayahuasca sarmaşığından huito boyasına, yağmur ormanının öğretmen bitkileri.',
           'kamerika':'Ak adaçayından peyoteye, Kuzey Amerika yerli halklarının bitkileri.'}
regcards = ''.join(f'<a class="regcard" href="/katalog/?bolge={k}"><span class="where">{dot(k)} {e(v["ad"])}</span><b>{cnt(lambda p,k=k: k in p["bolge"])} bitki</b><span>{e(REG_TXT.get(k,""))}</span></a>' for k,v in regs)

# ---------- her gün yeni bitki: ana sayfa bandı ----------
IG_URL = 'https://www.instagram.com/bitkitabani/'
NEXT_Q = min(KUYRUK_LEFT, key=lambda q: q['yayin']) if KUYRUK_LEFT else None
def teaser():
    if not NEXT_Q: return ''
    nd = datetime.date.fromisoformat(NEXT_Q['yayin'])
    when = 'Yarın' if (nd - LOCAL_DAY).days == 1 else tr_date(nd).rsplit(',', 1)[0]
    return f'<p class="teaser"><b>{when}:</b> {e(REG[NEXT_Q["bolge"][0]]["ad"])} bölgesinden yeni bir bitki geliyor.</p>'
def newband():
    if not NEWEST: return ''
    np_ = byId[NEWEST[0]]; d0 = YENI[np_['id']]
    lab = 'Bugün eklendi' if d0 == LOCAL_DAY else 'Dün eklendi' if (LOCAL_DAY - d0).days == 1 else 'Son eklenen · ' + tr_date(d0).rsplit(',', 1)[0]
    prev = ''.join(f'<li><a href="/{i}/">{e(byId[i]["tr"])}</a> <span class="mono-d">{YENI[i].day} {AYLAR[YENI[i].month-1]}</span></li>' for i in NEWEST[1:5])
    return f"""<section class="newband" aria-labelledby="nbh">
  <a class="nb-main" href="/{np_["id"]}/">{ph(np_, 500)}<span class="nb-txt"><span class="eyebrow">{lab}</span><b id="nbh">{e(np_["tr"])}</b><i>{e(short_la(np_))}</i><span class="nb-fact">{e(np_["ilginc"])}</span><span class="cta small">Sayfayı oku →</span></span></a>
  <div class="nb-side"><p class="nb-say"><b>Her gün yeni bir bitki.</b> Katalog her gece bir kayıt büyüyor.</p>{teaser()}{('<ul class="nb-list">' + prev + '</ul>') if prev else ''}<p class="nb-links"><a href="/yeni/">Bütün yeni eklenenler →</a><a href="{IG_URL}" rel="noopener">Instagram’da her gün →</a><a href="/yeni/rss.xml">RSS</a></p></div>
</section>"""
# ---------- ritüel ve mevsim takvimi ----------
from takvim import OLAYLAR
def olay_tarihi(o, yil):
    if len(o['tarih']) == 2: return datetime.date(yil, int(o['tarih']), 1), datetime.date(yil, int(o['tarih']) % 12 + 1, 1) - datetime.timedelta(days=1) if o['tarih'] != '12' else datetime.date(yil, 12, 31)
    m, d = map(int, o['tarih'].split('-')); g = datetime.date(yil, m, d); return g, g
def aktif_olay(gun):
    for o in OLAYLAR:
        bas, son = olay_tarihi(o, gun.year)
        if bas - datetime.timedelta(days=o['once']) <= gun <= son: return o, bas
    return None, None
AKTIF, AKTIF_T = aktif_olay(LOCAL_DAY)
def _olink(o):
    u, t = o['link']
    if u.startswith('/kavram/') and not any(u == f'/kavram/{k["slug"]}/' for k in KAV): return ('/toplama-takvimi/', 'Bu ay doğada neler var?')
    return u, t
def takvim_band():
    if not AKTIF: return ''
    o = AKTIF; ne = 'bugün' if AKTIF_T == LOCAL_DAY else ('bu ay' if len(o['tarih']) == 2 else f'{AKTIF_T.day} {AYLAR[AKTIF_T.month - 1]}')
    bt = ''.join(f'<a class="chip" href="/{x}/">{e(byId[x]["tr"])}</a>' for x in o['bitkiler'] if x in byId)
    return f'<section class="takvimband"><span class="eyebrow">Takvim · {ne}</span><h2><a href="/takvim/#{o["slug"]}">{e(o["ad"])}</a></h2><p>{e(o["kisa"])}</p>{("<div class=related>" + bt + "</div>") if bt else ""}<p><a class="cta small" href="{_olink(o)[0]}">{e(_olink(o)[1])} →</a></p></section>'

home = f'''
<header class="top">
  <div class="brand">
    <span class="eyebrow">Etnobotanik kayıt defteri</span>
    <h1 class="wordmark">Bitki <em>Tabanı</em></h1>
    <p class="lede">{LEDE}</p>
    <form class="hsearch" id="ara" action="/katalog/" method="get" role="search" autocomplete="off">
      <input id="hq" name="q" type="search" placeholder="Bitki ara ya da derdini yaz: kantaron, ardıç, uyku tutmuyor…" aria-label="Bitki ara" aria-controls="hqList" aria-autocomplete="list">
      <button type="submit" class="cta">Ara</button>
      <ul id="hqList" class="hq-list" role="listbox" hidden></ul>
    </form>
    <script id="hqData" type="application/json">{json.dumps([[p['id'], p['tr'], short_la(p), p['diger']] for p in P], ensure_ascii=False).replace('</', '<\\/')}</script>
  </div>
  <div class="todaybox"><a class="today" id="today" href="/{today_p["id"]}/" data-pool="{e(json.dumps([[p["id"], p["tr"], p["la"]] for p in pool], ensure_ascii=False))}"><span class="eyebrow">Bugünün bitkisi</span><b id="todayName">{e(today_p["tr"])}</b><i id="todayLatin">{e(today_p["la"])}</i></a><a class="cta small" href="/gunun-bitkisi/">Geçmiş günlerin bitkileri →</a><p class="streak" id="streak" hidden></p></div>
</header>
{takvim_band()}
<section class="pillars">
  <a class="pillar" href="/katalog/"><span class="eyebrow">Bitkiler</span><b>{len(P)} bitki, {len(REG)} bölge</b><span>Anadolu’dan Amazon’a, fotoğrafı, çizimi ve kaynaklarıyla her bitki.</span></a>
  <div class="pchips">{"".join(f'<a class="chip" href="/katalog/?bolge={k}">{dot(k)} {e(v["ad"])}</a>' for k, v in REG.items())}<a class="chip" href="/toplama-takvimi/">Doğada bu ay →</a></div>
  <a class="pillar" href="/rehber/"><span class="eyebrow">Şifa</span><b>Hangi derde hangi bitki?</b><span>Kanıtı en güçlü olandan başlayarak; güvenlik ve ilaç etkileşimiyle.</span></a>
  <div class="pchips">{"".join(f'<a class="chip" href="/rehber/{k["slug"]}/">{e(k["kisa"])}</a>' for k in [k for k in KONULAR if sum(1 for pid, _ in k["bitkiler"] if pid in byId) >= 2][:6])}<a class="chip" href="/bitki-bul/">Üç soruda bul →</a></div>
  <a class="pillar" href="/kultur/"><span class="eyebrow">Kültür ve ritüel</span><b>Bitkiler yalnızca ilaç değildir</b><span>Şamanizm, animizm, semboller, kutsal ağaçlar ve ritüel takvimi.</span></a>
  <div class="pchips"><a class="chip" href="/kavram/">Kavramlar</a><a class="chip" href="/semboller/">Semboller</a><a class="chip" href="/kopruler/">Kültür köprüleri</a><a class="chip" href="/yazilar/">Yazılar</a><a class="chip" href="/takvim/">Takvim</a></div>
</section>
<section class="sec"><h2>Nereden başlamalı?</h2><ol class="start">
<li><a href="/papatya/"><b>Papatya</b></a>: herkesin bildiği bir çayın arkasındaki bilim.</li>
<li><a href="/kantaron/"><b>Sarı kantaron</b></a>: kanıtı güçlü ama ilaç etkileşimleri ciddi.</li>
<li><a href="/uzerlik/"><b>Üzerlik</b></a>: nazar dumanından ayahuascaya uzanan bir köprü.</li>
<li><a href="/salep/"><b>Salep</b></a>: sevdiğimiz bir içeceğin yabani orkidelere bedeli.</li>
<li><a href="/koka/"><b>Koka</b></a>: And’larda kutsal bir yaprak, başka yerde yasak bir madde.</li>
</ol></section>
'''
ldsite = {"@context":"https://schema.org","@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/","inLanguage":"tr","description":"Şifalı ve ritüel bitkiler için Türkçe etnobotanik kayıt defteri."}
write('/index.html', page('Bitki Tabanı: şifalı ve ritüel bitkiler veri tabanı', f'{REG_LIST}’dan {len(P)} şifalı ve ritüel bitkisi: geleneksel kullanım, bilimsel kanıt, güvenlik ve kaynaklar.', '/', home, 'home', '<script src="/assets/streak.js" defer></script><script src="/assets/home.js" defer></script>', extra=f'<script type="application/ld+json">{json.dumps(ldsite, ensure_ascii=False)}</script>'))


# ---------- /yeni/: her gün eklenen bitkiler ----------
nl = ''.join(f'<li><span class="mono-d">{tr_date(YENI[i])}</span><a href="/{i}/">{e(byId[i]["tr"])}</a> <i class="latin">{e(short_la(byId[i]))}</i></li>' for i in NEWEST)
yn = f"""
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Yeni eklenenler</span></nav>
<header class="page-head"><span class="eyebrow">Her gün yeni bir bitki</span><h1>Yeni eklenenler</h1><p>Bitki Tabanı her gece yarısı bir kayıt büyüyor. Her yeni bitki öteki kayıtlar gibi geleneksel kullanım, bilimsel kanıt, güvenlik notu ve kaynaklarla gelir. Şu an katalogda {len(P)} bitki var.</p></header>
{teaser()}
{('<div class="grid">' + ''.join(card(byId[i]) for i in NEWEST[:12]) + '</div>') if NEWEST else '<p>İlk yeni bitki bu gece geliyor.</p>'}
{abone("yeni")}<section class="sec"><h2>Takip et</h2><p><a class="cta" href="{IG_URL}" rel="noopener">Instagram’da her gün bir bitki →</a></p><p class="tg-cta"><a class="cta" href="https://t.me/bitkitabani" rel="noopener" target="_blank">Telegram kanalında her akşam bir bitki →</a> <span class="muted-s">Bildirimle gelir, e-posta gerekmez.</span></p><p><a class="cta" href="/yeni/rss.xml">RSS ile takip et →</a> <span class="muted-s">Bir RSS okuyucusu her yeni bitkiyi getirir; bildirim ya da e-posta yok.</span></p></section>
{('<section class="sec"><h2>Bütün liste</h2><ul class="daylist">' + nl + '</ul></section>') if nl else ''}
"""
write('/yeni/', page(f'Yeni eklenen bitkiler | Bitki Tabanı', f'Bitki Tabanı’na her gün yeni bir şifalı ya da ritüel bitki ekleniyor. Son eklenenler ve tarihleri.', '/yeni/', yn, 'yeni', image=(f'{BASE}/img/{NEWEST[0]}-960.jpg' if NEWEST and NEWEST[0] in IMG else None)))
from email.utils import format_datetime as _fd
_it = ''
for i in NEWEST[:30]:
    q = byId[i]; d = YENI[i]; dt = datetime.datetime(d.year, d.month, d.day, 0, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=3)))
    _it += f'<item><title>Yeni bitki: {e(q["tr"])} ({e(short_la(q))})</title><link>{BASE}/{i}/</link><guid>{BASE}/{i}/</guid><pubDate>{_fd(dt)}</pubDate><description>{e(q["ilginc"])} {e(q["kul"][0][1])}</description></item>'
open(os.path.join(OUT, 'yeni', 'rss.xml'), 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Bitki Tabanı: yeni eklenen bitkiler</title><link>{BASE}/yeni/</link><description>Her gün kataloğa eklenen yeni bitki.</description><language>tr</language>{_it}</channel></rss>')

# ---------- günün bitkisi arşivi ----------
days = [LOCAL_DAY - datetime.timedelta(days=n) for n in range(14)]
tp = today_p
past = ''.join(f'<li><span class="mono-d">{tr_date(d)}</span><a href="/{day_pick(d)["id"]}/">{e(day_pick(d)["tr"])}</a> <i class="latin">{e(short_la(day_pick(d)))}</i></li>' for d in days[1:])
gb = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Günün bitkisi</span></nav>
<header class="page-head"><span class="eyebrow">{tr_date(LOCAL_DAY)}</span><h1>Günün bitkisi: {e(tp["tr"])}</h1><p>Her gün katalogdan bir bitki öne çıkıyor. Ölümcül zehirli ya da yüksek riskli bitkiler bu döngüye alınmaz.</p></header>
<div class="grid sim">{card(tp)}</div>
<section class="sec"><h2>Bugün okumak için</h2><p>{e(tp["kul"][0][1])}</p><p class="fact">{e(tp["ilginc"])}</p><p><a class="cta" href="/{tp["id"]}/">{e(tp["tr"])} sayfasının tamamı →</a></p></section>
<section class="sec"><h2>Her gün</h2><p class="tg-cta"><a class="cta" href="https://t.me/bitkitabani" rel="noopener" target="_blank">Telegram kanalında her akşam bir bitki →</a> <span class="muted-s">Bildirimle gelir, e-posta gerekmez.</span></p><p><a class="cta" href="/gunun-bitkisi/rss.xml">RSS ile takip et →</a> <span class="muted-s">Bir RSS okuyucusu (Feedly, NetNewsWire gibi) her sabah yeni bitkiyi getirir; bildirim ya da e-posta yok.</span></p></section>
<section class="sec"><h2>Son iki hafta</h2><ul class="daylist">{past}</ul></section>
'''
write('/gunun-bitkisi/', page(f'Günün bitkisi: {tp["tr"]} | Bitki Tabanı', f'Bugünün bitkisi {tp["tr"]} ({short_la(tp)}) ve son iki haftanın bitkileri.', '/gunun-bitkisi/', gb, '', narrow=True,
      image=(f'{BASE}/img/{tp["id"]}-960.jpg' if tp['id'] in IMG else None)))

# ---------- RSS ----------
from email.utils import format_datetime
items = ''
for d in days:
    q = day_pick(d); dt = datetime.datetime(d.year, d.month, d.day, 0, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=3)))
    items += f'<item><title>{e(tr_date(d))}: {e(q["tr"])} ({e(short_la(q))})</title><link>{BASE}/{q["id"]}/</link><guid isPermaLink="false">{BASE}/gunun-bitkisi/#{d.isoformat()}</guid><pubDate>{format_datetime(dt)}</pubDate><description>{e(q["kul"][0][1])} {e(q["ilginc"])}</description></item>'
os.makedirs(os.path.join(OUT, 'gunun-bitkisi'), exist_ok=True)
open(os.path.join(OUT, 'gunun-bitkisi', 'rss.xml'), 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Bitki Tabanı: günün bitkisi</title><link>{BASE}/gunun-bitkisi/</link><description>Her gün bir şifalı ya da ritüel bitkisi.</description><language>tr</language>{items}</channel></rss>')

# ---------- günün bilmecesi ----------
def mask(txt, p):
    words = set()
    for src in [p['tr'], p['diger'], p['la'].split()[0]]:
        for w in _re.split(r'[\s,;/()]+', src):
            w = w.strip('.’\'"')
            if len(w) >= 3 and w.lower() not in ('ve', 'otu', 'ağacı', 'kökü', 'çiçeği', 'yaprağı', 'tohumu'): words.add(w)
    for w in sorted(words, key=len, reverse=True):
        txt = _re.sub(r'(?i)\b' + _re.escape(w) + r'\w*', '＿＿＿', txt)
        txt = _re.sub(r'\b' + _re.escape(w.replace('i', 'İ').replace('ı', 'I').upper()[:1] + w[1:]) + r'\w*', '＿＿＿', txt)
    return txt
gp = []
for q in P:
    c = [['Bölge ve kullanım', ', '.join(REG[r]['ad'] for r in q['bolge']) + ' · ' + ', '.join(KAT[k] for k in q['kat'])],
         ['Kullanılan kısım', q['kisim']],
         ['Familya', q['fam'] + (f' ({FAM_TR[q["fam"]]})' if q['fam'] in FAM_TR else '')],
         ['Geleneksel kullanım', mask(q['kul'][0][0] + ': ' + q['kul'][0][1], q)],
         ['İlginç bilgi', mask(q['ilginc'], q)]]
    if q['id'] in IMG: c.append(['img', f'/img/{q["id"]}-500.jpg'])
    gp.append({'id': q['id'], 'tr': q['tr'], 'la': short_la(q), 'fam': q['fam'], 'bolge': q['bolge'], 'c': c})
opts = ''.join(f'<option value="{e(q["tr"])}">' for q in sorted(P, key=lambda q: q['tr']))
oy = f'''
<nav class="crumbs" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>Günün bilmecesi</span></nav>
<header class="page-head"><span class="eyebrow">Her gün yeni bir bitki</span><h1>Günün bilmecesi</h1><p>Katalogdaki {len(P)} bitkiden biri saklı. İlk ipucuyla tahmin et; her yanlış tahminde yeni bir ipucu açılır. Altı hakkın var. Sarı kare, tahminin bölge ya da familya olarak yakın olduğunu gösterir.</p></header>
<div id="game">
<div class="gprog" id="gprog" aria-live="polite"></div>
<ol class="clues" id="clues"><li class="clue"><p>Bilmece yükleniyor… JavaScript kapalıysa <a href="/gunun-bitkisi/">günün bitkisine</a> bakabilirsin.</p></li></ol>
<form id="guessForm" class="guess" autocomplete="off"><label for="guessInput" class="eyebrow">Tahminin</label><div class="row"><input id="guessInput" list="plantNames" placeholder="Bitki adı yaz, listeden seç" required><button type="submit" class="learn">Tahmin et</button></div><p class="muted-s"><span id="left"></span> <span id="gameMsg" role="status"></span></p><datalist id="plantNames">{opts}</datalist></form>
<ul class="guesses" id="guesses"></ul>
<div class="gameend" id="gameEnd" hidden></div>
</div>
<p class="muted-s">Tahminlerin ve serin yalnızca bu tarayıcıda saklanır.</p>
<script type="application/json" id="gameData">{json.dumps({"p": gp, "ay": AYLAR}, ensure_ascii=False)}</script>'''
pass   # bilmece sayfası kaldırıldı (/oyun/ → / yönlenir)

# ---------- hesap ve gizlilik ----------
hz = f'''
<header class="page-head"><span class="eyebrow">Hesap</span><h1>İlerlemeni sakla</h1><p>Google hesabınla giriş yaparsan öğrendiğin bitkiler, serin ve bilmece sonuçların hesabında saklanır; telefonda da bilgisayarda da aynısını görürsün. Giriş yapmadan da her şey çalışır, yalnızca bu tarayıcıda kalır.</p></header>
<div id="acct" data-client="{e(GOOGLE_CLIENT_ID)}">
<div class="stats"><span>Öğrendiklerim <strong id="stLearned">0</strong></span><span>Seri <strong id="stStreak">0</strong> gün</span><span>Bilmece <strong id="stGames">0</strong> gün</span></div>
<section class="sec" id="acctOut"><h2>Giriş</h2>{'<div id="gbtn"></div>' if GOOGLE_CLIENT_ID else '<p>Google ile giriş çok yakında açılacak.</p>'}<p class="muted-s">Yalnızca Google hesap kimlik numaran saklanır; e-postan, adın ve fotoğrafın saklanmaz. Ayrıntılar <a href="/gizlilik/">gizlilik</a> sayfasında.</p></section>
<section class="sec" id="acctIn" hidden><h2>Giriş yapıldı</h2><p>İlerlemen bu hesapla eşitleniyor.</p><p class="btnrow"><button type="button" class="learn" id="logout">Çıkış yap</button> <button type="button" class="learn danger" id="del">Hesabımdaki veriyi sil</button></p></section>
<p class="muted-s" id="acctMsg" role="status"></p>
</div>'''
write('/hesap/', page('Hesap | Bitki Tabanı', 'Google ile giriş yaparak öğrendiğin bitkileri, serini ve bilmece sonuçlarını bütün cihazlarında sakla.', '/hesap/', hz, 'acct', '<script src="/assets/hesap.js" defer></script>', narrow=True,
      extra='<meta name="robots" content="noindex, follow">'))
gz = '''
<header class="page-head"><span class="eyebrow">Gizlilik</span><h1>Hangi bilgileri saklıyorum?</h1><p>Kısaca: çok az. Bitki Tabanı reklam göstermez, seni siteler arasında izlemez ve kimseye veri satmaz.</p></header>
<section class="sec"><h2>Ziyaret sayıları</h2><p>Kaç kişinin hangi sayfayı okuduğunu görmek için Cloudflare Web Analytics ve Google Analytics kullanıyorum. Cloudflare Web Analytics çerez yazmaz ve yalnızca toplu sayılar tutar.</p><p>Google Analytics, ziyaretleri ayırt etmek için tarayıcına çerez yazar ve hangi sayfaları açtığın, siteye nereden geldiğin, cihaz türün ve yaklaşık konumun (ülke, şehir) gibi bilgileri Google’a gönderir. Bu bilgileri yalnızca toplu raporlar olarak görürüz; seni kişi olarak tanımlamak için kullanmam. Google’ın verileri nasıl işlediği için <a href="https://policies.google.com/technologies/partner-sites?hl=tr" rel="noopener">Google’ın açıklamasına</a> bakabilirsin. İstemezsen tarayıcının çerez ayarlarından ya da Google’ın <a href="https://tools.google.com/dlpage/gaoptout?hl=tr" rel="noopener">devre dışı bırakma eklentisiyle</a> engelleyebilirsin.</p></section>
<section class="sec"><h2>Giriş yapmazsan</h2><p>Öğrendiğin bitkiler, serin ve bilmece tahminlerin yalnızca kendi tarayıcının hafızasında (localStorage) durur. Bize hiçbir şey gelmez. Tarayıcı verilerini silersen bunlar da silinir.</p></section>
<section class="sec"><h2>Google ile giriş yaparsan</h2><p>Google bize senin adına bir kimlik belgesi gönderir. Bunun içinden yalnızca Google hesap kimlik numaranı (rastgele görünen bir sayı) saklarız. E-posta adresin, adın ve profil fotoğrafın saklanmaz.</p><p>Bu numarayla birlikte şunları saklarız: öğrendim olarak işaretlediğin bitkiler, serinin günleri ve bilmece tahminlerin. Oturumunu hatırlamak için tarayıcına yalnızca bu iş için kullanılan, 180 gün geçerli bir çerez yazılır.</p><p>Veriler Cloudflare’in sunucularında tutulur. Google ile girişte Google’ın kendi <a href="https://policies.google.com/privacy?hl=tr" rel="noopener">gizlilik politikası</a> geçerlidir.</p></section>
<section class="sec" id="bulten"><h2>Bülten</h2><p>Bültene kaydolursan yalnızca e-posta adresin, kayıt ve onay tarihi, kaydolduğun sayfa ve isteğe bağlı duyuru tercihin saklanır. Kayıt çift onaylıdır: gelen e-postadaki bağlantıya tıklamadıkça listeye eklenmezsin; onaylanmayan adresler 7 gün sonra silinir. E-postalar Resend aracılığıyla gönderilir. Her e-postadaki “Bültenden çık” bağlantısı adresini listeden hemen ve tamamen siler. Adresin kimseyle paylaşılmaz, satılmaz ve reklam için kullanılmaz. Duyuru kutusunu işaretlediysen, bülten dışında atölye, doğa yürüyüşü ya da gezi gibi Bitki Tabanı etkinliklerinin duyurularını da alırsın.</p></section>
<section class="sec"><h2>Silme</h2><p><a href="/hesap/">Hesap</a> sayfasındaki “Hesabımdaki veriyi sil” düğmesi saklanan bütün ilerlemeni hemen siler. Google hesabından da Bitki Tabanı’nın erişimini dilediğin zaman kaldırabilirsin.</p></section>
<section class="sec"><h2>Haklarına dair</h2><p>6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında verilerin hakkında bilgi isteme, düzeltme ve silme hakların vardır. Yukarıdaki silme düğmesi bu hakkı tek tıkla kullanmanı sağlar.</p></section>
'''
write('/gizlilik/', page('Gizlilik | Bitki Tabanı', 'Bitki Tabanı hangi bilgileri saklar: giriş yapmazsan hiçbirini; Google ile girişte yalnızca hesap kimlik numaranı ve ilerlemeni.', '/gizlilik/', gz, '', narrow=True))

# ---------- yöntem ----------
GZ_HTML = (f'<section class="sec" id="gozden"><h2>Uzman gözden geçirmesi</h2><p><b>{e(GZ_KISI["ad"])}</b>, {e(GZ_KISI.get("unvan", "Eczacı"))}. {e(GZ_KISI.get("aciklama", ""))}</p><p>Gözden geçirilen sayfalarda güvenlik notları, ilaç etkileşimleri ve kullanım bilgileri bir eczacı tarafından kontrol edilmiştir; kontrol tarihi her sayfanın altında yazar. Şu ana kadar {len(GZ)} bitki sayfası gözden geçirildi.</p></section>') if GZ_KISI else ''
yt = """
<header class="page-head"><span class="eyebrow">Yöntem</span><h1>Kayıtları nasıl hazırlıyorum?</h1><p>Bitki Tabanı bağımsız, ticari olmayan bir projedir. Her kayıt aynı kurallarla hazırlanır; bu sayfa o kuralları açıkça yazar ki neye ne kadar güvenebileceğini bil.</p></header>
<section class="sec" id="hazirlayan"><h2>Kim hazırlıyor</h2><p>""" + BIO + """</p><p>""" + SOCIAL + """</p><p>Bitki Tabanı’ndaki her kayıt onun tarafından hazırlanır ve aşağıdaki kurallarla kaynaklara dayandırılır.</p></section>
<section class="sec"><h2>Hangi kaynakları kullanıyorum</h2><ol class="srclist">
<li><b>Resmî bitkisel ilaç değerlendirmeleri:</b> Avrupa İlaç Ajansı Bitkisel Ürünler Komitesi (EMA/HMPC) monografları ve ABD Ulusal Tamamlayıcı ve Bütünleştirici Sağlık Merkezi (NCCIH) özetleri.</li>
<li><b>Sistematik derlemeler ve klinik çalışmalar:</b> Cochrane derlemeleri ve PubMed’de dizinlenen hakemli dergiler.</li>
<li><b>Bitki adı ve sınıflandırma:</b> Kew Kraliyet Botanik Bahçeleri’nin Plants of the World Online (POWO) veri tabanı.</li>
<li><b>Koruma ve ticaret:</b> IUCN Kırmızı Liste ve CITES.</li>
<li><b>Yasal durum:</b> resmî mevzuat ve BM Uyuşturucu ve Suç Ofisi (UNODC) yayınları.</li>
<li><b>Geleneksel kullanım:</b> etnobotanik saha çalışmaları ve akademik kitaplar; Anadolu için Turhan Baytop’un <i>Türkiye’de Bitkiler ile Tedavi</i> kitabı temel başvuru kaynağıdır.</li>
</ol><p>Vikipedi, haber siteleri, aktar ve takviye satıcılarının sayfaları kaynak olarak kullanılmaz.</p></section>
<section class="sec"><h2>Kanıt düzeyleri</h2><dl class="meta wide">
<div><dt>Klinik</dt><dd>Kontrollü insan çalışmaları ya da resmî olarak onaylanmış bir ilaç kullanımı var.</dd></div>
<div><dt>Sınırlı</dt><dd>Küçük ya da az sayıda insan çalışması var; sonuçlar umut verici ama kesin değil.</dd></div>
<div><dt>Geleneksel</dt><dd>Kullanım kültürel olarak belgelenmiş, ama insan çalışması yok ya da çok az. Bu, bitkinin işe yaramadığı anlamına gelmez; yalnızca bilimin henüz bilmediğini söyler.</dd></div>
</dl></section>
<section class="sec"><h2>Güvenlik etiketleri</h2><dl class="meta wide">
<div><dt>Genelde güvenli</dt><dd>Ölçülü ve geleneksel biçimde kullanıldığında ciddi yan etki bildirilmemiş.</dd></div>
<div><dt>Dikkat</dt><dd>İlaç etkileşimi, doz ya da belirli gruplar (hamileler, çocuklar, kronik hastalar) için risk var.</dd></div>
<div><dt>Yüksek risk</dt><dd>Zehirli ya da ciddi yan etkileri olan bitkiler. Kültürel ve tarihî önemleri için yer alırlar; kullanım önerisi değildir.</dd></div>
</dl><p>Yasal durum, güvenlik etiketinden ayrı gösterilir: bir bitki yasak olmadan zehirli, zehirli olmadan yasak olabilir.</p></section>
<section class="sec"><h2>Geleneksel bilgiye yaklaşım</h2><p>Geleneksel kullanımlar, onları yaşatan toplulukların adıyla ve bağlamıyla anlatılır; “Amazon yerlileri” gibi genellemeler yerine Shipibo, Huichol gibi somut adlar kullanılır. Kutsal ve törensel kullanımlar bir tavsiye olarak değil, kültürel bir kayıt olarak yazılır.</p></section>
""" + GZ_HTML + """<section class="sec"><h2>Nasıl doğrulanıyor</h2><p>Her kayıt bir kişi tarafından hazırlanır""" + ('' if GZ_KISI else '; şu an bağımsız bir uzman ya da eczacı kayıtları gözden geçirmiyor') + """. Bu yüzden her iddia, sayfanın altında listelenen kaynağa bağlanır ve okuyan herkes onu kendisi kontrol edebilir. Tıbbi bilgiler resmî değerlendirmelerden (EMA, NCCIH) ve sistematik derlemelerden alınır; kaynağı olmayan sağlık iddiası yazılmaz. Bir eczacı ya da farmakognozi uzmanı gözden geçirmeye katılırsa adı bu sayfada ve ilgili kayıtlarda belirtilecek.</p></section>
<section class="sec" id="yapay-zeka"><h2>Yapay zekâ ve otomasyon</h2><p>Sitenin yazılımı, kaynak taramaları ve metin taslaklarının bir kısmı yapay zekâ yardımıyla (Anthropic’in Claude modeli) hazırlanıyor. Görseller Wikimedia Commons’tan kurallara göre otomatik seçiliyor; sosyal medya paylaşımları, sesli videolar ve “derdini yaz” anlam araması da otomatik çalışıyor.</p><p>Yapay zekâ kaynak yerine geçmez: her sağlık bilgisi bağlantısı verilen bir kaynağa dayanır, kanıt ve güvenlik etiketleri yukarıdaki kurallarla belirlenir ve içeriğin sorumluluğu Edanaz Tınmazlar’dadır. Otomatik süreçlerde gözden kaçan bir hata görürsen aşağıdaki adrese yaz; düzeltilir.</p></section>
<section class="sec"><h2>Güncelleme ve düzeltme</h2><p>Her sayfanın altında son gözden geçirme tarihi yazar. Bir hata görürsen ya da yöresel bir kullanım biliyorsan <a href="mailto:iletisim@bitkitabani.com">iletisim@bitkitabani.com</a> adresine yaz; düzeltmeler kaynağıyla birlikte kontrol edilip eklenir.</p></section>
<section class="sec"><h2>Bağımsızlık</h2><p>Bitki Tabanı ürün satmaz, reklam almaz, satış ortaklığı (affiliate) bağlantısı kullanmaz ve hiçbir şirketten destek almaz.</p></section>
"""
write('/yontem/', page('Yöntem: kayıtları nasıl hazırlıyorum | Bitki Tabanı', 'Bitki Tabanı hangi kaynakları kullanır, kanıt düzeylerini ve güvenlik etiketlerini nasıl belirler, hataları nasıl düzeltir.', '/yontem/', yt, 'about', narrow=True))

# ---------- rehberler: derde göre, hamilelik, ilaç etkileşimi, tarifler, karşılaştırmalar ----------
GUIDE_URLS = []
KAN_SIRA = {'klinik': 0, 'sinirli': 1, 'geleneksel': 2, 'yok': 3}
DISCL = '<aside class="disclaimer" role="note"><b>Tıbbi tavsiye değildir.</b> Bu sayfa katalogdaki kayıtları bir araya getirir ve bilimsel bilgiyi özetler; teşhis ya da tedavi önerisi değildir. Bir bitkiyi kullanmadan önce, özellikle ilaç kullanıyorsan, hamileysen, emziriyorsan ya da bir hastalığın varsa hekimine veya eczacına danış. Zehirlenme şüphesinde Ulusal Zehir Danışma Merkezi’ni (UZEM) <b>114</b> numaradan ara.</aside>'
UPD = f'<p class="updated">Son gözden geçirme: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time></p>'
def crumbs(*xs):
    out = '<a href="/">Ana sayfa</a>'
    for i, (u, t) in enumerate(xs):
        out += '<span>/</span>' + (f'<a href="{u}">{e(t)}</a>' if i < len(xs) - 1 else f'<span>{e(t)}</span>')
    return f'<nav class="crumbs" aria-label="Konum">{out}</nav>'
def crumb_ld(*xs):
    items = [("/", "Ana sayfa")] + list(xs)
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":t,"item":BASE+u} for i, (u, t) in enumerate(items)]}
def lds(*xs): return ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in xs)
def rb_item(p, note):
    thumb = f'<img src="/img/{p["id"]}-500.jpg" alt="" width="96" height="128" loading="lazy" decoding="async">' if p['id'] in IMG else '<span class="rb-ph"></span>'
    return f'''<article class="rb-item" id="{p["id"]}"><a class="rb-img" href="/{p["id"]}/" tabindex="-1" aria-hidden="true">{thumb}</a><div class="rb-txt"><h3><a href="/{p["id"]}/">{e(p["tr"])}</a> <i class="latin">{e(short_la(p))}</i></h3>
<p class="rb-meta"><span class="ev">{pips(p["kanit"])} Kanıt: {kan_txt(p)}</span><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span></p><p>{e(note)}</p><p class="rb-more"><a href="/{p["id"]}/">{e(p["tr"])}: güvenlik notu, etkileşimler ve kaynaklar →</a></p></div></article>'''
def gimage(ids):
    for i in ids:
        if i in IMG: return f'{BASE}/img/{i}-960.jpg'
    return None

LIVE_K = [k for k in KONULAR if sum(1 for pid, _ in k['bitkiler'] if pid in byId) >= 2]
LIVE_T = [t for t in TARIFLER if t['bitki'] in byId]
LIVE_C = [c for c in KARS if c['a'] in byId and c['b'] in byId]
def takvim_tabs(cur): return '<nav class="tabs" aria-label="Takvim">' + ''.join(f'<a href="{h}"' + (' aria-current="page"' if k == cur else '') + f'>{l}</a>' for h, l, k in [('/takvim/', 'Ritüeller', 'r'), ('/toplama-takvimi/', 'Doğada bu ay', 'd')]) + '</nav>'
def other_guides(cur):
    return '<ul class="otherlist">' + ''.join(f'<li><a href="/rehber/{k["slug"]}/">{e(k["kisa"])}</a></li>' for k in LIVE_K if k['slug'] != cur) + '<li><a href="/rehber/hamilelik-emzirme/">Hamilelik ve emzirme</a></li><li><a href="/rehber/ilac-etkilesimi/">İlaç etkileşimi</a></li></ul>'

# --- derde göre rehberler ---
for k in LIVE_K:
    ps = sorted([(byId[pid], n) for pid, n in k['bitkiler'] if pid in byId], key=lambda x: KAN_SIRA[x[0]['kanit']])
    ids = [p['id'] for p, _ in ps]
    trs = [t for t in LIVE_T if t['bitki'] in ids]
    cms = [c for c in LIVE_C if c['a'] in ids and c['b'] in ids]
    extra_links = ''
    if trs: extra_links += '<section class="sec"><h2>Nasıl hazırlanır?</h2><ul class="otherlist">' + ''.join(f'<li><a href="/tarif/{t["slug"]}/">{e(t["ad"])}</a></li>' for t in trs) + '</ul></section>'
    if cms: extra_links += '<section class="sec"><h2>Karşılaştır</h2><ul class="otherlist">' + ''.join(f'<li><a href="/karsilastirma/{c["a"]}-ve-{c["b"]}/">{e(c["baslik"])}</a></li>' for c in cms) + '</ul></section>'
    path = f'/rehber/{k["slug"]}/'
    _kn = k['kisa']; _ad = [p['tr'] for p, _ in ps]
    _guclu = [p['tr'] for p, _ in ps if p['kanit'] in ('klinik', 'sinirli')]
    _etk = [p['tr'] for p, _ in ps if p['id'] in ETK]
    _risk = [p['tr'] for p, _ in ps if p['guv'] in ('dikkat', 'yuksek')]
    _sss = [(f'{_kn} için hangi bitkiler kullanılır?', f'Bu rehberde {len(_ad)} bitki var: {", ".join(_ad)}.' + (f' Bilimsel çalışması olanlar (kanıt düzeyi klinik ya da sınırlı): {", ".join(_guclu)}.' if _guclu else ' Hiçbirinin güçlü bilimsel kanıtı yok; kullanımları geleneğe dayanıyor.')),
            ('Bu bitkileri ilaçla birlikte kullanabilir miyim?', (f'{", ".join(_etk)} için bilinen ilaç etkileşimleri var; ayrıntılar her bitkinin sayfasında. ' if _etk else 'Bu rehberdeki bitkiler için kayıtlarımızda önemli bir ilaç etkileşimi yok. ') + 'Düzenli ilaç kullanıyorsan bitkisel bir ürüne başlamadan önce eczacına ya da hekimine danış.'),
            ('Hamilelikte ve emzirirken kullanılabilir mi?', (f'Güvenlik etiketi “dikkat” ya da “yüksek risk” olanlar: {", ".join(_risk)}. ' if _risk else '') + 'Hamilelikte ve emzirirken bitkisel ürünlere hekime danışmadan başlama. Ayrıntılı liste Hamilelik ve emzirme rehberinde.')]
    _sss_html = '<section class="sec"><h2>Sık sorulanlar</h2><div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in _sss) + '</div></section>'

    body = f'''{crumbs(('/rehber/', 'Rehberler'), (path, k['kisa']))}
<article class="sheet">
<header class="page-head"><span class="eyebrow">Derde göre rehber · {len(ps)} bitki</span><h1>{e(k["baslik"])}</h1><p>{e(k["giris"])}</p></header>
{sharebar(k['baslik'], path)}
<section class="kisaca"><h2>Kısaca</h2><p>{e(k["ozet"])}</p></section>
<section class="sec"><h2>Bitkiler, kanıtı en güçlü olandan başlayarak</h2><div class="rb-list">{"".join(rb_item(p, n) for p, n in ps)}</div></section>
<aside class="warnbox" role="note"><b>Ne zaman hekime gitmeli?</b> {e(k["uyari"])}</aside>
{extra_links}
{_sss_html}
{abone('rehber:' + k['slug'])}
{DISCL}
<p class="updated">Hazırlayan: <a href="/yontem/#hazirlayan">Edanaz Tınmazlar</a> · Son gözden geçirme: <time datetime="{CONTENT_DATE}">{DATE_TXT}</time></p>
<section class="sec"><h2>Diğer rehberler</h2>{other_guides(k["slug"])}</section>
</article>'''
    ld = [{"@context":"https://schema.org","@type":"Article","headline":k['baslik'],"description":k['aciklama'],"inLanguage":"tr","url":BASE+path,"author":AUTHOR,"dateModified":CONTENT_DATE,
           "isPartOf":{"@type":"WebSite","name":"Bitki Tabanı","url":BASE+"/"},"image":[f'{BASE}/img/{i}-960.jpg' for i in ids if i in IMG][:3]},
          {"@context":"https://schema.org","@type":"ItemList","name":k['baslik'],"itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{BASE}/{p["id"]}/',"name":p['tr']} for i, (p, _) in enumerate(ps)]},
          crumb_ld(('/rehber/', 'Rehberler'), (path, k['kisa'])),
          {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in _sss]}]
    write(path, page(f'{k["baslik"]} | Bitki Tabanı', k['aciklama'], path, body, 'rehber', narrow=True, extra=lds(*ld), image=gimage(ids)))
    GUIDE_URLS.append(path)

# --- hamilelik ve emzirme ---
def _preg(p):
    return [s for s in re.split(r'(?<=[.!?])\s+', p['guvNot']) if re.search(r'[Hh]amile|[Gg]ebe|[Ee]mzir', s)]
preg = sorted([(p, ' '.join(_preg(p))) for p in P if _preg(p)], key=lambda x: x[0]['tr'])
hi = [p for p in P if p['guv'] == 'yuksek' and not _preg(p)]
path = '/rehber/hamilelik-emzirme/'
body = f'''{crumbs(('/rehber/', 'Rehberler'), (path, 'Hamilelik ve emzirme'))}
<article class="sheet">
<header class="page-head"><span class="eyebrow">Güvenlik rehberi · {len(preg)} bitki</span><h1>Hamilelikte ve emzirirken dikkat edilmesi gereken bitkiler</h1><p>Bitki çayları “doğal” olduğu için çoğu zaman zararsız sanılır. Oysa bazı bitkiler rahmi uyarabilir, bazılarının içerdiği maddeler bebeğe geçebilir; birçoğu için ise hamilelikte güvenli olduğunu gösteren yeterli veri yoktur. Aşağıda, katalogdaki kayıtların güvenlik notunda hamilelik ya da emzirme için ayrıca uyarı bulunan bitkiler var.</p></header>
<aside class="warnbox" role="note"><b>Önemli:</b> Bir bitkinin bu listede olmaması, hamilelikte güvenli olduğu anlamına gelmez. Hamilelikte ve emzirirken yemekteki miktarı aşan her bitkisel ürün, çay kürü ya da takviye için önce hekimine ya da eczacına danış.</aside>
<section class="sec"><h2>Güvenlik notunda hamilelik ya da emzirme uyarısı olan bitkiler</h2><div class="tablewrap"><table class="cmp etk"><thead><tr><th scope="col">Bitki</th><th scope="col">Uyarı</th><th scope="col">Güvenlik</th></tr></thead><tbody>
{"".join(f'<tr><th scope="row"><a href="/{p["id"]}/">{e(p["tr"])}</a></th><td>{e(t)}</td><td><span class="sf {p["guv"]}">{GUV[p["guv"]]}</span></td></tr>' for p, t in preg)}
</tbody></table></div></section>
{('<section class="sec"><h2>Ayrıca: yüksek riskli bitkiler</h2><p>Bu bitkiler zehirli ya da ciddi yan etkili oldukları için hamilelikte de, hamilelik dışında da kullanım önerisi değildir; katalogda kültürel ve tarihî önemleri için yer alırlar.</p><ul class="otherlist">' + ''.join(f'<li><a href="/{p["id"]}/">{e(p["tr"])}</a></li>' for p in sorted(hi, key=lambda p: p["tr"])) + '</ul></section>') if hi else ''}
<section class="sec"><h2>Bulantı için</h2><p>Hamilelik bulantısında en çok araştırılan bitki zencefil; küçük çalışmalar olumlu sonuç veriyor. Bunu da kullanmadan önce hekimine danış. <a href="/rehber/bulanti/">Bulantı rehberine bak →</a></p></section>
{DISCL}
{UPD}
<section class="sec"><h2>Diğer rehberler</h2>{other_guides("")}</section>
</article>'''
write(path, page('Hamilelikte ve emzirirken dikkat edilmesi gereken bitkiler | Bitki Tabanı', f'Hamilelikte ve emzirirken kullanılmaması ya da dikkatle kullanılması gereken {len(preg)} şifalı bitki ve uyarıları: adaçayı, rezene, sinameki, hayıt ve diğerleri.', path, body, 'gebe', narrow=True,
      extra=lds({"@context":"https://schema.org","@type":"Article","headline":"Hamilelikte ve emzirirken dikkat edilmesi gereken bitkiler","inLanguage":"tr","url":BASE+path,"author":AUTHOR,"dateModified":CONTENT_DATE}, crumb_ld(('/rehber/', 'Rehberler'), (path, 'Hamilelik ve emzirme')))))
GUIDE_URLS.append(path)

# --- ilaç etkileşimi aracı ---
ILAC = [('kan', 'Kan sulandırıcılar (varfarin, aspirin vb.)', ['kan sulandırıcı', 'varfarin', 'kan pulcuğu']),
        ('seker', 'Şeker ilaçları ve insülin', ['şeker']),
        ('tansiyon', 'Tansiyon ilaçları', ['tansiyon', 'beta bloker', 'kalsiyum kanal', 'nitrat']),
        ('kalp', 'Kalp ilaçları (digoksin, kalp ritmi ilaçları)', ['digoksin', 'kalp ritmi', 'kalp glikozit', 'qt süresini', 'kalp ilaç']),
        ('antidep', 'Antidepresanlar ve migren ilaçları (triptanlar)', ['antidepresan', 'mao', 'ssri', 'triptan', 'serotonin']),
        ('uyku', 'Uyku ilaçları, yatıştırıcılar ve alkol', ['yatıştırıcı', 'uyku ilaç', 'sakinleştirici', 'opioid', 'alkol']),
        ('hormon', 'Doğum kontrol hapı ve hormon tedavisi', ['doğum kontrol', 'hormon']),
        ('bagisiklik', 'Bağışıklığı baskılayan ve organ nakli ilaçları', ['bağışıklı', 'organ nakli', 'siklosporin']),
        ('diuretik', 'İdrar söktürücüler (diüretikler)', ['idrar söktürücü', 'diüretik']),
        ('lityum', 'Lityum', ['lityum']),
        ('nobet', 'Nöbet (epilepsi) ilaçları', ['nöbet']),
        ('karaciger', 'Karaciğerde yıkılan ya da karaciğere yük getiren ilaçlar', ['karaciğer', 'cyp3a4', 'p-glikoprotein', 'parasetamol']),
        ('kortizon', 'Kortizon ilaçları', ['kortizon', 'kortikosteroid']),
        ('uyarici', 'Uyarıcılar ve kafein', ['uyarıcı', 'kafein']),
        ('antibiyotik', 'Antibiyotikler', ['antibiyotik', 'siprofloksasin']),
        ('kanser', 'Kanser ve HIV ilaçları', ['kanser', 'hiv']),
        ('demir', 'Demir takviyeleri', ['demir takviye']),
        ('mide', 'Mide asidi düşürücüler', ['mide asidi']),
        ('tum', 'Ağızdan alınan bütün ilaçlar (emilimi etkileyenler)', ['ağızdan alınan'])]
def _low(s): return s.replace('I', 'ı').replace('İ', 'i').lower()
etk_by = {c: [] for c, _, _ in ILAC}
for pid, rows in ETK.items():
    if pid not in byId: continue
    for g, w in rows:
        for c, _, keys in ILAC:
            if any(kw in _low(g).replace('göz tansiyonu', 'glokom') for kw in keys):
                if not any(x[0] == pid for x in etk_by[c]): etk_by[c].append((pid, g, w))
sel = ''.join(f'<option value="{c}">{e(ad)} ({len(etk_by[c])})</option>' for c, ad, _ in ILAC if etk_by[c])
secs = ''
for c, ad, _ in ILAC:
    if not etk_by[c]: continue
    rows_ = ''.join(f'<tr><th scope="row"><a href="/{pid}/">{e(byId[pid]["tr"])}</a></th><td>{e(w)}</td></tr>' for pid, g, w in sorted(etk_by[c], key=lambda x: byId[x[0]]['tr']))
    secs += f'<section class="sec etkgrp" id="{c}" data-c="{c}"><h2>{e(ad)}</h2><div class="tablewrap"><table class="cmp etk"><thead><tr><th scope="col">Bitki</th><th scope="col">Olası etkileşim</th></tr></thead><tbody>{rows_}</tbody></table></div></section>'
path = '/rehber/ilac-etkilesimi/'
nplants = len({pid for v in etk_by.values() for pid, _, _ in v})
body = f'''{crumbs(('/rehber/', 'Rehberler'), (path, 'İlaç etkileşimi'))}
<article class="sheet">
<header class="page-head"><span class="eyebrow">Güvenlik aracı · {nplants} bitki</span><h1>Bitki ve ilaç etkileşimi: kullandığın ilaçla hangi bitkiler sorun çıkarabilir?</h1><p>Bitkiler de ilaçlar gibi etken maddeler içerir. Bazıları ilacının etkisini artırır, bazıları azaltır, bazıları da aynı yan etkiyi büyütür. Kullandığın ilaç grubunu seç; katalogda o grupla etkileşimi bildirilen bitkileri gör.</p></header>
<form class="etkform" id="etkform" onsubmit="return false"><label for="etksel" class="eyebrow">İlaç grubu</label><select id="etksel"><option value="">Bütün gruplar</option>{sel}</select><input id="etkq" type="search" placeholder="ya da bitki adı yaz" aria-label="Bitki adıyla süz"><p class="muted-s" id="etkmsg" role="status"></p></form>
<aside class="warnbox" role="note"><b>Bu liste eksiksiz değildir.</b> Yalnızca katalogdaki kayıtlarda bildirilen etkileşimleri içerir; bir bitkinin listede olmaması ilacınla güvenle kullanılabileceği anlamına gelmez. Düzenli ilaç kullanıyorsan, bir bitkisel ürüne başlamadan önce eczacına sor. İlacını kendi başına bırakma ya da dozunu değiştirme.</aside>
<div id="etkres">{secs}</div>
<section class="sec"><h2>Özellikle dikkat</h2><p><a href="/kantaron/">Sarı kantaron</a>, doğum kontrol hapı, kan sulandırıcılar, bazı kalp ve organ nakli ilaçları dahil pek çok ilacın etkisini azaltan, en iyi bilinen bitkidir. Antidepresanlarla birlikte kullanıldığında serotonin sendromuna yol açabilir.</p></section>
{DISCL}
{UPD}
<section class="sec"><h2>Diğer rehberler</h2>{other_guides("")}</section>
</article>'''
write(path, page('Bitki ve ilaç etkileşimi: hangi bitki hangi ilaçla sorun çıkarır? | Bitki Tabanı', f'Kan sulandırıcı, tansiyon, şeker, antidepresan ve doğum kontrol hapı gibi ilaçlarla etkileşen {nplants} şifalı bitki. İlaç grubunu seç, etkileşimleri gör.', path, body, 'etk', '<script src="/assets/etkilesim.js" defer></script>', narrow=True,
      extra=lds({"@context":"https://schema.org","@type":"Article","headline":"Bitki ve ilaç etkileşimi","inLanguage":"tr","url":BASE+path,"author":AUTHOR,"dateModified":CONTENT_DATE}, crumb_ld(('/rehber/', 'Rehberler'), (path, 'İlaç etkileşimi')))))
GUIDE_URLS.append(path)

# --- bitki bulucu: derde göre, hamilelik ve ilaç durumuna göre süzen sihirbaz (tamamen tarayıcıda) ---
_tarif_of = {}
for t in LIVE_T: _tarif_of.setdefault(t['bitki'], t['slug'])
_preg_ids = {p['id'] for p, _ in preg}
_BB = {'k': [], 'g': [[c, ad] for c, ad, _ in ILAC if etk_by[c]], 'gk': {c: keys for c, _, keys in ILAC}, 'e': {c: sorted({pid for pid, _, _ in etk_by[c]}) for c, _, _ in ILAC if etk_by[c]}, 'p': {}, 'K': {k: [v['n'], v['ad']] for k, v in KANIT.items()}, 'G': {k: (v['ad'] if isinstance(v, dict) else v) for k, v in GUV.items()}}
for k in LIVE_K:
    ids = [(x, n) for x, n in k['bitkiler'] if x in byId]
    _BB['k'].append({'s': k['slug'], 'a': k['kisa'], 'i': ico(k['slug'], 'ico-b'), 'b': [x for x, _ in ids], 'n': {x: n for x, n in ids}, 'u': k['uyari']})
    for x, _ in ids:
        q = byId[x]
        _BB['p'][x] = {'t': q['tr'], 'l': short_la(q), 'k': q['kanit'], 'g': q['guv'], 'h': x in _preg_ids, 'y': bool(YASAL.get(x)), 'r': _tarif_of.get(x), 'm': x in IMG}
path = '/bitki-bul/'
body = f'''{crumbs((path, 'Bitki bulucu'))}
<article class="sheet">
<header class="page-head"><span class="eyebrow">Üç soruda</span><h1>Bana uygun bitki hangisi?</h1><p>Derdini seç, birkaç soruyu yanıtla; katalogdan sana uygun bitkileri, kanıtı en güçlü olandan başlayarak listeleyelim. Hamileysen ya da ilaç kullanıyorsan riskli olanlar kendiliğinden elenir.</p></header>
<div id="bb" class="bb">
 <section class="bbstep" data-s="1"><h2><span class="bbn">1</span> Derdin ne?</h2><div class="icongrid bbk"></div></section>
 <section class="bbstep" data-s="2" hidden><h2><span class="bbn">2</span> Hamile misin ya da emziriyor musun?</h2><div class="bbopts"><button type="button" class="chip" data-h="0">Hayır</button><button type="button" class="chip" data-h="1">Evet</button></div></section>
 <section class="bbstep" data-s="3" hidden><h2><span class="bbn">3</span> Düzenli kullandığın bir ilaç var mı?</h2><p class="muted-s">Birden fazla seçebilirsin.</p><div class="bbopts bbg"><button type="button" class="chip" data-g="yok">İlaç kullanmıyorum</button></div><p><button type="button" class="cta bbgo">Sonuçları göster →</button></p></section>
 <section class="bbstep" data-s="4" hidden><h2>Bu dert için öne çıkan bitkiler</h2><div class="bbres"></div><p><button type="button" class="linkbtn bbagain">Baştan başla</button></p></section>
</div>
<noscript><p>Bu araç JavaScript ile çalışır. <a href="/rehber/">Derde göre bitkiler</a> sayfasından da aynı listelere ulaşabilirsin.</p></noscript>
{DISCL}
<section class="sec"><h2>Diğer rehberler</h2>{other_guides("")}</section>
</article>
<script id="bbdata" type="application/json">{json.dumps(_BB, ensure_ascii=False).replace("</", "<\\/")}</script>'''
write(path, page('Bana uygun bitki hangisi? Derde göre bitki bulucu | Bitki Tabanı', 'Derdini seç, hamilelik ve ilaç durumunu belirt: katalogdan sana uygun şifalı bitkiler, kanıtı en güçlü olandan başlayarak. Riskli olanlar kendiliğinden elenir.', path, body, 'bul', scripts='<script src="/assets/bitkibul.js" defer></script>',
      extra=lds({"@context":"https://schema.org","@type":"WebPage","name":"Bitki bulucu","inLanguage":"tr","url":BASE+path,"author":AUTHOR,"dateModified":CONTENT_DATE})))
GUIDE_URLS.append(path)

# --- tarifler ---
def iso_min(m): return f'PT{m}M'
for t in LIVE_T:
    p = byId[t['bitki']]; path = f'/tarif/{t["slug"]}/'
    others = [x for x in LIVE_T if x is not t][:8]
    img = f'<figure class="tarif-img">{ph(p, 960)}<figcaption>{credit(p)}</figcaption></figure>' if p['id'] in IMG else ''
    body = f'''{crumbs(('/tarif/', 'Tarifler'), (path, t['ad']))}
<article class="sheet">
<header class="page-head"><span class="eyebrow">Tarif · {e(p["tr"])}</span><h1>{e(t["ad"])}</h1><p>{e(t["kisa"])}</p>
<p class="tarif-meta"><span>Hazırlık: <b>{t["hazirlik"]} dk</b></span><span>Toplam: <b>{t["toplam"]} dk</b></span><span>Verim: <b>{e(t["verim"])}</b></span></p></header>
{sharebar(t['ad'] + ' nasıl yapılır?', path)}
{img}
<section class="sec"><h2>Malzemeler</h2><ul class="malz">{"".join(f'<li>{e(m)}</li>' for m in t["malzeme"])}</ul></section>
<section class="sec"><h2>Hazırlanışı</h2><ol class="adim">{"".join(f'<li>{e(a)}</li>' for a in t["adim"])}</ol></section>
<p class="fact">{e(t["ipucu"])}</p>
<aside class="warnbox" role="note"><b>Kimler dikkat etmeli?</b> {e(p["guvNot"])}{(' <a href="/' + p["id"] + '/">İlaç etkileşimleri bitkinin sayfasında.</a>') if p["id"] in ETK else ''}</aside>
<p><a class="cta" href="/{p["id"]}/">{e(p["tr"])}: bilim ne diyor, ilaç etkileşimleri ve kaynaklar →</a></p>
{abone('tarif:' + t['slug'])}
{DISCL}
<section class="sec"><h2>Diğer tarifler</h2><ul class="otherlist">{"".join(f'<li><a href="/tarif/{x["slug"]}/">{e(x["ad"])}</a></li>' for x in others)}</ul><p><a class="cta" href="/tarif/">Bütün tarifler →</a></p></section>
</article>'''
    ld = {"@context":"https://schema.org","@type":"Recipe","name":t['ad'],"description":t['kisa'],"inLanguage":"tr","author":AUTHOR,"datePublished":CONTENT_DATE,
          "prepTime":iso_min(t['hazirlik']),"totalTime":iso_min(t['toplam']),"recipeYield":t['verim'],"recipeCategory":"İçecek" if 'corba' not in t['slug'] else 'Çorba',"recipeCuisine":"Türk",
          "keywords":f'{p["tr"]}, {short_la(p)}, bitki çayı',"recipeIngredient":t['malzeme'],"recipeInstructions":[{"@type":"HowToStep","text":a} for a in t['adim']]}
    if p['id'] in IMG: ld['image'] = [f'{BASE}/img/{p["id"]}-960.jpg']
    write(path, page(f'{t["ad"]} nasıl yapılır? | Bitki Tabanı', (t['kisa'] + f' Malzemeler, ölçüler ve kimlerin dikkat etmesi gerektiği.')[:158], path, body, 'tarif', narrow=True,
          extra=lds(ld, crumb_ld(('/tarif/', 'Tarifler'), (path, t['ad']))), image=gimage([p['id']])))
    GUIDE_URLS.append(path)
tl = ''.join(f'<a class="card" href="/tarif/{t["slug"]}/">{ph(byId[t["bitki"]], 500)}<div class="body"><h2>{e(t["ad"])}</h2><p class="muted-s">{e(t["kisa"])}</p><div class="foot"><span class="ev">{t["toplam"]} dk · {e(t["verim"])}</span></div></div></a>' for t in LIVE_T)
write('/tarif/', page('Bitki çayı tarifleri: ölçüleri ve demleme süreleriyle | Bitki Tabanı', f'Ihlamur, papatya, zencefil, kuşburnu ve {len(LIVE_T)-4} bitki çayı ve tarifi: ölçüler, demleme süreleri ve kimlerin dikkat etmesi gerektiği.', '/tarif/',
      f'{crumbs(("/tarif/", "Tarifler"))}<header class="page-head"><span class="eyebrow">{len(LIVE_T)} tarif</span><h1>Bitki çayları ve tarifler</h1><p>Katalogdaki bitkilerin geleneksel hazırlanışları: ölçüler, demleme süreleri ve her tarifin altında kimlerin dikkat etmesi gerektiği.</p></header><div class="grid">{tl}</div>{DISCL}', 'tarif',
      extra=lds(crumb_ld(('/tarif/', 'Tarifler')))))
GUIDE_URLS.append('/tarif/')

# --- karşılaştırmalar ---
for c in LIVE_C:
    a, b = byId[c['a']], byId[c['b']]; path = f'/karsilastirma/{c["a"]}-ve-{c["b"]}/'
    ets = ''
    for q in (a, b):
        if q['id'] in ETK: ets += f'<p><b>{e(q["tr"])}:</b> ' + '; '.join(f'{e(g)} ({e(w.rstrip("."))})' for g, w in ETK[q['id']]) + '.</p>'
    body = f'''{crumbs(('/rehber/', 'Rehberler'), (path, c['baslik']))}
<article class="sheet">
<header class="page-head"><span class="eyebrow">Karşılaştırma</span><h1>{e(c["baslik"])}</h1><p>{e(c["giris"])}</p></header>
<div class="vs">{''.join(f'<a href="/{q["id"]}/" class="vs-p">{ph(q, 500)}<b>{e(q["tr"])}</b><i>{e(short_la(q))}</i></a>' for q in (a, b))}</div>
{sharebar(c['baslik'], path)}
<section class="sec"><h2>Yan yana</h2>{cmp_rows([a, b])}</section>
<section class="sec"><h2>Başlıca farklar</h2><ul class="farklar">{"".join(f'<li>{e(x)}</li>' for x in c["fark"])}</ul></section>
<section class="kisaca"><h2>Hangisi, ne zaman?</h2><p>{e(c["sonuc"])}</p></section>
<section class="sec"><h2>Ayrıntılar</h2><p>Bilimsel kanıtın tamamı, güvenlik notları, ilaç etkileşimleri ve kaynaklar her bitkinin kendi sayfasında:</p><p class="brlinks">{"".join(f'<a class="cta" href="/{q["id"]}/">{e(q["tr"])} →</a> ' for q in (a, b))}</p></section>
{DISCL}
{UPD}
<section class="sec"><h2>Diğer karşılaştırmalar</h2><ul class="otherlist">{"".join(f'<li><a href="/karsilastirma/{x["a"]}-ve-{x["b"]}/">{e(x["baslik"])}</a></li>' for x in LIVE_C if x is not c)}</ul></section>
</article>'''
    desc = f'{a["tr"]} ve {b["tr"]} arasındaki farklar: bilimsel kanıt, kullanım, güvenlik ve ilaç etkileşimleri yan yana.'
    write(path, page(f'{c["baslik"]} | Bitki Tabanı', desc, path, body, 'kars', narrow=True,
          extra=lds({"@context":"https://schema.org","@type":"Article","headline":c['baslik'],"description":desc,"inLanguage":"tr","url":BASE+path,"author":AUTHOR,"dateModified":CONTENT_DATE,
                     "about":[{"@type":"Taxon","name":short_la(q),"alternateName":q['tr']} for q in (a, b)],"image":[f'{BASE}/img/{q["id"]}-960.jpg' for q in (a, b) if q['id'] in IMG]},
                    crumb_ld(('/rehber/', 'Rehberler'), (path, c['baslik']))), image=gimage([a['id'], b['id']])))
    GUIDE_URLS.append(path)

kl = ''.join(f'<li><a href="/karsilastirma/{c["a"]}-ve-{c["b"]}/"><b>{e(c["baslik"])}</b></a><span>{e(c["sonuc"])}</span></li>' for c in LIVE_C)
write('/karsilastirma/', page('Bitki karşılaştırmaları: hangisi, ne zaman? | Bitki Tabanı', 'Zencefil mi zerdeçal mı, adaçayı mı dağ çayı mı? Sık karıştırılan şifalı bitkiler kanıt, kullanım ve güvenlik açısından yan yana.', '/karsilastirma/',
      f'{crumbs(("/karsilastirma/", "Karşılaştırmalar"))}<header class="page-head"><span class="eyebrow">{len(LIVE_C)} karşılaştırma</span><h1>Hangisi, ne zaman?</h1><p>Sık karıştırılan ya da aynı dert için kullanılan bitkiler yan yana: kanıt düzeyi, güvenlik ve başlıca farklar.</p></header><section class="sec"><ul class="guidelist">{kl}</ul></section>{DISCL}', 'kars', narrow=True, extra=lds(crumb_ld(('/karsilastirma/', 'Karşılaştırmalar')))))
GUIDE_URLS.append('/karsilastirma/')

# --- semboller: el çizimi tek renk motifler ---
import random as _rnd
def motif_svg(mo, size=None, cls='motif-svg'):
    r = _rnd.Random(mo['slug'])
    def wob(pts, amp):
        out = []
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(2, int(math.hypot(x1 - x0, y1 - y0) / 3))
            for k in range(n):
                t = k / n; out.append((x0 + (x1 - x0) * t + r.uniform(-amp, amp), y0 + (y1 - y0) * t + r.uniform(-amp, amp)))
        out.append((pts[-1][0] + r.uniform(-amp, amp), pts[-1][1] + r.uniform(-amp, amp)))
        return out
    def path(pts):
        if len(pts) < 2: return ''
        d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
        for (ax, ay), (bx, by) in zip(pts[1:], pts[2:] + [pts[-1]]):
            d += f' Q{ax:.1f} {ay:.1f} {(ax + bx) / 2:.1f} {(ay + by) / 2:.1f}'
        return d
    body = ''.join(f'<path d="{path(wob(p, .45))}" fill="currentColor" stroke="none" opacity=".9"/>' for p in mo.get('dolu', []))
    body += ''.join(f'<path d="{path(wob(p, .55))}"/>' for p in mo['cizim'])
    body += ''.join(f'<path d="{path(wob(p, .9))}" stroke-width="1.1" opacity=".55"/>' for p in mo['cizim'])
    sz = f' width="{size}" height="{size}"' if size else ''
    return f'<svg class="{cls}" viewBox="-4 -4 108 108"{sz} fill="none" stroke="currentColor" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="{e(mo["ad"])} motifi çizimi">{body}</svg>'
import math
def _msrc(t):
    return re.sub(r'\[(\d+)\]', lambda m: f'<sup><a href="#k{m.group(1)}">[{m.group(1)}]</a></sup>', e(t))
for mo in MOTIFLER:
    path = f'/semboller/{mo["slug"]}/'
    bit = ''.join(f'<li><a href="/{x}/"><b>{e(byId[x]["tr"])}</b></a>: {e(n)}</li>' for x, n in mo['bitkiler'] if x in byId)
    same = [o for o in MOTIFLER if o['tema'] == mo['tema'] and o is not mo]
    kay = '<ol class="refs">' + ''.join((f'<li id="k{j}"><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' if u else f'<li id="k{j}"><cite>{e(t)}</cite></li>') for j, (t, u) in enumerate(mo['kaynaklar'], 1)) + '</ol>'
    body = f'''{crumbs(('/semboller/', 'Semboller'), (path, mo['ad']))}
<article class="sheet">
<header class="motif-head"><div class="motif-art">{motif_svg(mo)}</div><div><span class="eyebrow">{e(mo["bolge"])} · {e(TEMALAR[mo["tema"]])}</span><h1>{e(mo["ad"])}</h1><p class="lede">{e(mo["kisa"])}</p></div></header>
{sharebar(mo['ad'] + ' motifi: ' + mo['kisa'], path)}
<section class="sec"><h2>Ne anlatır?</h2><p>{_msrc(mo["anlam"])}</p></section>
{('<section class="sec"><h2>Bağlantılı bitkiler</h2><ul class="otherlist">' + bit + '</ul></section>') if bit else ''}
{('<section class="sec"><h2>Aynı temadan</h2><div class="motif-mini">' + ''.join(f'<a href="/semboller/{o["slug"]}/">{motif_svg(o)}<span>{e(o["ad"])}</span></a>' for o in same) + '</div></section>') if same else ''}
<section class="sec"><h2>Kaynaklar</h2>{kay}</section>
<aside class="disclaimer" role="note"><b>Kültürel kayıt.</b> Motiflerin anlamları kaynaklarda yazdığı biçimde verilmiştir; aynı motif farklı yörelerde farklı yorumlanabilir.</aside>
<p class="updated">Çizim: Bitki Tabanı, geleneksel motiften yorumlanmıştır.</p>
</article>'''
    write(path, page(f'{mo["ad"]} motifi: anlamı ve kökeni | Bitki Tabanı', f'{mo["ad"]} ({mo["bolge"]}): {mo["kisa"]} Anlamı, kaynakları ve bağlantılı bitkiler.'[:158], path, body, 'sembol', narrow=True,
          extra=lds({"@context":"https://schema.org","@type":"Article","headline":mo['ad'] + ' motifi',"description":mo['kisa'],"inLanguage":"tr","url":BASE+path,"author":AUTHOR,"citation":[t for t, u in mo['kaynaklar']]}, crumb_ld(('/semboller/', 'Semboller'), (path, mo['ad'])))))
    GUIDE_URLS.append(path)
_chips = '<button type="button" class="chip" data-t="" aria-pressed="true">Hepsi</button>' + ''.join(f'<button type="button" class="chip" data-t="{k}" aria-pressed="false">{e(v)}</button>' for k, v in TEMALAR.items())
_sc = ''.join(f'<a class="motifcard" data-t="{mo["tema"]}" href="/semboller/{mo["slug"]}/">{motif_svg(mo)}<b>{e(mo["ad"])}</b><span class="muted-s">{e(mo["bolge"])}</span></a>' for mo in MOTIFLER)
write('/semboller/', page('Semboller: kilim motiflerinden chakana’ya, anlamları ve kökenleri | Bitki Tabanı', 'Göz, pıtrak, elibelinde, koçboynuzu, hayat ağacı, chakana, kené: Anadolu’dan And’lara geleneksel motifler, anlamları, kaynakları ve bağlantılı bitkiler.', '/semboller/',
      f'''{crumbs(('/semboller/', 'Semboller'))}<header class="page-head"><span class="eyebrow">Semboller · {len(MOTIFLER)} motif</span><h1>Semboller</h1><p>Kilimlerdeki nazar gözünden And’ların basamaklı haçına, kuşaklar boyunca dokunan, boyanan ve çizilen motifler. Her birini el çizimiyle yeniden çizdik; anlamlarını kaynaklarıyla ve bağlantılı oldukları bitkilerle birlikte anlatıyoruz.</p></header>
<div class="chips motif-filtre" role="group" aria-label="Temaya göre">{_chips}</div>
<div class="motifgrid">{_sc}</div>
<p><a class="cta" href="/yazilar/">Şamanizm, ritüel bitkiler ve kadim bilgi üzerine yazılar →</a></p>
<script>(function(){{var B=document.querySelectorAll('.motif-filtre .chip');B.forEach(function(b){{b.addEventListener('click',function(){{var t=b.dataset.t;B.forEach(function(x){{x.setAttribute('aria-pressed',x===b?'true':'false')}});document.querySelectorAll('.motifcard').forEach(function(c){{c.hidden=!!t&&c.dataset.t!==t}})}})}})}})();</script>''', 'sembol', narrow=True, extra=lds(crumb_ld(('/semboller/', 'Semboller')))))
GUIDE_URLS.insert(0, '/semboller/')
_redir = ''.join(f'/semboller/{old}/ /semboller/{news[0]}/ 301\n' for old, news in MOTIF_ESKI.items() if old != news[0])
def _rel_motifs(slugs):
    out = []
    for sl in slugs:
        for m in MOTIF_ESKI.get(sl, [sl]):
            mo = next((x for x in MOTIFLER if x['slug'] == m), None)
            if mo and mo not in out: out.append(mo)
    return out
def _motif_list(slugs):
    ms = _rel_motifs(slugs)
    return ''.join(f'<li><a href="/semboller/{mo["slug"]}/">{e(mo["ad"])}</a></li>' for mo in ms)

# --- kavram yazıları ---
def _trlow(t): return t.replace('I', 'ı').replace('İ', 'i').lower()
def _ylink(m):
    pid = m.group(1)
    return f'<a href="/{pid}/">{e(_trlow(byId[pid]["tr"]))}</a>' if pid in byId else pid
def _yp(t):
    t = e(t)
    t = re.sub(r'\{([a-z0-9]+)\}', _ylink, t)
    return re.sub(r'\[(\d+)\]', lambda m: f'<sup><a href="#k{m.group(1)}">[{m.group(1)}]</a></sup>', t)
for y in YAZILAR:
    path = f'/yazilar/{y["slug"]}/'
    secs = ''.join(f'<section class="sec"><h2>{e(h)}</h2>' + ''.join(f'<p>{_yp(p)}</p>' for p in ps) + '</section>' for h, ps in y['bolumler'])
    kay = '<ol class="refs">' + ''.join((f'<li id="k{i}"><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' if u else f'<li id="k{i}"><cite>{e(t)}</cite></li>') for i, (t, u) in enumerate(y['kaynaklar'], 1)) + '</ol>'
    bit = ''.join(f'<a class="chip" href="/{x}/">{"".join(dot(r) for r in byId[x]["bolge"])}{e(byId[x]["tr"])}</a>' for x in y['bitkiler'] if x in byId)
    sem = _motif_list(y['semboller'])
    body = f'''{crumbs(('/yazilar/', 'Yazılar'), (path, y['baslik']))}
<article class="sheet yazi">
<header class="page-head"><span class="eyebrow">Yazı · {tr_date(datetime.date.fromisoformat(y["tarih"])).rsplit(",", 1)[0]}</span><h1>{e(y["baslik"])}</h1><p class="lede">{e(y["giris"])}</p></header>
{sharebar(y['baslik'], path)}
{secs}
{('<section class="sec"><h2>Yazıda geçen bitkiler</h2><div class="related">' + bit + '</div></section>') if bit else ''}
{('<section class="sec"><h2>İlgili semboller</h2><ul class="otherlist">' + sem + '</ul></section>') if sem else ''}
<section class="sec"><h2>Kaynaklar</h2>{kay}</section>
<p class="updated">Yazan: <a href="/yontem/#hazirlayan">Edanaz Tınmazlar</a> · <time datetime="{y["tarih"]}">{tr_date(datetime.date.fromisoformat(y["tarih"])).rsplit(",", 1)[0]}</time></p>
{abone('yazi:' + y['slug'])}
</article>'''
    write(path, page(f'{y["baslik"]} | Bitki Tabanı', y['aciklama'], path, body, 'yazi', narrow=True,
          extra=lds({"@context":"https://schema.org","@type":"Article","headline":y['baslik'],"description":y['aciklama'],"inLanguage":"tr","url":BASE+path,"author":AUTHOR,"datePublished":y['tarih'],"dateModified":y['tarih'],"citation":[t for t, u in y['kaynaklar']]}, crumb_ld(('/yazilar/', 'Yazılar'), (path, y['baslik']))),
          image=next((f'{BASE}/img/{x}-960.jpg' for x in y['bitkiler'] if x in IMG), None)))
    GUIDE_URLS.append(path)
_yl = ''.join(f'<li><a href="/yazilar/{y["slug"]}/"><b>{e(y["baslik"])}</b></a><span>{e(y["aciklama"])}</span></li>' for y in sorted(YAZILAR, key=lambda y: y['tarih'], reverse=True))
write('/yazilar/', page('Yazılar: şamanizm, ritüel bitkiler ve kadim bilgi | Bitki Tabanı', 'Şamanizm, animizm, tütsü gelenekleri ve bitkilerle kurulan kadim ilişki üzerine kaynaklı yazılar.', '/yazilar/',
      f'''{crumbs(('/yazilar/', 'Yazılar'))}<header class="page-head"><span class="eyebrow">Yazılar</span><h1>Bitkiler, ritüeller ve kadim bilgi</h1><p>Şamanizmden tütsü geleneklerine, kutsal ağaçlardan bitki “öğretmenlere”: bitkilerle kurulan kadim ilişki üzerine kaynaklı yazılar.</p></header><section class="sec"><ul class="guidelist">{_yl}</ul></section>''', 'yazi', narrow=True))
GUIDE_URLS.insert(0, '/yazilar/')

# --- günün kavramı ---
def kav_plant(k):
    p = byId[k['bitki']]
    return f'''<a class="kavbitki" href="/{p["id"]}/">{ph(p, 500)}<span><span class="eyebrow">Kavramın bitkisi</span><b>{e(p["tr"])}</b><i>{e(short_la(p))}</i><span class="muted-s">{e(p["ilginc"])}</span><span class="cta small">Bitkinin sayfası →</span></span></a>'''
for i, k in enumerate(KAV):
    path = f'/kavram/{k["slug"]}/'
    d = datetime.date.fromisoformat(k['yayin'])
    secs = ''.join(f'<p>{_yp(p)}</p>' for p in k['metin'])
    kay = '<ol class="refs">' + ''.join((f'<li id="k{j}"><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' if u else f'<li id="k{j}"><cite>{e(t)}</cite></li>') for j, (t, u) in enumerate(k['kaynaklar'], 1)) + '</ol>'
    bit = ''.join(f'<a class="chip" href="/{x}/">{"".join(dot(r) for r in byId[x]["bolge"])}{e(byId[x]["tr"])}</a>' for x in k['bitkiler'] if x in byId and x != k['bitki'])
    sem = _motif_list(k['semboller'])
    yz = ''.join(f'<li><a href="/yazilar/{y["slug"]}/">{e(y["baslik"])}</a></li>' for y in YAZILAR if y['slug'] in k['yazilar'])
    prev_, next_ = (KAV[i - 1] if i else None), (KAV[i + 1] if i + 1 < len(KAV) else None)
    body = f'''{crumbs(('/kavram/', 'Kavramlar'), (path, k['ad']))}
<article class="sheet yazi">
<header class="page-head"><span class="eyebrow">Günün kavramı · {tr_date(d).rsplit(",", 1)[0]}</span><h1>{e(k["ad"])}</h1><p class="lede">{e(k["kisa"])}</p></header>
{sharebar(k['ad'] + ': ' + k['kisa'], path)}
{kav_plant(k)}
<section class="sec">{secs}</section>
{('<section class="sec"><h2>İlgili bitkiler</h2><div class="related">' + bit + '</div></section>') if bit else ''}
{('<section class="sec"><h2>İlgili semboller</h2><ul class="otherlist">' + sem + '</ul></section>') if sem else ''}
{('<section class="sec"><h2>Daha fazlası</h2><ul class="otherlist">' + yz + '</ul></section>') if yz else ''}
<section class="sec"><h2>Kaynaklar</h2>{kay}</section>
<aside class="disclaimer" role="note"><b>Kültürel kayıt.</b> Ritüel ve inançlar, onları yaşatan toplulukların mirası olarak anlatılır; kullanım önerisi değildir.</aside>
<div class="sheet-foot"><a class="cta" href="/kavram/">Bütün kavramlar →</a><div class="pager">{(f'<a href="/kavram/{prev_["slug"]}/">← {e(prev_["ad"])}</a>') if prev_ else ''}{(f'<a href="/kavram/{next_["slug"]}/">{e(next_["ad"])} →</a>') if next_ else ''}</div></div>
{abone('kavram:' + k['slug'])}
</article>'''
    write(path, page(f'{k["ad"]} nedir? {k["kisa"][:60].rsplit(" ", 1)[0]}… | Bitki Tabanı' if len(k['kisa']) > 60 else f'{k["ad"]} nedir? {k["kisa"]} | Bitki Tabanı', k['kisa'], path, body, 'kavram', narrow=True,
          extra=lds({"@context":"https://schema.org","@type":"DefinedTerm","name":k['ad'],"description":k['kisa'],"inDefinedTermSet":BASE + '/kavram/',"url":BASE+path},
                    {"@context":"https://schema.org","@type":"Article","headline":k['ad'],"description":k['kisa'],"inLanguage":"tr","url":BASE+path,"author":AUTHOR,"datePublished":k['yayin'],"citation":[t for t, u in k['kaynaklar']]},
                    crumb_ld(('/kavram/', 'Kavramlar'), (path, k['ad']))), image=(f'{BASE}/img/{k["bitki"]}-960.jpg' if k['bitki'] in IMG else None)))
    GUIDE_URLS.append(path)
if True:
    _kl = ''.join(f'<li><a href="/kavram/{k["slug"]}/"><b>{e(k["ad"])}</b></a><span>{e(k["kisa"])} · Bitkisi: <a href="/{k["bitki"]}/">{e(byId[k["bitki"]]["tr"])}</a></span></li>' for k in sorted(KAV, key=lambda k: k['ad'].replace('Ç','C~').replace('Ö','O~').replace('Ş','S~').replace('Ü','U~').replace('İ','I~')))
    write('/kavram/', page('Kavramlar sözlüğü: şamanizm, ritüel ve kadim bilgi | Bitki Tabanı', 'Her gün bir kavram ve onunla eşleşen bir bitki: animizm, kam, nazar, Pachamama, limpia, öğretmen bitkiler ve daha fazlası.', '/kavram/',
          f'''{crumbs(('/kavram/', 'Kavramlar'))}<header class="page-head"><span class="eyebrow">Her gün bir kavram, bir bitki · {len(KAV)} madde</span><h1>Kavramlar sözlüğü</h1><p>Şamanizmden halk inançlarına, ritüellerden kadim bilgiye: her gün kısa, kaynaklı bir kavram ve onunla eşleşen bir bitki.</p></header>
{('<section class="sec"><h2>Bugünün kavramı</h2><p><a class="cta" href="/kavram/' + KAV_TODAY["slug"] + '/">' + e(KAV_TODAY["ad"]) + ' →</a></p>' + kav_plant(KAV_TODAY) + '</section>') if KAV_TODAY else ''}
{('<section class="sec"><h2>A’dan Z’ye</h2><ul class="guidelist">' + _kl + '</ul></section>') if _kl else '<p>İlk kavram yarın sabah burada.</p>'}''', 'kavram', narrow=True))
    GUIDE_URLS.insert(0, '/kavram/')

# --- takvim bileşeni (ritüel + toplama, aylık ızgara; tıklayınca takvime ekle / paylaş) ---
_TK_KIS = {'cicek': 'Çiçek', 'yaprak': 'Yaprak', 'herba': 'Toprak üstü', 'kok': 'Kök', 'tohum': 'Meyve ve tohum', 'kabuk': 'Kabuk', 'recine': 'Reçine'}
def _tk_kisim(p):
    for k in ('cicek', 'yaprak', 'herba', 'kok', 'tohum', 'kabuk', 'recine'):
        if k in kisim_of(p).split(): return k
    return 'herba'
def _tk_data():
    ol = [{'s': o['slug'], 'ad': o['ad'], 'kisa': o['kisa'], 'tur': o.get('tur', 'halk'), 't': o['tarih'], 'not': o.get('hazirlik', ''),
           'b': [[x, byId[x]['tr']] for x in o['bitkiler'] if x in byId], 'l': list(_olink(o))} for o in OLAYLAR]
    tp = []
    for p in P:
        if 'anadolu' in p['bolge'] and p['guv'] != 'yuksek' and p['id'] not in YASAL and not KORUMA.get(p['id'], {}).get('rozet') and p['id'] in EK:
            ay = sorted(months_of(EK[p['id']].get('mevsim', '')))
            if ay: tp.append({'id': p['id'], 'ad': p['tr'], 'ay': ay, 'k': _tk_kisim(p), 'm': EK[p['id']]['mevsim'], 'a': 1 if isinstance(TANIMA.get(p['id'] + ':kuru'), dict) else 0})
    _T = 'abcçdefgğhıijklmnoöprsştuüvyz'
    tp.sort(key=lambda x: [(-1 if c == ' ' else _T.index(c) if c in _T else 100 + ord(c)) for c in x['ad'].replace('I', 'ı').replace('İ', 'i').lower()])
    return {'o': ol, 'p': tp, 'k': _TK_KIS}
TK = _tk_data()
def takvim_widget(odak):
    return ('<section class="tk" data-odak="' + odak + '" aria-label="Takvim"><div class="tk-govde"><p class="muted-s">Takvim yükleniyor…</p></div>'
        '<p class="tk-abone muted-s">Bütün ritüelleri ve toplama mevsimlerini telefonunun takvimine ekle: <a href="webcal://bitkitabani.com/takvim.ics">Takvime abone ol</a> · <a href="/takvim.ics" download>.ics indir</a></p>'
        '<dialog class="tk-dlg"><form method="dialog"><button class="tk-x" aria-label="Kapat">×</button></form><div class="tk-ic"></div></dialog>'
        '<script type="application/json" id="tkData">' + json.dumps(TK, ensure_ascii=False).replace('</', '<\\/') + '</script></section>')
def _ics_esc(t): return str(t).replace('\\', '\\\\').replace(';', '\\;').replace(',', '\\,').replace('\n', '\\n')
_ics = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Bitki Tabani//Takvim//TR', 'CALSCALE:GREGORIAN', 'METHOD:PUBLISH', 'X-WR-CALNAME:Bitki Tabanı', 'X-WR-TIMEZONE:Europe/Istanbul', 'REFRESH-INTERVAL;VALUE=DURATION:P7D']
_y0 = LOCAL_DAY.year
for o in OLAYLAR:
    _b, _s = olay_tarihi(o, _y0)
    _ics += ['BEGIN:VEVENT', f'UID:olay-{o["slug"]}@bitkitabani.com', f'DTSTAMP:{_y0}0101T000000Z', f'DTSTART;VALUE=DATE:{_b:%Y%m%d}', f'DTEND;VALUE=DATE:{(_s + datetime.timedelta(days=1)):%Y%m%d}', 'RRULE:FREQ=YEARLY',
             'SUMMARY:' + _ics_esc(o['ad']), 'DESCRIPTION:' + _ics_esc(o['kisa'] + (' ' + o['hazirlik'] if o.get('hazirlik') else '') + ' ' + BASE + '/takvim/#' + o['slug']), f'URL:{BASE}/takvim/#{o["slug"]}', 'END:VEVENT']
for x in TK['p']:
    _m = x['ay'][0]
    _ics += ['BEGIN:VEVENT', f'UID:toplama-{x["id"]}@bitkitabani.com', f'DTSTAMP:{_y0}0101T000000Z', f'DTSTART;VALUE=DATE:{_y0}{_m:02d}01', f'DTEND;VALUE=DATE:{_y0}{_m:02d}02', 'RRULE:FREQ=YEARLY',
             'SUMMARY:' + _ics_esc('🌿 ' + x['ad'] + ' toplama mevsimi'), 'DESCRIPTION:' + _ics_esc(x['m'] + ' ' + BASE + '/' + x['id'] + '/'), f'URL:{BASE}/{x["id"]}/', 'END:VEVENT']
_ics.append('END:VCALENDAR')
def _fold(l):
    b = l.encode('utf-8'); out = []
    while len(b) > 73:
        i = 73
        while (b[i] & 0xC0) == 0x80: i -= 1
        out.append(b[:i].decode('utf-8')); b = b[i:]
    out.append(b.decode('utf-8')); return '\r\n '.join(out)
open(os.path.join(OUT, 'takvim.ics'), 'w', encoding='utf-8', newline='').write('\r\n'.join(_fold(l) for l in _ics) + '\r\n')

# --- takvim sayfası ---
_ol = []
for o in OLAYLAR:
    bas, son = olay_tarihi(o, LOCAL_DAY.year)
    if son < LOCAL_DAY: bas, son = olay_tarihi(o, LOCAL_DAY.year + 1)
    _ol.append((bas, o))
_ol.sort(key=lambda x: x[0])
def _olay_html(bas, o):
    tarih = AYLAR[bas.month - 1] + ' boyunca' if len(o['tarih']) == 2 else f'{bas.day} {AYLAR[bas.month - 1]}'
    bt = ''.join(f'<a class="chip" href="/{x}/">{e(byId[x]["tr"])}</a>' for x in o['bitkiler'] if x in byId)
    mo = ''.join(f'<a class="motif-mini-a" href="/semboller/{m["slug"]}/" title="{e(m["ad"])}">{motif_svg(m)}</a>' for m in MOTIFLER if m['slug'] in o['motifler'])
    kv = next((k for k in KAV if k['slug'] == o.get('kavram')), None)
    kay = ''.join(f' <a href="{e(u)}" target="_blank" rel="noopener">[{i}]</a>' for i, (t, u) in enumerate(o['kaynaklar'], 1))
    metin = re.sub(r'\s*\[\d+\]', '', o['metin'])
    return f'''<article class="olay{' aktif' if AKTIF is o else ''}" id="{o["slug"]}"><div class="olay-t"><b>{tarih}</b></div><div><h2>{e(o["ad"])}</h2><p>{e(metin)}{kay}</p>{('<div class="related">' + bt + '</div>') if bt else ''}{('<div class="olay-mo">' + mo + '</div>') if mo else ''}<p class="muted-s">{('<a href="/kavram/' + kv["slug"] + '/">Kavram: ' + e(kv["ad"]) + '</a> · ') if kv else ''}<a href="{_olink(o)[0]}">{e(_olink(o)[1])}</a></p></div></article>'''
write('/takvim/', page('Ritüel ve mevsim takvimi: Nevruz, Hıdrellez, gündönümleri | Bitki Tabanı', 'Nevruz, Hıdrellez, gündönümleri, ekinokslar ve And’larda Pachamama ayı: yılın ritüel ve mevsim takvimi, bitkileri ve sembolleriyle.', '/takvim/',
      f'''{crumbs(('/takvim/', 'Takvim'))}{takvim_tabs('r')}<header class="page-head"><span class="eyebrow">Ritüel ve mevsim takvimi</span><h1>Yılın dönüm noktaları</h1><p>Bayramlar, gündönümleri ve doğadaki büyük değişimler; her biri kendi bitkileri ve sembolleriyle. Çarktaki noktalar yılın dönüm noktaları; birine dokun, takvimine ekle ya da paylaş.</p></header>
{takvim_widget('o')}<details class="tk-detay" id="ayrinti"><summary>Ayrıntılar, semboller ve kaynaklar</summary>
<div class="olaylar">{"".join(_olay_html(b, o) for b, o in _ol)}</div></details>''', 'takvim', '<script src="/assets/takvim.js" defer></script>', narrow=True, extra=lds(crumb_ld(('/takvim/', 'Takvim')))))
GUIDE_URLS.append('/takvim/')

# --- yöresel ve diğer adlar sözlüğü ---
import unicodedata as _ud
_TRA = 'abcçdefgğhıijklmnoöprsştuüvyz'
def _trkey(w): return [(-1 if c == ' ' else _TRA.index(c) if c in _TRA else 100 + ord(c)) for c in w.replace('I', 'ı').replace('İ', 'i').lower()]
def _cap(w): return (w[0].replace('i', 'İ').replace('ı', 'I').upper() + w[1:]) if w else w
_BAD = re.compile(r'\b(akrabası|türleri|türü|denir|olarak|adıyla|anlamına|bilinir|ve|ile|gibi|da|de)\b', re.I)
_names = {}
for p in P:
    if p['guv'] == 'yuksek' and False: pass
    srcs = [p['diger']] + [EK.get(p['id'], {}).get('yoresel', '')]
    for src in srcs:
        for n in re.split(r'[,;/]', re.sub(r'\([^)]*\)', '', src or '')):
            n = n.strip().strip('.').strip()
            if 2 < len(n) < 32 and len(n.split()) <= 3 and not _BAD.search(n) and not re.search(r'[A-Z][a-z]+ [a-z]+$', n) and n.replace('I', 'ı').replace('İ', 'i').lower() != p['tr'].replace('I', 'ı').replace('İ', 'i').lower():
                _names.setdefault(n.replace('I', 'ı').replace('İ', 'i').lower(), (_cap(n), set()))[1].add(p['id'])
_rows = sorted(_names.values(), key=lambda x: _trkey(x[0]))
_groups = {}
for n, ids in _rows:
    L = n.replace('i', 'İ').replace('ı', 'I').upper()[0] if n else '#'
    _groups.setdefault(L, []).append((n, ids))
_letters = ''.join(f'<a href="#harf-{_ud.normalize("NFKD", L).encode("ascii", "ignore").decode() or "x"}{i}">{L}</a>' for i, L in enumerate(_groups))
_sec = ''.join(f'<details class="harf" id="harf-{_ud.normalize("NFKD", L).encode("ascii", "ignore").decode() or "x"}{i}"><summary><b>{L}</b> <span class="muted-s">{len(items)} ad</span></summary><ul class="adlar2">' + ''.join(f'<li data-s="{e(n.lower())}"><b>{e(n)}</b> <span aria-hidden="true">→</span> ' + ', '.join(f'<a href="/{x}/">{e(byId[x]["tr"])}</a>' for x in sorted(ids)) + '</li>' for n, ids in items) + '</ul></details>' for i, (L, items) in enumerate(_groups.items()))
_ADLAR_N = len(_rows)
_ADLAR_HTML = f'''<section class="sec" id="adlar"><h2>Yöresel adlar: hangi ad hangi bitki?</h2><p>Aynı bitki farklı yörelerde farklı adlarla anılır; bazen de aynı ad birbirinden çok farklı bitkilere verilir. Katalogdaki bitkilerin {len(_rows)} yöresel, halk arasındaki ve yabancı adı A’dan Z’ye; her ad doğru bitkiye bağlanır.</p>
<div class="adara"><input type="search" id="adq" placeholder="Bir ad yazın (ör. kömeç, akpüren)" aria-label="Adlarda ara"><span class="muted-s" id="adn" role="status"></span></div>
<nav class="harfler" aria-label="Harfler">{_letters}</nav><div class="harfler-list">{_sec}</div>
<script>(function(){{var q=document.getElementById('adq'),n=document.getElementById('adn'),D=document.querySelectorAll('details.harf');
function low(t){{return t.replace(/I/g,'ı').replace(/İ/g,'i').toLowerCase()}}
q.addEventListener('input',function(){{var t=low(q.value.trim()),c=0;D.forEach(function(d){{var k=0;d.querySelectorAll('li').forEach(function(li){{var v=!t||low(li.textContent).indexOf(t)>-1;li.hidden=!v;if(v)k++}});d.hidden=!k;d.open=!!t&&k>0;c+=k}});n.textContent=t?c+' sonuç':''}});
document.querySelectorAll('.harfler a').forEach(function(a){{a.addEventListener('click',function(){{var d=document.querySelector(a.getAttribute('href'));if(d)d.open=true}})}});
if(location.hash){{var d=document.querySelector(location.hash);if(d&&d.tagName==='DETAILS')d.open=true}}}})();</script>
<aside class="warnbox" role="note"><b>Karıştırma:</b> Bir ad birden fazla bitkiye bağlanıyorsa, o bitkiler halk arasında aynı adla anılıyor demektir. Toplarken ya da satın alırken Latince adına ve bitkinin sayfasındaki “karıştırma riski” notuna bak.</aside></section>'''

# --- halk hekimliğinden hikâyeler: her kaynaklı hikâyenin kendi sayfası (Threads/Instagram gönderileri buraya bağlanır) ---
from halk import hikayeler as _hik
HIK = _hik()
def _hik_bitki(h):
    if h.get('bitki') in byId: return h['bitki']
    l = (h.get('link') or '').strip('/')
    return l if l in byId else None
def _hik_kart(h):
    b = _hik_bitki(h)
    img = f'<img src="/img/{b}-500.jpg" alt="" loading="lazy" width="500" height="333">' if b and b in IMG and os.path.exists(os.path.join(HERE, 'img', f'{b}-500.jpg')) else ''
    return f'<li class="hk"><a href="/hikaye/{h["slug"]}/">{img}<b>{e(h["baslik"])}</b><span class="muted-s">{e(h.get("yore") or h["kisa"])}</span></a></li>'
for h in HIK:
    pth = f'/hikaye/{h["slug"]}/'
    b = _hik_bitki(h)
    ilgili = [x for x in HIK if x is not h and (_hik_bitki(x) == b and b)][:3] or [x for x in HIK if x is not h][:3]
    body = (f'{crumbs(("/hikaye/", "Halk hekimliğinden"), (pth, h["baslik"][:40]))}<article class="hikaye"><header class="page-head"><span class="eyebrow">Halk hekimliğinden{" · " + e(h["yore"]) if h.get("yore") else ""}</span><h1>{e(h["baslik"])}</h1></header>'
            f'{sharebar(h["baslik"], pth)}<p class="lead">{e(h["post"])}</p>'
            + f'<p class="muted-s">Kaynak: <a href="{h["kaynak"][1]}" target="_blank" rel="noopener">{e(h["kaynak"][0])}</a>. Bu bir halk kaydıdır, tedavi önerisi değildir.</p>'
            + (f'<section class="sec"><h2>Bu hikâyenin bitkisi</h2><div class="grid sim">{card(byId[b])}</div></section>' if b else (f'<p><a class="cta" href="/{h["link"]}">Devamı →</a></p>' if h.get('link') else ''))
            + f'</article>{abone("hikaye-" + h["slug"][:30], "Her hafta bir halk hekimliği hikâyesi", "Anadolu’dan kaynaklı şifa hikâyeleri, bitkileri ve uyarılarıyla; her pazar e-postanda.", kurs=False)}'
            + f'<section class="sec"><h2>Başka hikâyeler</h2><ul class="hklist">{"".join(_hik_kart(x) for x in ilgili)}</ul><p><a href="/hikaye/">Bütün hikâyeler →</a></p></section>')
    write(pth, page(f'{h["baslik"]} | Halk hekimliğinden | Bitki Tabanı', h['post'][:155].rsplit(' ', 1)[0] + '…', pth, body, 'hikaye', narrow=True,
          extra=lds({"@context": "https://schema.org", "@type": "Article", "headline": h["baslik"][:110], "inLanguage": "tr", "url": BASE + pth, "author": AUTHOR, "citation": h["kaynak"][0]}, crumb_ld(("/hikaye/", "Halk hekimliğinden"), (pth, h["baslik"][:40]))),
          image=(f'{BASE}/img/{b}-960.jpg' if b and b in IMG else None)))
    GUIDE_URLS.append(pth)
write('/hikaye/', page('Halk hekimliğinden: Anadolu’nun şifa hikâyeleri | Bitki Tabanı', f'Anadolu’dan {len(HIK)} kaynaklı halk hekimliği hikâyesi: ocaklar, nazar, yayla otları, yöresel şifa gelenekleri ve bitkileri.', '/hikaye/',
      f'{crumbs(("/hikaye/", "Halk hekimliğinden"))}<header class="page-head"><span class="eyebrow">{len(HIK)} hikâye · her hafta yenisi</span><h1>Halk hekimliğinden</h1><p>Anadolu’nun köylerinden, ocaklarından ve eski tıp metinlerinden kaynaklı şifa hikâyeleri. Her biri bir dergi makalesine ya da saha çalışmasına dayanır ve bir bitkiye bağlanır.</p></header><ul class="hklist">{"".join(_hik_kart(h) for h in reversed(HIK))}</ul>{abone("hikaye-liste", "Her hafta bir halk hekimliği hikâyesi", "Anadolu’dan kaynaklı şifa hikâyeleri, bitkileri ve uyarılarıyla; her pazar e-postanda.", kurs=False)}',
      'hikaye', narrow=True, extra=lds(crumb_ld(("/hikaye/", "Halk hekimliğinden")))))
GUIDE_URLS.insert(0, '/hikaye/')

# --- yöre sayfaları ---
_ils = sorted(YORE_IL, key=_trkey0)
_yb = sum(len(d['bitki']) for d in YORE_IL.values())
_ybody = f'''{crumbs(('/yoreler/', 'Yöreler'))}<header class="page-head"><span class="eyebrow">Yöreler · {len(YORE_IL)} il · {len(_YC)} saha çalışması · {_ADLAR_N} yöresel ad</span><h1>Anadolu’da hangi yörede hangi bitki kullanılıyor?</h1><p>Türkiye’de yapılmış etnobotanik saha çalışmalarında katalogdaki bitkilerin kaydedildiği yöreler. Renkli illere dokun; her kayıt kaynağına bağlıdır. Harita yeni çalışmalar işlendikçe büyüyor.</p></header>
<figure class="trmap-w">{tr_haritasi()}<figcaption>Harita: Natural Earth (kamu malı). Noktalar saha çalışmasının yapıldığı yeri gösterir. Kişi ve köy adları yayımlanmaz.</figcaption></figure>
<aside class="warnbox" role="note"><b>Okurken:</b> Bir bitkinin bir yörede kaydedilmiş olması, o kullanımın işe yaradığını göstermez; yalnızca halk arasında bilindiğini gösterir. Kanıt ve güvenlik için bitkinin kendi sayfasına bak.</aside>
<nav class="tabs" aria-label="Bölümler"><a href="#iller">İller</a><a href="#adlar">Yöresel adlar A–Z</a></nav><div id="iller"></div>''' + ''.join(f'<section class="sec" id="il-{_ilslug(il)}">' + _il_bolum(il, YORE_IL[il]) + (f'<p><a class="cta small" href="/yore/{_ilslug(il)}/">{e(il)} sayfası →</a></p>' if il in YORE_SAYFA else '') + '</section>' for il in _ils) + _ADLAR_HTML
write('/yoreler/', page(f'Yöreler ve yöresel adlar: Anadolu’da hangi yörede hangi şifalı bitki? | Bitki Tabanı', f'{len(YORE_IL)} ilde saha çalışmalarında kaydedilen şifalı bitkiler haritada ve {_ADLAR_N} yöresel bitki adı A’dan Z’ye: hangi ad hangi bitki, kaynaklarıyla.', '/yoreler/', _ybody, 'yore', narrow=True, extra=lds(crumb_ld(('/yoreler/', 'Yöreler')))))
GUIDE_URLS.append('/yoreler/')
for il in YORE_SAYFA:
    _p = f'/yore/{_ilslug(il)}/'
    _d = YORE_IL[il]
    _ad3 = ', '.join(byId[q]['tr'].lower() for q in sorted(_d['bitki'], key=lambda q: -len(_d['bitki'][q]))[:3])
    _body = f'''{crumbs(('/yoreler/', 'Yöreler'), (_p, il))}<header class="page-head"><span class="eyebrow">Yöre · {len(_d['bitki'])} bitki · {len(_d['cal'])} saha çalışması</span><h1>{e(il)} yöresinde kullanılan şifalı bitkiler</h1><p>{e(il)}’da yapılmış etnobotanik saha çalışmalarında halk arasında kullanıldığı kaydedilen ve Bitki Tabanı kataloğunda yer alan bitkiler. Her bitkinin kanıtı ve güvenlik notu kendi sayfasında.</p></header>
<figure class="trmap-w mini">{tr_haritasi(il)}</figure>
<section class="sec">{_il_bolum(il, _d, 'h2')}</section>
<aside class="warnbox" role="note"><b>Okurken:</b> Halk arasında kaydedilmiş bir kullanım, bitkinin o derde iyi geldiğini göstermez. İlaç kullanıyorsan, hamileysen ya da emziriyorsan bitkileri kullanmadan önce eczacına danış.</aside>
<p><a href="/yoreler/">Bütün yöreler →</a></p>'''
    write(_p, page(f'{il} yöresinde kullanılan şifalı bitkiler | Bitki Tabanı', f'{il}’da etnobotanik saha çalışmalarında kaydedilen {len(_d["bitki"])} şifalı bitki: {_ad3} ve diğerleri. Kaynaklarıyla.', _p, _body, 'yore', narrow=True, extra=lds(crumb_ld(('/yoreler/', 'Yöreler'), (_p, il)))))
    GUIDE_URLS.append(_p)

# --- toplama takvimi (ay ay) ---
_cal = {m: [] for m in range(1, 13)}
for p in P:
    if 'anadolu' in p['bolge'] and p['guv'] != 'yuksek' and p['id'] not in YASAL and not KORUMA.get(p['id'], {}).get('rozet') and p['id'] in EK:
        for m in months_of(EK[p['id']].get('mevsim', '')): _cal[m].append(p)
_cur = LOCAL_DAY.month
_order = [(_cur + i - 1) % 12 + 1 for i in range(12)]
_cs = ''.join(f'<section class="sec" id="ay-{m}"><h2>{AYLAR[m-1]}{" (bu ay)" if m == _cur else ""}</h2>' + ('<ul class="adlar">' + ''.join(f'<li><a href="/{q["id"]}/"><b>{e(q["tr"])}</b></a> · {e(EK[q["id"]]["mevsim"])}</li>' for q in sorted(_cal[m], key=lambda q: _trkey(q["tr"]))) + '</ul>' if _cal[m] else '<p class="muted-s">Bu ay katalogda toplama mevsimi olan bir bitki yok.</p>') + '</section>' for m in _order)
path = '/toplama-takvimi/'
write(path, page(f'Şifalı bitki toplama takvimi: {AYLAR[_cur-1]} ayında hangi bitkiler toplanır? | Bitki Tabanı', f'Anadolu’da ay ay toplanan şifalı bitkiler. {AYLAR[_cur-1]} ayında toplama mevsimi olan {len(_cal[_cur])} bitki ve yılın geri kalanı.', path,
      f'''{crumbs(('/takvim/', 'Takvim'), (path, 'Doğada bu ay'))}{takvim_tabs('d')}<header class="page-head"><span class="eyebrow">Ay ay · {AYLAR[_cur-1]} başta</span><h1>Şifalı bitki toplama takvimi</h1><p>Anadolu’da yetişen bitkilerin toplama mevsimleri, kayıtlardaki “Doğada” bilgisinden derlendi. Liste her ay kendiliğinden içinde bulunduğumuz aydan başlar. Koruma altındaki, yasal kısıtlı ve yüksek riskli bitkiler bu listeye alınmaz.</p></header>
<aside class="warnbox" role="note"><b>Toplarken:</b> Yalnızca kesin tanıdığın bitkileri, yol kenarından ve ilaçlanmış alanlardan uzakta topla; bir bitkinin tamamını değil bir kısmını alın ki yeniden büyüyebilsin.</aside>{takvim_widget('p')}<details class="tk-detay"><summary>Ay ay liste</summary>{_cs}</details>''', 'rehber', '<script src="/assets/takvim.js" defer></script>', narrow=True, extra=lds(crumb_ld(('/rehber/', 'Rehberler'), (path, 'Toplama takvimi')))))
GUIDE_URLS.append(path)

# --- rehber ana sayfası ---
gl = ''.join(f'<li class="gi"><a href="/rehber/{k["slug"]}/">{ico(k["slug"], "ico-b")}<b>{e(k["kisa"])}</b></a><span>{e(k["aciklama"])}</span></li>' for k in LIVE_K)
hub = f'''{crumbs(('/rehber/', 'Rehberler'))}
<header class="page-head"><span class="eyebrow">Şifa</span><h1>Hangi derde hangi bitki? Kanıtıyla ve riskleriyle</h1><p>Derdini kendi cümlelerinle yaz, üç soruda bul ya da aşağıdaki rehberlerden birini seç. Her rehberde bitkiler kanıtı en güçlü olandan başlayarak sıralanır; her birinin yanında güvenlik etiketi var.</p></header><section class="sec" id="ara"><h2>Derdini yaz</h2><form id="araForm" class="katki-form"><input id="araQ" name="q" maxlength="200" placeholder="Örn. uykuya dalmakta zorlanıyorum; hamileyim, mide bulantısı" required><button class="cta" type="submit">Ara</button></form><div id="araSonuc" role="status"></div><p class="muted-s">Yapay zekâ destekli anlam araması. Sonuçlar tavsiye değildir; her bitkinin güvenlik notuna bak. Ya da <a href="/bitki-bul/"><b>üç soruda bul</b></a>: hamilelik ve ilaç durumuna göre riskli olanlar kendiliğinden elenir.</p></section>
<section class="sec"><h2>Güvenlik</h2><ul class="guidelist"><li><a href="/rehber/ilac-etkilesimi/"><b>İlaç etkileşimi aracı</b></a><span>Kullandığın ilaç grubunu seç, katalogda o ilaçla etkileşimi bildirilen bitkileri gör.</span></li><li><a href="/rehber/hamilelik-emzirme/"><b>Hamilelik ve emzirme</b></a><span>Hamilelikte ve emzirirken kullanılmaması ya da dikkatle kullanılması gereken bitkiler.</span></li></ul></section>
<section class="sec"><h2>Derde göre</h2><ul class="guidelist">{gl}</ul></section>
<section class="sec"><h2>Karşılaştırmalar</h2><ul class="otherlist">{"".join(f'<li><a href="/karsilastirma/{c["a"]}-ve-{c["b"]}/">{e(c["baslik"])}</a></li>' for c in LIVE_C)}</ul></section>
<section class="sec"><h2>Tarifler</h2><ul class="otherlist">{"".join(f'<li><a href="/tarif/{t["slug"]}/">{e(t["ad"])}</a></li>' for t in LIVE_T)}</ul></section>
{DISCL}'''
write('/rehber/', page('Hangi derde hangi bitki? Şifalı bitki bulucu ve rehberler | Bitki Tabanı', 'Uyku, öksürük, mide, soğuk algınlığı, kaygı ve daha fazlası için şifalı bitkiler: kanıt düzeyleri, güvenlik notları, ilaç etkileşimleri ve tarifler.', '/rehber/', hub, 'rehber', '<script src="/assets/ara.js" defer></script>', narrow=True,
      extra=lds(crumb_ld(('/rehber/', 'Rehberler')))))
GUIDE_URLS.insert(0, '/rehber/')

# --- Pinterest için RSS (pano otomatik dolar) ---
from email.utils import format_datetime as _fdp
_pin = []
_d0 = datetime.datetime.fromisoformat(CONTENT_DATE + 'T09:00:00+03:00')
def _pitem(title, url, desc, pid, when):
    f = f'{pid}-1280.jpg' if os.path.exists(os.path.join(HERE, 'img', f'{pid}-1280.jpg')) else f'{pid}-960.jpg'
    return f'<item><title>{e(title)}</title><link>{BASE}{url}</link><guid>{BASE}{url}</guid><pubDate>{_fdp(when)}</pubDate><description>{e(f'<img src="{BASE}/img/{f}" alt="{title}"/><p>{desc}</p>')}</description><enclosure url="{BASE}/img/{f}" type="image/jpeg" length="0"/><media:content url="{BASE}/img/{f}" medium="image" type="image/jpeg"/></item>'
for i in NEWEST[:20]:
    if i in IMG:
        q = byId[i]; d = YENI[i]
        _pin.append(_pitem(f'{q["tr"]} ({short_la(q)})', f'/{i}/', q['ilginc'], i, datetime.datetime(d.year, d.month, d.day, 9, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=3)))))
for t in LIVE_T:
    if t['bitki'] in IMG: _pin.append(_pitem(t['ad'] + ' nasıl yapılır?', f'/tarif/{t["slug"]}/', t['kisa'], t['bitki'], _d0))
for k in LIVE_K:
    pid = next((x for x, _ in k['bitkiler'] if x in byId and x in IMG), None)
    if pid: _pin.append(_pitem(k['baslik'], f'/rehber/{k["slug"]}/', k['ozet'], pid, _d0))
open(os.path.join(OUT, 'pinterest.xml'), 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/"><channel><title>Bitki Tabanı</title><link>{BASE}/</link><description>Şifalı bitkiler: tarifler, rehberler ve yeni eklenen bitkiler.</description><language>tr</language>{"".join(_pin)}</channel></rss>')
def _pfeed(fn, title, desc, items):
    open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/"><channel><title>{e(title)}</title><link>{BASE}/</link><description>{e(desc)}</description><language>tr</language>{"".join(items)}</channel></rss>')
def _pimg(title, url, desc, img, when):
    return f'<item><title>{e(title)}</title><link>{BASE}{url}</link><guid>{BASE}{url}#{img.rsplit("/",1)[-1]}</guid><pubDate>{_fdp(when)}</pubDate><description>{e(f'<img src="{BASE}{img}" alt="{title}"/><p>{desc}</p>')}</description><enclosure url="{BASE}{img}" type="image/jpeg" length="0"/><media:content url="{BASE}{img}" medium="image" type="image/jpeg"/></item>'
# katalogun tamamı (her bitki bir pin)
_pfeed('pinterest-katalog.xml', 'Bitki Tabanı: şifalı bitkiler kataloğu', 'Her şifalı bitki: ne işe yarar, kanıtı ve uyarıları.',
       [_pitem(f'{q["tr"]} ({short_la(q)}): ne işe yarar, kimler kullanmamalı?', f'/{q["id"]}/', q['ilginc'], q['id'], _d0) for q in P if q['id'] in IMG])
# botanik çizimler (Köhler/Thomé levhaları)
_pfeed('pinterest-cizim.xml', 'Bitki Tabanı: botanik çizimler', 'Köhler ve Thomé’nin 19. yüzyıl tıbbi bitki levhaları.',
       [_pimg(f'{byId[k.split(":")[0]]["tr"]} botanik çizimi ({short_la(byId[k.split(":")[0]])})', f'/{k.split(":")[0]}/', (v.get('artist') or '') + '. ' + byId[k.split(":")[0]]['ilginc'], f'/img/tanima/{k.split(":")[0]}-cizim.jpg', _d0)
        for k, v in sorted(TANIMA.items()) if k.endswith(':cizim') and isinstance(v, dict) and k.split(':')[0] in byId])
# kavramlar ve kültür
_pfeed('pinterest-kultur.xml', 'Bitki Tabanı: şamanizm, ritüel ve kavramlar', 'Bitkilerle ilgili kavramlar, ritüeller ve semboller.',
       [_pitem(f'{k["ad"]} nedir? {k["kisa"]}'[:100], f'/kavram/{k["slug"]}/', k['kisa'], k['bitki'], _d0) for k in KAV if k['bitki'] in IMG] + [_pitem(h['baslik'][:100], f'/hikaye/{h["slug"]}/', h['post'][:300], _hik_bitki(h), _d0) for h in HIK if _hik_bitki(h) in IMG])

# ---------- bülten sayfaları ve kayıt hediyeleri ----------
_bscript = '<script src="/assets/bulten.js" defer></script>'
write('/bulten/', page('Bitki Tabanı bülteni: her pazar haftanın bitkileri | Bitki Tabanı', 'Haftada bir e-posta: yeni eklenen şifalı bitkiler, bir rehber ve bir tarif. Kaydolunca yazdırılabilir bitki–ilaç etkileşimi kartı hediye.', '/bulten/',
      f'''<header class="page-head"><span class="eyebrow">Bülten</span><h1>Her pazar, haftanın bitkileri</h1><p>Haftada yalnızca bir e-posta: o hafta kataloğa eklenen bitkiler, bir “derde göre” rehber ve bir çay tarifi. Reklam yok, adresin kimseyle paylaşılmaz, tek tıkla çıkabilirsin.</p></header>
<section class="sec"><h2>Kaydolunca hediye</h2><ul class="otherlist"><li><b>Bitki–ilaç etkileşimi kartı:</b> kan sulandırıcı, tansiyon, şeker ilacı ya da antidepresan kullananların dikkat etmesi gereken bitkiler, tek sayfada.</li><li><b>Hamilelikte dikkat listesi:</b> hamilelikte ve emzirirken kullanılmaması gereken bitkiler, buzdolabına asılacak boyutta.</li></ul></section>
{abone('bulten-sayfasi', 'Bültene kaydol', 'E-posta adresini yaz; gelen e-postadaki bağlantıya tıklayınca kaydın tamamlanır.', kurs=False)}
<p>Yeni başlıyorsanız: <a href="/kurs/">7 günlük ücretsiz e-posta kursu “Şifalı bitkilere başlangıç” →</a></p>''', '', narrow=True, scripts=_bscript))
from kurs import DERSLER
write('/kurs/', page('Ücretsiz e-posta kursu: Şifalı bitkilere başlangıç | Bitki Tabanı', '7 gün boyunca her sabah kısa ve görsel bir ders: kanıtı okumak, doğru demlemek, güvenli kullanmak, doğada toplamak ve kültürler arası bağlar. Ücretsiz.', '/kurs/',
      f'''<header class="page-head"><span class="eyebrow">Ücretsiz · 7 gün · e-posta</span><h1>Şifalı bitkilere başlangıç</h1><p>Yedi gün boyunca her sabah e-postana kısa, görsel bir ders ve küçük bir görev gelir. Sonunda bir bitki çayını bilinçli seçmeyi, güvenli kullanmayı ve internette okuduğun bir iddiayı kontrol etmeyi öğrenmiş olursun.</p></header>
<section class="sec"><h2>Dersler</h2><ol class="start">{"".join(f'<li><b>{e(d["baslik"])}</b>: {e(d["ozet"])}</li>' for d in DERSLER)}</ol></section>
{abone('kurs-sayfasi', 'Kursa kaydol', 'E-posta adresini yaz; gelen e-postadaki bağlantıya tıklayınca ilk ders hemen gelir.')}''', '', narrow=True))
GUIDE_URLS.append('/kurs/')
write('/bulten/onaylandi/', page('Kaydın tamamlandı | Bitki Tabanı', 'Bitki Tabanı bültenine kaydın tamamlandı.', '/bulten/onaylandi/',
      '''<header class="page-head"><span class="eyebrow">Bülten</span><h1>Teşekkürler, kaydın tamamlandı 🌿</h1><p>Kursa kaydolduysanız ilk ders birkaç dakika içinde e-postanızda; değilseniz ilk bülten pazar günü gelecek. Söz verdiğimiz iki hediye burada; yazdırmak için sayfayı açıp tarayıcının “Yazdır” ya da “PDF olarak kaydet” seçeneğini kullan.</p></header>
<section class="sec"><p><a class="cta" href="/indir/etkilesim-karti/">Bitki–ilaç etkileşimi kartı →</a></p><p><a class="cta" href="/indir/hamilelik-listesi/">Hamilelikte dikkat listesi →</a></p></section>''', '', narrow=True, extra='<meta name="robots" content="noindex, follow">'))
write('/bulten/ayrildiniz/', page('Bültenden ayrıldın | Bitki Tabanı', 'Bitki Tabanı bülteninden ayrıldın.', '/bulten/ayrildiniz/',
      '<header class="page-head"><span class="eyebrow">Bülten</span><h1>Bültenden ayrıldın</h1><p>E-posta adresin listemizden tamamen silindi; bir daha e-posta almayacaksın. Fikrini değiştirirseniz <a href="/bulten/">yeniden kaydolabilirsin</a>.</p></header>', '', narrow=True, extra='<meta name="robots" content="noindex, follow">'))
_kart = ''.join(f'<div class="kart-g"><h2>{e(ad)}</h2><p>{", ".join(e(byId[pid]["tr"]) for pid, _, _ in sorted(etk_by[c], key=lambda x: _trkey(byId[x[0]]["tr"])))}</p></div>' for c, ad, _ in ILAC if etk_by[c] and c != 'tum')
write('/indir/etkilesim-karti/', page('Bitki–ilaç etkileşimi kartı (yazdırılabilir) | Bitki Tabanı', 'Yazdırılabilir bitki–ilaç etkileşimi kartı.', '/indir/etkilesim-karti/',
      f'''<article class="kart"><header><p class="eyebrow">Bitki Tabanı · yazdırılabilir kart</p><h1>Bu ilacı kullanıyorsanız, bu bitkilere dikkat</h1><p>Aşağıdaki bitkilerle, yanındaki ilaç grubu arasında etkileşim bildirilmiştir. Liste eksiksiz değildir; bir bitkisel ürüne başlamadan önce eczacına sorun. İlacını kendi başına bırakma.</p></header>
<div class="kart-grid">{_kart}</div><footer><p>Ayrıntılar ve kaynaklar: bitkitabani.com/rehber/ilac-etkilesimi · Zehir Danışma: 114 · Tıbbi tavsiye değildir.</p></footer></article>
<p class="noprint"><button type="button" class="learn" onclick="window.print()">Yazdır / PDF olarak kaydet</button></p>''', '', narrow=True, extra='<meta name="robots" content="noindex, follow">'))
write('/indir/hamilelik-listesi/', page('Hamilelikte dikkat listesi (yazdırılabilir) | Bitki Tabanı', 'Yazdırılabilir hamilelikte dikkat listesi.', '/indir/hamilelik-listesi/',
      f'''<article class="kart"><header><p class="eyebrow">Bitki Tabanı · yazdırılabilir liste</p><h1>Hamilelikte ve emzirirken dikkat edilecek bitkiler</h1><p>Bu bitkilerin güvenlik notunda hamilelik ya da emzirme için ayrıca uyarı vardır. Listede olmayan bir bitki de güvenli demek değildir; yemekteki miktarı aşan her bitkisel ürün için hekimine danış.</p></header>
<ul class="kart-list">{"".join(f'<li><b>{e(p["tr"])}</b>: {e(t)}</li>' for p, t in preg)}</ul><footer><p>Ayrıntılar ve kaynaklar: bitkitabani.com/rehber/hamilelik-emzirme · Tıbbi tavsiye değildir.</p></footer></article>
<p class="noprint"><button type="button" class="learn" onclick="window.print()">Yazdır / PDF olarak kaydet</button></p>''', '', narrow=True, extra='<meta name="robots" content="noindex, follow">'))
GUIDE_URLS.append('/bulten/')

# ---------- 404, robots, sitemap, favicon ----------
nf = '<header class="page-head"><span class="eyebrow">404</span><h1>Bu sayfa bulunamadı</h1><p>Aradığın kayıt taşınmış ya da adres yanlış yazılmış olabilir.</p></header><section class="sec" id="nfs" hidden><h2>Bunu mu arıyordun?</h2><ul class="otherlist" id="nfList"></ul></section><p><a class="cta" id="nfSearch" href="/katalog/">Katalogda ara →</a></p>' + f'<script type="application/json" id="nfData">{json.dumps([[p["id"], p["tr"], p["la"]] for p in P] + [["kopruler/" + slug_of(x), x["t"], ""] for x in BR], ensure_ascii=False)}</script><script src="/assets/404.js" defer></script>'
open(os.path.join(OUT,'404.html'),'w',encoding='utf-8').write(page('Sayfa bulunamadı | Bitki Tabanı','Sayfa bulunamadı.','/404.html',nf,'', narrow=True))
_rules = 'Allow: /\nDisallow: /secim/\nDisallow: /api/\nDisallow: /hesap/\nDisallow: /*?\n'
_ai = ['Googlebot', 'Google-Extended', 'Bingbot', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'Perplexity-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'Applebot', 'Applebot-Extended', 'DuckAssistBot', 'meta-externalagent', 'CCBot']
open(os.path.join(OUT,'robots.txt'),'w').write('# Bitki Tabanı arama motorlarına ve yapay zekâ asistanlarına açıktır; alıntı yaparken kaynak göster.\n# Özet: ' + BASE + '/llms.txt\n\n' + ''.join(f'User-agent: {a}\n' for a in _ai) + _rules + '\nUser-agent: *\n' + _rules + f'\nSitemap: {BASE}/sitemap.xml\n')
import build_en
EN_URLS = build_en.run(globals())
urls = ['/', '/katalog/', '/kultur/', '/kopruler/', '/gunun-bitkisi/', '/yeni/', '/hakkinda/', '/yontem/', '/gizlilik/'] + [f'/kopruler/{slug_of(x)}/' for x in BR] + FAM_URLS + [f'/{p["id"]}/' for p in P] + GUIDE_URLS + EN_URLS
def _imgtag(u):   # görsel site haritası: bitki sayfalarına fotoğraflarını ekle
    pid = u.strip('/').split('/')[-1]
    if pid not in IMG or pid not in byId: return ''
    f = f'{pid}-1280.jpg' if os.path.exists(os.path.join(HERE, 'img', f'{pid}-1280.jpg')) else f'{pid}-960.jpg'
    return f'<image:image><image:loc>{BASE}/img/{f}</image:loc></image:image>'
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + ''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{(LOCAL_DAY.isoformat() if u in ('/', '/gunun-bitkisi/', '/oyun/', '/yeni/', '/katalog/', '/en/', '/en/catalog/') else max(CONTENT_DATE, YENI[u.strip('/').split('/')[-1]].isoformat()) if u.strip('/').split('/')[-1] in YENI else CONTENT_DATE)}</lastmod>{_imgtag(u)}</url>\n' for u in urls) + '</urlset>\n')
# ---------- llms.txt: yapay zekâ asistanları için özet ve tam metin ----------
def _md_plant(p, full=False):
    pid = p['id']; L = [f'## {p["tr"]} ({short_la(p)})', '', f'URL: {BASE}/{pid}/', f'Familya: {p["fam"]} · Bölge: {", ".join(REG[r]["ad"] for r in p["bolge"])} · Kullanılan kısım: {p["kisim"]}',
        f'Bilimsel kanıt: {KANIT[p["kanit"]]["ad"]} · Güvenlik: {GUV[p["guv"]]}' + (f' · Türkiye’de: {YASAL_AD[YASAL[pid][0]]}' if pid in YASAL else ''), '']
    if not full:
        return L[:4] + ['']
    L += ['### Geleneksel kullanım'] + [f'- {w}: {t}' for w, t in p['kul']] + ['', '### Hazırlama', p['haz'], '', '### Bilim ne diyor', p['bilim'], '', '### Güvenlik', p['guvNot'], '']
    if pid in ETK: L += ['### İlaç etkileşimleri'] + [f'- {g}: {w}' for g, w in ETK[pid]] + ['']
    if pid in DERIN: L += ['### İddialar ve kanıt'] + [f'- {i}: {KAN_AD[k]}. {n}' for i, k, n in DERIN[pid]['iddia']] + ['']
    ek = EK.get(pid, {})
    if ek: L += ['### Doğada', f'Nerede yetişir: {ek.get("yetisme","")}', f'Toplama mevsimi: {ek.get("mevsim","")}', f'Yöresel adlar: {ek.get("yoresel","")}', f'Karıştırma riski: {ek.get("karisma","")}', '']
    L += ['### İlginç bilgi', p['ilginc'], '']
    return L
_head = ['# Bitki Tabanı', '', f'> Şifalı ve ritüel bitkiler için Türkçe, kaynaklı ve ticari olmayan bir etnobotanik veri tabanı: {len(P)} bitki; Anadolu, Asya, And Dağları, Amazon ve Kuzey Amerika. Her kayıtta geleneksel kullanım, bilimsel kanıt düzeyi, güvenlik ve ilaç etkileşimleri, Türkiye’deki yasal durum ve kaynaklar yer alır. Hazırlayan: Edanaz Tınmazlar. Tıbbi tavsiye değildir.', '',
         'Alıntı yaparken lütfen bitkinin sayfasını kaynak olarak göster.', '', '## Sayfalar', f'- [Katalog]({BASE}/katalog/): bütün bitkiler, bölge, kullanım, kanıt ve güvenliğe göre', f'- [Kültür köprüleri]({BASE}/kopruler/): farklı kültürlerde benzer kullanılan bitkilerin karşılaştırması',
         f'- [Yöntem]({BASE}/yontem/): kaynaklar, kanıt düzeyleri ve güvenlik etiketleri nasıl belirlenir', f'- [Tam metin]({BASE}/llms-full.txt): bütün kayıtların düz metin hâli', f'- [English edition]({BASE}/en/): the same database in English', '', '## Bitkiler']
open(os.path.join(OUT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(_head + [f'- [{p["tr"]} ({short_la(p)})]({BASE}/{p["id"]}/): {GUV[p["guv"]]}, kanıt: {KANIT[p["kanit"]]["ad"].lower()}' for p in P]) + '\n\n## Kültür köprüleri\n' + '\n'.join(f'- [{x["t"]}]({BASE}/kopruler/{slug_of(x)}/): {x["d"]}' for x in BR) + '\n')
open(os.path.join(OUT, 'llms-full.txt'), 'w', encoding='utf-8').write('\n'.join(_head[:5] + ['Tıbbi tavsiye değildir. Zehirlenme şüphesinde Türkiye’de Ulusal Zehir Danışma Merkezi: 114.', ''] + [l for p in P for l in _md_plant(p, True)]))

os.makedirs(os.path.join(OUT,'assets'), exist_ok=True)
for f in os.listdir(os.path.join(HERE, 'assets')):
    _src = os.path.join(HERE, 'assets', f)
    if os.path.isdir(_src): shutil.copytree(_src, os.path.join(OUT, 'assets', f), dirs_exist_ok=True)
    else: shutil.copy(_src, os.path.join(OUT, 'assets', f))
if os.path.isdir(os.path.join(HERE, 'img')):
    shutil.copytree(os.path.join(HERE, 'img'), os.path.join(OUT, 'img'), dirs_exist_ok=True)
for f in os.listdir(os.path.join(HERE, 'kok')):   # site köküne olduğu gibi kopyalanan doğrulama dosyaları
    shutil.copy(os.path.join(HERE, 'kok', f), os.path.join(OUT, f))
_redir += '/yoresel-adlar/ /yoreler/#adlar 301\n/ara/ /rehber/#ara 301\n/oyun/ / 301\n'
open(os.path.join(OUT, '_redirects'), 'w').write(_redir)
open(os.path.join(OUT, '_headers'), 'w').write('''/*
  Cache-Control: public, max-age=0, must-revalidate
/assets/*
  Cache-Control: public, max-age=3600
/assets/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/img/*
  Cache-Control: public, max-age=2592000
/robots.txt
  Content-Type: text/plain; charset=utf-8
/llms.txt
  Content-Type: text/plain; charset=utf-8
/llms-full.txt
  Content-Type: text/plain; charset=utf-8
''')
# ---------- Instagram postları için veri (tools/ig.py okur; yayımlanmaz) ----------
os.makedirs(os.path.join(HERE, '.cache'), exist_ok=True)
json.dump({'day': LOCAL_DAY.isoformat(), 'yeni': {k: v.isoformat() for k, v in YENI.items()},
           'kuyruk': [[q['id'], q['yayin']] for q in _K.Q],
           'kanit': {k: v['ad'] for k, v in KANIT.items()}, 'guv': GUV, 'reg': {k: v['ad'] for k, v in REG.items()}, 'takvim': {m: [q['id'] for q in sorted(_cal[m], key=lambda q: _trkey(q['tr']))] for m in _cal}, 'derin': {k: [list(x) for x in v['iddia']] for k, v in DERIN.items() if k in byId}, 'karisma': {k: v.get('karisma', '') for k, v in EK.items() if k in byId and v.get('karisma')}, 'kanad': KAN_AD,
           'p': [dict(id=p['id'], no=p['no'], tr=p['tr'], la=short_la(p), fam=p['fam'], kisim=p['kisim'], yoresel=EK.get(p['id'], {}).get('yoresel', ''), bolge=p['bolge'], kat=p['kat'], kul=p['kul'], bilim=p['bilim'], kanit=p['kanit'],
                      guv=p['guv'], guvNot=p['guvNot'], ilginc=p['ilginc'], yasal=(YASAL[p['id']][0] if p['id'] in YASAL else None), img=(p['id'] in IMG),
                      foto=((IMG[p['id']].get('artist') or '') + (' · ' + IMG[p['id']].get('license', '') if IMG[p['id']].get('license') else '')) if p['id'] in IMG else '') for p in P]},
          open(os.path.join(HERE, '.cache', 'ig_input.json'), 'w', encoding='utf-8'), ensure_ascii=False)
# ---------- IndexNow: yeni sayfaları Bing ve Yandex'e bildir (tools/indexnow.py gönderir) ----------
INDEXNOW_KEY = '23b565a8462d297646dd69b30ae82bcf'
open(os.path.join(OUT, INDEXNOW_KEY + '.txt'), 'w').write(INDEXNOW_KEY)
_today = [i for i in YENI if YENI[i] == LOCAL_DAY]
_inx = ['/', '/yeni/', '/gunun-bitkisi/', '/katalog/', '/rehber/', '/tarif/'] + [f'/{i}/' for i in _today] + [u for i in _today for u, _ in GLINKS.get(i, [])]
json.dump({'key': INDEXNOW_KEY, 'urls': sorted(set(BASE + u for u in _inx))}, open(os.path.join(HERE, '.cache', 'indexnow.json'), 'w'))
# ---------- QR kartlar: aktar, pazar ve atölyeler için yazdırılabilir bitki kartları ----------
try:
    import segno
    def _qr(u): return segno.make(u, error='m').svg_inline(scale=4, border=1, dark='#1C2140')
except Exception:
    _qr = None
if _qr:
    def _kart(p):
        im = f'<img src="/img/{p["id"]}-500.jpg" alt="">' if p['id'] in IMG else ''
        bil = p['ilginc'].split('. ')[0].rstrip('.') + '.'
        return (f'<article class="kart"><div class="kart-ust">{im}<div><h2>{e(p["tr"])}</h2><p class="la">{e(short_la(p))}</p>'
                f'<p class="guv {p["guv"]}">{GUV[p["guv"]]}</p></div></div><p>{e(bil)}</p>'
                f'<div class="kart-alt">{_qr(BASE + "/api/q/" + p["id"])}<p>Okut: geleneksel kullanımı, bilimsel kanıtı, güvenliği ve kaynakları.<br><b>bitkitabani.com/{p["id"]}/</b></p></div></article>')
    _KCSS = ('<style>.kartlar{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}.kart{border:1px solid #cfc4ae;border-radius:10px;padding:14px;background:#fbf7ee;color:#1c2140;break-inside:avoid;page-break-inside:avoid}'
             '.kart-ust{display:flex;gap:12px;align-items:center}.kart-ust img{width:96px;height:96px;object-fit:cover;border-radius:8px}.kart h2{margin:0;font-size:1.3rem}.kart .la{margin:2px 0;font-style:italic}.kart .guv{margin:0;font-size:.8rem}'
             '.kart-alt{display:flex;gap:12px;align-items:center;font-size:.8rem}.kart-alt svg{width:96px;height:96px;flex:none}'
             '@media print{header.site,nav,footer,.page-head,.noprint{display:none!important}body{background:#fff}.kartlar{grid-template-columns:1fr 1fr;gap:8mm}.kart{height:95mm;overflow:hidden}}</style>')
    _ks = ''.join(_kart(p) for p in P if p['guv'] != 'yuksek')
    write('/kartlar/index.html', page('Yazdırılabilir bitki kartları (QR kodlu) | Bitki Tabanı', 'Aktarlar, pazarlar ve atölyeler için QR kodlu, yazdırılabilir şifalı bitki kartları.', '/kartlar/',
          _KCSS + '<header class="page-head"><h1>Yazdırılabilir bitki kartları</h1><p>Aktar, pazar ve atölyeler için: her kartta bitkinin adı, güvenlik düzeyi, kısa bir bilgi ve okutunca sayfasına götüren bir QR kod var. Yazdır de; A4 sayfaya dört kart sığar. Yüksek riskli bitkiler bu listede yok.</p><p class="noprint"><button type="button" onclick="print()">Yazdır</button></p></header><div class="kartlar">' + _ks + '</div>', 'kat'))
# ---------- Kültür ve ritüel ana sayfası ----------
_kh = [('/kavram/', 'Kavramlar', 'Şamanizm, animizm, Pachamama, Hıdrellez… Her kavram bir bitkiyle, kaynaklarıyla.'),
       ('/semboller/', 'Semboller', 'Kilim motiflerinden Shipibo kené desenlerine: çizilebilir semboller ve anlamları.'),
       ('/kopruler/', 'Kültür köprüleri', 'Anadolu ile Amazon ve And’larda aynı işi gören bitkiler ve ritüeller, yan yana.'),
       ('/yazilar/', 'Yazılar', 'Şamanizmden kutsal ağaçlara, kaynaklı uzun okumalar.'),
       ('/takvim/', 'Ritüel takvimi', 'Nevruz, Hıdrellez, gündönümleri, Pachamama ayı: yılın dönüm noktaları ve bitkileri.')]
write('/kultur/', page('Kültür ve ritüel: şamanizm, animizm, semboller ve kutsal bitkiler | Bitki Tabanı',
      'Bitkilerin kültürel ve ritüel dünyası: şamanizm, animizm, doğa kültü, semboller, kültür köprüleri ve ritüel takvimi; kaynaklarıyla.', '/kultur/',
      f'''{crumbs(('/kultur/', 'Kültür ve ritüel'))}<header class="page-head"><span class="eyebrow">Kültür ve ritüel</span><h1>Bitkiler yalnızca ilaç değildir</h1>
<p>Anadolu’da ardıç dumanıyla arınılır, dut ağacına dilek bezi bağlanır; And’larda koka yaprağı toprak anaya sunulur, Amazon’da bazı bitkilerin öğretmen olduğuna inanılır. Bu bölüm, bitkilerin insanlarla kurduğu bu ilişkiyi, onu yaşatan toplulukların adıyla ve kaynaklarıyla anlatır. Ritüel kullanım önerisi değil, kültürel bir kayıttır.</p></header>
<ul class="guidelist">{"".join(f'<li><a href="{h}"><b>{l}</b></a><span>{d}</span></li>' for h, l, d in _kh)}</ul>
<section class="sec"><h2>Son yazılar</h2><ul class="otherlist">{"".join(f'<li><a href="/yazilar/{y["slug"]}/">{e(y["baslik"])}</a></li>' for y in YAZILAR)}</ul></section>''',
      'kultur', narrow=True, extra=lds(crumb_ld(('/kultur/', 'Kültür ve ritüel')))))
# ---------- akıllı arama verisi ve sayfası ----------
import hashlib as _hl
def _cumleler(p):   # aramada gösterilecek cümleler: (etiket, sayfadaki bölüm, cümle)
    out = []
    for w, t in p['kul']:
        out += [(f'Geleneksel kullanım · {w}', 'geleneksel-kullanim', c) for c in re.split(r'(?<=[.!?])\s+', t) if len(c) > 15]
    for lab, an, t in [('Bilim ne diyor', 'bilim-ne-diyor', p['bilim']), ('Güvenlik', 'guvenlik', p['guvNot']), ('Hazırlama', 'hazirlama', p['haz']),
                       ('Doğada', 'dogada', ' '.join(str(EK.get(p['id'], {}).get(x, '')) for x in ('yoresel', 'mevsim')))]:
        out += [(lab, an, c) for c in re.split(r'(?<=[.!?])\s+', t or '') if len(c) > 15]
    return [list(x) for x in out]
_ara = [dict(id=p['id'], tr=p['tr'], la=short_la(p), guv=GUV[p['guv']], kisa=p['kul'][0][1].split('. ')[0][:140], c=_cumleler(p),
             t=f"{p['tr']} ({p['la']}). Diğer adları: {p['diger']}. Kullanım: {', '.join(KAT[k] for k in p['kat'])}. " + ' '.join(f'{w}: {x}' for w, x in p['kul'])[:700] + f" Bilim: {p['bilim'][:300]} Güvenlik: {GUV[p['guv']]}. {p['guvNot'][:300]}") for p in P]
_ver = _hl.sha1(json.dumps([x['t'] for x in _ara], ensure_ascii=False).encode()).hexdigest()[:12]
open(os.path.join(OUT, 'ara.json'), 'w', encoding='utf-8').write(json.dumps({'ver': _ver, 'p': _ara}, ensure_ascii=False))
# ---------- okur katkıları onay sayfası (yalnızca site sahibi; dizine eklenmez) ----------
write('/katki-onay/index.html', page('Katkı onayı | Bitki Tabanı', 'Okur katkıları', '/katki-onay/',
      '<header class="page-head"><h1>Okur katkıları</h1><p>Site formundan ve Threads yanıtlarından gelen notlar. Onayladıkların bir sonraki derlemede bitki sayfasına “Okurlardan” başlığıyla eklenir. Görmek için <a href="/hesap/">Google ile giriş yap</a>.</p>'
      '<p><label><input type="checkbox" id="kSadece" checked> Yalnızca bekleyenler</label></p></header><div id="kListe">Yükleniyor…</div>',
      'kat', '<script src="/assets/katki-onay.js" defer></script>', extra='<meta name="robots" content="noindex">'))
# ---------- tanıma görselleri kontrol sayfası (dizine eklenmez) ----------
_rows = ''.join(f'<section class="sec"><h2><a href="/{p["id"]}/">{e(p["tr"])}</a> <small>{e(p["id"])}</small></h2>{tanima_html(p["id"], h2=False) or "<p>Görsel yok.</p>"}'
                + ''.join(f'<p class="muted-s">{TANIMA_AD[t]}: bulunamadı</p>' for t in ('cizim', 'cicek', 'kuru') if TANIMA.get(f'{p["id"]}:{t}') == 'yok') + '</section>' for p in P)
write('/tanima-kontrol/index.html', page('Tanıma görselleri kontrolü | Bitki Tabanı', 'Tanıma görselleri kontrol listesi', '/tanima-kontrol/',
      '<header class="page-head"><h1>Tanıma görselleri: kontrol</h1><p>Beğenmediğin görselin bitki kimliğini ve türünü (çizim, çiçek, kuru) Claude’a yaz; yenisiyle değiştirilir.</p></header>' + _rows,
      'kat', extra='<meta name="robots" content="noindex">'))
print('ok', len(urls), 'sayfa')

