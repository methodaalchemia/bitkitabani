#!/usr/bin/env python3
"""Bir parti bitki için görsel adaylarını tek bir HTML sayfasında toplar.

Neden var (25 Kasım 2026): kayıt başına en pahalı adım görsel seçimiydi —
küçük resimleri indirip kontak sayfası yapıp bakmak, ölçülen 45.000 tokenın
yaklaşık üçte biri. Seçimi insan yaparsa o maliyet sıfıra iner.

Betik Commons ve iNaturalist'te yalnız serbest lisanslı (CC0 / CC BY / CC BY-SA)
fotoğrafları arar, küçük resimleri sayfaya gömer ve her adaya bir numara verir.
Bakan kişi "yabanihunnap: 3" der, numaralar refs.py'ye yazılır.

  python3 tools/gorsel_adaylari.py p005
  python3 tools/gorsel_adaylari.py --tek yerbademi "Cyperus esculentus"

Çıktı: /tmp/.../gorsel_adaylari.html (Artifact ile yayımlanır).
"""
import base64, html, io, json, os, re, subprocess, sys, urllib.parse

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = 'BitkiTabani/1.0 (https://bitkitabani.com; iletisim@bitkitabani.com)'
SERBEST = {'cc0', 'cc-by', 'cc-by-sa'}


def al(adres, deneme=4):
    """Commons ve iNaturalist hızlı art arda sorguda 429 veriyor; aralık açarak dener."""
    import time
    for i in range(deneme):
        r = subprocess.run(['curl', '-sL', '-m', '60', '-A', UA, adres],
                           capture_output=True, text=True, errors='replace')
        try:
            d = json.loads(r.stdout)
            if d and not d.get('error'): return d
        except Exception:
            pass
        time.sleep(4 * (i + 1))
    return None


def indir(adres):
    r = subprocess.run(['curl', '-sL', '-m', '60', '-A', UA, adres], capture_output=True)
    return r.stdout if r.stdout[:3] in (b'\xff\xd8\xff', b'\x89PN', b'RIF') else None


def commons(latin, adet=14):
    d = al('https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search'
           f'&gsrnamespace=6&gsrlimit={adet}&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=240'
           '&gsrsearch=' + urllib.parse.quote(latin))
    out = []
    for v in ((d or {}).get('query') or {}).get('pages', {}).values():
        ii = (v.get('imageinfo') or [{}])[0]
        em = ii.get('extmetadata') or {}
        lis = (em.get('LicenseShortName') or {}).get('value', '')
        if 'NC' in lis or 'ND' in lis: continue       # ticari olmayan / türetilemez alınmaz
        out.append({'kaynak': 'Commons', 'dosya': v['title'][5:],
                    'kucuk': ii.get('thumburl'), 'lisans': lis,
                    # 26 Kasım 2026: kart çözünürlük göstermediği için p008'de
                    # limon mersinine 448x256 bir dosya seçildi; site 500/960/1280
                    # kopya üretiyor, o kaynak en küçüğünü bile doldurmuyor.
                    'en': ii.get('width') or 0, 'boy': ii.get('height') or 0,
                    # Commons yazar alanı HTML döndürüyor (<a href=...>); etiketler
                    # ayıklanmazsa künyeye ham işaretleme giriyor.
                    'yazar': html.unescape(re.sub(r'<[^>]+>', '',
                             (em.get('Artist') or {}).get('value', '') or '')).strip()[:80],
                    'sayfa': ii.get('descriptionurl', '')})
    return out


def inat(latin, adet=10):
    d = al('https://api.inaturalist.org/v1/observations?per_page=%d&photo_license=%s&taxon_name=%s'
           % (adet, 'cc0,cc-by,cc-by-sa', urllib.parse.quote(latin)))
    out = []
    for o in (d or {}).get('results', []):
        ph = (o.get('photos') or [{}])[0]
        if (ph.get('license_code') or '') not in SERBEST: continue
        out.append({'kaynak': 'iNaturalist', 'dosya': str(ph.get('id')),
                    'en': 0, 'boy': 0,       # iNaturalist bu uçta boyut vermiyor
                    'kucuk': (ph.get('url') or '').replace('square', 'small'),
                    'lisans': (ph.get('license_code') or '').upper(),
                    'yazar': (ph.get('attribution') or '')[:80],
                    'sayfa': f"https://www.inaturalist.org/observations/{o['id']}",
                    'tam': (ph.get('url') or '').replace('square', 'original')})
    return out


# Latince ad tek başına işe yaramayan kayıtlar. Spirulina mikroskobik bir
# siyanobakteri: gözle görülecek bir bitkisi yok, tür adıyla arayınca da
# neredeyse hiçbir şey çıkmıyor. Böyle kayıtlarda neyin fotoğraflanabileceği
# elle yazılır — üretim havuzu, mikroskop görüntüsü, kurutulmuş hâli.
EK_TERIM = {
    'spirulina': ['Spirulina microscope', 'Arthrospira', 'Spirulina powder',
                  'Spirulina cultivation pond', 'Spirulina harvest'],
    # 26 Kasım 2026: p008'de Eucalyptus citriodora yalnız 10 aday verdi ve
    # hiçbiri işe yaramadı. Sebep ad: Commons dosyaları büyük ölçüde kabul
    # edilen ad (Corymbia citriodora) altında duruyor.
    'limonokaliptusu': ['Corymbia citriodora', 'Corymbia citriodora leaves',
                        'Corymbia citriodora bark', 'Corymbia citriodora tree',
                        'lemon scented gum', 'Corymbia citriodora flowers'],
}


