# Haftalık site sağlık kontrolü: kırık iç bağlantılar, bozuk yapılandırılmış veri, açılmayan kaynak bağlantıları ve eksik fotoğraflar.
# Sorun bulursa rapor.md yazar ve 1 ile çıkar (iş akışı bu raporla bir GitHub "issue" açar).
import os, re, json, sys, urllib.request, urllib.parse, concurrent.futures
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(HERE, 'site')
ic, dis, ld, img = set(), {}, [], []
for dp, _, fs in os.walk(S):
    for f in fs:
        if not f.endswith('.html'): continue
        rel = os.path.relpath(os.path.join(dp, f), S); t = open(os.path.join(dp, f), encoding='utf-8').read()
        for m in re.findall(r'(?:href|src)="(/[^"#?]*)', t):
            p = S + m + ('index.html' if m.endswith('/') else '')
            if not (os.path.exists(p) or os.path.exists(p + '.html') or os.path.exists(p.rstrip('/') + '/index.html')): ic.add((m, rel))
        for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            try: json.loads(j)
            except Exception as e: ld.append((rel, str(e)[:80]))
        for u in re.findall(r'<a href="(https?://[^"]+)" target="_blank" rel="noopener">', t):   # kaynak bağlantıları
            if not re.search(r'bitkitabani\.com|commons\.wikimedia\.org|creativecommons\.org|gnu\.org|artlibre\.org', u): dis.setdefault(u, rel)   # fotoğraf lisans bağlantıları hariç
for f in os.listdir(os.path.join(S, 'img')) if os.path.isdir(os.path.join(S, 'img')) else []:
    if f.startswith('imza-'): continue   # e-posta imzası grafikleri: küçük olmaları normal
    if os.path.getsize(os.path.join(S, 'img', f)) < 2000: img.append(f)
def check(u):
    q = urllib.parse.quote(u, safe=":/?#[]@!$&'()*+,;=%~")   # tırnak gibi ASCII dışı karakterli adresler istek kuralına uymuyor
    for method in ('HEAD', 'GET'):
        try:
            r = urllib.request.urlopen(urllib.request.Request(q, method=method, headers={'User-Agent': 'Mozilla/5.0 (BitkiTabani link check)'}), timeout=25)
            return u, r.status
        except urllib.error.HTTPError as e:
            if method == 'GET' or e.code not in (403, 405, 429): return u, e.code
        except Exception as e:
            if method == 'GET': return u, str(e)[:60]
    return u, 'bilinmiyor'
bad_ext, gecici = [], []
def _gecici(st):   # sunucu hatası ya da bağlantı sorunu: adres kırık değil, karşı taraf o an cevap vermiyor
    if isinstance(st, int): return st >= 500
    return bool(re.search(r'CERTIFICATE_VERIFY_FAILED|timed out|timeout|Connection reset|Remote end closed|temporary failure', str(st), re.I))
with concurrent.futures.ThreadPoolExecutor(12) as ex:
    for u, st in ex.map(check, sorted(dis)):
        if (isinstance(st, int) and st < 400) or st in (403, 429): continue   # 403/429: bot engeli, kırık sayılmaz
        (gecici if _gecici(st) else bad_ext).append((u, st, dis[u]))
lines = []
# yayın kuyruğu: yeni bitkiler 10 günden az yetecekse uyar
import datetime
sys.path.insert(0, HERE); import kuyruk as _K
_son = max((datetime.date.fromisoformat(q['yayin']) for q in _K.Q), default=datetime.date.today())
_gun = (_son - datetime.date.today()).days
if _gun < 10: lines += ['## Yayın kuyruğu azaldı', '', f'- Son yeni bitki {_son.isoformat()} tarihinde yayımlanacak ({max(0, _gun)} gün kaldı). Claude’dan kuyruğa yeni bitki eklemesini isteyin.', '']
if ic: lines += ['## Kırık iç bağlantılar', ''] + [f'- `{m}` ← {r}' for m, r in sorted(ic)[:100]] + ['']
if ld: lines += ['## Bozuk yapılandırılmış veri', ''] + [f'- {r}: {e}' for r, e in ld[:50]] + ['']
if bad_ext: lines += ['## Açılmayan kaynak bağlantıları', ''] + [f'- {u} → {st} (ör. {r})' for u, st, r in bad_ext[:100]] + ['']
if gecici: lines += ['## Geçici olabilir (sunucu hatası ya da bağlantı sorunu)', '', 'Adres kırık değil; karşı taraf kontrol anında cevap vermedi. Üst üste birkaç hafta görünürse kaynağı değiştirin.', ''] + [f'- {u} → {st} (ör. {r})' for u, st, r in gecici[:50]] + ['']
if img: lines += ['## Bozuk görünen fotoğraflar', ''] + [f'- {f}' for f in img[:50]] + ['']
print(f'{len(dis)} kaynak bağlantısı kontrol edildi; iç: {len(ic)}, veri: {len(ld)}, kaynak: {len(bad_ext)}, geçici: {len(gecici)}, foto: {len(img)}')
if lines:
    open(os.path.join(HERE, 'rapor.md'), 'w', encoding='utf-8').write('Haftalık kontrolde şu sorunlar bulundu. Claude bir sonraki oturumda bunları düzeltebilir.\n\n' + '\n'.join(lines))
    if ic or ld or bad_ext or img: sys.exit(1)   # yalnızca geçici sunucu hatası varsa iş akışı kırılmasın
