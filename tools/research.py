"""Araştırma yardımcısı (GitHub Actions'ta çalışır): tools/research.txt içindeki
'id | pubmed sorgusu' satırları için PubMed'den ilk sonuçları, 'URL <adres>' satırları için
HTTP durumunu toplar ve research/sonuc.json dosyasına yazar."""
import json, os, time, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = 'BitkiTabani/1.0 (https://bitkitabani.com; research)'
def get(url, raw=False):
    for a in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                b = r.read(); return (r.status, b) if raw else json.loads(b)
        except urllib.error.HTTPError as e:
            if raw: return (e.code, b'')
            time.sleep(2)
        except Exception as e:
            time.sleep(2)
    return (0, b'') if raw else {}
E = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
out = {'pubmed': {}, 'urls': {}}
for line in open(os.path.join(ROOT, 'tools', 'research.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    if line.startswith('URL '):
        u = line[4:].strip(); st, b = get(u, raw=True)
        t = ''
        try:
            s = b.decode('utf-8', 'ignore'); i = s.find('<title'); t = s[s.find('>', i)+1:s.find('</title>')].strip()[:160] if i > -1 else ''
        except Exception: pass
        out['urls'][u] = [st, t]; time.sleep(0.5); continue
    pid, q = [x.strip() for x in line.split('|', 1)]
    r = get(E + 'esearch.fcgi?db=pubmed&retmode=json&retmax=6&sort=relevance&term=' + urllib.parse.quote(q))
    ids = r.get('esearchresult', {}).get('idlist', [])
    res = []
    if ids:
        s = get(E + 'esummary.fcgi?db=pubmed&retmode=json&id=' + ','.join(ids))
        for i in ids:
            d = s.get('result', {}).get(i, {})
            pmc = next((a['value'] for a in d.get('articleids', []) if a.get('idtype') == 'pmc'), '')
            res.append([i, d.get('title', ''), d.get('source', ''), d.get('pubdate', '')[:4], ','.join(d.get('pubtype', [])), pmc])
    out['pubmed'].setdefault(pid, []).append([q, res]); time.sleep(0.4)
os.makedirs(os.path.join(ROOT, 'research'), exist_ok=True)
json.dump(out, open(os.path.join(ROOT, 'research', 'sonuc.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('tamam', len(out['pubmed']), len(out['urls']))