def kart(a, n, pid):
    """Tek aday kartı.

    Küçük resim sayfaya gömülüyor: Artifact'in içerik güvenlik kuralı dış
    adreslerden resim çekmeye izin vermiyor, uzaktan bağlanan her kare boş
    çıkıyor. Bu yüzden 240 piksellik küçük kopyalar base64 olarak gömülü.
    """
    ham = indir(a['kucuk']) if a.get('kucuk') else None
    if not ham: return ''
    b64 = base64.b64encode(ham).decode()
    return (f'<button type="button" class="ad" data-pid="{html.escape(pid)}" data-no="{n}">'
            f'<span class="no">{n}</span>'
            f'<img src="data:image/jpeg;base64,{b64}" alt="" loading="lazy">'
            f'<span class="alt"><b>{html.escape(a["kaynak"])}</b> · {html.escape(a["lisans"])}'
            f'{olcu(a)}<br>'
            f'{html.escape(a["yazar"])}</span></button>')


def olcu(a):
    """Çözünürlüğü karta yazar; 1280 pikseli doldurmayanı uyarıyla işaretler."""
    en, boy = a.get('en') or 0, a.get('boy') or 0
    if not en or not boy: return ''
    kucuk = ' ⚠ küçük' if max(en, boy) < 1280 else ''
    return f' · {en}×{boy}{kucuk}'


def sayfa(gruplar):
    g, veri = [], {}
    for pid, latin, adaylar in gruplar:
        kartlar = []
        veri[pid] = {}
        for n, a in enumerate(adaylar, 1):
            k = kart(a, n, pid)
            if not k: continue
            kartlar.append(k)
            veri[pid][str(n)] = a
        g.append(f'<section id="b-{html.escape(pid)}"><h2>{html.escape(pid)}'
                 f'<em>{html.escape(latin)}</em>'
                 f'<span class="durum" data-for="{html.escape(pid)}">seçilmedi</span></h2>'
                 f'<div class="grid">{"".join(kartlar)}</div></section>')
    j = json.dumps(veri, ensure_ascii=False).replace('<', '\\u003c')
    return ('<script type="application/json" id="veri">' + j + '</script>') + ''.join(g)


