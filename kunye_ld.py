"""APA künyesini schema.org `citation` nesnesine çevirir.

Sayfaların altındaki numaralı kaynak listesi insana görünüyordu, makineye görünmüyordu.
Aynı künyelerden üretilen bu nesneler, bir arama motoru ya da dil modelinin
"bu sayfadaki iddia neye dayanıyor" sorusuna cevap verebilmesi için.
Yeni bilgi üretilmez; yalnızca var olan künye ayrıştırılır.
"""
import re

_YIL = re.compile(r'\((\d{4})[a-z]?\)')
_DOI = re.compile(r'(10\.\d{4,9}/[^\s,;)\]]+)')
_KITAP = {'Kitap', 'Book'}
_MAKALE = {'Araştırma', 'Research', 'EMA monografisi', 'EMA monograph', 'EMA raporu', 'EMA report'}


def cite_one(kind, apa, url=''):
    """(tür, APA künyesi, adres) -> schema.org CreativeWork sözlüğü ya da None."""
    apa = (apa or '').strip()
    if not apa:
        return None
    m = _YIL.search(apa)
    yazar = re.sub(r'[\s,]+$', '', apa[:m.start()].strip()) if m else ''   # baş harften sonraki noktayı koru
    kalan = apa[m.end():].lstrip(' .') if m else apa
    baslik = kalan.split('. ')[0].strip().rstrip('.').strip() if kalan else ''
    tip = 'Book' if kind in _KITAP else ('ScholarlyArticle' if kind in _MAKALE else 'CreativeWork')
    d = {'@type': tip, 'name': (baslik or apa)[:300]}
    if yazar and 2 < len(yazar) < 200:
        d['author'] = yazar
    if m:
        d['datePublished'] = m.group(1)
    doi = _DOI.search(apa) or _DOI.search(url or '')
    if doi:
        d['identifier'] = 'https://doi.org/' + doi.group(1).rstrip('.')
    if url:
        d['url'] = url
    return d


def cite_ld(items, limit=40):
    """refs() listesindeki (tür, künye, adres) üçlülerinden citation dizisi; yinelenenler atılır."""
    out, gorulen = [], set()
    for k, apa, url in items:
        c = cite_one(k, apa, url)
        if not c:
            continue
        anahtar = c.get('identifier') or c.get('url') or c['name']
        if anahtar in gorulen:
            continue
        gorulen.add(anahtar)
        out.append(c)
        if len(out) >= limit:
            break
    return out
