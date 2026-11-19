# WHO monografı partisi IV (26–28 Kasım 2026): Baykal takke otu, beş tat
# meyvesi, Çin yüksükotu. Üçü de Doğu Asya'nın büyük geleneksel drogları;
# DSÖ Cilt 3 (2007) üçünde de "klinik veriyle desteklenen kullanım: yok"
# diyor. Türkçe adları yok; başlıklar çeviri ve öyle olduğu yazıldı.
from kunye_elle import who_url
Q = [

    dict(
        yayin='2026-11-25',
        id='baykaltakkesi',
        foto='',
        tr='Baykal takke otu',
        la='Scutellaria baicalensis Georgi',
        fam='Lamiaceae (ballıbabagiller)',
        diger='Türkçe yerleşik adı yok; "Baykal takke otu" İngilizce Baikal '
              'skullcap adının karşılığıdır (Scutellaria cinsine Türkçede takke '
              'otu / kaside otu denir). Çince huáng qín ("sarı altın"), Japonca '
              'ōgon. Sinonimleri S. grandiflora Adams, S. lanceolaria Miq., S. '
              'macrantha Fisch. TİTCK ve AB monografı yok; kayıt DSÖ monografına '
              '(Cilt 3, 2007) ve PubMed’e dayanıyor.',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Kurutulmuş kökleri',
        taxon='Scutellaria baicalensis',
        kul=[
            ['DSÖ monografı — kök', 'Dünya Sağlık Örgütü monografı (Cilt 3, '
             '2007): **klinik veriyle desteklenen kullanım yok** — olgu '
             'bildirimleri bağışıklığı uyardığını düşündürse de kontrollü '
             'çalışma verisi eksik. Farmakopelerde tanımlanan kullanım: ateş, '
             'bulantı ve kusma, akut dizanteri, sarılık, öksürük, çıban ve '
             'yaralar, düşük tehdidi. Geleneksel tıpta: alerji, ateroskleroz, '
             'ishal, dermatit, hipertansiyon. Günlük doz 3–9 g kök, infüzyon ya '
             'da dekoksiyon.'],
            ['Türkiye', 'TİTCK Tıbbi Bitki Listesi’nde bu bitki için monograf '
             'yok; Türkiye’de yetişmiyor. Anadolu’da Scutellaria cinsinin yerli '
             'türleri (S. orientalis, S. salviifolia) bulunur ama onlar ayrı '
             'türlerdir ve bu monografın kapsamında değildir.'],
            ['Çin — huáng qín', 'Çin tıbbının en eski "ısı temizleyen" acı-soğuk '
             'droglarından; Shennong Bencao Jing’de yer alır. Sarı kökü '
             'baikalin, baikalein ve wogonin adlı flavonları taşır; bugün Çin’de '
             'yüzlerce bileşik formülün (Tanreqing enjeksiyonu dahil) '
             'bileşenidir.'],
        ],
        haz='DSÖ monografı günlük doz olarak 3–9 g kurutulmuş kök veriyor, '
            'infüzyon ya da dekoksiyon. Kök, özüt, infüzyon ve dekoksiyon '
            'biçimleri. **Gebelikte, emzirirken ve 12 yaş altında '
            'kontrendike.**',
        bilim='Baykal takke otunun tek başına, monograf endikasyonunda sınandığı '
              'bir klinik çalışma yok. Son yıllardaki insan çalışmaları hep '
              'karışımlarla: 2025’te Journal of Psychopharmacology dergisinde '
              'takke otu + alıç + magnezyum + krom karışımı stresli kişilerde; '
              'Nutritional Neuroscience dergisinde Acacia catechu ile birleşik '
              'özüt bilişsel işlevde; Nutrients dergisinde safranla birleşik '
              'özüt depresif belirtilerde. Hepsi karışımı ölçüyor, takke otunu '
              'değil. Çin’deki çalışmalar ise çok bileşenli formüllerle '
              '(Tanreqing enjeksiyonu için 2024 meta-analizi gibi). DSÖ '
              'monografı 2007’de "kontrollü çalışma verisi eksik" demişti; '
              'tek bileşenli kanıt açısından durum değişmedi. Kanıt düzeyi '
              '"geleneksel".',
        kanit='geleneksel',
        guv='orta',
        guvNot='**Gebelikte, emzirirken ve 12 yaş altında kontrendike** — DSÖ '
               'monografı olası teratojen ve mutajen etkiler ile veri yokluğu '
               'nedeniyle. Monograf hayvan verisindeki çelişkiyi de aktarıyor: '
               'bir çalışmada sulu özüt gebe sıçanlarda teratojen bulunmuş, '
               'başka bir çalışmada metanol özütü bulunmamış. Ağızdan kullanımda '
               'seyrek mide-bağırsak rahatsızlığı ve ishal bildirilmiş. '
               '**Karaciğer:** monograf kökün karaciğer hasarı yapabileceğinin '
               'öne sürüldüğünü, ama yayımlanmış olgularla doğrudan bağ '
               'kurulamadığını yazıyor; takke otu içeren karışımlar için '
               'sonradan bildirilen karaciğer olguları nedeniyle, kullanırken '
               'sarılık ya da koyu idrar görülürse bırakıp hekime gidilmeli. '
               'Etkileşim verisi yok.',
        etk=[
            ['DSÖ: etkileşim verisi yok',
             'Monograf ilaç etkileşimleri konusunda bilgi bulunmadığını '
             'yazıyor. Flavonlarının laboratuvarda CYP enzimlerini etkilediği '
             'bilindiğinden, düzenli ilaç kullananların hekimine söylemesi '
             'kuramsal olarak doğrudur.'],
            ['Karışım ürünleri',
             'Takke otu Batı’da neredeyse hiç tek başına satılmıyor; '
             'çalışmaların tamamı karışımlarla. Bir karışımın verisi bu '
             'bitkiye ait sayılamaz.'],
        ],
        ilginc='Türkçede bu bitkinin adı yok ama cinsinin var: Anadolu’da '
               'yetişen yerli Scutellaria türlerine takke otu ya da kaside otu '
               'denir — çiçeğin takkeye benzeyen çanağından. Çin tıbbının '
               'binlerce yıllık "sarı altın"ı bu yüzden Türkçeye bir akrabasının '
               'adıyla girebiliyor. Ama kanıt tarafında durum tersine: DSÖ '
               '2007’de "kontrollü çalışma yok" dedi ve o günden beri yapılan '
               'bütün insan çalışmaları başka bitkilerle karışık. Bir bitkinin '
               'iki bin yıllık kullanımı ile tek başına sınanmış olmaması aynı '
               'anda doğru olabiliyor.',
        ek=dict(
            mevsim='Yazın mavi-mor takke biçimli çiçekler; kökler sonbaharda '
                   'ya da ilkbaharda sökülür, kurutulunca sarıdır.',
            yetisme='Kore Yarımadası, Çin, Japonya, Moğolistan ve Rusya; kuru '
                    'yamaçlar. Türkiye’de yetişmiyor.',
            yoresel='Türkçe adı yok; Çince huáng qín, Japonca ōgon.',
            karisma='⚠️ Amerikan takke otu (Scutellaria lateriflora) ayrı tür, '
                    'ayrı gelenek (sinir yatıştırıcı); ikisi "skullcap" adıyla '
                    'karışır ve ürünlerde birbirinin yerine geçebilir. '
                    'Anadolu’nun yerli takke otları da bu monografın kapsamında '
                    'değildir.',
        ),
        ema=[],
        kaynak=[
            ['F. Dodd ve ark., “Effects of a Scutellaria baicalensis/Crataegus '
             'laevigata, magnesium and chromium supplement on stressed '
             'individuals: A randomised, double-blind, placebo-controlled '
             'trial”, Journal of Psychopharmacology 39(12), 2025',
             'https://pubmed.ncbi.nlm.nih.gov/41194549/'],
            ['Radix Scutellariae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 3, 2007', who_url(3, 'radix-scutellariae')],
        ],
        rel=['ginseng', 'melisa', 'kediotu'],
        en=dict(
            name='Baikal skullcap',
            other='No established Turkish name; "Baykal takke otu" renders the '
                  'English Baikal skullcap (the genus Scutellaria is called takke '
                  'otu, "cap herb", in Turkish). Chinese huáng qín ("yellow '
                  'gold"), Japanese ōgon. Synonyms S. grandiflora Adams, S. '
                  'lanceolaria Miq., S. macrantha Fisch. No Turkish or EU '
                  'monograph; the record rests on the WHO monograph (Vol. 3, '
                  '2007) and PubMed.',
            part='The dried roots',
            uses=[
                ['WHO monograph — the root', 'The World Health Organization '
                 'monograph (Vol. 3, 2007): **no use supported by clinical '
                 'data** — case reports suggest immune stimulation, but data '
                 'from controlled trials are lacking. Uses described in '
                 'pharmacopoeias: fever, nausea and vomiting, acute dysentery, '
                 'jaundice, cough, carbuncles and sores, threatened abortion. '
                 'In traditional medicine: allergies, arteriosclerosis, '
                 'diarrhoea, dermatitis, hypertension. Daily dose 3–9 g of '
                 'root as infusion or decoction.'],
                ['Turkey', 'There is no monograph for this plant on the Turkish '
                 'list; it does not grow in Turkey. Native Scutellaria species '
                 '(S. orientalis, S. salviifolia) occur in Anatolia, but they '
                 'are different species outside this monograph.'],
                ['China — huáng qín', 'One of the oldest "heat-clearing" '
                 'bitter-cold drugs of Chinese medicine, listed in the Shennong '
                 'Bencao Jing. Its yellow root carries the flavones baicalin, '
                 'baicalein and wogonin; today it is an ingredient of hundreds '
                 'of compound formulas in China (including Tanreqing '
                 'injection).'],
            ],
            prep='The WHO monograph gives a daily dose of 3–9 g of dried root as '
                 'infusion or decoction. Root, extracts, infusions and '
                 'decoctions. **Contraindicated in pregnancy, lactation and '
                 'under 12.**',
            science='There is no clinical trial of Baikal skullcap alone in the '
                    'monograph indication. Recent human studies all use '
                    'mixtures: in 2025, in the Journal of Psychopharmacology, '
                    'skullcap + hawthorn + magnesium + chromium in stressed '
                    'people; in Nutritional Neuroscience, a combined extract '
                    'with Acacia catechu for cognition; in Nutrients, a '
                    'combination with saffron for depressive symptoms. All '
                    'measure the mixture, not the skullcap. The Chinese trials '
                    'use multi-herb formulas (such as the 2024 meta-analysis of '
                    'Tanreqing injection). The WHO monograph said in 2007 that '
                    'controlled-trial data were lacking; for single-ingredient '
                    'evidence nothing has changed. Evidence level Traditional.',
            safety='**Contraindicated in pregnancy, lactation and under 12** — '
                   'the WHO monograph, owing to possible teratogenic and '
                   'mutagenic effects and lack of data. The monograph also '
                   'reports the conflict in animal data: in one study an '
                   'aqueous extract was teratogenic in pregnant rats, in '
                   'another a methanol extract was not. Rare gastrointestinal '
                   'discomfort and diarrhoea have been reported with oral use. '
                   '**Liver:** the monograph writes that liver damage from the '
                   'root has been suggested but no direct link to published '
                   'cases established; given liver cases later reported with '
                   'skullcap-containing mixtures, anyone developing jaundice or '
                   'dark urine while using it should stop and see a doctor. No '
                   'interaction data.',
            fact='Turkish has no name for this plant but has one for its genus: '
                 'the native Scutellaria species of Anatolia are called takke '
                 'otu or kaside otu — from the cap-shaped calyx of the flower. '
                 'That is how the "yellow gold" of two thousand years of Chinese '
                 'medicine can enter Turkish under a relative’s name. On the '
                 'evidence side the situation is reversed: the WHO said "no '
                 'controlled trials" in 2007, and every human trial since has '
                 'mixed it with other plants. Two thousand years of use and '
                 'never having been tested alone can both be true at once.',
            season='Blue-purple cap-shaped flowers in summer; the roots are '
                   'lifted in autumn or spring and are yellow when dried.',
            habitat='The Korean peninsula, China, Japan, Mongolia and Russia; '
                    'dry slopes. It does not grow in Turkey.',
            local='No Turkish name; Chinese huáng qín, Japanese ōgon.',
            confusion='⚠️ American skullcap (Scutellaria lateriflora) is a '
                      'different species with a different tradition (a nervine); '
                      'the two are confused under the name "skullcap" and may '
                      'substitute for each other in products. The native '
                      'skullcaps of Anatolia are also outside this monograph.',
        ),
        etk_en=[
            ['WHO: no interaction data',
             'The monograph states that no information is available on drug '
             'interactions. Because its flavones are known to affect CYP '
             'enzymes in the laboratory, it is theoretically right for anyone '
             'on regular medication to tell their doctor.'],
            ['Mixture products',
             'Skullcap is almost never sold alone in the West; all the trials '
             'use mixtures. A mixture’s data cannot be attributed to this '
             'plant.'],
        ],
    ),

    dict(
        yayin='2026-11-26',
        id='bestatmeyvesi',
        foto='',
        tr='Beş tat meyvesi',
        la='Schisandra chinensis (Turcz.) Baill.',
        fam='Schisandraceae (şisandragiller)',
        diger='Türkçe yerleşik adı yok; takviye pazarında "şisandra" ya da '
              '"beş tat meyvesi" diye geçer — Çince wǔ wèi zi ("beş tat '
              'tohumu") adının çevirisi: meyvenin tatlı, ekşi, acı, tuzlu ve '
              'keskin tatları bir arada taşıdığı söylenir. Korece omija. '
              'Sinonimleri Kadsura chinensis Turcz., Maximowiczia chinensis '
              'Rupr. TİTCK ve AB monografı yok; kayıt DSÖ monografına (Cilt 3, '
              '2007) ve PubMed’e dayanıyor.',
        bolge=['asya'],
        kat=['sifa', 'besin'],
        kisim='Kurutulmuş olgun meyveleri',
        taxon='Schisandra chinensis',
        kul=[
            ['DSÖ monografı — meyve', 'Dünya Sağlık Örgütü monografı (Cilt 3, '
             '2007): **klinik veriyle desteklenen kullanım yok** — psikoz, '
             'gastrit, hepatit ve yorgunlukta bazı klinik kanıtlar olsa da '
             'kontrollü çalışma eksik. Farmakopelerde tanımlanan kullanım: '
             'kronik öksürük ve astım, diyabet, idrar yolu bozuklukları; '
             'hastalığa bağlı yorgunlukta genel tonik. Geleneksel tıpta: '
             'büzücü, öksürük kesici, ishal kesici, balgam söktürücü, '
             'yatıştırıcı. Günlük 1,5–6 g kuru meyve.'],
            ['Türkiye', 'TİTCK Tıbbi Bitki Listesi’nde bu bitki için monograf '
             'yok; Türkiye’de yetişmiyor. Adaptojen takviyesi olarak ithal '
             'kapsül ve meyve hâlinde satılıyor.'],
            ['Kore ve Çin — omija çayı', 'Kore’de omija (beş tat) meyvesinden '
             'soğuk çay ve şurup yapılır; Çin tıbbında ciğer ve böbrek '
             'tonikidir. 20. yüzyılda Sovyet araştırmacıları Sibirya ginsengiyle '
             'birlikte "adaptojen" olarak inceledi; Batı pazarındaki ünü '
             'buradan geliyor.'],
        ],
        haz='DSÖ monografı ortalama günlük doz olarak 1,5–6,0 g kuru meyve '
            'veriyor. **Yatmadan önce alınmamalı** (uykusuzluk yapabilir); '
            'sakinleştirici ilaçlarla ve alkolle birlikte kullanılmamalı. '
            'Gebelikte kullanılmamalı.',
        bilim='Beş tat meyvesinin monograf endikasyonlarında kanıtı yok, ama '
              'tek bileşenli, plasebo kontrollü iki randomize çalışma var — '
              'ikisi de başka alanlarda. 2016’da Climacteric dergisinde '
              'yayımlanan çift kör çalışma 36 menopoz dönemindeki kadında 6 '
              'haftalık standardize özütün Kupperman indeksini plaseboya göre '
              'anlamlı düşürdüğünü bildirdi (p=0,042) — özellikle sıcak '
              'basması, terleme ve çarpıntıda; 36 kişi, tek merkez. 2021’de '
              'American Journal of Clinical Nutrition dergisinde yayımlanan '
              'çift kör çalışma 50 yaş üstü 54 kişide 12 hafta günde 1 g özüt '
              '+ hafif yürüyüşün diz ekstansör kas gücünü plaseboya göre '
              'artırdığını (sağ 10,2 Nm; %95 GA 3,7–16,8), ama **kas '
              'kütlesinde, iltihap ve antioksidan belirteçlerinde ve yaşam '
              'kalitesinde fark olmadığını** buldu; yan etki yok. İki küçük '
              'çalışma, iki ayrı sonlanım, ikisi de monograf dışı — kanıt '
              'düzeyi "sınırlı". Monografın "yorgunlukta tonik" endikasyonunu '
              'doğrudan sınayan çalışma yok.',
        kanit='sinirli',
        guv='orta',
        guvNot='**Doz aşımında huzursuzluk, uykusuzluk ve nefes darlığı** — DSÖ '
               'monografının uyarısı. **Gebelikte kullanılmamalı:** monograf, '
               'tentürün gebelere verildiği kontrolsüz bir çalışmada ikinci '
               'dozdan sonra doğumun başladığını ve tavşanlarda rahim '
               'kasılmalarının arttığını aktarıyor — bitki rahmi uyarıyor. Mide '
               'ekşimesi, mide ağrısı, iştahsızlık, alerjik deri tepkileri ve '
               'ürtiker bildirilmiş. Monograf kontrendikasyon vermiyor; ama '
               'etkileşim bölümü (aşağıda) kataloğumuzdaki en kapsamlılardan.',
        etk=[
            ['Sakinleştirici ilaçlar ve alkol',
             'DSÖ monografı meyvenin merkezi sinir sistemini baskılayıcı '
             'etkisi olabileceğini ve sedatiflerle ya da alkolle birlikte '
             'kullanılmaması gerektiğini yazıyor.'],
            ['CYP450 ile metabolize olan ilaçlar — siklosporin, varfarin, '
             'proteaz inhibitörleri, hormonlar',
             'Monografın en önemli satırı: meyve karaciğerde sitokrom P450 '
             'etkinliğini **uyarıyor** (faz I ve II enzimlerini indükliyor). '
             'Bildirilmiş etkileşim olmasa da, bu enzimlerle işlenen ilaçların '
             '— siklosporin, varfarin, HIV proteaz inhibitörleri, östrojen-'
             'progesteron birleşimleri — düzeyini düşürebilir; monograf '
             'birlikte kullanımı ancak hekim gözetiminde uygun görüyor. '
             'Sarı kantaronla aynı mantık ve aynı liste.'],
        ],
        ilginc='Adı bir tat deneyidir: Çince wǔ wèi zi, "beş tat tohumu" — '
               'tatlı, ekşi, acı, tuzlu ve keskin tatları tek meyvede '
               'taşıdığına inanılır. DSÖ monografındaki en dikkat çekici bulgu '
               'ise tat değil enzim: bitki karaciğerin ilaç işleyen enzimlerini '
               'sarı kantaron gibi uyarıyor ve monograf, "bildirilmiş '
               'etkileşim yok" demesine rağmen varfarinden siklosporine uzanan '
               'bir listeyi hekim gözetimine bağlıyor. Takviye rafında '
               '"adaptojen" diye satılan meyvenin arkasında, doğum başlatan '
               'tentür ve enzim indükleyen lignanlar var.',
        ek=dict(
            mevsim='Sonbaharda parlak kırmızı üzümsü salkımlar; meyve olgunken '
                   'toplanıp kurutulur.',
            yetisme='Rusya’nın Uzak Doğusu, Kuzeydoğu Çin, Kore, Japonya; nemli '
                    'ormanlarda tırmanıcı. Çin ve Kore’de kültürü yapılıyor. '
                    'Türkiye’de yetişmiyor.',
            yoresel='Türkçe adı yok; Çince wǔ wèi zi, Korece omija.',
            karisma='Güney şisandrası (Schisandra sphenanthera) Çin '
                    'farmakopesinde ayrı bir drogdur ve ürünlerde S. chinensis '
                    'yerine geçebilir; monograf yalnızca S. chinensis içindir.',
        ),
        ema=[],
        kaynak=[
            ['J. Y. Park ve K. H. Kim, “A randomized, double-blind, '
             'placebo-controlled trial of Schisandra chinensis for menopausal '
             'symptoms”, Climacteric 19(6), 2016',
             'https://pubmed.ncbi.nlm.nih.gov/27763802/'],
            ['Y. H. Cho ve ark., “Effect of Schisandra chinensis Baillon '
             'extracts and regular low-intensity exercise on muscle strength '
             'and mass in older adults: a randomized, double-blind, '
             'placebo-controlled trial”, American Journal of Clinical '
             'Nutrition 113(6), 2021',
             'https://pubmed.ncbi.nlm.nih.gov/33710261/'],
            ['Fructus Schisandrae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 3, 2007', who_url(3, 'fructus-schisandrae')],
        ],
        rel=['sibiryaginsengi', 'ginseng', 'ashwagandha'],
        en=dict(
            name='Schisandra',
            other='No established Turkish name; on the supplement market it goes '
                  'as "şisandra" or "beş tat meyvesi" — a translation of the '
                  'Chinese wǔ wèi zi ("five-flavour seed"): the fruit is said to '
                  'carry sweet, sour, bitter, salty and pungent at once. Korean '
                  'omija. Synonyms Kadsura chinensis Turcz., Maximowiczia '
                  'chinensis Rupr. No Turkish or EU monograph; the record rests '
                  'on the WHO monograph (Vol. 3, 2007) and PubMed.',
            part='The dried ripe fruit',
            uses=[
                ['WHO monograph — the fruit', 'The World Health Organization '
                 'monograph (Vol. 3, 2007): **no use supported by clinical '
                 'data** — some clinical evidence exists for psychosis, '
                 'gastritis, hepatitis and fatigue, but controlled trials are '
                 'lacking. Uses described in pharmacopoeias: chronic cough and '
                 'asthma, diabetes, urinary tract disorders; as a general tonic '
                 'for fatigue associated with illness. In traditional medicine: '
                 'astringent, antitussive, antidiarrhoeal, expectorant, '
                 'sedative. Daily dose 1.5–6 g of dried fruit.'],
                ['Turkey', 'There is no monograph for this plant on the Turkish '
                 'list; it does not grow in Turkey. It is sold as an imported '
                 'adaptogen supplement, in capsules and as dried fruit.'],
                ['Korea and China — omija tea', 'In Korea a cold tea and syrup '
                 'are made from the omija (five-flavour) berry; in Chinese '
                 'medicine it is a liver and kidney tonic. In the 20th century '
                 'Soviet researchers studied it alongside Siberian ginseng as '
                 'an "adaptogen"; its Western reputation comes from there.'],
            ],
            prep='The WHO monograph gives an average daily dose of 1.5–6.0 g of '
                 'dried fruit. **Not before bedtime** (it may cause insomnia); '
                 'not together with sedatives or alcohol. Not in pregnancy.',
            science='There is no evidence for schisandra in the monograph '
                    'indications, but there are two single-ingredient, '
                    'placebo-controlled randomised trials — both in other '
                    'fields. A double-blind trial published in 2016 in '
                    'Climacteric reported that 6 weeks of a standardised extract '
                    'lowered the Kupperman index significantly against placebo '
                    'in 36 menopausal women (p=0.042) — notably for hot flushes, '
                    'sweating and palpitations; 36 people, one centre. A '
                    'double-blind trial published in 2021 in the American Journal '
                    'of Clinical Nutrition found that in 54 adults over 50, 12 '
                    'weeks of 1 g of extract a day plus light walking raised '
                    'knee-extensor strength against placebo (right, 10.2 Nm; 95% '
                    'CI 3.7–16.8), but **no difference in muscle mass, '
                    'inflammatory or antioxidant markers or quality of life**; '
                    'no adverse events. Two small trials, two separate outcomes, '
                    'both outside the monograph — evidence level Limited. No '
                    'trial directly tests the monograph’s "tonic for fatigue" '
                    'indication.',
            safety='**Symptoms of overdose include restlessness, insomnia and '
                   'dyspnoea** — the WHO monograph’s warning. **Not in '
                   'pregnancy:** the monograph reports an uncontrolled study in '
                   'which a tincture given to pregnant women induced labour after '
                   'the second dose, and increased uterine contractions in '
                   'rabbits — the plant stimulates the uterus. Heartburn, '
                   'stomach pain, anorexia, allergic skin reactions and '
                   'urticaria have been reported. The monograph gives no '
                   'contraindications; but its interaction section (below) is '
                   'among the most extensive in this catalog.',
            fact='Its name is a taste experiment: Chinese wǔ wèi zi, '
                 '"five-flavour seed" — believed to carry sweet, sour, bitter, '
                 'salty and pungent in one fruit. The most striking finding in '
                 'the WHO monograph, though, is not taste but enzymes: the plant '
                 'induces the liver’s drug-metabolising enzymes much as St '
                 'John’s wort does, and the monograph, while saying "no '
                 'interactions reported", places a list running from warfarin '
                 'to ciclosporin under medical supervision. Behind the berry '
                 'sold as an "adaptogen" on the supplement shelf stand a '
                 'labour-inducing tincture and enzyme-inducing lignans.',
            season='Bright red grape-like clusters in autumn; the fruit is '
                   'gathered ripe and dried.',
            habitat='The Russian Far East, north-eastern China, Korea, Japan; a '
                    'climber of damp forests. Cultivated in China and Korea. It '
                    'does not grow in Turkey.',
            local='No Turkish name; Chinese wǔ wèi zi, Korean omija.',
            confusion='Southern schisandra (Schisandra sphenanthera) is a '
                      'separate drug in the Chinese pharmacopoeia and can stand '
                      'in for S. chinensis in products; the monograph is for S. '
                      'chinensis only.',
        ),
        etk_en=[
            ['Sedatives and alcohol',
             'The WHO monograph states the fruit may have CNS-depressant '
             'effects and should not be used together with sedatives or '
             'alcohol.'],
            ['Drugs metabolised by CYP450 — ciclosporin, warfarin, protease '
             'inhibitors, hormones',
             'The monograph’s most important line: the fruit **stimulates** '
             'hepatic cytochrome P450 (inducing phase I and II enzymes). Though '
             'no interaction has been reported, it may lower the levels of '
             'drugs processed by those enzymes — ciclosporin, warfarin, HIV '
             'protease inhibitors, oestrogen-progestogen combinations — and the '
             'monograph allows co-administration only under medical '
             'supervision. The same logic and the same list as St John’s '
             'wort.'],
        ],
    ),

    dict(
        yayin='2026-11-27',
        id='cinyuksukotu',
        foto='',
        tr='Çin yüksükotu',
        la='Rehmannia glutinosa Libosch.',
        fam='Orobanchaceae (canavarotugiller; DSÖ eski sınıflamayla '
            'Scrophulariaceae yazıyor)',
        diger='Türkçe yerleşik adı yok; "Çin yüksükotu" İngilizce Chinese '
              'foxglove adının karşılığıdır — çiçeği yüksükotuna benzer ama '
              'yüksükotu değildir ve kalp glikoziti taşımaz. Çince dì huáng '
              '("toprak sarısı"). Sinonimleri Digitalis glutinosa Gaertn., '
              'Rehmannia chinensis Libosch. TİTCK ve AB monografı yok; kayıt DSÖ '
              'monografına (Cilt 3, 2007) ve PubMed’e dayanıyor.',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Kurutulmuş kök ve rizomları',
        taxon='Rehmannia glutinosa',
        kul=[
            ['DSÖ monografı — kök', 'Dünya Sağlık Örgütü monografı (Cilt 3, '
             '2007): **klinik veriyle desteklenen kullanım yok** — romatoid '
             'artrit ve hipertansiyonda olgu bildirimleri var, kontrollü '
             'çalışma eksik. Farmakopelerde tanımlanan kullanım: ateş, diyabet, '
             'hipertansiyon, deri döküntüleri, boğaz ağrısı, aşırı ve sık adet '
             'kanaması; bağışıklığı uyaran tonik. Geleneksel tıpta: spazm '
             'çözücü, idrar söktürücü; yanık, ishal, dizanteri. Günlük 9–15 g '
             'kök.'],
            ['Türkiye', 'TİTCK Tıbbi Bitki Listesi’nde bu bitki için monograf '
             'yok; Türkiye’de yetişmiyor ve Türk takviye pazarında da nadirdir. '
             'Kataloğumuza girmesinin nedeni DSÖ monografı ve Çin tıbbındaki '
             'merkezi yeri.'],
            ['Çin — dì huáng ve Altı Bileşenli Rehmannia', 'Çin tıbbının en '
             'çok kullanılan köklerinden; çiğ (shēng), kurutulmuş ve şarapla '
             'pişirilmiş (shú) biçimleri ayrı droglar sayılır. Dünyaca ünlü '
             '"Liu Wei Di Huang Wan" (Altı Bileşenli Rehmannia Hapı) formülünün '
             'baş bileşenidir — kanıt tartışmasının çoğu da bu formülle ilgili, '
             'bitkiyle değil.'],
        ],
        haz='DSÖ monografı günlük doz olarak 9–15 g kurutulmuş kök ve rizom '
            'veriyor, infüzyon ya da dekoksiyon. **Kronik karaciğer ve '
            'mide-bağırsak hastalığında, ishalde ve gebelikte kontrendike.** '
            'Emzirirken ve çocuklarda hekim gözetimi olmadan önerilmiyor.',
        bilim='Çin yüksükotunun tek başına sınandığı bir klinik çalışma yok; '
              'bütün insan verisi onu baş bileşen yapan çok bileşenli '
              'formüllerden. 2023’te Clinical Journal of the American Society of '
              'Nephrology dergisinde yayımlanan çok merkezli randomize çalışma '
              '(148 hasta, 48 hafta), tip 2 diyabet ve böbrek hastalığında '
              'standart tedaviye eklenen Rehmannia-6 temelli granüllerin eGFR '
              'düşüşünü yılda 2,7 ml/dk yavaşlattığını buldu — ama albüminüride '
              'anlamlı fark yoktu ve çalışma değerlendirici-kör, plasebosuz. '
              '2025’te Saudi Medical Journal dergisinde yayımlanan meta-analiz '
              '(17 RKÇ, 1.139 hasta) meme kanseri hastalarında perimenopozal '
              'belirtilerde Rehmannia’yı "hükümdar drog" yapan formülleri '
              'inceliyor ve yöntem kusurlarını vurguluyor. Her ikisi de '
              'formülü ölçüyor; Rehmannia’nın payı ayrıştırılmış değil. Kanıt '
              'düzeyi "geleneksel".',
        kanit='geleneksel',
        guv='orta',
        guvNot='**Kronik karaciğer ve mide-bağırsak hastalığında ve ishalde '
               'kontrendike** — DSÖ monografı Çin farmakopesinden aktarıyor. '
               '**Gebelikte kontrendike:** farelerde embriyo yerleşimini '
               'engellediği gösterilmiş (olası anti-implantasyon etkisi). '
               'İshal, karın ağrısı, ödem, yorgunluk, baş dönmesi ve çarpıntı '
               'bildirilmiş; monograf bunların geçici olduğunu ve birkaç günde '
               'kaybolduğunu yazıyor. Emzirirken ve çocuklarda hekim gözetimi '
               'olmadan önerilmiyor. Adındaki "yüksükotu" yanıltmasın: kalp '
               'glikoziti taşımaz.',
        etk=[
            ['DSÖ: etkileşim verisi yok',
             'Monograf ilaç etkileşimleri konusunda bilgi bulunmadığını '
             'yazıyor. Kan şekerini etkilediği öne sürülen bir bitki olarak '
             'antidiyabetiklerle üst üste binme kuramsal bir nottur; '
             'diyabet-böbrek çalışmasında hastalar ilaçlarına devam etti ve '
             'ciddi etkileşim bildirilmedi.'],
            ['Formül verisini bitkiye mal etmemek',
             'Rehmannia-6 ve benzeri formüller beş-yedi bitki içerir; '
             'onların sonuçları bu kökün kanıtı sayılamaz.'],
        ],
        ilginc='Adı ile akrabalığı birbirini tutmuyor: "Çin yüksükotu" denir, '
               'eski sınıflamada yüksükotuyla aynı familyaya (Scrophulariaceae) '
               'konmuştu — DSÖ monografı hâlâ öyle yazar — ama modern '
               'sınıflama onu canavarotugillere (Orobanchaceae) taşıdı ve kalp '
               'glikoziti taşımaz. Çin tıbbında ise aynı kökün üç hâli üç ayrı '
               'drogdur: çiğ, kuru ve şarapla pişirilmiş. Bir bitkinin '
               'hazırlanış biçiminin onu başka bir ilaç yapabildiğinin '
               'kataloğumuzdaki en açık örneği.',
        ek=dict(
            mevsim='İlkbaharda mor-kahverengi yüksük biçimli çiçekler; kökler '
                   'sonbaharda sökülür ve ya kurutulur ya da şarapla buharda '
                   'pişirilir.',
            yetisme='Çin kökenli; Çin, Japonya ve Kore’de kültürü yapılıyor. '
                    'Türkiye’de yetişmiyor.',
            yoresel='Türkçe adı yok; Çince dì huáng, shēng dì (çiğ), shú dì '
                    '(pişmiş).',
            karisma='⚠️ Yüksükotu (Digitalis) ile adı ve çiçeği karışır; '
                    'yüksükotu ölümcül kalp glikozitleri taşır, bu bitki '
                    'taşımaz. Çin farmakopesinde çiğ ve pişmiş kök ayrı '
                    'droglardır ve ayrı amaçlarla kullanılır.',
        ),
        ema=[],
        kaynak=[
            ['K. W. Chan ve ark., “Add-on Rehmannia-6-Based Chinese Medicine in '
             'Type 2 Diabetes and CKD: A Multicenter Randomized Controlled '
             'Trial”, Clinical Journal of the American Society of Nephrology '
             '18(9), 2023',
             'https://pubmed.ncbi.nlm.nih.gov/37307005/'],
            ['D. Kong ve ark., “Rehmannia glutinosa for perimenopausal syndrome '
             'in patients with breast cancer: A systematic review and '
             'meta-analysis”, Saudi Medical Journal 46(7), 2025',
             'https://pubmed.ncbi.nlm.nih.gov/40628433/'],
            ['Radix Rehmanniae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 3, 2007', who_url(3, 'radix-rehmanniae')],
        ],
        rel=['yuksukotu', 'ginseng', 'goji'],
        en=dict(
            name='Chinese foxglove',
            other='No established Turkish name; "Çin yüksükotu" renders the '
                  'English Chinese foxglove — its flower resembles foxglove, but '
                  'it is not a foxglove and carries no cardiac glycosides. '
                  'Chinese dì huáng ("earth yellow"). Synonyms Digitalis '
                  'glutinosa Gaertn., Rehmannia chinensis Libosch. No Turkish or '
                  'EU monograph; the record rests on the WHO monograph (Vol. 3, '
                  '2007) and PubMed.',
            part='The dried roots and rhizomes',
            uses=[
                ['WHO monograph — the root', 'The World Health Organization '
                 'monograph (Vol. 3, 2007): **no use supported by clinical '
                 'data** — case reports in rheumatoid arthritis and '
                 'hypertension, controlled trials lacking. Uses described in '
                 'pharmacopoeias: fevers, diabetes, hypertension, skin '
                 'eruptions, sore throat, hypermenorrhoea and polymenorrhoea; a '
                 'tonic to stimulate the immune system. In traditional '
                 'medicine: antispasmodic, diuretic; burns, diarrhoea, '
                 'dysentery. Daily dose 9–15 g of root.'],
                ['Turkey', 'There is no monograph for this plant on the Turkish '
                 'list; it does not grow in Turkey and is rare on the Turkish '
                 'supplement market. It enters this catalog because of the WHO '
                 'monograph and its central place in Chinese medicine.'],
                ['China — dì huáng and Six-Ingredient Rehmannia', 'One of the '
                 'most-used roots of Chinese medicine; its raw (shēng), dried '
                 'and wine-steamed (shú) forms count as separate drugs. It is '
                 'the chief ingredient of the world-famous "Liu Wei Di Huang '
                 'Wan" (Six-Ingredient Rehmannia Pill) — and most of the '
                 'evidence debate concerns that formula, not the plant.'],
            ],
            prep='The WHO monograph gives a daily dose of 9–15 g of dried roots '
                 'and rhizomes as infusion or decoction. **Contraindicated in '
                 'chronic liver or gastrointestinal disease, in diarrhoea and '
                 'in pregnancy.** Not recommended in lactation or in children '
                 'without medical supervision.',
            science='There is no clinical trial of Chinese foxglove on its own; '
                    'all the human data come from multi-herb formulas in which '
                    'it is the chief ingredient. A multicentre randomised trial '
                    'published in 2023 in the Clinical Journal of the American '
                    'Society of Nephrology (148 patients, 48 weeks) found that '
                    'Rehmannia-6-based granules added to standard care in type 2 '
                    'diabetes with kidney disease slowed the decline in eGFR by '
                    '2.7 ml/min a year — but there was no significant difference '
                    'in albuminuria, and the trial was assessor-blind without '
                    'placebo. A meta-analysis published in 2025 in the Saudi '
                    'Medical Journal (17 RCTs, 1,139 patients) examines formulas '
                    'with Rehmannia as the "monarch drug" for perimenopausal '
                    'symptoms in breast-cancer patients and stresses '
                    'methodological flaws. Both measure the formula; '
                    'Rehmannia’s share is not separated. Evidence level '
                    'Traditional.',
            safety='**Contraindicated in chronic liver and gastrointestinal '
                   'disease and in diarrhoea** — the WHO monograph, from the '
                   'Chinese pharmacopoeia. **Contraindicated in pregnancy:** it '
                   'has been shown to inhibit embryo implantation in mice (a '
                   'possible anti-implantation effect). Diarrhoea, abdominal '
                   'pain, oedema, fatigue, vertigo and palpitations have been '
                   'reported; the monograph writes that these were transient '
                   'and disappeared within days. Not recommended in lactation '
                   'or in children without medical supervision. The "foxglove" '
                   'in its name should not mislead: it carries no cardiac '
                   'glycosides.',
            fact='Its name and its kinship do not agree: it is called "Chinese '
                 'foxglove", and the old classification put it in the foxglove '
                 'family (Scrophulariaceae) — the WHO monograph still does — but '
                 'modern classification moved it to the broomrape family '
                 '(Orobanchaceae), and it carries no cardiac glycosides. In '
                 'Chinese medicine, meanwhile, three states of the same root are '
                 'three separate drugs: raw, dried and wine-steamed. The '
                 'clearest example in this catalog of how the way a plant is '
                 'prepared can make it a different medicine.',
            season='Purple-brown thimble-shaped flowers in spring; the roots '
                   'are lifted in autumn and either dried or steamed with '
                   'wine.',
            habitat='Native to China; cultivated in China, Japan and Korea. It '
                    'does not grow in Turkey.',
            local='No Turkish name; Chinese dì huáng, shēng dì (raw), shú dì '
                  '(prepared).',
            confusion='⚠️ Its name and flower run together with foxglove '
                      '(Digitalis); foxglove carries lethal cardiac glycosides, '
                      'this plant does not. In the Chinese pharmacopoeia the raw '
                      'and prepared roots are separate drugs used for separate '
                      'purposes.',
        ),
        etk_en=[
            ['WHO: no interaction data',
             'The monograph states no information is available on drug '
             'interactions. As a plant credited with effects on blood glucose, '
             'stacking on antidiabetics is a theoretical note; in the '
             'diabetes-kidney trial patients continued their medication and no '
             'serious interaction was reported.'],
            ['Not attributing formula data to the plant',
             'Rehmannia-6 and similar formulas contain five to seven plants; '
             'their results cannot count as evidence for this root.'],
        ],
    ),

]