ŞABLON = """<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Görsel Adayları</title><style>
:root{--bg:#fbfaf7;--fg:#211d17;--ln:#ddd6c7;--mut:#6b6354;--ac:#5d6f3f;--card:#fff}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17150f;--fg:#ece6d8;--ln:#39342a;--mut:#9c9382;--ac:#a8c47c;--card:#1f1c15}}
:root[data-theme="dark"]{--bg:#17150f;--fg:#ece6d8;--ln:#39342a;--mut:#9c9382;--ac:#a8c47c;--card:#1f1c15}
*{box-sizing:border-box}
body{margin:0;padding:0 16px 80px;background:var(--bg);color:var(--fg);
font:16px/1.55 ui-serif,Georgia,serif;-webkit-text-size-adjust:100%}
header{max-width:1100px;margin:0 auto;padding:40px 0 14px;border-bottom:1px solid var(--ln)}
h1{font-size:1.65rem;margin:0 0 8px;letter-spacing:-.01em}
p.lead{color:var(--mut);margin:0;font-size:.95rem;max-width:62ch}
#bilgi{max-width:1100px;margin:14px auto 0;padding:10px 12px;border:1px solid var(--ln);
border-radius:8px;font:13px/1.5 ui-sans-serif,system-ui;color:var(--mut);background:var(--card)}
section{max-width:1100px;margin:0 auto;padding:26px 0;border-bottom:1px solid var(--ln)}
h2{font-size:1.1rem;margin:0 0 14px;display:flex;flex-wrap:wrap;gap:10px;align-items:baseline}
h2 em{font-style:italic;font-weight:400;color:var(--mut);font-size:.9rem}
.durum{font:600 12px/1 ui-sans-serif,system-ui;color:var(--mut);border:1px solid var(--ln);
padding:5px 8px;border-radius:20px}
.durum.var{color:var(--ac);border-color:var(--ac)}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}
button.ad{all:unset;cursor:pointer;display:block;border:2px solid var(--ln);border-radius:9px;
overflow:hidden;position:relative;background:var(--card)}
button.ad:focus-visible{outline:3px solid var(--ac);outline-offset:2px}
button.ad img{display:block;width:100%;height:180px;object-fit:cover}
button.ad .no{position:absolute;top:8px;left:8px;background:rgba(0,0,0,.72);color:#fff;
font:600 13px/1 ui-sans-serif,system-ui;padding:6px 9px;border-radius:5px}
button.ad .alt{display:block;padding:8px 10px;font:12px/1.45 ui-sans-serif,system-ui;color:var(--mut);
word-break:break-word}
button.ad[aria-pressed="true"]{border-color:var(--ac)}
button.ad[aria-pressed="true"] .no{background:var(--ac)}
button.ad[aria-pressed="true"]::after{content:"seçildi";position:absolute;top:8px;right:8px;
background:var(--ac);color:#fff;font:600 12px/1 ui-sans-serif,system-ui;padding:6px 9px;border-radius:5px}
@media(max-width:560px){button.ad img{height:150px}}
</style></head><body>
<header><h1>Görsel adayları</h1>
<p class="lead">Her bitki için serbest lisanslı adaylar. Beğendiğine dokun, seçim kaydedilir &mdash;
geri yazmana gerek yok. Aynı bitkide başka birine dokunursan seçim değişir,
seçilene tekrar dokunursan kalkar. Yalnız CC0, CC BY ve CC BY-SA var.</p>
<div id="bilgi">bağlanıyor&hellip;</div></header>
__ICERIK__
<script>
(function(){
var veri={};try{veri=JSON.parse(document.getElementById('veri').textContent)}catch(e){}
var bilgi=document.getElementById('bilgi');
function durumYaz(pid,no){
  var d=document.querySelector('.durum[data-for="'+CSS.escape(pid)+'"]');
  if(d){d.textContent=no?('seçildi: '+no):'seçilmedi';d.classList.toggle('var',!!no)}
  document.querySelectorAll('button.ad[data-pid="'+CSS.escape(pid)+'"]').forEach(function(b){
    b.setAttribute('aria-pressed',b.dataset.no===String(no)?'true':'false')})}
Object.keys(veri).forEach(function(p){durumYaz(p,null)});
var zaman=setTimeout(function(){bilgi.textContent='Kayıt bağlantısı kurulamadı — seçim saklanamaz. Sayfayı Claude içinde açtığından emin ol.'},10000);
claude.use('db').then(function(db){
  clearTimeout(zaman);
  if(!db){bilgi.textContent='Kayıt bağlantısı yok (oturum açık mı?) — seçim saklanamaz.';return}
  bilgi.textContent='Seçimler kaydediliyor. İşin bitince Claude’a “seçimler hazır” demen yeter.';
  var kol=db.collection('secimler');
  kol.onSnapshot(function(snap){
    var gelen={};snap.docs.forEach(function(d){gelen[d.id]=d.data()&&d.data().no});
    Object.keys(veri).forEach(function(p){durumYaz(p,gelen[p]||null)})});
  document.addEventListener('click',function(ev){
    var b=ev.target.closest('button.ad');if(!b)return;
    var pid=b.dataset.pid,no=b.dataset.no;
    var secili=b.getAttribute('aria-pressed')==='true';
    if(secili){kol.doc(pid).delete();durumYaz(pid,null);return}
    var a=(veri[pid]||{})[no]||{};
    kol.doc(pid).set({no:no,kaynak:a.kaynak||'',dosya:a.dosya||'',lisans:a.lisans||'',
      yazar:a.yazar||'',sayfa:a.sayfa||'',tam:a.tam||''});
    durumYaz(pid,no)})},
function(){clearTimeout(zaman);bilgi.textContent='Kayıt bağlantısı kurulamadı — seçim saklanamaz.'});
})();
</script>
</body></html>"""


def uret(cift, cikti):
    gruplar = []
    for pid, latin in cift:
        import time
        a = commons(latin) + inat(latin)
        for t in EK_TERIM.get(pid, []):
            a += commons(t, adet=6)
            time.sleep(1)
        gorulen, tekil = set(), []
        for x in a:                       # aynı dosya iki aramadan da gelebilir
            if x['dosya'] in gorulen: continue
            gorulen.add(x['dosya']); tekil.append(x)
        a = tekil
        gruplar.append((pid, latin, a))
        print(f'{pid}: {len(a)} aday')
        time.sleep(2)
    io.open(cikti, 'w', encoding='utf-8').write(ŞABLON.replace('__ICERIK__', sayfa(gruplar)))
    print('yazıldı:', cikti, os.path.getsize(cikti) // 1024, 'KB')


if __name__ == '__main__':
    cikti = os.environ.get('CIKTI', '/tmp/claude-0/gorsel_adaylari.html')
    if len(sys.argv) > 3 and sys.argv[1] == '--tek':
        uret([(sys.argv[2], ' '.join(sys.argv[3:]))], cikti)
    elif len(sys.argv) > 1:
        f = os.path.join(KOK, 'veri', 'parti', sys.argv[1] + '.txt')
        c = []
        for s in open(f, encoding='utf-8'):
            if s.startswith('#') or '|' not in s: continue
            p = [x.strip() for x in s.split('|')]
            c.append((p[0], p[1]))
        uret(c, cikti)
    else:
        print(__doc__)
