# Kaynaklı halk hekimliği kayıtları. İki yerde kullanılır:
#  1) bitki ve yore varsa: bitki sayfasının "Geleneksel kullanım" bölümüne (yöre, metin) eklenir, kaynak sayfanın kaynak listesine girer.
#  2) post: Threads'te 21:30 slotunda "Halk hekimliğinden" postu olarak çıkar (eski "…sever misiniz?" sorularının yerine).
# Metin yalnızca kaynağın söylediğini aktarır; kayıt, öneri değildir. Post metni 400 karakteri geçmesin (kaynak ve bağlantı eklenecek).

DOGAN = ('Oğuz Doğan, “Diyadin ve Doğubayazıt Yöresi Halk Hekimliğinde Kullanılan Yabani Bitkiler”, Lokman Hekim Dergisi 13(1), 2023',
         'https://dergipark.org.tr/tr/pub/mutftd/article/1173028')
OZCIFTCI = ('Seçil Özçiftçi, Çağatay Üstün, Nermin Ersoy, “Manisa/Akçapınar’da Uygulanagelen Bir Halk Hekimliği Örneği: Otu Kesme Ocağı”, Lokman Hekim Dergisi 13(3), 2023',
            'https://dergipark.org.tr/tr/pub/mutftd/article/1319022')
ASIL = ('Eriş Asil, Mekin Tanker, Sevgi Şar, “İç Anadolu Bölgesi’nde Baş Ağrılarına Karşı Kullanılan Halk İlaçları”, Ankara Ü. Eczacılık Fak. Dergisi 14(1), 1984',
        'https://dergipark.org.tr/tr/pub/jfpanu/article/394823')
GURSOY = ('Ülkü Gürsoy, “Türk Kültüründe Ağaç Kültü ve Dut Ağacı”, Türk Kültürü ve Hacı Bektaş Veli Araştırma Dergisi 61, 2013',
          'https://dergipark.org.tr/tr/pub/tkhcbva/article/1157366')
AG = 'Ağrı (Diyadin, Doğubayazıt)'
_L = 'https://dergipark.org.tr/tr/pub/mutftd/article/'
KIRICI = ('Saliha Kırıcı, Sevgi Demirci Kayıran, Gülşen Tokuzi, “Doğu Akdeniz Bölgesinde Üzerlik (Peganum harmala L.) Bitkisinin Tütsü Olarak Kullanımı”, Lokman Hekim Dergisi 8(1), 2018', _L + '523820')
KARDAS = ('Celal Kardaş, “Muş’ta Yabani Bitkilerin Halk Hekimliğinde Kullanılması”, Lokman Hekim Dergisi 9(1), 2019', _L + '468848')
SEN = ('Esra Şen, Hatice Dinç Kaya, “Doğumda Geleneksel Uygulamalar: Fatma Ana Eli Bitkisi (Anastatica hierochuntica L.)”, Lokman Hekim Dergisi 11(2), 2021', _L + '871831')
HITIT = ('Sinem Yeğenoğlu, Burcu Sözen Şahne, Ezgi Ulutaş, “Hitit Uygarlığında Bitkilerin Yeri”, Lokman Hekim Dergisi 6(3), 2016', _L + '523739')
MITOS = ('Nazlıcan Tarhan, Mustafa Arslan, Sevgi Şar, “Bazı Tıbbi Bitkiler ve Onlara Ait Mitoslar”, Lokman Hekim Dergisi 6(1), 2016', _L + '523708')
KOKBOYA = ('Fatma Birgili, Mehmet Özcan, “Kök Boya Ustasından Bitki Kökleri ile Yanık Uygulaması”, Lokman Hekim Dergisi 2(3), 2012', _L + '523500')
TAFLAN = ('Mehmet Karasu, Aytaç Yaşar, “Taflan (Laurocerasus officinalis Roemer) Bitkisinin Ordu-Giresun Yöresinde Hayvanlarda Folklorik Kullanımı”, Lokman Hekim Dergisi 13(2), 2023', _L + '1245849')
LADEN = ('Nazım Şekeroğlu, Sevgi Gezici, “Türkiye’nin Virüs Savar Bitkisi Laden (Cistus spp.) Türleri”, Lokman Hekim Dergisi 11(2), 2021', _L + '895397')
OCAK = ('Hakan Volkan Acar, “Türk Halk Hekimliğindeki Ocak Çeşitleri”, Lokman Hekim Dergisi 7(2), 2017', _L + '523762')
NAZAR = ('Deniz Güçlü, “Anadolu’da Nazar İnancı: Halk Hekimliğinde Tanı ve Korunma Pratikleri”, Lokman Hekim Dergisi 16(2), 2026', _L + '1808091')
MEVLANA = ('Sinem Yeğenoğlu, Burcu Sözen Şahne, “Maddeden Manaya: Bitkiler ve Mevlana”, Lokman Hekim Dergisi 6(1), 2016', _L + '523714')
GUL = ('A. E. Güler, S. Karataş, “Tarihin Önemli Sırrı: Gül, Gül Yağı ve Gülsuyu”, Lokman Hekim Dergisi, XI. Türk Eczacılık Tarihi Toplantısı bildirileri, 2014', _L + '590199')
SAFRAN = ('Lale Paşayeva, Halil Tekiner, “Türk-İslam Tıbbında Safranın Yeri”, Lokman Hekim Dergisi 4(3), 2014', _L + '523667')
SAC = ('Günseli Serarslan, Ayhan Altıntaş, “Şifalı Yağlardan Modern Bilime: XIV. ve XV. Yüzyıl Tıp Metinlerinde Saç Tedavileri”, Lokman Hekim Dergisi 16(3), 2026', _L + '1938020')
MERYEM = ('H. B. Ereni, Sevgi Şar, “Meryemana Dikeni Bitkisi: Farmakolojik ve Folklorik Bir Değerlendirme”, Lokman Hekim Dergisi 10(1), 2020', _L + '631944')
TERE = ('İ. Başağaoğlu, G. Kavalalı, “Halk Hekimliğinde Tere Bitkisinin (Lepidium sativum L.) Kullanılması”, Lokman Hekim Dergisi 9(3), 2019', _L + '592053')
LH = 'Lokman Hekim Dergisi'

