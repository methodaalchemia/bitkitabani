# -*- coding: utf-8 -*-
# Familya bilgisi: /familya/ sayfası ve familya sayfaları için.
# "ortak": familyayı tanıtan, üyelerinin paylaştığı botanik ve kimyasal özellikler.
# "dikkat": familya düzeyinde güvenlik ya da karıştırma uyarısı (varsa).
# Kaynak: familya düzeyindeki bileşik grupları için farmakognozi el kitabı, taksonomi için Kew POWO.

EVANS = ('William Charles Evans, Trease and Evans’ Pharmacognosy, 16. baskı, Saunders/Elsevier, 2009', '')
BAYTOP_K = ('Turhan Baytop, Türkiye’de Bitkiler ile Tedavi, Nobel Tıp Kitabevleri, 2021 (3. baskı)', '')

FAM_TR = {
 'Lamiaceae': 'ballıbabagiller', 'Solanaceae': 'patlıcangiller', 'Asteraceae': 'papatyagiller',
 'Rubiaceae': 'kökboyasıgiller', 'Malvaceae': 'ebegümecigiller', 'Fabaceae': 'baklagiller',
 'Anacardiaceae': 'sakızağacıgiller', 'Ranunculaceae': 'düğünçiçeğigiller', 'Rosaceae': 'gülgiller',
 'Apiaceae': 'maydanozgiller', 'Cactaceae': 'kaktüsgiller', 'Euphorbiaceae': 'sütleğengiller',
 'Lythraceae': 'kınagiller', 'Arecaceae': 'palmiyegiller', 'Myrtaceae': 'mersingiller',
 'Papaveraceae': 'gelincikgiller', 'Zingiberaceae': 'zencefilgiller', 'Rutaceae': 'sedefotugiller',
 'Lauraceae': 'defnegiller', 'Sapindaceae': 'sabunağacıgiller',
}

