# -*- coding: utf-8 -*-
# Kuyruk 7: Göbekli Tepe dörtlüsü — badem, antep fıstığı, mercimek, arpa (13–16 Aralık 2026)
# Not: Neef 2003'teki kalıntılar YABANİ akrabalardır. "Evcil X bulundu" denmez.
# Antep fıstığı için Göbekli Tepe bağlantısı YOKTUR: oradaki Pistacia, cf. atlantica (menengiç).
P = 'https://pubmed.ncbi.nlm.nih.gov/'
D = 'https://doi.org/'
NEEF = ('Reinder Neef, “Overlooking the Steppe-Forest: A Preliminary Report on the Botanical '
        'Remains from Early Neolithic Göbekli Tepe (Southeastern Turkey)”, Neo-Lithics 2/03: 13–16, 2003',
        'https://www.exoriente.org/docs/00046.pdf')
AKSU = ('Hatice Aksu, İlhan Kaya Tekbudak, M. Alp Furan, Gülistan Genli, “Şırnak (İdil) Yöresinde '
        'Halk Hekimliğinde Kullanılan Bitkiler ve Kullanım Alanları”, Doğu Fen Bilimleri Dergisi 7(2): 92–106, 2024',
        'https://dergipark.org.tr/tr/pub/dfbd/article/1455612')
EKSIK = ('Cebrail Eksik, Hasan Akan, “Mardin’in Kırsal Köylerindeki Yerli Halkın Kullandıkları Bazı '
         'Bitkilerin Etnobotanik Açıdan Değerlendirilmesi”, Bağbahçe Bilim Dergisi 8(3): 97–130, 2021',
         'https://dergipark.org.tr/tr/pub/bagbahce/article/937816')
YALCIN = ('Serhan Yalçın, Hasan Akan, Uğur Çakılcıoğlu, “Suruç’ta (Şanlıurfa-Türkiye) Bazı Şifalı '
          'Bitkilerin Geleneksel Kullanımları”, Türk Doğa ve Fen Dergisi 10(1): 236–244, 2021',
          'https://dergipark.org.tr/tr/pub/tdfd/article/880363')
AB432 = ('Regulation (EU) No 432/2012, izin verilen sağlık beyanları listesi (Ek)',
         'https://www.legislation.gov.uk/eur/2012/432/annex')

