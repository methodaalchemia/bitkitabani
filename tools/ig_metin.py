# Instagram metinleri: her bitki için elle, özenle yazılmış slayt ve açıklama metinleri.
# Dil: akıcı, düzgün cümleler; okura "siz" diye seslenilir; abartı ve "mucize" dili yok.
# Bilgiler katalogdaki kayıtla aynıdır (kaynaklar sitede); burada yalnızca anlatım sadeleşir.
#
# Alanlar:
#   ilk      açıklamanın ilk satırı (bitkinin adını içerir; aramada bulunmak için önemli)
#   kapak    kapak slaytındaki büyük soru ya da cümle
#   aciklama açıklamada ilk satırın ardından gelen iki üç cümle
#   kisaca   üç satırlık özet: (başlık, metin)
#   hikaye, gelenek, bilim, nasil: (başlık, metin)
#   dikkat   kimlerin dikkat etmesi gerektiği (liste), dikkat_not: altına kısa not
#   kaydet   son slayttaki çağrı, soru: açıklamanın sonundaki yorum sorusu

M = {
'zencefil': dict(
    ilk='Zencefil bulantıya gerçekten iyi gelir mi? 🫚', kapak='Bulantıya gerçekten iyi gelir mi?',
    aciklama='Zencefil, bulantıya iyi geldiği bilimsel olarak gösterilmiş az sayıdaki bitkiden biri. Yine de “her derde deva” değil: eklem ağrısı ve zayıflama iddialarını destekleyen güçlü bir kanıt bulunmuyor.',
    kisaca=[('Kökeni', 'Güney ve Doğu Asya'), ('Geleneksel kullanımı', 'Bulantı, soğuk algınlığı ve hazımsızlık'), ('Bilimsel kanıt', 'Bulantıda güçlü, diğer iddialarda zayıf')],
    hikaye=('Yabani hâli hiç bulunamadı', 'Zencefilin doğada kendiliğinden yetişen bir hâli bilinmiyor. Bitki binlerce yıldır yalnızca insan eliyle, kök parçalarından çoğaltılıyor.'),
    gelenek=('Ayurveda’nın “evrensel ilacı”', 'Hint geleneğinde neredeyse her derde başvurulan bir bitkidir. Çin’de taze kökü soğuk algınlığında kaynatılarak içilir; Osmanlı macunlarında da sıkça yer alırdı.'),
    bilim=('En güçlü kanıt bulantıda', 'Avrupa İlaç Ajansı, zencefilin taşıt tutmasına bağlı bulantıda kullanımını kabul ediyor. Hamilelik bulantısıyla ilgili küçük çalışmalar da olumlu sonuç veriyor. Eklem ağrısı ve kilo verme iddiaları ise kanıtlanmış değil.'),
    dikkat=['Kan sulandırıcı ilaç kullananlar', 'Safra taşı olanlar', 'Yüksek dozda takviye almayı düşünenler'], dikkat_not='Yemeklerde kullanılan miktarlar güvenlidir.',
    nasil=('Zencefil çayı', 'Üç dört ince dilim taze zencefili bir bardak suda 10 dakika kaynatın. Dilerseniz limon ve bal ekleyin.'),
    kaydet='Soğuk günler için kaydedin.', soru='Siz zencefili en çok nasıl tüketiyorsunuz?'),

'zerdecal': dict(
    ilk='Zerdeçal: mucize baharat mı, iyi pazarlama mı? 🟡', kapak='Mucize baharat mı, iyi pazarlama mı?',
    aciklama='Zerdeçal son yıllarda neredeyse her derde iyi gelen bir baharat gibi anlatılıyor. Oysa bilimsel kanıt, bu ünün çok gerisinde kalıyor.',
    kisaca=[('Kökeni', 'Hindistan ve Güneydoğu Asya'), ('Geleneksel kullanımı', 'İltihap, eklem ağrısı ve sindirim'), ('Bilimsel kanıt', 'Diz ağrısında biraz umut verici, diğer iddialarda zayıf')],
    hikaye=('Sarı rengin ardındaki kurşun', 'Bangladeş’te ucuz zerdeçalın rengini canlandırmak için kurşun içeren boya kullanıldığı ortaya çıktı ve kurşun zehirlenmeleri yaşandı. Bu yüzden zerdeçalı güvenilir kaynaktan almak önemli.'),
    gelenek=('Hint düğünlerinin rengi', 'Hindistan’da düğünden önce gelin ve damadın bedenine zerdeçal sürülür. Anadolu’da ise safranın ucuz bir ikamesi olarak zerde tatlısına ve pilava renk verir.'),
    bilim=('Etken maddesi zor emiliyor', 'Diz kireçlenmesinde ağrıyı biraz azaltabildiğini gösteren küçük çalışmalar var. Ancak etken maddesi kurkumin vücutta zayıf emiliyor ve iddiaların çoğu henüz kanıtlanmış değil.'),
    dikkat=['Kan sulandırıcı ilaç kullananlar', 'Safra taşı olanlar', 'Yüksek dozda kapsül almayı düşünenler'], dikkat_not='Yüksek dozlu kapsüllerle karaciğer hasarı bildirildi; yemeklerdeki miktar güvenlidir.',
    nasil=('Zerdeçallı süt', 'Bir bardak ılık süte yarım çay kaşığı zerdeçal, bir tutam karabiber ve biraz bal ekleyin. Karabiber, kurkuminin emilimini artırır.'),
    kaydet='Mutfakta kullanmak için kaydedin.', soru='Zerdeçalı en çok hangi yemekte kullanıyorsunuz?'),

'adacayi': dict(
    ilk='Boğaz ağrısında neden hep adaçayı? 🌿', kapak='Boğaz ağrısında neden hep adaçayı?',
    aciklama='Ege ve Akdeniz’de kuşaktan kuşağa aktarılan bu alışkanlığın bilimsel bir karşılığı var. Yine de adaçayının her gün ve uzun süre içilmemesi gerekiyor.',
    kisaca=[('Kökeni', 'Ege ve Akdeniz’in kayalık yamaçları'), ('Geleneksel kullanımı', 'Boğaz ağrısı, ağız iltihabı ve terleme'), ('Bilimsel kanıt', 'Gargarada geleneksel kullanımı kabul görüyor')],
    hikaye=('Adı “kurtarmak” kökünden geliyor', 'Latince adı Salvia, “iyileştirmek, kurtarmak” anlamındaki salvare kökünden gelir. Orta Çağ Avrupası’nda her derde deva sayılırdı.'),
    gelenek=('Ege’nin kış çayı', 'Köylerde boğaz ağrısı, mide rahatsızlığı ve soğuk algınlığı için demlenir. Çoğu zaman ıhlamur ve ayva yaprağıyla karıştırılarak içilir.'),
    bilim=('Ağız ve boğazda kabul görüyor', 'Avrupa İlaç Ajansı adaçayını ağız ve boğaz iltihabı ile aşırı terlemede geleneksel kullanımda tanıyor. Anadolu’da yetişen türde tuyon genellikle daha azdır.'),
    dikkat=['Hamileler ve emzirenler', 'Epilepsi hastaları', 'Her gün, uzun süre içmeyi düşünenler'], dikkat_not='İçerdiği tuyon, yüksek dozda sinir sistemini etkileyebilir.',
    nasil=('Boğaz için gargara', 'Bir tatlı kaşığı kuru yaprağı bir bardak kaynar suda 10 dakika demleyin. Ilıdıktan sonra gargara yapın.'),
    kaydet='Boğazınız ağrıdığında bakmak için kaydedin.', soru='Adaçayını neyle karıştırarak içiyorsunuz?'),

'ihlamur': dict(
    ilk='Ihlamur neden kış akşamlarının çayıdır? 🍵', kapak='Kış akşamlarının vazgeçilmezi',
    aciklama='Ihlamur, soğuk algınlığında içilen en yaygın bitki çaylarından biri. Avrupa’da da bu kullanım geleneksel olarak kabul görüyor.',
    kisaca=[('Kökeni', 'Karadeniz ve Marmara ormanları'), ('Geleneksel kullanımı', 'Soğuk algınlığı ve rahatlama'), ('Bilimsel kanıt', 'Geleneksel kullanım; klinik çalışma az')],
    hikaye=('Yüzyıllarca yaşayan ağaç', 'Bir ıhlamur ağacı birkaç yüz yıl yaşayabilir. Avrupa’da köy meydanlarının ve buluşmaların ağacı olarak bilinir.'),
    gelenek=('Terleten, rahatlatan bir çay', 'Soğuk algınlığında terlemek ve rahatlamak için içilir. İstanbul’un sokaklarındaki ıhlamur ağaçlarının çiçekleri Haziran’da toplanır.'),
    bilim=('Avrupa’da da kabul görüyor', 'Avrupa İlaç Ajansı ıhlamur çiçeğini soğuk algınlığı belirtileri ve hafif stres için geleneksel kullanımda tanıyor. Klinik çalışmalar ise oldukça sınırlı.'),
    dikkat=['Bilinen önemli bir yan etkisi yoktur'], dikkat_not='Çoğu kişi için güvenli bir çaydır.',
    nasil=('İyi ıhlamur nasıl seçilir?', 'Çiçekler sarımsı olmalı, yaprakçığıyla birlikte toplanmış olmalı ve güçlü kokmalı. Bir tatlı kaşığını 10 dakika demleyin.'),
    kaydet='Kış için kaydedin.', soru='Ihlamuru ballı mı, limonlu mu seviyorsunuz?'),

'papatya': dict(
    ilk='Papatya çayı neden uyku getirir? 🌼', kapak='Papatya çayı neden uyku getirir?',
    aciklama='Papatya, bilimsel kanıtı en sağlam bitki çaylarından biri. Sakinleştirici etkisinin arkasında beyindeki belirli reseptörlere bağlanan bir molekül olabilir.',
    kisaca=[('Kökeni', 'Anadolu’dan And Dağları’na'), ('Geleneksel kullanımı', 'Mide, uyku ve cilt tahrişi'), ('Bilimsel kanıt', 'Sindirim ve ciltte kabul görüyor')],
    hikaye=('Sakinliğin molekülü', 'Papatyanın içerdiği apigenin, beyinde sakinleştirici ilaçların da bağlandığı reseptörlere bağlanıyor. Rahatlatıcı etkisinin kaynağı bu olabilir.'),
    gelenek=('İki kıtanın ilk ilacı', 'Anadolu’da mide ağrısında ve uykusuzlukta içilir. Peru ve Bolivya’da manzanilla adıyla bilinir ve mide rahatsızlığında ilk başvurulan bitkidir.'),
    bilim=('Kanıtı güçlü bir çay', 'Avrupa İlaç Ajansı papatyayı hafif sindirim şikâyetleri, ağız ve boğaz iltihabı ile cilt tahrişinde tanıyor. Kaygı üzerine yapılan küçük çalışmaların sonuçları da olumlu.'),
    dikkat=['Papatyagillere alerjisi olanlar', 'Kan sulandırıcı ilaç kullananlar'], dikkat_not='Çoğu kişi için güvenlidir.',
    nasil=('Uykudan önce papatya', 'Bir tatlı kaşığı kuru papatyayı ağzı kapalı bir bardakta 5–10 dakika demleyin. Yatmadan yarım saat önce için.'),
    kaydet='Uykusuz bir gece için kaydedin.', soru='Papatya çayı size de uyku getiriyor mu?'),

'isirgan': dict(
    ilk='Isırgan: yakan ot neden sofraya girer? 🌱', kapak='Yakan ot neden sofraya girer?',
    aciklama='Isırgan, baharın ilk yabani sebzelerinden biri. Halk hekimliğinde ise hem Anadolu’da hem de And Dağları’nda şaşırtıcı biçimde benzer şekilde kullanılıyor.',
    kisaca=[('Kökeni', 'Anadolu’dan And Dağları’na'), ('Geleneksel kullanımı', 'Eklem ağrısı, idrar söktürme ve bahar yemekleri'), ('Bilimsel kanıt', 'Geleneksel kullanımı kabul görüyor')],
    hikaye=('Birbirinden habersiz iki gelenek', 'Ağrıyan bir ekleme taze ısırganla vurmak Antik Roma’dan beri bilinen bir yöntem. Aynı yöntem bugün Anadolu’da ve And Dağları’nda birbirinden habersiz uygulanıyor.'),
    gelenek=('Baharın ilk yeşili', 'Körpe yaprakları çorbaya, böreğe ve kavurmaya girer. And Dağları’nda ortiga adıyla bilinir ve arınma törenlerinde bedene hafifçe vurulur.'),
    bilim=('Yaprağı ve kökü farklı amaçlarla', 'Avrupa İlaç Ajansı, yaprağını eklem ağrısında ve idrar söktürücü olarak, kökünü ise prostat büyümesine bağlı idrar şikâyetlerinde geleneksel kullanımda tanıyor.'),
    dikkat=['Tansiyon ilacı kullananlar', 'Şeker ilacı kullananlar'], dikkat_not='Taze bitki ciltte kaşıntı yapar; eldivenle toplanmalıdır.',
    nasil=('Isırgan çorbası', 'Eldivenle topladığınız körpe yaprakları haşlayın. Yakıcılığı pişince tamamen kaybolur; ıspanak gibi kullanabilirsiniz.'),
    kaydet='Bahar için kaydedin.', soru='Isırganı en çok hangi yemekte kullanıyorsunuz?'),

'nane': dict(
    ilk='Nane mide rahatsızlıklarında gerçekten işe yarar mı? 🌿', kapak='Midede kanıtı en güçlü bitkilerden biri',
    aciklama='Nane, yalnızca mutfağın değil bilimin de iyi tanıdığı bir bitki. Özellikle nane yağı, huzursuz bağırsak belirtilerinde birçok çalışmada etkili bulundu.',
    kisaca=[('Kökeni', 'Akdeniz’den And Dağları’na'), ('Geleneksel kullanımı', 'Bulantı, gaz ve hazımsızlık'), ('Bilimsel kanıt', 'Nane yağı kapsüllerinde güçlü')],
    hikaye=('Bir perinin adını taşıyor', 'Yunan mitolojisinde Minthe adlı peri, Persephone tarafından naneye dönüştürülür. Bitkinin Latince adı da buradan gelir.'),
    gelenek=('Ayrandan cacığa', 'Anadolu’da mide bulantısı ve gaz için çayı içilir, kurusu kışın buharla solunur. Peru ve Bolivya’da hierbabuena adıyla en sık demlenen otlardan biridir.'),
    bilim=('Huzursuz bağırsakta etkili', 'Nane yağı kapsülleri, birçok kontrollü çalışmada huzursuz bağırsak belirtilerini plasebodan daha fazla azalttı. Nane yaprağı da hazımsızlıkta geleneksel olarak kabul görüyor.'),
    dikkat=['Reflü şikâyeti olanlar', 'Bebekler ve küçük çocuklar (saf nane yağı yüze sürülmemelidir)'], dikkat_not='Çay ve yemeklerdeki miktarlar güvenlidir.',
    nasil=('Taze nane çayı', 'Bir avuç taze yaprağı bardağa koyun, üzerine kaynar su dökün ve 5 dakika bekletin.'),
    kaydet='Midenizi düşünerek kaydedin.', soru='Naneyi en çok hangi yemekte kullanıyorsunuz?'),

'kekik': dict(
    ilk='Kekik aslında tek bir bitki değil 🌿', kapak='Kekik aslında tek bir bitki değil',
    aciklama='Türkçede “kekik” dediğimizde benzer kokulu onlarca farklı türden söz ediyoruz. Türkiye ise bu bitkilerin dünyadaki en büyük ihracatçısı.',
    kisaca=[('Kökeni', 'Anadolu’nun dağları ve Akdeniz'), ('Geleneksel kullanımı', 'Öksürük, soğuk algınlığı ve mide'), ('Bilimsel kanıt', 'Öksürükte geleneksel kullanımı kabul görüyor')],
    hikaye=('Onlarca türün ortak adı', 'Kekik, birbirine benzeyen pek çok türe verilen ortak bir addır. Güneydoğu Anadolu’nun kahvaltılarındaki zahter de bunlardan biri.'),
    gelenek=('Cesaretin simgesi', 'Antik Yunan’da kekik cesaretin simgesiydi ve tapınaklarda tütsü olarak yakılırdı. Anadolu’da ise kekik suyu ve kekik yağı yaygın birer halk ilacıdır.'),
    bilim=('Timol ve karvakrolün etkisi', 'İçerdiği timol ve karvakrol, laboratuvar çalışmalarında güçlü antimikrobiyal etki gösteriyor. Kekik, balgamlı öksürükte geleneksel bitkisel ilaç olarak kabul görüyor.'),
    dikkat=['Saf kekik yağını seyreltmeden cilde sürmeyin', 'Saf kekik yağını kesinlikle yutmayın'], dikkat_not='Yemeklerdeki miktarlar güvenlidir.',
    nasil=('Öksürük için kekik çayı', 'Bir tatlı kaşığı kuru kekiği bir bardak kaynar suda 5–10 dakika demleyin. Dilerseniz bal ekleyin.'),
    kaydet='Öksürük mevsimi için kaydedin.', soru='Sizin yörenizde kekiğe ne ad veriliyor?'),

'biberiye': dict(
    ilk='Biberiye gerçekten hafızanın bitkisi mi? 🌿', kapak='Gerçekten hafızanın bitkisi mi?',
    aciklama='Biberiye, Antik Yunan’dan beri hafızayla ilişkilendiriliyor. Bilim ise bu konuda henüz kesin bir şey söyleyemiyor.',
    kisaca=[('Kökeni', 'Akdeniz kıyıları'), ('Geleneksel kullanımı', 'Sindirim, kas ağrısı ve saç bakımı'), ('Bilimsel kanıt', 'Geleneksel; hafıza iddiası kesin değil')],
    hikaye=('Sınavlarda saça takılırdı', 'Antik Yunan’da biberiye hafızanın simgesiydi; öğrencilerin sınavlarda saçlarına biberiye taktığı anlatılır. Shakespeare’in Hamlet’inde de bu anlamda geçer.'),
    gelenek=('Bahçeden banyoya', 'Akdeniz’de çit bitkisi olarak yetiştirilir; yağı saç dökülmesinde ve kas ağrısında ovularak kullanılır. Peru’da ise romero, kötü enerjiyi uzaklaştırmak için banyo suyuna katılır.'),
    bilim=('Hafıza için henüz erken', 'Avrupa İlaç Ajansı biberiyeyi hafif sindirim şikâyetlerinde ve dıştan kas-eklem ağrısında tanıyor. Hafıza üzerine küçük çalışmalar var, ancak sonuçlar kesin değil.'),
    dikkat=['Epilepsi hastaları (yüksek dozda yağ)', 'Hamileler (yüksek dozda yağ)'], dikkat_not='Yemeklerdeki miktarlar güvenlidir.',
    nasil=('Biberiye suyu', 'Bir dal taze biberiyeyi bir litre suda 5 dakika kaynatın. Soğuduktan sonra saç durulama suyu olarak kullanabilirsiniz.'),
    kaydet='Denemek için kaydedin.', soru='Biberiyeyi en çok hangi yemekte kullanıyorsunuz?'),

'lavanta': dict(
    ilk='Lavanta kaygıda gerçekten işe yarıyor mu? 💜', kapak='Kaygıda gerçekten işe yarıyor mu?',
    aciklama='Lavantanın kaygı üzerindeki etkisi, şifalı bitkiler arasında en iyi araştırılmış konulardan biri. Ancak bu sonuçlar ağızdan alınan standart yağ kapsülleriyle elde edildi.',
    kisaca=[('Kökeni', 'Akdeniz; Türkiye’de Isparta'), ('Geleneksel kullanımı', 'Kaygı, uyku ve baş ağrısı'), ('Bilimsel kanıt', 'Yağ kapsüllerinde güçlü')],
    hikaye=('Adı “yıkamak” kökünden', 'Adının Latince “yıkamak” anlamındaki lavare kökünden geldiği düşünülür. Romalılar banyo sularına lavanta katardı.'),
    gelenek=('Isparta’nın mor tarlaları', 'Isparta’nın Kuyucak köyündeki tarlalar Temmuz’da çiçeklenir ve her yıl binlerce ziyaretçi çeker. Kurutulmuş lavanta dolaplara güveye karşı konur.'),
    bilim=('Kaygıda plasebodan üstün', 'Ağızdan alınan standart lavanta yağı kapsülleri, birçok kontrollü çalışmada kaygı bozukluğunda plasebodan daha etkili bulundu.'),
    dikkat=['Sakinleştirici ilaç kullananlar', 'Kapsül formu bulantı ve geğirme yapabilir'], dikkat_not='Çoğu kişi için güvenlidir.',
    nasil=('Lavanta kesesi', 'Bir avuç kuru lavantayı küçük bir bez keseye koyun ve yastığınızın yanına bırakın.'),
    kaydet='Huzurlu bir uyku için kaydedin.', soru='Kuyucak’ın lavanta tarlalarını gördünüz mü?'),

'corekotu': dict(
    ilk='Çörek otu gerçekten her derde deva mı? 🖤', kapak='Gerçekten her derde deva mı?',
    aciklama='Çörek otu yağı, Anadolu’da en yaygın ev ilaçlarından biri. Bilimsel çalışmalar bazı hafif etkiler gösteriyor, ancak bu ünü destekleyecek güçte değil.',
    kisaca=[('Kökeni', 'Anadolu, Orta Doğu ve Hindistan'), ('Öne çıkan iddialar', 'Kolesterol, kan şekeri ve tansiyon'), ('Bilimsel kanıt', 'Küçük çalışmalarda hafif etki')],
    hikaye=('Tutankamon’un mezarında', 'Çörek otu tohumları Tutankamon’un mezarında bulundu. Binlerce yıldır değer verilen bir tohum.'),
    gelenek=('Bir hadisin ünü', '“Ölümden başka her derde deva” olarak aktarılan bir hadis nedeniyle çörek otu yağı Anadolu’da çok yaygın bir ev ilacıdır.'),
    bilim=('Hafif etkiler, sınırlı kanıt', 'Küçük çalışmalarda kolesterolde, kan şekerinde ve tansiyonda hafif düşüş görüldü. Ancak bu çalışmalar kısa süreli ve kalitesi düşük.'),
    dikkat=['Şeker ilacı kullananlar', 'Tansiyon ilacı kullananlar'], dikkat_not='Pide ve çöreklerdeki miktarlar güvenlidir.',
    nasil=('Mutfakta çörek otu', 'Tavada birkaç saniye kavurun; kokusu çıkınca peynire, salataya ya da pilava serpin.'),
    kaydet='Hatırlamak için kaydedin.', soru='Çörek otu yağını siz de kullanıyor musunuz?'),

'dagcayi': dict(
    ilk='Toroslar’da “adaçayı” diye içilen bitki aslında ne? ⛰️', kapak='Toroslar’ın “adaçayı” aslında ne?',
    aciklama='Toroslar’da ve Batı Anadolu yaylalarında adaçayı diye toplanan çayın büyük kısmı, aslında bambaşka bir bitki: dağ çayı. Türlerinin çoğu yalnızca Anadolu’da yetişiyor.',
    kisaca=[('Kökeni', 'Toroslar ve Batı Anadolu yaylaları'), ('Geleneksel kullanımı', 'Öksürük, soğuk algınlığı ve mide'), ('Bilimsel kanıt', 'Geleneksel kullanımı kabul görüyor')],
    hikaye=('Türlerin çoğu yalnızca burada', 'Türkiye, dağ çayının dünyadaki en zengin yurdu. Burada yetişen türlerin çoğu başka hiçbir ülkede bulunmuyor.'),
    gelenek=('Yaylanın kış çayı', 'Yaz sonunda toplanan çiçekli dalları kış boyunca demlenir. Birçok yörede adaçayı olarak anılır; Yunanistan’da ise “dağ çayı” diye bilinir.'),
    bilim=('Uzun bir geçmişe dayanan kabul', 'Avrupa İlaç Ajansı dağ çayını soğuk algınlığına bağlı öksürükte ve hafif mide şikâyetlerinde geleneksel kullanımda tanıyor. İnsanlarda yapılmış çalışmalar ise az.'),
    dikkat=['Hamileler ve emzirenler', 'Küçük çocuklar'], dikkat_not='Yabandan toplanmış değil, üretilmiş çayı tercih edin; bazı türler azalıyor.',
    nasil=('Dağ çayı demlemek', 'Bir avuç kuru dalı kaynamış suda 5–10 dakika demleyin. Limon ve bal çok yakışır.'),
    kaydet='Kış hazırlığı için kaydedin.', soru='Sizin yörenizde bu çaya ne ad veriliyor?'),

'atkestanesi': dict(
    ilk='At kestanesi yenmez, ama ilaç olur 🌰', kapak='Yenmez, ama ilaç olur',
    aciklama='At kestanesinin tohumu zehirlidir; yine de arındırılmış ekstresi Avrupa’da yaygın bir damar ilacıdır. Hikâyesi ise İstanbul’dan başlıyor.',
    kisaca=[('Kökeni', 'Balkan dağları; İstanbul’un parkları'), ('Kullanım alanı', 'Bacakta şişlik ve ağırlık hissi'), ('Bilimsel kanıt', 'Standart ekstrede güçlü')],
    hikaye=('Avrupa’ya İstanbul’dan gitti', 'Ağaç Batı Avrupa’ya 1576’da İstanbul’dan götürüldü. Adının, Osmanlıların tohumu öksüren atlara vermesinden geldiği anlatılır.'),
    gelenek=('Saray bahçelerinin ağacı', 'İstanbul’un parklarına, saray ve yalı bahçelerine dikildi. 20. yüzyılda tohumundan elde edilen ekstre, Avrupa’da bir damar ilacına dönüştü.'),
    bilim=('Bacak şişliğinde etkili', 'Cochrane derlemesine göre standart ekstre, toplardamar yetmezliğinde bacak ağrısını, şişliği ve kaşıntıyı kısa sürede plasebodan daha fazla azaltıyor.'),
    dikkat=['Çiğ tohumu asla yemeyin; zehirlidir', 'Kan sulandırıcı ilaç kullananlar', 'Böbrek ya da karaciğer hastaları', 'Hamileler'], dikkat_not='',
    nasil=('Evde hazırlanmaz', 'Tohumu zehirlidir. Yalnızca eczanelerde satılan, zehirli maddesi arındırılmış standart ekstre kullanılır.'),
    kaydet='Kestaneyle karıştırmamak için kaydedin.', soru='Çocukken siz de at kestanesi toplar mıydınız?'),

'tarcin': dict(
    ilk='Hangi tarçını kullandığınızı biliyor musunuz? 🤎', kapak='Hangi tarçını kullanıyorsunuz?',
    aciklama='Markette satılan tarçının çoğu, Seylan tarçını değil kasya tarçını. Aradaki fark yalnızca tatta değil: kasya, her gün yüksek miktarda tüketildiğinde karaciğere zarar verebilecek kadar kumarin içeriyor.',
    kisaca=[('Kökeni', 'Sri Lanka ve Çin'), ('Öne çıkan iddia', 'Kan şekerini düşürmek'), ('Bilimsel kanıt', 'Tutarsız')],
    hikaye=('Dev kuşların yuvası masalı', 'Antik yazar Herodot, tarçının dev kuşların yuvalarından toplandığını yazar. Tüccarlar, gerçek kaynağı gizlemek için bu masalları yaymıştı.'),
    gelenek=('Sahlepten aşureye', 'Sahlep, aşure, sütlaç ve kış çaylarının vazgeçilmezidir. Osmanlı mutfağında etli yemeklerde de kullanılırdı.'),
    bilim=('Kan şekeri için kanıt yetersiz', 'Kan şekeri üzerine çok sayıda küçük çalışma yapıldı, ancak sonuçlar tutarsız. Tarçının herhangi bir hastalıkta işe yaradığı henüz gösterilmiş değil.'),
    dikkat=['Her gün çay kaşığıyla tüketenler', 'Karaciğer hastaları'], dikkat_not='Seylan tarçınında kumarin çok daha azdır.',
    nasil=('Seylan mı, kasya mı?', 'Seylan tarçını ince, kat kat ve kolay kırılır. Kasya tarçını ise kalın, sert ve tek katmanlıdır.'),
    kaydet='Alışverişte bakmak için kaydedin.', soru='Tarçını en çok nerede kullanıyorsunuz?'),

'ekinezya': dict(
    ilk='Ekinezya soğuk algınlığını gerçekten kısaltır mı? 🌸', kapak='Soğuk algınlığını kısaltır mı?',
    aciklama='Ekinezya, soğuk algınlığı için en çok satılan bitkisel ürünlerden biri. Bilimsel çalışmalar küçük bir etkiye işaret ediyor, ancak sonuçlar birbirini tutmuyor.',
    kisaca=[('Kökeni', 'Kuzey Amerika’nın Büyük Ovaları'), ('Kullanım alanı', 'Soğuk algınlığı'), ('Bilimsel kanıt', 'Küçük ve tutarsız bir etki')],
    hikaye=('Kirpiye benzeyen çiçek', 'Çiçeğinin ortasındaki dikenli koni kirpiyi andırır. Latince adı da Yunanca “kirpi” anlamındaki ekhinos kelimesinden gelir.'),
    gelenek=('Ovaların ilacı', 'Büyük Ovalar’ın yerli halkları kökünü yılan ısırığında, diş ağrısında ve yaralarda çiğner ya da sürerdi.'),
    bilim=('Küçük bir fark olabilir', 'Soğuk algınlığını önlemede ya da kısaltmada küçük bir etkisi olabilir, ancak sonuçlar tutarsız. Avrupa’da kısa süreli kullanımı kabul görüyor.'),
    dikkat=['Papatyagillere alerjisi olanlar', 'Otoimmün hastalığı olanlar'], dikkat_not='Kısa süreli kullanılmalıdır.',
    nasil=('Ne zaman kullanılır?', 'Kullanılacaksa ilk belirtilerde başlanır ve birkaç gün sürdürülür; yıl boyunca her gün alınmaz.'),
    kaydet='Kış için kaydedin.', soru='Soğuk algınlığında ilk neye başvuruyorsunuz?'),

'ashwagandha': dict(
    ilk='Ashwagandha: popüler stres takviyesi ne kadar güvenli? 🌿', kapak='Popüler stres takviyesi ne kadar güvenli?',
    aciklama='Ashwagandha son yıllarda stres ve uyku için en çok satılan takviyelerden biri oldu. Ancak yapılan çalışmalar kısa süreli; uzun süre kullanmanın güvenliği bilinmiyor.',
    kisaca=[('Kökeni', 'Hindistan'), ('Kullanım alanı', 'Stres, uyku ve dayanıklılık'), ('Bilimsel kanıt', 'Küçük ve kısa süreli çalışmalar')],
    hikaye=('Adı “at kokusu” demek', 'Sanskritçe adı “at kokusu” anlamına gelir. Patlıcanın ve domatesin akrabasıdır; meyvesi ince bir kılıf içinde duran küçük, kırmızı bir kirazdır.'),
    gelenek=('Ayurveda’nın gençleştiricisi', 'Ayurveda’da güç ve dayanıklılık veren bir bitki olarak bilinir. Kök tozu sütle kaynatılarak içilir.'),
    bilim=('Uzun vadeli güvenliği bilinmiyor', 'Birkaç küçük çalışmada stres ve kaygıda azalma bildirildi. Ancak çalışmalar kısa süreli ve uzun vadeli güvenlik henüz bilinmiyor.'),
    dikkat=['Hamileler (kullanmamalı)', 'Tiroit hastaları', 'Karaciğer hastaları'], dikkat_not='Karaciğer hasarı vakaları bildirildi; bazı Avrupa ülkeleri takviyelerini kısıtladı.',
    nasil=('Takviye almadan önce', 'Mutlaka hekiminize ya da eczacınıza danışın.'),
    kaydet='Takviye almadan önce bakmak için kaydedin.', soru='Ashwagandha kullandınız mı?'),

'melisa': dict(
    ilk='Melisa, yani oğul otu: arıları neden çeker? 🐝', kapak='Arıları neden bu kadar çeker?',
    aciklama='Melisanın adı, Yunanca bal arısı anlamına geliyor. Çayı ise hafif stres ve uyku sorunlarında Avrupa’da geleneksel olarak kabul görüyor.',
    kisaca=[('Kökeni', 'Anadolu ve Akdeniz'), ('Geleneksel kullanımı', 'Stres, uyku ve sindirim'), ('Bilimsel kanıt', 'Geleneksel; küçük çalışmalar olumlu')],
    hikaye=('Adı “bal arısı” demek', 'Melissa, Yunanca bal arısı demektir. Arıcılar kovanları oğul otuyla ovarak arı oğulunu kovana çeker.'),
    gelenek=('Sinirleri yatıştıran çay', 'Anadolu’da oğul otu adıyla bilinir. Çayı sinirleri yatıştırmak ve uykuya dalmak için içilir.'),
    bilim=('Hafif streste kabul görüyor', 'Avrupa İlaç Ajansı melisayı hafif stres, uyku sorunları ve hazımsızlıkta geleneksel kullanımda tanıyor. Küçük çalışmaların sonuçları da olumlu.'),
    dikkat=['Tiroit ilacı kullananlar'], dikkat_not='Çoğu kişi için güvenlidir.',
    nasil=('Limon kokulu bir çay', 'Bir avuç taze ya da bir tatlı kaşığı kuru yaprağı 10 dakika demleyin.'),
    kaydet='Yorucu bir gün için kaydedin.', soru='Oğul otu çayını denediniz mi?'),

'kantaron': dict(
    ilk='Sarı kantaron: kanıtı güçlü, riski büyük 💛', kapak='Kanıtı güçlü, riski büyük',
    aciklama='Sarı kantaron, hafif depresyonda bazı ilaçlara yakın etki gösteren nadir bitkilerden biri. Ancak pek çok ilacın etkisini azalttığı için en dikkat edilmesi gereken bitkilerin de başında geliyor.',
    kisaca=[('Kökeni', 'Anadolu ve Avrupa'), ('Kullanım alanı', 'Hafif depresyon; yağı yara ve yanıkta'), ('Bilimsel kanıt', 'Hafif ve orta depresyonda güçlü')],
    hikaye=('Kırmızı yağ, sarı çiçek', 'Türkçede kantaron iki ayrı bitkinin adıdır: sarı kantaron ve kırmızı kantaron. Kırmızı renkli kantaron yağı ise sarı kantarondan yapılır.'),
    gelenek=('Güneşte demlenen yağ', 'Anadolu’da çiçekleri zeytinyağında güneşte bekletilir ve kırmızı kantaron yağı elde edilir. Bu yağ yanıkta ve yarada kullanılır.'),
    bilim=('Depresyonda etkili', 'Cochrane derlemesine göre standart ekstreler hafif ve orta depresyonda plasebodan üstün, bazı antidepresanlara yakın etki gösteriyor.'),
    dikkat=['Doğum kontrol hapı kullananlar', 'Kan sulandırıcı ilaç kullananlar', 'Antidepresan ya da düzenli ilaç kullananlar'], dikkat_not='Pek çok ilacın etkisini azaltır; mutlaka hekime danışılmalıdır.',
    nasil=('Kantaron yağı', 'Taze çiçekler zeytinyağıyla bir kavanoza konur ve birkaç hafta güneşte bekletilir. Yağ dıştan kullanılır.'),
    kaydet='Hatırlamak için kaydedin.', soru='Evinizde kantaron yağı var mı?'),

'ceviz': dict(
    ilk='Ceviz ağacının altında neden domates yetişmez? 🌰', kapak='Ağacının altında neden domates yetişmez?',
    aciklama='Ceviz ağacı, köklerinden ve yapraklarından toprağa geçen bir maddeyle çevresindeki bitkilerin büyümesini engeller. Cevizin kendisi ise kolesterol üzerindeki etkisi en iyi kanıtlanmış besinlerden biri.',
    kisaca=[('Kökeni', 'Anadolu, Kafkasya ve İran'), ('Kullanım alanı', 'Kolesterol; yaprağı ciltte'), ('Bilimsel kanıt', 'Cevizde güçlü, yaprakta zayıf')],
    hikaye=('Komşusunu istemeyen ağaç', 'Cevizin kökünden ve yaprağından toprağa juglon adlı bir madde geçer. Bu madde, başka bitkilerin büyümesini engeller.'),
    gelenek=('Boyadan reçele', 'Yeşil kabuğu yüne ve halıya kahverengi renk verir. Yeşil cevizden reçel yapılır; yaprak çayı ise halk arasında şeker için içilir.'),
    bilim=('Kolesterolde kanıtlı', 'Pek çok kontrollü çalışma, düzenli ceviz tüketiminin LDL kolesterolü düşürdüğünü gösterdi. Yaprağı için kanıt ise zayıf.'),
    dikkat=['Ceviz alerjisi olanlar', 'Hamileler (yaprak çayı)'], dikkat_not='Yeşil kabuk elleri kahverengiye boyar.',
    nasil=('Günde bir avuç', 'Çalışmalarda genellikle günde bir avuç kadar (yaklaşık 30 gram) ceviz kullanıldı.'),
    kaydet='Kahvaltı için kaydedin.', soru='Yeşil ceviz reçelini sever misiniz?'),

'rezene': dict(
    ilk='Rezene çayı bebeklere verilir mi? 🌾', kapak='Bebeklere verilir mi?',
    aciklama='Rezene, gaz sancısında en çok başvurulan çaylardan biri. Ancak içerdiği estragol nedeniyle küçük çocuklarda ve hamilelikte uzun süre kullanılmaması öneriliyor.',
    kisaca=[('Kökeni', 'Akdeniz ve Ege'), ('Geleneksel kullanımı', 'Gaz, şişkinlik ve adet sancısı'), ('Bilimsel kanıt', 'Sindirimde kabul görüyor')],
    hikaye=('Maraton bir rezene ovası', 'Maraton adı, Atina yakınlarındaki rezene tarlalarıyla dolu ovadan gelir. Yunanca marathon, rezene demektir.'),
    gelenek=('Annelerin çayı', 'Bebeklerde gaz sancısında ve emziren annelerde süt artırmak için içilir. Ege’de yumrusu ve sapı yemeklere girer.'),
    bilim=('Sindirimde kabul görüyor', 'Avrupa İlaç Ajansı rezene tohumunu hafif sindirim şikâyetleri, gaz ve adet sancısında tanıyor.'),
    dikkat=['Küçük çocuklar (uzun süreli kullanım)', 'Hamileler (uzun süreli kullanım)', 'Kereviz ya da havuç alerjisi olanlar'], dikkat_not='Kısa süreli kullanılmalıdır.',
    nasil=('Rezene çayı', 'Bir çay kaşığı tohumu hafifçe ezin ve bir bardak kaynar suda 10 dakika demleyin.'),
    kaydet='Gerektiğinde bakmak için kaydedin.', soru='Rezeneyi yemeklerde de kullanıyor musunuz?'),

'karanfil': dict(
    ilk='Diş ağrısında neden karanfil kullanılır? 🟤', kapak='Diş ağrısında neden karanfil?',
    aciklama='Karanfilin diş ağrısındaki kullanımı yalnızca bir halk geleneği değil. İçerdiği öjenol, diş hekimliğinde uzun süredir ağrı kesici olarak kullanılıyor.',
    kisaca=[('Kökeni', 'Endonezya’nın Baharat Adaları'), ('Geleneksel kullanımı', 'Diş ağrısı ve ağız iltihabı'), ('Bilimsel kanıt', 'Diş hekimliğinde kullanılıyor')],
    hikaye=('Çocukla birlikte dikilen ağaç', 'Maluku Adaları’nda bir çocuk doğduğunda karanfil ağacı dikilirdi. Ağacın sağlığı, çocuğun sağlığıyla bir tutulurdu.'),
    gelenek=('Dişin yanına bir tane', 'Anadolu’da ağrıyan dişin yanına bir tane karanfil konur. Kış çaylarına, komposto ve hoşaflara da katılır.'),
    bilim=('Öjenolün etkisi', 'Karanfil yağındaki öjenol, diş hekimliğinde lokal ağrı kesici ve antiseptik olarak uzun süredir kullanılıyor.'),
    dikkat=['Saf yağı yutmayın; çocuklar için tehlikelidir', 'Diş etine sık sürmeyin', 'Kan sulandırıcı ilaç kullananlar'], dikkat_not='Baharat olarak güvenlidir.',
    nasil=('Doğal oda kokusu', 'Bir portakalın kabuğuna karanfil tanelerini batırın ve odanıza asın. Hem güzel kokar hem uzun süre dayanır.'),
    kaydet='Diş ağrısında hatırlamak için kaydedin.', soru='Karanfili en çok nerede kullanıyorsunuz?'),

'aloe': dict(
    ilk='Aloe vera: jeli ile özsuyu aynı şey değil 🪴', kapak='Jeli ile özsuyu aynı şey değil',
    aciklama='Aloe yaprağının içindeki şeffaf jel ciltte kullanılır. Yaprağın kabuğundan akan sarı özsu ise güçlü bir müshildir ve içilmesi önerilmez.',
    kisaca=[('Kökeni', 'Arap Yarımadası ve Afrika'), ('Kullanım alanı', 'Yanık ve güneş yanığı'), ('Bilimsel kanıt', 'Jelde küçük çalışmalar olumlu')],
    hikaye=('“Sarısabır” nereden geliyor?', 'Aloenin Arapça adı sabir’dir. Osmanlı eczacılığındaki “sarısabır” adı da buradan gelir.'),
    gelenek=('Saksıdaki ilk yardım', 'Akdeniz’deki evlerde saksıda yetiştirilir. Yaprağın jeli yanığa ve güneş yanığına sürülür.'),
    bilim=('Jel ciltte, özsu değil', 'Jelin hafif yanıklarda iyileşmeyi hızlandırabileceğini gösteren küçük çalışmalar var. Sarı özsu ise güçlü bir müshil olduğu için içilmesi önerilmiyor.'),
    dikkat=['Yaprak özsuyunu içmeyin', 'Hamileler (ağızdan kullanım)'], dikkat_not='Jel, cilde sürüldüğünde genellikle güvenlidir.',
    nasil=('Jeli doğru almak', 'Kestiğiniz yaprağı, sarı özsuyu aksın diye birkaç dakika dik bekletin. Ardından içindeki şeffaf jeli kaşıkla alın.'),
    kaydet='Yaz için kaydedin.', soru='Evinizde aloe yetiştiriyor musunuz?'),

'incir': dict(
    ilk='İncir, buğdaydan önce mi evcilleştirildi? 🍃', kapak='Buğdaydan önce incir mi?',
    aciklama='Ürdün Vadisi’nde bulunan 11.400 yıllık incirler, incirin bilinen en eski tarım ürünlerinden biri olabileceğini düşündürüyor. Yaprağı ise güneşle birleştiğinde cildi yakabiliyor.',
    kisaca=[('Kökeni', 'Ege, Akdeniz ve Orta Doğu'), ('Geleneksel kullanımı', 'Kabızlık; sütü siğilde'), ('Bilimsel kanıt', 'Kabızlıkta küçük çalışmalar')],
    hikaye=('11.400 yıllık incirler', 'Ürdün Vadisi’nde bulunan 11.400 yıllık incirler, incirin buğdaydan yaklaşık bin yıl önce evcilleştirilmiş olabileceğini düşündürüyor.'),
    gelenek=('Aydın’ın “ileklemesi”', 'Aydın’da dişi incir ağaçlarına erkek incir dalları asılır; küçük bir arı türü tozlaşmayı sağlar. Kur’an’daki Tîn suresi de incir ve zeytin üzerine yeminle başlar.'),
    bilim=('Lif bakımından zengin', 'Kuru incir lif bakımından zengindir; kabızlıkta faydasını gösteren birkaç küçük çalışma bulunuyor.'),
    dikkat=['Yaprak ve dal sütü cilde değdiyse güneşe çıkmayın', 'Kuru incirin şekeri yüksektir'], dikkat_not='İncir yaprağıyla bronzlaşmaya çalışanlarda ciddi yanıklar görüldü.',
    nasil=('Kabızlık için kuru incir', 'Akşamdan iki üç kuru inciri suda bekletin; sabah suyuyla birlikte yiyin.'),
    kaydet='Hatırlamak için kaydedin.', soru='Ege inciri mi, Güneydoğu inciri mi?'),

'kusburnu': dict(
    ilk='Kuşburnu çayında C vitamini kalıyor mu? 🔴', kapak='Çayında C vitamini kalıyor mu?',
    aciklama='Taze kuşburnu C vitamini bakımından çok zengin. Ancak kurutma ve kaynatma bu vitaminin büyük kısmını yok ediyor.',
    kisaca=[('Kökeni', 'Bütün Anadolu; Gümüşhane ve Bayburt'), ('Geleneksel kullanımı', 'Soğuk algınlığı ve eklem ağrısı'), ('Bilimsel kanıt', 'Diz ağrısında birkaç küçük çalışma')],
    hikaye=('Savaş yıllarının vitamini', 'İkinci Dünya Savaşı’nda narenciye gelmeyen İngiltere’de, çocuklar C vitamini için kuşburnu toplamaya seferber edildi.'),
    gelenek=('Marmelat, pekmez ve çay', 'Kışın soğuk algınlığına karşı içilir. Gümüşhane ve Bayburt’un bilinen yöresel ürünlerindendir.'),
    bilim=('Taze ve kuru arasında fark var', 'Kurutma ve kaynatma C vitaminini büyük ölçüde azaltır. Kuşburnu tozunun diz kireçlenmesinde ağrıyı hafifletebileceğini gösteren birkaç çalışma var.'),
    dikkat=['Çekirdek tüylerini süzmeden tüketmeyin'], dikkat_not='Çoğu kişi için güvenlidir.',
    nasil=('Vitamini korumak için', 'Çayı kaynatmayın. Kaynamış suyu biraz soğutun, kuşburnunu 10 dakika demleyin ve tülbentten süzün.'),
    kaydet='Kış için kaydedin.', soru='Kuşburnunu marmelat olarak mı, çay olarak mı seversiniz?'),

'feslegen': dict(
    ilk='Fesleğen ile reyhan aynı bitki mi? 🌿', kapak='Fesleğen ile reyhan aynı mı?',
    aciklama='Fesleğen ve reyhan aynı türün farklı adları. Mor reyhan ise bu türün koyu renkli bir çeşidi.',
    kisaca=[('Kökeni', 'Hindistan’dan Anadolu’ya'), ('Geleneksel kullanımı', 'Mutfak; halk arasında sindirim'), ('Bilimsel kanıt', 'Geleneksel; insan çalışması az')],
    hikaye=('İki dilde iki ad', 'Batı dillerindeki adı, Yunanca “kraliyet otu” anlamındaki basilikon’dan gelir. Türkçedeki reyhan ise Arapçada “güzel kokulu bitki” demektir.'),
    gelenek=('Türkülerin bitkisi', 'Pencere önlerinde yetiştirilir ve türkülerde sevgilinin simgesidir. Doğu Anadolu’da mor reyhandan şerbet yapılır.'),
    bilim=('Laboratuvarda umut verici', 'Antimikrobiyal ve iltihap giderici etkileri hayvan çalışmalarında görüldü. İnsanlarda yapılmış çalışma ise yok denecek kadar az.'),
    dikkat=['Hamileler ve çocuklar (uçucu yağ)', 'Varfarin kullananlar (birden çok miktarda tüketmemeli)'], dikkat_not='Yemeklerde ve çayda güvenlidir.',
    nasil=('Reyhan şerbeti', 'Mor reyhan yapraklarını sıcak suda demleyin, süzün ve soğutun. Limon ve şekerle karıştırarak servis edin.'),
    kaydet='Yaz için kaydedin.', soru='Siz bu bitkiye reyhan mı, fesleğen mi diyorsunuz?'),

'ginkgo': dict(
    ilk='Ginkgo hafızayı gerçekten güçlendirir mi? 🍂', kapak='Hafızayı gerçekten güçlendirir mi?',
    aciklama='Ginkgo, yüz milyonlarca yıllık bir soyun yaşayan son temsilcisi. Hafıza üzerindeki etkisi ise büyük bir çalışmayla sorgulandı.',
    kisaca=[('Kökeni', 'Çin’in tapınak bahçeleri'), ('Öne çıkan iddialar', 'Hafıza ve kan dolaşımı'), ('Bilimsel kanıt', 'Demansı önlemiyor')],
    hikaye=('Yaşayan bir fosil', 'Ginkgo, 200 milyon yıllık bir soyun yaşayan tek üyesi. Dinozorlarla aynı dönemde yaşamış ağaçların son temsilcisi.'),
    gelenek=('Hiroşima’dan sağ çıkan ağaç', 'Hiroşima’daki atom bombasından sağ kurtulan ginkgo ağaçları, bugün barışın ve dayanıklılığın simgesi.'),
    bilim=('Büyük bir çalışma, net bir sonuç', 'Standart ekstresi Avrupa’da yaşa bağlı hafif unutkanlıkta kabul görüyor. Ancak ABD’de yapılan büyük bir çalışma, ginkgonun yaşlılarda demansı önlemediğini gösterdi.'),
    dikkat=['Kan sulandırıcı ilaç kullananlar', 'Ameliyat olacaklar', 'Nöbet geçirenler'], dikkat_not='Çiğ tohumları zehirlidir.',
    nasil=('Ginkgoyu tanımak', 'Yelpaze biçimli yapraklarından kolayca tanınır. Sonbaharda altın sarısına döner; Türkiye’de de park ağacı olarak yetiştirilir.'),
    kaydet='Hatırlamak için kaydedin.', soru='Yakınınızda bir ginkgo ağacı var mı?'),

'anason': dict(
    ilk='Rakı suyla karışınca neden beyazlaşır? Cevap anasonda 🤍', kapak='Rakı neden beyazlaşır?',
    aciklama='Rakıyı beyazlatan, anasonun içerdiği anetol. Anason çayı ise Avrupa’da hafif sindirim şikâyetlerinde geleneksel olarak kabul görüyor.',
    kisaca=[('Kökeni', 'Göller Bölgesi ve Ege'), ('Geleneksel kullanımı', 'Gaz, hazımsızlık ve öksürük'), ('Bilimsel kanıt', 'Geleneksel kullanımı kabul görüyor')],
    hikaye=('“Uzo etkisi”', 'Anasondaki anetol alkolde çözünür, suda çözünmez. Su eklenince küçük damlacıklar oluşur ve ışığı saçar; rakı bu yüzden beyazlaşır.'),
    gelenek=('Rakıdan çaya', 'Anason çayı gaz, hazımsızlık ve öksürük için içilir; emziren annelere süt artırmak için verilir.'),
    bilim=('Sindirimde kabul görüyor', 'Avrupa İlaç Ajansı anasonu hafif hazımsızlık, gaz ve öksürükte geleneksel kullanımda tanıyor.'),
    dikkat=['Kereviz ya da rezene alerjisi olanlar', 'Hamileler ve çocuklar (uçucu yağ)', 'Bebeklere vermeden önce hekime danışılmalı'], dikkat_not='Çay olarak genellikle güvenlidir.',
    nasil=('Anason çayı', 'Bir çay kaşığı tohumu hafifçe ezin ve bir bardak kaynar suda 10 dakika demleyin.'),
    kaydet='Sofrada anlatmak için kaydedin.', soru='Bu bilgiyi daha önce duymuş muydunuz?'),

'sarimsak': dict(
    ilk='Sarımsak: iki kıtada aynı nazar koruyucusu 🧄', kapak='İki kıtada aynı nazar koruyucusu',
    aciklama='Sarımsak hem Anadolu’da hem And Dağları’nda nazara karşı taşınıyor. Bilim ise tansiyon ve kolesterol üzerinde küçük ama gerçek bir etki gösteriyor.',
    kisaca=[('Kökeni', 'Anadolu’dan And Dağları’na'), ('Kullanım alanı', 'Tansiyon, kolesterol ve soğuk algınlığı'), ('Bilimsel kanıt', 'Tansiyonda küçük ama gerçek bir etki')],
    hikaye=('Aynı bitki, aynı görev', 'Anadolu’da sarımsak kapıya ve beşik başına nazara karşı asılır. Peru ve Bolivya’da da aynı amaçla yanda taşınır.'),
    gelenek=('Çiğ yemenin sırrı', 'Soğuk algınlığında ve tansiyonda çiğ olarak yenir. Ezildiğinde oluşan allisin, hem kokusunun hem etkisinin kaynağıdır.'),
    bilim=('Küçük ama gerçek bir etki', 'Meta-analizler, sarımsak preparatlarının tansiyonu ve kolesterolü hafifçe düşürdüğünü gösteriyor.'),
    dikkat=['Kan sulandırıcı ilaç kullananlar', 'Ameliyat olacaklar'], dikkat_not='Yemeklerde güvenlidir.',
    nasil=('Ezin ve bekletin', 'Sarımsağı ezdikten sonra 10 dakika bekletip öyle pişirin. Allisin bu sürede oluşur.'),
    kaydet='Mutfakta denemek için kaydedin.', soru='Sizin evinizde de nazara karşı sarımsak asılır mıydı?'),

'keten': dict(
    ilk='Keten tohumu: hem kumaş hem şifa 🌾', kapak='Hem kumaş hem şifa',
    aciklama='Keten, insanlığın en eski dokuma liflerinden biri. Tohumu ise kabızlıkta etkisi kabul görmüş, lif bakımından zengin bir besin.',
    kisaca=[('Kökeni', 'Anadolu’dan And Dağları’na'), ('Kullanım alanı', 'Kabızlık ve kolesterol'), ('Bilimsel kanıt', 'Kabızlıkta güçlü')],
    hikaye=('En eski kumaşlardan', 'Keten, insanlığın en eski dokuma liflerinden biri. Anadolu’da Neolitik çağdan kalma keten kumaş parçaları bulundu.'),
    gelenek=('Peru’nun sabah içeceği', 'Anadolu’da kabızlık için tohum suda bekletilerek içilir. Peru’da ise linaza adıyla sokaklarda sabah içeceği olarak satılır.'),
    bilim=('Kabızlıkta kabul görüyor', 'Avrupa İlaç Ajansı keten tohumunu kabızlıkta yerleşik kullanımda tanıyor. Kolesterolde hafif düşüş gösteren çalışmalar da var.'),
    dikkat=['Bol suyla tüketilmeli; az suyla bağırsakta tıkanma yapabilir', 'Çiğ tohum ölçülü tüketilmeli'], dikkat_not='',
    nasil=('Öğüterek kullanın', 'Bütün tohum çoğu zaman sindirilmeden geçer. Öğütüp yoğurda ya da salataya ekleyin ve yanında bol su için.'),
    kaydet='Kahvaltı için kaydedin.', soru='Keten tohumunu nasıl tüketiyorsunuz?'),

'turunc': dict(
    ilk='Turunç: zayıflama haplarındaki acı portakal 🍊', kapak='Zayıflama haplarındaki acı portakal',
    aciklama='Turunç, “yağ yakıcı” takviyelere sinefrin kaynağı olarak ekleniyor. Bu iddiayı destekleyen kanıt ise zayıf; üstelik kalp üzerinde riskleri olabiliyor.',
    kisaca=[('Kökeni', 'Antalya’dan Hatay’a; Sevilla'), ('Kullanım alanı', 'Reçel ve sos; zayıflama takviyeleri'), ('Bilimsel kanıt', 'Kilo kaybında belirsiz')],
    hikaye=('Avrupa’nın ilk portakalı', 'Avrupa’ya ilk ulaşan turunçgil tatlı portakal değil, Araplarla Endülüs’e gelen acı portakaldı. Sevilla’nın sokakları bugün hâlâ turunç ağaçlarıyla dolu.'),
    gelenek=('Limonun yerine turunç', 'Kabuğundan reçel yapılır; ekşi suyu salatalarda limon yerine kullanılır. Çiçeğinden ise portakal çiçeği suyu damıtılır.'),
    bilim=('“Yağ yakıcı” iddiası zayıf', 'Takviyelerdeki sinefrinin kilo kaybına etkisi küçük ve belirsiz. Kafeinle birlikte kullanılan ürünlerde çarpıntı ve inme vakaları bildirildi.'),
    dikkat=['Kalp hastaları (takviye kullanmamalı)', 'Yüksek tansiyonu olanlar', 'Düzenli ilaç kullananlar (greyfurt gibi etkileşir)'], dikkat_not='Meyve ve reçel olarak güvenlidir.',
    nasil=('Turunç reçeli', 'Kabukları ince şeritler hâlinde kesin. Acılığı gitsin diye birkaç kez haşlayıp suyunu dökün, ardından şekerle pişirin.'),
    kaydet='Kış reçeli için kaydedin.', soru='Turunç reçelini sever misiniz?'),

'meyan': dict(
    ilk='Meyan kökü: şekerden 50 kat tatlı 🍂', kapak='Şekerden 50 kat tatlı bir kök',
    aciklama='Meyan kökünün tatlılığı, glisirizin adlı bir maddeden geliyor. Aynı madde, düzenli ve fazla tüketildiğinde tansiyonu yükseltiyor.',
    kisaca=[('Kökeni', 'Güneydoğu Anadolu ve Asya'), ('Geleneksel kullanımı', 'Öksürük ve mide yanması'), ('Bilimsel kanıt', 'Geleneksel kullanımı kabul görüyor')],
    hikaye=('Sigaranın gizli tadı', 'Meyan kökünün dünyadaki en büyük alıcılarından biri tütün sanayisi. Kök, sigaraya tat vermek için kullanılıyor.'),
    gelenek=('Ramazan şerbeti', 'Güneydoğu Anadolu’da Ramazan’da meyan şerbeti içilir. Çin tıbbında ise diğer bitkileri “uyumlu hâle getirdiği” düşünülerek reçetelere eklenir.'),
    bilim=('Tatlılığın iki yüzü', 'Avrupa İlaç Ajansı meyanı öksürükte ve hafif mide şikâyetlerinde tanıyor. Ancak tatlılığını veren glisirizin, fazla tüketildiğinde tansiyonu yükseltir.'),
    dikkat=['Yüksek tansiyonu olanlar', 'Kalp ya da böbrek hastaları', 'Hamileler'], dikkat_not='Her gün ve çok miktarda tüketilmemelidir.',
    nasil=('Meyan şerbeti', 'Ezilmiş kökü bir gece soğuk suda bekletip süzün. Bol suyla ve ölçülü için.'),
    kaydet='Ramazan için kaydedin.', soru='Meyan şerbetini hiç içtiniz mi?'),

'defne': dict(
    ilk='Defne: Hatay’ın ünlü sabununun sırrı 🌿', kapak='Hatay’ın ünlü sabununun sırrı',
    aciklama='Defne yaprağı mutfağımızın sessiz bir parçası. Meyvesinin yağı ise zeytinyağıyla birleşerek Hatay’ın ünlü defne sabununa dönüşüyor.',
    kisaca=[('Kökeni', 'Akdeniz; Hatay’ın defne koruları'), ('Kullanım alanı', 'Mutfak, sabun ve romatizma ağrısı'), ('Bilimsel kanıt', 'İnsan çalışması çok az')],
    hikaye=('Antakya’nın eski adı', 'Antakya’nın Harbiye semtinin antik adı Daphne’dir. Burası Apollon tapınağı ve defne korularıyla ünlüydü.'),
    gelenek=('Kazananların tacı', 'Antik Yunan’da kazananlara defne yapraklarından taç verilirdi. Hatay’da meyve yağı zeytinyağıyla karıştırılarak sabun yapılır.'),
    bilim=('Laboratuvarda antimikrobiyal', 'Yaprak yağındaki sineol, laboratuvar çalışmalarında antimikrobiyal etki gösteriyor. İnsanlarda yapılmış çalışma ise çok az.'),
    dikkat=['Kuru yaprağı bütün hâlde yutmayın', 'Hassas cildi olanlar yağı önce küçük bir alanda denemeli'], dikkat_not='Mutfakta güvenlidir.',
    nasil=('Dolaplar için defne', 'Birkaç kuru defne yaprağını dolaplara ve un kavanozlarına koyun. Halk arasında güveyi uzak tuttuğuna inanılır.'),
    kaydet='Hatırlamak için kaydedin.', soru='Defne sabunu kullanıyor musunuz?'),

'kakule': dict(
    ilk='Kakule neden bu kadar pahalı? 💚', kapak='Neden bu kadar pahalı?',
    aciklama='Kakule, safran ve vanilyayla birlikte dünyanın en pahalı baharatları arasında. Bunun nedeni, kapsüllerinin olgunlaşmadan tek tek elle toplanması.',
    kisaca=[('Kökeni', 'Güney Hindistan; bugün en çok Guatemala'), ('Geleneksel kullanımı', 'Sindirim ve ağız kokusu'), ('Bilimsel kanıt', 'Küçük çalışmalarda hafif etki')],
    hikaye=('Tek tek, elle', 'Kakule kapsülleri olgunlaşmadan, tek tek elle toplanır. Bu yüzden safran ve vanilyayla birlikte en pahalı baharatlar arasında yer alır.'),
    gelenek=('Kahvenin eşlikçisi', 'Arap kahvesi kakuleyle demlenir; Güneydoğu Anadolu’da ve Hatay’da da kahveye kakule katılır. Hindistan’da ise masala çayının vazgeçilmezidir.'),
    bilim=('Hafif ve tutarsız etkiler', 'Küçük çalışmalarda tansiyonu ve bazı iltihap göstergelerini biraz düşürdüğü görüldü. Kolesterol ve kan şekerinde ise sonuçlar tutarsız.'),
    dikkat=['Hamileler (yüksek doz takviye)'], dikkat_not='Baharat olarak güvenlidir.',
    nasil=('Kakuleli kahve', 'Bir iki kakule tanesini hafifçe ezin ve kahveyle birlikte pişirin.'),
    kaydet='Kahve keyfi için kaydedin.', soru='Kahvenize kakule ekler misiniz?'),

'enginar': dict(
    ilk='Enginarın yediğimiz kısmı aslında bir çiçek 💜', kapak='Yediğimiz kısım aslında bir çiçek',
    aciklama='Enginar, açmamış bir çiçek başı. Yaprağı ise Avrupa’da hafif hazımsızlıkta geleneksel olarak kabul görüyor.',
    kisaca=[('Kökeni', 'Ege ve İstanbul mutfağı'), ('Geleneksel kullanımı', 'Hazımsızlık ve şişkinlik'), ('Bilimsel kanıt', 'Geleneksel; küçük çalışmalar olumlu')],
    hikaye=('Açarsa mor bir çiçeğe dönüşür', 'Enginarın yediğimiz kısmı açmamış bir çiçek başıdır. Toplanmazsa mor, devedikenine benzeyen bir çiçeğe dönüşür.'),
    gelenek=('Baharın müjdecisi', 'Zeytinyağlı enginar, Ege ve İstanbul mutfağında baharın gelişini müjdeler. Haşlama suyu ve yaprak çayı karaciğer ve safra için içilir.'),
    bilim=('Hazımsızlıkta kabul görüyor', 'Avrupa İlaç Ajansı enginar yaprağını hafif hazımsızlık ve şişkinlikte geleneksel kullanımda tanıyor.'),
    dikkat=['Safra taşı ya da safra yolu tıkanıklığı olanlar', 'Papatyagillere alerjisi olanlar'], dikkat_not='Yemek olarak güvenlidir.',
    nasil=('Kararmasını önlemek için', 'Temizlediğiniz enginarı hemen limonlu suya atın; havayla temas edince kararır.'),
    kaydet='Bahar için kaydedin.', soru='Zeytinyağlı enginar sever misiniz?'),
}
