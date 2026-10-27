"""Çizim serisi taraması: Köhler/Thomé'de aynı türü olmayan bitkiler için başka tarihî çizim serilerinde aynı türün levhası var mı?
GitHub Actions'ta elle çalıştırılır (Seri taraması iş akışı); sonuç seri_tara.json ve günlüğe yazılır."""
import json, os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tanima as T

SERILER = [   # ad, arama eki, metinde aranacak ifade
 ('Köhler', 'intitle:"Medizinal-Pflanzen"', r'medizinal-pflanzen'),
 ('Thomé', 'Thomé', r'thom[ée]|flora von deutschland'),
 ('Bentley & Trimen', 'Bentley Trimen "Medicinal plants"', r'bentley|trimen'),
 ('Flora Graeca', '"Flora Graeca"', r'flora graeca|sibthorp'),
 ('Flora Peruviana', '"Flora Peruviana"', r'flora peruviana|ruiz|pav[óo]n'),
 ('Flora Brasiliensis', '"Flora Brasiliensis"', r'flora brasiliensis|martius'),
 ('Curtis', '"Botanical Magazine"', r"botanical magazine|curtis"),
 ('Medical Botany', '"Medical Botany"', r'medical botany|woodville|churchill|stephenson'),
 ('Flora de Filipinas', '"Flora de Filipinas"', r'flora de filipinas|blanco'),
 ('Sturm', 'Sturm "Deutschlands Flora"', r'deutschlands flora|sturm'),
 ('Lindman', 'Lindman "Nordens Flora"', r'nordens flora|lindman'),
 ('Plantae Asiaticae / Roxburgh', 'Roxburgh "Plants of the Coast of Coromandel"', r'roxburgh|coromandel'),
 ('Jacquin', 'Jacquin', r'jacquin'),
]

def ara(taxon, ek, need):
    url = ('https://commons.wikimedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=6&gsrlimit=15&gsrsearch='
           + urllib.parse.quote('"' + taxon + '" ' + ek) + '&prop=imageinfo&iiprop=extmetadata&iiextmetadatafilter=Categories|ImageDescription|ObjectName')
    pages = sorted(T.get(url).get('query', {}).get('pages', {}).values(), key=lambda x: x.get('index', 99))
    t = taxon.lower()
    for pg in pages:
        ii = (pg.get('imageinfo') or [{}])[0]; m = ii.get('extmetadata', {})
        text = ' '.join([pg['title'], m.get('ObjectName', {}).get('value', ''), m.get('Categories', {}).get('value', ''), T.plain(m.get('ImageDescription', {}).get('value', ''))]).lower()
        if t in text and re.search(need, text) and not re.search(r'herbari|specimen|photo|stamp', pg['title'].lower()):
            return pg['title'][5:]
    return None

def main():
    from refs import POWO
    import kuyruk as K
    D = json.load(open(os.path.join(T.ROOT, 'data.json'), encoding='utf-8'))
    for q in K.Q: POWO.setdefault(q['id'], q.get('taxon'))
    plants = [(p['id'], p['la']) for p in D['P']] + [(q['id'], q['la']) for q in K.Q if q['id'] not in {p['id'] for p in D['P']}]
    res, say = {}, {s[0]: 0 for s in SERILER}
    for pid, la in plants:
        taxon = re.sub(r'\s+ve diğer.*$', '', (POWO.get(pid) or la.split(',')[0]).strip()).replace('× ', '')
        bul = {}
        for ad, ek, need in SERILER:
            try:
                f = ara(taxon, ek, need)
                if f: bul[ad] = f; say[ad] += 1
            except Exception as e: print('hata', pid, ad, str(e)[:80])
            time.sleep(0.2)
        res[pid] = {'taxon': taxon, 'seriler': bul}
        print(pid, taxon, '→', ', '.join(bul) or '-', flush=True)
    json.dump(res, open(os.path.join(T.ROOT, 'seri_tara.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    kh = {p for p, v in res.items() if {'Köhler', 'Thomé'} & set(v['seriler'])}
    print('\n=== ÖZET ===')
    print('toplam bitki', len(res), '| Köhler/Thomé', len(kh))
    for ad, _, _ in SERILER:
        ek = sum(1 for p, v in res.items() if p not in kh and ad in v['seriler'])
        print(f'{ad}: toplam {say[ad]}, Köhler/Thomé dışındakilerden {ek}')
    hic = [p for p, v in res.items() if not v['seriler']]
    print('hiçbir seride yok:', len(hic), ', '.join(hic))

if __name__ == '__main__':
    main()
