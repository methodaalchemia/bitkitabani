# Yeni ve değişen sayfaları IndexNow ile Bing, Yandex ve diğer katılımcı arama motorlarına bildirir.
# ALL=1 verilirse site haritasındaki bütün adresler gönderilir (ilk kurulumda bir kez).
import json, os, re, urllib.request
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(HERE, '.cache', 'indexnow.json')))
urls = d['urls']
if os.environ.get('ALL') == '1':
    urls = re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(HERE, 'site', 'sitemap.xml'), encoding='utf-8').read())
body = json.dumps({'host': 'bitkitabani.com', 'key': d['key'], 'keyLocation': f'https://bitkitabani.com/{d["key"]}.txt', 'urlList': urls[:10000]}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    with urllib.request.urlopen(req, timeout=30) as r: print('IndexNow', r.status, len(urls), 'adres')
except urllib.error.HTTPError as e:
    print('IndexNow hata', e.code, e.read()[:300])
