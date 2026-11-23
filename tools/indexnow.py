# Yeni ve değişen sayfaları IndexNow ile Bing, Yandex ve diğer katılımcı arama motorlarına bildirir.
# ALL=1 verilirse site haritasındaki bütün adresler gönderilir (ilk kurulumda bir kez).
import json, os, re, urllib.request
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(HERE, '.cache', 'indexnow.json')))
urls = d['urls']
# 23 Kasım: kapsam genişledi. Derlemenin verdiği günlük liste (bugünün bitkisi ve sabit sayfalar) yetmiyordu:
# yeni karşılaştırma, tarif, İngilizce sayfa ya da açıklaması değişen bitki hiç bildirilmiyordu.
# Artık bu koşunun yayımladığı farkta değişen her sayfa da gönderiliyor (önceki tepe → şimdiki tepe).
import subprocess
def _git(*a): return subprocess.run(['git', *a], cwd=HERE, capture_output=True, text=True).stdout.strip()
once = os.environ.get('ONCE', '')
if not once or set(once) == {'0'} or not _git('cat-file', '-t', once): once = 'HEAD~1'
degisen = [f for f in _git('diff', '--name-only', once, 'HEAD', '--', 'site').splitlines() if f.endswith('index.html')]
yol = lambda f: '/' + f[len('site/'):-len('index.html')]
urls = sorted(set(urls) | {'https://bitkitabani.com' + yol(f) for f in degisen if not yol(f).startswith(('/404', '/kartlar/', '/hesap/', '/katki-onay/'))})
print('değişen sayfa', len(degisen), '·', once[:7], '→ HEAD')
if os.environ.get('ALL') == '1':
    urls = re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(HERE, 'site', 'sitemap.xml'), encoding='utf-8').read())
body = json.dumps({'host': 'bitkitabani.com', 'key': d['key'], 'keyLocation': f'https://bitkitabani.com/{d["key"]}.txt', 'urlList': urls[:10000]}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    with urllib.request.urlopen(req, timeout=30) as r: print('IndexNow', r.status, len(urls), 'adres')
except urllib.error.HTTPError as e:
    print('IndexNow hata', e.code, e.read()[:300])
