# Zehirli bitkiler ve en çok karıştırılanlar (/rehber/zehirli-bitkiler/).
# id: katalogdaki sayfa (yoksa None). Metinler kaynaklardan özetlenmiştir; birebir alıntı yok.

KARIS = [
dict(id='gucigdemi', ad='Güz çiğdemi', lat='Colchicum türleri',
     benzer='Yenen çiğdem (Crocus) yumrusu; ilkbaharda ayı sarımsağı yaprakları',
     ayirt='Baytop’a göre yenen çiğdemde gövde yumrunun tam ortasından, güz çiğdeminde yanından çıkar. Ayı sarımsağı yaprağı ezilince belirgin sarımsak kokar; güz çiğdemi yaprağı kokmaz.',
     belirti='Kolşisin zehirlenmesi: birkaç saat sonra başlayan kusma ve şiddetli ishal, ardından organ yetmezliği. Belirtiler geç başladığı için “bir şey olmadı” sanılmamalı.'),
dict(id=None, ad='Baldıran', lat='Conium maculatum',
     benzer='Maydanoz, yabani havuç, rezene gibi şemsiyegillerden yenen otlar',
     ayirt='Gövde tüysüz, içi boş ve üzeri esmer-mor lekeli (Baytop). Ezilen yaprak kötü, fare idrarını andıran bir koku verir. Şemsiyegillerden bir otu kesin tanımıyorsan toplama.',
     belirti='Ağızda yanma, kas güçsüzlüğü, bacaklardan yukarı doğru ilerleyen felç; solunum durabilir. Sokrates’in zehirlendiği bitki budur.'),
dict(id='tatula', ad='Tatula', lat='Datura stramonium',
     benzer='Tohumları tahıl ve baklagillere karışabiliyor; dikenli meyvesi çocukların ilgisini çekiyor',
     ayirt='Ceviz büyüklüğünde, dikenli meyve kapsülü; içinde siyah, böbrek biçimli tohumlar. Yaprakları ezilince ağır ve hoş olmayan bir koku verir.',
     belirti='Ağız kuruluğu, göz bebeklerinde büyüme, yüzde kızarma, ateş, çarpıntı, huzursuzluk ve sanrılar.'),
dict(id='banotu', ad='Banotu', lat='Hyoscyamus niger',
     benzer='Yöreye göre “gavurhaşhaşı” ya da “dağdağan” diye de anılıyor; aynı adlar başka bitkilere de veriliyor (Baytop)',
     ayirt='Yapışkan tüylü yapraklar, mor damarlı soluk sarı çiçekler ve ağır bir koku. Yöresel ada güvenme, bitkinin kendisine bak.',
     belirti='Tatulayla aynı tablo: ağız kuruluğu, göz bebeklerinde büyüme, çarpıntı, bilinç bulanıklığı.'),
dict(id=None, ad='Yüksük otu', lat='Digitalis türleri',
     benzer='Çiçek açmadan önce yaprakları karakafes otu ve sığır kuyruğu yapraklarına benziyor',
     ayirt='Çiçeklenince yüksük biçimli, sarkık ve sapın tek yanına dizilmiş çiçekler. Çiçeksiz bir yaprak rozetini kesin tanımadan çay yapma.',
     belirti='Kalp glikozitleri: bulantı, kusma, görmede sarı-yeşil renkler, kalp ritim bozukluğu.'),
]

HALK = [
dict(id=None, ad='Deli bal (ormangülü)', metin='Doğu Karadeniz’de arıların ormangülü (Rhododendron ponticum; yörede komar, kara ağu) ve sarı çiçekli R. luteum (sarı ağu) çiçeklerinden yaptığı baldır. Atinalı Ksenofon, MÖ 400 dolaylarında bu bölgeden geçen Grek askerlerinin bu baldan zehirlendiğini anlatır. Bugün “şifa” diye kaşıkla yenmesi zehirlenmelerin başlıca nedeni: baş dönmesi, bulantı, terleme, nabız ve tansiyon düşmesi görülür. Hastanede tedavi edilir (Baytop).'),
dict(id='zakkum', ad='Zakkum', metin='Park ve bahçelerde süs bitkisi olarak her yerde. Yaprağının şeker ya da kanser için kaynatılıp içilmesi ciddi kalp zehirlenmelerine yol açıyor; az miktarı bile tehlikeli.'),
dict(id='hashas', ad='Haşhaş', metin='Sağlık Bakanlığı’nın Fitoterapi kitabına göre etnobotanik çalışmalarda afyonun çocuk uyutmak için kullanıldığı hâlâ görülüyor; bu kullanım Osmanlı dönemine uzanıyor. Bebeklerde solunumu durdurabilir.'),
dict(id=None, ad='Acı badem ve kayısı çekirdeği', metin='İçerdikleri amigdalin vücutta siyanüre dönüşür. Çocuklar için birkaç tane bile tehlikeli olabilir; “kanser tedavisi” diye satılan acı kayısı çekirdeği de aynı riski taşır.'),
]

NEDEN = ['Tedavi için kullanılan bir bitkiden fazla miktarda almak',
         'Şifalı bitki yerine ona benzeyen zehirli bir bitkiyi kullanmak',
         'Sebze ya da ot diye toplanan bitkinin yerine yanlışlıkla zehirli bir türü yemek',
         'Bir bitkinin hangi kısmının zehirli olduğunu bilmeden yemek',
         'Çocuk düşürmek amacıyla zehirli bitki kullanmak']

KAYNAK = [('Baytop T., Türkiye’de Bitkiler ile Tedavi: Geçmişte ve Bugün, 3. baskı, Nobel Tıp Kitabevleri, 2021', ''),
          ('T.C. Sağlık Bakanlığı, Fitoterapi Uygulaması Kitabı, 2022 (“Zehirli bitkiler” bölümü)', ''),
          ('Baytop T., Baytop A., Mat A., Sun S., Türkiye’de zehirli bitkiler, bitki zehirlenmeleri ve tedavi yöntemleri, İstanbul Üniversitesi, 1989 (Fitoterapi kitabındaki atıfla)', '')]
