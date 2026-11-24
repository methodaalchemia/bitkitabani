#!/usr/bin/env python3
"""site/ gönderilmeden önce temel sayfaların yerinde olduğunu doğrular.
Derleme yarıda kalırsa ana sayfa ve katalog eksik kalır; bu betik o hâlin gönderilmesini engeller.
Çalıştırma: python3 tools/site_saglik.py  (çıkış kodu 0 ise gönderilebilir)"""
import os, sys, glob
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(KOK, 'site')
ZORUNLU = ['index.html', 'katalog/index.html', 'en/index.html', 'en/catalog/index.html',
           'sitemap.xml', 'yeni/index.html', 'yeni/rss.xml', '_headers']
hata = []
for y in ZORUNLU:
    p = os.path.join(S, y)
    if not os.path.exists(p): hata.append(f'eksik: site/{y}')
    elif os.path.getsize(p) < (400 if y == '_headers' else 2000): hata.append(f'çok küçük ({os.path.getsize(p)}B): site/{y}')
n = len(glob.glob(os.path.join(S, '**', 'index.html'), recursive=True))
if n < 1200: hata.append(f'sayfa sayısı düşük: {n} (beklenen 1200+) — derleme yarıda kalmış olabilir')
# Görselli sayfa sayısı: images.json toptan kaybolduğunda derleme sorunsuz
# tamamlanıyor ama bütün bitki sayfaları fotoğrafsız çıkıyor (24 Kasım 2026).
gorselli = 0
for f in glob.glob(os.path.join(S, '*', 'index.html')):
    with open(f, encoding='utf-8', errors='ignore') as fh:
        if '-500.webp' in fh.read(): gorselli += 1
if gorselli < 200:
    hata.append(f'görselli bitki sayfası yalnız {gorselli} (200+ beklenir) — images.json kaybolmuş olabilir')

print('\n'.join(hata) if hata else f'tamam: {n} sayfa, {gorselli} görselli sayfa, temel sayfalar yerinde')
sys.exit(1 if hata else 0)
