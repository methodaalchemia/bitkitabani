#!/usr/bin/env python3
"""TİTCK monograf dosyasını indirip düz metne çevirir.

Monograflar iki biçimde yayımlanıyor: çoğu PDF, bir kısmı .docx. Dosya
uzantısı her zaman doğru değil — bazı .docx dosyaları adres satırında
PDF gibi duruyor — bu yüzden biçim içeriğin ilk baytlarından anlaşılıyor
(``%PDF`` ile başlıyorsa PDF, ``PK`` ile başlıyorsa zip, yani docx).

Çalıştırma:  python3 tools/titck_oku.py "Latince ad" ["Latince ad" ...]
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from html import unescape

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                    'Chrome/120 Safari/537.36'}


def metin(ham):
    """Ham baytları düz metne çevirir; biçimi baytlardan anlar."""
    if ham[:4] == b'%PDF':
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            f.write(ham)
            yol = f.name
        try:
            return subprocess.run(['pdftotext', '-layout', yol, '-'],
                                  capture_output=True, text=True,
                                  timeout=120).stdout
        finally:
            os.unlink(yol)
    if ham[:2] == b'PK':
        with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as f:
            f.write(ham)
            yol = f.name
        try:
            x = zipfile.ZipFile(yol).read('word/document.xml').decode('utf-8', 'replace')
            x = re.sub(r'</w:p>', '\n', x)
            return re.sub(r'[ \t]+', ' ', unescape(re.sub(r'<[^>]+>', '', x)))
        finally:
            os.unlink(yol)
    return ham.decode('utf-8', 'replace')


def oku(latin_ad):
    parti = json.load(open(os.path.join(KOK, 'parti70.json'), encoding='utf-8'))
    kayit = [o for o in parti if o['latin'] == latin_ad]
    if not kayit:
        return None, f'{latin_ad} parti dosyasında yok'
    u = kayit[0]['titck_pdf']
    if not u:
        return None, f'{latin_ad} için monograf adresi yok'
    ham = urllib.request.urlopen(
        urllib.request.Request(u, headers=UA), timeout=120).read()
    t = metin(ham)
    return '\n'.join(l.rstrip() for l in t.split('\n') if l.strip()), None


def main():
    for ad in sys.argv[1:]:
        t, hata = oku(ad)
        print('=' * 74)
        print(ad)
        print(hata if hata else t[:2200])


if __name__ == '__main__':
    main()
