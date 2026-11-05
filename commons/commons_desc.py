# -*- coding: utf-8 -*-
import json, os, re

R = json.load(open('/home/claude/commons/motifler.json', encoding='utf-8'))

BOLGE_EN = {
 'Altay, Sayan ve Sibirya': 'the Altai, Sayan and Siberia',
 'Amazon': 'the Amazon',
 'Anadolu': 'Anatolia',
 'Anadolu (Geç Hitit’ten Osmanlı’ya)': 'Anatolia (Neo-Hittite to Ottoman)',
 'Anadolu (Osmanlı mezar taşları)': 'Anatolia (Ottoman gravestones)',
 'Anadolu (Osmanlı)': 'Anatolia (Ottoman)',
 'Anadolu (Selçuklu, Osmanlı)': 'Anatolia (Seljuk and Ottoman)',
 'Anadolu kilimleri': 'Anatolian kilims',
 'Anadolu ve Batı': 'Anatolia and Europe',
 'Anadolu, Kuzey Afrika, Orta Doğu': 'Anatolia, North Africa and the Middle East',
 'And Dağları': 'the Andes',
 'Antik Yunan ve Roma': 'ancient Greece and Rome',
 'Denizli (iğne oyası)': 'Denizli, Turkey (needle lace)',
 'Hindistan (Budist sanatı)': 'India (Buddhist art)',
 'Kelt Avrupası': 'Celtic Europe',
 'Kuzey Amerika (Meksika)': 'North America (Mexico)',
 'Mezopotamya (Yeni Asur)': 'Mesopotamia (Neo-Assyrian)',
 'Mısır, Hindistan, Orta Asya ve Anadolu': 'Egypt, India, Central Asia and Anatolia',
 'Orta Asya ve Anadolu': 'Central Asia and Anatolia',
 'Orta Asya’dan Anadolu’ya (Selçuklu, Osmanlı)': 'Central Asia to Anatolia (Seljuk and Ottoman)',
 'Orta Asya’dan Osmanlı’ya': 'Central Asia to the Ottoman world',
 'Çin': 'China',
 'İran, Hindistan ve Anadolu halıları': 'Persian, Indian and Anatolian carpets',
 'İskandinav mitolojisi': 'Norse mythology',
}
TEMA_EN = {
 'Bereket ve doğurganlık': 'fertility and abundance',
 'Bitki motifleri': 'plant motifs',
 'Evren, gök ve döngü': 'cosmos, sky and cycle',
 'Görü ve ruhlar dünyası': 'vision and the spirit world',
 'Koruma ve nazar': 'protection and the evil eye',
}

def kategoriler(b):
    k = ['Category:Motifs']
    if 'Anadolu' in b or 'Denizli' in b or 'Osmanlı' in b or 'Selçuklu' in b:
        k += ['Category:Kilim', 'Category:Symbols of Turkey']
    else:
        k += ['Category:Ornaments']
    return k

out = {}
for d in R:
    b_en = BOLGE_EN.get(d['bolge'], d['bolge'])
    t_en = TEMA_EN.get(d['tema'], d['tema'])
    kay = d['kaynaklar'][0] if d['kaynaklar'] else ''
    tr = (f"{d['ad']} motifi. {d['kisa']} "
          f"Bölge: {d['bolge']}. Tema: {d['tema']}. "
          f"Tek renk çizim; Bitki Tabanı (bitkitabani.com) için çizilmiştir.")
    if kay:
        tr += f" Motifin anlamı için kullanılan kaynak: {kay}."
    en = (f"Line drawing of the \"{d['ad']}\" motif from {b_en}; "
          f"theme: {t_en}. Drawn for the Bitki Tabanı database (bitkitabani.com).")
    cats = '\n'.join('[[%s]]' % c for c in kategoriler(d['bolge']))
    wt = f"""=={{{{int:filedesc}}}}==
{{{{Information
|description={{{{tr|1={tr}}}}}
{{{{en|1={en}}}}}
|date=2026-11-05
|source={{{{own}}}}
|author=[[User:BItkitabani|Edanaz Tınmazlar]]
|permission=
|other versions=
}}}}

=={{{{int:license-header}}}}==
{{{{self|cc-by-sa-4.0}}}}

{cats}
"""
    out[d['dosya']] = {'wikitext': wt, 'ad': d['ad'], 'slug': d['slug']}

json.dump(out, open('/home/claude/commons/aciklamalar.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('açıklama üretilen dosya:', len(out))
print()
k = 'Pıtrak motifi - Bitki Tabani cizimi.svg'
print(out[k]['wikitext'])
