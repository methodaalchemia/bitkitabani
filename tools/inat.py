"""iNaturalist: her bitkinin Türkiye'deki araştırma kalitesindeki gözlemlerinin aylara dağılımı -> inat.json.
Derlemeden önce GitHub Actions'ta çalışır; 30 günde bir yenilenir. Bitki sayfasındaki 'Doğada' bölümüne bir satır ekler."""
import json, os, re, sys, time, datetime, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
OUT = os.path.join(ROOT, 'inat.json'); TR = 7183   # iNaturalist'te Türkiye
UA = {'User-Agent': 'BitkiTabani/1.0 (https://bitkitabani.com)'}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as r: return json.loads(r.read())
def main():
    from refs import POWO
    import kuyruk as K
    D = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
    old = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    bugun = datetime.date.today().isoformat(); n = 0
    for p in D['P'] + [q for q in K.Q if q['id'] not in {x['id'] for x in D['P']}]:
        o = old.get(p['id'])
        if o and (datetime.date.fromisoformat(bugun) - datetime.date.fromisoformat(o['at'])).days < 30: continue
        t = re.sub(r'\s+ve diğer.*$', '', (POWO.get(p['id']) or p.get('taxon') or p['la'].split(',')[0]).strip()).replace('× ', '')
        try:
            tx = get('https://api.inaturalist.org/v1/taxa?rank=species,hybrid,genus&per_page=1&q=' + urllib.parse.quote(t))['results']
            if not tx or tx[0]['name'].lower() != t.lower(): old[p['id']] = {'at': bugun, 'yok': True}; continue
            h = get(f'https://api.inaturalist.org/v1/observations/histogram?taxon_id={tx[0]["id"]}&place_id={TR}&quality_grade=research&date_field=observed&interval=month_of_year')
            ay = [h['results']['month_of_year'].get(str(m), 0) for m in range(1, 13)]
            old[p['id']] = {'at': bugun, 'taxon_id': tx[0]['id'], 'ay': ay, 'toplam': sum(ay)}; n += 1
        except Exception as e: print('inat', p['id'], str(e)[:80])
        time.sleep(1.1)   # iNaturalist: saniyede ~1 istek
    json.dump(old, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
    print('inat: güncellenen', n)
if __name__ == '__main__': main()