EGE = ('Bintuğ Öztürk ve ark., “Türkiye’nin Etnobotanik Veritabanı”, Ege Üniversitesi BAP sonuç raporu, 2020',
       'https://acikerisim.ege.edu.tr/server/api/core/bitstreams/c2e0e3a1-ac5b-4664-bc34-33187274efea/content')

HALK = [
 dict(kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023', link='toplama-takvimi/',
  post='Ağrı’nın Diyadin ve Doğubayazıt yörelerinde şifalı otlar nisan ve mayısta, filizlenince toplanmaya başlanıyor. Bilgi verenlere göre otların çoğu ağustosta tohuma geçince gücünü yitiriyor; bu yüzden toplama temmuz sonunda bitiyor. Yağmurlu, çok güneşli ve rüzgârlı günlerde ot toplanmıyor.'),
 dict(kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023', link='toplama-takvimi/',
  post='Doğubayazıt ve Diyadin’de otları toplayıp hastalara verenler çoğunlukla kadınlar; yaylada yaşayan kadınlar ve çobanlar da bu bilgiyi taşıyor. Görüşülen bir çoban, hangi otun hangi derde iyi geldiğini ve ne zaman toplanacağını büyükleriyle defalarca dağa çıkarak öğrendiğini anlatıyor. Bilgi kitapla değil, birlikte yürüyerek aktarılıyor.'),
 dict(bitki='civanpercemi', yore=AG, kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023',
  metin='Kurutulup un gibi öğütülür ve açık yaraya serpilir; mide, karın ve adet sancısı için sıcak suda demlenip içilir.',
  post='Ağrı’nın Diyadin ve Doğubayazıt yörelerinde civanperçemi kurutulup un gibi öğütülüyor ve açık yaraya serpiliyor. Adı Akhilleus’tan gelen bu bitkinin yarada kullanımı, Anadolu’dan Kuzey Amerika’ya pek çok halkta karşımıza çıkıyor.'),
 dict(bitki='hatmi', yore=AG, kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023',
  metin='Kurutulmuş ot demlenip bel ağrısında ağrıyan yere masajla sürülür; bu uygulama hacamatla birlikte yapılır. Kuru öksürükte de kullanılır.',
  post='Diyadin ve Doğubayazıt’ta hatmi yalnızca öksürükte içilmiyor: kurutulmuş ot demlenip bel ağrısında ağrıyan yere masajla sürülüyor, bunu da çoğu zaman hacamatla birlikte yapıyorlar. Bitkiyi, kupayı ve eli bir arada kullanan bir halk tedavisi.'),
 dict(bitki='isirgan', yore=AG, kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023',
  metin='Kaynatılıp suyu içilir; saç dökülmesine karşı kaynatma suyu düzenli olarak saça sürülür.',
  post='Ağrı yöresinde ısırganın kaynatma suyu yalnızca içilmiyor, saç dökülmesine karşı düzenli olarak saça da sürülüyor. Isırgan saç bakımında Avrupa halk geleneğinde de sık geçen bir bitki.'),
 dict(bitki='papatya', yore=AG, kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023',
  metin='Yörede papatya denen Anthemis armeniaca’nın yalnızca çiçek başı kullanılır: kurutulup kaynatılır ve buharı sinüzit için solunur.',
  post='Her “papatya” aynı bitki değil. Doğubayazıt yöresinde papatya denen bitki Anthemis armeniaca; yalnızca çiçek başları kurutulup kaynatılıyor ve buharı sinüzit için soluluyor. Bildiğimiz çay papatyası ise Matricaria chamomilla. Yerel adlar, bitkiyi tanımadan kullanmanın neden riskli olduğunu gösteriyor.'),
 dict(bitki='ebegumeci', yore=AG, kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023',
  metin='Çocuk isteyen kadınlar suyunu düzenli olarak içer; mide iltihabında da kullanılır.',
  post='Diyadin ve Doğubayazıt’ta ebegümecinin suyunu çocuk isteyen kadınlar düzenli olarak içiyor. Ebegümeci Anadolu’da çoğunlukla yemeği ve öksürükteki kullanımıyla bilinir; bu kayıt, aynı bitkinin yöreden yöreye bambaşka anlamlar kazandığını gösteriyor.'),
 dict(bitki='uzerlik', yore=AG, kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023',
  metin='Tohumu kullanılır: hemoroit için tohum ağza alınıp üzerine bir bardak su içilir ve bu on beş gün sürdürülür. (Üzerlik tohumu zehirlenmeye yol açabilir; bu bir kayıttır, öneri değildir.)',
  post='Üzerlik Anadolu’da çoğunlukla nazarlıkla anılır; kapıya asılır, tohumu tütsülenir. Ağrı yöresinde ise tohumu ağızdan da kullanılıyor. Dikkat: üzerlik tohumu zehirlenmelere yol açabilen güçlü alkaloitler içerir; bu bir kültürel kayıttır, öneri değildir.'),
 dict(kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023', link='toplama-takvimi/',
  post='Diyadin ve Doğubayazıt’ta “dağ sakızı” (Scorzonera latifolia) böyle yapılıyor: kök kesiliyor, akan süt gibi özsu bir kavanozda toplanıyor, karıştırılarak kaynatılıyor ve sertleşmeye bırakılıyor. Ortaya çıkan sakız mide ağrısı için çiğneniyor. Bir bitkiden “ilaç” değil, bir zanaat ürünü çıkarılıyor.'),
 dict(kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023', link='toplama-takvimi/',
  post='Ağrı yöresinde sığırdili (Anchusa azurea) yaylaya gidip dönünce boş kalmış evlerde yakılıyor; dumanı böcekleri öldürmek için. Aynı kayıt, bitkinin çok kullanılırsa zehirleyebileceği uyarısını da içeriyor. Bitki dumanıyla ev arındırmanın gündelik, pratik bir hâli.'),
 dict(kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023', link='toplama-takvimi/',
  post='Ağrı yöresinde dadırak (Salvia verticillata) mide ağrısında kullanılıyor, zayıf kuzulara da yediriliyor; kuzuların kilo aldığı söyleniyor. Yörede bir uyarı da dilden dile geçiyor: “Çok fazla tüketilirse ölüme sebep olur.” Halk bilgisi, dozun önemini de kendi diliyle taşıyor.'),
 dict(kaynak=DOGAN, kisa='Doğan, Lokman Hekim Dergisi, 2023', link='toplama-takvimi/',
  post='Doğubayazıt yöresinde ağrıyan, iltihaplı bir diş için sinir otu (Plantago major) ezilip dişin üzerine konuyor ve sabaha kadar bırakılıyor; iltihaplı yaralara da yaprağı yapıştırılıyor. Sinir otunun yaprağı yara üzerinde Avrupa’dan Amerika’ya pek çok halkta karşımıza çıkar.'),
 dict(kaynak=OZCIFTCI, kisa='Özçiftçi, Üstün, Ersoy, Lokman Hekim Dergisi, 2023', link='yazilar/samanizm-ve-kam-gelenegi/',
  post='Manisa Turgutlu’nun Akçapınar köyünde “Otu Kesme Ocağı” bugün de çalışıyor. Araştırmacılar 2020’de ocağı gözlemleyip ocaklı ve hastalarla görüştü: ocağa çoğunlukla cilt hastalıkları için gidiliyor, hastalar çevre köy ve ilçelerden geliyor. Ocaklıya göre iyileşmenin şartı, verilen yönteme uymak.'),
 dict(kaynak=OZCIFTCI, kisa='Özçiftçi, Üstün, Ersoy, Lokman Hekim Dergisi, 2023', link='yazilar/samanizm-ve-kam-gelenegi/',
  post='Anadolu’da “ocak”, şifa gücünün bir ailede kuşaktan kuşağa geçtiğine inanılan bir gelenek. Akçapınar’daki Otu Kesme Ocağı’nı inceleyen tıp tarihçileri, kullanılan toprak, bitkiler ve hastalıklar için ilgili alanların uzman hekimlerine de danıştı. Halk tıbbını ciddiye almak, onu hem kayda geçirmek hem de sorgulamak demek.'),
 dict(kaynak=ASIL, kisa='Asil, Tanker, Şar, Ankara Ü. Eczacılık Fak. Dergisi, 1984', link='rehber/',
  post='1984’te eczacılık tarihçileri İç Anadolu’da baş ağrısına karşı kullanılan halk ilaçlarını sözlü anlatılardan derledi: 28 maddeden 24’ü bitkisel, 3’ü hayvansal, 1’i mineral. Bu 28 maddeden yalnızca 4’ü modern tıpta hâlâ kullanılıyor; 5’inden etken madde elde edilmiş.'),
 dict(kaynak=GURSOY, kisa='Gürsoy, Türk Kültürü ve Hacı Bektaş Veli Araştırma Dergisi, 2013', link='yazilar/samanizm-ve-kam-gelenegi/',
  post='Dilek dileyip dut ağacının dallarına bez bağlamak, Ülkü Gürsoy’a göre eski Türk ağaç kültüne dayanan bir gelenek. Alevi-Bektaşi geleneğinde dut ağacı kutsallığını korumuş, “evin ruhu” sayılmış. Bugün “âdet” dediğimiz pek çok şeyin kökü bozkıra uzanıyor.'),

 # ---- 2011–2026 arşiv taraması (Ekim 2026) ----
 dict(bitki='uzerlik', yore='Mersin (Mut), Adana (Karaisalı), Sivas, Gaziantep (Nizip)', kaynak=KIRICI, kisa=f'Kırıcı ve ark., {LH}, 2018',
  metin='Tohumu tuzla birlikte közde yakılır, dumanı nazara karşı evin bütün odalarında dolaştırılır; tohumlar dizilip nazarlık olarak duvara asılır. Karaisalı’da kuru dal soğan ve sarımsak kabuğuyla yakılır, dumanın üzerinden atlanır, kül evden uzağa gömülür. Sivas’ta demetler kapı üstüne asılır. Yörede adı yüzerlik ve yüzellik olarak da geçer.',
  post='Mersin Mut’ta üzerlik tohumu tuzla közde yakılıyor ve dumanı nazara karşı evin her odasında dolaştırılıyor. Yöredeki söz: “Yılan bir gecede yüz eve gelir, yüzerlikli eve gelmez.” Karaisalı’da dumanın üzerinden atlanıyor, kül evden uzağa gömülüyor. Not: üzerlik tohumu zehirlidir; hamileler için özellikle tehlikelidir.'),
 dict(kaynak=NAZAR, kisa=f'Güçlü, {LH}, 2026', link='uzerlik/',
  post='Anadolu’da üzerlik yalnızca nazardan korumak için değil, nazarı “ölçmek” için de kullanılıyor: ocaklarda tohumlar kızgın sacın üzerine atılıyor ve ne kadar çok çatlarsa nazarın o kadar güçlü olduğuna inanılıyor. Kayseri’de tohumlar dört yol ağzından toplanan çalılarla, Van’da ölçülmüş iplikler ve nazar ettiğinden şüphelenilen kişinin adıyla birlikte yakılıyor.'),
 dict(kaynak=NAZAR, kisa=f'Güçlü, {LH}, 2026', link='corekotu/',
  post='Çocukların boynuna asılan nazarlık keselerine üzerlik tohumunun yanında karabiber, sarımsak kabuğu ve çörek otu da konuyor. Bunun sebebi, keskin kokuların nazarı “bozduğuna” inanılması. Alanya’da çaltı dikeninin tohumlarından tespih ve kolye yapılıyor, dalları kapılara, arabalara ve düğün atlarına asılıyor.'),
 dict(bitki='isgin', yore='Muş (Kurtik Dağı)', kaynak=KARDAS, kisa=f'Kardaş, {LH}, 2019',
  metin='Bir efsaneye göre ani bir rüzgârla uçan bir kadının süsü bu bitkiye takılmış; kadın bitkiye süsün adını vermiş ve o günden beri yenir. Baş ağrısı, mide ağrısı ve şeker hastalığı için kullanılır.',
  post='Muş’ta anlatılan bir efsane: bir lokman hekim çarşıda her yerde gulik (çiriş otu) satıldığını görünce “Bu halk sık hastalanacak” diye düşünüp şehri terk etmiş. Yörede söz hâlâ yaşıyor: “Muş halkı gulikten hastalanır, ışkından iyileşir.” Işkın, ilkbaharda dağlardan toplanan ışgın (Rheum ribes).'),
 dict(kaynak=KARDAS, kisa=f'Kardaş, {LH}, 2019', link='toplama-takvimi/',
  post='Muş’ta yılanyastığı (Arum elongatum, yörede karî-kardî) eskiden gelinlerin çeyizine konur, gelin ziyaretlerinde de götürülürmüş; varlığı çocuğa hazırlığın işaretiymiş. Elmani aşiretinden kimilerine göre ise onu toplayan kişi ailesinden birine ağır hastalık getirir. Not: yılanyastığı zehirli bir bitkidir.'),
 dict(kaynak=KARDAS, kisa=f'Kardaş, {LH}, 2019', link='toplama-takvimi/',
  post='Muş’un Varto ilçesinde çakşır (Ferula rigidula, yörede cağ) için bir ad daha var: “ikiziksiri”. Yöre halkı Kaynarca köyünde yüz kadar ikizin doğduğunu bu bitkiye bağlıyor; söylenene göre çakşır hem ikiz doğurtur hem de çocuğu olmayana çocuk verir.'),
 dict(bitki='hatmi', yore='Muş', kaynak=KARDAS, kisa=f'Kardaş, {LH}, 2019',
  metin='Yörede hîro denen hatmi çiçeğinin (Alcea) sapı, çiçeği ve yaprağı dövülüp ayranla karıştırılır ve yılan sokmasına yedi gün sürülür. Köpürdüğü için yoksulluk zamanlarında sabun yerine ölü yıkamada kullanılmıştır.',
  post='Muş’ta hatmi çiçeği (Alcea, yörede hîro) köpürdüğü için yoksulluk yıllarında sabun yerine ölü yıkamada kullanılmış. Yılan sokmasında ise sapı, çiçeği ve yaprağı dövülüp ayranla karıştırılarak yedi gün sürülüyor. Hatmi köklerindeki kaygan müsilaj, köpürmesinin de kaynağı.'),
 dict(bitki='ebegumeci', yore='Muş', kaynak=KARDAS, kisa=f'Kardaş, {LH}, 2019',
  metin='Yörede tolik denen ebegümeci (Malva neglecta) kısırlığa karşı pişirilip beze sarılır ve en az üç gece sıcak sıcak kadının karnına konur; şişkin bebeklerin karnına da unla karıştırılarak sarılır.'),
 dict(bitki='isirgan', yore='Muş', kaynak=KARDAS, kisa=f'Kardaş, {LH}, 2019',
  metin='Yörede gezgezk denen ısırganın taze suyu saç dökülmesine karşı saç diplerine sürülür; çorbası kan hastalıklarına önerilir.'),
 dict(kaynak=SEN, kisa=f'Şen ve Dinç Kaya, {LH}, 2021', link='rehber/',
  post='Anadolu’da doğum odasında bir kâse su ve içinde kuru bir bitki: Fatma Ana Eli (Anastatica hierochuntica). Bitki suda açıldıkça doğumun da su gibi kolay olacağına inanılıyor. Bazı yörelerde ebe, kadının sırtını ovarken “Bu el benim elim değil, Fatma Anamızın eli” diyor. Not: gebelikte bu bitkinin suyunu içmenin güvenliği kanıtlanmamıştır.'),
 dict(kaynak=SEN, kisa=f'Şen ve Dinç Kaya, {LH}, 2021', link='rehber/',
  post='Aynı bitki, farklı adlar: Anastatica hierochuntica Ankara, Sivas ve Tokat’ta Fadime Ana, Meryem Ana ya da Havva Ana diye anılıyor. Suda açıldıkça “hacet kapılarının” da açıldığına inanılıyor. Karaman’da yapılan bir araştırmada kadınların yüzde 77,9’u doğumu kolaylaştırmak için bu bitkiyi kullandığını söylemiş.'),
 dict(bitki='ardic', yore='Hititler', kaynak=HITIT, kisa=f'Yeğenoğlu ve ark., {LH}, 2016',
  metin='Hititler ardıcı dinî törenlerde tüketmiş, mezar yapımında ve ilaç hazırlamada kullanmıştır.',
  post='Hititler ardıcı dinî törenlerde kullanmış, mezar yapımında da ardıca yer vermiş. İştahsızlıkta hastaya yedi gün şeytan teresi (Ferula communis) verilir, iyileşmezse sarımsak gibi başka bitkilere geçilirmiş. Hangi bitkinin ilaca gireceğine de bazen fal ile karar verilirmiş.'),
 dict(bitki='gucigdemi', yore='Hititler', kaynak=HITIT, kisa=f'Yeğenoğlu ve ark., {LH}, 2016',
  metin='Hititlerin bitki hayatının yenilenmesini kutladığı ANTAHŞUM bayramı adını bu bitkiden alır.',
  post='Hititlerin yaklaşık 18 bayramından biri olan ANTAHŞUM, adını bir çiğdemden alıyordu ve bitki hayatının yenilenmesini kutluyordu. Bir bitki adının bir bayrama ad olması, bitkinin o toplum için ne kadar önemli olduğunu gösteriyor. Not: güz çiğdemi çok zehirli bir bitkidir.'),
 dict(bitki='adamotu', yore='Antik dönem', kaynak=MITOS, kisa=f'Tarhan ve ark., {LH}, 2016',
  metin='Söylenceye göre kökü topraktan sökülürken çığlık atar ve bu sesi duyan sağır olur ya da ölür; bu yüzden kök bir köpeğe bağlatılır, ses de davullarla bastırılırmış. Bu sahne bir Dioskorides elyazmasında resmedilmiştir. Tevrat’ta (Yaratılış 30) adamotu bir bereket armağanıdır.',
  post='Adamotu söylencesi: kökü topraktan sökülürken çığlık atar, bu sesi duyan sağır olur ya da ölürmüş. Bu yüzden kök bir köpeğe bağlatılır, ses de davullarla bastırılırmış; sahne bir Dioskorides elyazmasında resmedilmiş. Tevrat’ta ise Rahel ile Lea adamotu takas eder ve Lea çocuk sahibi olur. Not: adamotu çok zehirlidir.'),
 dict(bitki='nane', yore='Antik Yunan', kaynak=MITOS, kisa=f'Tarhan ve ark., {LH}, 2016',
  metin='Yunan söylencesinde Hades’in sevgilisi su perisi Menthe, nane bitkisine dönüştürülür; bitkinin adı da buradan gelir.',
  post='Naneye adını veren bir peri var: Yunan söylencesinde yeraltı tanrısı Hades’in sevgilisi su perisi Menthe nane bitkisine dönüştürülüyor. Şakayığın (Paeonia) adı da bitkiye dönüştürülen hekim Paeon’dan geliyor. Mısır’da şakayık kökü sara nöbeti geçirenlerin üzerinde haç biçiminde dolaştırılır, ona “haçotu” denirmiş.'),
 dict(bitki='ginseng', yore='Kore', kaynak=MITOS, kisa=f'Tarhan ve ark., {LH}, 2016',
  metin='Bir Kore söylencesinde dağ ruhu yoksul bir çocuğa ginsengin yerini gösterir; kökünden yapılan içecek çocuğun babasını iyileştirir.'),
 dict(bitki='hayit', yore='Muğla (Ula)', kaynak=KOKBOYA, kisa=f'Birgili ve Özcan, {LH}, 2012',
  metin='Ula’da bir kök boya ustasının ailesinde dört kuşaktır sürdürülen yanık karışımında hayıt ağacının dış kabuğu kaynatılarak kullanılır.',
  post='Muğla Ula’da kök boyacı Recep Tütüncü (1865–1950), boya kazanlarında sık yanık olunca kendi karışımını hazırladı: kiriş otu kökü, palamut meşesinin ince kökleri, hayıt kabuğu ve sakız ağacının reçinesi, bitkisel yağlarla. Bilgi oğluna, sonra torunlarına geçti. Vücudun büyük kısmı yanmışsa hastayı hastaneye gönderiyorlar.'),
 dict(bitki='sakiz', yore='Muğla (Ula)', kaynak=KOKBOYA, kisa=f'Birgili ve Özcan, {LH}, 2012',
  metin='Ula’da bir kök boya ustasının ailesinde dört kuşaktır sürdürülen yanık karışımına sakız ağacı kaynatılarak elde edilen sıvı katılır.'),
 dict(bitki='kina', yore='Kastamonu, Yozgat (mantar ocağı)', kaynak=OCAK, kisa=f'Acar, {LH}, 2017',
  metin='Mantar ocaklarında dua okunup yara yeri sirkeli sıcak suyla yıkandıktan sonra üzerine sirke, su ve kına karışımı sürülür.'),
 dict(kaynak=OCAK, kisa=f'Acar, {LH}, 2017', link='yazilar/samanizm-ve-kam-gelenegi/',
  post='Türk halk hekimliğinde yaklaşık 150 ocak çeşidi kaydedilmiş. Balıkesir’deki fıtık ocağında bir gül dalı koparılmadan boyuna yarılıyor, hasta dua okunurken bu aralıktan geçiriliyor ve dal pamuk iplikle yeniden sarılıyor. Dal kaynadıkça fıtığın da iyileşeceğine inanılıyor.'),
 dict(kaynak=OCAK, kisa=f'Acar, {LH}, 2017', link='yazilar/samanizm-ve-kam-gelenegi/',
  post='Denizli’deki devre ocağında yara için hastanın getirdiği patates üç dilime kesilip ipe diziliyor ve eve asılıyor; patates kurudukça yaranın da kuruyacağına inanılıyor. Konya’daki çıbık ocağında ise asma çubuğu halka yapılıyor ve gözü burnu kızaran çocuk bu halkanın içinden geçiriliyor.'),
 dict(kaynak=TAFLAN, kisa=f'Karasu ve Yaşar, {LH}, 2023', link='toplama-takvimi/',
  post='Ordu ve Giresun’da taflan (karayemiş, Laurocerasus officinalis) hayvanların kış yemi: yapraklar ahır tavanına asılıyor. Keşap’ta inekte meme siğili için yapraklar yedi gün memeye sürülüyor; bu sırada hayvanın etrafında dönülüp İhlas suresi okunuyor, sonra bir yaprak üç gün hayvanın yanına bırakılıyor.'),
 dict(kaynak=LADEN, kisa=f'Şekeroğlu ve Gezici, {LH}, 2021', link='toplama-takvimi/',
  post='Laden (Cistus, kaya gülü, pamukluk, tavşancıl) reçinesi eskiden bitkilerin arasında otlayan keçi ve koyunların yününe yapışır, yün taranarak toplanırmış. Bugün yapraklı dallar suda kaynatılıyor, dibe çöken reçine toplanıyor. Laden Türkiye’de doğadan en çok toplanan üç bitkiden biri.'),
 dict(bitki='mersin', yore='XIV.–XV. yüzyıl Türkçe tıp metinleri', kaynak=SAC, kisa=f'Serarslan ve Altıntaş, {LH}, 2026',
  metin='Hacı Paşa’nın Müntahab-ı Şifâ’sı ve Sabuncuoğlu’nun Terceme-i Akrabâdîn’i gibi eserlerde saç dökülmesine mersin yağı ve mersin yaprağı önerilir; bir tarifte karışım her gece saç diplerine sürülür ve sabah mersin suyuyla yıkanır.',
  post='600 yıllık saç bakımı: Hacı Paşa ve Sabuncuoğlu gibi 14. ve 15. yüzyıl hekimleri saç dökülmesine mersin yağı öneriyor. Bir tarifte mersin yaprağı, mazı ve fesleğen kaynatılıyor, susam yağı ve laden ekleniyor; karışım her gece saç diplerine sürülüp sabah mersin suyuyla yıkanıyor.'),
 dict(bitki='safran', yore='XIV.–XVI. yüzyıl Türkçe tıp metinleri', kaynak=SAFRAN, kisa=f'Paşayeva ve Tekiner, {LH}, 2014',
  metin='İshak bin Murad’ın Edviye-i Müfrede’sinde (14. yy.) safran sıcak ve kuru mizaçlı sayılır, mide zayıflığına iyi geldiği ama fazlasının baş ağrısı yaptığı yazılır. Kemaliyye (16. yy.) de fazla safranın baş ağrısı yaptığı uyarısını tekrarlar.',
  post='14. yüzyılda yazılan ilk Türkçe ilaç kitaplarından Edviye-i Müfrede’de safran “sıcak ve kuru” mizaçlı sayılıyor, mideyi güçlendirdiği yazılıyor; ama bir uyarıyla: fazlası baş ağrısı yapar. Safran Osmanlı sultanlarının güç macunlarına da giriyordu. Safranbolu ise adını bu bitkiden alıyor.'),
 dict(kaynak=GUL, kisa=f'Güler ve Karataş, {LH}, 2014', link='kavram/',
  post='Edirne Sarayı’nın Gülhane’sinde hem gül bahçesi hem de gülsuyu yapılan bir bina vardı; Topkapı’daki Gülhane’de de sarayda yetişen güllerden gülsuyu yapılıyordu. 15. yüzyıl hekimlik kitabı Kemaliye, hamamdan sonra nemli boyna gül tozu sürülmesini öneriyor. Gül yağı Osmanlı’da hafızlık eğitiminde de yer almış.'),
 dict(kaynak=MEVLANA, kisa=f'Yeğenoğlu ve Sözen Şahne, {LH}, 2016', link='kavram/',
  post='Mevlânâ’da üzüm bir yolculuktur: koruk, olgun üzüm ve şarap bilmenin, bulmanın ve olmanın aşamalarını anlatır. Varlığın sırrına eren derviş için “üzüm olan derviş” denir. Konya’daki türbe bahçesine gülleri, babasının gül sevgisini yaşatmak için oğlu diktirmiş.'),
 dict(bitki='devedikeni', yore='Hristiyan söylencesi; Türkiye', kaynak=MERYEM, kisa=f'Ereni ve Şar, {LH}, 2020',
  metin='Söylenceye göre Meryem bu bitkinin altında dinlenip İsa’yı emzirirken sütünden bir damla yapraklara düşmüş; yapraklardaki beyaz damarların buradan geldiğine inanılır. Türkiye’de deve kengeri, sütlü kengel, akdiken, mübarek diken ve şevkülmeryem gibi adlarla bilinir.',
  post='Meryemana dikeninin yapraklarındaki beyaz damarlar bir söylenceye bağlanıyor: Meryem bu bitkinin altında İsa’yı emzirirken sütünden bir damla yapraklara düşmüş. Türkiye’de ise bitkinin pek çok adı var: deve kengeri, sütlü kengel, akdiken, mübarek diken, şevkülmeryem.'),
 dict(kaynak=TERE, kisa=f'Başağaoğlu ve Kavalalı, {LH}, 2019', link='rehber/',
  post='Tere (Lepidium sativum) Anadolu’da kerdeme ve cırcır adlarıyla da biliniyor. Halk arasında yaprağı salataya giriyor, tohumu baharat olarak kullanılıyor, ezilmiş tohumu siğile sürülüyor. Aynı kaynak bir uyarı da yapıyor: tohumun fazla alınması vücutta bozukluklara yol açabilir.'),
dict(kaynak=EGE, kisa='Öztürk ve ark., Türkiye’nin Etnobotanik Veritabanı, 2020', bitki='isirgan',
  post='1928–2014 arasında Türkiye’de yapılmış 930 etnobotanik çalışma tek bir veritabanında toplandı. En sık kaydedilen bitkiler: ısırgan (178 yayın), kuşburnu (157), ceviz (136), sarı kantaron (112), sinirotu (112) ve ebegümeci (109). Hepsi köy yollarında, bahçe kenarlarında bulunan sıradan bitkiler.'),
dict(kaynak=EGE, kisa='Öztürk ve ark., Türkiye’nin Etnobotanik Veritabanı, 2020', bitki='kusburnu',
  post='Kuşburnu için Türkiye’de 60 kadar yöresel ad kayıtlı: itburnu, köpek gülü, it gülü, öküzgötü, şilan, gülburnu, deligül, gelin göbeği, gülbubusu, dikenbaşı… Aynı bitki, her yörede başka bir adla. Sizin yörenizde ne deniyor?'),
dict(kaynak=EGE, kisa='Öztürk ve ark., Türkiye’nin Etnobotanik Veritabanı, 2020', bitki='kantaron',
  post='Anadolu’da “yara otu” adı tek bir bitkiye ait değil: Kastamonu’da sarı kantarona, Ankara’da boz otuna, Balıkesir, Bolu ve Giresun’da sinirotuna, Bilecik’te ise Prunella türlerine bu ad veriliyor. Yöresel ad tek başına bitkiyi tanımaya yetmez; Latince adı bu yüzden önemli.'),
dict(kaynak=EGE, kisa='Öztürk ve ark., Türkiye’nin Etnobotanik Veritabanı, 2020', bitki='isirgan',
  post='Türkiye’deki halk kayıtlarında bitkilerin en çok başvurulduğu dert hemoroid (367 farklı bitki), ardından mide ağrısı geliyor. Ciltte ise açık ara ilk sırada yara iyileştirme var: 467 bitki, 1.093 kayıt. Bu sayılar etkinliği değil, derdin ne kadar yaygın olduğunu anlatıyor.'),
]

def site_kul():
    """bitki id → [(yöre, metin)], kaynaklar: bitki id → [(etiket, url)]"""
    kul, kay = {}, {}
    for h in HALK:
        if h.get('bitki') and h.get('metin'):
            kul.setdefault(h['bitki'], []).append((h['yore'], h['metin']))
            if h['kaynak'] not in kay.setdefault(h['bitki'], []): kay[h['bitki']].append(h['kaynak'])
    return kul, kay

def post_metni(h, P=None):
    link = h.get('link') or (h['bitki'] + '/')
    return f"Halk hekimliğinden 🌿\n\n{h['post']}\n\nKaynak: {h['kisa']}\nbitkitabani.com/{link}\n\n#halkhekimliği"
