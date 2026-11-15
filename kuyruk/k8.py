# TİTCK + AB monografı birlikte olan bitkilerden ilk parti (17–19 Aralık).
#
# Bu üç kayıt, hem TİTCK Tıbbi Bitki Listesi'nde hem Avrupa İlaç Ajansı'nın
# bitkisel monograflarında bulunan 68 türlük kümeden geliyor. Üçünün EMA
# monografı da "iyi bilinen kullanım" (well-established use) kategorisinde,
# yani EMA klinik kanıta dayandığını kabul ediyor.
#
# ⚠️ Kanıt düzeyi yine de EMA kategorisine eşitlenmedi. EMA'nın "iyi bilinen
# kullanım" demesi, bağımsız sistematik derlemelerin aynı şeyi söylediği
# anlamına gelmiyor: sarmaşıkta derleme etkinin klinik anlamını "asgari"
# buluyor ve yanlılık riskini yüksek görüyor. Her kayıtta düzenleyici
# kategori ile literatürün söylediği ayrı ayrı yazıldı.
Q = [

    dict(
        yayin='2026-12-17',
        id='sarmasik',
        foto='Hedera helix Dover.jpg',
        tr='Sarmaşık',
        la='Hedera helix L.',
        fam='Araliaceae (sarmaşıkgiller)',
        diger='Duvar sarmaşığı, orman sarmaşığı. TİTCK monografı Hedera aurantiaca '
              've Hedera baccifera adlarını sinonim olarak veriyor. İngilizce ivy, '
              'common ivy, English ivy.',
        bolge=['anadolu', 'avrupa'],
        kat=['sifa'],
        kisim='Yaprak',
        taxon='Hedera helix',
        kul=[
            ['Avrupa — balgam söktürücü', 'Sarmaşık yaprağı ekstresi Avrupa’da '
             'balgamlı öksürükte en çok satılan bitkisel ilaç biçimlerinden biri: '
             'şurup, damla ve efervesan tablet hâlinde reçetesiz satılıyor. Avrupa '
             'İlaç Ajansı yaprağı 2009’da monografa aldı ve endikasyonu "iyi bilinen '
             'kullanım" başlığı altına koydu — yani ajansa göre kullanım klinik '
             'kanıta dayanıyor, yalnızca kullanım geçmişine değil. Monograftaki '
             'endikasyon tek cümle: balgamlı öksürükte balgam söktürücü.'],
            ['Türkiye — resmî liste', 'TİTCK Tıbbi Bitki Listesi’nde yaprağıyla yer '
             'alıyor; monograf kullanılan kısmı "yapraklar" diye veriyor ve '
             'güvenlilik uyarılarını ayrı bölümde sıralıyor. Türkiye’de sarmaşık '
             'yaprağı ekstresi içeren öksürük şurupları eczanelerde bulunuyor.'],
            ['Anadolu', 'Sarmaşık Türkiye’nin nemli orman ve bahçelerinde yayılış '
             'gösteriyor; duvarlara ve ağaç gövdelerine tutunan yaprağı yıl boyu '
             'yeşil kalıyor. Yaprağın tıbbi kullanımı Anadolu halk hekimliğinden '
             'çok Avrupa fitoterapisinden geliyor.'],
        ],
        haz='Avrupa İlaç Ajansı monografı yaprağın kendisini değil, ondan '
            'hazırlanan standart ekstreleri tarif ediyor; dolayısıyla evde '
            'hazırlanan bir biçim yok. Monografta ergen, yetişkin ve yaşlılar için '
            'beş ayrı ekstre tipi ve her birinin günlük dozu ayrı ayrı yazılı; '
            'kuru ekstreler için tek doz 15–65 mg, günlük doz 45–105 mg aralığında, '
            'etanol içeren bitmiş ürünlerde günlük en yüksek doz 67 mg. Bu dozlar '
            'ekstrenin kendisine ait: hangi ekstre tipinin kullanıldığı ürünün '
            'kutusunda yazılıdır ve biri diğerinin yerine geçmez. Yaprağın çayı '
            'monografta yer almıyor.',
        bilim='Burada düzenleyici karar ile bağımsız literatür ayrışıyor ve bu ayrım '
              'kaydın en önemli bilgisi. Avrupa İlaç Ajansı endikasyonu "iyi bilinen '
              'kullanım" kategorisine koyuyor. Buna karşılık 2021’de güncellenen bir '
              'sistematik derleme (Eur J Clin Pharmacol) altı randomize çalışma, bir '
              'kontrollü çalışma ve dört gözlemsel çalışmayı değerlendirip şu sonuca '
              'varıyor: çalışmaların hepsi sarmaşık ekstresini etkili ve güvenli '
              'buluyor, üç randomize çalışma öksürüğün şiddetinde ya da sıklığında '
              'daha hızlı azalma bildiriyor, ama bu etkilerin klinik anlamı asgari '
              'görünüyor; raporlama kalitesi düşük ve yanlılık riski yüksek. Ciddi '
              'yan etki bildirilmemiş. Yani etkinin varlığı değil büyüklüğü ve '
              'kanıtın kalitesi tartışmalı. Sitede kanıt düzeyi bu yüzden "klinik" '
              'değil "sınırlı" olarak etiketlendi: düzenleyici onay tek başına güçlü '
              'bağımsız kanıt demek değil.',
        kanit='sinirli',
        guv='orta',
        guvNot='İki yaşın altındaki çocuklarda kullanılmaz: Avrupa İlaç Ajansı '
               'monografı bunu kontrendikasyon olarak yazıyor, gerekçe balgam '
               'söktürücülerin solunum belirtilerini ağırlaştırma riski. İki–dört '
               'yaş arasında inatçı ya da yineleyen öksürük, tedaviden önce hekim '
               'tanısı gerektiriyor. Araliaceae familyası bitkilerine ya da etkin '
               'maddeye aşırı duyarlılık olanlar kullanmamalı. Taze yapraklar '
               'alerjik kontak dermatite yol açabilir. Bildirilmiş istenmeyen '
               'etkiler: bulantı, kusma, ishal gibi mide-bağırsak tepkileri ve '
               'ürtiker, deri döküntüsü, nefes darlığı, anafilaktik tepki gibi '
               'alerjik tepkiler; ikisinin de sıklığı bilinmiyor. Gastrit ya da '
               'mide ülseri olanlarda dikkatli kullanılmalı. Nefes darlığı, ateş '
               'ya da iltihaplı balgam varsa hekime ya da eczacıya başvurulmalı. '
               'Yeterli veri olmadığı için gebelikte ve emzirme döneminde '
               'kullanılması önerilmiyor; doğurganlık verisi yok.',
        etk=[
            ['Öksürük kesiciler (kodein, dekstrometorfan)',
             'TİTCK monografı sarmaşığın kodein ya da dekstrometorfan gibi öksürük '
             'kesici ilaçlarla etkileşebileceğini yazıyor. Mantık şu: sarmaşık '
             'balgam söktürücü, yani balgamı sulandırıp atılmasını kolaylaştırıyor; '
             'öksürük kesici ise balgamı dışarı atacak refleksi bastırıyor. İkisi '
             'birlikte alındığında sulanan balgam solunum yollarında birikebilir. '
             'Birlikte kullanım hekim ya da eczacı değerlendirmesi gerektirir.'],
            ['Avrupa İlaç Ajansı monografında bildirilmiş etkileşim yok',
             'EMA monografının etkileşim bölümü "bildirilmemiş" diyor. Bu, '
             'etkileşim olmadığının kanıtı değil, araştırılmadığının ifadesidir; '
             'TİTCK’nin öksürük kesici uyarısı farmakolojik akıl yürütmeye '
             'dayanıyor.'],
        ],
        ilginc='Sarmaşığın tıbbi kullanımı yaprakta; oysa bitkinin ünü meyvesinden '
               'gelen zehirlilikle karışıyor. Monografa giren kısım yalnızca '
               'yaprak, ve orada da kullanılan şey yaprağın kendisi değil ondan '
               'çıkarılan standart ekstre. "Doğal olduğu için yumuşaktır" '
               'varsayımının nerede kırıldığının iyi bir örneği: iki yaş altı '
               'çocuklarda kullanımı yasaklayan şey bitkinin zehirliliği değil, '
               'balgam söktürücü etkisinin kendisi.',
        ek=dict(
            mevsim='Yıl boyu yeşil. Eylül–kasım arasında yeşilimsi sarı çiçek '
                   'açar — Avrupa’da sonbaharın en son nektar kaynaklarından biri. '
                   'Meyveler kış sonu ve ilkbaharda olgunlaşır.',
            yetisme='Avrupa, Batı Asya ve Kuzey Afrika kökenli. Türkiye’nin nemli '
                    'ormanlarında, bahçe duvarlarında ve ağaç gövdelerinde yayılış '
                    'gösterir. Gölgeye son derece dayanıklı; köksü yapılarla '
                    'tutunarak 20–30 metreye kadar tırmanır.',
            yoresel='Türkiye’de en yaygın adı sarmaşık; TİTCK monografı "sarmaşık, '
                    'duvar sarmaşığı" diye veriyor. Not: "sarmaşık" adı Türkçede '
                    'tırmanan birçok bitki için kullanılıyor — kahve sarmaşığı, '
                    'acem borusu, filbahri gibi. Tıbbi olan tür Hedera helix.',
            karisma='Adı tırmanan birçok bitkiye verildiği için karışma riski '
                    'yüksek. Özellikle zehirli Amerikan sarmaşığı (Parthenocissus) '
                    've acem borusu (Campsis) ile karıştırılmamalı. Eczane '
                    'ürünlerinde kullanılan kısım standart ekstre olduğu için '
                    'kutudaki Latince ad belirleyicidir.',
        ),
        ema=[('Hederae helicis folium',
              'https://www.ema.europa.eu/en/medicines/herbal/hederae-helicis-folium')],
        kaynak=[
            ['Elizabeth Sierocinski, Felix Holzinger, Jean-François Chenot, '
             '“Ivy leaf (Hedera helix) for acute upper respiratory tract '
             'infections: an updated systematic review”, European Journal of '
             'Clinical Pharmacology 77(8): 1113–1122, 2021',
             'https://pubmed.ncbi.nlm.nih.gov/33523253/'],
            ['Hedera helix L. monografı, TİTCK Tıbbi Bitki Listesi',
             'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/HederahelixL.46da4ab6263f4179b100319e18963e6b_a66612a6-308e-4ce9-b1be-3e24d66a74b6.pdf'],
        ],
        rel=['mese', 'ihlamur'],
        en=dict(
            name='Common ivy',
            other='Also called English ivy or wall ivy. The Turkish regulatory '
                  'monograph lists Hedera aurantiaca and Hedera baccifera as '
                  'synonyms.',
            part='The leaf',
            uses=[
                ['Europe — expectorant', 'Ivy leaf extract is one of the '
                 'best-selling over-the-counter herbal preparations for productive '
                 'cough in Europe, sold as syrup, drops and effervescent tablets. '
                 'The European Medicines Agency adopted a monograph in 2009 and '
                 'placed the indication under "well-established use", meaning the '
                 'agency accepts that the use rests on clinical evidence rather '
                 'than on a history of use alone. The monograph indication is one '
                 'sentence: an expectorant in case of productive cough.'],
                ['Turkey — official list', 'The leaf is listed in the Turkish '
                 'Medicines and Medical Devices Agency’s medicinal plant '
                 'inventory, with its own safety warnings. Cough syrups containing '
                 'ivy leaf extract are available in Turkish pharmacies.'],
                ['Anatolia', 'Ivy grows in moist woodland and gardens across '
                 'Turkey, clinging to walls and tree trunks, evergreen all year. '
                 'Its medicinal use comes from European phytotherapy rather than '
                 'from Anatolian folk medicine.'],
            ],
            prep='The EMA monograph describes standardised extracts rather than the '
                 'leaf itself, so there is no home preparation. It lists five '
                 'separate extract types for adolescents, adults and the elderly, '
                 'each with its own dose; for dry extracts a single dose of '
                 '15–65 mg and a daily dose of 45–105 mg, with a maximum daily dose '
                 'of 67 mg for ethanol-containing finished products. These doses '
                 'belong to the extract, not the plant, and one extract type is not '
                 'interchangeable with another. Leaf tea is not in the monograph.',
            science='Here the regulatory decision and the independent literature '
                    'diverge, and that divergence is the important part. The EMA '
                    'places the indication under "well-established use". An updated '
                    'systematic review in 2021 (Eur J Clin Pharmacol) assessed six '
                    'randomised trials, one controlled trial and four observational '
                    'studies and concluded: all studies found ivy leaf extract '
                    'effective and safe, three randomised trials reported a more '
                    'rapid reduction in cough severity or frequency, but the '
                    'clinical significance of these effects appears to be minimal, '
                    'the overall quality of reporting was low and the risk of bias '
                    'was high. No serious adverse effects were reported. What is '
                    'disputed is not whether there is an effect but how large it is '
                    'and how good the evidence behind it is. The evidence level on '
                    'this site is therefore labelled Limited rather than Clinical: '
                    'regulatory approval on its own does not amount to strong '
                    'independent evidence.',
            safety='Contraindicated in children under 2 years of age: the EMA '
                   'monograph gives this as a contraindication, on the grounds that '
                   'secretolytic medicines can aggravate respiratory symptoms. '
                   'Persistent or recurrent cough in children aged 2–4 requires a '
                   'medical diagnosis before treatment. Not for anyone '
                   'hypersensitive to the active substance or to plants of the '
                   'Araliaceae family. Fresh leaves can cause allergic contact '
                   'dermatitis. Reported undesirable effects are gastrointestinal '
                   '(nausea, vomiting, diarrhoea) and allergic (urticaria, skin '
                   'rash, dyspnoea, anaphylactic reaction); the frequency of both '
                   'is unknown. Caution in gastritis or gastric ulcer. Seek medical '
                   'advice if dyspnoea, fever or purulent sputum occurs. Safety in '
                   'pregnancy and lactation has not been established, so use is not '
                   'recommended; no fertility data are available.',
            fact='The medicinal part is the leaf, while the plant’s reputation '
                 'for toxicity comes from its berries. What enters the monograph is '
                 'the leaf only, and even then not the leaf itself but a '
                 'standardised extract of it. It is also a good example of where '
                 '"natural means gentle" breaks down: what rules it out for '
                 'children under two is not the plant’s toxicity but the '
                 'expectorant effect itself.',
            season='Evergreen. Flowers greenish-yellow from September to November, '
                   'one of the last nectar sources of the European autumn. Berries '
                   'ripen in late winter and spring.',
            habitat='Native to Europe, western Asia and North Africa. Found in '
                    'moist woodland, on garden walls and tree trunks throughout '
                    'Turkey. Extremely shade-tolerant; climbs 20–30 m using '
                    'rootlike holdfasts.',
            local='Usually sarmaşık in Turkish; the regulatory monograph gives '
                  '"sarmaşık, duvar sarmaşığı". Note that sarmaşık is used in '
                  'Turkish for many climbing plants; the medicinal species is '
                  'Hedera helix.',
            confusion='Because the Turkish name is applied to many climbers, the '
                      'risk of confusion is high — in particular with Virginia '
                      'creeper (Parthenocissus) and trumpet vine (Campsis). In '
                      'pharmacy products the part used is a standardised extract, '
                      'so the Latin name on the box is what settles it.',
        ),
        etk_en=[
            ['Antitussives (codeine, dextromethorphan)',
             'The Turkish regulatory monograph notes that ivy may interact with '
             'antitussive medicines such as codeine or dextromethorphan. The '
             'reasoning: ivy is an expectorant, thinning mucus so that it can be '
             'coughed up, while an antitussive suppresses the very reflex that '
             'clears it. Taken together, thinned secretions may accumulate in the '
             'airways. Combined use calls for a doctor’s or pharmacist’s '
             'assessment.'],
            ['No interactions reported in the EMA monograph',
             'The interaction section of the EMA monograph says "none reported". '
             'That is a statement about what has been studied, not evidence that no '
             'interaction exists; the Turkish warning rests on pharmacological '
             'reasoning.'],
        ],
    ),

    dict(
        yayin='2026-12-18',
        id='karniyarik',
        foto='Plantago ovata kz13.jpg',
        tr='Karnıyarık otu',
        la='Plantago ovata Forssk.',
        fam='Plantaginaceae (sinirotugiller)',
        diger='TİTCK monografı Türkçe adı "sarı karnıyarık otu", İngilizce adı '
              '"ispaghula husk" diye veriyor; sinonimleri Plantago brunnea, '
              'Plantago fastigiata ve Plantago insularis. Ticarette psyllium ya da '
              'ispagula adıyla geçer. Dikkat: Türkçede "karnıyarık" adı sinirotu '
              '(Plantago major, P. lanceolata) için de kullanılıyor; bu kayıt '
              'yalnızca P. ovata için.',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Tohum, tohum kabuğu',
        taxon='Plantago ovata',
        kul=[
            ['Hindistan ve İran — lif kaynağı', 'Tohum kabuğu suyla temas ettiğinde '
             'hacminin kat kat üstüne şişen bir jel oluşturuyor; geleneksel '
             'kullanım da bu fiziksel özelliğe dayanıyor. Dünya üretiminin büyük '
             'bölümü Hindistan’ın Gucerat bölgesinden geliyor.'],
            ['Avrupa — kabızlıkta onaylı kullanım', 'Avrupa İlaç Ajansı tohumu ve '
             'tohum kabuğunu ayrı monograflarla aldı ve her ikisinde de alışkanlık '
             'hâline gelmiş kabızlık endikasyonunu "iyi bilinen kullanım" başlığına '
             'koydu. Monograflarda kabızlığın yanında, dışkının yumuşak kalmasının '
             'tıbbi olarak gerekli olduğu durumlar da endikasyon olarak yazılı.'],
            ['Türkiye — resmî liste', 'TİTCK monografı kullanılan kısmı '
             '"tohumları, tohum kabukları (testa epiderması)" diye veriyor ve '
             'uyarıları sıralıyor; literatür olarak EMA 2013 monografını '
             'gösteriyor.'],
        ],
        haz='TİTCK monografı iki noktayı öne çıkarıyor: yeterli miktarda sıvı (su, '
            'süt, meyve suyu ya da benzeri) ile alınması ve etkinin 12–24 saat '
            'sonra başlaması. Sıvı koşulu biçimsel bir uyarı değil: kabuk bağırsakta '
            'jel oluşturarak çalıştığı için yetersiz sıvıyla alındığında tıkanmaya '
            'yol açabilir. Diğer ilaçlarla aynı anda alınmamalı — araya en az bir '
            'saat konmalı. Üç gün kullanımda belirtiler geçmezse hekime başvurulmalı.',
        bilim='Psyllium lifi, bitkisel ürünler arasında randomize kanıtı en sağlam '
              'olanlardan biri. LDL kolesterol üzerine 28 randomize çalışmanın '
              '(toplam 1924 katılımcı) meta-analizi, günde ortalama 10,2 gram '
              'psyllium’un LDL kolesterolü 0,33 mmol/L düşürdüğünü buluyor (%95 '
              'güven aralığı 0,27–0,38); HDL dışı kolesterolde 0,39 mmol/L, '
              'apolipoprotein B’de 0,05 g/L düşüş var. GRADE değerlendirmesinde LDL '
              've HDL dışı kolesterol için kanıt "orta" kalitede (tutarsızlık '
              'nedeniyle düşürülmüş), apoB için "yüksek" kalitede. Kabızlık tarafı '
              'daha zayıf: beş randomize çalışmayı toplayan bir meta-analiz lifin '
              'dışkılama sıklığını plaseboya göre anlamlı biçimde artırdığını, ama '
              'dışkı kıvamı, tedavi başarısı, müshil kullanımı ve ağrılı dışkılama '
              'bakımından anlamlı fark bulunmadığını bildiriyor. Bir başka randomize '
              'çalışma, ülseratif kolitte remisyonun sürdürülmesinde P. ovata '
              'tohumunu mesalazinle karşılaştırıyor. Toparlarsak: lipit etkisi iyi '
              'belgelenmiş ve ölçülü büyüklükte, kabızlık etkisi dar bir son noktada '
              'gösterilmiş.',
        kanit='klinik',
        guv='orta',
        guvNot='Yutma güçlüğü ya da boğaz problemi olanlar kullanmamalı. Bağırsak '
               'tıkanması (ileus), bağırsak felci, megakolon, mide-bağırsak yolu ve '
               'yemek borusu problemleri ile kalp hastalığı durumunda '
               'kullanılmamalı. TİTCK monografı diyabet ve tiroit hastalarının '
               'kullanmaması gerektiğini yazıyor. Yeterli miktarda sıvıyla '
               'alınmalı; yetersiz sıvı tıkanma riski doğurur. Yeterli veri '
               'olmadığı için gebelikte ve emzirme döneminde kullanılması '
               'önerilmiyor, 12 yaşın altındaki çocuklarda da önerilmiyor. Etkin '
               'maddeye aşırı duyarlılık görülebilir.',
        etk=[
            ['Bütün ilaçlar — emilim gecikmesi',
             'TİTCK monografı, başka ilaç kullananların bitkisel ürünle ilaç '
             'arasına en az bir saat koymasını istiyor. Gerekçe fiziksel: bağırsakta '
             'oluşan jel, yanında alınan ilacın emilimini geciktirip azaltabilir. '
             'Bu, tek tek ilaçlara özgü bir etkileşim değil, lifin kendisinden '
             'kaynaklanan genel bir kuraldır.'],
            ['B12 vitamini, mineraller, kardiyak glikozitler, kumarin türevleri, '
             'karbamazepin, lityum',
             'TİTCK monografı bu grupları adıyla sayıyor: bağırsaktan emilen '
             'mineraller ve vitaminler (B12), kalp glikozitleri (dijital grubu), '
             'kumarin türevi kan sulandırıcılar, karbamazepin ve lityum. Bunların '
             'hepsinde etki, kan düzeyinin dar bir aralıkta kalmasına bağlı olduğu '
             'için emilimdeki değişiklik önemlidir.'],
            ['Bağırsak hareketini yavaşlatan ilaçlar (opioidler)',
             'TİTCK monografı peristaltik hareketleri baskılayan ilaçlarla birlikte '
             'kullanılmaması gerektiğini yazıyor. Jel oluşturan lif, bağırsak '
             'hareketi yavaşlatılmışken ilerleyemeyip tıkanmaya yol açabilir.'],
        ],
        ilginc='Etkisi kimyasal değil fiziksel: psyllium kabuğu bağırsakta '
               'fermente olmayan, jel oluşturan bir lif. Kolesterolü düşürmesi de, '
               'kabızlıkta işe yaraması da aynı mekanizmadan geliyor — safra '
               'asitlerini bağlayıp jel hâlinde tutmak. Aynı mekanizma yetersiz '
               'sıvıyla alındığında neden tıkanma riski doğurduğunu da açıklıyor.',
        ek=dict(
            mevsim='Yıllık bitki; ilkbaharda çiçek açar, tohumlar yaz başında '
                   'olgunlaşır.',
            yetisme='Akdeniz havzası ve Batı Asya kökenli; kurak, kumlu topraklarda '
                    'yetişir. Ticari üretim büyük ölçüde Hindistan’ın kuzeybatısında '
                    've İran’da yapılıyor.',
            yoresel='TİTCK monografı "sarı karnıyarık otu" diyor. Ticarette '
                    'psyllium ve ispagula adlarıyla satılıyor.',
            karisma='Türkçede "karnıyarık" ve "sinirotu" adları Plantago cinsinin '
                    'birçok türü için kullanılıyor; en çok karıştığı türler '
                    'Plantago major ve Plantago lanceolata. Bunların kullanılan '
                    'kısmı yaprak, oysa bu kayıttaki tür için kullanılan kısım '
                    'tohum ve tohum kabuğu — kullanımları da farklı. Ürün '
                    'kutusundaki Latince ad belirleyici.',
        ),
        ema=[('Plantaginis ovatae semen',
              'https://www.ema.europa.eu/en/medicines/herbal/plantaginis-ovatae-semen'),
             ('Plantaginis ovatae seminis tegumentum',
              'https://www.ema.europa.eu/en/medicines/herbal/plantaginis-ovatae-seminis-tegumentum')],
        kaynak=[
            ['Elena Jovanovski ve ark., “Effect of psyllium (Plantago ovata) fiber '
             'on LDL cholesterol and alternative lipid targets, non-HDL cholesterol '
             'and apolipoprotein B: a systematic review and meta-analysis of '
             'randomized controlled trials”, The American Journal of Clinical '
             'Nutrition 108(5): 922–932, 2018',
             'https://pubmed.ncbi.nlm.nih.gov/30239559/'],
            ['Jing Yang ve ark., “Effect of dietary fiber on constipation: a meta '
             'analysis”, World Journal of Gastroenterology 18(48): 7378–7383, 2012',
             'https://pubmed.ncbi.nlm.nih.gov/23326148/'],
            ['Plantago ovata Forssk. monografı, TİTCK Tıbbi Bitki Listesi',
             'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/PlantagoovataForssk..pdf13db3a84bb1f466ab06f79db489eca8e_d021c0b3-2cbe-46b2-8738-8295f105ee52.pdf'],
        ],
        rel=['sinameki', 'keten'],
        en=dict(
            name='Ispaghula',
            other='The Turkish regulatory monograph gives the Turkish name as '
                  '"sarı karnıyarık otu" and the English as "ispaghula husk", with '
                  'Plantago brunnea, P. fastigiata and P. insularis as synonyms. '
                  'Sold commercially as psyllium. Note that the Turkish name '
                  'karnıyarık is also used for Plantago major and P. lanceolata; '
                  'this record covers P. ovata only.',
            part='The seed and the seed husk',
            uses=[
                ['India and Iran — a fibre crop', 'The seed husk forms a gel many '
                 'times its own volume on contact with water, and the traditional '
                 'use follows from that physical property. Most of the world crop '
                 'comes from Gujarat in India.'],
                ['Europe — an approved use in constipation', 'The European '
                 'Medicines Agency has separate monographs for the seed and the '
                 'husk, and in both the indication for habitual constipation sits '
                 'under "well-established use". Alongside constipation, the '
                 'monographs also list conditions in which a softened stool is '
                 'medically necessary.'],
                ['Turkey — official list', 'The Turkish monograph gives the part '
                 'used as "the seeds and seed husks (testa epidermis)" and lists '
                 'its warnings, citing the 2013 EMA monograph.'],
            ],
            prep='The Turkish monograph stresses two points: it must be taken with '
                 'enough fluid (water, milk, fruit juice or similar), and the effect '
                 'begins after 12–24 hours. The fluid requirement is not a '
                 'formality: because the husk works by forming a gel in the gut, '
                 'taking it with too little fluid can cause obstruction. It should '
                 'not be taken at the same time as other medicines — leave at least '
                 'an hour between them. If symptoms persist for three days, consult '
                 'a doctor.',
            science='Psyllium fibre has some of the firmest randomised evidence of '
                    'any herbal product. A meta-analysis of 28 randomised trials '
                    '(1,924 participants) found that a median dose of 10.2 g of '
                    'psyllium a day lowered LDL cholesterol by 0.33 mmol/L (95% CI '
                    '0.27–0.38), non-HDL cholesterol by 0.39 mmol/L and '
                    'apolipoprotein B by 0.05 g/L. Under GRADE the evidence was '
                    'rated moderate quality for LDL and non-HDL cholesterol '
                    '(downgraded for inconsistency) and high quality for apoB. The '
                    'constipation side is weaker: a meta-analysis of five '
                    'randomised trials found that fibre significantly increased '
                    'stool frequency against placebo, but found no significant '
                    'difference in stool consistency, treatment success, laxative '
                    'use or painful defecation. A separate randomised trial '
                    'compared P. ovata seed with mesalamine for maintaining '
                    'remission in ulcerative colitis. In short: the lipid effect is '
                    'well documented and of measured size, while the constipation '
                    'effect has been shown on one narrow endpoint.',
            safety='Not for anyone with difficulty swallowing or throat problems. '
                   'Not to be used in intestinal obstruction (ileus), intestinal '
                   'paralysis, megacolon, problems of the gastrointestinal tract or '
                   'oesophagus, or heart disease. The Turkish monograph states that '
                   'people with diabetes or thyroid disease should not use it. It '
                   'must be taken with enough fluid; too little fluid creates a '
                   'risk of obstruction. Use is not recommended in pregnancy or '
                   'lactation, nor in children under 12, for lack of data. '
                   'Hypersensitivity to the active substance can occur.',
            fact='The effect is physical rather than chemical: psyllium husk is a '
                 'non-fermented, gel-forming fibre. Both the cholesterol lowering '
                 'and the effect in constipation come from the same mechanism — '
                 'binding bile acids and holding them in a gel. The same mechanism '
                 'explains why taking it with too little fluid creates a risk of '
                 'obstruction.',
            season='An annual; flowers in spring, seeds ripen in early summer.',
            habitat='Native to the Mediterranean basin and western Asia; grows on '
                    'dry, sandy soils. Commercial production is concentrated in '
                    'north-western India and Iran.',
            local='The Turkish monograph gives "sarı karnıyarık otu". Sold as '
                  'psyllium or ispaghula.',
            confusion='In Turkish, karnıyarık and sinirotu are used for several '
                      'Plantago species, most often P. major and P. lanceolata. For '
                      'those the part used is the leaf, whereas here it is the seed '
                      'and husk, and the uses differ. The Latin name on the package '
                      'is what settles it.',
        ),
        etk_en=[
            ['All medicines — delayed absorption',
             'The Turkish monograph asks anyone taking other medicines to leave at '
             'least an hour between them and the herbal product. The reason is '
             'physical: the gel that forms in the gut can delay and reduce the '
             'absorption of a medicine taken alongside it. This is not an '
             'interaction specific to particular drugs but a general consequence of '
             'the fibre itself.'],
            ['Vitamin B12, minerals, cardiac glycosides, coumarin derivatives, '
             'carbamazepine, lithium',
             'The Turkish monograph names these groups: minerals and vitamins '
             'absorbed from the gut (B12), cardiac glycosides, coumarin '
             'anticoagulants, carbamazepine and lithium. For all of them the effect '
             'depends on blood levels staying within a narrow range, which is why a '
             'change in absorption matters.'],
            ['Medicines that slow gut motility (opioids)',
             'The Turkish monograph says it should not be used together with '
             'medicines that inhibit peristalsis. A gel-forming fibre may fail to '
             'move on when motility is suppressed, and can cause obstruction.'],
        ],
    ),

    dict(
        yayin='2026-12-19',
        id='asmayapragi',
        foto='2014 11 09 022 Blaetter.jpg',
        tr='Asma yaprağı',
        la='Vitis vinifera L.',
        fam='Vitaceae (asmagiller)',
        diger='Bitkinin Türkçe adı asma ya da üzüm; bu kayıt yaprağı konu alıyor, '
              'çünkü monografa giren kısım yaprak. Ticarette "kırmızı asma yaprağı" '
              '(red vine leaf) deniyor: sonbaharda kızaran yapraklar kullanılıyor.',
        bolge=['anadolu', 'avrupa'],
        kat=['sifa', 'besin'],
        kisim='Yaprak',
        taxon='Vitis vinifera',
        kul=[
            ['Anadolu — yemeklik', 'Asma yaprağı Anadolu mutfağının temel '
             'malzemelerinden: yaprak sarma, salamura yaprak. Bu kullanım besin '
             'kullanımıdır ve aşağıda anlatılan tıbbi kullanımla aynı şey değil — '
             'tıbbi etki için kullanılan şey sonbaharda kızarmış yapraktan '
             'hazırlanan standart ekstre.'],
            ['Avrupa — bacak dolaşımı', 'Avrupa İlaç Ajansı monografı yaprağı iki '
             'kategoride birden ele alıyor. "İyi bilinen kullanım" başlığı altında '
             'endikasyon kronik venöz yetmezlik: bacaklarda şişme, ağırlık ve ağrı '
             'belirtileri. "Geleneksel kullanım" başlığı altında ayrıca hemoroide '
             'bağlı kaşıntı ve yanma ile deri kılcal damar kırılganlığı var. '
             'Sitedeki 68 bitlik partide monografı iki kategoriyi birlikte '
             'kullanan tek tür bu.'],
            ['Türkiye — resmî liste', 'TİTCK monografı kullanılan kısmı "yapraklar" '
             'diye veriyor, drogun Fransız Farmakopesi X monografına uygun olması '
             'gerektiğini yazıyor ve kullanım sürelerini endikasyon endikasyon '
             'ayırıyor: bacaklardaki rahatsızlık ve ağırlık için önerilen süre dört '
             'hafta, hemoroid ve kılcal damar kırılganlığı için bir hafta.'],
        ],
        haz='Tıbbi kullanım için evde hazırlanan bir biçim yok: çalışmalar da, '
            'monograflar da sonbahar yapraklarından elde edilen standart kuru '
            'ekstreyi konu alıyor (literatürde AS 195 kodlu ekstre). Yemeklik '
            'kullanım bambaşka: taze ya da salamura yaprak, dolma harcıyla '
            'sarılarak pişiriliyor. TİTCK monografı tıbbi kullanım için süre '
            'sınırları koyuyor — dört hafta sonunda ya da belirtiler iki haftadan '
            'uzun sürdüğünde hekime ya da eczacıya başvurulmalı.',
        bilim='Kırmızı asma yaprağı ekstresi, bacak venlerinin yetmezliğinde '
              'ölçülebilir ama küçük bir etki gösteriyor. 2011’de yayımlanan '
              'randomize, plasebo kontrollü bir çalışmada 248 hastanın 12 haftalık '
              'izleminde ekstre, bacak hacmini plaseboya göre ortalama 19,9 mililitre '
              'azaltıyor (%95 güven aralığı 2,3–37,5 ml; standartlaştırılmış etki '
              'büyüklüğü 0,28). Görsel analog ölçekte "bacaklarda ağrı" belirtisi de '
              'plasebodan farklı çıkıyor, ama diğer belirtilerde anlamlı değişiklik '
              'yok. Çalışmanın kendi dikkat çektiği nokta önemli: hastaların '
              'etkinliğe dair genel değerlendirmesi, ölçülen hacim azalmasıyla iyi '
              'örtüşmüyor. 2020’de beş çalışmayı toplayan sistematik derleme de aynı '
              'yöne işaret ediyor: ekstre bacak hacmi, baldır ve ayak bileği çevresi, '
              'yorgun ve ağır bacaklar, karıncalanma ve ağrı gibi son noktaları '
              '"yalnızca bazı çalışmalarda" anlamlı biçimde iyileştiriyor; '
              'tolere edilebilirlik iyi. Derleme, güçlü kanıt için daha yüksek '
              'kaliteli çalışmalara ihtiyaç olduğunu yazıyor. Bu yüzden kanıt düzeyi '
              '"klinik" değil "sınırlı": etki plasebo kontrollü ortamda ölçülmüş, '
              'ama küçük ve tutarsız.',
        kanit='sinirli',
        guv='orta',
        guvNot='Etkin maddeye aşırı duyarlılık gösterenler kullanmamalı. TİTCK '
               'monografı, tıbbi kullanım sırasında hekime başvurulmasını gerektiren '
               'durumları ayrıca sayıyor: ciltte iltihap, tromboflebit ya da deri '
               'altı sertleşme, şiddetli ağrı, ülser, bir veya iki bacakta ani '
               'şişme, kalp ya da böbrek yetmezliği. Bunlar kronik venöz yetmezliğin '
               'kendi başına bitkisel ürünle geçiştirilmemesi gereken belirtileri: '
               'ani bacak şişmesi damar tıkanıklığının işareti olabilir. Deri üzerine '
               'uygulanan biçimlerde hasarlı cilt, göz çevresi ve mukoza üzerine '
               'uygulanmamalı. Kullanım süreleri monografta endikasyona göre '
               'sınırlı: bacak belirtileri için dört hafta, hemoroid ve kılcal '
               'damar kırılganlığı için bir hafta. Yemeklik yaprak kullanımı bu '
               'uyarıların konusu değildir.',
        etk=[
            ['Avrupa İlaç Ajansı monografında bildirilmiş etkileşim yok',
             'Monografın etkileşim bölümü bildirilmiş bir etkileşim olmadığını '
             'yazıyor; TİTCK monografı da ilaç etkileşimi bölümünde bir şey '
             'saymıyor. Bu, etkileşim olmadığının kanıtı değil, araştırılmadığının '
             'ifadesidir.'],
            ['Kan sulandırıcı kullananlar için not',
             'Kronik venöz yetmezlik ve bacak şişmesi tablosu, kan sulandırıcı '
             'kullanmayı gerektiren damar hastalıklarıyla örtüşebiliyor. Doğrulanmış '
             'bir etkileşim çalışması olmasa da, bu ilaçları kullananların bitkisel '
             'ürünü hekimine söylemesi gerekir — çünkü asıl risk etkileşim değil, '
             'tanı gerektiren bir belirtinin bitkisel ürünle örtülmesidir.'],
        ],
        ilginc='Aynı bitkinin aynı kısmı, iki ayrı kullanım kategorisinde: Anadolu '
               'mutfağında yaprak sarmanın malzemesi, Avrupa eczanesinde bacak '
               'dolaşımı için standart ekstre. Tıbbi olan sonbaharda kızaran yaprak '
               '— kırmızı rengi veren antosiyaninler ekstrenin tanımına giriyor. '
               'Yani dolma yaprağı ile ilaç yaprağı aynı ağaçtan, ama aynı mevsimden '
               'değil.',
        ek=dict(
            mevsim='Yemeklik yaprak mayıs–haziranda, bitki körpeyken toplanıyor. '
                   'Tıbbi ekstreye giren yaprak ise sonbaharda, kızardıktan sonra '
                   'hasat ediliyor.',
            yetisme='Kökeni Güney Kafkasya ve Anadolu; Türkiye dünyanın en eski ve '
                    'en çeşitli asma gen kaynaklarından birine sahip. Ülkenin hemen '
                    'her bölgesinde yetişiyor.',
            yoresel='Bitkinin adı asma ya da üzüm; yaprağı için "asma yaprağı", '
                    'salamurası için "yaprak" deniyor. Ticari tıbbi ürünlerde '
                    '"kırmızı asma yaprağı" adı geçiyor.',
            karisma='Yemeklik ve tıbbi kullanımın karışması asıl risk: eczanedeki '
                    'ekstrenin dozu ile mutfaktaki yaprağın miktarı birbirinin '
                    'yerine geçmez, ve sarma yemek bacak şişmesine bir etki '
                    'göstermez. Yaban asması (Vitis sylvestris) ile de '
                    'karıştırılmamalı.',
        ),
        ema=[('Vitis viniferae folium',
              'https://www.ema.europa.eu/en/medicines/herbal/vitis-viniferae-folium')],
        kaynak=[
            ['Eberhard Rabe ve ark., “Efficacy and tolerability of a red-vine-leaf '
             'extract in patients suffering from chronic venous insufficiency — '
             'results of a double-blind placebo-controlled study”, European Journal '
             'of Vascular and Endovascular Surgery 41(4): 540–547, 2011',
             'https://pubmed.ncbi.nlm.nih.gov/21239190/'],
            ['Maryam Azhdari ve ark., “Red vine leaf extract (AS 195) can improve '
             'some signs and symptoms of chronic venous insufficiency, a systematic '
             'review”, Phytotherapy Research 34(10): 2577–2585, 2020',
             'https://pubmed.ncbi.nlm.nih.gov/32314844/'],
            ['Vitis vinifera L. monografı, TİTCK Tıbbi Bitki Listesi',
             'https://titck.gov.tr/storage/Archive/2026/dynamicModulesAttachment/VitisviniferaL.v1_f066e76f-99ff-46ca-8e28-91b751022bac.pdf'],
        ],
        rel=['incir', 'alic'],
        en=dict(
            name='Grapevine leaf',
            other='The plant is the grapevine; this record covers the leaf, because '
                  'the leaf is the part in the monograph. It is sold medicinally as '
                  '"red vine leaf": the leaves used are those that have turned red '
                  'in autumn.',
            part='The leaf',
            uses=[
                ['Anatolia — in cooking', 'Vine leaves are a staple of Anatolian '
                 'cooking, fresh or brined, wrapped around a rice filling. That is '
                 'a food use and not the same thing as the medicinal use below, '
                 'which involves a standardised extract of autumn-reddened leaves.'],
                ['Europe — leg circulation', 'The EMA monograph covers the leaf '
                 'under two categories at once. Under "well-established use" the '
                 'indication is chronic venous insufficiency: swelling, heaviness '
                 'and pain in the legs. Under "traditional use" it also lists '
                 'itching and burning from haemorrhoids, and cutaneous capillary '
                 'fragility. Of the 68 plants in this batch, this is the only one '
                 'whose monograph uses both categories together.'],
                ['Turkey — official list', 'The Turkish monograph gives the part '
                 'used as "leaves", requires the herbal substance to comply with '
                 'the French Pharmacopoeia X monograph, and sets separate durations '
                 'of use per indication: four weeks for discomfort and heaviness in '
                 'the legs, one week for haemorrhoids and capillary fragility.'],
            ],
            prep='There is no home preparation for the medicinal use: both the '
                 'trials and the monographs concern a standardised dry extract of '
                 'autumn leaves (coded AS 195 in the literature). The culinary use '
                 'is something else entirely: fresh or brined leaves wrapped around '
                 'a filling and cooked. The Turkish monograph sets limits on the '
                 'medicinal use — consult a doctor or pharmacist after four weeks, '
                 'or if symptoms last longer than two weeks.',
            science='Red vine leaf extract shows a measurable but small effect in '
                    'venous insufficiency of the legs. In a randomised, '
                    'placebo-controlled trial published in 2011, 248 patients '
                    'followed for 12 weeks, the extract reduced lower limb volume '
                    'by a mean of 19.9 ml against placebo (95% CI 2.3–37.5 ml; '
                    'standardised effect size 0.28). Leg pain on a visual analogue '
                    'scale also differed from placebo, but other symptoms showed no '
                    'significant change. The trial itself flags something important: '
                    'patients’ overall rating of efficacy did not correlate '
                    'well with the measured reduction in limb volume. A 2020 '
                    'systematic review of five trials points the same way: the '
                    'extract significantly improved endpoints such as limb volume, '
                    'calf and ankle circumference, tired and heavy legs, tingling '
                    'and pain in only some of the trials, with good tolerability. '
                    'The review concludes that higher-quality trials are needed for '
                    'strong evidence. The evidence level here is therefore Limited '
                    'rather than Clinical: the effect has been measured against '
                    'placebo, but it is small and inconsistent.',
            safety='Not for anyone hypersensitive to the active substance. The '
                   'Turkish monograph separately lists the situations that require '
                   'medical advice during use: inflammation of the skin, '
                   'thrombophlebitis or subcutaneous induration, severe pain, '
                   'ulceration, sudden swelling of one or both legs, and cardiac or '
                   'renal failure. These are the signs that chronic venous '
                   'insufficiency should not be managed with a herbal product '
                   'alone: sudden swelling of a leg can indicate a clot. '
                   'Preparations applied to the skin must not be used on damaged '
                   'skin, around the eyes or on mucous membranes. Durations of use '
                   'are limited by indication: four weeks for leg symptoms, one '
                   'week for haemorrhoids and capillary fragility. The culinary use '
                   'of vine leaves is not the subject of these warnings.',
            fact='The same part of the same plant in two different categories of '
                 'use: the wrapper for stuffed vine leaves in an Anatolian kitchen, '
                 'and a standardised extract for leg circulation in a European '
                 'pharmacy. The medicinal leaf is the one that reddens in autumn — '
                 'the anthocyanins that give it that colour are part of the '
                 'definition of the extract. The leaf for cooking and the leaf for '
                 'medicine come from the same vine, but not from the same season.',
            season='Leaves for cooking are picked in May and June while still '
                   'tender. Leaves for the medicinal extract are harvested in '
                   'autumn, after they have reddened.',
            habitat='Originating in the South Caucasus and Anatolia; Turkey holds '
                    'one of the oldest and most diverse grapevine gene pools in the '
                    'world. Grown in almost every region of the country.',
            local='The plant is asma or üzüm in Turkish; the leaf is "asma '
                  'yaprağı", and brined leaves are simply "yaprak". Commercial '
                  'medicinal products use the name red vine leaf.',
            confusion='The real risk is confusing the culinary and medicinal uses: '
                      'the dose of a pharmacy extract and the quantity of leaves in '
                      'a kitchen are not interchangeable, and eating stuffed vine '
                      'leaves has no effect on leg swelling. Not to be confused with '
                      'wild grapevine (Vitis sylvestris) either.',
        ),
        etk_en=[
            ['No interactions reported in the EMA monograph',
             'The interaction section of the monograph reports none, and the Turkish '
             'monograph lists nothing under drug interactions either. That is a '
             'statement about what has been studied, not evidence that no '
             'interaction exists.'],
            ['A note for people on anticoagulants',
             'Chronic venous insufficiency and leg swelling overlap with vascular '
             'conditions that call for anticoagulant treatment. Although no '
             'interaction study confirms a problem, anyone on these medicines should '
             'tell their doctor about the herbal product — the real risk is not an '
             'interaction but a symptom that needs diagnosis being masked by a '
             'herbal product.'],
        ],
    ),

]