# fam: (ortak özellikler, familya düzeyinde dikkat notu ya da '')
FAM_BILGI = {
 'Lamiaceae': ('Dört köşeli gövdesi, karşılıklı yaprakları ve dudak biçimli çiçekleriyle tanınır. Yaprak yüzeyindeki salgı tüylerinde uçucu yağ biriktirir; timol, karvakrol, linalool ve 1,8-sineol gibi monoterpenler bu familyada yaygındır. Mutfakta ve çay olarak kullanılan bitkilerin büyük bölümü buradan gelir.',
   'Bitkinin kendisi çay olarak ölçülü kullanıldığında genelde sorun çıkarmaz; aynı bitkinin damıtılmış uçucu yağı ise çok daha derişiktir ve ağızdan alınması tahriş edicidir.'),
 'Solanaceae': ('Aynı familyada hem günlük gıdalar hem de en güçlü etkili bitkiler bulunur. Üyelerinin bir bölümü tropan alkaloitleri (atropin, skopolamin, hiyosiyamin) ya da nikotin taşır; bu maddeler sinir sisteminde asetilkolin ve nikotin almaçları üzerinden iş görür.',
   'Bu familyanın ritüel bitkilerinde etkili doz ile zehirli doz birbirine çok yakındır. Veri tabanındaki yüksek riskli kayıtların önemli bölümü buradan gelir.'),
 'Asteraceae': ('Çiçek sandığımız yapı aslında yüzlerce küçük çiçekten oluşan bir başçıktır. Seskiterpen laktonlar, acı maddeler ve depo karbonhidratı olarak inülin familyada yaygındır.',
   'Seskiterpen laktonlar temas alerjisi yapabilir: bir papatyagile duyarlı olan kişi aynı familyanın başka üyelerine de tepki verebilir.'),
 'Fabaceae': ('Kelebek biçimli çiçekleri ve bakla meyvesiyle tanınır. Kök yumrularındaki bakterilerle havanın azotunu toprağa bağlar. Saponinler, izoflavonlar ve bazı türlerde toksik alkaloitler ya da lektinler bulunur.',
   'Familyanın bazı üyelerinin çiğ tohumu lektin içerir ve pişirilmeden yenmez.'),
 'Malvaceae': ('Müsilaj denen kaygan polisakkaritler bakımından zengindir. Geleneksel kullanımların çoğu bu kaygan tabakanın boğazı ve sindirim yolunu kaplamasına dayanır.',
   'Müsilaj aynı anda alınan ilaçların emilimini geciktirebilir; araya birkaç saat koymak gerekir.'),
 'Rubiaceae': ('İndol alkaloitleri ve antrakinon boyalar bu familyanın imzasıdır. Sıtma ilacı kinin de, kahvenin kafeini de, kök boyanın kırmızısı da buradan çıkar.', ''),
 'Myrtaceae': ('Yaprakları ışığa tutulduğunda görülen saydam bezlerde uçucu yağ taşır; 1,8-sineol ve öjenol familyada yaygındır. Çoğu üyesi hem baharat hem kokulu bitki olarak kullanılır.',
   'Uçucu yağları derişiktir: küçük çocuklarda yüze ya da buruna sürülmesi solunum sorunu yaratabilir.'),
 'Ranunculaceae': ('Taze bitkide bulunan ranunkulin, doku ezildiğinde tahriş edici protoanemonine dönüşür. Familyada izokinolin alkaloitleri de yaygındır.',
   'Taze haldeyken deriyi ve mukozayı tahriş eden türleri çoktur; kurutma bu etkiyi büyük ölçüde giderir.'),
 'Apiaceae': ('Şemsiye biçimli çiçek durumu ve kokulu meyveleriyle tanınır. Anetol ve kumin aldehit gibi uçucu yağ bileşenleri, bir de furanokumarinler taşır.',
   'Bu familya karıştırma riskinin en yüksek olduğu familyadır: yenen türlerle ölümcül zehirli türler (baldıran gibi) birbirine benzer. Furanokumarinler ayrıca deriyi güneşe duyarlı hale getirebilir.'),
 'Anacardiaceae': ('Reçine kanalları ve tanen bakımından zengindir; sakız, baharat ve boya veren üyeleri vardır. Urushiol benzeri alkilfenoller familyanın ayırt edici bileşik grubudur.',
   'Alkilfenoller duyarlı kişilerde temas dermatiti yapabilir.'),
 'Papaveraceae': ('Gövdesi kırıldığında süt ya da renkli lateks verir. İzokinolin alkaloitleri familyanın imzasıdır; morfin de sanguinarin de bu gruptandır.',
   'Familyanın alkaloitleri güçlü etkilidir ve bir bölümü Türkiye’de yasal denetime tabidir.'),
 'Zingiberaceae': ('Toprak altındaki rizomda uçucu yağ ve keskin tatlı maddeler biriktirir: gingeroller ve kurkuminoidler bu familyaya özgüdür.',
   'Kan sulandırıcı kullananlarda yüksek dozları kanama riskini artırabilir.'),
 'Rutaceae': ('Yapraklarındaki saydam yağ bezleri familyanın en kolay tanınan özelliğidir. Turunçgiller de sedef otu da bu familyadandır; furanokumarin ve uçucu yağ bakımından zengindir.',
   'Furanokumarinler hem deriyi güneşe duyarlı hale getirir hem de karaciğerdeki ilaç enzimlerini etkileyerek ilaç düzeylerini değiştirebilir.'),
 'Rosaceae': ('Beş taç yapraklı çiçekleri ve çok sayıda erkek organıyla tanınır. Tanen bakımından zengindir; meyveleri yenen pek çok türü içerir.',
   'Bazı üyelerinin çekirdeğinde siyanojenik glikozitler bulunur; çekirdek yenmez.'),
 'Lauraceae': ('Kokulu, derimsi yaprakları olan ağaç ve çalılardan oluşur. Sinnamaldehit ve öjenol gibi uçucu yağ bileşenleri familyada yaygındır.', ''),
 'Cactaceae': ('Su depolayan etli gövdeleri ve yaprak yerine dikenleriyle tanınır. Bazı türleri fenetilamin alkaloitleri taşır ve And geleneğinde ritüel bitkisi olarak kullanılır.',
   'Alkaloit taşıyan türleri Türkiye’de ve pek çok ülkede yasal denetime tabidir.'),
 'Euphorbiaceae': ('Çoğu üyesi kırıldığında beyaz lateks verir. Familya hem temel gıda bitkilerini hem güçlü tahriş edici türleri barındırır.',
   'Lateks deride ve gözde tahriş yapabilir; türlerin önemli bir bölümü ağızdan alınmaz.'),
 'Lythraceae': ('Naftokinon boyalar familyanın ayırt edici özelliğidir; kınanın rengini veren lawson bu gruptandır.',
   'Doğal kına turuncu-kırmızı boyar; “siyah kına” diye satılan karışımlara eklenen boyar madde ağır alerji yapabilir.'),
 'Sapindaceae': ('Saponin bakımından zengindir; bazı türlerinin meyvesi suyla çırpıldığında köpürür ve geleneksel olarak sabun yerine kullanılmıştır. Familyanın bir bölümü kafein taşır.', ''),
 'Arecaceae': ('Tek bir büyüme noktasından gelişen gövdesi ve büyük yapraklarıyla ayrılır. Meyveleri yağ asitleri, fitosteroller ve yağda çözünen renk maddeleri bakımından zengindir.', ''),
}

def fam_kaynak(f, anadolu=False):
    """Familya sayfasının kaynakları."""
    ks = [('Kitap', EVANS[0], '')]
    if anadolu: ks.append(('Kitap', BAYTOP_K[0], ''))
    ks.append(('Botanik kayıt', f'Kew Plants of the World Online: {f}', 'https://powo.science.kew.org/results?q=' + f))
    return ks
