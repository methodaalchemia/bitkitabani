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
