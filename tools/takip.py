"""Haftalık yeni yayın takibi. Bulduğu varsa takip.md yazar; iş akışı bunu bir GitHub kaydı (issue) olarak açar.
- PubMed: son 7 günde eklenen, bitkilerimizden birinin Latince adını başlık/özette geçiren derleme, meta-analiz,
  randomize çalışma ve etnobotanik makaleler.
- Lokman Hekim Dergisi: arşivde daha önce görülmemiş makaleler (görülenler tools/takip_durum.json'da)."""
import json, os, re, sys, time, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
DURUM = os.path.join(ROOT, 'tools', 'takip_durum.json')
UA = {'User-Agent': 'BitkiTabani/1.0 (https://bitkitabani.com; literature watch)'}
EU = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

def get(url, js=True):
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r: d = r.read()
            return json.loads(d) if js else d.decode('utf-8', 'replace')
        except Exception as e:
            time.sleep(3 * (a + 1)); err = e
    raise err

def taksonlar():
    from refs import POWO
    import kuyruk as K
    D = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
    out = {}
    for p in D['P'] + [q for q in K.Q if q['id'] not in {x['id'] for x in D['P']}]:
        t = re.sub(r'\s+ve diğer.*$', '', (POWO.get(p['id']) or p.get('taxon') or p['la'].split(',')[0]).strip()).replace('× ', '')
        if ' ' in t: out[p['id']] = (p['tr'], t)
    return out

def pubmed(tx):
    sonuc = []
    for pid, (tr, t) in tx.items():
        q = f'"{t}"[Title/Abstract] AND (review[pt] OR meta-analysis[pt] OR randomized controlled trial[pt] OR systematic review[pt] OR ethnobotan*[Title/Abstract] OR ethnopharmacolog*[Title/Abstract])'
        try:
            r = get(EU + 'esearch.fcgi?db=pubmed&retmode=json&datetype=edat&reldate=7&retmax=5&term=' + urllib.parse.quote(q))
            ids = r.get('esearchresult', {}).get('idlist', [])
            if ids:
                s = get(EU + 'esummary.fcgi?db=pubmed&retmode=json&id=' + ','.join(ids))['result']
                for i in ids:
                    x = s.get(i, {}); sonuc.append((tr, pid, x.get('title', '').rstrip('.'), x.get('fulljournalname') or x.get('source', ''), ', '.join(pt for pt in x.get('pubtype', []) if pt != 'Journal Article'), i))
        except Exception as e: print('pubmed hata', pid, str(e)[:80])
        time.sleep(0.4)
    return sonuc

def turkiye(durum):
    """Türkiye/Anadolu halk hekimliği ve etnobotanik: PubMed (son 7 gün) + DergiPark araması (yeni olanlar)."""
    out = []
    q = '((ethnobotan*[Title/Abstract] OR "folk medicine"[Title/Abstract] OR "traditional medicine"[Title/Abstract] OR "folk medicinal"[Title/Abstract] OR "medicinal plants"[Title/Abstract]) AND (Turkey[Title/Abstract] OR Türkiye[Title/Abstract] OR Turkiye[Title/Abstract] OR Anatolia*[Title/Abstract]))'
    try:
        r = get(EU + 'esearch.fcgi?db=pubmed&retmode=json&datetype=edat&reldate=7&retmax=15&term=' + urllib.parse.quote(q))
        ids = r.get('esearchresult', {}).get('idlist', [])
        if ids:
            sm = get(EU + 'esummary.fcgi?db=pubmed&retmode=json&id=' + ','.join(ids))['result']
            for i in ids: x = sm.get(i, {}); out.append((x.get('title', '').rstrip('.'), 'https://pubmed.ncbi.nlm.nih.gov/' + i + '/', x.get('fulljournalname') or x.get('source', '')))
    except Exception as e: print('pubmed tr hata', str(e)[:80])
    seen = set(durum.get('dp', [])); ilk = 'dp' not in durum; dp = []
    for t in ('etnobotanik', 'halk ilacı', 'halk hekimliği bitki', 'Anadolu tıbbi bitkiler'):
        try:
            h = get('https://dergipark.org.tr/tr/search?q=' + urllib.parse.quote(t) + '&section=articles&sortBy=newest', js=False)
            for url, ttl in re.findall(r'href="(https://dergipark\.org\.tr/tr/(?:pub/[\w-]+/)?(?:issue/\d+/)?article/\d+)"[^>]*>\s*([^<]{15,300}?)\s*<', h)[:15]:
                if url not in seen: seen.add(url); dp.append((re.sub(r'\s+', ' ', ttl).strip(), url, 'DergiPark'))
        except Exception as e: print('dergipark hata', t, str(e)[:80])
        time.sleep(1)
    durum['dp'] = sorted(seen)[-3000:]
    return out + ([] if ilk else dp)

def lokman(durum):
    h = get('https://dergipark.org.tr/tr/pub/mutftd/archive', js=False)
    son = re.findall(r'/tr/pub/mutftd/issue/(\d+)', h)[:2]   # en yeni iki sayı
    seen = set(durum.get('lokman', [])); yeni = []
    for iss in son:
        t = get('https://dergipark.org.tr/tr/pub/mutftd/issue/' + iss, js=False)
        for aid, ttl in re.findall(r'href="https://dergipark\.org\.tr/tr/pub/mutftd/(?:issue/\d+/)?article/(\d+)"[^>]*>\s*([^<]{15,300}?)\s*<', t):
            if aid not in seen: seen.add(aid); yeni.append((aid, re.sub(r'\s+', ' ', ttl).strip()))
    ilk = 'lokman' not in durum
    durum['lokman'] = sorted(seen)
    return [] if ilk else yeni   # ilk çalıştırmada yalnızca mevcutları kaydeder

def main():
    durum = json.load(open(DURUM, encoding='utf-8')) if os.path.exists(DURUM) else {}
    tx = taksonlar(); pm = pubmed(tx)
    try: lh = lokman(durum)
    except Exception as e: lh = []; print('lokman hata', str(e)[:100])
    try: tr_ = turkiye(durum)
    except Exception as e: tr_ = []; print('türkiye hata', str(e)[:100])
    json.dump(durum, open(DURUM, 'w', encoding='utf-8'), ensure_ascii=False)
    L = []
    if lh: L += ['## Lokman Hekim Dergisi: yeni makaleler', ''] + [f'- [{t}](https://dergipark.org.tr/tr/pub/mutftd/article/{a})' for a, t in lh] + ['']
    if tr_: L += ['## Türkiye ve Anadolu: halk hekimliği ve etnobotanik (yeni)', ''] + [f'- [{t}]({u}) · {j}' for t, u, j in tr_] + ['']
    if pm: L += ['## PubMed: bitkilerimizle ilgili yeni derleme ve çalışmalar (son 7 gün)', ''] + [f'- **{tr}**: [{ttl}](https://pubmed.ncbi.nlm.nih.gov/{i}/) · {j}' + (f' · {pt}' if pt else '') for tr, pid, ttl, j, pt, i in pm] + ['']
    print(f'pubmed {len(pm)}, lokman {len(lh)}, türkiye {len(tr_)}')
    if L:
        open(os.path.join(ROOT, 'takip.md'), 'w', encoding='utf-8').write('Bu hafta bitkilerimizle ilgili yeni yayınlar. Claude’dan “takip kaydını işle” diyerek ilgili olanları siteye ve postlara eklemesini isteyebilirsiniz.\n\n' + '\n'.join(L))

if __name__ == '__main__':
    main()
