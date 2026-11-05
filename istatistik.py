# -*- coding: utf-8 -*-
# /istatistik/ sayfasındaki elle güncellenen rakamlar.
# Kapsam, kanıt ve güvenlik dağılımları derleme sırasında veriden hesaplanır; burada yalnızca
# dışarıdan gelen (Search Console) veriler durur. Ayda bir güncellenir.

ARAMA = dict(
    tarih='5 Kasım 2026',
    donem='son 28 gün',
    tiklama=87,
    gosterim=11500,
    to='%0,8',
    konum='16,8',
    dizinli=464,
    kuruldu='17 Ekim 2026',
    # (sorgu, gösterim, konum, tıklama)
    sorgular=[
        ('güz çiğdemi', 357, '10,2', 2),
        ('kantuta', 226, '7,3', 0),
        ('ayı üzümü', 136, '9,4', 0),
        ('pıtrak motifi', 87, '9,4', 0),
        ('su yolu motifi anlamı', 62, '8,0', 0),
        ('bereket motifi anlamı', 61, '9,0', 0),
        ('haşhaş', 57, '7,3', 0),
        ('tarçın çayı nasıl yapılır', 48, '10,1', 0),
        ('çengel motifi anlamı', 18, '8,2', 1),
        ('mersin yaprağının zararları', 8, '—', 2),
    ],
)
