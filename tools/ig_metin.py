# Instagram için elle yazılmış, sade ve sohbet diliyle metinler.
# Her bitki: kapak sorusu, kısaca (3 satır), hikâye, gelenek, bilim, dikkat, nasıl, kayıt cümlesi, yorum sorusu.
# Bilgiler katalogdaki kayıtla aynıdır (kaynaklar sitede); burada yalnızca dil sadeleşir.
# Metni olmayan bitkiler tools/ig2.py içinde katalog verisinden otomatik sadeleştirilir.

M = {
'zencefil': dict(
    kapak='Bulantıya gerçekten iyi gelir mi?', emoji='🫚',
    kisaca=[('Nereden', 'Hindistan ve Çin; Osmanlı mutfağında da baş baharat'), ('Ne için', 'Bulantı, soğuk algınlığı, hazımsızlık'), ('Kanıt', 'Bulantıda iyi. Gerisinde zayıf')],
    hikaye=('Kimse onu yabanda görmedi', 'Zencefilin yabani hâli bilinmiyor. Binlerce yıldır yalnızca insan eliyle, kök parçalarından çoğaltılıyor.'),
    gelenek=('Ayurveda’da adı: “evrensel ilaç”', 'Çin’de taze kökü kaynatılıp soğuk algınlığında içilir. Osmanlı macunlarında da hep vardı.'),
    bilim=('İşe yaradığı yer: bulantı', 'Avrupa İlaç Ajansı taşıt tutmasında kullanımını kabul ediyor. Hamilelik bulantısında küçük çalışmalar olumlu. Eklem ağrısı ve zayıflama iddiaları ise kanıtlanmış değil.'),
    dikkat=['Kan sulandırıcı kullanıyorsan', 'Safra taşın varsa', 'Yüksek doz takviye alacaksan'], dikkat_not='Yemekteki miktar güvenli.',
    nasil=('Zencefil çayı', '3–4 ince dilim taze zencefili bir bardak suda 10 dakika kaynat. Limon ve bal ekle.'),
    kaydet='Kaydet, kışın lazım olacak.', soru='Sen zencefili en çok nasıl kullanıyorsun?'),

'zerdecal': dict(
    kapak='Mucize baharat mı, iyi pazarlama mı?', emoji='🟡',
    kisaca=[('Nereden', 'Hindistan; Anadolu’da zerde tatlısının rengi'), ('Ne için', 'İltihap, eklem ağrısı, sindirim'), ('Kanıt', 'Dizde biraz umut var. Gerisi abartı')],
    hikaye=('Sarısının arkasındaki kurşun', 'Bangladeş’te ucuz zerdeçalın rengi kurşun kromat boyasıyla canlandırıldı. Sonuç: kurşun zehirlenmeleri. Güvenilir yerden almak bu yüzden önemli.'),
    gelenek=('Hint düğünlerinin sarısı', 'Haldi töreninde gelin ve damadın bedenine zerdeçal sürülür. Anadolu’da ise safranın ucuz ikamesi olarak pilava ve zerdeye renk verir.'),
    bilim=('Kurkumin zor emiliyor', 'Diz kireçlenmesinde ağrıyı biraz azaltabildiğini gösteren küçük çalışmalar var. Ama kurkumin vücutta zayıf emilir ve çoğu iddia kanıtlanmış değil.'),
    dikkat=['Kan sulandırıcı kullanıyorsan', 'Safra taşın varsa', 'Yüksek doz kapsül alacaksan (karaciğer hasarı bildirildi)'], dikkat_not='Yemekteki miktar güvenli.',
    nasil=('Altın süt', 'Bir bardak ılık süte yarım çay kaşığı zerdeçal, bir tutam karabiber ve biraz bal ekle. Karabiber emilimi artırır.'),
    kaydet='Kaydet, sonra hatırla.', soru='Zerdeçalı en çok hangi yemeğe katıyorsun?'),

'adacayi': dict(
    kapak='Boğaz ağrısına neden adaçayı?', emoji='🌿',
    kisaca=[('Nereden', 'Ege ve Akdeniz’in kayalık yamaçları'), ('Ne için', 'Boğaz ağrısı, ağız iltihabı, terleme'), ('Kanıt', 'Gargarada geleneksel olarak kabul görüyor')],
    hikaye=('Adı “kurtarmak”tan geliyor', 'Latince adı Salvia, “iyileştirmek, kurtarmak” anlamındaki salvare’den gelir. Orta Çağ Avrupası onu her derde deva sayardı.'),
    gelenek=('Ege’nin kış çayı', 'Köylerde boğaz ağrısı, mide ve soğuk algınlığı için demlenir. Çoğu zaman ıhlamur ve ayva yaprağıyla karıştırılır.'),
    bilim=('Gargarada işe yarıyor', 'Avrupa İlaç Ajansı adaçayını ağız ve boğaz iltihabı ile aşırı terlemede geleneksel kullanımda tanıyor. Anadolu türü daha az tuyon içerir.'),
    dikkat=['Hamileysen ya da emziriyorsan', 'Epilepsin varsa', 'Her gün, uzun süre içeceksen'], dikkat_not='İçindeki tuyon yüksek dozda sinir sistemini etkiler.',
    nasil=('Boğaz gargarası', 'Bir tatlı kaşığı kuru yaprağı bir bardak kaynar suda 10 dakika demle. Ilıyınca gargara yap.'),
    kaydet='Kaydet, boğazın ağrıdığında lazım.', soru='Adaçayını neyle karıştırıp içersin?'),

'ihlamur': dict(
    kapak='Kış akşamlarının çayı neden ıhlamur?', emoji='🍵',
    kisaca=[('Nereden', 'Karadeniz ve Marmara ormanları, şehir sokakları'), ('Ne için', 'Soğuk algınlığı, rahatlamak'), ('Kanıt', 'Geleneksel; klinik çalışma az')],
    hikaye=('Yüzyıllar yaşayan ağaç', 'Bir ıhlamur ağacı birkaç yüz yıl yaşayabilir. Avrupa’da köy meydanlarının, buluşmaların ağacıdır.'),
    gelenek=('Terletip rahatlatan çay', 'Soğuk algınlığında terlemek ve rahatlamak için içilir. İstanbul’un sokaklarında çiçekleri Haziran’da toplanır.'),
    bilim=('Avrupa’da da kabul görüyor', 'Avrupa İlaç Ajansı ıhlamur çiçeğini soğuk algınlığı belirtileri ve hafif stres için geleneksel kullanımda tanıyor. Klinik çalışma ise az.'),
    dikkat=['Bilinen bir yan etkisi yok'], dikkat_not='Genelde güvenli bir çay.',
    nasil=('İyi ıhlamur nasıl seçilir?', 'Sarımsı çiçekler, yaprakçığıyla birlikte ve kokusu güçlü olmalı. Bir tatlı kaşığını 10 dakika demle.'),
    kaydet='Kaydet, kış geliyor.', soru='Ihlamuru ballı mı, limonlu mu içersin?'),

'papatya': dict(
    kapak='Papatya çayı neden uyutur?', emoji='🌼',
    kisaca=[('Nereden', 'Anadolu’dan And Dağları’na'), ('Ne için', 'Mide, uyku, cilt tahrişi'), ('Kanıt', 'Mide ve ciltte kabul görüyor; kaygıda umut verici')],
    hikaye=('Sakinliğin molekülü', 'Papatyadaki apigenin, beyinde sakinleştirici ilaçların bağlandığı reseptörlere bağlanır. Rahatlatıcı etkisinin kaynağı bu olabilir.'),
    gelenek=('İki kıtanın ilk ilacı', 'Anadolu’da mide ağrısı ve uykusuzlukta içilir. Peru ve Bolivya’da manzanilla, mide rahatsızlığında ilk başvurulan ottur.'),
    bilim=('Kanıtı en sağlam çaylardan', 'Avrupa İlaç Ajansı papatyayı hafif sindirim şikâyetleri, ağız-boğaz iltihabı ve cilt tahrişi için tanıyor. Kaygı üzerine küçük çalışmalar olumlu.'),
    dikkat=['Papatyagillere alerjin varsa', 'Kan sulandırıcı kullanıyorsan'], dikkat_not='Çoğu kişi için güvenli.',
    nasil=('Uyku öncesi papatya', 'Bir tatlı kaşığı kuru papatyayı kapağı kapalı 5–10 dakika demle. Yatmadan yarım saat önce iç.'),
    kaydet='Kaydet, uykusuz bir gece için.', soru='Papatya çayı sana gerçekten uyku getiriyor mu?'),

'isirgan': dict(
    kapak='Yakıcı ot neden sofraya girer?', emoji='🌱',
    kisaca=[('Nereden', 'Anadolu’dan And Dağları’na'), ('Ne için', 'Eklem ağrısı, idrar, bahar sofrası'), ('Kanıt', 'Geleneksel olarak kabul görüyor')],
    hikaye=('Isırganla vurmak', 'Ağrıyan ekleme taze ısırganla vurmak Antik Roma’dan beri bilinir. Aynı yöntem Anadolu’da ve And’larda birbirinden habersiz kullanılıyor.'),
    gelenek=('Baharın ilk yeşili', 'Körpe yaprakları çorba, börek ve kavurma olur. And’larda ise ortiga, arınma törenlerinde bedene hafifçe vurulur.'),
    bilim=('Yaprak ve kök ayrı işte', 'Avrupa İlaç Ajansı yaprağı eklem ağrısı ve idrar söktürücü olarak, kökü prostat büyümesine bağlı idrar şikâyetlerinde geleneksel kullanımda tanıyor.'),
    dikkat=['Tansiyon ilacı kullanıyorsan', 'Şeker ilacı kullanıyorsan'], dikkat_not='Taze bitki kaşındırır; eldivenle topla.',
    nasil=('Isırgan çorbası', 'Eldivenle toplanan körpe uçları haşla. Yakıcılığı pişince geçer; ıspanak gibi kullan.'),
    kaydet='Kaydet, baharda topla.', soru='Isırganı en çok nasıl yersin?'),

'nane': dict(
    kapak='Mide için en çok kanıtlanan ot?', emoji='🌿',
    kisaca=[('Nereden', 'Anadolu mutfağından And pazarlarına'), ('Ne için', 'Bulantı, gaz, hazımsızlık'), ('Kanıt', 'Nane yağı kapsülünde güçlü')],
    hikaye=('Bir perinin adı', 'Yunan mitolojisinde Minthe adlı peri, kıskanç Persephone tarafından naneye dönüştürülür. Latince adı buradan gelir.'),
    gelenek=('Ayrandan cacığa', 'Anadolu’da mide bulantısı ve gaz için çayı içilir, kurusu kışın buharla solunur. And’larda hierbabuena en sık demlenen otlardandır.'),
    bilim=('Huzursuz bağırsakta kanıtlı', 'Nane yağı kapsülleri pek çok kontrollü çalışmada huzursuz bağırsak belirtilerini plaseboya göre azalttı. Nane yaprağı hazımsızlıkta geleneksel olarak kabul görüyor.'),
    dikkat=['Reflün varsa', 'Bebeğin ya da küçük çocuğun varsa (saf yağ yüze sürülmez)'], dikkat_not='Çay ve yemek olarak güvenli.',
    nasil=('Taze nane çayı', 'Bir avuç taze yaprağı bardağa koy, üstüne kaynar su dök, 5 dakika beklet.'),
    kaydet='Kaydet, midene iyi gelecek.', soru='Naneyi en çok neye katarsın?'),

'kekik': dict(
    kapak='Kekik tek bir bitki değil', emoji='🌿',
    kisaca=[('Nereden', 'Anadolu’nun dağları; dünyanın en büyük ihracatçısı Türkiye'), ('Ne için', 'Öksürük, soğuk algınlığı, mide'), ('Kanıt', 'Öksürükte geleneksel olarak kabul görüyor')],
    hikaye=('Onlarca bitkinin ortak adı', 'Türkçede kekik, benzer kokulu onlarca türe verilen ortak bir addır. Güneydoğu’nun zahteri de bunlardan biri.'),
    gelenek=('Cesaretin otu', 'Antik Yunan’da cesaretin simgesiydi ve tapınaklarda tütsü olarak yakılırdı. Anadolu’da kekik suyu ve kekik yağı halk ilacıdır.'),
    bilim=('Timolün gücü', 'İçindeki timol ve karvakrol laboratuvarda güçlü antimikrobiyal etki gösterir. Kekik, balgamlı öksürükte geleneksel bitkisel ilaç olarak kabul görüyor.'),
    dikkat=['Saf kekik yağını sulandırmadan cilde sürme', 'Saf yağı asla yutma'], dikkat_not='Mutfaktaki miktar güvenli.',
    nasil=('Öksürük için kekik çayı', 'Bir tatlı kaşığı kuru kekiği bir bardak kaynar suda 5–10 dakika demle. Bal ekle.'),
    kaydet='Kaydet, öksürük mevsimi geliyor.', soru='Senin yöresinde kekiğe ne denir?'),

'biberiye': dict(
    kapak='Hafızanın bitkisi mi?', emoji='🌿',
    kisaca=[('Nereden', 'Akdeniz kıyıları'), ('Ne için', 'Sindirim, kas ağrısı, saç'), ('Kanıt', 'Geleneksel; hafıza iddiası kesin değil')],
    hikaye=('Sınavda saça takılırdı', 'Antik Yunan’da biberiye hafızanın simgesiydi; öğrencilerin sınavda saçlarına taktığı anlatılır. Shakespeare’in Hamlet’inde de bu anlamla geçer.'),
    gelenek=('Bahçeden banyoya', 'Akdeniz’de çit bitkisidir; yağı saç dökülmesi ve kas ağrısında ovulur. Peru’da romero, kötü enerjiyi uzaklaştırmak için banyo suyuna katılır.'),
    bilim=('Hafıza için henüz erken', 'Avrupa İlaç Ajansı biberiyeyi hafif sindirim şikâyetleri ve dıştan kas-eklem ağrısı için tanıyor. Hafıza üzerine küçük çalışmalar var ama sonuç kesin değil.'),
    dikkat=['Epilepsin varsa (yüksek doz yağ)', 'Hamileysen (yüksek doz yağ)'], dikkat_not='Mutfaktaki miktar güvenli.',
    nasil=('Biberiye suyu', 'Bir dal taze biberiyeyi bir litre suda 5 dakika kaynat. Soğuyunca saç durulama suyu olarak kullan.'),
    kaydet='Kaydet, saçına dene.', soru='Biberiyeyi en çok hangi yemekte kullanırsın?'),

'lavanta': dict(
    kapak='Kaygıda gerçekten işe yarıyor mu?', emoji='💜',
    kisaca=[('Nereden', 'Akdeniz; Isparta’nın Kuyucak köyü'), ('Ne için', 'Kaygı, uyku, baş ağrısı'), ('Kanıt', 'Yağ kapsülünde güçlü')],
    hikaye=('Adı “yıkamak”tan', 'Adının Latince lavare, yani yıkamak kökünden geldiği düşünülür. Romalılar banyo suyuna lavanta katardı.'),
    gelenek=('Isparta’nın mor tarlaları', 'Kuyucak köyündeki tarlalar Temmuz’da çiçeklenir ve binlerce kişiyi çeker. Kurusu dolaplara güveye karşı konur.'),
    bilim=('Kaygıda plasebodan iyi', 'Ağızdan alınan standart lavanta yağı kapsülleri birçok kontrollü çalışmada kaygı bozukluğunda plaseboya üstün bulundu.'),
    dikkat=['Sakinleştirici ilaç kullanıyorsan', 'Kapsül bulantı ve geğirme yapabilir'], dikkat_not='Genelde güvenli.',
    nasil=('Yastık kesesi', 'Bir avuç kuru lavantayı küçük bir bez keseye koy, yastığının yanına bırak.'),
    kaydet='Kaydet, uykusuz geceler için.', soru='Kuyucak’ın lavanta tarlalarını gördün mü?'),

'corekotu': dict(
    kapak='Her derde deva mı?', emoji='🖤',
    kisaca=[('Nereden', 'Anadolu, Orta Doğu, Hindistan'), ('Ne için', 'Kolesterol, şeker, tansiyon iddiaları'), ('Kanıt', 'Küçük çalışmalarda hafif etki')],
    hikaye=('Tutankamon’un mezarında', 'Çörek otu tohumları Tutankamon’un mezarında bulundu. Binlerce yıldır değerli bir tohum.'),
    gelenek=('Bir hadisin ünü', '“Ölümden başka her derde deva” olarak anılan bir hadis yüzünden yağı Anadolu’da çok yaygın bir ev ilacıdır.'),
    bilim=('Hafif ama kesin değil', 'Küçük çalışmalarda kolesterol, kan şekeri ve tansiyonda hafif düşüş görüldü. Ama çalışmalar kısa ve kalitesi düşük.'),
    dikkat=['Şeker ilacı kullanıyorsan', 'Tansiyon ilacı kullanıyorsan'], dikkat_not='Pidede, çörekte güvenli.',
    nasil=('Mutfakta çörek otu', 'Tavada birkaç saniye kavur, kokusu çıkınca peynire, salataya ya da pilava serp.'),
    kaydet='Kaydet, unutma.', soru='Çörek otu yağını sen de kullanıyor musun?'),

'dagcayi': dict(
    kapak='Toroslar’ın “adaçayı” aslında ne?', emoji='⛰️',
    kisaca=[('Nereden', 'Toroslar ve Batı Anadolu yaylaları'), ('Ne için', 'Öksürük, soğuk algınlığı, mide'), ('Kanıt', 'Geleneksel olarak kabul görüyor')],
    hikaye=('Türlerin çoğu yalnızca burada', 'Türkiye dağ çayının dünyadaki en zengin yurdu. Burada yetişen türlerin çoğu başka hiçbir yerde yok.'),
    gelenek=('Yaylanın kışlığı', 'Yaz sonu toplanan çiçekli dallar kış çayı olur. Birçok yörede adı adaçayıdır; Yunanistan’da “dağ çayı” diye bilinir.'),
    bilim=('Uzun geçmişe dayanan kabul', 'Avrupa İlaç Ajansı dağ çayını soğuk algınlığındaki öksürük ve hafif mide şikâyetleri için geleneksel kullanımda tanıyor. İnsan çalışması az.'),
    dikkat=['Hamileysen ya da emziriyorsan', 'Küçük çocuklara'], dikkat_not='Yabandan değil, üretilmiş çay al: bazı türler azalıyor.',
    nasil=('Dağ çayı demi', 'Bir avuç kuru dalı kaynamış suda 5–10 dakika demle. Limon ve bal yakışır.'),
    kaydet='Kaydet, kışlığını al.', soru='Senin yöresinde bu çaya ne denir?'),

'atkestanesi': dict(
    kapak='Yenmez ama ilaç olur', emoji='🌰',
    kisaca=[('Nereden', 'Balkan dağları; İstanbul’un parkları'), ('Ne için', 'Bacakta şişlik ve ağırlık'), ('Kanıt', 'Standart ekstrede güçlü')],
    hikaye=('Avrupa’ya İstanbul’dan gitti', 'Ağaç Batı Avrupa’ya 1576’da İstanbul’dan götürüldü. “At kestanesi” adı, Osmanlıların tohumu öksüren atlara verdiği anlatısından gelir.'),
    gelenek=('Saray bahçelerinin ağacı', 'İstanbul’un parklarına, saray ve yalı bahçelerine dikildi. 20. yüzyılda tohumu Avrupa’da damar ilacına dönüştü.'),
    bilim=('Bacak şişliğinde işe yarıyor', 'Cochrane derlemesine göre standart ekstre, toplardamar yetmezliğinde bacak ağrısını, şişliği ve kaşıntıyı kısa sürede plaseboya göre azaltıyor.'),
    dikkat=['Çiğ tohumu asla yeme: zehirli', 'Kan sulandırıcı kullanıyorsan', 'Böbrek ya da karaciğer hastasıysan', 'Hamileysen'], dikkat_not='',
    nasil=('Evde hazırlanmaz', 'Tohumu zehirlidir. Yalnızca eczanede satılan, zehirli maddesi arındırılmış standart ekstre kullanılır.'),
    kaydet='Kaydet, kestaneyle karıştırma.', soru='Çocukken at kestanesi toplar mıydın?'),

'tarcin': dict(
    kapak='Hangi tarçını alıyorsun?', emoji='🤎',
    kisaca=[('Nereden', 'Sri Lanka ve Çin'), ('Ne için', 'Kan şekeri iddiaları, sindirim'), ('Kanıt', 'Tutarsız')],
    hikaye=('Dev kuşların yuvası masalı', 'Herodot, tarçının dev kuşların yuvalarından toplandığını yazar. Tüccarlar gerçek kaynağı gizlemek için bu masalları yaydı.'),
    gelenek=('Sahlepten aşureye', 'Sahlep, aşure, sütlaç ve kış çaylarının vazgeçilmezi. Osmanlı mutfağında etli yemeklerde de kullanılırdı.'),
    bilim=('Şeker için kanıt yetersiz', 'Kan şekeri üzerine çok sayıda küçük çalışma var ama sonuçlar tutarsız. Herhangi bir hastalıkta işe yaradığı gösterilmiş değil.'),
    dikkat=['Her gün çay kaşığıyla tüketiyorsan', 'Karaciğer hastasıysan'], dikkat_not='Markette en çok satılan kasya tarçını çok kumarin içerir; Seylan tarçınında az.',
    nasil=('Seylan mı, kasya mı?', 'Seylan tarçını ince, kat kat ve kolay kırılır. Kasya kalın, sert ve tek kattır.'),
    kaydet='Kaydet, markette bak.', soru='Tarçını en çok neye koyarsın?'),

'ekinezya': dict(
    kapak='Soğuk algınlığını kısaltır mı?', emoji='🌸',
    kisaca=[('Nereden', 'Kuzey Amerika’nın Büyük Ovaları'), ('Ne için', 'Soğuk algınlığı'), ('Kanıt', 'Küçük ve tutarsız etki')],
    hikaye=('Kirpiye benzeyen çiçek', 'Çiçeğinin ortasındaki dikenli koni kirpiyi andırır. Latince adı Yunanca kirpi, ekhinos’tan gelir.'),
    gelenek=('Ovaların ilacı', 'Büyük Ovalar halkları kökünü yılan ısırığı, diş ağrısı ve yaralar için çiğner ya da sürerdi.'),
    bilim=('Küçük bir fark olabilir', 'Soğuk algınlığını önlemede ya da kısaltmada küçük bir etkisi olabilir ama sonuçlar tutarsız. Avrupa’da kısa süreli kullanım için kabul görüyor.'),
    dikkat=['Papatyagillere alerjin varsa', 'Otoimmün bir hastalığın varsa'], dikkat_not='Kısa süreli kullanılır.',
    nasil=('Ne zaman başlanır?', 'Kullanılacaksa ilk belirtilerde başlanır ve birkaç gün sürdürülür; her gün yıl boyu alınmaz.'),
    kaydet='Kaydet, kışa hazırlan.', soru='Soğuk algınlığında ilk neye başvurursun?'),

'ashwagandha': dict(
    kapak='Stres için popüler takviye güvenli mi?', emoji='🌿',
    kisaca=[('Nereden', 'Hindistan'), ('Ne için', 'Stres, uyku, güç'), ('Kanıt', 'Küçük ve kısa çalışmalar')],
    hikaye=('Adı “at kokusu”', 'Sanskritçe adı at kokusu anlamına gelir. Patlıcanın ve domatesin akrabasıdır; meyvesi ince bir kılıf içinde küçük bir kirazdır.'),
    gelenek=('Ayurveda’nın gençleştiricisi', 'Ayurveda’da güç ve dayanıklılık veren bir bitki sayılır; kök tozu sütle kaynatılıp içilir.'),
    bilim=('Uzun süreli güvenliği bilinmiyor', 'Birkaç küçük çalışmada stres ve kaygıda azalma bildirildi. Ama çalışmalar kısa; uzun süre kullanmanın güvenliği bilinmiyor.'),
    dikkat=['Hamileysen: kullanma', 'Tiroit hastalığın varsa', 'Karaciğer hastasıysan'], dikkat_not='Bazı Avrupa ülkeleri takviyelerini kısıtladı.',
    nasil=('Takviye almadan önce', 'Hekimine ya da eczacına danış. Karaciğer hasarı vakaları bildirildi.'),
    kaydet='Kaydet, almadan önce bak.', soru='Ashwagandha kullandın mı?'),

'melisa': dict(
    kapak='Arıları neden çeker?', emoji='🐝',
    kisaca=[('Nereden', 'Anadolu ve Akdeniz'), ('Ne için', 'Stres, uyku, sindirim'), ('Kanıt', 'Geleneksel; küçük çalışmalar olumlu')],
    hikaye=('Adı “bal arısı”', 'Melissa Yunanca bal arısı demek. Arıcılar kovanları oğul otuyla ovarak arı oğulunu çeker.'),
    gelenek=('Sinir yatıştıran çay', 'Anadolu’da oğul otu adıyla bilinir; çayı sinirleri yatıştırmak ve uyumak için içilir.'),
    bilim=('Hafif stres için kabul görüyor', 'Avrupa İlaç Ajansı melisayı hafif stres, uyku sorunu ve hazımsızlık için geleneksel kullanımda tanıyor. Küçük çalışmalar olumlu.'),
    dikkat=['Tiroit ilacı kullanıyorsan'], dikkat_not='Genelde güvenli.',
    nasil=('Limon kokulu çay', 'Bir avuç taze ya da bir tatlı kaşığı kuru yaprağı 10 dakika demle.'),
    kaydet='Kaydet, gergin bir günde iç.', soru='Oğul otu çayını hiç denedin mi?'),

'ceviz': dict(
    kapak='Ceviz ağacının altında neden domates yetişmez?', emoji='🌰',
    kisaca=[('Nereden', 'Anadolu, Kafkasya, İran'), ('Ne için', 'Kolesterol; yaprak cilt için'), ('Kanıt', 'Cevizde güçlü, yaprakta zayıf')],
    hikaye=('Komşusunu istemeyen ağaç', 'Ceviz kökünden ve yaprağından toprağa juglon geçer. Bu madde başka bitkilerin büyümesini engeller.'),
    gelenek=('Boya, reçel, çay', 'Yeşil kabuğu yüne ve halıya kahverengi verir. Yeşil cevizden reçel yapılır; yaprak çayı halk arasında şeker için içilir.'),
    bilim=('Kolesterolde kanıtlı', 'Düzenli ceviz yemenin LDL kolesterolü düşürdüğü pek çok kontrollü çalışmayla gösterildi. Yaprak için kanıt zayıf.'),
    dikkat=['Ceviz alerjin varsa', 'Yaprak çayını hamileyken içme'], dikkat_not='Yeşil kabuk elini kahverengiye boyar.',
    nasil=('Günde bir avuç', 'Çalışmalarda günde yaklaşık bir avuç (30 gram) ceviz kullanıldı.'),
    kaydet='Kaydet, kahvaltına ekle.', soru='Yeşil ceviz reçeli sever misin?'),

'rezene': dict(
    kapak='Bebek gazında güvenli mi?', emoji='🌾',
    kisaca=[('Nereden', 'Akdeniz ve Ege'), ('Ne için', 'Gaz, şişkinlik, adet sancısı'), ('Kanıt', 'Sindirimde kabul görüyor')],
    hikaye=('Maraton bir rezene tarlası', 'Maraton adı, Atina yakınlarındaki rezene dolu ovadan gelir. Yunanca marathon, rezene demektir.'),
    gelenek=('Annelerin çayı', 'Bebeklerde gaz sancısı ve emziren annelerde süt için içilir. Ege’de yumrusu ve sapı yemeklere girer.'),
    bilim=('Sindirimde kabul görüyor', 'Avrupa İlaç Ajansı rezene tohumunu hafif sindirim şikâyetleri, gaz ve adet sancısı için tanıyor.'),
    dikkat=['Küçük çocuklarda uzun süre kullanma', 'Hamileysen uzun süre kullanma', 'Kereviz ya da havuç alerjin varsa'], dikkat_not='İçindeki estragol nedeniyle kısa süreli kullanılır.',
    nasil=('Rezene çayı', 'Bir çay kaşığı tohumu hafifçe ez, bir bardak kaynar suda 10 dakika demle.'),
    kaydet='Kaydet, şiştiğinde lazım.', soru='Rezeneyi yemekte de kullanır mısın?'),

'karanfil': dict(
    kapak='Diş ağrısında neden karanfil?', emoji='🟤',
    kisaca=[('Nereden', 'Endonezya’nın Baharat Adaları'), ('Ne için', 'Diş ağrısı, ağız iltihabı'), ('Kanıt', 'Diş hekimliğinde kullanılıyor')],
    hikaye=('Çocukla birlikte dikilen ağaç', 'Maluku Adaları’nda çocuk doğunca bir karanfil ağacı dikilirdi; ağacın sağlığı çocuğunkine bağlanırdı.'),
    gelenek=('Dişin yanına bir tane', 'Anadolu’da ağrıyan dişin yanına bir tane karanfil konur. Kış çaylarına, komposto ve hoşaflara katılır.'),
    bilim=('Öjenolün işi', 'Karanfil yağındaki öjenol, diş hekimliğinde lokal ağrı kesici ve antiseptik olarak uzun süredir kullanılıyor.'),
    dikkat=['Saf yağı yutma, çocuklarda tehlikeli', 'Diş etine sık sürme', 'Kan sulandırıcı kullanıyorsan'], dikkat_not='Baharat olarak güvenli.',
    nasil=('Oda kokusu', 'Bir portakala karanfil tanelerini batır, odana as. Hem güzel kokar hem dayanır.'),
    kaydet='Kaydet, diş ağrısında hatırla.', soru='Karanfili en çok neye katarsın?'),

'aloe': dict(
    kapak='Jel ile özsu aynı şey değil', emoji='🪴',
    kisaca=[('Nereden', 'Arap Yarımadası ve Afrika'), ('Ne için', 'Yanık, güneş yanığı'), ('Kanıt', 'Jelde küçük çalışmalar olumlu')],
    hikaye=('“Sarısabır” nereden gelir?', 'Aloenin Arapça adı sabir. Osmanlı eczacılığındaki “sarısabır” adı buradan gelir.'),
    gelenek=('Saksıdaki ilk yardım', 'Akdeniz’deki evlerde saksıda yetiştirilir; yaprağın jeli yanık ve güneş yanığına sürülür.'),
    bilim=('Jel dışarıya, özsu değil', 'Jelin hafif yanıklarda iyileşmeyi hızlandırabileceğine dair küçük çalışmalar var. Yaprağın sarı özsuyu ise güçlü bir müshil ve içilmesi önerilmiyor.'),
    dikkat=['Yaprak özsuyunu içme', 'Hamileysen ağızdan kullanma'], dikkat_not='Jel cilde sürüldüğünde genelde güvenli.',
    nasil=('Jeli doğru almak', 'Yaprağı kes, sarı özsuyu akıp gitsin diye birkaç dakika dik beklet. Sonra içindeki şeffaf jeli kaşıkla al.'),
    kaydet='Kaydet, yaz için.', soru='Evinde aloe var mı?'),

'incir': dict(
    kapak='Buğdaydan önce incir mi vardı?', emoji='🍃',
    kisaca=[('Nereden', 'Ege, Akdeniz, Orta Doğu'), ('Ne için', 'Kabızlık; sütü siğil için'), ('Kanıt', 'Kabızlıkta küçük çalışmalar')],
    hikaye=('11.400 yıllık incirler', 'Ürdün Vadisi’nde bulunan 11.400 yıllık incirler, incirin buğdaydan yaklaşık bin yıl önce evcilleştirilmiş olabileceğini düşündürüyor.'),
    gelenek=('Aydın’ın ileklemesi', 'Aydın’da dişi ağaçlara erkek incir dalları asılır; küçük bir yaban arısı tozlaşmayı sağlar. Kur’an’ın Tîn suresi de incir ve zeytin üzerine yeminle başlar.'),
    bilim=('Lifi bol', 'Kuru incir lif bakımından zengin; kabızlıkta faydasını gösteren birkaç küçük çalışma var.'),
    dikkat=['Yaprak ve dal sütü cilde değdiyse güneşe çıkma', 'Kuru incirin şekeri yüksek'], dikkat_not='İncir yaprağıyla bronzlaşmaya çalışanlarda ağır yanıklar görüldü.',
    nasil=('Kabızlık için', 'Akşamdan 2–3 kuru inciri suda beklet, sabah suyuyla birlikte ye.'),
    kaydet='Kaydet, güneşte dikkat et.', soru='Ege inciri mi, Güneydoğu inciri mi?'),

'kusburnu': dict(
    kapak='C vitamini çayda kalıyor mu?', emoji='🔴',
    kisaca=[('Nereden', 'Bütün Anadolu; Gümüşhane, Bayburt'), ('Ne için', 'Soğuk algınlığı, eklem ağrısı'), ('Kanıt', 'Dizde birkaç küçük çalışma')],
    hikaye=('Savaşın vitamini', 'İkinci Dünya Savaşı’nda portakal gelmeyen İngiltere’de çocuklar C vitamini için kuşburnu toplamaya seferber edildi.'),
    gelenek=('Marmelat, pekmez, çay', 'Kışın soğuk algınlığına karşı içilir; Gümüşhane ve Bayburt’un yöresel ürünüdür.'),
    bilim=('Taze ile kuru farklı', 'Taze meyve C vitamini bakımından çok zengin, ama kurutma ve kaynatma bunu büyük ölçüde azaltır. Kuşburnu tozu dizde ağrıyı hafifletebilir.'),
    dikkat=['Çekirdek tüylerini süzmeden tüketme'], dikkat_not='Genelde güvenli.',
    nasil=('Daha çok C vitamini için', 'Çayı kaynatma: kaynamış suyu biraz soğut, kuşburnunu 10 dakika demle ve tülbentten süz.'),
    kaydet='Kaydet, kış çayın hazır.', soru='Kuşburnu marmelatı mı, çayı mı?'),

'feslegen': dict(
    kapak='Reyhan ile fesleğen aynı mı?', emoji='🌿',
    kisaca=[('Nereden', 'Hindistan’dan Anadolu’ya'), ('Ne için', 'Mutfak; halk arasında sindirim'), ('Kanıt', 'Geleneksel; insan çalışması az')],
    hikaye=('İki dilde iki ad', 'Batıdaki adı Yunanca “kraliyet otu” anlamındaki basilikon’dan gelir. Türkçedeki reyhan ise Arapçada “güzel kokulu bitki” demek.'),
    gelenek=('Türkülerin otu', 'Pencere önlerinde yetiştirilir, türkülerde sevgilinin simgesidir. Doğu Anadolu’da mor reyhandan şerbet yapılır.'),
    bilim=('Laboratuvarda umut verici', 'Antimikrobiyal ve iltihap giderici etkiler hayvan çalışmalarında görüldü; insan çalışması yok denecek kadar az.'),
    dikkat=['Uçucu yağı hamilelikte ve çocuklarda kullanma', 'Varfarin kullanıyorsan birden çok yeme'], dikkat_not='Yemekte ve çayda güvenli.',
    nasil=('Reyhan şerbeti', 'Mor reyhan yapraklarını sıcak suda demle, süz, soğut. Limon ve şekerle karıştır.'),
    kaydet='Kaydet, yaz şerbeti.', soru='Sen ona reyhan mı dersin, fesleğen mi?'),

'ginkgo': dict(
    kapak='Hafızayı gerçekten güçlendirir mi?', emoji='🍂',
    kisaca=[('Nereden', 'Çin’in tapınak bahçeleri'), ('Ne için', 'Hafıza, dolaşım iddiaları'), ('Kanıt', 'Demansı önlemiyor')],
    hikaye=('Yaşayan fosil', 'Ginkgo 200 milyon yıllık bir soyun yaşayan tek üyesi; dinozorlarla aynı dönemde yaşamış ağaçların son temsilcisi.'),
    gelenek=('Hiroşima’dan sağ kalan', 'Hiroşima’daki atom bombasından sağ kalan ginkgo ağaçları bugün barışın ve dayanıklılığın simgesi.'),
    bilim=('Büyük çalışma: önlemiyor', 'Avrupa’da standart ekstresi yaşa bağlı hafif unutkanlıkta kabul görüyor. Ama büyük bir ABD çalışması yaşlılarda demansı önlemediğini gösterdi.'),
    dikkat=['Kan sulandırıcı kullanıyorsan', 'Ameliyat olacaksan', 'Nöbet geçiriyorsan'], dikkat_not='Çiğ tohumları zehirli.',
    nasil=('Sokakta ginkgo', 'Yelpaze biçimli yaprağından tanırsın. Sonbaharda altın sarısına döner; Türkiye’de de park ağacıdır.'),
    kaydet='Kaydet, parkta bak.', soru='Sokağında ginkgo ağacı var mı?'),

'anason': dict(
    kapak='Rakı neden beyazlaşır?', emoji='🤍',
    kisaca=[('Nereden', 'Göller Bölgesi ve Ege'), ('Ne için', 'Gaz, hazımsızlık, öksürük'), ('Kanıt', 'Geleneksel olarak kabul görüyor')],
    hikaye=('Uzo etkisi', 'Anasondaki anetol alkolde çözünür ama suda çözünmez. Su eklenince küçük damlacıklar oluşur ve ışığı saçar: rakı beyazlaşır.'),
    gelenek=('Rakıdan çaya', 'Anason çayı gaz, hazımsızlık ve öksürük için içilir; emziren annelere süt için verilir.'),
    bilim=('Sindirimde kabul görüyor', 'Avrupa İlaç Ajansı anasonu hafif hazımsızlık, gaz ve öksürükte geleneksel kullanımda tanıyor.'),
    dikkat=['Kereviz ya da rezene alerjin varsa', 'Uçucu yağı hamilelikte ve çocuklarda kullanma', 'Bebeğe vermeden önce hekime sor'], dikkat_not='Çay olarak genelde güvenli.',
    nasil=('Anason çayı', 'Bir çay kaşığı tohumu hafifçe ez, bir bardak kaynar suda 10 dakika demle.'),
    kaydet='Kaydet, sofrada anlat.', soru='Bu “uzo etkisi”ni biliyor muydun?'),

'sarimsak': dict(
    kapak='İki kıtada nazar boncuğu', emoji='🧄',
    kisaca=[('Nereden', 'Anadolu’dan And Dağları’na'), ('Ne için', 'Tansiyon, kolesterol, soğuk algınlığı'), ('Kanıt', 'Tansiyonda küçük ama gerçek etki')],
    hikaye=('Aynı bitki, aynı görev', 'Sarımsak Anadolu’da kapıya, beşik başına nazara karşı asılır. Peru ve Bolivya’da da nazara karşı yanında taşınır.'),
    gelenek=('Çiğ yemenin sırrı', 'Soğuk algınlığı ve tansiyon için çiğ yenir. Ezilince ortaya çıkan allisin, kokusunun ve etkisinin kaynağı.'),
    bilim=('Küçük ama gerçek', 'Meta-analizler sarımsak preparatlarının tansiyonu ve kolesterolü hafifçe düşürdüğünü gösteriyor.'),
    dikkat=['Kan sulandırıcı kullanıyorsan', 'Ameliyat olacaksan'], dikkat_not='Yemekte güvenli.',
    nasil=('Ez ve beklet', 'Sarımsağı ezdikten sonra 10 dakika beklet, sonra pişir. Allisin bu sürede oluşur.'),
    kaydet='Kaydet, mutfakta dene.', soru='Senin evinde de nazara karşı sarımsak asılır mıydı?'),

'keten': dict(
    kapak='Keten tohumu: lif mi, kumaş mı?', emoji='🌾',
    kisaca=[('Nereden', 'Anadolu’dan And’lara'), ('Ne için', 'Kabızlık, kolesterol'), ('Kanıt', 'Kabızlıkta güçlü')],
    hikaye=('En eski kumaşlardan', 'Keten insanlığın en eski dokuma liflerinden. Anadolu’da Neolitik çağdan keten kumaş parçaları bulundu.'),
    gelenek=('Peru’nun sabah içeceği', 'Anadolu’da tohum suda bekletilip kabızlık için içilir. Peru’da linaza sokaklarda sabah içeceği olarak satılır.'),
    bilim=('Kabızlıkta kabul görüyor', 'Avrupa İlaç Ajansı keten tohumunu kabızlık için iyi yerleşmiş kullanımda tanıyor. Kolesterolde hafif düşüş görülen çalışmalar da var.'),
    dikkat=['Bol suyla al: az suyla bağırsak tıkayabilir', 'Çiğ tohumu ölçülü tüket'], dikkat_not='',
    nasil=('Öğütüp kullan', 'Bütün tohum çoğu zaman sindirilmeden geçer. Öğüt, yoğurda ya da salataya ekle, yanında bol su iç.'),
    kaydet='Kaydet, kahvaltıda kullan.', soru='Keten tohumunu nasıl tüketiyorsun?'),

'turunc': dict(
    kapak='Zayıflama hapındaki portakal', emoji='🍊',
    kisaca=[('Nereden', 'Antalya’dan Hatay’a; Sevilla'), ('Ne için', 'Reçel, sos; zayıflama takviyeleri'), ('Kanıt', 'Kilo kaybında belirsiz')],
    hikaye=('Avrupa’nın ilk portakalı', 'Avrupa’ya ilk ulaşan turunçgil tatlı portakal değil, Araplarla Endülüs’e gelen acı portakaldı. Sevilla’nın sokakları hâlâ turunç dolu.'),
    gelenek=('Limon yerine turunç', 'Kabuğundan reçel yapılır, ekşi suyu salataya limon yerine sıkılır. Çiçeğinden portakal çiçeği suyu damıtılır.'),
    bilim=('“Yağ yakıcı” iddiası zayıf', 'Zayıflama takviyelerindeki sinefrinin kilo kaybına etkisi küçük ve belirsiz. Kafeinle birlikte kullanılan ürünlerde çarpıntı ve inme vakaları bildirildi.'),
    dikkat=['Kalp hastasıysan: takviye kullanma', 'Yüksek tansiyonun varsa', 'Düzenli ilaç kullanıyorsan (greyfurt gibi etkileşir)'], dikkat_not='Meyve ve reçel olarak güvenli.',
    nasil=('Turunç reçeli', 'Kabukları ince şeritler hâlinde kes, acılığı gitsin diye birkaç kez haşlayıp suyunu dök, sonra şekerle pişir.'),
    kaydet='Kaydet, kışın reçel yap.', soru='Turunç reçelini sever misin?'),

'meyan': dict(
    kapak='Şekerden 50 kat tatlı kök', emoji='🍂',
    kisaca=[('Nereden', 'Güneydoğu Anadolu, Asya'), ('Ne için', 'Öksürük, mide yanması'), ('Kanıt', 'Geleneksel olarak kabul görüyor')],
    hikaye=('Sigaranın gizli tadı', 'Meyan kökünün dünyadaki en büyük alıcılarından biri tütün sanayisi; sigaraya tat vermek için kullanılıyor.'),
    gelenek=('Ramazan şerbeti', 'Güneydoğu’da Ramazan’da meyan şerbeti içilir. Çin tıbbında diğer otları “uyumlu hâle getirdiği” için reçetelere eklenir.'),
    bilim=('Glisirizinin iki yüzü', 'Avrupa İlaç Ajansı meyanı öksürük ve hafif mide şikâyetleri için tanıyor. Ama tatlılığını veren glisirizin, fazlası tansiyonu yükseltir.'),
    dikkat=['Tansiyonun yüksekse', 'Kalp ya da böbrek hastasıysan', 'Hamileysen'], dikkat_not='Her gün ve çok miktarda içme.',
    nasil=('Meyan şerbeti', 'Ezilmiş kökü bir gece soğuk suda beklet, süz. Bol suyla ve ölçülü iç.'),
    kaydet='Kaydet, Ramazan’da hatırla.', soru='Meyan şerbetini hiç içtin mi?'),

'defne': dict(
    kapak='Hatay’ın meşhur sabunu', emoji='🌿',
    kisaca=[('Nereden', 'Akdeniz; Hatay’ın defne koruları'), ('Ne için', 'Mutfak, sabun, romatizma ağrısı'), ('Kanıt', 'İnsan çalışması çok az')],
    hikaye=('Antakya’nın eski adı', 'Antakya’nın Harbiye semtinin antik adı Daphne; Apollon tapınağı ve defne korularıyla ünlüydü.'),
    gelenek=('Galiplerin tacı', 'Antik Yunan’da galiplere defne tacı verilirdi. Hatay’da meyvesinin yağı zeytinyağıyla karışıp defne sabunu olur.'),
    bilim=('Laboratuvarda antimikrobiyal', 'Yaprak yağındaki sineol laboratuvarda antimikrobiyal etki gösteriyor; insan çalışması çok az.'),
    dikkat=['Kuru yaprağı bütün hâlde yutma', 'Hassas cildin varsa yağı önce az yerde dene'], dikkat_not='Mutfakta güvenli.',
    nasil=('Dolap kokusu', 'Birkaç kuru defne yaprağını dolaplarına ve un kavanozlarına koy. Halk arasında güveyi uzak tuttuğuna inanılır.'),
    kaydet='Kaydet, dolabına koy.', soru='Defne sabunu kullanıyor musun?'),

'kakule': dict(
    kapak='Dünyanın en pahalı baharatlarından', emoji='💚',
    kisaca=[('Nereden', 'Güney Hindistan; bugün en çok Guatemala'), ('Ne için', 'Sindirim, ağız kokusu, tat'), ('Kanıt', 'Küçük çalışmalarda hafif etki')],
    hikaye=('Tek tek, elle', 'Kakule kapsülleri olgunlaşmadan, tek tek elle toplanır. Bu yüzden safran ve vanilyayla birlikte en pahalı baharatlardandır.'),
    gelenek=('Kahvenin yoldaşı', 'Arap kahvesi kakuleyle demlenir; Güneydoğu’da ve Hatay’da da kahveye kakule katılır. Hindistan’da masala çayının parçası.'),
    bilim=('Hafif ama tutarsız', 'Küçük çalışmalarda tansiyonu ve bazı iltihap göstergelerini biraz düşürdü; kolesterol ve şekerde sonuçlar tutarsız.'),
    dikkat=['Yüksek doz takviyeleri hamilelikte kullanma'], dikkat_not='Baharat olarak güvenli.',
    nasil=('Kakuleli kahve', 'Bir iki kakule tanesini hafifçe ez, kahveyle birlikte pişir.'),
    kaydet='Kaydet, kahvene dene.', soru='Kahvene kakule koyar mısın?'),

'enginar': dict(
    kapak='Yediğimiz kısım aslında bir çiçek', emoji='💜',
    kisaca=[('Nereden', 'Ege ve İstanbul mutfağı'), ('Ne için', 'Hazımsızlık, şişkinlik'), ('Kanıt', 'Geleneksel; küçük çalışmalar olumlu')],
    hikaye=('Açarsa mor bir çiçek', 'Enginarın yediğimiz kısmı açmamış bir çiçek başı. Toplanmazsa mor, devedikenine benzeyen bir çiçeğe dönüşür.'),
    gelenek=('Baharın müjdecisi', 'Zeytinyağlı enginar Ege ve İstanbul mutfağında baharı müjdeler. Haşlama suyu ve yaprak çayı karaciğer ve safra için içilir.'),
    bilim=('Hazımsızlıkta kabul görüyor', 'Avrupa İlaç Ajansı enginar yaprağını hafif hazımsızlık ve şişkinlikte geleneksel kullanımda tanıyor.'),
    dikkat=['Safra taşın ya da safra yolu tıkanıklığın varsa', 'Papatyagillere alerjin varsa'], dikkat_not='Yemek olarak güvenli.',
    nasil=('Kararmasın', 'Temizlediğin enginarı hemen limonlu suya at; havayla temas edince kararır.'),
    kaydet='Kaydet, baharda lazım.', soru='Zeytinyağlı enginar sever misin?'),
}
