# -*- coding: utf-8 -*-
"""Künyeleri APA 7 biçimine çevirir.

Üstveri yayıncıdan gelir, elle yazılmaz: PubMed/PMC için NCBI E-utilities,
DOI için Crossref, DergiPark için sayfanın citation_* meta etiketleri.
Sonuç kunye_apa.json'a yazılır; derleme ağa çıkmaz, oradan okur.

    python3 tools/apa.py          # eksikleri çek
    python3 tools/apa.py --yenile # hepsini yeniden çek
"""
import json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
ONBELLEK = os.path.join(HERE, 'kunye_apa.json')
UA = {'User-Agent': 'BitkiTabaniBot/1.0 (https://bitkitabani.com)'}
E = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

KUCUK = {'of', 'and', 'the', 'in', 'for', 'on', 'a', 'an', 'to', 'at', 'from', 'with', 'de', 'la'}


def al(url, timeout=60):
    for deneme in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()
        except Exception:
            if deneme == 3:
                raise
            time.sleep(4 * (deneme + 1))


def dergi_adi(s):
    """PubMed dergi adlarını küçük harfle verir; APA başlık biçimi ister."""
    if not s:
        return ''
    kelimeler = s.split()
    out = []
    for i, k in enumerate(kelimeler):
        if i and k.lower() in KUCUK:
            out.append(k.lower())
        elif k.isupper() or (len(k) <= 4 and k.isupper()):
            out.append(k)
        else:
            out.append(k[0].upper() + k[1:])
    return ' '.join(out)


def yazarlar(ad_listesi):
    """['Cantrell CL', 'Jones AM'] -> 'Cantrell, C. L., & Jones, A. M.'"""
    bicimli = []
    for ad in ad_listesi:
        parca = ad.rsplit(' ', 1)
        if len(parca) == 2 and parca[1].isupper() and len(parca[1]) <= 4:
            soyad, bas = parca
            # Eski PubMed kayıtlarında soyadı tamamen büyük harf olabiliyor
            if soyad.isupper() and len(soyad) > 1:
                soyad = soyad[0] + soyad[1:].lower()
            bicimli.append(f"{soyad}, {' '.join(h + '.' for h in bas)}")
        else:
            bicimli.append(ad)
    if not bicimli:
        return ''
    if len(bicimli) == 1:
        return bicimli[0]
    if len(bicimli) <= 20:
        return ', '.join(bicimli[:-1]) + ', & ' + bicimli[-1]
    return ', '.join(bicimli[:19]) + ', . . . ' + bicimli[-1]


def baslik_duzelt(t):
    # PubMed uzun tireyi iki kısa çizgiyle yazıyor
    t = (t or '').strip().replace('--', '\u2014')
    return re.sub(r'\.+$', '', t)


def apa_makale(d):
    au = yazarlar([a['name'] for a in d.get('authors', []) if a.get('authtype') == 'Author'])
    yil = (d.get('pubdate') or '')[:4] or 'n.d.'
    baslik = baslik_duzelt(d.get('title'))
    dergi = dergi_adi(d.get('fulljournalname') or d.get('source'))
    cilt = d.get('volume') or ''
    sayi = d.get('issue') or ''
    sayfa = (d.get('pages') or '').replace('-', '–')
    doi = next((x['value'] for x in d.get('articleids', []) if x['idtype'] == 'doi'), '')
    kitap = d.get('booktitle')

    if kitap and not dergi:
        yayinci = d.get('publishername') or ''
        s = f"{baslik}. ({yil}). In {kitap}. {yayinci}."
        return re.sub(r'\s+', ' ', s).strip()

    s = f"{au} ({yil}). {baslik}. {dergi}"
    if cilt:
        s += f", {cilt}"
        if sayi:
            s += f"({sayi})"
    if sayfa:
        s += f", {sayfa}"
    s += '.'
    if doi:
        s += f" https://doi.org/{doi}"
    return re.sub(r'\s+', ' ', s).strip()


