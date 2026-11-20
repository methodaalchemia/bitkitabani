# -*- coding: utf-8 -*-
"""Arayüz metinleri — tek yerde.

Sitede tekrar eden bölüm başlıkları, buton etiketleri ve boş durum
metinleri burada durur; build.py bunları `UI.<AD>` diye kullanır. Amaç
kalıcı bir denetim yüzeyi: bir dil turunda bütün dizeler tek dosyadan
okunur ve değiştirilir, 2.700 satırlık şablonun içinde aranmaz.

⚠️ Bölüm çapaları (#bilim-ne-diyor gibi) metne bağlı değildir ve burada
tutulmaz; başlık değişse de çapa aynı kalır, dışarıdan verilmiş bağlar
kırılmasın diye.

Son dil turu: D2, 20 Kasım 2026 (claude/d2-dil-turu-onerileri.md).
"""


class UI:
    # --- bitki sayfası bölüm başlıkları ---
    GELENEKSEL = 'Geleneksel kullanım'
    ARASTIRMALAR = 'Araştırmalar ne gösteriyor'        # D2: eski "Bilim ne diyor"
    KANIT = 'Faydaları ne kadar kanıtlı?'
    DOGADA = 'Doğada nasıl görünür'                     # D2: eski "Doğada ve tanıma"
    HAZIRLAMA = 'Nasıl hazırlanır'
    GUVENLIK = 'Güvenlik'
    ETKILESIM = 'İlaç etkileşimleri'
    YASAL = 'Yasal durum'
    KORUMA = 'Koruma durumu'
    BENZER = 'Benzer bitkiler'
    TANIMA = 'Nasıl tanınır?'
    HATALAR = 'Sık yapılan hatalar'
    KOMSULAR = 'Aynı bölgeden, aynı kullanımdan'        # D2: eski "Aynı bölge ve kullanımda"
    SIMGE = 'Kültürdeki simgesi'                        # D2: eski "Sembollerde"
    DEVAM = 'Bununla ilgili başka sayfalar'             # D2: eski "Devamını oku"
    SSS = 'Sık sorulanlar'
    KAYNAKLAR = 'Kaynaklar'
    ILGILI_SEMBOL = 'İlgili semboller'

    # --- butonlar ---
    OGRENDIM = 'Öğrendim'                               # D2: eski "Öğrendim olarak işaretle"

    # --- katalog ---
    KATALOG_BOS = 'Bu arama ve filtrelere uyan bitki yok.'   # D2
    KATALOG_BOS_NOT = 'Bir filtreyi kaldırmayı ya da farklı bir kelime denemeyi dene.'

    # --- köprü ve motif ---
    YANYANA = 'İki bitki yan yana'                      # D2: eski "Yan yana"
    KOPRU = 'Kültür köprüsü'
    DIGER_KOPRU = 'Diğer köprüler'
    MOTIF_ANLAM = 'Motif ne anlatır'                    # D2: eski "Ne anlatır?"

    # --- rehber ---
    ILAC_HEPSI = 'Bütün ilaç grupları'                  # D2: eski "Bütün gruplar"
    DIGER_REHBER = 'Diğer rehberler'

    # --- eczacı çağrısı (bant, H1, title, og:title ve şema adı aynı dizeden) ---
    ECZACI_BASLIK = 'İçeriği eczacı gözüyle değerlendirecek beş eczacı arıyoruz'   # D2
