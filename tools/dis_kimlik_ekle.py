"""dis_kimlik.csv'yi katalogla eşitler: yeni bitkilere dış kimlik arar.

Şemadaki `sameAs` bu dosyadan üretiliyor. Dosya elle doldurulduğu için, kuyruktan
her gece yeni bir bitki yayına girdiğinde o kayıt kimliksiz kalıyordu. Bu betik
katalogda olup dosyada olmayan (ya da kimliği eksik) kayıtlar için GBIF ve Wikidata'ya
bilimsel adla sorar; yalnızca kesin eşleşmeyi yazar, şüpheliyi boş bırakıp `not`a yazar.

    python3 tools/dis_kimlik_ekle.py            # eksikleri tamamla, CSV'yi güncelle
    python3 tools/dis_kimlik_ekle.py --rapor    # yalnızca rapor
"""
import os, sys, csv, json, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
CSV = os.path.join(ROOT, 'dis_kimlik.csv')
SUTUN = ['id', 'turkce_ad', 'eslesen_takson', 'wikidata_qid', 'powo_id', 'gbif_id', 'not']
UA = {'User-Agent': 'BitkiTabani/1.0 (https://bitkitabani.com; iletisim@bitkitabani.com)'}


def _json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.loads(r.read())


def gbif(ad):
    """GBIF tür eşleşmesi: yalnızca EXACT eşleşme kabul edilir."""
    try:
        j = _json('https://api.gbif.org/v1/species/match?strict=true&name=' + urllib.parse.quote(ad))
    except Exception as ex:
        print('  gbif hata:', str(ex)[:80]); return None, ''
    if j.get('matchType') == 'EXACT' and j.get('usageKey'):
        return str(j['usageKey']), (j.get('rank') or '').lower()
    return None, (j.get('matchType') or 'yok').lower()


def wikidata(ad):
    """Taksona göre Wikidata: P225 (taxon name) tam eşleşmesi aranır."""
    sorgu = ('SELECT ?x WHERE { ?x wdt:P225 "%s" } LIMIT 2' % ad.replace('"', ''))
    url = 'https://query.wikidata.org/sparql?format=json&query=' + urllib.parse.quote(sorgu)
    try:
        j = _json(url)
    except Exception as ex:
        print('  wikidata hata:', str(ex)[:80]); return None
    b = j.get('results', {}).get('bindings', [])
    if len(b) == 1:
        return b[0]['x']['value'].rsplit('/', 1)[-1]
    return None   # sıfır ya da birden çok aday: elle bakılsın


def main():
    rapor = '--rapor' in sys.argv
    rows = list(csv.DictReader(open(CSV, encoding='utf-8')))
    by = {r['id'].strip(): r for r in rows if r.get('id')}
    data = json.load(open(os.path.join(ROOT, '.cache', 'ig_input.json'), encoding='utf-8'))

    yeni, tamamlanan = [], []
    for p in data['p']:
        pid = p['id']
        r = by.get(pid)
        if r and (r.get('wikidata_qid') or '').strip() and (r.get('gbif_id') or '').strip(): continue
        ad = (r or {}).get('eslesen_takson', '').strip() or p['la'].split(',')[0].strip()
        if not r:
            r = {k: '' for k in SUTUN}; r['id'] = pid; r['turkce_ad'] = p['tr']; r['eslesen_takson'] = ad
            rows.append(r); by[pid] = r; yeni.append(pid)
        if rapor:
            tamamlanan.append(pid); print(f'eksik: {pid:18} {ad}'); continue
        print(f'{pid:18} {ad}')
        if not (r.get('wikidata_qid') or '').strip():
            q = wikidata(ad)
            if q: r['wikidata_qid'] = q; print('   wikidata', q)
        if not (r.get('gbif_id') or '').strip():
            g, rank = gbif(ad)
            if g: r['gbif_id'] = g; print('   gbif', g, rank)
            else: print('   gbif eşleşmedi:', rank)
        if not r.get('not'): r['not'] = 'kimlikler otomatik arandı'
        tamamlanan.append(pid)
        time.sleep(1.1)   # iki servise de nazik davran

    if rapor:
        print(f'\n{len(data["p"])} kayıt · kimliği eksik {len(yeni) + len(tamamlanan)}'); return 0
    if tamamlanan:
        with open(CSV, 'w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, SUTUN); w.writeheader()
            for r in rows: w.writerow({k: r.get(k, '') for k in SUTUN})
        print(f'\n{len(tamamlanan)} kayıt güncellendi ({len(yeni)} yeni satır):', ', '.join(tamamlanan))
    else:
        print('\neksik kimlik yok')
    return 0


if __name__ == '__main__':
    sys.exit(main())