Q = [

# ---------------------------------------------------------------- 13 Aralık: BADEM
{'yayin': '2026-12-13',
 'id': 'badem',
 'foto': 'Prunus amygdalus 2601.jpg',
 'tr': 'Badem',
 'la': 'Prunus dulcis (Mill.) D.A.Webb',
 'fam': 'Rosaceae (gülgiller)',
 'diger': 'Amygdalus communis L. ve Prunus amygdalus Batsch adlarıyla da yazılır; Türk etnobotanik '
          'literatüründe çoğunlukla Amygdalus communis geçer. Kürtçe behiv, bıiv, beivf; Mardin’de payam.',
 'bolge': ['anadolu'],
 'kat': ['sifa', 'besin'],
 'kisim': 'Çekirdek (tohum içi); yaprak ve reçine yerel olarak',
 'taxon': 'Prunus dulcis',
 'kul': [('Göbekli Tepe',
          'Göbekli Tepe’nin III. tabakasında, 1950 litre toprağın yüzdürülmesiyle elde edilen kalıntılar '
          'arasında Prunus cinsine ait kabuk parçaları var: 158 parça, tahminen 13,5 bütün meyveye karşılık '
          'geliyor. Odun kömürünün bir bölümü de Prunus cf. amygdalus olarak tanımlanmış. Yani bulunan, '
          'evcil badem değil yabani akrabası; kazının arkeobotanikçisi Reinder Neef bütün malzemede '
          'evcilleşmeye dair hiçbir kanıt bulunmadığını yazıyor. Odun kömürünün yaklaşık onda dokuzu '
          'yabani fıstık ve yabani bademden oluşuyor; bu da tepeyi çevreleyen bitki örtüsünün '
          '“bademli-fıstıklı step-ormanı” olduğunu gösteriyor.'),
         ('Şanlıurfa — Suruç',
          'Göbekli Tepe ile aynı ilde, Suruç köylerinde badem meyvesi şeker hastalığı için yeniyor; '
          'yerel adı “beivf”.'),
         ('Şırnak — İdil',
          'Taze badem meyvesi ağız yaralarına, egzamaya ve saçı gürleştirmek için kullanılıyor; '
          'yerel adları “badem” ve “behiv”.'),
         ('Mardin — tıbbi olmayan kullanım',
          'Badem ve doğu bademinin (Amygdalus orientalis) gövdesinden sızan reçine yapıştırıcı olarak '
          'kullanılıyor: kopan kitap sayfaları bununla birbirine tutturuluyor. Gövde yakacak olarak da değerli.')],
 'haz': 'Resmî bir hazırlama şekli yoktur: ne Avrupa İlaç Ajansı’nın monografı ne de NCCIH sayfası vardır. '
        'Klinik çalışmalarda kullanılan biçim, günde 30–60 gram civarında çiğ ya da kavrulmuş tatlı bademdir; '
        'bu bir ilaç dozu değil, besin miktarıdır.',
 'bilim': 'Badem, kardiyometabolik son noktalarda randomize kontrollü çalışmaların en çok yapıldığı '
          'kuruyemişlerden biri. Randomize çalışmaların meta-analizleri bademin LDL kolesterolü ve toplam '
          'kolesterolü düşürdüğünü, trigliseritleri çok az etkilediğini, HDL’yi değiştirmediğini gösteriyor. '
          'İnsanda yapılan çalışmalar ayrıca öğün öncesi bademin prediyabetli kişilerde öğün sonrası kan '
          'şekerini düşürdüğünü, bademin bağırsak hareketleri ve mikrobiyota üzerinde ölçülebilir etkisi '
          'olduğunu bildiriyor. Bütün bu kanıt “besin olarak” kanıttır: bademin onaylanmış bir tıbbi '
          'endikasyonu yoktur.',
 'kanit': 'klinik',
 'guv': 'orta',
 'guvNot': 'Badem bir ağaç kuruyemişidir ve ağaç kuruyemişi alerjisi ağır, hayatı tehdit eden tepkilere yol '
           'açabilir. Bademin ana allerjeni amandin (prunin); Pru du 6 proteini badem alerjisinin belirteci '
           'olarak kullanılıyor. Gülgiller familyasındaki diğer meyvelerle çapraz tepkime bildirilmiştir. '
           'ACI BADEM ayrı bir konudur: yabani badem türleri amigdalin adlı siyanojenik bileşiği biriktirir '
           've bu bileşik vücutta siyanüre dönüşür. Acı badem yedikten sonra ağır laktik asidozla seyreden '
           'siyanür zehirlenmesi vakası yayımlanmıştır. Acı badem ve amigdalin (laetril) gıda ya da ilaç '
           'olarak kullanılmamalıdır. Tatlı badem için ilaç etkileşimi ve hamilelik-emzirme konusunda '
           'doğrulanmış veri yoktur.',
 'ilginc': 'Bugün yediğimiz tatlı badem, tek bir gen arızasının ürünü: yabani badem türleri acı ve zehirli '
           'amigdalin biriktirir, ama bir bHLH transkripsiyon faktörü genindeki mutasyon çekirdeği '
           'tatlılaştırmış ve bademin evcilleştirilmesini mümkün kılmıştır.',
 'ek': {'mevsim': 'Şubat–mart arasında, yapraklardan önce çiçek açar; Anadolu’da baharın ilk çiçeklenen '
                  'ağaçlarından biridir. Meyveler ağustos–eylülde olgunlaşır; taze “çağla” olarak mayıs–haziranda yenir.',
        'yetisme': 'Ön Asya kökenli; Türkiye’nin hemen her bölgesinde yetişir, Ege, Akdeniz ve Güneydoğu’da '
                   'yoğunlaşır. Kurağa dayanıklı, geç donlara duyarlıdır.',
        'yoresel': 'Behiv, bıiv, beivf, payam',
        'karisma': 'Acı badem ile tatlı badem aynı türün iki biçimidir ve dıştan ayırt edilemez; fark tada '
                   've amigdalin içeriğine dayanır. Doğu bademi (Amygdalus orientalis) ve yabani badem '
                   'türleri Anadolu’da doğal olarak bulunur ve halk arasında aynı adla anılabilir. '
                   'Göbekli Tepe kalıntıları “Prunus sp.” ve “Prunus cf. amygdalus” olarak kayıtlıdır: '
                   'yabani, tür düzeyinde kesinleşmemiş.'},
 'etk': [('Bilinen bir ilaç etkileşimi yok',
          'Tatlı badem için doğrulanmış bir ilaç etkileşimi çalışması bulunmuyor. Besin olarak tüketilen '
          'miktarlarda bir kaygı bildirilmemiştir. Acı badem ve amigdalin içeren ürünler için durum farklıdır: '
          'bunlar siyanür zehirlenmesi riski taşıdığı için hiçbir ilaçla birlikte ya da tek başına kullanılmamalıdır.')],
 'etk_en': [('No known drug interaction',
             'No verified interaction study exists for sweet almond, and none has been reported at food '
             'amounts. Bitter almond and amygdalin (laetrile) products are a different matter: they carry a '
             'risk of cyanide poisoning and should not be taken at all.')],
 'kaynak': [NEEF,
            YALCIN,
            AKSU,
            EKSIK,
            ('Mohammadifard N ve ark., “The effect of tree nut, peanut, and soy nut consumption on blood '
             'pressure” / badem ve kardiyovasküler risk etmenleri üzerine randomize çalışmaların '
             'meta-analizi, Advances in Nutrition, 2019 (PMID 31243439)', P + '31243439/'),
            ('Eslampour E ve ark., “The effect of almond intake on lipid profile: a systematic review and '
             'meta-analysis of randomized controlled trials”, Food & Function, 2021 (PMID 33586744)', P + '33586744/'),
            ('Creedon AC ve ark., “The impact of almonds and almond processing on gastrointestinal '
             'physiology, luminal microbiology, and gastrointestinal symptoms”, American Journal of '
             'Clinical Nutrition, 2022 (PMID 36130222)', P + '36130222/'),
            ('Crosby L ve ark., “Almonds as a preload: postprandial glycaemia in prediabetes”, Clinical '
             'Nutrition ESPEN, 2023 (PMID 36963852)', P + '36963852/'),
            ('Sánchez-Pérez R ve ark., “Mutation of a bHLH transcription factor allowed almond '
             'domestication”, Science 364(6445): 1095–1098, 2019 (PMID 31197015)', P + '31197015/'),
            ('Dubois AEJ ve ark., “Pru du 6 as a marker allergen for almond allergy”, Allergy, 2021 '
             '(PMID 33020913)', P + '33020913/'),
            ('Bolarinwa IF ve ark., “Amygdalin: toxicity and determination in plant seeds”, Molecules, '
             '2021 (PMID 33924691)', P + '33924691/'),
            ('Seghizzi P ve ark., “Cyanide poisoning with severe lactic acidosis after bitter almond '
             'ingestion”, Intensive Care Medicine, 2011 (PMID 20845029)', P + '20845029/'),
            ('Geiser F ve ark., “Tree nut allergy: a review”, Postępy Dermatologii i Alergologii, 2021 '
             '(PMID 34658691)', P + '34658691/')],
 'rel': ['mese', 'alic', 'arpa', 'mercimek'],
 'en': {'name': 'Almond',
        'other': 'Also written Amygdalus communis L. or Prunus amygdalus Batsch; Kurdish behiv, bıiv, beivf',
        'part': 'The kernel; leaf and resin in local use',
        'uses': [('Göbekli Tepe',
                  'Layer III at Göbekli Tepe yielded shell fragments of the genus Prunus — 158 pieces, an '
                  'estimated 13.5 whole fruits — and part of the charcoal was identified as Prunus cf. '
                  'amygdalus. What was found is not the domesticated almond but its wild relative: the '
                  'excavation’s archaeobotanist, Reinder Neef, writes that there is no evidence for '
                  'domestication anywhere in the material. About nine tenths of the charcoal is wild '
                  'pistachio and wild almond, which points to an almond-pistachio steppe-forest around the site.'),
                 ('Şanlıurfa — Suruç',
                  'In the same province as Göbekli Tepe, villagers in Suruç eat almond fruit for diabetes; '
                  'the local name is “beivf”.'),
                 ('Şırnak — İdil',
                  'Fresh almond fruit is used for mouth sores, eczema and to thicken hair, under the names '
                  '“badem” and “behiv”.'),
                 ('Mardin — a non-medicinal use',
                  'Resin that seeps from the trunk of almond and eastern almond is used as glue: loose book '
                  'pages are stuck back together with it. The wood is valued as fuel.')],
        'prep': 'There is no official preparation: neither a European Medicines Agency monograph nor an '
                'NCCIH page exists. Clinical trials use roughly 30–60 g a day of raw or roasted sweet '
                'almonds — a food amount, not a drug dose.',
        'science': 'Almond is among the most trialled nuts for cardiometabolic endpoints. Meta-analyses of '
                   'randomised trials find that almonds lower LDL and total cholesterol, barely affect '
                   'triglycerides and leave HDL unchanged. Human trials also report that almonds eaten '
                   'before a meal lower post-meal blood glucose in prediabetes, and that they measurably '
                   'affect gut transit and the gut microbiota. All of this is evidence for almonds as a '
                   'food; there is no approved medical indication.',
        'safety': 'Almond is a tree nut and tree-nut allergy can cause severe, life-threatening reactions. '
                  'Its main allergen is amandin (prunin); the Pru du 6 protein is used as a marker for '
                  'almond allergy, and cross-reactivity with other Rosaceae fruits is on record. BITTER '
                  'ALMOND is a separate matter: wild almond species accumulate the cyanogenic compound '
                  'amygdalin, which the body converts to cyanide. A case of cyanide poisoning with severe '
                  'lactic acidosis after eating bitter almonds has been published. Bitter almond and '
                  'amygdalin (laetrile) should not be used as food or medicine. For sweet almond there is '
                  'no verified data on drug interactions or on pregnancy and breastfeeding.',
        'fact': 'The sweet almond we eat today is the product of a single broken gene: wild almond species '
                'accumulate the bitter, toxic compound amygdalin, and a mutation in one bHLH transcription '
                'factor made the kernel sweet — and almond domestication possible.',
        'season': 'Flowers in February and March, before the leaves — one of the first trees to bloom in '
                  'Anatolia. Fruit ripens in August and September; eaten green as “çağla” in May and June.',
        'habitat': 'Native to western Asia; grown across Turkey, concentrated in the Aegean, Mediterranean '
                   'and southeast. Drought-hardy but sensitive to late frost.',
        'local': 'Behiv, bıiv, beivf, payam',
        'confusion': 'Bitter and sweet almond are two forms of the same species and cannot be told apart by '
                     'eye; the difference is taste and amygdalin content. Eastern almond (Amygdalus '
                     'orientalis) and wild almond species grow naturally in Anatolia and may share the same '
                     'local name. The Göbekli Tepe remains are recorded as “Prunus sp.” and “Prunus cf. '
                     'amygdalus”: wild, and not settled at species level.'}},

# ---------------------------------------------------------------- 14 Aralık: ANTEP FISTIĞI
{'yayin': '2026-12-14',
 'id': 'antepfistigi',
 'foto': 'Ağaçta Fıstık.jpg',
 'tr': 'Antep fıstığı',
 'la': 'Pistacia vera L.',
 'fam': 'Anacardiaceae (sakızağacıgiller)',
 'diger': 'Şam fıstığı; İng. pistachio. Yazar kısaltması “L.” olmalıdır: Pistacia vera Mill. geçersiz bir addır.',
 'bolge': ['anadolu'],
 'kat': ['besin', 'sifa'],
 'kisim': 'Çekirdek (tohum içi)',
 'taxon': 'Pistacia vera',
 'kul': [('Bereketli Hilal’de evcilleştirme',
          'Antep fıstığı Bereketli Hilal’de evcilleştirilmiş bir kuruyemiş ağacıdır. Türkiye’de Gaziantep, '
          'Şanlıurfa ve Siirt çevresi üretimin merkezidir; türün ilk referans genomu da Siirt çeşidinin '
          'dişi bir bireyinden dizilenmiştir.'),
         ('Anadolu halk hekimliğinde yabani akrabalar',
          'Anadolu etnobotanik kayıtlarında halk hekimliği kullanımı belgelenen Pistacia türleri yabani '
          'olanlardır, antep fıstığının kendisi değil. Şırnak’ta Pistacia eurycarpa (“bendek”, “kızvan”, '
          '“bıttım”) dal ve meyvesi kaynatılarak kabızlık, hemoroit, mide ağrısı ve mide yarasına karşı '
          'kullanılıyor. Mardin’de Pistacia khinjuk (“bıttım”, “kızvan”) meyvesinden bıttım sabunu yapılıyor. '
          'Pistacia terebinthus ise menengiç adıyla bilinir ve meyvesiyle reçinesi kullanılır. '
          'Antep fıstığının (Pistacia vera) kendisi için Anadolu halk hekimliği kaydı bulunamadı; '
          'kültürel ağırlığı mutfakta ve ticarettedir.'),
         ('Göbekli Tepe’de bulunmamıştır',
          'Göbekli Tepe’nin III. tabakasında Pistacia cinsine ait meyve kalıntıları (124 parça, tahminen '
          '17 bütün) ve odun kömürünün en büyük payı (3,14 g, 104 tanımlama) bulunmuştur. Ancak odun kömürü '
          'Pistacia cf. atlantica olarak tanımlanmıştır: bu, antep fıstığı değil yabani bir Pistacia, yani '
          'menengiç/buttum türüdür. “Göbekli Tepe’de antep fıstığı bulundu” cümlesi kaynakla desteklenmez.')],
 'haz': 'Resmî bir hazırlama şekli yoktur: ne Avrupa İlaç Ajansı’nın monografı ne de NCCIH sayfası vardır. '
        'Klinik çalışmalarda günde yaklaşık 40–70 gram kabuklu fıstık kullanılmıştır; bu bir besin '
        'miktarıdır, ilaç dozu değil.',
 'bilim': 'Antep fıstığı insan üzerinde randomize kontrollü çalışmaların yapıldığı az sayıdaki kuruyemişten '
          'biri. Çalışmalar fıstığın lipid profilini iyileştirdiğini, tip 2 diyabetli kişilerde kan basıncı '
          've kalp hızı değişkenliği ölçümlerini etkilediğini, insülin direnci ve inflamasyon belirteçlerinde '
          'iyileşme gösterdiğini bildiriyor. Bir çapraz geçişli çalışmada DNA oksidasyonu ve telomer bakımıyla '
          'ilgili genlerin ifadesinde değişiklik ölçülmüştür. Metabolik sendrom üzerine yapılmış randomize '
          'çalışmaların meta-analizi de vardır. Bu kanıt “besin olarak” kanıttır; onaylanmış bir tıbbi '
          'endikasyon yoktur.',
 'kanit': 'klinik',
 'guv': 'orta',
 'guvNot': 'Antep fıstığı bir ağaç kuruyemişidir; alerjisi ağır tepkilere yol açabilir. En önemli nokta '
           'KAJU ÇAPRAZ REAKTİVİTESİDİR: kaju alerjisi olan kişilerde antep fıstığı riski yüksektir, iki '
           'bitki aynı familyadadır (Anacardiaceae). Çocuklarda mango, antep fıstığı ve kaju arasında '
           'klinik çapraz tepkime gösterilmiştir. Kaju–antep fıstığı alerjisinde oral immünoterapi '
           'denenmiştir ama bu bir hekim gözetiminde yürütülen tedavidir. İlaç etkileşimi, hamilelik ve '
           'emzirme konusunda doğrulanmış veri yoktur.',
 'ilginc': 'Antep fıstığı iki evcikli bir ağaçtır ve kuşlarla bazı memelilerde görülen türden ZW eşey '
           'kromozomu taşır. W kromozomunun yaklaşık yüzde 23’ü rekombinasyona kapanmış bir bölgedir ve '
           'bu eşey kromozomu sistemi sıradan bir kromozomdan yaklaşık 8 milyon yıl önce türemiştir.',
 'ek': {'mevsim': 'Mart–nisanda çiçek açar, meyveler ağustos–eylülde olgunlaşır. Ağaç iki yılda bir bol '
                  'ürün verir; buna “periyodisite” denir.',
        'yetisme': 'Kurak ve sıcak iklimi sever, derin kök sistemiyle susuz koşullara dayanır. Türkiye’de '
                   'Gaziantep, Şanlıurfa, Siirt, Adıyaman ve Kahramanmaraş çevresinde yetiştirilir; sık sık '
                   'yabani Pistacia anaçlarına aşılanır.',
        'yoresel': 'Şam fıstığı',
        'karisma': 'Antep fıstığı ile karıştırılan türlerin hiçbiri aynı bitki değildir. Menengiç '
                   '(Pistacia terebinthus), buttum/bıttım (P. khinjuk, P. eurycarpa) ve P. atlantica ayrı '
                   'yabani türlerdir; Anadolu’da bunların meyve, reçine ve kahvesi kullanılır. Sakız '
                   '(mastic) ise Pistacia lentiscus reçinesidir ve Avrupa İlaç Ajansı’nın monografı olan '
                   'tek Pistacia türüdür — antep fıstığının monografı yoktur.'},
 'etk': [('Bilinen bir ilaç etkileşimi yok',
          'Antep fıstığı için doğrulanmış bir ilaç etkileşimi çalışması bulunmuyor. Besin olarak tüketilen '
          'miktarlarda bir kaygı bildirilmemiştir. Kaju alerjisi olan kişiler fıstıktan kaçınmalıdır; '
          'bu bir etkileşim değil, alerji riskidir.')],
 'etk_en': [('No known drug interaction',
             'No verified interaction study exists for pistachio, and none has been reported at food '
             'amounts. People allergic to cashew should avoid pistachio — that is an allergy risk, not an '
             'interaction.')],
 'kaynak': [('Jiang S ve ark., “The chromosome-level genome of pistachio (Pistacia vera) and the evolution '
             'of its ZW sex chromosomes”, Plant Communications 4(3): 100497, 2023 (PMID 36435969)', P + '36435969/'),
            AKSU,
            EKSIK,
            NEEF,
            ('Canudas S ve ark., “Pistachio consumption modulates DNA oxidation and genes related to '
             'telomere maintenance”, American Journal of Clinical Nutrition, 2019 (PMID 31051499)', P + '31051499/'),
            ('Hernández-Alonso P ve ark., “Beneficial effect of pistachio consumption on glucose '
             'metabolism, insulin resistance and inflammation”, Diabetes Care, 2014 (PMID 25125505)', P + '25125505/'),
            ('Sauder KA ve ark., “Effects of pistachios on the lipid/lipoprotein profile, '
             'hemodynamics and heart rate variability in type 2 diabetes”, Journal of the American Heart '
             'Association, 2014 (PMID 24980134)', P + '24980134/'),
            ('Ghanavati M ve ark., “Pistachios and metabolic syndrome: a systematic review and '
             'meta-analysis of randomized controlled trials”, Nutrition Reviews, 2022 (PMID 35689651)', P + '35689651/'),
            ('Elvan Çağlar Çıtak ve ark. / NUT CRACKER çalışması, “Oral immunotherapy for '
             'cashew–pistachio allergy”, Allergy, 2022 (PMID 35000223)', P + '35000223/'),
            ('Gradman J ve ark., “Clinical cross-reactivity between mango, pistachio and cashew in '
             'children”, Journal of Allergy and Clinical Immunology: In Practice, 2020 (PMID 32531479)', P + '32531479/'),
            ('Noorbakhsh R ve ark., “Pistachio allergy: prevalence and in vitro cross-reactivity with '
             'other tree nuts”, Allergology International, 2011 (PMID 21593580)', P + '21593580/')],
 'rel': ['badem', 'mese', 'okseotu'],
 'en': {'name': 'Pistachio',
        'other': 'Also called Damascus nut. The author abbreviation must be “L.”: Pistacia vera Mill. is an '
                 'illegitimate name.',
        'part': 'The kernel',
        'uses': [('Domesticated in the Fertile Crescent',
                  'Pistachio is a nut crop domesticated in the Fertile Crescent. In Turkey, Gaziantep, '
                  'Şanlıurfa and Siirt are the centre of production, and the species’ first reference '
                  'genome was sequenced from a female plant of the Siirt cultivar.'),
                 ('Wild relatives in Anatolian folk medicine',
                  'The Pistacia species with documented folk-medicinal use in Anatolia are the wild ones, '
                  'not pistachio itself. In Şırnak, Pistacia eurycarpa (“bendek”, “kızvan”, “bıttım”) is '
                  'boiled — branch and fruit — for constipation, haemorrhoids, stomach ache and gastric '
                  'ulcer. In Mardin, soap is made from the fruit of Pistacia khinjuk. Pistacia terebinthus '
                  'is known as menengiç and its fruit and resin are used. No Anatolian folk-medicinal '
                  'record was found for Pistacia vera itself; its cultural weight is culinary and commercial.'),
                 ('Not found at Göbekli Tepe',
                  'Layer III at Göbekli Tepe yielded fruit remains of the genus Pistacia (124 fragments, an '
                  'estimated 17 whole) and the largest share of the charcoal (3.14 g, 104 identifications). '
                  'But the charcoal was identified as Pistacia cf. atlantica — a wild Pistacia, not the '
                  'pistachio of commerce. The claim that pistachio was found at Göbekli Tepe is not '
                  'supported by the source.')],
        'prep': 'There is no official preparation: neither a European Medicines Agency monograph nor an '
                'NCCIH page exists. Clinical trials have used roughly 40–70 g of in-shell pistachios a day, '
                'a food amount rather than a drug dose.',
        'science': 'Pistachio is one of the few nuts trialled in randomised controlled studies in humans. '
                   'Trials report improvements in the lipid profile, effects on blood pressure and heart '
                   'rate variability in type 2 diabetes, and improvements in insulin resistance and '
                   'inflammatory markers. One crossover trial measured changes in the expression of genes '
                   'related to DNA oxidation and telomere maintenance. A meta-analysis of randomised trials '
                   'on metabolic syndrome also exists. This is evidence for pistachio as a food; there is '
                   'no approved medical indication.',
        'safety': 'Pistachio is a tree nut and its allergy can be severe. The key point is CASHEW '
                  'CROSS-REACTIVITY: people allergic to cashew are at high risk with pistachio, and the two '
                  'belong to the same family (Anacardiaceae). Clinical cross-reactivity between mango, '
                  'pistachio and cashew has been shown in children. Oral immunotherapy for '
                  'cashew–pistachio allergy has been trialled, but that is a treatment carried out under '
                  'medical supervision. There is no verified data on drug interactions, pregnancy or '
                  'breastfeeding.',
        'fact': 'Pistachio is dioecious and carries ZW sex chromosomes of the kind seen in birds and some '
                'mammals. About 23 per cent of the W chromosome is a region closed to recombination, and '
                'the system arose from an ordinary chromosome roughly 8 million years ago.',
        'season': 'Flowers in March and April, fruit ripens in August and September. The tree bears heavily '
                  'in alternate years.',
        'habitat': 'Likes a hot, dry climate and tolerates drought with a deep root system. Grown in Turkey '
                   'around Gaziantep, Şanlıurfa, Siirt, Adıyaman and Kahramanmaraş, often grafted onto '
                   'wild Pistacia rootstocks.',
        'local': 'Damascus nut',
        'confusion': 'None of the species confused with pistachio is the same plant. Menengiç (Pistacia '
                     'terebinthus), buttum (P. khinjuk, P. eurycarpa) and P. atlantica are separate wild '
                     'species whose fruit, resin and coffee are used in Anatolia. Mastic is the resin of '
                     'Pistacia lentiscus and is the only Pistacia with a European Medicines Agency '
                     'monograph — pistachio has none.'}},

# ---------------------------------------------------------------- 15 Aralık: MERCİMEK
{'yayin': '2026-12-15',
 'id': 'mercimek',
 'foto': 'Lens culinaris sl1.jpg',
 'tr': 'Mercimek',
 'la': 'Lens culinaris Medik.',
 'fam': 'Fabaceae (baklagiller)',
 'diger': 'Vicia lens (L.) Coss. & Germ. adıyla da yazılır; tarım ve tıp literatürü Lens culinaris adını kullanır.',
 'bolge': ['anadolu'],
 'kat': ['besin'],
 'kisim': 'Tohum',
 'taxon': 'Lens culinaris',
 'kul': [('Göbekli Tepe — yarım tohum',
          'Göbekli Tepe’de 1950 litre toprağın yüzdürülmesinden çıkan tüm mercimek kalıntısı, tek bir '
          'tohumun yarısıdır. Reinder Neef bu yarım tohumun çapını ölçmüş: 2,1 milimetre, yani yabani '
          'mercimek sınırları içinde. Evcil mercimek değil.'),
         ('Anadolu mutfağında',
          'Mercimek Anadolu’da en eski ve en yaygın temel gıdalardan biri; çorbası, köftesi ve pilavı '
          'bölgeden bölgeye değişen onlarca biçimde yapılır. Buna karşın taradığımız Türkçe etnobotanik ve '
          'halk hekimliği makalelerinin hiçbirinde mercimek bir halk ilacı olarak geçmiyor: Suruç, Şırnak, '
          'Mardin ve Develi derlemelerinde kayıt yok. Mercimeğin ağırlığı mutfakta, halk hekimliğinde değil.'),
         ('Tarımın başlangıcında',
          'Mercimek, Bereketli Hilal’de tahıllarla birlikte evcilleştirilen ilk baklagillerden biri. '
          'Yabani atası Lens culinaris subsp. orientalis. Arkeobotanik çalışmalar baklagillerin '
          'evcilleşmesinin tahıllardan daha yavaş olduğunu gösteriyor; tohum boyundaki artış yüzyıllar sürüyor.')],
 'haz': 'Resmî bir hazırlama şekli yoktur: ne Avrupa İlaç Ajansı’nın monografı ne de NCCIH sayfası vardır. '
        'Klinik çalışmalarda kullanılan biçim günde 100–200 gram civarında pişmiş mercimektir; '
        'bu bir besin miktarıdır.',
 'bilim': 'Mercimek insan üzerinde randomize kontrollü çalışmalarla incelenmiştir. On iki haftalık günlük '
          'mercimek tüketimi açlık kolesterolünü, öğün sonrası kan şekerini ve inflamasyon belirteçlerini '
          'etkiliyor; sekiz haftalık bir çalışma insülin direncinin ilerlemesini yavaşlattığını ve '
          'sindirim şikâyetlerini artırmadığını bildiriyor. Akut çalışmalarda pirinç ya da patatesin '
          'mercimekle değiştirilmesi öğün sonrası kan şekerini düşürüyor. Demirle zenginleştirilmiş '
          'mercimeğin ergen kızlarda demir durumunu iyileştirdiği küme randomize bir çalışmada '
          'gösterilmiştir. Bütün bu kanıt besin olarak kanıttır.',
 'kanit': 'klinik',
 'guv': 'dusuk',
 'guvNot': 'Mercimek için doğrulanmış bir ilaç etkileşimi, hamilelik-emzirme kısıtı ya da zehirlilik kaydı '
           'bulunamadı. Baklagil alerjisi vardır ama mercimeğe özgü doğrulanmış bir kaynak bulunamadığı '
           'için iddia edilmiyor. Baklagillerin çiğ tüketilmemesi genel bir mutfak kuralıdır.',
 'ilginc': 'Göbekli Tepe’den 1950 litre toprağın yüzdürülmesiyle elde edilen tüm mercimek kalıntısı tek bir '
           'tohumun yarısıdır — ve 2,1 milimetrelik çapıyla bu yarım tohum evcil değil, yabani mercimek '
           'sınırları içindedir.',
 'ek': {'mevsim': 'Kışlık ya da yazlık ekilir; Türkiye’de kırmızı mercimek çoğunlukla sonbaharda ekilip '
                  'haziran–temmuzda hasat edilir.',
        'yetisme': 'Bereketli Hilal kökenli. Türkiye’de Güneydoğu Anadolu, özellikle Şanlıurfa, Diyarbakır '
                   've Mardin, dünyanın en büyük kırmızı mercimek üretim bölgelerinden biridir. '
                   'Kurağa dayanıklı, az su ister.',
        'yoresel': '',
        'karisma': 'Mercimek ile burçak, bakla ve nohut gibi diğer baklagiller kuru tohum olarak '
                   'karıştırılabilir ama ayrı türlerdir. Yabani mercimek (Lens culinaris subsp. orientalis) '
                   'Anadolu’da doğal olarak bulunur ve tohumları evcil mercimekten belirgin biçimde küçüktür: '
                   'arkeologlar iki biçimi bu ölçüyle ayırır.'},
 'kaynak': [NEEF,
            ('Liber M ve ark., “Insights into the molecular basis of lentil domestication”, Frontiers in '
             'Plant Science 12: 628439, 2021 (PMID 33841458)', P + '33841458/'),
            ('Fuller DQ, “Contrasting patterns in crop domestication and domestication rates: recent '
             'archaeobotanical insights from the Old World”, Annals of Botany, 2007 (PMID 17495986)', P + '17495986/'),
            ('Moravek D ve ark., “Daily lentil consumption and fasting cholesterol, postprandial glucose '
             'and inflammation”, Nutrients 16(3): 419, 2024 (PMID 38337705)', P + '38337705/'),
            ('Ramdath DD ve ark., “Lentil consumption slows the progression of insulin resistance without '
             'increasing gastrointestinal symptoms”, Nutrition Research, 2022 (PMID 36122501)', P + '36122501/'),
            ('Mollard RC ve ark., “Replacing rice or potatoes with lentils lowers postprandial glycemia”, '
             'Journal of Nutrition, 2018 (PMID 29659967)', P + '29659967/'),
            ('Podder R ve ark., “Iron-fortified lentil and iron status in adolescent girls: a double-blind '
             'cluster-randomized trial”, Journal of Nutrition, 2024 (PMID 38458577)', P + '38458577/')],
 'rel': ['bugday', 'arpa', 'badem'],
 'en': {'name': 'Lentil',
        'other': 'Also written Vicia lens (L.) Coss. & Germ.; the agricultural and medical literature uses '
                 'Lens culinaris.',
        'part': 'The seed',
        'uses': [('Göbekli Tepe — half a seed',
                  'All the lentil recovered from 1,950 litres of floated soil at Göbekli Tepe is half of a '
                  'single seed. Reinder Neef measured it: 2.1 mm across, well within the range of a wild '
                  'lentil. Not the domesticated plant.'),
                 ('In Anatolian cooking',
                  'Lentil is one of the oldest and most widespread staples in Anatolia, made into soups, '
                  'köfte and pilaf in dozens of regional forms. Even so, none of the Turkish ethnobotanical '
                  'and folk-medicine papers we searched records lentil as a folk remedy: nothing in the '
                  'Suruç, Şırnak, Mardin or Develi surveys. Its weight is culinary, not medicinal.'),
                 ('At the beginning of agriculture',
                  'Lentil is among the first legumes domesticated alongside cereals in the Fertile '
                  'Crescent; its wild ancestor is Lens culinaris subsp. orientalis. Archaeobotanical work '
                  'shows legumes were domesticated more slowly than cereals — the increase in seed size '
                  'took centuries.')],
        'prep': 'There is no official preparation: neither a European Medicines Agency monograph nor an '
                'NCCIH page exists. Clinical trials use roughly 100–200 g of cooked lentils a day, a food amount.',
        'science': 'Lentil has been studied in randomised controlled trials in humans. Twelve weeks of '
                   'daily lentils affects fasting cholesterol, post-meal glucose and inflammatory markers; '
                   'an eight-week trial reports that it slows the progression of insulin resistance without '
                   'increasing gastrointestinal symptoms. In acute trials, replacing rice or potato with '
                   'lentils lowers post-meal blood glucose. Iron-fortified lentil improved iron status in '
                   'adolescent girls in a cluster-randomised trial. All of this is evidence for lentil as a food.',
        'safety': 'No verified drug interaction, pregnancy or breastfeeding restriction, or record of '
                  'toxicity was found for lentil. Legume allergy exists, but no lentil-specific verified '
                  'source was found, so no claim is made. Not eating legumes raw is a general kitchen rule.',
        'fact': 'All the lentil recovered from 1,950 litres of floated soil at Göbekli Tepe is half of a '
                'single seed — and at 2.1 mm across, that half seed is wild, not domesticated.',
        'season': 'Sown in winter or spring; in Turkey red lentil is mostly sown in autumn and harvested in '
                  'June and July.',
        'habitat': 'Native to the Fertile Crescent. Southeastern Anatolia — especially Şanlıurfa, Diyarbakır '
                   'and Mardin — is one of the world’s largest red lentil producing regions. Drought-hardy '
                   'and low in water need.',
        'local': '',
        'confusion': 'Lentil can be confused with bitter vetch, broad bean and chickpea as dry seed, but '
                     'these are separate species. Wild lentil (Lens culinaris subsp. orientalis) grows '
                     'naturally in Anatolia and its seeds are markedly smaller than the domesticated form: '
                     'archaeologists tell the two apart by that measurement.'}},

# ---------------------------------------------------------------- 16 Aralık: ARPA
{'yayin': '2026-12-16',
 'id': 'arpa',
 'foto': 'Barley J1.jpg',
 'tr': 'Arpa',
 'la': 'Hordeum vulgare L.',
 'fam': 'Poaceae (buğdaygiller)',
 'diger': 'Kürtçe ca, ce, ceh. Yabani atası Hordeum vulgare subsp. spontaneum (K.Koch) Asch. & Graebn., '
          'eski adıyla Hordeum spontaneum K.Koch.',
 'bolge': ['anadolu'],
 'kat': ['sifa', 'besin', 'ritual'],
 'kisim': 'Tane; gövde zanaatta',
 'taxon': 'Hordeum vulgare',
 'kul': [('Göbekli Tepe — ve bugün aynı yamaçta',
          'Göbekli Tepe’nin III. tabakasında Hordeum cf. spontaneum, yani yabani arpa tanımlanmıştır: '
          'tahminen 16 bütün taneye karşılık gelen parçalar. Reinder Neef taneleri ölçmüş; yassı '
          '(0,7–1,4 mm) ve geniş oluklu olmaları yabani arpayı gösteriyor. Aynı rapor bugünkü bitki '
          'örtüsünü de kaydediyor: Göbekli Tepe platosunun yamaçları hâlâ yabani arpanın baskın olduğu bir '
          'ot stepiyle kaplı. Yani bu bitki on bir buçuk bin yıldır aynı yamaçta duruyor.'),
         ('Mardin — siğil ritüeli',
          'Mardin’in kırsal köylerinde arpa taneleri, vücuttaki siğilleri yok edeceği düşüncesiyle, '
          'üzerlerine bazı özel dualar okunduktan sonra toprağın altına gömülüyor. Aynı inanç kapsamında '
          'kuş kirazı ve asma da kullanılıyor. Yerel adı “ceh”.'),
         ('Şırnak — halk hekimliği',
          'Arpa tohumunun kaynatılıp içilmesi bağırsak iltihabı ve kabızlık için kullanılıyor; '
          'yerel adları “ca” ve “ce”.'),
         ('Mardin — zanaat',
          'Arpa gövdesi sepet ve pipet yapımında kullanılıyor. “Temir” ya da “kendırge” adı verilen bir '
          'müzik aletinin yapımında da geçiyor: dişlerin arasına alınıp üflenerek zurnaya benzer bir ses çıkarılıyor.')],
 'haz': 'Avrupa İlaç Ajansı’nın monografı ve NCCIH sayfası yoktur, ama arpa bu dört bitki arasında '
        'düzenleyici onaylı sağlık beyanı olan tek bitkidir. Avrupa Birliği’nin izin verilen sağlık '
        'beyanları listesine göre: porsiyon başına en az 1 gram beta-glukan içeren gıdalar için '
        '“beta-glukanlar normal kan kolesterol düzeylerinin korunmasına katkıda bulunur” beyanı '
        'kullanılabilir ve belirtilen fayda günde 3 gram alımda geçerlidir. Porsiyondaki her 30 gram '
        'kullanılabilir karbonhidrat için en az 4 gram beta-glukan içeren gıdalar, öğünle birlikte '
        'alındığında kan şekeri yükselişini azaltma beyanını taşıyabilir. “Arpa tanesi lifi dışkı '
        'hacminin artmasına katkıda bulunur” beyanı ise yalnızca “yüksek lifli” sayılan gıdalar içindir.',
 'bilim': 'Arpanın beta-glukanı, randomize kontrollü çalışmaların meta-analizleriyle LDL kolesterolü, '
          'HDL dışı kolesterolü ve apolipoprotein B’yi düşürdüğü gösterilmiş bir çözünür liftir. '
          'Arpa kaynaklı çözünür lifin serum lipidlerine etkisi insanlarda ayrıca ölçülmüş; hafif yüksek '
          'kolesterollü kişilerde dışkıyla safra asidi atılımını ve kısa zincirli yağ asidi üretimini '
          'artırdığı bildirilmiştir. Dört bitki arasında düzenleyici onay almış tek beyan arpaya aittir.',
 'kanit': 'klinik',
 'guv': 'orta',
 'guvNot': 'ÇÖLYAK VE GLUTEN — kritik: arpa hordein içerir ve çölyak hastalığında yasaktır. Glutensiz diyet '
           'buğday, çavdar ve arpanın tamamen çıkarılmasını gerektirir. Arpa suyu, arpa maltı, malt '
           'ekstraktı, malt sirkesi ve bira da glutenlidir. Amerikan Gastroenteroloji Koleji’nin 2023 '
           'kılavuzu bu üçlüyü birlikte sayar. Beta-glukan öğün sonrası kan şekerini düşürdüğü için '
           'şeker hastalığı ilacı kullananlarda teorik bir dikkat gerekir; bunu doğrudan ölçen bir '
           'etkileşim çalışması bulunamadı. Hamilelik, emzirme ve zehirlilik konusunda kayıt bulunamadı.',
 'ilginc': 'Mardin’in kırsal köylerinde arpa taneleri bugün hâlâ, üzerlerine dua okunarak siğillerin '
           'geçmesi için toprağa gömülüyor — ve aynı yabani arpa, on bir buçuk bin yıl önce Göbekli '
           'Tepe’yi çevreleyen step bitki örtüsünün baskın türüydü. Bugün de platonun yamaçlarını kaplıyor.',
 'ek': {'mevsim': 'Çoğunlukla sonbaharda ekilir, haziranda hasat edilir; yazlık ekim de yapılır. '
                  'Buğdaydan daha erken olgunlaşır.',
        'yetisme': 'Bereketli Hilal kökenli; Türkiye’nin her bölgesinde yetişir. Buğdaydan daha kurağa, '
                   'tuza ve kısa yetişme dönemine dayanıklıdır, bu yüzden step ve yüksek rakımlarda '
                   'buğdayın yetişemediği yerlerde ekilir.',
        'yoresel': 'Ca, ce, ceh',
        'karisma': 'Arpa ile buğday ve çavdar başaktan ayırt edilir: arpanın kılçıkları çok uzun ve '
                   'başağın tamamı boyunca dizilidir. Yabani arpa (Hordeum vulgare subsp. spontaneum) '
                   'Anadolu’da doğal olarak bulunur ve başağı olgunlaşınca kendiliğinden dağılır; '
                   'arkeologlar evcil ile yabaniyi bu özellikten ve tane biçiminden ayırır. '
                   'Üçü de glutenli olduğu için çölyak açısından aralarında fark yoktur.'},
 'etk': [('Şeker hastalığı ilaçları ve insülin',
          'Arpanın beta-glukanı öğün sonrası kan şekeri yükselişini azaltır; bu etki Avrupa Birliği '
          'tarafından onaylanmış bir sağlık beyanıdır. Bunu doğrudan ölçen bir ilaç etkileşimi çalışması '
          'bulunamadı, ama kan şekeri düşürücü ilaç ya da insülin kullananların beslenmesinde belirgin bir '
          'değişiklik yapmadan önce hekimine danışması doğru olur.'),
         ('Çölyak hastalığı ve gluten duyarlılığı',
          'Bu bir ilaç etkileşimi değil kesin bir kısıttır: arpa hordein içerir ve çölyak hastalığında '
          'hiçbir biçimde tüketilmemelidir. Arpa maltı, malt ekstraktı, malt sirkesi ve bira da buna dahildir.')],
 'etk_en': [('Diabetes medicines and insulin',
             'Barley beta-glucan reduces the post-meal rise in blood glucose — an approved health claim in '
             'the European Union. No interaction study measuring this directly was found, but anyone on '
             'glucose-lowering medicines or insulin should speak to their doctor before changing their diet '
             'substantially.'),
            ('Coeliac disease and gluten sensitivity',
             'This is not an interaction but a firm restriction: barley contains hordein and must not be '
             'eaten at all in coeliac disease. That includes barley malt, malt extract, malt vinegar and beer.')],
 'kaynak': [NEEF,
            EKSIK,
            AKSU,
            AB432,
            ('Ho HVT ve ark., “The effect of oat and barley β-glucan on LDL-cholesterol, non-HDL-cholesterol '
             'and apoB: a systematic review and meta-analysis of randomised controlled trials”, '
             'European Journal of Clinical Nutrition, 2016 (PMID 27273067)', P + '27273067/'),
            ('Talati R ve ark., “The lipid-lowering capacity of barley β-glucan: a meta-analysis of '
             'randomized controlled trials”, European Journal of Clinical Nutrition, 2010 (PMID 20924392)', P + '20924392/'),
            ('Talati R ve ark., “The effects of barley-derived soluble fiber on serum lipids”, '
             'Annals of Family Medicine, 2009 (PMID 19273871)', P + '19273871/'),
            ('Wang Y ve ark., “Barley β-glucan, faecal bile acid excretion and short-chain fatty acids in '
             'mildly hypercholesterolaemic adults”, Food & Function, 2018 (PMID 29872803)', P + '29872803/'),
            ('Rubio-Tapia A ve ark., “American College of Gastroenterology Guidelines Update: Diagnosis and '
             'Management of Celiac Disease”, American Journal of Gastroenterology, 2023 (PMID 36602836)', P + '36602836/'),
            ('Lindfors K ve ark., “Coeliac disease”, Nature Reviews Disease Primers, 2019 (PMID 30631077)', P + '30631077/')],
 'rel': ['bugday', 'mercimek', 'badem'],
 'en': {'name': 'Barley',
        'other': 'Kurdish ca, ce, ceh. Its wild ancestor is Hordeum vulgare subsp. spontaneum (K.Koch) '
                 'Asch. & Graebn., formerly Hordeum spontaneum K.Koch.',
        'part': 'The grain; the stem in craft use',
        'uses': [('Göbekli Tepe — and still on the same slope',
                  'Layer III at Göbekli Tepe yielded Hordeum cf. spontaneum, wild barley: fragments '
                  'amounting to an estimated 16 whole grains. Reinder Neef measured them — flat (0.7–1.4 mm) '
                  'with a relatively wide furrow, which marks them as wild. The same report records the '
                  'present-day vegetation too: the slopes of the Göbekli Tepe plateau are still covered in '
                  'a grass steppe dominated by wild barley. The plant has been on that slope for eleven and '
                  'a half thousand years.'),
                 ('Mardin — a wart ritual',
                  'In the rural villages of Mardin, barley grains are buried in the ground after certain '
                  'prayers are said over them, in the belief that this will make warts on the body '
                  'disappear. Bird cherry and grapevine are used in the same way. The local name is “ceh”.'),
                 ('Şırnak — folk medicine',
                  'A decoction of barley seed is drunk for bowel inflammation and constipation, under the '
                  'names “ca” and “ce”.'),
                 ('Mardin — craft',
                  'Barley stems are used to make baskets and drinking straws. They also go into an '
                  'instrument called “temir” or “kendırge”, held between the teeth and blown to produce a '
                  'sound like a zurna.')],
        'prep': 'There is no European Medicines Agency monograph and no NCCIH page, but barley is the only '
                'one of these four plants with an approved regulatory health claim. Under the European '
                'Union’s list of permitted health claims, foods with at least 1 g of beta-glucan per '
                'portion may carry the claim that beta-glucans contribute to the maintenance of normal '
                'blood cholesterol levels, with the stated benefit at an intake of 3 g a day. Foods with at '
                'least 4 g of beta-glucan per 30 g of available carbohydrate may carry the claim that '
                'eating them as part of a meal reduces the rise in blood glucose. The claim that barley '
                'grain fibre contributes to an increase in faecal bulk applies only to foods qualifying as '
                '“high fibre”.',
        'science': 'Barley beta-glucan is a soluble fibre shown in meta-analyses of randomised controlled '
                   'trials to lower LDL cholesterol, non-HDL cholesterol and apolipoprotein B. The effect '
                   'of barley-derived soluble fibre on serum lipids has also been measured in humans, and '
                   'in mildly hypercholesterolaemic adults it increased faecal bile acid excretion and '
                   'short-chain fatty acid production. Of these four plants, barley is the only one with a '
                   'claim that has regulatory approval.',
        'safety': 'COELIAC DISEASE AND GLUTEN — critical: barley contains hordein and is forbidden in '
                  'coeliac disease. A gluten-free diet requires the complete removal of wheat, rye and '
                  'barley. Barley water, barley malt, malt extract, malt vinegar and beer all contain '
                  'gluten. The 2023 guideline of the American College of Gastroenterology names the three '
                  'together. Because beta-glucan lowers post-meal blood glucose, theoretical caution is '
                  'needed for people on diabetes medicines; no study measuring this interaction directly '
                  'was found. No record was found for pregnancy, breastfeeding or toxicity.',
        'fact': 'In the rural villages of Mardin, barley grains are still buried in the ground with prayers '
                'said over them to make warts go away — and the same wild barley was the dominant species '
                'of the steppe vegetation around Göbekli Tepe eleven and a half thousand years ago. '
                'It still covers the slopes of the plateau today.',
        'season': 'Mostly sown in autumn and harvested in June; spring sowing is also practised. It ripens '
                  'earlier than wheat.',
        'habitat': 'Native to the Fertile Crescent; grown in every region of Turkey. More tolerant than '
                   'wheat of drought, salt and a short growing season, so it is sown on the steppe and at '
                   'altitudes where wheat will not grow.',
        'local': 'Ca, ce, ceh',
        'confusion': 'Barley is told from wheat and rye by the ear: its awns are very long and run the '
                     'whole length of it. Wild barley (Hordeum vulgare subsp. spontaneum) grows naturally '
                     'in Anatolia and its ear shatters on its own when ripe; archaeologists distinguish '
                     'domesticated from wild by that trait and by grain shape. All three contain gluten, so '
                     'for coeliac disease there is no difference between them.'}},
]