def apa_crossref(m):
    au = yazarlar([f"{a.get('family','')} {''.join(p[0].upper() for p in (a.get('given') or '').replace('.',' ').split())}".strip()
                   for a in m.get('author', []) if a.get('family')])
    yil = str((m.get('issued', {}).get('date-parts') or [[None]])[0][0] or 'n.d.')
    baslik = baslik_duzelt((m.get('title') or [''])[0])
    dergi = dergi_adi((m.get('container-title') or [''])[0])
    cilt, sayi = m.get('volume') or '', m.get('issue') or ''
    sayfa = (m.get('page') or '').replace('-', '–')
    s = f"{au} ({yil}). {baslik}. {dergi}"
    if cilt:
        s += f", {cilt}"
        if sayi:
            s += f"({sayi})"
    if sayfa:
        s += f", {sayfa}"
    s += '.'
    if m.get('DOI'):
        s += f" https://doi.org/{m['DOI']}"
    return re.sub(r'\s+', ' ', s).strip()


def doi_to_pmid(doi):
    try:
        u = E + 'esearch.fcgi?' + urllib.parse.urlencode(
            {'db': 'pubmed', 'term': f'{doi}[DOI]', 'retmode': 'json'})
        ids = json.loads(al(u))['esearchresult']['idlist']
        return str(ids[0]) if ids else None
    except Exception:
        return None


def pmc_esearch(pmcid):
    try:
        u = E + 'esearch.fcgi?' + urllib.parse.urlencode(
            {'db': 'pubmed', 'term': f'{pmcid}[PMCID]', 'retmode': 'json'})
        ids = json.loads(al(u))['esearchresult']['idlist']
        return str(ids[0]) if ids else None
    except Exception:
        return None


def europepmc(pmcid):
    """PubMed'de olmayan PMC kayitlari icin yedek cozucu."""
    try:
        u = ('https://www.ebi.ac.uk/europepmc/webservices/rest/search?' +
             urllib.parse.urlencode({'query': f'PMCID:{pmcid}', 'format': 'json',
                                     'resultType': 'core', 'pageSize': 1}))
        r = json.loads(al(u))['resultList']['result']
        if not r:
            return None
        x = r[0]
        ad = [a['fullName'] for a in (x.get('authorList') or {}).get('author', [])]
        if not ad and x.get('authorString'):
            ad = [p.strip() for p in x['authorString'].rstrip('.').split(',') if p.strip()]
        ji = x.get('journalInfo', {}) or {}
        d = {
            'authors': [{'name': a, 'authtype': 'Author'} for a in ad],
            'pubdate': str(x.get('pubYear') or ''),
            'title': x.get('title'),
            'fulljournalname': (ji.get('journal') or {}).get('title'),
            'volume': ji.get('volume') or '', 'issue': ji.get('issue') or '',
            'pages': x.get('pageInfo') or '',
            'articleids': ([{'idtype': 'doi', 'value': x['doi']}] if x.get('doi') else []),
        }
        return apa_makale(d)
    except Exception:
        return None


def dergipark(url):
    try:
        h = al(url).decode('utf-8', 'replace')
    except Exception:
        return None
    g = lambda n: [m.group(1) for m in re.finditer(
        r'<meta[^>]+name="citation_' + n + r'"[^>]+content="([^"]*)"', h)]
    au = g('author')
    if not au:
        return None
    bicimli = []
    for a in au:
        if ',' in a:
            soyad, ad = [x.strip() for x in a.split(',', 1)]
        else:
            p = a.rsplit(' ', 1); soyad, ad = (p[1], p[0]) if len(p) == 2 else (a, '')
        bas = ' '.join(x[0].upper() + '.' for x in ad.split() if x)
        bicimli.append(f'{soyad}, {bas}'.strip().rstrip(','))
    yaz = bicimli[0] if len(bicimli) == 1 else ', '.join(bicimli[:-1]) + ', & ' + bicimli[-1]
    t = (g('title') or [''])[0]
    dergi = (g('journal_title') or [''])[0]
    yil = (g('publication_date') or g('date') or [''])[0][:4] or 'n.d.'
    cilt = (g('volume') or [''])[0]; sayi = (g('issue') or [''])[0]
    ilk = (g('firstpage') or [''])[0]; son = (g('lastpage') or [''])[0]
    s2 = f'{yaz} ({yil}). {baslik_duzelt(t)}. {dergi}'
    if cilt:
        s2 += f', {cilt}'
        if sayi:
            s2 += f'({sayi})'
    if ilk:
        s2 += f', {ilk}' + (f'\u2013{son}' if son and son != ilk else '')
    s2 += '.'
    doi = (g('doi') or [''])[0]
    if doi:
        s2 += f' https://doi.org/{doi}'
    return re.sub(r'\s+', ' ', s2).strip()


