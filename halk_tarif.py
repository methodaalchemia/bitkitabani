# Hikâyelerde kaynağın aktardığı hazırlanış (tarif). Yalnızca kaynakta yazanlar; ölçü verilmemişse uydurulmaz.
# Alanlar: ad, malzeme (liste), adim (liste), olcu (ölçüler hakkında not), uyari, kaynak (kısa atıf; boşsa hikâyenin kaynağı)
TARIF = {
 '600-yillik-sac-bakimi-haci-pasa': [
  dict(ad='Sabuncuoğlu’nun gece yağı (Terceme-i Akrabâdîn, 15. yüzyıl)',
       malzeme=['Mersin yaprağı', 'Mazı', 'Helile otu', 'Fesleğen şarabı', 'Susam yağı', 'Laden reçinesi (Cistus creticus)', 'Yıkamak için mersin suyu'],
       adim=['Mazı, helile otu ve mersin yaprağı fesleğen şarabıyla kaynatılır ve süzülür.', 'Süzülen sıvıya susam yağı ve laden eklenip yeniden kaynatılır.', 'Karışım her gece saç köklerine sürülür.', 'Ertesi sabah saç mersin suyuyla yıkanır.']),
  dict(ad='Hekim Hayreddin’in mersinli yağı (Kitâb-ı Akrâbâdîn)',
       malzeme=['Emlec otu (Phyllanthus emblica)', 'Mersin yaprağı', 'Su', 'Zeytinyağı', 'Laden reçinesi'],
       adim=['Emlec otu ve mersin yaprakları suda kaynatılır.', 'Zeytinyağı eklenir ve su tamamen buharlaşana kadar kaynatmaya devam edilir; geriye ilaçlı yağ kalır.', 'Son olarak laden eklenip bir kez daha kaynatılır.']),
 ],
 'mugla-ula-kok-boyaci-recep-tutuncu': [
  dict(ad='Tütüncü ailesinin yanık karışımı (kayıttaki hazırlanış)',
       malzeme=['Kirişlik (çiriş otu, Asphodelus aestivus) kökü', 'Piynar meşesinin (Quercus aucheri) kılcal kökleri', 'Hayıt (Vitex agnus-castus) ağacının dış kabuğu', 'Sakız ağacının (Pistacia lentiscus) akıtması', 'Badem yağı, Hint yağı, susam yağı, ayçiçek yağı ve gliserin'],
       adim=['Kirişlik kökleri kaynatılıp suyu alınır.', 'Toprağın iki üç parmak altındaki piynar kökleri ile hayıt kabuğu ayrı ayrı kaynatılır; sakız ağacı kaynatılarak akıtması alınır.', 'Piynar, hayıt ve sakız ağacı sıvıları karıştırılır; sarı bir sıvı elde edilir ve kirişlik suyu eklenir.', 'Bu sıvıya yağlar ve gliserin katılarak kremsi bir ham karışım yapılır; bir yıl boyunca kullanılır.'],
       olcu='Aile tam ölçüleri açıklamıyor; makalede 7–8 bitki kökü ve çeşitli yağlarla “belirli ölçülerle” hazırlandığı yazıyor.',
       uyari='Bu bir ailenin kuşaktan kuşağa aktardığı uygulamanın kaydıdır, evde denenecek bir yöntem değildir. Yanıkta ilk iş yanan yeri 10–20 dakika ılık akan suyun altında tutmak ve geniş, derin, yüzde, elde ya da çocuktaki yanıklarda hemen sağlık kuruluşuna gitmektir. Aile de vücudun büyük kısmı yanmışsa, ateş ya da kusma varsa hastayı hastaneye gönderiyor.'),
 ],
 'diyadin-dogubayazit-dag-sakizi-scorzonera-latifolia': [
  dict(ad='Dağ sakızı',
       malzeme=['Dağ sakızı bitkisinin (Scorzonera latifolia) kökü', 'Bıçak, kaşık ve kavanoz'],
       adim=['Toprağın altındaki kökün çevresi bıçakla açılır.', 'Kökün bir kısmı kesilir ve süt gibi akan özsuyun gelmesi beklenir.', 'Akan süt kaşıkla kavanoza alınır.', 'Süt birkaç dakika ateşte, sürekli karıştırılarak kaynatılır.', 'Soğumaya bırakılan karışım zamanla sakıza dönüşür; mide ağrısında çiğnenir.']),
 ],
 'agri-nin-diyadin-dogubayazit-yorelerinde-civanpercemi': [
  dict(ad='Yara tozu ve civanperçemi suyu',
       malzeme=['Kurutulmuş civanperçemi (Achillea millefolium)', 'Sıcak su'],
       adim=['Yara için: bitki öğütülüp un hâline getirilir ve açık yaranın üzerine serpilir.', 'Karın ağrısı ve adet sancısı için: bitki birkaç dakika sıcak suda bekletilir ve suyu içilir; yörede günde 2–3 kez içildiği anlatılıyor.'],
       uyari='Kirli ya da derin yaraya toz serpmek iltihap riskini artırabilir. Hamilelikte civanperçemi içilmez; papatyagillere alerjisi olanlar dikkat etmeli.'),
 ],
 'diyadin-dogubayazit-hatmi-yalnizca-oksurukte-icilmiyor': [
  dict(ad='Bel ağrısı için hatmi suyu',
       malzeme=['Toplanıp kurutulmuş hatmi (Althaea officinalis)', 'Kaynar su'],
       adim=['Kurutulmuş ot demlenir ve suyu süzülür.', 'Süzülen su ağrıyan yere masaj yapılarak sürülür; uygulama akşamları yapılır.', 'Yörede aralıklarla sürülen suyla birlikte bardak (kupa) da çekiliyor.']),
 ],
 'agri-yoresinde-isirganin-kaynatma-suyu-yalnizca': [
  dict(ad='Saç için ısırgan suyu',
       malzeme=['Isırgan otu (Urtica dioica)', 'Su'],
       adim=['Isırgan suda kaynatılır.', 'Suyu süzülür.', 'Süzülen su düzenli olarak saça sürülür.'],
       uyari='Taze ısırganı eldivenle topla. Saç dökülmesi ani ya da öbek öbekse önce bir hekime görün; demir eksikliği ve tiroit sık nedenlerdir.'),
 ],
 'her-papatya-ayni-bitki-degil': [
  dict(ad='Papatya buharı',
       malzeme=['Papatyanın (yörede Anthemis armeniaca) yalnızca çiçek başları', 'Su'],
       adim=['Çiçek başları toplanıp kurutulur.', 'Kurutulan çiçekler suda kaynatılır.', 'Kaynayan suyun buharı solunur; yörede sinüzite iyi geldiği söyleniyor.'],
       uyari='Buhar alırken kaynar suya fazla yaklaşma; çocuklarda haşlanma riski yüzünden önerilmez. Papatyagillere alerjisi olanlar kullanmamalı.'),
 ],
 'dogubayazit-yoresinde-agriyan-iltihapli-dis-sinir': [
  dict(ad='Diş için sinir otu lapası',
       malzeme=['Taze sinir otu yaprağı (Plantago major)'],
       adim=['Yaprak ezilir.', 'Ağrıyan, iltihaplı dişin üzerine konur.', 'Sabaha kadar bekletilir.'],
       uyari='İltihaplı diş yayılabilir; yüzde şişlik ya da ateş varsa beklemeden diş hekimine git.'),
 ],
}
