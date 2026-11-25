# Parti 006 (26 Kasım 2026): Amazon kökenli sekiz bitki.
# Kaynak notu: PubMed sayfaları WebFetch'e reCAPTCHA döndürdüğü için künyeler ve
# özetler NCBI E-utilities üzerinden okundu; adresler aynı kayıtların
# pubmed.ncbi.nlm.nih.gov adresleridir. Adlar Kew WCVP'nin yerel kopyasından,
# EMA durumu yerel monograf indeksinden (204 kayıt, 159 monograf) doğrulandı:
# sekiz türün hiçbirinin EMA monografı yok. Cins düzeyindeki iki eşleşme tür
# düzeyinde ayrıldı — Passiflorae herba yalnız P. incarnata; Capsici fructus
# C. annuum var. minimum ve C. frutescens'in küçük meyveli çeşitleri (monograf
# metninde C. chinense geçmiyor).
POWO = 'https://powo.science.kew.org/'
Q = [

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='manyok',
        foto='',
        tr='Manyok',
        la='Manihot esculenta Crantz',
        taxon='Manihot esculenta',
        fam='Euphorbiaceae (sütleğengiller)',
        diger='Türkçede manyok ve kasava; nişastası tapyoka adıyla satılır. '
              'İngilizce cassava, manioc, yuca; Portekizce mandioca. Bu türün '
              'ne Avrupa İlaç Ajansı’nda ne TİTCK’de monografı vardır — bir '
              'ilaç bitkisi değil, temel besindir. Acı ve tatlı çeşitleri '
              'ayrı ayrı anılır; aradaki fark işlenme zorunluluğudur.',
        bolge=['amazon', 'afrika'],
        kat=['besin', 'zehir'],
        kisim='Nişastalı depo kökleri',
        kul=[
            ['Tropik Amerika, Afrika ve Asya — 300–500 milyon kişinin enerji kaynağı',
             'Critical Reviews in Food Science and Nutrition’da yayımlanan '
             'derleme manyoku Güney Amerika, Afrika ve Asya’da 300–500 milyon '
             'kişinin başlıca enerji kaynağı olarak tanımlar. Ekimi yılda '
             'yaklaşık 11 milyon hektarı kaplar ve 105 milyon tonun yarıdan '
             'fazlası insan tarafından tüketilir. Aynı derleme bitkinin birim '
             'alanda güneş enerjisini çözünür karbonhidrata en çok çeviren '
             'ürünlerden biri olduğunu, buna karşılık **protein içeriğinin ve '
             'kalitesinin zayıf** olduğunu ve sökülen köklerin birkaç günde '
             'bozulduğunu yazar.'],
            ['Afrika — acı çeşidin işlenmesi ve konzo',
             'Journal of the Neurological Sciences’taki derleme, konzo '
             'denen felç tablosunun her seferinde **yetersiz işlenmiş acı '
             'manyok köklerinin** tek düze tüketimiyle ve çok az protein '
             'desteğiyle birlikte görüldüğünü kaydeder. Geleneksel '
             'işleme — ıslatma, fermente etme ve pişirme — bu yüzden bir '
             'mutfak tercihi değil, zorunlu bir adımdır.'],
            ['Brezilya — çeşide göre değişen bileşim',
             'Food Research International’da 2024’te yayımlanan çalışma '
             'Brezilya’nın kuzeydoğu ve güneyinden dört manyok çeşidini '
             'karşılaştırmış; lif, dirençli nişasta, frukto-oligosakkarit, '
             'organik asit ve fenolik bileşik miktarlarının çeşitten çeşide '
             'değiştiğini bulmuştur. Çalışma laboratuvar ortamında '
             'yürütülmüştür.'],
        ],
        haz='Resmî bir monografta kabul edilmiş bir doz yoktur; manyok bir '
            'gıdadır. Dayanak alınan kaynaklarda **ev yapımı bir ilaç '
            'hazırlığı tarif edilmez.** Acı çeşidin kökleri ıslatma, '
            'fermente etme ve pişirme basamaklarından geçmeden yenmez; '
            'konzo tablosunun bildirildiği her yerde ortak nokta bu '
            'basamakların eksik kalmasıdır. Köklerin proteini zayıf '
            'olduğundan dayanak alınan derleme yanında protein kaynağı '
            'bulunmasının önemine dikkat çeker. Türkiye’de satılan tapyoka, '
            'kökten ayrılmış nişastadır.',
        bilim='Annals of the New York Academy of Sciences’taki 2017 tarihli '
              'derleme, manyoğa dayanan topluluklarda kanda **litrede 80 '
              'mikromole varan** siyanür düzeylerinin olağan olduğunu ve '
              'akut zehirlenme belirtilerine yol açtığını bildirir. Uzun '
              'vadeli etkiler konzo denen geri dönüşsüz spastik felç ve '
              'özellikle sıralı işlemleme (görsel-uzamsal çözümleme) '
              'alanında bilişsel kayıptır. Derlemenin saydığı sorumlu '
              'bileşikler siyanür, tiyosiyanat, siyanat ve '
              '2-iminotiyazolidin-4-karboksilik asittir; duyarlılığı '
              'artıran etkenler küçük yaş, kadın cinsiyet ve proteinden '
              'yoksul beslenmedir. Brain Research Bulletin’deki derleme '
              'konzonun Kongo Demokratik Cumhuriyeti, Mozambik, Tanzanya, '
              'Orta Afrika Cumhuriyeti, Angola, Kamerun ve Zambiya’da '
              'belgelendiğini, tablonun simetrik, kalıcı ve geri dönüşsüz '
              'olduğunu, duyu ve idrar-üreme belirtisi vermediğini yazar; '
              'aynı derleme **hastalığın mekanizmasının hâlâ bilinmediğini** '
              'belirtir. Annals of Neurology’deki çözümleme salgınların '
              'kuraklıklarla birlikte döngüsel geldiğini, Kongo’da baskın '
              'döngünün 3–6 yıl olduğunu gösterir. Manyoğun bir hastalığı '
              'tedavi ettiğini sınayan klinik çalışma bu kaynaklarda yoktur.',
        kanit='geleneksel',
        guv='orta',
        guvNot='Yeterince işlenmiş manyok yüz milyonlarca insanın günlük '
               'besinidir. Risk bitkinin kendisinde değil, **yetersiz '
               'işlenmiş acı çeşittedir.** Dayanak alınan derlemelere göre '
               'sonuç konzo adı verilen simetrik, kalıcı ve geri dönüşsüz '
               'bacak felci ve çocuklarda bilişsel gerilik olabilir; '
               'bildirilen salgınlar en çok **çocukları ve doğurganlık '
               'çağındaki kadınları** vurmuştur. Duyarlılığı artıran '
               'etkenler küçük yaş, kadın cinsiyet ve proteinden yoksul '
               'beslenmedir; salgınlar kuraklık dönemlerinde, beslenme '
               'neredeyse tümüyle manyoğa indiğinde çıkmıştır. Bilinen bir '
               'panzehir bu kaynaklarda anılmaz. Gebelik, emzirme ve '
               'çocuklar için gıda dışı kullanımı değerlendiren bir kaynak '
               'yoktur.',
        ilginc='Kuraklığa dayanan bitki, tam kuraklıkta tehlikeli oluyor: '
               'konzo salgınları yağış döngüsünü izliyor, çünkü kurak yılda '
               'beslenme manyoğa iniyor ve uzun işleme adımları atlanıyor.',
        etk=[
            ['İlaç etkileşimi çalışması yok',
             'Dayanak alınan kaynaklarda manyok için ilaç etkileşimi '
             'çalışması bulunmuyor; asıl risk etkileşim değil, yetersiz '
             'işlenmiş acı çeşidin siyanojenik glikozitleridir.'],
        ],
        etk_en=[
            ['No interaction studies',
             'The sources relied on here contain no drug-interaction study '
             'for cassava; the risk is not interaction but the cyanogenic '
             'glycosides of insufficiently processed bitter varieties.'],
        ],
        ek=dict(
            mevsim='Türkiye’de yetişmez; dayanak alınan kaynaklarda Türkiye '
                   'için bir toplama takvimi yoktur. Kökler ekimden 8–24 ay '
                   'sonra sökülür ve sökülünce birkaç gün içinde bozulur.',
            yetisme='Kew’in kayıtlarına göre yayılışı 90 bölgeyi kapsar; '
                    'tropik kuşağın hemen her yerinde yetiştirilir. Kökeni '
                    'Amazon havzasıdır; kuraklığa dayanıklı olduğu için '
                    'yağışın düştüğü yıllarda ekimi artar.',
            yoresel='Türkçede manyok, kasava; nişastası tapyoka.',
            karisma='Acı ve tatlı çeşitler dışarıdan benzer görünür, '
                    'siyanojenik glikozit içerikleri ise farklıdır; '
                    'bildirilen zehirlenmelerin tamamı yetersiz işlenmiş acı '
                    'çeşitle ilgilidir. Tapyoka incisi ya da unu, kökün '
                    'kendisiyle aynı şey değildir.',
        ),
        kaynak=[
            ['Manihot esculenta Crantz, World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['B. O. Okezie ve F. V. Kosikowski, “Cassava as a food”, Critical Reviews in Food Science and Nutrition 17(3), 1982',
             'https://pubmed.ncbi.nlm.nih.gov/6756790/'],
            ['B. Adamolekun, “Etiology of Konzo, epidemic spastic paraparesis associated with cyanogenic glycosides in cassava: role of thiamine deficiency?”, Journal of the Neurological Sciences 296(1–2), 2010',
             'https://pubmed.ncbi.nlm.nih.gov/20619859/'],
            ['D. Tshala-Katumbay ve ark., “Cyanide and the human brain: perspectives from a model of food (cassava) poisoning”, Annals of the New York Academy of Sciences 1378(1), 2016',
             'https://pubmed.ncbi.nlm.nih.gov/27450775/'],
            ['E. Kashala-Abotnes ve ark., “Konzo: a distinct neurological disease associated with food (cassava) cyanogenic poisoning”, Brain Research Bulletin 145, 2019',
             'https://pubmed.ncbi.nlm.nih.gov/29981837/'],
            ['O. S. Oluwole, “Cyclical konzo epidemics and climate variability”, Annals of Neurology 77(3), 2015',
             'https://pubmed.ncbi.nlm.nih.gov/25523348/'],
            ['Í. M. Mafaldo ve ark., “Cassava (Manihot esculenta) Brazilian cultivars have different chemical compositions, present prebiotic potential, and beneficial effects on the colonic microbiota of celiac individuals”, Food Research International, 2024',
             'https://pubmed.ncbi.nlm.nih.gov/39277216/'],
        ],
        rel=['kinoa', 'acai'],
        en=dict(
            name='Cassava',
            other='In Turkish manyok and kasava; its starch is sold as '
                  'tapioca. English cassava, manioc, yuca; Portuguese '
                  'mandioca. Neither the European Medicines Agency nor the '
                  'Turkish agency has a monograph for this species — it is '
                  'not a medicinal plant but a staple food. Bitter and sweet '
                  'varieties are named separately; the difference between '
                  'them is how much processing they require.',
            part='Starchy storage roots',
            uses=[
                ['Tropical America, Africa and Asia — the energy source of 300–500 million people',
                 'A review in Critical Reviews in Food Science and Nutrition '
                 'describes cassava as a principal energy source for 300–500 '
                 'million people in South America, Africa and Asia. Its '
                 'cultivation covers some 11 million hectares a year, and '
                 'more than half of the 105 million tonnes produced is eaten '
                 'by people. The same review notes that it is among the crops '
                 'converting the most solar energy per unit area into soluble '
                 'carbohydrate, while its **protein content and quality are '
                 'poor** and the lifted roots spoil within a few days.'],
                ['Africa — processing the bitter variety, and konzo',
                 'A review in the Journal of the Neurological Sciences records '
                 'that the paralytic condition called konzo has invariably '
                 'been seen alongside the monotonous consumption of '
                 '**inadequately processed bitter cassava roots** with very '
                 'little protein in the diet. Traditional processing — '
                 'soaking, fermenting and cooking — is therefore not a '
                 'culinary preference but a required step.'],
                ['Brazil — composition that differs by cultivar',
                 'A 2024 study in Food Research International compared four '
                 'cassava cultivars from north-eastern and southern Brazil '
                 'and found that fibre, resistant starch, '
                 'fructo-oligosaccharide, organic acid and phenolic content '
                 'varied between them. The work was carried out in the '
                 'laboratory.'],
            ],
            prep='No official monograph sets an accepted dose; cassava is a '
                 'food. The sources relied on here **describe no home '
                 'medicinal preparation.** Roots of the bitter variety are '
                 'not eaten without soaking, fermenting and cooking; '
                 'wherever konzo has been reported, the common factor is '
                 'that these steps were left incomplete. Because the roots '
                 'are poor in protein, the review relied on here stresses '
                 'the importance of a protein source alongside them. '
                 'Tapioca sold in Turkey is starch separated from the root.',
            science='A 2017 review in the Annals of the New York Academy of '
                    'Sciences reports that in communities relying on cassava, '
                    'blood cyanide concentrations of **up to 80 micromoles '
                    'per litre** are commonplace and produce signs of acute '
                    'toxicity. The long-term effects are the irreversible '
                    'spastic paralysis called konzo and cognitive loss, '
                    'mainly in sequential processing (visual-spatial '
                    'analysis). The compounds the review holds responsible '
                    'are cyanide, thiocyanate, cyanate and '
                    '2-iminothiazolidine-4-carboxylic acid; susceptibility is '
                    'increased by younger age, female sex and a '
                    'protein-deficient diet. A review in Brain Research '
                    'Bulletin records konzo in the Democratic Republic of '
                    'Congo, Mozambique, Tanzania, the Central African '
                    'Republic, Angola, Cameroon and Zambia, describes the '
                    'picture as symmetrical, permanent and irreversible with '
                    'no sensory or genitourinary signs, and states that '
                    '**the mechanism of the disease is still unknown.** An '
                    'analysis in Annals of Neurology shows the epidemics '
                    'arriving cyclically with droughts, the dominant cycle in '
                    'Congo being 3–6 years. These sources contain no clinical '
                    'trial testing cassava as a treatment for any condition.',
            safety='Adequately processed cassava is the daily food of '
                   'hundreds of millions. The risk lies not in the plant but '
                   'in the **insufficiently processed bitter variety.** '
                   'According to the reviews relied on here the outcome can '
                   'be konzo, a symmetrical, permanent and irreversible '
                   'paralysis of the legs, and cognitive delay in children; '
                   'the reported epidemics have struck **children and women '
                   'of childbearing age** hardest. Susceptibility is '
                   'increased by younger age, female sex and a '
                   'protein-deficient diet; the epidemics have appeared '
                   'during droughts, when the diet narrows to cassava almost '
                   'alone. These sources name no known antidote. No source '
                   'assesses non-food use in pregnancy, lactation or '
                   'children.',
            fact='The plant that survives drought becomes dangerous in '
                 'drought: konzo epidemics follow the rainfall cycle, because '
                 'in a dry year the diet narrows to cassava alone and the '
                 'long processing gets skipped.',
            season='It does not grow in Turkey; the sources relied on here '
                   'give no collection calendar for Turkey. Roots are lifted '
                   '8–24 months after planting and spoil within days.',
            habitat='According to Kew’s records its range covers 90 regions; '
                    'it is grown almost throughout the tropics. Its origin is '
                    'the Amazon basin, and because it withstands drought its '
                    'planting increases in dry years.',
            local='In Turkish manyok, kasava; its starch tapioca.',
            confusion='Bitter and sweet varieties look alike from the '
                      'outside but differ in cyanogenic glycoside content; '
                      'every reported poisoning involves the insufficiently '
                      'processed bitter variety. Tapioca pearls or flour are '
                      'not the same thing as the root itself.',
        ),
    ),

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='yerfistigi',
        foto='Arachis hypogaea 003.JPG',
        tr='Yer fıstığı',
        la='Arachis hypogaea L.',
        taxon='Arachis hypogaea',
        fam='Fabaceae (baklagiller)',
        diger='Türkçede yer fıstığı, Amerikan fıstığı; bazı yörelerde çerez '
              'olarak "fıstık" denir ama antep fıstığı başka bir bitkidir. '
              'İngilizce peanut, groundnut. Bu türün ne Avrupa İlaç '
              'Ajansı’nda ne TİTCK’de monografı vardır. Bir baklagildir; '
              'meyveleri toprağın altında olgunlaşır.',
        bolge=['amazon'],
        kat=['besin'],
        kisim='Tohum',
        kul=[
            ['Güney Amerika — ekilen fıstığın kökeni',
             'Yer fıstığı Güney Amerika kökenli bir kültür bitkisidir; '
             'bugün dünyanın sıcak kuşağında yağ, protein ve çerez için '
             'ekilir. Dayanak alınan kaynaklar bitkiyi bir ilaç bitkisi '
             'olarak değil, gıda ve alerjen olarak ele alır.'],
            ['Günümüz tıbbı — alerjenin kendisi ilaç olarak',
             'Bu tür için bulunan insan çalışmalarının neredeyse tamamı '
             'bitkinin faydasını değil, **fıstık alerjisinin tedavisini** '
             'inceliyor. Ağızdan immünoterapide kullanılan şey ölçülü '
             'miktarda fıstık proteininin kendisidir; Avrupa ve ABD’de bu '
             'amaçla ruhsatlanmış bir ürün vardır. Yani fıstık burada '
             'şifalı bitki değil, alerjisi olan kişide bağışıklığı '
             'alıştırmak için kullanılan maddedir.'],
        ],
        haz='Resmî bir monografta kabul edilmiş bir doz yoktur; yer fıstığı '
            'bir gıdadır. **Ağızdan immünoterapi evde yapılacak bir şey '
            'değildir:** dayanak alınan çalışmalarda dozlar hekim '
            'gözetiminde, anafilaksiye hazırlıklı ortamda ve haftalar '
            'boyunca basamak basamak artırılarak verilmiştir. Çalışmalarda '
            'katılımcıların neredeyse tamamında istenmeyen etki görülmüştür.',
        bilim='Molecular Immunology’deki derleme, fıstıkta **16 proteinin '
              'resmen alerjen olarak tanındığını** ve bu alerjenlerin '
              'duyarlı kişilerde özgül IgE üretimini tetiklediğini yazar. '
              'Journal of Allergy and Clinical Immunology: In Practice’te '
              'yayımlanan ARC004 çalışması, PALISADE adlı randomize '
              'kontrollü çalışmanın açık etiketli uzantısıdır: 4–17 yaş '
              'arası 358 katılımcıyla sürdürülmüş, günlük doz alan '
              'kümelerde duyarsızlaşma oranı günaşırı alanlardan yüksek '
              'çıkmış, katılımcıların **%83’ünde hafif ya da orta şiddette '
              'istenmeyen etki** görülmüştür. Annals of Allergy, Asthma and '
              'Immunology’deki RAMSES çalışmasında 506 çocukta doz artırma '
              'döneminde istenmeyen etki oranı ilaç kolunda %55, plasebo '
              'kolunda %33,9; sürdürme döneminde %98,8’e karşı %94 '
              'bulunmuştur; en sık görülenler sindirim sistemi '
              'yakınmalarıdır. Bu çalışmaların hiçbiri fıstığın bir '
              'hastalığı iyileştirdiğini göstermez; **ölçtükleri şey '
              'alerjik kişinin fıstığa dayanma eşiğidir.**',
        kanit='klinik',
        guv='dusuk',
        guvNot='Yer fıstığı yaygın bir gıdadır ve çoğu kişide sorun '
               'çıkarmaz. Asıl konu **alerjidir:** derlemeye göre fıstıkta '
               'resmen tanınmış 16 alerjen bulunur ve duyarlı kişilerde '
               'tepki anafilaksiye kadar gidebilir; bu, az miktarda '
               'temasla da olabilir. Alerjisi olan kişi için güvenli miktar '
               'diye bir şey kendi başına belirlenemez. Ağızdan '
               'immünoterapi yalnızca hekim gözetiminde yürütülür ve '
               'çalışmalarda katılımcıların büyük kısmında istenmeyen etki '
               'bildirilmiştir. Gebelik ve emzirmede gıda miktarının '
               'üzerinde kullanımı değerlendiren bir kaynak yoktur. '
               'Küflenmiş fıstıkta aflatoksin birikebildiği için '
               'kararmış, buruşmuş taneler yenmez.',
        ilginc='Yer fıstığının insanda en çok çalışılmış etkisi bir faydası '
               'değil: bu tür için bulunan klinik çalışmaların neredeyse '
               'tamamı, fıstığa alerjisi olan çocukları yine fıstıkla '
               'tedavi etme denemeleridir.',
        ek=dict(
            mevsim='Türkiye’de Akdeniz ve Ege kıyılarında yetiştirilir; '
                   'hasat sonbahardadır. Dayanak alınan kaynaklarda şifa '
                   'amacıyla bir toplama takvimi yoktur.',
            yetisme='Kew’in kayıtlarına göre yayılışı 103 bölgeyi kapsar; '
                    'sıcak ve kumlu toprak ister. Kökeni Güney Amerika’dır. '
                    'Çiçek döllendikten sonra sapı aşağı kıvrılır ve meyve '
                    'toprağın içinde olgunlaşır.',
            yoresel='yer fıstığı, Amerikan fıstığı, çerez fıstığı.',
            karisma='Antep fıstığı (Pistacia vera) ve kaju bambaşka '
                    'bitkilerdir; alerjileri de ayrıdır. Fıstık alerjisi '
                    'olan kişilerde susam ve bazı baklagillerle çapraz '
                    'tepkime bildirilmiştir.',
        ),
        kaynak=[
            ['Arachis hypogaea L., World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['C. Palladino ve H. Breiteneder, “Peanut allergens”, Molecular Immunology 100, 2018',
             'https://pubmed.ncbi.nlm.nih.gov/29680589/'],
            ['B. P. Vickery ve ark., “Continuous and Daily Oral Immunotherapy for Peanut Allergy: Results from a 2-Year Open-Label Follow-On Study”, Journal of Allergy and Clinical Immunology: In Practice 9(5), 2021',
             'https://pubmed.ncbi.nlm.nih.gov/33359589/'],
            ['C. Ciaccio ve ark., “Participant characteristics and safety outcomes of peanut oral immunotherapy in the RAMSES and ARC011 trials”, Annals of Allergy, Asthma and Immunology, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/35973655/'],
        ],
        rel=['sachainchi', 'susam'],
        en=dict(
            name='Peanut',
            other='In Turkish yer fıstığı and Amerikan fıstığı; in some '
                  'regions it is simply called "fıstık" as a snack, but the '
                  'pistachio is a different plant. English peanut, '
                  'groundnut. Neither the European Medicines Agency nor the '
                  'Turkish agency has a monograph for this species. It is a '
                  'legume, and its fruits ripen underground.',
            part='Seed',
            uses=[
                ['South America — the origin of the cultivated peanut',
                 'The peanut is a crop of South American origin, now grown '
                 'through the warm zones of the world for oil, protein and '
                 'snacks. The sources relied on here treat the plant not as '
                 'a medicinal plant but as a food and an allergen.'],
                ['Modern medicine — the allergen itself as the medicine',
                 'Almost every human study found for this species examines '
                 'not a benefit of the plant but **the treatment of peanut '
                 'allergy.** What is used in oral immunotherapy is measured '
                 'amounts of peanut protein itself, and a product licensed '
                 'for this purpose exists in Europe and the United States. '
                 'Here the peanut is not a healing herb but the substance '
                 'used to accustom an allergic person’s immune system.'],
            ],
            prep='No official monograph sets an accepted dose; the peanut is '
                 'a food. **Oral immunotherapy is not something to do at '
                 'home:** in the studies relied on here, doses were given '
                 'under medical supervision, in settings prepared for '
                 'anaphylaxis, and raised step by step over weeks. Almost '
                 'all participants in those studies had adverse events.',
            science='A review in Molecular Immunology states that **16 '
                    'proteins in peanut are officially recognised as '
                    'allergens** and that they trigger specific IgE '
                    'production in predisposed people. The ARC004 study, '
                    'published in the Journal of Allergy and Clinical '
                    'Immunology: In Practice, is the open-label follow-on to '
                    'the randomised controlled PALISADE trial: it continued '
                    'with 358 participants aged 4–17, desensitisation rates '
                    'appeared higher in the daily-dosing cohorts than in the '
                    'non-daily ones, and **83% of participants had mild or '
                    'moderate adverse events.** In the RAMSES trial in '
                    'Annals of Allergy, Asthma and Immunology, among 506 '
                    'children the adverse-event rate during initial dose '
                    'escalation was 55% on treatment against 33.9% on '
                    'placebo, and 98.8% against 94% during updosing; the '
                    'commonest were gastrointestinal. None of these studies '
                    'shows the peanut curing a disease; **what they measure '
                    'is an allergic person’s threshold of tolerance to '
                    'peanut.**',
            safety='The peanut is a common food and causes no trouble for '
                   'most people. The issue is **allergy:** according to the '
                   'review there are 16 officially recognised allergens in '
                   'peanut, and in sensitised people the reaction can go as '
                   'far as anaphylaxis, including after contact with small '
                   'amounts. For an allergic person no safe amount can be '
                   'worked out alone. Oral immunotherapy is conducted only '
                   'under medical supervision, and most participants in the '
                   'trials reported adverse events. No source assesses use '
                   'above food amounts in pregnancy or lactation. Because '
                   'aflatoxin can accumulate in mouldy nuts, darkened and '
                   'shrivelled kernels are not eaten.',
            fact='The most-studied effect of the peanut in humans is not a '
                 'benefit: almost every clinical trial found for this '
                 'species is an attempt to treat peanut-allergic children '
                 'with peanut itself.',
            season='It is grown on Turkey’s Mediterranean and Aegean coasts, '
                   'with harvest in autumn. The sources relied on here give '
                   'no collection calendar for medicinal use.',
            habitat='According to Kew’s records its range covers 103 '
                    'regions; it needs warmth and sandy soil. Its origin is '
                    'South America. After the flower is fertilised its stalk '
                    'bends down and the fruit ripens in the soil.',
            local='yer fıstığı, Amerikan fıstığı, çerez fıstığı.',
            confusion='The pistachio (Pistacia vera) and the cashew are '
                      'quite different plants, with different allergies. '
                      'Cross-reactivity with sesame and some legumes has '
                      'been reported in peanut-allergic people.',
        ),
    ),

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='habanero',
        foto='Habanero chile - fruits (aka).jpg',
        tr='Habanero',
        la='Capsicum chinense Jacq.',
        taxon='Capsicum chinense',
        fam='Solanaceae (patlıcangiller)',
        diger='Türkçede habanero adıyla bilinir; aynı türün Hindistan’daki '
              'çeşidi bhut jolokia ya da naga biberi adıyla anılır. '
              'İngilizce habanero, Scotch bonnet, ghost pepper. Tür adı '
              '"chinense" yanıltıcıdır: bitki Çin’den değil, Amazon '
              'havzasından gelir. **Avrupa İlaç Ajansı’nın Capsici fructus '
              'monografı bu türe ait değildir:** monograf Capsicum annuum '
              'var. minimum ile Capsicum frutescens’in küçük meyveli '
              'çeşitleri içindir, metninde C. chinense geçmez. TİTCK’de de '
              'bu türün monografı yoktur.',
        bolge=['amazon'],
        kat=['besin', 'sifa'],
        kisim='Olgun meyve',
        kul=[
            ['Tropik Amerika — baharat ve halk hekimliği',
             'International Journal of Molecular Sciences’taki derleme, '
             'Capsicum cinsinin beş evcilleştirilmiş türünden birinin C. '
             'chinense olduğunu yazar ve meyvelerin gıda katkısı olarak diş '
             'ağrısı, parazit enfeksiyonları, öksürük, yara iyileşmesi, '
             'boğaz ağrısı ve romatizmada kullanıldığını kaydeder. Aynı '
             'derleme bitkinin provitamin A, E ve C vitaminleri, '
             'karotenoitler ve kapsaisinoitler bakımından zengin olduğunu '
             'belirtir.'],
            ['Kuzeydoğu Hindistan — naga biberi',
             'Journal of Ethnopharmacology’deki derleme, aynı türün '
             'Hindistan’ın kuzeydoğusuna özgü "naga biberi" ya da "bhut '
             'jolokia" çeşidinin bölge halkları tarafından çok eskiden beri '
             'çeşitli rahatsızlıklarda kullanıldığını yazar ve onu dünyanın '
             'en acı biber çeşidi olarak tanımlar. Derleme, bitkinin '
             'biyolojisi ve yetiştiriciliğine ilişkin bilginin dağınık ve '
             'yetersiz olduğunu da belirtir.'],
        ],
        haz='Bu tür için resmî bir monografta kabul edilmiş doz yoktur; '
            'habanero bir baharattır. Kas ağrısında kullanılan haricî '
            'kapsaisin ürünlerinin ölçüleri **başka Capsicum türlerinin** '
            'monografından gelir ve bu kayda uygulanmaz. Dayanak alınan '
            'kaynaklarda ev yapımı bir hazırlık tarif edilmez; acılığı çok '
            'yüksek olduğundan mutfakta da çok küçük miktarlarda '
            'kullanılır.',
        bilim='Current Drug Delivery’de yayımlanan çalışma, bhut '
              'jolokia’dan elde edilen yarı saflaştırılmış kapsaisinoit '
              'özütünü nanolipit keseciklere yerleştirmiş; etkililiği '
              '**sıçanlarda** karragenan ve formaldehitle oluşturulan '
              'iltihap ile Freund adjuvanı artriti modellerinde sınamış, '
              'insanlarda ise yalnızca birinci evre bir çalışmayla '
              'formülasyonun **kabul edilebilirliğini** ölçmüştür. Yani bu '
              'çalışmanın insanda gösterdiği şey ağrı kesici etki değil, '
              'ürünün tahriş yüzünden bırakılmadan kullanılabilmesidir. '
              'Derlemeler kapsaisinoitlerin ağrı tedavisi, vücut sıcaklığı '
              'düzenlenmesi, kilo ve kanser üzerindeki olası etkilerini '
              'sıralar, ama bunları **araştırılması gereken alanlar** '
              'olarak anar. Bu türle yapılmış, bir hastalıkta etkililiği '
              'ölçen randomize kontrollü bir çalışma dayanak alınan '
              'kaynaklarda yoktur.',
        kanit='geleneksel',
        guv='orta',
        guvNot='Gıda miktarlarında yaygın olarak tüketilir. Bu tür '
               'olağanüstü acı çeşitler içerir ve asıl sorun '
               '**kapsaisinin tahriş ediciliğidir:** dayanak alınan '
               'çalışma, özütün derişime bağlı tahrişi yüzünden hastaların '
               'tedaviyi bıraktığını, formülasyon çalışmasının da bu yüzden '
               'yapıldığını yazar. Meyve ya da özüt göz çevresine ve '
               'mukozalara değdirilmez; eldeyken göze dokunulmaması ve '
               'kullanımdan sonra ellerin yıkanması gerekir. Çok acı '
               'çeşitlerin bir seferde fazla miktarda yenmesi mide ve '
               'yemek borusunda şiddetli yakınmaya yol açabilir. Gebelik, '
               'emzirme ve çocuklarda gıda dışı kullanımı değerlendiren '
               'bir kaynak yoktur; bu türe ait bir monograf bulunmadığı '
               'için resmî bir kontrendikasyon listesi de yoktur.',
        ilginc='Adı "Çin biberi" anlamına gelir ama bitki Çin’i hiç '
               'görmemiştir: Amazon havzasında evcilleştirilmiş, adı '
               '18. yüzyılda yanlış bir coğrafyayla kayda geçmiştir.',
        etk=[
            ['Aynı bölgeye sürülen diğer haricî ürünler (ısıtıcı merhemler, ağrı kesici jeller)',
             'Kapsaisin tahrişi artırabileceği için aynı yere aynı anda '
             'uygulanmaması uygun olur.'],
            ['Sıcak uygulama, duş ve güneş',
             'Kapsaisin sürülen bölgede sıcakla birlikte yanma şiddetlenir.'],
            ['ACE inhibitörleri',
             'Haricî kapsaisin kullanımıyla öksürük bildirilmiştir; bu '
               'ilaçları kullananlarda öksürük zaten sık görülür.'],
        ],
        etk_en=[
            ['Other topical products on the same area (warming balms, analgesic gels)',
             'Capsaicin may increase irritation, so applying them to the '
             'same spot at the same time is best avoided.'],
            ['Heat, showers and sun',
             'Burning on the treated area intensifies with heat.'],
            ['ACE inhibitors',
             'Cough has been reported with topical capsaicin use, and cough '
             'is already common with these medicines.'],
        ],
        ek=dict(
            mevsim='Türkiye’de doğal olarak yetişmez; seralarda ve '
                   'saksıda yetiştirilir, meyveler yaz sonu ve sonbaharda '
                   'olgunlaşır.',
            yetisme='Kew’in kayıtlarına göre yayılışı 21 bölgeyi kapsar; '
                    'Amazon havzası, Karayipler ve Orta Amerika’nın sıcak '
                    've nemli yerleri. Kurağa ve soğuğa dayanmaz.',
            yoresel='Türkçede yerleşik bir yöresel adı yok; habanero, '
                    'naga biberi, bhut jolokia adlarıyla geçer.',
            karisma='Acı biber (C. annuum var. minimum), küçük meyveli '
                    'C. frutescens çeşitleri ve rocoto (C. pubescens) ayrı '
                    'türlerdir. Bir türün '
                    'monografı ve kısıtlamaları akrabasına ait değildir: '
                    'Avrupa İlaç Ajansı’nın biber monografı C. annuum var. '
                    'minimum ile C. frutescens için yazılmıştır, bu tür '
                    'için değil.',
        ),
        kaynak=[
            ['Capsicum chinense Jacq., World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['G. E. Batiha ve ark., “Biological Properties, Bioactive Constituents, and Pharmacokinetics of Some Capsicum spp. and Capsaicinoids”, International Journal of Molecular Sciences 21(15), 2020',
             'https://pubmed.ncbi.nlm.nih.gov/32707790/'],
            ['M. K. Meghvansi ve ark., “Naga chilli: a potential source of capsaicinoids with broad-spectrum ethnopharmacological applications”, Journal of Ethnopharmacology 132(1), 2010',
             'https://pubmed.ncbi.nlm.nih.gov/20728519/'],
            ['K. K. Sarwa ve ark., “Topical Analgesic Nanolipid Vesicles Formulation of Capsaicinoids Extract of Bhut Jolokia (Capsicum chinense Jacq): Pharmacodynamic Evaluation in Rat Models and Acceptability studies in Human Volunteers”, Current Drug Delivery 13(8), 2016',
             'https://pubmed.ncbi.nlm.nih.gov/27306849/'],
        ],
        rel=['acibiber'],
        en=dict(
            name='Habanero',
            other='Known in Turkish as habanero; the variety of the same '
                  'species grown in India is called bhut jolokia or naga '
                  'chilli. English habanero, Scotch bonnet, ghost pepper. '
                  'The species name "chinense" misleads: the plant comes not '
                  'from China but from the Amazon basin. **The European '
                  'Medicines Agency’s Capsici fructus monograph does not '
                  'belong to this species:** it covers Capsicum annuum var. '
                  'minimum and small-fruited varieties of Capsicum '
                  'frutescens, and C. chinense does not appear in its text. '
                  'The Turkish agency has no monograph for this species '
                  'either.',
            part='Ripe fruit',
            uses=[
                ['Tropical America — spice and folk medicine',
                 'A review in the International Journal of Molecular Sciences '
                 'states that C. chinense is one of the five domesticated '
                 'species of Capsicum and records the fruits being used as '
                 'food additives for toothache, parasitic infections, '
                 'coughs, wound healing, sore throat and rheumatism. The '
                 'same review notes the plant is rich in provitamin A, '
                 'vitamins E and C, carotenoids and capsaicinoids.'],
                ['North-east India — the naga chilli',
                 'A review in the Journal of Ethnopharmacology writes that '
                 'the "naga chilli" or "bhut jolokia" variety of this same '
                 'species, indigenous to north-east India, has long been '
                 'used by the region’s peoples for various ailments, and '
                 'describes it as the hottest chilli variety in the world. '
                 'The review also notes that knowledge of the plant’s '
                 'biology and cultivation is scattered and scanty.'],
            ],
            prep='No official monograph sets an accepted dose for this '
                 'species; the habanero is a spice. The measures used for '
                 'topical capsaicin products in muscle pain come from the '
                 'monograph of **other Capsicum species** and do not apply '
                 'to this record. The sources relied on here describe no '
                 'home preparation; because the pungency is very high, it is '
                 'used in very small amounts in the kitchen as well.',
            science='A study in Current Drug Delivery encapsulated a '
                    'semi-purified capsaicinoid extract of bhut jolokia in '
                    'nanolipid vesicles; efficacy was tested **in rats** in '
                    'carrageenan- and formaldehyde-induced inflammation and '
                    'Freund’s adjuvant arthritis models, while in humans a '
                    'phase I study measured only the **acceptability** of '
                    'the formulation. What that study shows in humans is '
                    'therefore not an analgesic effect but that the product '
                    'can be used without being abandoned because of '
                    'irritation. Reviews list possible effects of '
                    'capsaicinoids on pain, body-temperature regulation, '
                    'weight and cancer, but present them as **areas '
                    'warranting research.** The sources relied on here '
                    'contain no randomised controlled trial measuring '
                    'efficacy of this species in any condition.',
            safety='It is widely eaten in food amounts. This species '
                   'includes extraordinarily pungent varieties, and the real '
                   'issue is **the irritancy of capsaicin:** the study '
                   'relied on here reports that concentration-dependent '
                   'irritation led patients to withdraw from therapy, which '
                   'is why the formulation work was done. The fruit or '
                   'extract is kept away from the area around the eyes and '
                   'from mucous membranes; the eyes should not be touched '
                   'while handling it and the hands washed afterwards. '
                   'Eating a large amount of a very pungent variety at once '
                   'can cause severe stomach and oesophageal complaints. No '
                   'source assesses non-food use in pregnancy, lactation or '
                   'children; as there is no monograph for this species, '
                   'there is no official list of contraindications either.',
            fact='Its name means "Chinese pepper", yet the plant has never '
                 'seen China: it was domesticated in the Amazon basin and '
                 'recorded in the eighteenth century with the wrong '
                 'geography.',
            season='It does not grow wild in Turkey; it is raised in '
                   'greenhouses and pots, with fruit ripening in late summer '
                   'and autumn.',
            habitat='According to Kew’s records its range covers 21 '
                    'regions: the warm, humid parts of the Amazon basin, the '
                    'Caribbean and Central America. It tolerates neither '
                    'drought nor cold.',
            local='No established Turkish regional name; it appears as '
                  'habanero, naga biberi, bhut jolokia.',
            confusion='Chilli pepper (C. annuum var. minimum), '
                      'small-fruited C. frutescens varieties and rocoto (C. '
                      'pubescens) are separate species. A monograph and its '
                      'restrictions do not '
                      'belong to a relative: the European Medicines '
                      'Agency’s pepper monograph was written for C. annuum '
                      'var. minimum and C. frutescens, not for this '
                      'species.',
        ),
    ),

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='prontoalivio',
        foto='Lippia alba (11627884485).jpg',
        tr='Pronto alivio',
        la='Lippia alba (Mill.) N.E.Br. ex Britton & P.Wilson',
        taxon='Lippia alba',
        fam='Verbenaceae (mineçiçeğigiller)',
        diger='Türkçede yerleşik bir adı yoktur; Kew’in yayılış '
              'kayıtlarında Türkiye yoktur. İspanyolca "pronto alivio" '
              '(çabuk rahatlama), Brezilya’da "erva cidreira" ve "falsa '
              'melissa"; İngilizce bushy matgrass. Adı melisayı çağırsa da '
              'melisa (Melissa officinalis) başka bir bitkidir. Bu türün ne '
              'Avrupa İlaç Ajansı’nda ne TİTCK’de monografı vardır.',
        bolge=['amazon', 'kamerika'],
        kat=['sifa'],
        kisim='Yapraklar ve çiçekli dallar',
        kul=[
            ['Tropik Amerika — sindirim, solunum ve yatıştırıcı',
             'Journal of Ethnopharmacology’deki derleme, türün başlıca '
             'sindirim ve solunum yolu rahatsızlıklarında, ayrıca '
             'yatıştırıcı ve tansiyon düşürücü bir çare olarak '
             'kullanıldığını kaydeder. Derleme bu kullanımlardan bir '
             'kısmının bitkinin iltihap ve mikroba karşı etkileri ile ağrı '
             'kesici özellikleriyle açıklanabileceğini belirtir.'],
            ['Kemotip sorunu — aynı adla yedi farklı bitki',
             'Aynı derleme türün uçucu yağında **yedi ayrı kemotip** '
             'bulunduğunu yazar. Bu, aynı Latince adı taşıyan iki bitkinin '
             'kokusunun ve etken bileşiklerinin birbirinden belirgin '
             'biçimde farklı olabileceği anlamına gelir; derleme bu '
             'değişkenliğin araştırma sonuçlarının geçerliliği için önemli '
             'olduğunu vurgular.'],
        ],
        haz='Resmî bir monografta kabul edilmiş bir doz yoktur. Dayanak '
            'alınan klinik çalışmalarda kullanılan şey yaprakların '
            '**hidroalkolik özütüdür** ve çalışmalar belirli bir kemotiple '
            '(geranial-karvenon) yürütülmüştür; evde demlenen bir çayla '
            'aynı şey değildir. Derleme, uçucu yağ bileşiminin kemotipe '
            'göre değiştiğini belirttiği için elde bulunan bir bitkinin '
            'çalışılan bitkiyle aynı bileşimde olduğu varsayılamaz.',
        bilim='Journal of Ethnopharmacology’deki derleme yatıştırıcı ve '
              'kaygı giderici etkiler için **kısmî ve olumlu** sonuçlar '
              'bulunduğunu, ama türün birçok endikasyonu için iyi '
              'yürütülmüş biyolojik çalışmaların hâlâ gerektiğini yazar. '
              'Phytomedicine’de yayımlanan iki çalışma migrende '
              'hidroalkolik özütü denemiştir: ilki ikinci evre, '
              '**kontrolsüz** bir kohort çalışmasıdır ve hastaların '
              '%80’inden fazlasında ağrı şiddeti ve sıklığında en az '
              'yarıya inme bildirir; ikincisi 21 kadınla yürütülmüş, yine '
              '**kontrolsüz** bir çalışmadır ve MIDAS ile HIT-6 '
              'ölçeklerinde düşüş, hastaların %70’inden fazlasında ağrı '
              'sıklığında en az yarıya inme bildirir. İkisinde de plasebo '
              'kolu yoktur; yani bu sonuçlar bitkiyi plaseboyla '
              'karşılaştırmamıştır ve migren gibi dalgalı seyirli bir '
              'yakınmada kontrolsüz çalışmalar fazla iyimser sonuç '
              'verebilir. Her iki çalışma tek bir kemotiple yapılmıştır.',
        kanit='sinirli',
        guv='orta',
        guvNot='Dayanak alınan iki klinik çalışmada istenmeyen etki '
               'bildirilmemiştir, ama çalışmalar küçük ve kontrolsüzdür; '
               'bu, güvenliğin gösterildiği anlamına gelmez. Bitkinin '
               'geleneksel kullanımı yatıştırıcı ve tansiyon düşürücü '
               'yöndedir, dolayısıyla **uyku ve kaygı ilaçları ile tansiyon '
               'ilaçları kullananlarda dikkat gerekir.** Kemotip '
               'değişkenliği yüzünden elde bulunan bitkinin bileşimi '
               'bilinmez. Gebelik, emzirme ve çocuklar için ayrı bir '
               'değerlendirme dayanak alınan kaynaklarda yoktur; monograf '
               'bulunmadığı için resmî bir kontrendikasyon listesi de '
               'yoktur.',
        ilginc='Aynı Latince adı taşıyan iki bitkinin kokusu ve etken '
               'bileşikleri farklı olabiliyor: derleme türde yedi ayrı '
               'kemotip sayıyor, klinik çalışmalar ise yalnız birini '
               'denemiş.',
        etk=[
            ['Yatıştırıcılar, uyku ve kaygı ilaçları',
             'Geleneksel kullanımı ve derlemedeki kısmî yatıştırıcı '
             'bulgular nedeniyle uyuşukluğu artırabilir.'],
            ['Tansiyon ilaçları',
             'Halk hekimliğinde tansiyon düşürücü olarak kullanıldığı '
             'için birlikte kullanımda tansiyonun izlenmesi uygun olur.'],
            ['Migren ilaçları',
             'Klinik çalışmalar bitkiyi migrende tek başına denemiştir; '
             'reçeteli migren tedavisinin yerine geçmez ve birlikte '
             'kullanımı değerlendiren bir çalışma yoktur.'],
        ],
        etk_en=[
            ['Sedatives, sleep and anxiety medicines',
             'Given its traditional use and the partial sedative findings in '
             'the review, it may increase drowsiness.'],
            ['Blood-pressure medicines',
             'As it is used in folk medicine to lower blood pressure, '
             'monitoring blood pressure is sensible when the two are '
             'combined.'],
            ['Migraine medicines',
             'The clinical studies tested the plant alone in migraine; it '
             'does not replace prescribed migraine treatment and no study '
             'assesses the combination.'],
        ],
        ek=dict(
            mevsim='Türkiye’de yetişmez; dayanak alınan kaynaklarda '
                   'Türkiye için bir toplama takvimi yoktur.',
            yetisme='Kew’in kayıtlarına göre yayılışı 56 bölgeyi kapsar; '
                    'tropik ve astropik Amerika’nın açık, nemli yerleri. '
                    'Başka kıtalarda da yerleşmiştir.',
            yoresel='Türkçe yöresel adı yok. Yerel adları: pronto alivio, '
                    'erva cidreira, falsa melissa.',
            karisma='Melisa (Melissa officinalis) ve limon otu '
                    '(Cymbopogon) ile karıştırılabilir; üçü de limon '
                    'kokulu, üçü de ayrı bitkidir. Aynı türün kemotipleri '
                    'de birbirinden farklı koktuğu için koku tek başına '
                    'tanıma ölçütü değildir.',
        ),
        kaynak=[
            ['Lippia alba (Mill.) N.E.Br. ex Britton & P.Wilson, World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['T. Hennebelle ve ark., “Ethnopharmacology of Lippia alba”, Journal of Ethnopharmacology 116(2), 2008',
             'https://pubmed.ncbi.nlm.nih.gov/18207682/'],
            ['R. Conde ve ark., “Chemical composition and therapeutic effects of Lippia alba (Mill.) N. E. Brown leaves hydro-alcoholic extract in patients with migraine”, Phytomedicine 18(14), 2011',
             'https://pubmed.ncbi.nlm.nih.gov/21802924/'],
            ['F. Carmona ve ark., “Lippia alba (Mill.) N. E. Brown hydroethanolic extract of the leaves is effective in the treatment of migraine in women”, Phytomedicine 20(10), 2013',
             'https://pubmed.ncbi.nlm.nih.gov/23639189/'],
        ],
        rel=['pasiflora', 'kediotu'],
        en=dict(
            name='Pronto alivio',
            other='It has no established Turkish name, and Turkey does not '
                  'appear in Kew’s distribution records. Spanish "pronto '
                  'alivio" (quick relief), in Brazil "erva cidreira" and '
                  '"falsa melissa"; English bushy matgrass. Although the '
                  'name evokes lemon balm, lemon balm (Melissa officinalis) '
                  'is a different plant. Neither the European Medicines '
                  'Agency nor the Turkish agency has a monograph for this '
                  'species.',
            part='Leaves and flowering stems',
            uses=[
                ['Tropical America — digestion, breathing and as a sedative',
                 'A review in the Journal of Ethnopharmacology records the '
                 'species being used mainly for digestive and respiratory '
                 'ailments, and as a sedative and antihypertensive remedy. '
                 'The review notes that some of these uses may be explained '
                 'by the plant’s anti-infective and analgesic properties.'],
                ['The chemotype problem — seven different plants under one name',
                 'The same review states that **seven separate chemotypes** '
                 'exist in the species’ essential oil. This means two plants '
                 'carrying the same Latin name can differ markedly in scent '
                 'and in active compounds; the review stresses that this '
                 'variability matters for the validity of research results.'],
            ],
            prep='No official monograph sets an accepted dose. What the '
                 'clinical studies relied on here used was a '
                 '**hydroalcoholic extract** of the leaves, and they were '
                 'carried out with one particular chemotype '
                 '(geranial-carvenone); that is not the same thing as a tea '
                 'brewed at home. Because the review states that essential '
                 'oil composition varies by chemotype, a plant in hand '
                 'cannot be assumed to match the one studied.',
            science='The review in the Journal of Ethnopharmacology states '
                    'that **partial, positive** results have been obtained '
                    'for sedative and anxiolytic effects, but that well '
                    'conducted biological studies are still needed for '
                    'several of the species’ indications. Two studies in '
                    'Phytomedicine tested the hydroalcoholic extract in '
                    'migraine: the first is a phase 2, **non-controlled** '
                    'cohort study reporting that more than 80% of patients '
                    'had at least a halving of pain intensity and frequency; '
                    'the second, with 21 women, is again **non-controlled** '
                    'and reports falls in MIDAS and HIT-6 scores with more '
                    'than 70% of patients having at least a halving of pain '
                    'frequency. Neither had a placebo arm, so these results '
                    'were not compared against placebo, and in a fluctuating '
                    'complaint such as migraine uncontrolled studies can '
                    'read far too optimistically. Both studies used a single '
                    'chemotype.',
            safety='The two clinical studies relied on here reported no '
                   'adverse effects, but they were small and uncontrolled, '
                   'which does not mean safety was demonstrated. The '
                   'plant’s traditional use is sedative and '
                   'blood-pressure-lowering, so **care is needed for people '
                   'taking sleep or anxiety medicines and blood-pressure '
                   'medicines.** Because of chemotype variability the '
                   'composition of a plant in hand is unknown. The sources '
                   'relied on here contain no separate assessment for '
                   'pregnancy, lactation or children, and as there is no '
                   'monograph there is no official list of '
                   'contraindications.',
            fact='Two plants bearing the same Latin name can differ in scent '
                 'and in active compounds: the review counts seven '
                 'chemotypes in this species, while the clinical studies '
                 'tested only one of them.',
            season='It does not grow in Turkey; the sources relied on here '
                   'give no collection calendar for Turkey.',
            habitat='According to Kew’s records its range covers 56 '
                    'regions: open, humid places in tropical and '
                    'subtropical America. It has also naturalised on other '
                    'continents.',
            local='No Turkish regional name. Local names: pronto alivio, '
                  'erva cidreira, falsa melissa.',
            confusion='It can be confused with lemon balm (Melissa '
                      'officinalis) and lemongrass (Cymbopogon); all three '
                      'smell of lemon and all three are separate plants. '
                      'Since chemotypes of this one species also smell '
                      'different from each other, scent alone is not an '
                      'identifying criterion.',
        ),
    ),

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='kuasya',
        foto='Quassia amara11.JPG',
        tr='Kuasya',
        la='Quassia amara L.',
        taxon='Quassia amara',
        fam='Simaroubaceae',
        diger='Türkçede yerleşik bir adı yoktur; kuasya, acı ağaç ve '
              '"acı kabuk" adlarıyla geçer. İngilizce bitterwood, amargo, '
              'Surinam quassia. Tür adı "amara" acı demektir; odunundaki '
              'kuassin bilinen en acı doğal maddelerden biri sayılır. Bu '
              'türün ne Avrupa İlaç Ajansı’nda ne TİTCK’de monografı '
              'vardır.',
        bolge=['amazon'],
        kat=['sifa'],
        kisim='Odun ve kabuk',
        kul=[
            ['Tropik Amerika — acı tonik ve haricî kullanım',
             'Current Drug Safety’de yayımlanan Güney Amerika taramasına '
             'göre Quassia amara, Arjantin’de kendi kendine ilaç olarak en '
             'sık kullanılan bitkiler arasındadır; tarama Buenos Aires '
             'eyaletinde 73 eczanede bir yıl boyunca 37.102 kendi kendine '
             'kullanılan bitkiye karşılık yalnızca 1.532 hekim reçetesi '
             'saymıştır. Aynı derleme kendi kendine kullanımın asıl riski '
             'olduğunu, kontrendikasyonların ve etkileşimlerin hesaba '
             'katılmasıyla yan etkilerin önlenebileceğini belirtir.'],
            ['Dermatoloji — %4’lük jel olarak',
             'Bitkinin insanda sınanmış kullanımı ağızdan değil '
             '**cilde sürülen özüttür.** Antiparazitik ve iltihap giderici '
             'özellikleri bildirildiği için %4’lük Quassia amara özütü '
             'içeren jel rozasea ve yüz seboreik dermatitinde '
             'denenmiştir.'],
        ],
        haz='Resmî bir monografta kabul edilmiş bir doz yoktur. Dayanak '
            'alınan insan çalışmalarında kullanılan şey **%4’lük '
            'standardize özüt içeren hazır jeldir** ve haricen '
            'uygulanmıştır; evde hazırlanan bir kaynatma ile aynı şey '
            'değildir. Ağızdan kullanım için dayanak alınan kaynaklarda '
            'kabul edilmiş bir ölçü yoktur.',
        bilim='Journal of Drugs in Dermatology’de yayımlanan '
              '**randomize, çift kör** karşılaştırmalı çalışma, yüz '
              'seboreik dermatiti olan 60 hastayı üç kola ayırıp dört '
              'hafta boyunca %4 Quassia amara jeli, %2 ketokonazol jeli ya '
              'da %1 siklopiroksolamin jeli vermiş; 54 hasta çalışmayı '
              'bitirmiş, üç seçenek de etkili bulunmuş, kuasya özütü '
              'etkililikte **anlamlı bir üstünlük** göstermiştir. Journal '
              'of Clinical Pharmacology’deki çalışma aynı jeli rozaseada '
              'denemiştir; ancak bu çalışma tek merkezli ve **açık '
              'etiketlidir** (plasebo ya da karşılaştırma kolu yoktur), 30 '
              'hastanın 27’si tamamlamıştır. İki çalışma da aynı araştırmacı '
              'çevresinden gelir ve küçüktür. Ağızdan kullanım için '
              'insanda yapılmış kontrollü bir çalışma dayanak alınan '
              'kaynaklarda yoktur; sıtma ve mikroplara karşı bildirilen '
              'etkiler **hayvan ve laboratuvar** çalışmalarından gelir.',
        kanit='sinirli',
        guv='orta',
        guvNot='İnsanda sınanmış olan tek kullanım biçimi haricî %4’lük '
               'jeldir; iki çalışmada da güvenlik ve tolere edilebilirlik '
               'iyi bulunmuştur. **Ağızdan kullanım aynı şey değildir** ve '
               'bu kaydın güvenlik düzeyini belirleyen şey odur. '
               '**Gebelikte ve emzirirken ağızdan alınmamalıdır.** Kaydın '
               'kullanılan kısmı olan odun ve kabuk, kuasin adlı bileşiği '
               'taşır; bu bileşik üzerine **hayvan** çalışmalarında '
               'tutarlı bir üreme toksisitesi bildirilmiştir. Erkek '
               'sıçanlarda testis ağırlığı, sperm sayısı ve testosteron '
               'düzeyinde düşüş bulunmuş (Life Sci 1997; Reprod Toxicol '
               '2003); dişi sıçanlarda ağızdan verilen kuasinle over '
               'ağırlığında ve yavru sayısında düşüş bildirilmiştir '
               '(Niger J Physiol Sci 2010). **Bunlar hayvan '
               'çalışmalarıdır; insanda üreme etkisi ölçülmemiştir** — ama '
               'insanda bir güvenlik verisi de bulunmadığı için ihtiyat '
               'gerekir. Çocuklarda ve doğurganlık çağında ağızdan '
               'kullanımdan kaçınılmalıdır. Güney Amerika taramasında '
               'bitki kendi kendine en sık kullanılanlar arasında geçer ve '
               'derleme asıl riskin bu denetimsiz kullanım olduğunu '
               'söyler. Monograf bulunmadığı için resmî bir '
               'kontrendikasyon listesi yoktur.',
        ilginc='Acılığıyla tanınan bu Amazon ağacının insanda kontrollü '
               'çalışmayla sınanmış tek etkisi yüz derisindedir: '
               'randomize çift kör bir çalışmada %4’lük jeli, seboreik '
               'dermatitte iki reçeteli kremle yarışıp öne geçti.',
        ek=dict(
            mevsim='Türkiye’de yetişmez; dayanak alınan kaynaklarda '
                   'Türkiye için bir toplama takvimi yoktur. Odun ve kabuk '
                   'yıl boyu toplanır.',
            yetisme='Kew’in kayıtlarına göre yayılışı 33 bölgeyi kapsar; '
                    'Amazon havzası, Orta Amerika ve Karayipler’in nemli '
                    'ormanları. Küçük bir ağaç ya da çalıdır.',
            yoresel='Türkçe yöresel adı yok. Yerel adları: quassia, '
                    'amargo, hombre grande.',
            karisma='Jamaika kuasyası (Picrasma excelsa) ayrı bir türdür '
                    've aynı adla satılabilir. Piyasadaki "acı ağaç" '
                    'ürünlerinin hangi türden geldiği etiketten '
                    'anlaşılmayabilir.',
        ),
        kaynak=[
            ['Quassia amara L., World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['C. Diehl ve A. Ferrari, “Efficacy of topical 4% Quassia amara gel in facial seborrheic dermatitis: a randomized, double-blind, comparative study”, Journal of Drugs in Dermatology 12(3), 2013',
             'https://pubmed.ncbi.nlm.nih.gov/23545914/'],
            ['A. Ferrari ve C. Diehl, “Evaluation of the efficacy and tolerance of a topical gel with 4% quassia extract in the treatment of rosacea”, Journal of Clinical Pharmacology 52(1), 2012',
             'https://pubmed.ncbi.nlm.nih.gov/21343346/'],
            ['A. E. Consolini ve ark., “Patterns of self-medication with medicinal plants and related adverse events — a South American survey”, Current Drug Safety 5(4), 2010',
             'https://pubmed.ncbi.nlm.nih.gov/20615178/'],
            ['Y. Raji ve A. F. Bolarinwa, “Antifertility activity of Quassia amara in male rats — in vivo study”, Life Sciences 61(11), 1997',
             'https://pubmed.ncbi.nlm.nih.gov/9307052/'],
            ['S. Parveen ve ark., “A comprehensive evaluation of the reproductive toxicity of Quassia amara in male rats”, Reproductive Toxicology 17(1), 2003',
             'https://pubmed.ncbi.nlm.nih.gov/12507657/'],
            ['Y. Raji ve ark., “Reproductive activities of female albino rats treated with quassin, a bioactive triterpenoid from stem bark extract of Quassia amara”, Nigerian Journal of Physiological Sciences 25(2), 2010',
             'https://pubmed.ncbi.nlm.nih.gov/22314945/'],
            ['E. O. Ajaiyeoba ve ark., “In vivo antimalarial activities of Quassia amara and Quassia undulata plant extracts in mice”, Journal of Ethnopharmacology 67(3), 1999',
             'https://pubmed.ncbi.nlm.nih.gov/10617067/'],
        ],
        rel=['kinin', 'pauarco'],
        en=dict(
            name='Quassia',
            other='It has no established Turkish name; it appears as '
                  'kuasya, acı ağaç and "acı kabuk". English bitterwood, '
                  'amargo, Surinam quassia. The species name "amara" means '
                  'bitter; quassin in its wood is counted among the most '
                  'bitter natural substances known. Neither the European '
                  'Medicines Agency nor the Turkish agency has a monograph '
                  'for this species.',
            part='Wood and bark',
            uses=[
                ['Tropical America — bitter tonic and topical use',
                 'According to a South American survey in Current Drug '
                 'Safety, Quassia amara is among the plants most often used '
                 'in self-medication in Argentina; over one year in 73 '
                 'pharmacies of Buenos Aires province the survey counted '
                 '37,102 self-medicated plants against only 1,532 '
                 'physician-prescribed ones. The same review holds that '
                 'self-medication is the main risk and that adverse '
                 'reactions could be avoided by taking contraindications '
                 'and interactions into account.'],
                ['Dermatology — as a 4% gel',
                 'The use tested in humans is not oral but **extract '
                 'applied to the skin.** Because antiparasitic and '
                 'anti-inflammatory properties have been reported, a gel '
                 'containing 4% Quassia amara extract has been tried in '
                 'rosacea and facial seborrhoeic dermatitis.'],
            ],
            prep='No official monograph sets an accepted dose. What the '
                 'human studies relied on here used was a **ready-made gel '
                 'containing 4% standardised extract**, applied topically; '
                 'that is not the same thing as a decoction made at home. '
                 'The sources relied on here give no accepted measure for '
                 'oral use.',
            science='A **randomised, double-blind** comparative study in the '
                    'Journal of Drugs in Dermatology divided 60 patients '
                    'with facial seborrhoeic dermatitis into three arms and '
                    'gave 4% Quassia amara gel, 2% ketoconazole gel or 1% '
                    'ciclopirox olamine gel for four weeks; 54 patients '
                    'completed the study, all three options were effective, '
                    'and the quassia extract showed a **significant '
                    'advantage** in efficacy. A study in the Journal of '
                    'Clinical Pharmacology tried the same gel in rosacea, '
                    'but it was single-centre and **open-label** (no placebo '
                    'or comparator arm), with 27 of 30 patients completing. '
                    'Both studies are small and come from the same circle of '
                    'investigators. The sources relied on here contain no '
                    'controlled human study of oral use; reported effects '
                    'against malaria and microbes come from **animal and '
                    'laboratory** work.',
            safety='The only form tested in humans is a topical 4% gel, and '
                   'safety and tolerability were good in both studies. '
                   '**Oral use is not the same thing**, and that is what '
                   'sets the safety level of this record. **It must not be '
                   'taken orally during pregnancy or breastfeeding.** The '
                   'wood and bark used here carry a compound called '
                   'quassin, and **animal** studies report a consistent '
                   'reproductive toxicity for it. In male rats, testis '
                   'weight, sperm count and testosterone levels fell (Life '
                   'Sci 1997; Reprod Toxicol 2003); in female rats, oral '
                   'quassin lowered ovary weight and litter size (Niger J '
                   'Physiol Sci 2010). **These are animal studies; no '
                   'reproductive effect has been measured in humans** — but '
                   'since there is no human safety data either, caution is '
                   'warranted. Oral use should be avoided in children and '
                   'by anyone of childbearing age. The South American '
                   'survey lists the plant among those most often '
                   'self-medicated, and the review holds that this '
                   'unsupervised use is the real risk. As there is no '
                   'monograph there is no official list of '
                   'contraindications.',
            fact='The only effect of this famously bitter Amazonian tree '
                 'tested in humans by a controlled study is on the skin of '
                 'the face: in a randomised double-blind trial its 4% gel '
                 'ran against two prescription creams in seborrhoeic '
                 'dermatitis and came out ahead.',
            season='It does not grow in Turkey; the sources relied on here '
                   'give no collection calendar for Turkey. Wood and bark '
                   'are gathered year-round.',
            habitat='According to Kew’s records its range covers 33 '
                    'regions: humid forests of the Amazon basin, Central '
                    'America and the Caribbean. It is a small tree or '
                    'shrub.',
            local='No Turkish regional name. Local names: quassia, amargo, '
                  'hombre grande.',
            confusion='Jamaica quassia (Picrasma excelsa) is a separate '
                      'species and may be sold under the same name. Which '
                      'species a "bitterwood" product comes from may not be '
                      'clear from the label.',
        ),
    ),

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='ananas',
        foto='Im Palmengarten - Ananas (Ananas comosus) 02.jpg',
        tr='Ananas',
        la='Ananas comosus (L.) Merr.',
        taxon='Ananas comosus',
        fam='Bromeliaceae (ananasgiller)',
        diger='Türkçede ananas; İngilizce pineapple, Portekizce abacaxi, '
              'İspanyolca piña. Ad, Tupi dilindeki "nanas" sözünden gelir. '
              'Meyvenin enzim karışımına **bromelain** denir ve '
              'araştırmaların çoğu meyvenin kendisiyle değil bu karışımla '
              'yapılmıştır. Bu türün ne Avrupa İlaç Ajansı’nda ne TİTCK’de '
              'monografı vardır.',
        bolge=['amazon'],
        kat=['besin', 'sifa'],
        kisim='Meyve; eczacılıkta gövde ve meyveden elde edilen enzim '
              'karışımı (bromelain)',
        kul=[
            ['Güney Amerika — meyve olarak',
             'Food Research International’daki derleme ananası tropik bir '
             'meyve olarak tanıtır, mineral ve vitamin bakımından zengin '
             'olduğunu, muz ve turunçgillerin ardından dünyada en çok talep '
             'gören üçüncü meyve olduğunu yazar. Aynı derleme meyvenin '
             'kokusunu veren çok sayıda uçucu bileşiği ve gıda sanayisinde '
             'işlenme biçimlerini ele alır.'],
            ['Günümüz — bromelain olarak',
             'Nutrition and Health’teki sistematik derleme, ananasın '
             'etnofarmakolojide önemli bir yeri olduğunu ve enzimi '
             'bromelainin tıbbi özellikleri için kapsamlı biçimde '
             'incelendiğini belirtir. Bugün bromelain ameliyat sonrası '
             'şişlik ve ağrıda, sinüzitte ve yara bakımında denenmektedir; '
             'bu kullanımlar meyveyi yemekten değil, standardize edilmiş '
             'enzim ürünlerinden gelir.'],
        ],
        haz='Resmî bir monografta kabul edilmiş bir doz yoktur; ananas bir '
            'gıdadır. Dayanak alınan çalışmalarda kullanılan şey **ağızdan '
            'alınan standardize bromelain ürünleri ya da yaraya sürülen '
            'bromelain hazırlıklarıdır**; meyveyi yemek ya da suyunu içmek '
            'bunlarla aynı şey değildir. Derleme, ağızdan alındıktan sonra '
            'bromelainin kanda proteini parçalayıcı etkinliğini '
            'koruduğunu bildirir.',
        bilim='Nutrition and Health’te yayımlanan sistematik derleme ve '
              'meta-analiz 54 yayını niteliksel olarak, 39’unu '
              'meta-analizle incelemiştir. Bulgular: bromelain '
              '**sinüzitte etkili olabilir, kalp-damar hastalıklarında '
              'etkili değildir.** Ağızdan alınan bromelainle ağrıda '
              'kontrollere göre küçük ama anlamlı bir azalma bulunmuştur '
              '(ağrı puanında ortalama fark −0,27; %95 GA −0,45 ile −0,08; '
              '9 çalışma). Cilde uygulanan bromelain yara temizliğinin '
              'tamamlanma süresini anlamlı biçimde kısaltmıştır (ortalama '
              'fark −6,89 gün; %95 GA −7,94 ile −5,83; 4 çalışma). '
              'Yazarlar kanıtı **orta kalitede** bulmuş, ağızdan '
              'bromelainin ağrı denetiminde, haricî bromelainin yara '
              'bakımında umut verdiğini yazmıştır. Nutrients’ta '
              'yayımlanan randomize, plasebo kontrollü üç kollu çalışma, '
              'alt çene üçüncü azı dişi cerrahisinden sonra liyofilize '
              'ananas özütü ya da saflaştırılmış bromelain verilen '
              'hastalarda ağrı ve şişlikte plaseboya göre anlamlı azalma, '
              'ibuprofen gereksiniminde anlamlı düşüş bulmuş; çene '
              'kilitlenmesinde anlamlı fark bulmamıştır (42 hasta).',
        kanit='klinik',
        guv='dusuk',
        guvNot='Ananas yaygın bir gıdadır. Sistematik derleme bromelain '
               'tedavisi sırasında **önemli bir sağlık riski '
               'bildirilmediğini** yazar; ağızdan alımda görülen '
               'istenmeyen etkiler gaz, bulantı ve baş ağrısıdır. Cilde '
               'uygulamada yanma hissi, ağrı, ateş ve sepsis bildirilmiş, '
               'ancak derleme bunların ilgisiz olabileceğini belirtir. '
               'Bromelain bir proteaz olduğundan **kan sulandırıcı '
               'kullananlarda ve ameliyat öncesinde dikkat gerekir;** '
               'dayanak alınan derlemede bu konuda doğrudan bir etkileşim '
               'çalışması anılmaz. Olgunlaşmamış meyve ve çok miktarda '
               'meyve suyu ağızda ve dilde yanma yapabilir. Gebelik, '
               'emzirme ve çocuklar için gıda miktarının üzerinde kullanımı '
               'değerlendiren bir kaynak yoktur.',
        ilginc='Ananasın tıpta en çok çalışılan yanı tadı değil enzimi: '
               'bromelain üzerine 54 çalışmayı derleyen meta-analiz, onu '
               'sinüzitte umut verici, kalp-damar hastalıklarında ise '
               'etkisiz buldu.',
        ek=dict(
            mevsim='Türkiye’de ticari olarak yetişmez; dayanak alınan '
                   'kaynaklarda Türkiye için bir toplama takvimi yoktur.',
            yetisme='Kew’in kayıtlarına göre yayılışı 66 bölgeyi kapsar; '
                    'tropik kuşakta yetiştirilir. Kökeni Güney '
                    'Amerika’dır; rozet biçiminde, topraktan su '
                    'gereksinimi az olan bir bromelyadır.',
            yoresel='Türkçede ananas.',
            karisma='Satılan bromelain ürünlerinin enzim etkinliği '
                    'markadan markaya değişir; meyve suyu ile standardize '
                    'enzim ürünü aynı şey değildir.',
        ),
        kaynak=[
            ['Ananas comosus (L.) Merr., World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['N. Leelakanok ve ark., “Efficacy and safety of bromelain: A systematic review and meta-analysis”, Nutrition and Health, 2023',
             'https://pubmed.ncbi.nlm.nih.gov/37157782/'],
            ['A. Colletti ve ark., “An Evaluation of the Effects of Pineapple-Extract and Bromelain-Based Treatment after Mandibular Third Molar Surgery: A Randomized Three-Arm Clinical Study”, Nutrients 16(6), 2024',
             'https://pubmed.ncbi.nlm.nih.gov/38542694/'],
            ['M. Mohd Ali ve ark., “Pineapple (Ananas comosus): A comprehensive review of nutritional values, volatile compounds, health benefits, and potential food products”, Food Research International 137, 2020',
             'https://pubmed.ncbi.nlm.nih.gov/33233252/'],
            ['U. Kansakar ve ark., “Exploring the Therapeutic Potential of Bromelain: Applications, Benefits, and Mechanisms”, Nutrients 16(13), 2024',
             'https://pubmed.ncbi.nlm.nih.gov/38999808/'],
        ],
        rel=['papaya', 'camucamu'],
        en=dict(
            name='Pineapple',
            other='Turkish ananas; English pineapple, Portuguese abacaxi, '
                  'Spanish piña. The name comes from the Tupi word "nanas". '
                  'The fruit’s mixture of enzymes is called **bromelain**, '
                  'and most research has been done not with the fruit but '
                  'with that mixture. Neither the European Medicines Agency '
                  'nor the Turkish agency has a monograph for this species.',
            part='Fruit; in pharmacy the enzyme mixture obtained from stem '
                 'and fruit (bromelain)',
            uses=[
                ['South America — as a fruit',
                 'A review in Food Research International presents the '
                 'pineapple as a tropical fruit, rich in minerals and '
                 'vitamins, ranked third in world demand behind banana and '
                 'citrus. The same review covers the many volatile compounds '
                 'that give the fruit its aroma and the ways it is processed '
                 'in the food industry.'],
                ['Today — as bromelain',
                 'A systematic review in Nutrition and Health notes that the '
                 'pineapple has an important place in ethnopharmacology and '
                 'that its enzyme bromelain has been extensively '
                 'investigated for medicinal properties. Bromelain is now '
                 'tried for post-operative swelling and pain, for sinusitis '
                 'and in wound care; these uses come not from eating the '
                 'fruit but from standardised enzyme products.'],
            ],
            prep='No official monograph sets an accepted dose; the pineapple '
                 'is a food. What the studies relied on here used were '
                 '**standardised oral bromelain products or bromelain '
                 'preparations applied to wounds**; eating the fruit or '
                 'drinking its juice is not the same thing. The review '
                 'reports that bromelain retains proteolytic activity in '
                 'serum after oral absorption.',
            science='The systematic review and meta-analysis in Nutrition '
                    'and Health included 54 articles qualitatively and 39 in '
                    'meta-analysis. Its findings: bromelain **may be '
                    'effective in sinusitis and is not effective in '
                    'cardiovascular disease.** Oral bromelain gave a small '
                    'but significant reduction in pain compared with '
                    'controls (mean difference in pain score −0.27; 95% CI '
                    '−0.45 to −0.08; 9 studies). Topical bromelain '
                    'significantly shortened the time to complete '
                    'debridement (mean difference −6.89 days; 95% CI −7.94 '
                    'to −5.83; 4 studies). The authors judged the evidence '
                    '**moderate quality** and wrote that oral bromelain '
                    'shows promise in pain control and topical bromelain in '
                    'wound care. A randomised, placebo-controlled three-arm '
                    'study in Nutrients found that after mandibular third '
                    'molar surgery, patients given lyophilised pineapple '
                    'extract or purified bromelain had significantly less '
                    'pain and swelling and significantly less need for '
                    'ibuprofen than placebo, with no significant difference '
                    'in trismus (42 patients).',
            safety='The pineapple is a common food. The systematic review '
                   'states that **no major health risks were reported** '
                   'during bromelain treatment; the adverse events seen with '
                   'oral use are flatulence, nausea and headache. With '
                   'topical use, burning, pain, fever and sepsis were '
                   'reported, though the review notes these may be '
                   'irrelevant. As bromelain is a protease, **care is needed '
                   'for people on blood thinners and before surgery;** the '
                   'review relied on here cites no direct interaction study '
                   'on this. Unripe fruit and large amounts of juice can '
                   'burn the mouth and tongue. No source assesses use above '
                   'food amounts in pregnancy, lactation or children.',
            fact='The most-studied thing about the pineapple in medicine is '
                 'not its taste but its enzyme: a meta-analysis pooling 54 '
                 'studies of bromelain found it promising in sinusitis and '
                 'ineffective in cardiovascular disease.',
            season='It is not grown commercially in Turkey; the sources '
                   'relied on here give no collection calendar for Turkey.',
            habitat='According to Kew’s records its range covers 66 '
                    'regions; it is cultivated across the tropics. Its '
                    'origin is South America, and it is a rosette-forming '
                    'bromeliad with modest water needs.',
            local='Turkish ananas.',
            confusion='The enzyme activity of bromelain products on sale '
                      'varies between brands; fruit juice and a '
                      'standardised enzyme product are not the same thing.',
        ),
    ),

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='carkifelekmeyvesi',
        foto='Passiflora edulis flower in Hong Kong Mar 9 2013.JPG',
        tr='Çarkıfelek meyvesi',
        la='Passiflora edulis Sims',
        taxon='Passiflora edulis',
        fam='Passifloraceae (çarkıfelekgiller)',
        diger='Türkçede çarkıfelek meyvesi, passion meyvesi; İngilizce '
              'passion fruit, Portekizce maracujá. **Avrupa İlaç '
              'Ajansı’nın çarkıfelek monografı bu türe ait değildir:** '
              'Passiflorae herba monografı Passiflora incarnata L. '
              'içindir. Bu tür meyvesi için yetiştirilir ve TİTCK’de de '
              'monografı yoktur. Sarı (f. flavicarpa) ve mor (f. edulis) '
              'olmak üzere iki biçimi vardır.',
        bolge=['amazon'],
        kat=['besin'],
        kisim='Meyve; çalışmalarda ayrıca kabuk unu ve tohum özütü',
        kul=[
            ['Tropik ve astropik bölgeler — meyve olarak',
             'Frontiers in Pharmacology’deki derleme, bitkinin dünyanın '
             'tropik ve astropik bölgelerinde yaygın olarak yetiştiğini ve '
             'dengeli besin değeri ile yaygınlaştığını yazar. Derlemeye '
             'göre bitkinin farklı kısımlarından **110’dan fazla bileşik** '
             'tanımlanmıştır; en büyük payı flavonoitler ve triterpenoitler '
             'tutar.'],
            ['Araştırmada — meyve dışındaki kısımlar',
             'Aynı derleme yaprak, gövde, meyve ve kabuğun özütleri ile '
             'meyve suyunun antioksidan, tansiyon düşürücü, tümöre karşı, '
             'şeker düşürücü ve kan yağlarını düşürücü etkiler '
             'gösterdiğini bildirir. Bu etkilerin çoğu hücre ve hayvan '
             'çalışmalarından gelir; insanda sınananlar aşağıda.'],
        ],
        haz='Resmî bir monografta kabul edilmiş bir doz yoktur; çarkıfelek '
            'meyvesi bir gıdadır. İnsan çalışmalarında kullanılan şey '
            'meyvenin kendisi değil, **tohumdan elde edilen pikeatannol '
            'kapsülü (günde 20 mg)** ve **sarı meyvenin kabuk unudur**; '
            'bunlar meyveyi yemekle aynı şey değildir. Derleme, günlük '
            'olağan miktarlarda meyve tüketiminin zehirli olmadığını ve '
            'güvenli olduğunu belirtir.',
        bilim='Frontiers in Pharmacology’deki derleme, olağan dozlarda '
              'günlük tüketimin zehirli olmadığını yazar ve bitkinin geniş '
              'bir etki yelpazesi için araştırıldığını özetler. İnsanda '
              'yapılmış iki çalışma vardır. Nutrients’taki randomize, '
              'plasebo kontrollü çalışmada tohumdan elde edilen '
              'pikeatannol (günde 20 mg) sekiz hafta boyunca 39 kişiye '
              'verilmiş; **yalnızca fazla kilolu erkeklerde** serum '
              'insülini, HOMA-IR, tansiyon ve kalp hızında düşüş '
              'görülmüştür. Fazla kilolu olmayan erkeklerde ve kadınların '
              'hiçbir kümesinde insülin duyarlılığı, tansiyon ve kalp '
              'hızında yarar bulunmamış; vücut ağırlığı, beden bileşimi, '
              'damar işlevi, kan yağları, iltihap ve oksidatif stres '
              'göstergelerinde de etki saptanmamıştır. Nutrition '
              'Journal’da yayımlanan çalışma sarı çarkıfelek kabuğu '
              'ununun etkisini incelemiştir. Yani insanda ölçülmüş '
              'bulgular **tek bir alt kümeye sınırlıdır** ve meyvenin '
              'kendisiyle değil ondan ayrılmış bileşenlerle elde '
              'edilmiştir.',
        kanit='sinirli',
        guv='dusuk',
        guvNot='Derleme, meyvenin olağan miktarlarda günlük tüketiminin '
               'zehirli olmadığını ve güvenli olduğunu belirtir. '
               'Olgunlaşmamış meyve ekşi ve sert olduğu için yenmez. '
               'Dayanak alınan kaynaklarda gebelik, emzirme ve çocuklar '
               'için gıda miktarının üzerinde kullanımı değerlendiren bir '
               'kaynak yoktur. **Çarkıfelek çayı diye satılan ürün '
               'genellikle bu tür değildir:** yatıştırıcı kullanımı olan '
               've Avrupa İlaç Ajansı monografı bulunan bitki Passiflora '
               'incarnata’dır; bu kayıttaki bulgular ona uygulanmaz, '
               'onunkiler de buraya. Tohum özütü (pikeatannol) kapsülü bir '
               'gıda takviyesidir ve insanda yarar görülen tek küme fazla '
               'kilolu erkeklerdir.',
        ilginc='Pazarda "çarkıfelek" iki ayrı bitkinin adı: meyvesini '
               'yediğimiz tür (P. edulis) ile yatıştırıcı olarak '
               'monografı bulunan tür (P. incarnata) aynı cinsten ama '
               'birinin kanıtı ötekine geçmiyor.',
        ek=dict(
            mevsim='Türkiye’de Akdeniz kıyılarında ve seralarda '
                   'yetiştirilir; meyveler yazdan sonbahara olgunlaşır. '
                   'Dayanak alınan kaynaklarda şifa amacıyla bir toplama '
                   'takvimi yoktur.',
            yetisme='Kew’in kayıtlarına göre yayılışı 92 bölgeyi kapsar; '
                    'tropik ve astropik kuşakta yetiştirilir. Sarılıcı bir '
                    'bitkidir, kökeni Güney Amerika’dır.',
            yoresel='Türkçede çarkıfelek meyvesi, passion meyvesi.',
            karisma='Passiflora incarnata ile karıştırılması asıl risktir: '
                    'o tür yatıştırıcı olarak kullanılır ve monografı '
                    'vardır, bu tür meyvesi için yetiştirilir. Süs olarak '
                    'yetiştirilen P. caerulea’nın meyvesi yenmez.',
        ),
        kaynak=[
            ['Passiflora edulis Sims, World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['X. He ve ark., “Passiflora edulis: An Insight Into Current Researches on Phytochemistry and Pharmacology”, Frontiers in Pharmacology 11, 2020',
             'https://pubmed.ncbi.nlm.nih.gov/32508631/'],
            ['M. Kitada ve ark., “The Effect of Piceatannol from Passion Fruit (Passiflora edulis) Seeds on Metabolic Health in Humans”, Nutrients 9(10), 2017',
             'https://pubmed.ncbi.nlm.nih.gov/29057795/'],
            ['M. S. de Queiroz ve ark., “Effect of the yellow passion fruit peel flour (Passiflora edulis f. flavicarpa deg.) in insulin sensitivity in type 2 diabetes mellitus patients”, Nutrition Journal 11, 2012',
             'https://pubmed.ncbi.nlm.nih.gov/23088514/'],
        ],
        rel=['pasiflora', 'camucamu'],
        en=dict(
            name='Passion fruit',
            other='Turkish çarkıfelek meyvesi, passion meyvesi; English '
                  'passion fruit, Portuguese maracujá. **The European '
                  'Medicines Agency’s passionflower monograph does not '
                  'belong to this species:** the Passiflorae herba '
                  'monograph is for Passiflora incarnata L. This species is '
                  'grown for its fruit and the Turkish agency has no '
                  'monograph for it either. It has two forms, yellow (f. '
                  'flavicarpa) and purple (f. edulis).',
            part='Fruit; in studies also peel flour and seed extract',
            uses=[
                ['Tropical and subtropical regions — as a fruit',
                 'A review in Frontiers in Pharmacology writes that the '
                 'plant is widely distributed through the tropical and '
                 'subtropical regions of the world and has become popular '
                 'for its balanced nutrition. According to the review, '
                 '**more than 110 compounds** have been identified from the '
                 'plant’s different parts, with flavonoids and triterpenoids '
                 'holding the largest share.'],
                ['In research — the parts other than the fruit',
                 'The same review reports that extracts of leaf, stem, fruit '
                 'and peel, and the fruit juice, have shown antioxidant, '
                 'antihypertensive, antitumour, antidiabetic and '
                 'lipid-lowering effects. Most of these come from cell and '
                 'animal work; what has been tested in humans is below.'],
            ],
            prep='No official monograph sets an accepted dose; passion fruit '
                 'is a food. What the human studies used was not the fruit '
                 'itself but **piceatannol capsules from the seed (20 mg a '
                 'day)** and **the peel flour of the yellow form**; these '
                 'are not the same as eating the fruit. The review states '
                 'that daily consumption of the fruit at common doses is '
                 'non-toxic and safe.',
            science='The review in Frontiers in Pharmacology states that '
                    'daily consumption at common doses is non-toxic and '
                    'safe, and summarises the breadth of effects the plant '
                    'has been studied for. There are two human studies. In '
                    'the randomised, placebo-controlled study in Nutrients, '
                    'piceatannol from the seed (20 mg a day) was given to 39 '
                    'people for eight weeks; serum insulin, HOMA-IR, blood '
                    'pressure and heart rate fell **only in overweight '
                    'men.** No benefit to insulin sensitivity, blood '
                    'pressure or heart rate was found in non-overweight men '
                    'or in any group of women, and no effect was detected on '
                    'body weight, body composition, endothelial function, '
                    'lipids, inflammation or oxidative stress. A study in '
                    'Nutrition Journal examined the effect of yellow passion '
                    'fruit peel flour. The findings measured in humans are '
                    'therefore **confined to a single subgroup** and were '
                    'obtained not with the fruit itself but with components '
                    'separated from it.',
            safety='The review states that daily consumption of the fruit at '
                   'common doses is non-toxic and safe. Unripe fruit is sour '
                   'and hard and is not eaten. The sources relied on here '
                   'contain no assessment of use above food amounts in '
                   'pregnancy, lactation or children. **A product sold as '
                   '"passionflower tea" is usually not this species:** the '
                   'plant with sedative use and a European Medicines Agency '
                   'monograph is Passiflora incarnata; the findings in this '
                   'record do not apply to it, nor its findings here. The '
                   'seed-extract (piceatannol) capsule is a food supplement, '
                   'and the only group showing benefit in humans was '
                   'overweight men.',
            fact='"Passionflower" names two different plants on the market: '
                 'the species whose fruit we eat (P. edulis) and the species '
                 'with a sedative monograph (P. incarnata) share a genus, '
                 'but the evidence for one does not carry to the other.',
            season='It is grown on Turkey’s Mediterranean coast and in '
                   'greenhouses, with fruit ripening from summer into '
                   'autumn. The sources relied on here give no collection '
                   'calendar for medicinal use.',
            habitat='According to Kew’s records its range covers 92 '
                    'regions; it is cultivated through the tropics and '
                    'subtropics. It is a climber, and its origin is South '
                    'America.',
            local='Turkish çarkıfelek meyvesi, passion meyvesi.',
            confusion='Confusion with Passiflora incarnata is the real '
                      'risk: that species is used as a sedative and has a '
                      'monograph, while this one is grown for its fruit. '
                      'The fruit of the ornamental P. caerulea is not '
                      'eaten.',
        ),
    ),

    dict(
        yayin='2026-11-26',
        arsiv=True,
        id='chaliponga',
        foto='Hojas del yagé (Diplopterys cabrerana).jpg',
        tr='Chaliponga',
        la='Diplopterys cabrerana (Cuatrec.) B.Gates',
        taxon='Diplopterys cabrerana',
        fam='Malpighiaceae',
        diger='Türkçede adı yoktur. Yerel adları chaliponga, chagropanga, '
              'chagrupanga ve oco yagé; eski botanik yazısında '
              'Banisteriopsis rusbyana adıyla da geçer. Amazon’un '
              'kuzeybatısında ayahuasca kaynatmasına **katkı bitkisi** '
              'olarak girer. Bu türün ne Avrupa İlaç Ajansı’nda ne '
              'TİTCK’de monografı vardır. **İçerdiği DMT Türkiye’de '
              'kontrollü maddedir.**',
        bolge=['amazon'],
        kat=['ritual'],
        kisim='Yapraklar',
        kul=[
            ['Kuzeybatı Amazon — ayahuasca kaynatmasının katkı bitkisi',
             'Journal of Addictions Nursing’deki yazı ayahuascayı, '
               'monoamin oksidaz inhibitörü taşıyan Banisteriopsis caapi '
               'kabuğu ile serotonin 2A reseptör agonisti N,N-dimetiltriptamin '
               '(DMT) taşıyan Psychotria viridis **ya da Diplopterys '
               'cabrerana** yapraklarından yapılan bir karışım olarak '
               'tanımlar. Yani bu bitki tek başına değil, ikili bir '
               'bileşimin yarısı olarak kullanılır: biri etken maddeyi, '
               'öteki onun sindirimde yıkılmasını engelleyen inhibitörü '
               'taşır.'],
            ['Tören bağlamı',
             'Aynı yazı ayahuascanın yüzyıllardır şamanik törenlerde '
             'kullanılan bir töresel içecek olduğunu ve son yıllarda '
             'Amazon dışında da yayıldığını kaydeder. Bu sayfa töresel '
             'kullanımı kültürel bir kayıt olarak anlatır, bir öneri '
             'olarak değil.'],
        ],
        haz='**Bu sayfada hazırlanışı anlatılmaz.** Bitkinin taşıdığı DMT '
            'Türkiye’de kontrollü maddedir; kaynatmanın yapılışı yasa dışı '
            'bir maddenin hazırlanışı olacağından yazılmaz. Resmî bir '
            'monografta kabul edilmiş bir doz da yoktur.',
        bilim='Bu tür üzerine insanda yapılmış bir etkililik çalışması '
              'dayanak alınan kaynaklarda yoktur; bulunan yayınların '
              'tamamı bitkiyi ayahuasca karışımının bir bileşeni olarak '
              'ele alır. Mental Health Clinician’daki derleme, '
              'ayahuascanın çağdaş psikiyatrik hastalıklarda kullanımını '
              'tartışan yayınları değerlendirir. Journal of Addictions '
              'Nursing’deki yazı, karışımın etkilerinin **kötü kalite '
              'denetimi, öngörülemezlik ve çoklu ilaç etkileşimleri** '
              'yüzünden belirsiz kaldığını vurgular. iScience’ta '
              'yayımlanan 2026 tarihli çalışma, herbaryum yapraklarından '
              'makine öğrenmesiyle Banisteriopsis caapi’nin halk '
              'sınıflandırmasını tanımaya çalışmış ve bu türü dış küme '
              'olarak kullanmıştır; yani botanik ayırt etme üzerinedir, '
              'tedavi üzerine değil.',
        kanit='geleneksel',
        guv='yuksek',
        guvNot='**DMT Türkiye’de kontrollü maddedir; bu bitki bir tedavi '
               'seçeneği değildir.** Dayanak alınan kaynaklara göre asıl '
               'tehlikeler DMT’ye bağlı psikotik ataklar ve **yaşamı '
               'tehdit edebilen serotonin sendromudur.** Karışımdaki '
               'monoamin oksidaz inhibitörü, başka serotonerjik maddelerle '
               'birlikte alındığında kişiyi serotonerjik zehirlenmeye açık '
               'hâle getirir. Cureus’ta yayımlanan olgu sunumunda 46 '
               'yaşında bir erkek, üç gün boyunca ayahuasca aldıktan sonra '
               'reçetesiz dekstrometorfan ve difenhidramin kullanmış; '
               '**akut solunum yetmezliğiyle seyreden ağır serotonin '
               'sendromu** gelişmiş, acil entübasyon ve yoğun bakım '
               'gerekmiş, damardan benzodiazepin ve ağızdan siproheptadin '
               'ile düzelmiştir. Kaynaklar ayrıca ürünlerin içeriğinin '
               'denetimsiz ve öngörülemez olduğunu belirtir. Gebelik, '
               'emzirme ve çocuklar için değerlendirme yoktur ve söz konusu '
               'olamaz.',
        ilginc='Bitki tek başına ağızdan alındığında etkisiz kalır: '
               'taşıdığı DMT sindirimde yıkılır. Töresel kullanımda '
               'etkinin ortaya çıkması, karışımın öteki yarısındaki '
               'monoamin oksidaz inhibitörüne bağlıdır — tehlikeli ilaç '
               'etkileşimlerinin kaynağı da aynı madde.',
        yasal='DMT, BM 1971 Psikotrop Maddeler Sözleşmesi’nin I sayılı '
              'listesinde kontrollü maddedir ve Türkiye’de yasa dışıdır. '
              'Bitkinin kendisinin hukuki durumu ülkeye göre değişir.',
        etk=[
            ['Antidepresanlar (SSRI, SNRI), triptanlar, tramadol, '
             'dekstrometorfan, linezolid',
             'Karışımdaki monoamin oksidaz inhibitörüyle birlikte '
             'serotonin sendromuna yol açabilir; bildirilmiş bir olguda '
             'tablo solunum yetmezliğine gitmiştir.'],
            ['Monoamin oksidaz inhibitörü ilaçlar',
             'Etki birikir; hipertansif kriz ve serotonerjik zehirlenme '
             'riski taşır.'],
            ['Tiramin bakımından zengin besinler (olgun peynirler, '
             'fermente ürünler)',
             'Monoamin oksidaz inhibitörü varlığında tansiyon yükselmesine '
             'yol açabilir.'],
        ],
        etk_en=[
            ['Antidepressants (SSRIs, SNRIs), triptans, tramadol, '
             'dextromethorphan, linezolid',
             'Together with the monoamine oxidase inhibitor in the brew '
             'these can cause serotonin syndrome; in one reported case the '
             'course led to respiratory failure.'],
            ['Monoamine oxidase inhibitor medicines',
             'The effects add up, carrying a risk of hypertensive crisis '
             'and serotonergic toxicity.'],
            ['Tyramine-rich foods (aged cheeses, fermented products)',
             'In the presence of a monoamine oxidase inhibitor these can '
             'raise blood pressure.'],
        ],
        ek=dict(
            mevsim='Türkiye’de yetişmez; toplama takvimi yoktur ve '
                   'toplanması söz konusu değildir.',
            yetisme='Kew’in kayıtlarına göre yayılışı yalnızca beş bölgeyi '
                    'kapsar: Brezilya’nın kuzeyi, Kolombiya, Ekvador, Peru '
                    've Venezuela. Kuzeybatı Amazon’un nemli ormanlarında '
                    'sarılıcı olarak yetişir.',
            yoresel='Türkçe adı yok. Yerel adları: chaliponga, '
                    'chagropanga, oco yagé.',
            karisma='Ayahuasca karışımında DMT kaynağı olarak chacruna '
                    '(Psychotria viridis) ile dönüşümlü kullanılır; iki '
                    'bitki akraba değildir. Asma olan Banisteriopsis '
                    'caapi ise karışımın öteki yarısıdır ve farklı '
                    'alkaloitler taşır.',
        ),
        kaynak=[
            ['Diplopterys cabrerana (Cuatrec.) B.Gates, World Checklist of Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'],
            ['D. Goldin ve ark., “Ayahuasca: What Healthcare Providers Need to Know”, Journal of Addictions Nursing 32(2), 2021',
             'https://pubmed.ncbi.nlm.nih.gov/34060770/'],
            ['S. Pack ve ark., “Severe Serotonin Syndrome With Acute Respiratory Failure Following Ayahuasca and Dextromethorphan Use: A Case Report”, Cureus, 2026',
             'https://pubmed.ncbi.nlm.nih.gov/42713547/'],
            ['B. J. Malcolm ve K. Lee, “Ayahuasca: An ancient sacrament for treatment of contemporary psychiatric illness?”, Mental Health Clinician 7(1), 2017',
             'https://pubmed.ncbi.nlm.nih.gov/29955496/'],
            ['S. C. Biazatti ve ark., “Machine learning recovers folk classification of Banisteriopsis caapi from herbarium leaves of an ayahuasca liana”, iScience, 2026',
             'https://pubmed.ncbi.nlm.nih.gov/42100741/'],
        ],
        rel=['yopo', 'chiricsanango'],
        en=dict(
            name='Chaliponga',
            other='It has no Turkish name. Local names chaliponga, '
                  'chagropanga, chagrupanga and oco yagé; in older botanical '
                  'writing it also appears as Banisteriopsis rusbyana. In '
                  'the north-west Amazon it enters the ayahuasca brew as an '
                  '**admixture plant.** Neither the European Medicines '
                  'Agency nor the Turkish agency has a monograph for this '
                  'species. **The DMT it contains is a controlled substance '
                  'in Turkey.**',
            part='Leaves',
            uses=[
                ['North-west Amazon — admixture plant of the ayahuasca brew',
                 'An article in the Journal of Addictions Nursing describes '
                 'ayahuasca as a mixture made from the bark of '
                 'Banisteriopsis caapi, which carries a monoamine oxidase '
                 'inhibitor, and the leaves of Psychotria viridis **or '
                 'Diplopterys cabrerana**, which carry the serotonin 2A '
                 'receptor agonist N,N-dimethyltryptamine (DMT). This plant '
                 'is therefore used not alone but as one half of a pairing: '
                 'one carries the active substance, the other the inhibitor '
                 'that stops it being broken down in digestion.'],
                ['The ceremonial context',
                 'The same article records ayahuasca as a traditional '
                 'psychoactive sacrament used in shamanic ceremonies for '
                 'centuries, and notes that its use has spread beyond the '
                 'Amazon in recent years. This page describes the '
                 'ceremonial use as a cultural record, not as a '
                 'recommendation.'],
            ],
            prep='**This page does not describe how it is prepared.** The '
                 'DMT the plant carries is a controlled substance in Turkey, '
                 'so setting out how the brew is made would be setting out '
                 'the preparation of an illegal substance. Nor does any '
                 'official monograph set an accepted dose.',
            science='The sources relied on here contain no efficacy study of '
                    'this species in humans; every publication found treats '
                    'the plant as a component of the ayahuasca mixture. A '
                    'review in Mental Health Clinician assesses the '
                    'literature discussing ayahuasca in contemporary '
                    'psychiatric illness. The article in the Journal of '
                    'Addictions Nursing stresses that the consequences of '
                    'the mixture remain uncertain because of **poor quality '
                    'control, unpredictability and polydrug '
                    'interactions.** A 2026 study in iScience used machine '
                    'learning on herbarium leaves to recover folk '
                    'classifications of Banisteriopsis caapi, with this '
                    'species as an outgroup; it concerns botanical '
                    'discrimination, not treatment.',
            safety='**DMT is a controlled substance in Turkey, and this '
                   'plant is not a treatment option.** According to the '
                   'sources relied on here the main dangers are psychotic '
                   'episodes related to DMT and **serotonin syndrome, which '
                   'can be life-threatening.** The monoamine oxidase '
                   'inhibitor in the mixture leaves a person open to '
                   'serotonergic toxicity when other serotonergic agents are '
                   'taken as well. In a case report in Cureus a 46-year-old '
                   'man took ayahuasca over three days and then '
                   'over-the-counter dextromethorphan and diphenhydramine; '
                   'he developed **severe serotonin syndrome complicated by '
                   'acute respiratory failure**, needed emergency intubation '
                   'and intensive care, and recovered with intravenous '
                   'benzodiazepines and oral cyproheptadine. The sources '
                   'also note that the content of such products is '
                   'unregulated and unpredictable. There is no assessment '
                   'for pregnancy, lactation or children, and none could '
                   'apply.',
            fact='Taken by mouth on its own the plant has no effect: the DMT '
                 'it carries is broken down in digestion. In ceremonial use '
                 'the effect depends on the monoamine oxidase inhibitor in '
                 'the other half of the mixture — the same substance that is '
                 'the source of the dangerous drug interactions.',
            season='It does not grow in Turkey; there is no collection '
                   'calendar and no question of collecting it.',
            habitat='According to Kew’s records its range covers only five '
                    'regions: northern Brazil, Colombia, Ecuador, Peru and '
                    'Venezuela. It grows as a climber in the humid forests '
                    'of the north-west Amazon.',
            local='No Turkish name. Local names: chaliponga, chagropanga, '
                  'oco yagé.',
            confusion='In the ayahuasca mixture it is used interchangeably '
                      'with chacruna (Psychotria viridis) as the DMT '
                      'source; the two plants are not related. '
                      'Banisteriopsis caapi, the vine, is the other half of '
                      'the mixture and carries different alkaloids.',
        ),
    ),
]