def pmid_cek(pmidler):
    out = {}
    for i in range(0, len(pmidler), 100):
        obek = pmidler[i:i + 100]
        obek = [str(x) for x in obek]
        u = E + "esummary.fcgi?" + urllib.parse.urlencode({"db": "pubmed", "id": ",".join(obek), "retmode": "json"})
        d = json.loads(al(u))['result']
        for p in obek:
            if p in d and not d[p].get('error'):
                out[p] = d[p]
        time.sleep(1)
    return out


def pmc_to_pmid(pmcler):
    eslesme = {}
    for i in range(0, len(pmcler), 100):
        obek = pmcler[i:i + 100]
        u = ('https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?format=json&ids=' +
             ','.join(obek) + '&tool=bitkitabani&email=iletisim@bitkitabani.com')
        try:
            d = json.loads(al(u))
        except Exception as ex:
            print('  idconv hata:', ex)
            time.sleep(3)
            continue
        for kayit in d.get('records', []):
            if kayit.get('pmid'):
                eslesme[kayit.get('pmcid')] = str(kayit['pmid'])
        time.sleep(1)
    return eslesme


# Kimligi adresinden okunamayan ama yayinci kaydi bulunan birkac adres.
# Deger elle degil, yine PubMed/Crossref'ten cekilir.
ZORLAMA = {
    'https://www.nature.com/articles/s41559-018-0697-x': ('pmid', '30374172'),
    'https://www.sciencedirect.com/science/article/abs/pii/S027841652100060X': ('doi', '10.1016/j.jaa.2021.101327'),
}


def kimlik(url):
    if url in ZORLAMA:
        return ZORLAMA[url]
    m = re.search(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)', url)
    if m:
        return ('pmid', m.group(1))
    m = re.search(r'pmc\.ncbi\.nlm\.nih\.gov/articles/(PMC\d+)', url)
    if m:
        return ('pmc', m.group(1))
    m = re.search(r'doi\.org/(10\.[^\s"<>]+)', url)
    if m:
        return ('doi', m.group(1).rstrip('/'))
    return (None, None)


