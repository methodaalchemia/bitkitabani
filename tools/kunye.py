#!/usr/bin/env python3
"""Künye denetimi: DergiPark bağlantısı olan bütün kaynakları yayıncı üstverisiyle karşılaştırır.

Site kaynaklarında yazar adı yanlış yazmak, okuyan akademisyenden düzeltme maili almakla
sonuçlanıyor. Bu betik her kaynağın yazar adlarını DergiPark'ın citation_author üstverisinden
çeker ve künye metninde geçip geçmediğine bakar.

    python3 tools/kunye.py            # hepsini tara
    python3 tools/kunye.py --json     # makine okunur çıktı

Çıkış kodu: farklılık bulunursa 1, bulunmazsa 0.
"""
import os, re, sys, json, html, time, unicodedata, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
ATLA = ('/site', '/.git', '__pycache__', '/node_modules')


def kaynaklari_topla():
    """Python dosyalarındaki ('künye metni', 'url') ikililerini bulur."""
    cift = []
    for kok, _d, dosyalar in os.walk(HERE):
        if any(x in kok for x in ATLA): continue
        for f in dosyalar:
            if not f.endswith('.py'): continue
            p = os.path.join(kok, f)
            s = open(p, encoding='utf-8').read()
            for m in re.finditer(r"\(\s*(['\"])(.{10,400}?)\1\s*,\s*(['\"])(https?://[^'\"]+)\3\s*\)", s, re.S):
                cift.append((os.path.relpath(p, HERE), re.sub(r'\s+', ' ', m.group(2)), m.group(4)))
            for m in re.finditer(r"\(\s*(['\"])(.{10,400}?)\1\s*,\s*_?L\s*\+\s*(['\"])(\d+)\3\s*\)", s, re.S):
                cift.append((os.path.relpath(p, HERE), re.sub(r'\s+', ' ', m.group(2)),
                             'https://dergipark.org.tr/tr/pub/mutftd/article/' + m.group(4)))
    gorulen, out = set(), []
    for p, t, u in cift:
        if 'dergipark.org.tr' not in u or '/article/' not in u or u in gorulen: continue
        gorulen.add(u); out.append((p, t, u))
    return out


def sadele(x):
    x = x.replace('İ', 'i').replace('I', 'ı').lower()
    return ''.join(c for c in unicodedata.normalize('NFD', x) if unicodedata.category(c) != 'Mn')


def uste_bak(url):
    r = urllib.request.Request(url, headers={'User-Agent': UA})
    h = urllib.request.urlopen(r, timeout=40).read().decode('utf-8', 'replace')
    yazar = [html.unescape(a) for a in re.findall(r'<meta name="citation_author" content="([^"]+)"', h)]
    b = re.search(r'<meta name="citation_title" content="([^"]+)"', h)
    return yazar, (html.unescape(b.group(1)) if b else '')


def main():
    kaynaklar = kaynaklari_topla()
    rapor, fark = [], 0
    for p, t, u in kaynaklar:
        try:
            yazar, baslik = uste_bak(u)
        except Exception as e:
            rapor.append(dict(dosya=p, url=u, durum='HATA', hata=str(e)[:80])); continue
        if not yazar:
            rapor.append(dict(dosya=p, url=u, durum='USTVERI YOK')); continue
        nt = sadele(t)
        def gecer(a): return all(w in nt for w in sadele(a).split() if len(w) > 2)
        if ('ve ark' in nt or 'et al' in nt) and gecer(yazar[0]):
            eksik = []          # "ve ark." kısaltması: ilk yazar doğruysa yeter
        else:
            eksik = [a for a in yazar if not gecer(a)]
        d = dict(dosya=p, url=u, kunye=t, yazarlar=yazar, baslik=baslik,
                 durum='TAMAM' if not eksik else 'FARKLI')
        if eksik: fark += 1
        rapor.append(d)
        time.sleep(1.2)
    if '--json' in sys.argv:
        print(json.dumps(rapor, ensure_ascii=False, indent=1))
    else:
        for d in rapor:
            if d['durum'] == 'TAMAM': continue
            print(f"[{d['durum']}] {d['dosya']}  {d['url']}")
            if 'kunye' in d:
                print('   sitede :', d['kunye'][:150])
                print('   gerçek :', ', '.join(d.get('yazarlar', [])), '||', d.get('baslik', '')[:90])
        print(f"\n{len(kaynaklar)} kaynak tarandı, {fark} farklılık.")
    return 1 if fark else 0


if __name__ == '__main__':
    sys.exit(main())
