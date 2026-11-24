#!/usr/bin/env python3
"""Toplu kayıt dosyasındaki kaynakları canlı denetler: python3 tools/arsiv_kaynak_kontrol.py kuyruk/aNNN.py
PubMed / PMC adresleri NCBI'den sorgulanır; künyedeki yıl ve ilk yazar soyadı, başlıktan sözcükler gerçek kayıtla karşılaştırılır.
Diğer adresler için yalnızca yanıt kodu yazılır. Uyuşmayan her satır elle bakılmalıdır."""
import sys, re, json, time, importlib.util, urllib.request, unicodedata
UA = {'User-Agent': 'bitkitabani-kaynak/1.0 (+https://bitkitabani.com)'}
def al(u, js=True):
    for _ in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40)
            return json.loads(r.read()) if js else r.status
        except urllib.error.HTTPError as e:
            if not js: return e.code
            time.sleep(2)
        except Exception: time.sleep(2)
    return None
def sade(t): return unicodedata.normalize('NFKD', t or '').encode('ascii', 'ignore').decode().lower()
def main(f):
    sp = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    sorun = 0; n = 0
    for q in m.Q:
        for kun, u in list(q.get('kaynak', [])) + list(q.get('ema', [])):
            n += 1
            pm = re.search(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)', u); pc = re.search(r'PMC(\d+)', u)
            if pm or pc:
                db, i = ('pubmed', pm.group(1)) if pm else ('pmc', pc.group(1))
                d = al(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db={db}&id={i}&retmode=json'); time.sleep(0.4)
                r = (d or {}).get('result', {}).get(i, {})
                if not r or r.get('error'): print(f'{q["id"]}: KAYIT YOK {u}'); sorun += 1; continue
                yil = (r.get('pubdate') or r.get('epubdate') or '')[:4]; yz = sade((r.get('authors') or [{}])[0].get('name', '')).split(' ')[0]
                bas = [w for w in re.findall(r'[a-z]{5,}', sade(r.get('title', '')))][:8]
                k = sade(kun); tut = sum(1 for w in bas if w in k)
                h = []
                if yz and yz not in k: h.append(f'ilk yazar "{yz}" künyede yok')
                if yil and yil not in kun and str(int(yil) + 1) not in kun and str(int(yil) - 1) not in kun: h.append(f'yıl {yil} künyede yok')
                if bas and tut < max(1, len(bas) // 3): h.append(f'başlık uyuşmuyor: gerçek başlık "{r.get("title", "")[:90]}"')
                if h: print(f'{q["id"]}: {u}\n    künye: {kun[:120]}\n    ' + '; '.join(h)); sorun += 1
            else:
                kod = al(u, js=False)
                if kod not in (200, 403): print(f'{q["id"]}: yanıt {kod} {u}'); sorun += 1
    print(f'{n} kaynak denetlendi, {sorun} satır elle bakılmalı')
if __name__ == '__main__': main(sys.argv[1])