def main():
    import refs
    yenile = '--yenile' in sys.argv
    onbellek = {} if yenile else (json.load(open(ONBELLEK, encoding='utf-8')) if os.path.exists(ONBELLEK) else {})

    urller = []
    for sozluk in (refs.EMA, refs.OTHER):
        for v in sozluk.values():
            for _, u in v:
                if u and u not in urller:
                    urller.append(u)
    # Kuyruktaki kayıtların kendi kaynakları derleme anında OTHER'a ekleniyor
    # (build.py), bu yüzden refs.py üzerinden görünmüyorlar.
    try:
        import kuyruk
        for q in kuyruk.Q:
            for _, u in (q.get('kaynak') or []):
                if u and u not in urller:
                    urller.append(u)
    except Exception as ex:
        print('kuyruk okunamadı:', ex)
    # Familya sayfalarının kaynakları
    try:
        from familya import FAM_BILGI
        for v in FAM_BILGI.values():
            for _, u in (v.get('kaynak') or []) if isinstance(v, dict) else []:
                if u and u not in urller:
                    urller.append(u)
    except Exception:
        pass

    # Derlenmiş sitedeki künye listelerinden de topla: yazı, motif ve rehber
    # sayfalarının kaynakları yukarıdaki modüllerden geçmiyor.
    try:
        import glob
        kok = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'site')
        for f in glob.glob(os.path.join(kok, '**', '*.html'), recursive=True):
            h = open(f, encoding='utf-8').read()
            for ol in re.findall(r'<ol class="refs">(.*?)</ol>', h, re.S):
                for u in re.findall(r'<li[^>]*>.*?href="(https?://[^"]+)"', ol, re.S):
                    if u not in urller:
                        urller.append(u)
    except Exception as ex:
        print('site taranamadı:', ex)

    eksik = [u for u in urller if u not in onbellek]
    print(f'{len(urller)} benzersiz adres, {len(eksik)} tanesi önbellekte yok.')

    pmid_url, pmc_url, doi_url = {}, {}, {}
    for u in eksik:
        t, k = kimlik(u)
        if t == 'pmid':
            pmid_url.setdefault(str(k), []).append(u)
        elif t == 'pmc':
            pmc_url.setdefault(k, []).append(u)
        elif t == 'doi':
            doi_url.setdefault(k, []).append(u)

    if pmc_url:
        print(f'  {len(pmc_url)} PMC kimliği PMID\'e çevriliyor...')
        for pmc, pmid in pmc_to_pmid(list(pmc_url)).items():
            pmid_url.setdefault(str(pmid), []).extend(pmc_url[pmc])

    if pmid_url:
        print(f'  {len(pmid_url)} PubMed kaydı çekiliyor...')
        for pmid, d in pmid_cek(list(pmid_url)).items():
            s = apa_makale(d)
            for u in pmid_url[pmid]:
                onbellek[u] = {'apa': s, 'kaynak': f'pubmed:{pmid}'}

    for doi, us in doi_url.items():
        pmid = doi_to_pmid(doi)
        time.sleep(1)
        if pmid:
            d = pmid_cek([pmid]).get(pmid)
            if d:
                s = apa_makale(d)
                for u in us:
                    onbellek[u] = {'apa': s, 'kaynak': f'pubmed:{pmid}'}
                continue
        try:
            m = json.loads(al('https://api.crossref.org/works/' + urllib.parse.quote(doi)))['message']
            s = apa_crossref(m)
            for u in us:
                onbellek[u] = {'apa': s, 'kaynak': f'crossref:{doi}'}
        except Exception as ex:
            print('  DOI çözülemedi:', doi, ex)
        time.sleep(1)

    # idconv'un bulamadığı PMC kayıtları
    for u in [x for x in eksik if x not in onbellek and 'pmc.ncbi' in x]:
        m = re.search(r'(PMC\d+)', u)
        pmid = pmc_esearch(m.group(1)) if m else None
        time.sleep(1)
        if pmid:
            d = pmid_cek([pmid]).get(pmid)
            if d:
                onbellek[u] = {'apa': apa_makale(d), 'kaynak': f'pubmed:{pmid}'}

    for u in [x for x in eksik if x not in onbellek and 'pmc.ncbi' in x]:
        m = re.search(r'(PMC\d+)', u)
        s = europepmc(m.group(1)) if m else None
        if s:
            onbellek[u] = {'apa': s, 'kaynak': 'europepmc'}
        time.sleep(1)

    for u in [x for x in eksik if x not in onbellek and 'dergipark' in x]:
        s = dergipark(u)
        if s:
            onbellek[u] = {'apa': s, 'kaynak': 'dergipark'}
        time.sleep(1)

    json.dump(dict(sorted(onbellek.items())), open(ONBELLEK, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cozulen = sum(1 for u in urller if u in onbellek)
    print(f'\n{cozulen}/{len(urller)} adres çözüldü, {ONBELLEK} yazıldı.')
    kalan = [u for u in urller if u not in onbellek]
    if kalan:
        print(f'\nOtomatik çözülemeyen {len(kalan)} adres (elle APA yazılacak):')
        for u in kalan:
            print('  ', u[:100])


if __name__ == '__main__':
    main()
