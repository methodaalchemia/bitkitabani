# -*- coding: utf-8 -*-
"""Elle yazılan editoryal gönderiler. Otomasyon tek biçim kalır; bu dosya yalnızca
belirtilen günde belirtilen yuvanın metnini değiştirir, hattı durdurmaz ya da silmez.

yuva='ogle'  → Facebook 17:30 + Threads 17:24
yuva='soru'  → Threads 21:24–23:30 (anekdot/efsane için; ölçülen en iyi saat)

metin   : Facebook'a giden tam metin (uzunluk sınırı yok)
threads : Threads'e giden kısa sürüm (495 karakterde kesilir)
gorsel  : tam adres; boş bırakılırsa bitkinin site fotoğrafı kullanılır
bitki   : görseli ondan alınır (katalog id)

Kaynak: hepsi kendi kayıtlarımızdan; uydurma iddia yok, kaynak kişi ve köy adı geçmez.
Biçim kuralı (23 Kasım ölçümü): her gönderi soru ya da sezgiye aykırı olguyla açılır;
haftada bir kişisel anı biçimi (etkileşim alan tek biçim); duyuru biçimi kullanılmaz.
"""

EDITORYAL = [

dict(yayin='2026-11-25', yuva='ogle', bitki='zencefil',
 metin="""Zencefil doğada yetişmez.

Yabani hâli yok. Binlerce yıldır yalnızca insan eliyle, rizomundan parça alınarak çoğaltılmış. Yani elinizdeki her zencefil, birinin bir başkasına verdiği parçanın devamı.

Hindistan'da Ayurveda'da "evrensel ilaç" sayılır; Çin'de soğuk algınlığında taze rizomu kaynatılır. Araştırmalara gelince: EMA taşıt tutmasına bağlı bulantıda iyi yerleşmiş kullanım olarak tanıyor. Eklem ağrısı ve kilo verme iddiaları için kanıt zayıf.

Kan sulandırıcı kullanıyorsanız ya da safra taşınız varsa, takviye almadan önce hekiminize danışın.

Kaynaklarıyla: bitkitabani.com/zencefil""",
 threads="""Zencefil doğada yetişmez.

Yabani hâli yok. Binlerce yıldır yalnızca insan eliyle, rizomundan parça alınarak çoğaltılmış. Elinizdeki her zencefil, birinin bir başkasına verdiği parçanın devamı.

EMA, taşıt tutmasına bağlı bulantıda iyi yerleşmiş kullanım olarak tanıyor. Eklem ağrısı ve kilo verme iddiaları için kanıt zayıf.

bitkitabani.com/zencefil"""),

dict(yayin='2026-11-26', yuva='soru', bitki='ardic',
 metin="""Cin içkisinin adı ardıç kozalağından geliyor: Felemenkçe "jenever".

Aynı kozalak Anadolu'da içilmez, yakılır. Yörükler ardıç dalını tutuşturup evi ve ağılı tütsüler.

Binlerce kilometre ötede, Kırgız ve Moğol şamanizminde de aynı şey yapılır: arça dumanı törenden önce mekânı ve insanları arındırır.

Bir ağaç, üç ayrı iş.

bitkitabani.com/ardic""",
 threads="""Cin içkisinin adı ardıç kozalağından geliyor: Felemenkçe "jenever".

Aynı kozalak Anadolu'da içilmez, yakılır. Yörükler ardıç dalını tutuşturup evi ve ağılı tütsüler.

Binlerce kilometre ötede, Kırgız ve Moğol şamanizminde de aynı şey yapılır: arça dumanı törenden önce mekânı ve insanları arındırır.

Bir ağaç, üç ayrı iş.

bitkitabani.com/ardic"""),

dict(yayin='2026-11-27', yuva='ogle', bitki='meyan',
 metin="""Meyan kökünün dünyadaki en büyük alıcılarından biri tütün sanayisi.

Sigaraya tat vermek için kullanılıyor. Oysa Güneydoğu'da Ramazan'da şerbeti içilir, öksürüğe ve mide yanmasına karşı kökü çiğnenir. Çin tıbbında ise en sık kullanılan bitkilerden biridir — diğer otları "uyumlu hâle getirdiği" için neredeyse her reçeteye eklenir.

Şekerden 50 kat tatlı. Ama düzenli ve yüksek miktarda tüketimi tansiyonu yükseltir, potasyumu düşürür. Tansiyon, kalp ve böbrek hastaları ile gebeler kaçınmalı.

Kaynaklarıyla: bitkitabani.com/meyan""",
 threads="""Meyan kökünün dünyadaki en büyük alıcılarından biri tütün sanayisi.

Oysa Güneydoğu'da Ramazan'da şerbeti içilir. Çin tıbbında ise en sık kullanılan bitkilerden biri — diğer otları "uyumlu hâle getirdiği" için neredeyse her reçeteye ekleniyor.

Şekerden 50 kat tatlı. Düzenli ve yüksek tüketim tansiyonu yükseltir; tansiyon, kalp ve böbrek hastaları ile gebeler kaçınmalı.

bitkitabani.com/meyan"""),

dict(yayin='2026-11-28', yuva='soru', bitki='kusburnu',
 metin="""İkinci Dünya Savaşı'nda İngiltere'ye portakal girmiyordu.

C vitamini açığını kapatmak için çocuklar çalılıklara gönderildi: kuşburnu toplamaya.

İşin tuhafı, bugün biliyoruz ki o meyveyi kurutmak ve kaynatmak C vitamininin büyük kısmını götürüyor. Yani kış çayından beklenen şey, beklendiği kadar değil.

bitkitabani.com/kusburnu""",
 threads="""İkinci Dünya Savaşı'nda İngiltere'ye portakal girmiyordu.

C vitamini açığını kapatmak için çocuklar çalılıklara gönderildi: kuşburnu toplamaya.

İşin tuhafı, bugün biliyoruz ki o meyveyi kurutmak ve kaynatmak C vitamininin büyük kısmını götürüyor. Yani kış çayından beklenen şey, beklendiği kadar değil.

bitkitabani.com/kusburnu"""),

dict(yayin='2026-11-30', yuva='ogle', bitki='ihlamur',
 metin="""Üşüttüğümüzde evde çay değil, "o çay" demlenirdi.

Mutfakta ayrı bir kavanozu vardı. Kaynatılmazdı — "kaynatırsan uçar" denirdi; su demlikte biraz dinlendirilir, sonra üstüne dökülürdü. Bardağa konunca kokusu bütün eve yayılırdı.

Yıllar sonra öğrendim ki o çiçekler haziranda toplanıyormuş. Yani kışın içtiğimiz şey, yazdan kalan bir şeymiş.

Ihlamurdan bahsediyorum.

Sizin evinizde kışın hangi çay demlenirdi? Yorumlarda buluşalım.

Kaynaklarıyla: bitkitabani.com/ihlamur""",
 threads="""Üşüttüğümüzde evde çay değil, "o çay" demlenirdi.

Kaynatılmazdı — "kaynatırsan uçar" denirdi; su demlikte dinlendirilir, sonra üstüne dökülürdü.

Yıllar sonra öğrendim ki o çiçekler haziranda toplanıyormuş. Kışın içtiğimiz şey, yazdan kalan bir şeymiş.

Ihlamurdan bahsediyorum.

bitkitabani.com/ihlamur"""),

dict(yayin='2026-12-02', yuva='ogle', bitki='kusburnu',
 metin="""İngiltere'de çocuklar neden kuşburnu toplamaya seferber edildi?

İkinci Dünya Savaşı'nda ülkeye narenciye girmiyordu. C vitamini açığını kapatmak için çocuklar çalılıklara gönderildi.

Bugün bilinen şu: taze meyve C vitamini bakımından gerçekten çok zengin — ama kurutma ve kaynatma bu vitamini büyük ölçüde azaltıyor. Yani kış çayınızdan beklediğiniz C vitamini, beklediğiniz kadar olmayabilir.

Çekirdeklerin çevresindeki tüyler ağzı ve bağırsağı tahriş eder; süzmeden tüketmeyin.

Kaynaklarıyla: bitkitabani.com/kusburnu""",
 threads="""Taze kuşburnu C vitamini bakımından çok zengin.

Ama kurutmak ve kaynatmak bu vitamini büyük ölçüde azaltıyor. Yani kış çayınızdan beklediğiniz C vitamini, beklediğiniz kadar olmayabilir.

Çekirdeklerin çevresindeki tüyler ağzı ve bağırsağı tahriş eder; süzmeden tüketmeyin.

bitkitabani.com/kusburnu"""),

dict(yayin='2026-12-04', yuva='ogle', bitki='ardic',
 metin="""Cin içkisinin adı nereden geliyor?

Ardıç kozalağından. Felemenkçe "jenever" — tadı da oradan.

Aynı kozalağın Anadolu'da bambaşka bir işi var: Yörükler ardıç dalını yakıp evi, ağılı ve hastayı tütsüler. Kırgız, Kazak ve Moğol şamanizminde arça dumanı kötü ruhları kovar; törenlerden önce mekân ve insanlar bu dumanla arındırılır.

Kozalağın uzun süreli ya da yüksek dozda alınması böbreği tahriş edebilir. Gebelikte ve böbrek hastalığında kullanılmamalı.

Kaynaklarıyla: bitkitabani.com/ardic""",
 threads="""Cin içkisinin adı ardıç kozalağından: Felemenkçe "jenever".

Anadolu'da aynı kozalak içilmez, yakılır: Yörükler ardıç dalıyla evi ve ağılı tütsüler.

Kozalağın uzun süreli ya da yüksek dozda alınması böbreği tahriş edebilir. Gebelikte ve böbrek hastalığında kullanılmamalı.

bitkitabani.com/ardic"""),

dict(yayin='2026-12-05', yuva='soru', bitki='meyan',
 metin="""Çin tıbbında meyan kökü neredeyse her reçetede var.

Tek başına bir derde deva olduğu için değil — diğer otları "uyumlu hâle getirdiği" için ekleniyor. Reçetenin arabulucusu gibi.

Güneydoğu'da ise Ramazan'da şerbeti içilir; serinletici ve mide dostu sayılır.

Şekerden 50 kat tatlı olan bu kök, bugün en çok tütün sanayisine satılıyor.

bitkitabani.com/meyan""",
 threads="""Çin tıbbında meyan kökü neredeyse her reçetede var.

Tek başına bir derde deva olduğu için değil — diğer otları "uyumlu hâle getirdiği" için ekleniyor. Reçetenin arabulucusu gibi.

Güneydoğu'da ise Ramazan'da şerbeti içilir.

Şekerden 50 kat tatlı olan bu kök, bugün en çok tütün sanayisine satılıyor.

bitkitabani.com/meyan"""),

dict(yayin='2026-12-07', yuva='ogle', bitki='ihlamur',
 metin="""Kış çayı dediğimiz ıhlamurun çiçekleri haziranda toplanır.

Ağacın kendisi birkaç yüz yıl yaşayabiliyor; Avrupa'da köy meydanlarının, buluşmaların ağacı. İstanbul'da da sokak ağacı olarak yaygın — yazın altından geçtiğiniz ağaç, kışın bardağınızda.

EMA, ıhlamur çiçeğini soğuk algınlığı belirtileri ve hafif zihinsel stres için geleneksel kullanımda tanıyor. Klinik çalışması az.

TİTCK monografı lityumla etkileşim bildiriyor. EMA gebelikte ve emzirirken yeterli veri olmadığı için önermiyor.

Kaynaklarıyla: bitkitabani.com/ihlamur""",
 threads="""Kış çayı dediğimiz ıhlamurun çiçekleri haziranda toplanır.

Ağaç birkaç yüz yıl yaşayabiliyor. İstanbul'da sokak ağacı olarak yaygın — yazın altından geçtiğiniz ağaç, kışın bardağınızda.

EMA soğuk algınlığı belirtileri ve hafif zihinsel stres için geleneksel kullanımda tanıyor; klinik çalışması az.

bitkitabani.com/ihlamur"""),

dict(yayin='2026-12-09', yuva='ogle', bitki='adacayi',
 metin="""Bardağınızdaki adaçayı nereden geldi?

Türkiye'de satılan adaçayının çoğu tarladan değil, yabandan toplanıyor. Aşırı toplama bazı bölgelerde popülasyonları azaltıyor.

Latince adı "salvare" kökünden gelir: iyileştirmek, kurtarmak. Orta Çağ Avrupa'sında her derde deva sayılırdı. Ege ve Akdeniz köylerinde boğaz ağrısı ve soğuk algınlığı için demlenir, ıhlamur ve ayva yaprağıyla karıştırılır.

Tuyon içerdiği için uzun süre ve yüksek dozda kullanılmamalı. Gebelik, emzirme ve epilepside önerilmez.

Kaynaklarıyla: bitkitabani.com/adacayi""",
 threads="""Türkiye'de satılan adaçayının çoğu tarladan değil, yabandan toplanıyor. Aşırı toplama bazı bölgelerde popülasyonları azaltıyor.

Latince adı "salvare" kökünden: iyileştirmek, kurtarmak.

Tuyon içerdiği için uzun süre ve yüksek dozda kullanılmamalı. Gebelik, emzirme ve epilepside önerilmez.

bitkitabani.com/adacayi"""),
]
