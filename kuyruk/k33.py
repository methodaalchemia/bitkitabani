# WHO monografı partisi I (17–19 Kasım 2026): soğan, şakayık, yılankökü.
# Kaynak: DSÖ "Monographs on selected medicinal plants" Cilt 1 (1999) +
# güncel PubMed derlemesi + POWO. DSÖ monografları 1999 tarihli olduğu
# için kanıt düzeyi hep güncel derlemeye göre verildi.
from kunye_elle import who_url
Q = [

    dict(
        yayin='2026-11-17',
        id='sogan',
        foto='',
        tr='Soğan',
        la='Allium cepa L.',
        fam='Amaryllidaceae (nergisgiller)',
        diger='Türkçe soğan, baş soğan, kuru soğan; İngilizce onion. DSÖ '
              'monografı droğu "Bulbus Allii Cepae" — taze ya da kurutulmuş '
              'soğan başı — diye tanımlıyor. TİTCK ve AB monografı yok; kayıt '
              'DSÖ monografına, PubMed’e ve POWO’ya dayanıyor. Sarımsakla aynı '
              'cinsten.',
        bolge=['anadolu', 'asya', 'avrupa'],
        kat=['sifa', 'besin'],
        kisim='Taze ya da kurutulmuş soğan başı',
        taxon='Allium cepa',
        kul=[
            ['DSÖ monografı (1999)', 'Dünya Sağlık Örgütü’nün tıbbi bitki '
             'monografları serisinin ilk cildinde soğan var. "Klinik veriyle '
             'desteklenen kullanım" başlığında damarlarda yaşa bağlı '
             'değişikliklerin önlenmesi ve iştahsızlık; farmakopelerde ve '
             'geleneksel sistemlerde dizanteri gibi bakteriyel enfeksiyonlar, '
             'idrar söktürücü, yara ve yanık izi, astım ve diyabette yardımcı '
             'tedavi. Günlük doz 50 g taze soğan ya da 20 g kuru drog. '
             'Monografın güvenlik cümlesi kataloğumuzdaki en kısa olanı: '
             '"güvenlik düzeyi, dünya çapında sebze olarak tüketilmesiyle '
             'yansıtılmaktadır."'],
            ['Türkiye', 'TİTCK Tıbbi Bitki Listesi’nde soğan için monograf yok '
             '— bir sebze olarak listeye gerek de görülmemiş. Anadolu halk '
             'hekimliğinde soğanın yara, çıban ve öksürükte kullanımı yaygın '
             'biliniyor; kataloğumuz bu kullanımları kaynaklı olarak '
             'genişletmiyor.'],
            ['Dünya — en eski sebzelerden', 'Soğan Orta Asya kökenli; Mısır, '
             'Mezopotamya ve Hitit kaynaklarında geçiyor ve bugün dünyanın en '
             'çok yetiştirilen sebzelerinden. Yara izi jeli olarak soğan özütü '
             'Avrupa ve Amerika’da ticari bir ürün — kanıt bölümünde bu ürün '
             'ayrıca ele alınıyor.'],
        ],
        haz='DSÖ monografı günlük doz olarak 50 g taze soğan ya da 20 g '
            'kurutulmuş drog veriyor; hazırlıkların dozu buna göre '
            'hesaplanıyor. Bir sebze olduğu için ayrı bir "hazırlayış" yok; '
            'yara izi için satılan soğan özütlü jeller ayrı ürünlerdir.',
        bilim='Soğanın iki ayrı kanıt hattı var. **Metabolik parametreler:** '
              '2023’te Clinical Nutrition ESPEN dergisinde yayımlanan '
              'sistematik derleme ve meta-analiz 14 randomize çalışmayı '
              'birleştirdi: soğan takviyesi vücut yağ oranını, LDL ve toplam '
              'kolesterolü ve sistolik kan basıncını anlamlı ölçüde '
              'iyileştirdi; 12 haftadan uzun ve günde 300 mg’ın üstündeki '
              'kullanımlarda kilo, bel çevresi ve beden kitle indeksinde de '
              'fark görüldü. Bu, DSÖ’nün 1999’da "damarlarda yaşa bağlı '
              'değişiklik" diye yazdığı kullanımın güncel karşılığı. **Yara '
              'izi:** soğan özütlü jel en çok satılan soğan ürünü; ama 2021’de '
              'International Wound Journal’da yayımlanan meta-analizin başlığı '
              'sonucu özetliyor — soğan özütü jeli yara izi yönetiminde öteki '
              'topikal tedavilerden **daha iyi değil.** Yani ünlü ürünün '
              'kanıtı, ünlü olmayan kullanımdan zayıf. Etki büyüklükleri '
              'ölçülü ve çalışmaların kalitesi karışık; kanıt düzeyi '
              '"sınırlı".',
        kanit='sinirli',
        guv='yuksek',
        guvNot='DSÖ monografı kontrendikasyon olarak yalnızca soğan alerjisini '
               'veriyor ve uyarı bildirmiyor; istenmeyen etki olarak alerjik '
               'rinokonjunktivit ve kontakt dermatit (özellikle soğan doğrayan '
               'mutfak çalışanlarında) bildirilmiş. Gebelik, emzirme, çocuk ve '
               'ilaç etkileşimi için monograf "bildirilmemiş" diyor — sebze '
               'dozlarında bir güvenlik sorunu beklenmiyor. Takviye dozlarında '
               '(özüt, kapsül) kan şekeri ve pıhtılaşma üzerindeki olası '
               'etkiler nedeniyle antidiyabetik ve antikoagülan kullananların '
               'hekimine söylemesi mantıklı — bu bir kuramsal nottur.',
        etk=[
            ['DSÖ monografında bildirilmiş etkileşim yok',
             'Monograf ilaç etkileşimi bildirmiyor. Sarımsakla aynı cinsten '
             'olduğu için sarımsak kaydındaki antikoagülan uyarısı takviye '
             'dozlarında soğan için de kuramsal olarak akılda tutulabilir; '
             'sebze olarak yenen soğan için böyle bir uyarı yoktur.'],
        ],
        ilginc='Dünya Sağlık Örgütü bir sebzeye monograf yazdı ve güvenlik '
               'bölümünü tek cümleyle geçti: güvenliği, dünya çapında sebze '
               'olarak yenmesiyle gösterilmiş. Kataloğumuzda hiçbir bitkinin '
               'güvenlik kanıtı bu kadar büyük bir örnekleme dayanmıyor. Buna '
               'karşılık soğanın en çok satılan tıbbi ürünü — yara izi jeli — '
               'meta-analizde öteki tedavilerden daha iyi çıkmadı. Mutfaktaki '
               'soğan ile eczanedeki soğan aynı bitkiden iki ayrı kanıt '
               'hikâyesi.',
        ek=dict(
            mevsim='İki yıllık; birinci yıl soğan başı oluşur, yaz sonunda '
                   'hasat edilir ve kurutulup saklanır.',
            yetisme='Orta Asya kökenli; dünyanın her yerinde kültür bitkisi. '
                    'Türkiye büyük üreticilerden.',
            yoresel='Soğan, baş soğan, kuru soğan; yöresel adlar kaynaksız '
                    'genişletilmedi.',
            karisma='Yabani Allium türleriyle karışma mutfakta değil doğada '
                    'olur; bazı soğanımsı soğanlı bitkiler (örneğin Colchicum, '
                    'acıçiğdem) zehirlidir ve yabani "soğan" diye '
                    'toplanmamalıdır.',
        ),
        ema=[],
        kaynak=[
            ['N. Hejazi ve ark., “Onion supplementation and health metabolic '
             'parameters: A systematic review and meta-analysis of randomized '
             'controlled trials”, Clinical Nutrition ESPEN 58, 2023',
             'https://pubmed.ncbi.nlm.nih.gov/38056991/'],
            ['X. Yuan ve ark., “Onion extract gel is not better than other '
             'topical treatments in scar management: A meta-analysis from '
             'randomised controlled trails”, International Wound Journal '
             '18(3), 2021',
             'https://pubmed.ncbi.nlm.nih.gov/33372412/'],
            ['Bulbus Allii Cepae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 1, 1999', who_url(1, 'bulbus-allii-cepae')],
        ],
        rel=['sarimsak', 'zeytin'],
        en=dict(
            name='Onion',
            other='Turkish soğan, baş soğan, kuru soğan; in English onion. The '
                  'WHO monograph defines the drug as "Bulbus Allii Cepae" — the '
                  'fresh or dried bulb. No Turkish or EU monograph; the record '
                  'rests on the WHO monograph, PubMed and POWO. Same genus as '
                  'garlic.',
            part='The fresh or dried bulb',
            uses=[
                ['WHO monograph (1999)', 'Onion is in the first volume of the '
                 'World Health Organization’s medicinal plant monographs. '
                 'Under "uses supported by clinical data": prevention of '
                 'age-dependent changes in the blood vessels, and loss of '
                 'appetite; in pharmacopoeias and traditional systems: '
                 'bacterial infections such as dysentery, as a diuretic, for '
                 'wounds and scars, asthma, and as adjuvant therapy in '
                 'diabetes. Daily dose 50 g fresh onion or 20 g dried drug. '
                 'The monograph’s safety sentence is the shortest in this '
                 'catalog: "the level of safety ... is reflected by its '
                 'worldwide use as a vegetable."'],
                ['Turkey', 'There is no monograph for onion on the Turkish '
                 'list — as a vegetable, none was thought necessary. The use '
                 'of onion for wounds, boils and coughs in Anatolian folk '
                 'medicine is widely known; this catalog does not extend those '
                 'uses without a source.'],
                ['World — among the oldest vegetables', 'Onion originates in '
                 'central Asia; it appears in Egyptian, Mesopotamian and '
                 'Hittite sources and is today one of the world’s most '
                 'cultivated vegetables. Onion extract as a scar gel is a '
                 'commercial product in Europe and America — the science '
                 'section deals with that product separately.'],
            ],
            prep='The WHO monograph gives a daily dose of 50 g fresh onion or '
                 '20 g dried drug, with preparations dosed accordingly. Being '
                 'a vegetable it has no separate "preparation"; the onion '
                 'extract gels sold for scars are separate products.',
            science='Onion has two separate lines of evidence. **Metabolic '
                    'parameters:** a systematic review and meta-analysis '
                    'published in 2023 in Clinical Nutrition ESPEN pooled 14 '
                    'randomised trials: onion supplementation significantly '
                    'improved body fat percentage, LDL and total cholesterol '
                    'and systolic blood pressure; with use longer than 12 '
                    'weeks and above 300 mg/day, weight, waist circumference '
                    'and body mass index differed too. That is the current '
                    'counterpart of what the WHO wrote in 1999 as '
                    '"age-dependent changes in the blood vessels". **Scars:** '
                    'onion extract gel is the best-selling onion product; but '
                    'the title of a meta-analysis published in 2021 in the '
                    'International Wound Journal sums up the result — onion '
                    'extract gel is **not better** than other topical '
                    'treatments in scar management. So the famous product has '
                    'weaker evidence than the unfamous use. Effect sizes are '
                    'modest and trial quality mixed; evidence level Limited.',
            safety='The WHO monograph gives only onion allergy as a '
                   'contraindication and reports no warnings; allergic '
                   'rhinoconjunctivitis and contact dermatitis (especially in '
                   'kitchen workers who chop onions) have been reported as '
                   'adverse reactions. For pregnancy, lactation, children and '
                   'drug interactions the monograph says "none reported" — no '
                   'safety problem is expected at vegetable doses. At '
                   'supplement doses (extract, capsule), because of possible '
                   'effects on blood glucose and clotting, anyone on '
                   'antidiabetics or anticoagulants would sensibly tell their '
                   'doctor — a theoretical note.',
            fact='The World Health Organization wrote a monograph for a '
                 'vegetable and dealt with the safety section in one '
                 'sentence: its safety is shown by its being eaten worldwide '
                 'as a vegetable. No plant in this catalog has safety evidence '
                 'resting on a larger sample. Yet onion’s best-selling '
                 'medical product — the scar gel — came out no better than '
                 'other treatments in meta-analysis. The onion in the kitchen '
                 'and the onion in the pharmacy are two evidence stories from '
                 'one plant.',
            season='Biennial; the bulb forms in the first year, is harvested in '
                   'late summer, dried and stored.',
            habitat='Native to central Asia; cultivated everywhere. Turkey is '
                    'among the large producers.',
            local='Soğan, baş soğan, kuru soğan; regional names not extended '
                  'without a source.',
            confusion='Confusion with wild Allium species happens in the field, '
                      'not the kitchen; some bulbous look-alikes (e.g. '
                      'Colchicum, autumn crocus) are poisonous and must not be '
                      'gathered as wild "onion".',
        ),
        etk_en=[
            ['No interactions reported in the WHO monograph',
             'The monograph reports no drug interactions. Being of the same '
             'genus as garlic, the anticoagulant caution in the garlic record '
             'may theoretically be kept in mind for onion at supplement doses; '
             'no such caution applies to onion eaten as a vegetable.'],
        ],
    ),

    dict(
        yayin='2026-11-18',
        id='sakayik',
        foto='',
        tr='Şakayık',
        la='Paeonia lactiflora Pall.',
        fam='Paeoniaceae (şakayıkgiller)',
        diger='Türkçe şakayık, beyaz şakayık; Çince báisháo (beyaz şakayık '
              'kökü), İngilizce white peony root. DSÖ monografı droğu "Radix '
              'Paeoniae" — kurutulmuş kök — diye tanımlıyor. TİTCK monografı '
              'yok; AB için 2015’te monograf yerine kamu açıklaması yayımlandı. '
              'Türkiye’deki yabani şakayıklar (P. mascula, P. peregrina) başka '
              'türlerdir.',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Kurutulmuş kökü',
        taxon='Paeonia lactiflora',
        kul=[
            ['DSÖ monografı (1999)', '"Klinik veriyle desteklenen kullanım": '
             'yok. Farmakopelerde ve geleneksel sistemlerde: amenore, '
             'dismenore, göğüs ve karın ağrısında ağrı kesici, iltihap '
             'giderici ve spazm çözücü; baş ağrısı, baş dönmesi, baldır '
             'krampları, karaciğer hastalığı ve alerjiler. Günlük en çok 6–15 g '
             'kök (paeoniflorin için standardize). **Gebelikte kontrendike:** '
             'geleneksel kayıtlar düşük yaptırıcı etkiye işaret ediyor.'],
            ['Avrupa — monograf yok, kamu açıklaması var', 'Avrupa İlaç Ajansı '
             '2015’te beyaz şakayık kökü için monograf yerine kamu açıklaması '
             'yayımladı: AB’de yeterli kullanım geçmişi ve veri olmadığı için '
             'monograf kurulamadı. Çin tıbbının en temel droglarından birinin '
             'Avrupa’da resmî yeri yok.'],
            ['Çin — temel drog', 'Beyaz şakayık kökü (báisháo) Çin tıbbının en '
             'eski ve en çok kullanılan droglarından; kan ve karaciğer '
             '"besleyici" formüllerin bileşeni. Kökün standardize özütü '
             '("total glucosides of paeony", TGP) Çin’de romatoid artrit için '
             'ruhsatlı bir ilaç — ve kanıt bölümündeki meta-analiz buna ait.'],
        ],
        haz='DSÖ monografı günlük en çok 6–15 g kurutulmuş kök veriyor, '
            'paeoniflorin için standardize. Çin’de kullanılan TGP kapsülleri '
            'reçeteli ilaçtır. **Gebelikte kullanılmaz;** emzirirken ve '
            'çocuklarda da önerilmiyor.',
        bilim='Şakayık kökünün en güçlü kanıtı Çin’de ruhsatlı özütüne ait. '
              '2021’de BMC Complementary Medicine and Therapies dergisinde '
              'yayımlanan sistematik derleme ve meta-analiz, romatoid artritte '
              'TGP’nin standart ilaçlara (metotreksat, leflunomid ve diğerleri) '
              '**eklenmesini** inceleyen 39 çalışmayı (3.680 hasta) birleştirdi '
              've asıl bulgusu güvenlikle ilgili: TGP eklenen gruplarda '
              'karaciğer yan etkisi (RR 0,31; %95 GA 0,23–0,41) ve lökopeni '
              'anlamlı ölçüde daha azdı. Yani çalışmalar şakayığın hastalığı '
              'tedavi ettiğini değil, ilaçların yan etkisini azaltabildiğini '
              'ölçüyor; hepsi Çin’de yapılmış ve kalite değişken. DSÖ '
              'monografının 1999’daki "klinik veri yok" hükmü bu özüt için '
              'artık eski, ama drog olarak kök çayı için hâlâ geçerli. Kanıt '
              'düzeyi "sınırlı".',
        kanit='sinirli',
        guv='orta',
        guvNot='**Gebelikte kontrendike** — DSÖ monografı geleneksel kayıtlara '
               'dayanarak düşük yaptırıcı etkiden söz ediyor. Emzirirken ve '
               'çocuklarda veri olmadığı için önerilmiyor. İstenmeyen etki '
               'bilgisi monografta yok; TGP meta-analizinde en sık bildirilen '
               'etki yumuşak dışkı ve ishaldir. Monograf, Çin tıbbı '
               'geleneğinden üç bitkiyle birlikte kullanılmamasını da '
               'aktarıyor (aşağıda). Türkiye’deki yabani şakayık türleri bu '
               'monografın kapsamında değildir ve kökleri doğadan '
               'sökülmemelidir.',
        etk=[
            ['Fritillaria, Cuscuta ve ravent (Rheum officinale)',
             'DSÖ monografı Çin farmakopesine dayanarak şakayık kökünün bu '
             'üç drogla birleştirilmemesi gerektiğini aktarıyor — '
             'geleneksel uyumsuzluk kuralı, farmakolojik etkileşim verisi '
             'değil.'],
            ['Antikoagülanlar (kuramsal)',
             'Monograf geleneksel kullanımlar arasında "antikoagülan" '
             'sayıyor; kan sulandırıcı kullananlar için kuramsal bir '
             'üst üste binme notu.'],
        ],
        ilginc='Çin tıbbının en temel droglarından biri, Avrupa’da resmî bir '
               'yere sahip değil: Avrupa İlaç Ajansı 2015’te monograf yerine '
               'kamu açıklaması yayımladı. Oysa aynı kökün özütü Çin’de '
               'romatoid artrit için ruhsatlı ilaç ve 39 çalışmalık bir '
               'meta-analizi var. Bir bitkinin "resmî" durumu kıtaya göre '
               'değişiyor — ve Türkiye’de bahçelerde süs için yetişen şakayık '
               'ile Çin eczanesindeki báisháo aynı cinsten ayrı türler.',
        ek=dict(
            mevsim='İlkbahar sonunda iri beyaz-pembe çiçekler; kök '
                   'sonbaharda, 4–5 yıllık bitkilerden sökülür.',
            yetisme='Kuzey Çin, Moğolistan ve Sibirya’nın yerlisi; Çin’de '
                    'geniş çapta kültürü yapılıyor. Türkiye’de süs bitkisi.',
            yoresel='Şakayık, beyaz şakayık; Çince báisháo.',
            karisma='⚠️ Türkiye’de yabani şakayıklar (Paeonia mascula, P. '
                    'peregrina, P. tenuifolia) ayrı türlerdir ve bazıları '
                    'korunur; monograf yalnızca P. lactiflora içindir. "Kırmızı '
                    'şakayık kökü" (chìsháo) aynı türün işlenmemiş kökü ya da '
                    'P. veitchii’dir ve Çin tıbbında ayrı bir drogdur.',
        ),
        ema=[],
        kaynak=[
            ['B. Liu ve ark., “Clinical safety of total glucosides of paeony '
             'adjuvant therapy for rheumatoid arthritis treatment: a '
             'systematic review and meta-analysis”, BMC Complementary Medicine '
             'and Therapies 21(1), 2021',
             'https://pubmed.ncbi.nlm.nih.gov/33771151/'],
            ['Radix Paeoniae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 1, 1999', who_url(1, 'radix-paeoniae')],
        ],
        rel=['seytanpencesi', 'sogut'],
        en=dict(
            name='White peony root',
            other='Turkish şakayık, beyaz şakayık; Chinese báisháo (white peony '
                  'root), English white peony root. The WHO monograph defines '
                  'the drug as "Radix Paeoniae" — the dried root. No Turkish '
                  'monograph; for the EU a public statement was issued in 2015 '
                  'instead of a monograph. The wild peonies of Turkey (P. '
                  'mascula, P. peregrina) are different species.',
            part='The dried root',
            uses=[
                ['WHO monograph (1999)', '"Uses supported by clinical data": '
                 'none. In pharmacopoeias and traditional systems: as an '
                 'analgesic, anti-inflammatory and antispasmodic in '
                 'amenorrhoea, dysmenorrhoea and chest and abdominal pain; '
                 'headache, vertigo, calf cramps, liver disease and allergies. '
                 'Maximum daily dose 6–15 g of root (standardised for '
                 'paeoniflorin). **Contraindicated in pregnancy:** traditional '
                 'reports point to abortifacient activity.'],
                ['Europe — no monograph, a public statement', 'In 2015 the '
                 'European Medicines Agency issued a public statement instead '
                 'of a monograph for white peony root: with insufficient '
                 'history of use and data in the EU, no monograph could be '
                 'established. One of Chinese medicine’s most basic drugs '
                 'has no official place in Europe.'],
                ['China — a foundational drug', 'White peony root (báisháo) is '
                 'among the oldest and most used drugs of Chinese medicine, an '
                 'ingredient of blood- and liver-"nourishing" formulas. A '
                 'standardised extract of the root ("total glucosides of '
                 'paeony", TGP) is a licensed drug for rheumatoid arthritis in '
                 'China — and the meta-analysis in the science section belongs '
                 'to it.'],
            ],
            prep='The WHO monograph gives a maximum daily dose of 6–15 g of '
                 'dried root, standardised for paeoniflorin. The TGP capsules '
                 'used in China are a prescription drug. **Not in pregnancy;** '
                 'not recommended in lactation or in children either.',
            science='Peony root’s strongest evidence belongs to its '
                    'extract licensed in China. A systematic review and '
                    'meta-analysis published in 2021 in BMC Complementary '
                    'Medicine and Therapies pooled 39 studies (3,680 patients) '
                    'examining TGP **added to** standard drugs (methotrexate, '
                    'leflunomide and others) in rheumatoid arthritis, and its '
                    'main finding concerns safety: in the TGP-added groups '
                    'hepatic adverse effects (RR 0.31; 95% CI 0.23–0.41) and '
                    'leukopenia were significantly rarer. So the trials '
                    'measure not whether peony treats the disease but whether '
                    'it can reduce the drugs’ side effects; all were done '
                    'in China and quality varies. The WHO monograph’s 1999 '
                    'verdict of "no clinical data" is now dated for this '
                    'extract, but still holds for the root as a tea. Evidence '
                    'level Limited.',
            safety='**Contraindicated in pregnancy** — the WHO monograph cites '
                   'abortifacient activity on the basis of traditional '
                   'reports. Not recommended in lactation or children for lack '
                   'of data. The monograph has no adverse-reaction '
                   'information; in the TGP meta-analysis the commonest effect '
                   'reported is loose stool and diarrhoea. The monograph also '
                   'relays from Chinese tradition that it is not to be '
                   'combined with three plants (below). The wild peonies of '
                   'Turkey are not covered by this monograph and their roots '
                   'should not be dug from the wild.',
            fact='One of Chinese medicine’s most basic drugs has no '
                 'official place in Europe: in 2015 the European Medicines '
                 'Agency issued a public statement instead of a monograph. Yet '
                 'an extract of the same root is a licensed rheumatoid '
                 'arthritis drug in China with a 39-study meta-analysis. A '
                 'plant’s "official" status changes with the continent — '
                 'and the peony grown for show in Turkish gardens and the '
                 'báisháo in a Chinese pharmacy are different species of one '
                 'genus.',
            season='Large white-pink flowers in late spring; the root is '
                   'lifted in autumn from 4–5-year-old plants.',
            habitat='Native to northern China, Mongolia and Siberia; widely '
                    'cultivated in China. An ornamental in Turkey.',
            local='Şakayık, beyaz şakayık; Chinese báisháo.',
            confusion='⚠️ The wild peonies of Turkey (Paeonia mascula, P. '
                      'peregrina, P. tenuifolia) are separate species, some '
                      'protected; the monograph is for P. lactiflora only. '
                      '"Red peony root" (chìsháo) is the unprocessed root of the '
                      'same species or P. veitchii, a separate drug in Chinese '
                      'medicine.',
        ),
        etk_en=[
            ['Fritillaria, Cuscuta and rhubarb (Rheum officinale)',
             'The WHO monograph, citing the Chinese pharmacopoeia, relays that '
             'peony root should not be combined with these three drugs — a '
             'traditional incompatibility rule, not pharmacological '
             'interaction data.'],
            ['Anticoagulants (theoretical)',
             'The monograph lists "anticoagulant" among traditional uses; a '
             'theoretical note of overlap for anyone on a blood thinner.'],
        ],
    ),

    dict(
        yayin='2026-11-19',
        id='yilankoku',
        foto='',
        tr='Yılankökü',
        la='Rauvolfia serpentina (L.) Benth. ex Kurz',
        fam='Apocynaceae (zakkumgiller)',
        diger='Türkçe yılankökü, Hint yılankökü; İngilizce rauwolfia, Indian '
              'snakeroot; Hintçe sarpagandha. DSÖ monografı droğu "Radix '
              'Rauwolfiae" — kurutulmuş kök — diye tanımlıyor. TİTCK ve AB '
              'monografı yok. Modern tansiyon ilacı **reserpinin** kaynağı; '
              'bu yüzden kataloğumuzdaki en "ilaç gibi" bitki.',
        bolge=['asya'],
        kat=['sifa', 'zehir'],
        kisim='Kurutulmuş kökü',
        taxon='Rauvolfia serpentina',
        kul=[
            ['DSÖ monografı (1999)', '"Klinik veriyle desteklenen kullanım": '
             'hafif esansiyel hipertansiyon — genellikle sıvı tutulumunu '
             'önlemek için bir diüretikle birlikte. Farmakopelerde: sinir ve '
             'ruh hastalıklarında sakinleştirici. Monografın kontrendikasyon ve '
             'uyarı bölümleri bir reçeteli ilacınki kadar uzun: **depresyon '
             'öyküsü (özellikle intihar eğilimi), MAO inhibitörü tedavisi, '
             'aktif peptik ülser, sinüs düğümü bozuklukları, ülseratif kolit, '
             'epilepsi, böbrek yetmezliği, elektrokonvülsif tedavi.**'],
            ['Türkiye', 'TİTCK Tıbbi Bitki Listesi’nde yılankökü yok; '
             'Türkiye’de yetişmiyor ve aktarlarda bulunmaz. Reserpin içeren '
             'ilaçlar Türkiye’de de yıllarca tansiyon tedavisinde kullanıldı; '
             'bugün yerini yeni ilaç sınıflarına bıraktı.'],
            ['Hindistan — sarpagandha', 'Ayurveda’nın yılan ısırığı, '
             'uykusuzluk ve "delilik" bitkisi; adı Sanskritçe sarpagandha '
             '(yılan kokusu). 1950’lerde kökünden ayrılan reserpin, modern '
             'tıbbın ilk etkili tansiyon ve antipsikotik ilaçlarından oldu — '
             've bir bitkinin sentetik olmayan tek bir maddeyle ilaç rafına '
             'girmesinin ders kitabı örneği.'],
        ],
        haz='Bu kayıt kullanım için doz vermiyor: DSÖ monografındaki dozlar '
            '(toz drog günde 200 mg, idame 50–300 mg; reserpin alkaloitlerine '
            'göre ayarlanarak, en az on günlük aralıklarla küçük artışlarla) '
            'hekim gözetiminde kullanılan bir ilacın dozlarıdır. Yılankökü '
            'kendi başına kullanılacak bir bitki değildir; aktar ya da takviye '
            'ürünü olarak alınmamalıdır.',
        bilim='Yılankökü, kataloğumuzda bitkiden ilaca geçişin en net örneği: '
              'kökündeki reserpin ruhsatlı bir tansiyon ilacı. 2016 Cochrane '
              'derlemesi reserpinin birincil hipertansiyondaki etkisini '
              'inceledi: 237 katılımcılı dört randomize çalışmada reserpin '
              'plaseboya göre sistolik kan basıncını anlamlı ölçüde düşürdü ve '
              'yazarlar etkiyi "kabaca öteki birinci basamak tansiyon ilaçları '
              'kadar" diye niteledi; ama çalışma sayısı az olduğu için '
              'doz-yanıt ilişkisi ve doza bağlı güvenlik profili '
              'belirlenemedi. DSÖ monografı da hipertansiyonu "klinik veriyle '
              'desteklenen" tek kullanım sayıyor. Kanıt düzeyini "klinik" '
              'yazıyoruz — ama bu kanıt bitkinin çayına değil, kökünden '
              'ayrılmış ve dozu ayarlanmış alkaloide aittir. Bitkinin kendisi '
              'için aynı sonuç geçerli değildir: alkaloit içeriği kökten köke '
              'değişir ve dozlanamaz.',
        kanit='klinik',
        guv='dusuk',
        guvNot='**Depresyona yol açabilir** — DSÖ monografının en ağır uyarısı: '
               'ilaç kaynaklı depresyon kesildikten sonra aylarca sürebilir ve '
               'intiharla sonuçlanacak kadar ağır olabilir; depresyon belirtisi '
               '(çökkünlük, sabah erken uyanma, iştahsızlık, cinsel isteksizlik, '
               'kendini küçümseme) başlar başlamaz kesilmeli. **Depresyon '
               'öyküsü olanlarda, MAO inhibitörü kullananlarda, aktif ülserde, '
               'sinüs düğümü bozukluklarında, ülseratif kolitte, epilepside ve '
               'böbrek yetmezliğinde kontrendike.** Uyanıklığı azaltır; araç '
               've makine kullanımı sakıncalıdır. Bradikardi ve aritmi '
               '(özellikle digoksin ya da kinidinle birlikte), burun '
               'tıkanıklığı, ödem, mide salgısında artış bildirilmiş. Gebelikte '
               've emzirirken kullanılmaz. Güvenlik düzeyi "düşük": bu bir '
               'bitki değil, bitki biçiminde bir ilaçtır.',
        etk=[
            ['Digoksin ve kinidin',
             'DSÖ monografı birlikte kullanımda bradikardi ve aritmi riskinin '
             'arttığını yazıyor.'],
            ['MAO inhibitörleri',
             'Monografın kontrendikasyonu: MAO inhibitörü tedavisi sırasında '
             've hemen sonrasında kullanılmaz.'],
            ['Alkol ve merkezi sinir sistemi depresanları, antihipertansifler, '
             'diüretikler',
             'Monograf bunların yılankökünün etkisini güçlendirebileceğini '
             'yazıyor: sedasyon derinleşir, kan basıncı fazla düşer.'],
            ['Levodopa ve trisiklik antidepresanlar',
             'Reserpin beyinde monoaminleri boşalttığı için antidepresanların '
             've Parkinson ilaçlarının etkisiyle çatışır; monograf etkileşim '
             'listesinde sayıyor.'],
        ],
        ilginc='Bir bitki kökünden, ilaç tarihinin en önemli maddelerinden biri '
               'çıktı: reserpin, 1950’lerde hem ilk etkili tansiyon ilaçlarından '
               'hem de ilk antipsikotiklerden biri oldu ve beyinde '
               'nörotransmitterlerin nasıl depolandığını anlamanın kapısını '
               'açtı. DSÖ monografı bu yüzden yılankökünü bir çay bitkisi gibi '
               'değil, bir reçeteli ilaç gibi yazıyor: iki sayfa '
               'kontrendikasyon, depresyon ve intihar uyarısı, on günlük doz '
               'ayarlama aralıkları. Kataloğumuzda "doğal" ile "zararsız" '
               'arasındaki mesafenin en uzun olduğu kayıt.',
        ek=dict(
            mevsim='Yaz başında beyaz-pembe çiçek demetleri; kök 3–4 yıllık '
                   'bitkilerden sonbaharda sökülür.',
            yetisme='Hindistan, Bangladeş, Sri Lanka ve Güneydoğu Asya’nın '
                    'nemli ormanları; aşırı toplama nedeniyle doğada azalmış, '
                    'CITES Ek II’de. Türkiye’de yetişmiyor.',
            yoresel='Yılankökü, Hint yılankökü; Sanskritçe sarpagandha, Hintçe '
                    'chandrika.',
            karisma='Aynı cinsin Afrika türü (Rauvolfia vomitoria) de '
                    'reserpin kaynağıdır; "yılankökü" adı Türkçede başka '
                    'bitkiler (Polygala senega gibi) için de kullanılıyor. '
                    'Hiçbiri kendi başına kullanılacak bitki değildir.',
        ),
        ema=[],
        kaynak=[
            ['S. D. Shamon ve ark., “Blood pressure-lowering efficacy of '
             'reserpine for primary hypertension”, Cochrane Database of '
             'Systematic Reviews 2016(12), CD007655',
             'https://pubmed.ncbi.nlm.nih.gov/27997978/'],
            ['Radix Rauwolfiae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 1, 1999', who_url(1, 'radix-rauwolfiae')],
        ],
        rel=['alic', 'kediotu', 'zeytin'],
        en=dict(
            name='Indian snakeroot',
            other='Turkish yılankökü, Hint yılankökü; English rauwolfia, '
                  'Indian snakeroot; Hindi sarpagandha. The WHO monograph '
                  'defines the drug as "Radix Rauwolfiae" — the dried root. No '
                  'Turkish or EU monograph. The source of the modern '
                  'blood-pressure drug **reserpine**; hence the most '
                  '"drug-like" plant in this catalog.',
            part='The dried root',
            uses=[
                ['WHO monograph (1999)', '"Uses supported by clinical data": '
                 'mild essential hypertension — usually with a diuretic to '
                 'prevent fluid retention. In pharmacopoeias: a tranquilliser '
                 'in nervous and mental disorders. The monograph’s '
                 'contraindication and warning sections are as long as a '
                 'prescription drug’s: **history of depression (especially '
                 'with suicidal tendency), MAO-inhibitor therapy, active peptic '
                 'ulcer, sinus-node disorders, ulcerative colitis, epilepsy, '
                 'reduced renal function, electroconvulsive therapy.**'],
                ['Turkey', 'Snakeroot is not on the Turkish list; it does not '
                 'grow in Turkey and is not found at herbalists. Drugs '
                 'containing reserpine were used for years in Turkey too for '
                 'hypertension; today they have given way to newer drug '
                 'classes.'],
                ['India — sarpagandha', 'Ayurveda’s plant for snakebite, '
                 'insomnia and "madness"; its name is Sanskrit sarpagandha '
                 '(snake scent). Reserpine, isolated from its root in the '
                 '1950s, became one of modern medicine’s first effective '
                 'blood-pressure and antipsychotic drugs — the textbook case '
                 'of a plant reaching the pharmacy shelf through a single '
                 'unsynthesised substance.'],
            ],
            prep='This record gives no dose for use: the doses in the WHO '
                 'monograph (powdered drug 200 mg daily, maintenance 50–300 '
                 'mg; adjusted by reserpine alkaloid content in small '
                 'increments at intervals of at least ten days) are those of '
                 'a drug used under medical supervision. Snakeroot is not a '
                 'plant to use on one’s own and should not be bought as a '
                 'herbalist’s or supplement product.',
            science='Snakeroot is the clearest example in this catalog of the '
                    'passage from plant to drug: the reserpine in its root is '
                    'a licensed antihypertensive. The 2016 Cochrane review '
                    'examined reserpine’s effect in primary hypertension: '
                    'in four randomised trials with 237 participants reserpine '
                    'lowered systolic blood pressure significantly against '
                    'placebo, and the authors judged the effect "roughly to '
                    'the same degree as other first-line antihypertensive '
                    'drugs"; but with so few trials the dose-response pattern '
                    'and dose-related safety profile could not be established. '
                    'The WHO monograph likewise counts hypertension as the sole '
                    '"use supported by clinical data". We record the evidence '
                    'level as Clinical — but that evidence belongs not to a '
                    'tea of the plant but to the alkaloid isolated from its '
                    'root and dosed. The same conclusion does not hold for the '
                    'plant itself: alkaloid content varies from root to root '
                    'and cannot be dosed.',
            safety='**It can cause depression** — the WHO monograph’s '
                   'gravest warning: drug-induced depression may persist for '
                   'months after withdrawal and be severe enough to result in '
                   'suicide; it must be stopped at the first sign of '
                   'depression (despondency, early-morning insomnia, loss of '
                   'appetite, impotence, self-deprecation). **Contraindicated '
                   'with a history of depression, during MAO-inhibitor '
                   'therapy, in active ulcer, sinus-node disorders, ulcerative '
                   'colitis, epilepsy and renal insufficiency.** It impairs '
                   'alertness; driving and operating machinery are inadvisable. '
                   'Bradycardia and arrhythmia (especially with digoxin or '
                   'quinidine), nasal congestion, oedema and increased gastric '
                   'secretion have been reported. Not in pregnancy or '
                   'lactation. Safety level Low: this is not a plant but a '
                   'drug in the shape of a plant.',
            fact='From one plant root came one of the most important '
                 'substances in the history of medicine: in the 1950s '
                 'reserpine became both one of the first effective '
                 'blood-pressure drugs and one of the first antipsychotics, '
                 'and opened the door to understanding how the brain stores '
                 'neurotransmitters. That is why the WHO monograph writes '
                 'snakeroot not like a tea plant but like a prescription drug: '
                 'two pages of contraindications, a depression and suicide '
                 'warning, ten-day dose-adjustment intervals. The record in '
                 'this catalog where the distance between "natural" and '
                 '"harmless" is longest.',
            season='White-pink flower clusters in early summer; the root is '
                   'lifted in autumn from 3–4-year-old plants.',
            habitat='Humid forests of India, Bangladesh, Sri Lanka and '
                    'Southeast Asia; depleted in the wild by over-collection, '
                    'listed in CITES Appendix II. It does not grow in Turkey.',
            local='Yılankökü, Hint yılankökü; Sanskrit sarpagandha, Hindi '
                  'chandrika.',
            confusion='The African species of the same genus (Rauvolfia '
                      'vomitoria) is also a reserpine source; the Turkish name '
                      '"yılankökü" (snakeroot) is used for other plants too '
                      '(such as Polygala senega). None is a plant to use on '
                      'one’s own.',
        ),
        etk_en=[
            ['Digoxin and quinidine',
             'The WHO monograph states the risk of bradycardia and arrhythmia '
             'rises with concurrent use.'],
            ['MAO inhibitors',
             'The monograph’s contraindication: not during or shortly '
             'after MAO-inhibitor therapy.'],
            ['Alcohol and CNS depressants, antihypertensives, diuretics',
             'The monograph states these may potentiate snakeroot: sedation '
             'deepens, blood pressure falls too far.'],
            ['Levodopa and tricyclic antidepressants',
             'Because reserpine depletes monoamines in the brain it works '
             'against antidepressants and Parkinson’s drugs; the monograph '
             'lists them among interactions.'],
        ],
    ),

]
