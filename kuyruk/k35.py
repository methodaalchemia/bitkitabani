# WHO monografı partisi III (23–25 Kasım 2026): karamuk, dereotu, çayır
# üçgülü. Üçü de Anadolu'da yetişen, mutfağa ya da kıra ait bitkiler;
# üçünün de DSÖ monografı "klinik veriyle desteklenen kullanım: yok"
# diyor, üçünde de sonradan yapılmış meta-analizler var.
from kunye_elle import who_url
Q = [

    dict(
        yayin='2026-11-22',
        id='karamuk',
        foto='',
        tr='Karamuk',
        la='Berberis vulgaris L.',
        fam='Berberidaceae (karamukgiller)',
        diger='Türkçe karamuk, kadıntuzluğu, amberbaris; İngilizce barberry, '
              'European barberry; Farsça zereşk. DSÖ monografının drogu **gövde '
              'kabuğu** (Cortex Berberidis); Türkiye’de ve İran’da yenen ve '
              'çalışılan kısım ise **meyvesi**. Bu bitki için TİTCK ve AB '
              'monografı yok; kayıt DSÖ monografına (Cilt 4, 2009) ve PubMed’e '
              'dayanıyor.',
        bolge=['anadolu', 'avrupa', 'asya'],
        kat=['sifa', 'besin'],
        kisim='Kurutulmuş gövde kabuğu (DSÖ); meyvesi (gıda ve klinik '
              'çalışmalar)',
        taxon='Berberis vulgaris',
        kul=[
            ['DSÖ monografı — kabuk', 'Dünya Sağlık Örgütü monografı (Cilt 4, '
             '2009) gövde kabuğunu üç başlıkta değerlendiriyor. **Klinik '
             'veriyle desteklenen kullanım: yok.** Farmakopelerde tanımlanan '
             'kullanım: dispepsi, ishal, gastrit, dolgunluk ve gaz gibi sindirim '
             'şikâyetleri — ağızdan. Geleneksel tıpta: sistit, dismenore, '
             'egzama, ateş, basur, burun tıkanıklığı, romatizma; safra '
             'söktürücü, idrar söktürücü, tonik. Monograf açıkça yazıyor: '
             'kabukla yapılmış klinik çalışma yok; bilinen etkin madde '
             '**berberin** ve berberinin kendisi bakteriyel ishalde, '
             'trahomda ve deri leishmaniasisinde sınanmış.'],
            ['Türkiye', 'TİTCK Tıbbi Bitki Listesi’nde karamuk için monograf '
             'yok. Bitki Anadolu’da yaygın bir diken çalısı; ekşi kırmızı '
             'meyvesi kurutulup yenir, pilava katılır (İran mutfağındaki '
             'zereşk aynı meyve). Sarı kökü ve kabuğu yün boyar; "kadıntuzluğu" '
             'adı yaygın halk adıdır.'],
            ['İran — meyvenin klinik çalışmaları', 'Son yirmi yılda yapılan '
             'randomize çalışmaların neredeyse tamamı İran’dan ve DSÖ’nün '
             'drogu olan kabukla değil, **meyve** ya da meyve özütüyle '
             'yapılmış: kan yağları, kan şekeri, kan basıncı. Yani monografın '
             'bitkisi ile klinik literatürün bitkisi aynı tür, ama ayrı '
             'kısım.'],
        ],
        haz='DSÖ monografı kabuk için günlük doz veriyor: 0,5–1,0 g drog günde 3 '
            'kez, dekoksiyon olarak; sıvı özüt (1:1, %60 etanol) 0,3–1,0 ml günde '
            '3 kez; tentür (1:10) 2–4 ml günde 3 kez. Meyvenin klinik '
            'çalışmalarındaki dozlar ayrıdır (çoğunlukla günde 1–3 g kuru meyve '
            'ya da özüt). 12 yaş altında, gebelikte ve emzirirken önerilmiyor.',
        bilim='Karamukta kanıt var ama DSÖ’nün onayladığı endikasyonda değil ve '
              'DSÖ’nün drogu olan kısımla değil. 2019’da Complementary Therapies '
              'in Medicine dergisinde yayımlanan meta-analiz 5 randomize '
              'çalışmayı (339 kişi) birleştirdi: karamuk takviyesi toplam '
              'kolesterolü 23,6 mg/dL, trigliseriti 29,2 mg/dL ve LDL’yi 13,8 '
              'mg/dL düşürdü; HDL’de anlamlı fark yok. 2020’de aynı dergide '
              'yayımlanan ikinci meta-analiz (7 çalışma, 452 kişi) kan şekeri '
              'tarafında daha temkinli: insülin düzeyi düştü ama **açlık kan '
              'şekeri, HbA1c ve HOMA-IR’de anlamlı değişiklik yok**; '
              'heterojenlik çok yüksek. 2021’de üçüncü bir meta-analiz kan '
              'basıncını inceledi. Üç derleme de daha büyük ve uzun '
              'çalışmalar istiyor; çalışmaların neredeyse hepsi tek ülkeden '
              've küçük. Kanıt düzeyi "sınırlı" — ve not: bu kanıt meyveye '
              'ait, DSÖ monografının kabuğuna değil. Kabuğun kendisi için '
              'monografın dediği geçerli: klinik çalışma yok.',
        kanit='sinirli',
        guv='orta',
        guvNot='**Yüksek tansiyon, diyabet, glokom ve kalp-damar hastalığı '
               'öyküsü olanlar dikkatli kullanmalı** — DSÖ monografının genel '
               'uyarısı; berberinin kan basıncı ve kan şekeri üzerindeki '
               'etkileri ilaçla çakışabilir. **Berberin içeren topikal '
               'hazırlıklar sürüldükten sonra güneşe ve UVA ışığına '
               'çıkılmamalı.** Bitkiye alerjisi olanlar kullanmamalı. 12 yaş '
               'altında, gebelikte ve emzirirken veri yokluğu nedeniyle '
               'önerilmiyor. Meyvenin çalışmalarında ciddi yan etki '
               'bildirilmemiş; kabuk ve kök alkaloit bakımından zengindir ve '
               'meyve gibi gıda sayılmaz.',
        etk=[
            ['Siklosporin',
             'DSÖ monografı böbrek nakli hastalarında berberin hidroklorürün '
             'siklosporin kan düzeyini %75 artırdığını bildiren çalışmayı '
             'aktarıyor; toksisite artmamış ama düzey artışı dar güvenlik '
             'aralığı olan bir ilaç için önemlidir. Nakil hastası bu bitkiyi '
             'kullanmamalı.'],
            ['Kemoterapi ilaçları (paklitaksel)',
             'Monograf berberinin çoklu ilaç direnci taşıyıcısının (P-gp) '
             'ifadesini artırdığını ve kemoterapötiklerin hücrede '
             'tutulmasını azaltabileceğini yazıyor. Kemoterapi gören biri '
             'hekimine sormadan kullanmamalı.'],
            ['Antidiyabetikler ve antihipertansifler (kuramsal)',
             'Monografın "dikkatli kullanım" uyarısının karşılığı: kan '
             'şekerini ve basıncını etkileyen bir bitki, aynı yöndeki ilaçla '
             'üst üste binebilir.'],
        ],
        ilginc='Aynı bitkinin iki hayatı var: DSÖ kabuğunu yazdı, bilim '
               'meyvesini çalıştı. Monograf 2009’da "kabukla klinik çalışma '
               'yok, bildiğimiz şey berberin" derken, sonraki on yılda İran’da '
               'ekşi meyvenin kan yağları üzerine randomize çalışmaları '
               'birikti. Kataloğumuzun kuralı kısmı ayırmaktır: meyvenin '
               'meta-analizi kabuğun kanıtı değil, kabuğun berberini meyvenin '
               'güvenliği değil. Anadolu’da pilavın üstündeki kırmızı tane ile '
               'eczacının sarı kabuğu aynı çalıdan ama aynı şey değil.',
        ek=dict(
            mevsim='Mayısta sarı salkım çiçekler; eylül–ekimde ekşi kırmızı '
                   'meyveler. Kabuk ilkbahar ya da sonbaharda soyulur.',
            yetisme='Avrupa ve Kuzey Asya; Türkiye’de Kuzey ve İç Anadolu’nun '
                    'orman kenarları ve çalılıkları.',
            yoresel='Karamuk, kadıntuzluğu, amberbaris — yaygın Türkçe adlar; '
                    'Farsça zereşk.',
            karisma='Berberis cinsinin Türkiye’de başka türleri de var (B. '
                    'crataegina gibi) ve meyveleri birlikte toplanır; DSÖ '
                    'monografı yalnızca B. vulgaris içindir. Altınmühür '
                    '(Hydrastis) ve Coptis de berberin taşır; "berberin" '
                    'takviyesi genellikle bu bitkiden değil, başka '
                    'kaynaklardan üretilir.',
        ),
        ema=[],
        kaynak=[
            ['A. Hadi ve ark., “Barberry (Berberis vulgaris L.) is a safe '
             'approach for management of lipid parameters: A systematic review '
             'and meta-analysis of randomized controlled trials”, Complementary '
             'Therapies in Medicine 43, 2019',
             'https://pubmed.ncbi.nlm.nih.gov/30935518/'],
            ['Z. Safari ve ark., “The effect of barberry (Berberis vulgaris L.) '
             'on glycemic indices: A systematic review and meta-analysis of '
             'randomized controlled trials”, Complementary Therapies in '
             'Medicine 51, 2020',
             'https://pubmed.ncbi.nlm.nih.gov/32507431/'],
            ['Cortex Berberidis, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 4, 2009', who_url(4, 'cortex-berberidis')],
        ],
        rel=['altinmuhur', 'aciyonca', 'centiyan'],
        en=dict(
            name='Barberry',
            other='Turkish karamuk, kadıntuzluğu, amberbaris; in English '
                  'barberry, European barberry; Persian zereshk. The drug of '
                  'the WHO monograph is the **stem bark** (Cortex Berberidis); '
                  'the part eaten and studied in Turkey and Iran is the '
                  '**fruit**. There is no Turkish or EU monograph; the record '
                  'rests on the WHO monograph (Vol. 4, 2009) and PubMed.',
            part='The dried stem bark (WHO); the fruit (food and clinical '
                 'trials)',
            uses=[
                ['WHO monograph — the bark', 'The World Health Organization '
                 'monograph (Vol. 4, 2009) assesses the stem bark under three '
                 'headings. **Uses supported by clinical data: none.** Uses '
                 'described in pharmacopoeias: digestive complaints such as '
                 'dyspepsia, diarrhoea, gastritis, fullness and flatulence — '
                 'orally. In traditional medicine: cystitis, dysmenorrhoea, '
                 'eczema, fever, haemorrhoids, nasal congestion, rheumatism; '
                 'as cholagogue, diuretic and tonic. The monograph says so '
                 'plainly: no clinical trial of the bark exists; the known '
                 'active principle is **berberine**, and berberine itself has '
                 'been tested in bacterial diarrhoea, trachoma and cutaneous '
                 'leishmaniasis.'],
                ['Turkey', 'There is no monograph for barberry on the Turkish '
                 'list. The plant is a common thorny shrub of Anatolia; its '
                 'sour red fruit is dried and eaten and added to rice (the '
                 'zereshk of Persian cooking is the same fruit). Its yellow '
                 'root and bark dye wool; "kadıntuzluğu" is a widespread folk '
                 'name.'],
                ['Iran — clinical trials of the fruit', 'Nearly all the '
                 'randomised trials of the last twenty years come from Iran '
                 'and were done not with the bark that is the WHO drug but '
                 'with the **fruit** or its extract: blood lipids, blood '
                 'glucose, blood pressure. The monograph’s plant and the '
                 'clinical literature’s plant are the same species, but a '
                 'different part.'],
            ],
            prep='The WHO monograph gives a daily dose for the bark: 0.5–1.0 g '
                 'of drug three times daily, as a decoction; liquid extract '
                 '(1:1, 60% ethanol) 0.3–1.0 ml three times daily; tincture '
                 '(1:10) 2–4 ml three times daily. The doses in the clinical '
                 'trials of the fruit are separate (mostly 1–3 g of dried '
                 'fruit or extract daily). Not recommended under 12, in '
                 'pregnancy or lactation.',
            science='Barberry has evidence, but not in the indication the WHO '
                    'approves nor with the part that is the WHO drug. A '
                    'meta-analysis published in 2019 in Complementary '
                    'Therapies in Medicine pooled 5 randomised trials (339 '
                    'people): barberry supplementation lowered total '
                    'cholesterol by 23.6 mg/dL, triglycerides by 29.2 mg/dL '
                    'and LDL by 13.8 mg/dL; no significant change in HDL. A '
                    'second meta-analysis published in 2020 in the same '
                    'journal (7 trials, 452 people) is more cautious on blood '
                    'glucose: insulin fell, but **no significant change in '
                    'fasting glucose, HbA1c or HOMA-IR**, with very high '
                    'heterogeneity. A third meta-analysis in 2021 examined '
                    'blood pressure. All three call for larger and longer '
                    'trials; nearly all the trials are small and from one '
                    'country. Evidence level Limited — and note: this '
                    'evidence belongs to the fruit, not to the bark of the WHO '
                    'monograph. For the bark itself the monograph’s verdict '
                    'stands: no clinical trial.',
            safety='**Use with caution in high blood pressure, diabetes, '
                   'glaucoma or a history of cardiovascular disease** — the '
                   'WHO monograph’s general precaution; berberine’s '
                   'effects on blood pressure and glucose can collide with '
                   'medication. **Avoid sunlight and UVA after applying '
                   'topical preparations containing berberine.** Not for '
                   'anyone allergic to the plant. Not recommended under 12, '
                   'in pregnancy or lactation for lack of safety data. No '
                   'serious adverse events were reported in the fruit trials; '
                   'the bark and root are rich in alkaloids and do not count '
                   'as food the way the fruit does.',
            fact='One plant with two lives: the WHO wrote up its bark, science '
                 'studied its fruit. While the 2009 monograph said "no '
                 'clinical trial of the bark; what we know is berberine", the '
                 'following decade saw randomised trials of the sour fruit on '
                 'blood lipids accumulate in Iran. This catalog’s rule is to '
                 'keep parts apart: the fruit’s meta-analysis is not the '
                 'bark’s evidence, and the bark’s berberine is not the '
                 'fruit’s safety. The red grain on the rice in Anatolia and '
                 'the pharmacist’s yellow bark come from the same shrub but '
                 'are not the same thing.',
            season='Yellow flower clusters in May; sour red berries in '
                   'September–October. The bark is stripped in spring or '
                   'autumn.',
            habitat='Europe and northern Asia; forest edges and scrub of '
                    'northern and central Anatolia.',
            local='Karamuk, kadıntuzluğu, amberbaris — common Turkish names; '
                  'Persian zereshk.',
            confusion='Other Berberis species grow in Turkey (B. crataegina '
                      'among them) and their fruits are gathered together; '
                      'the WHO monograph is for B. vulgaris only. Goldenseal '
                      '(Hydrastis) and Coptis also carry berberine; '
                      '"berberine" supplements are usually made from other '
                      'sources, not this plant.',
        ),
        etk_en=[
            ['Ciclosporin',
             'The WHO monograph cites a study in kidney-transplant patients in '
             'which berberine hydrochloride raised ciclosporin blood levels by '
             '75%; toxicity did not increase, but a rise in level matters for '
             'a narrow-margin drug. Transplant patients should not use this '
             'plant.'],
            ['Chemotherapy drugs (paclitaxel)',
             'The monograph states that berberine upregulates the multidrug '
             'resistance transporter (P-gp) and may reduce the retention of '
             'chemotherapeutic agents. Anyone on chemotherapy should not use '
             'it without asking their doctor.'],
            ['Antidiabetics and antihypertensives (theoretical)',
             'The counterpart of the monograph’s "use with caution": a plant '
             'affecting blood glucose and pressure can stack on a drug acting '
             'the same way.'],
        ],
    ),

    dict(
        yayin='2026-11-23',
        id='dereotu',
        foto='',
        tr='Dereotu',
        la='Anethum graveolens L.',
        fam='Apiaceae (maydanozgiller)',
        diger='Türkçe dereotu; sinonimleri Pastinaca anethum Spreng., '
              'Peucedanum graveolens Benth. & Hook., Selinum anethum Roth. '
              'İngilizce dill. DSÖ monografının drogu **olgun kuru meyveleri** '
              '(Fructus Anethi); Türk mutfağındaki taze yaprağı monografın '
              'konusu değil. TİTCK ve AB monografı yok; kayıt DSÖ monografına '
              '(Cilt 3, 2007) ve PubMed’e dayanıyor.',
        bolge=['anadolu', 'avrupa', 'asya'],
        kat=['sifa', 'besin'],
        kisim='Olgun kuru meyveleri; uçucu yağı',
        taxon='Anethum graveolens',
        kul=[
            ['DSÖ monografı — meyve', 'Dünya Sağlık Örgütü monografı (Cilt 3, '
             '2007): **klinik veriyle desteklenen kullanım yok.** '
             'Farmakopelerde tanımlanan kullanım: dispepsi, gastrit, gaz ve '
             'mide ağrısı. Geleneksel tıpta: iştah açıcı, idrar söktürücü, süt '
             'artırıcı, ağrı kesici; ishal, astım, nevralji, uykusuzluk, '
             'böbrek taşı — ve, dikkat, **gebeliği önleyici ve doğumu '
             'başlatıcı** olarak. Bu son geleneksel kullanım, monografın '
             'gebelik kontrendikasyonunun gerekçesi.'],
            ['Türkiye', 'TİTCK Tıbbi Bitki Listesi’nde dereotu için monograf '
             'yok. Anadolu mutfağının temel yeşilliklerinden; cacıkta, '
             'zeytinyağlıda, börekte taze yaprağı kullanılır. Halk hekimliğinde '
             'tohumunun bebeklerde gaz sancısına karşı kaynatıldığı yaygın '
             'bilgidir; DSÖ monografı çocuk kullanımı için veri olmadığını '
             'yazıyor.'],
            ['Avrupa — "gripe water"', 'Dereotu yağı İngiltere’de bebek gaz '
             'sancısı için satılan "gripe water"ın 19. yüzyıldan beri klasik '
             'bileşeni; "dill" adının Eski İngilizce "yatıştırmak" '
             'anlamındaki dylle’den geldiği söylenir. Monograf bebek için '
             'veri yok diyor; gelenek ile veri burada da ayrı.'],
        ],
        haz='DSÖ monografı ortalama günlük doz veriyor: meyve 3 g; uçucu yağ '
            '0,1–0,3 g; ya da eşdeğer hazırlıklar. Çay, uçucu yağ ve galenik '
            'hazırlıklar ağızdan. **Gebelikte ve emzirirken önerilmiyor.** '
            'Çocuklar için veri yok.',
        bilim='Dereotunun DSÖ endikasyonunda (sindirim) klinik çalışması yok; '
              'ama metabolik alanda bir meta-analiz var. 2022’de Critical '
              'Reviews in Food Science and Nutrition dergisinde yayımlanan '
              'sistematik derleme 7 randomize çalışmayı (330 kişi) '
              'birleştirdi: dereotu takviyesi LDL kolesterolü 15,6 mg/dL, serum '
              'insülini ve HOMA-IR’yi düşürdü; **toplam kolesterol, '
              'trigliserit, HDL ve açlık kan şekerinde anlamlı etki yok.** '
              'Yazarlar yüksek dozda ve uzun sürede etkinin arttığını, '
              'bulguların doğrulanması gerektiğini yazıyor. 2016 Cochrane '
              'derlemesi (dismenorede besin takviyeleri) ve 2026 tarihli bir '
              'maydanozgil meta-analizi dereotunu adet ağrısında inceliyor — '
              'kanıt düşük kaliteli. Hepsi tohum ya da özütle; mutfaktaki taze '
              'yaprakla değil. Kanıt düzeyi "sınırlı".',
        kanit='sinirli',
        guv='orta',
        guvNot='**Gebelikte ve emzirirken kullanılmamalı** — DSÖ monografı bunu '
               'kesin kontrendikasyon olarak yazıyor: meyve özütleri geleneksel '
               'olarak gebeliği önlemek ve doğumu başlatmak için kullanılmış ve '
               'teratojen olabileceğine dair veri var. Mutfakta yaprağının '
               'yemeğe katılması bu uyarının kapsamında değil; uyarı tohum '
               'özütü ve uçucu yağ dozları içindir. Alerjik rinit öyküsü olan '
               'bir hastada ağızda kaşıntı, dil ve boğazda şişme, ürtiker, '
               'kusma ve ishal bildirilmiş — maydanozgil alerjisi olanlar '
               'dikkat etmeli. Uçucu yağ laboratuvarda insan lenfositlerine '
               'sitotoksik bulunmuş; uçucu yağ ağızdan ancak ölçülü dozda '
               'alınır. Çocuklar için veri yok.',
        etk=[
            ['DSÖ: etkileşim verisi yok',
             'Monograf ilaç etkileşimleri, teratojen etkiler ve çocuk kullanımı '
             'konusunda bilgi bulunmadığını açıkça yazıyor. Kan şekerini ve '
             'LDL’yi etkileyen bir takviye olarak antidiyabetiklerle üst üste '
             'binme olasılığı kuramsal bir nottur.'],
        ],
        ilginc='Türkiye’de dereotu denince yaprak akla gelir; DSÖ monografı '
               'yaprağı hiç anmaz, yalnızca tohumu yazar. Ve o tohum için '
               'monografın en kesin cümlesi şudur: gebelikte kullanılmaz, '
               'çünkü geleneksel tıpta tam tersi amaçla — gebeliği önlemek ve '
               'doğumu başlatmak için — kullanılmıştır. Cacığın üstündeki '
               'yeşillik ile eczacının tohum özütü aynı bitkiden, ama '
               'monografın uyarısı ikisini ayırıyor.',
        ek=dict(
            mevsim='Yazın sarı şemsiye çiçekler; meyveler yaz sonunda '
                   'olgunlaşıp kurutulur. Yaprak ilkbahardan itibaren taze '
                   'toplanır.',
            yetisme='Güney Avrupa ve Batı Asya kökenli; dünyanın her yerinde '
                    'ekiliyor. Türkiye’de her bahçede.',
            yoresel='Dereotu — yaygın Türkçe ad; yöresel adlar kaynaksız '
                    'verilmedi.',
            karisma='⚠️ Rezene ile görünüşü ve kokusu karışır; ikisi ayrı cins '
                    've ayrı monograf. Maydanozgillerin tohumu doğadan '
                    'toplanmamalı; familyada baldıran gibi ölümcül türler var.',
        ),
        ema=[],
        kaynak=[
            ['S. M. Mousavi ve ark., “The effects of Anethum graveolens (dill) '
             'supplementation on lipid profile and glycemic control: a '
             'systematic review and meta-analysis of randomized controlled '
             'trials”, Critical Reviews in Food Science and Nutrition 62(21), '
             '2022',
             'https://pubmed.ncbi.nlm.nih.gov/33624557/'],
            ['P. Pattanittum ve ark., “Dietary supplements for dysmenorrhoea”, '
             'Cochrane Database of Systematic Reviews 2016(3), CD002124',
             'https://pubmed.ncbi.nlm.nih.gov/27000311/'],
            ['Fructus Anethi, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 3, 2007', who_url(3, 'fructus-anethi')],
        ],
        rel=['rezene', 'anason', 'frenkkimyonu'],
        en=dict(
            name='Dill',
            other='Turkish dereotu; synonyms Pastinaca anethum Spreng., '
                  'Peucedanum graveolens Benth. & Hook., Selinum anethum Roth. '
                  'In English dill. The drug of the WHO monograph is the **dried '
                  'ripe fruit** (Fructus Anethi); the fresh leaf of Turkish '
                  'cooking is not the monograph’s subject. No Turkish or EU '
                  'monograph; the record rests on the WHO monograph (Vol. 3, '
                  '2007) and PubMed.',
            part='The dried ripe fruit; the essential oil',
            uses=[
                ['WHO monograph — the fruit', 'The World Health Organization '
                 'monograph (Vol. 3, 2007): **no use supported by clinical '
                 'data.** Uses described in pharmacopoeias: dyspepsia, '
                 'gastritis, flatulence and stomach ache. In traditional '
                 'medicine: appetite stimulant, diuretic, galactagogue, '
                 'analgesic; diarrhoea, asthma, neuralgia, insomnia, kidney '
                 'stones — and, note, as a **contraceptive and to induce '
                 'labour**. That last traditional use is the reason for the '
                 'monograph’s pregnancy contraindication.'],
                ['Turkey', 'There is no monograph for dill on the Turkish list. '
                 'One of the staple greens of Anatolian cooking; its fresh leaf '
                 'goes into cacık, olive-oil dishes and pastries. In folk '
                 'medicine its seed is widely boiled against colic in infants; '
                 'the WHO monograph writes that there are no data for use in '
                 'children.'],
                ['Europe — "gripe water"', 'Dill oil has been a classic '
                 'ingredient of the "gripe water" sold in Britain for infant '
                 'colic since the 19th century; the name "dill" is said to come '
                 'from Old English dylle, "to soothe". The monograph says there '
                 'are no data for infants; tradition and data part ways here '
                 'too.'],
            ],
            prep='The WHO monograph gives an average daily dose: fruit 3 g; '
                 'essential oil 0.1–0.3 g; or equivalent preparations. Tea, '
                 'essential oil and galenical preparations, orally. **Not '
                 'recommended in pregnancy or lactation.** No data for '
                 'children.',
            science='There is no clinical trial of dill in the WHO indication '
                    '(digestion); but there is a meta-analysis in the metabolic '
                    'field. A systematic review published in 2022 in Critical '
                    'Reviews in Food Science and Nutrition pooled 7 randomised '
                    'trials (330 people): dill supplementation lowered LDL '
                    'cholesterol by 15.6 mg/dL, serum insulin and HOMA-IR; **no '
                    'significant effect on total cholesterol, triglycerides, HDL '
                    'or fasting glucose.** The authors write that the effect '
                    'grew with higher doses and longer use and that the '
                    'findings need confirming. A 2016 Cochrane review (dietary '
                    'supplements for dysmenorrhoea) and a 2026 Apiaceae '
                    'meta-analysis examine dill in period pain — low-quality '
                    'evidence. All with seed or extract, not the fresh leaf of '
                    'the kitchen. Evidence level Limited.',
            safety='**Not to be used in pregnancy or lactation** — the WHO '
                   'monograph writes this as a firm contraindication: fruit '
                   'extracts have traditionally been used to prevent pregnancy '
                   'and induce labour, and there are data suggesting '
                   'teratogenic effects. Adding the leaf to food in the kitchen '
                   'is not within this warning; the warning concerns seed '
                   'extract and essential-oil doses. In a patient with a history '
                   'of allergic rhinitis, oral itching, swelling of tongue and '
                   'throat, urticaria, vomiting and diarrhoea were reported — '
                   'anyone allergic to the carrot family should take care. The '
                   'essential oil was cytotoxic to human lymphocytes in the '
                   'laboratory; the oil is taken orally only in measured doses. '
                   'No data for children.',
            fact='In Turkey "dereotu" means the leaf; the WHO monograph never '
                 'mentions the leaf and writes only of the seed. And for that '
                 'seed the monograph’s firmest sentence is this: not in '
                 'pregnancy, because in traditional medicine it was used for '
                 'the opposite purpose — to prevent pregnancy and to start '
                 'labour. The green on top of the cacık and the pharmacist’s '
                 'seed extract come from one plant, but the monograph’s '
                 'warning separates them.',
            season='Yellow umbels in summer; the fruit ripens in late summer '
                   'and is dried. The leaf is picked fresh from spring on.',
            habitat='Native to southern Europe and western Asia; grown '
                    'everywhere. In every garden in Turkey.',
            local='Dereotu — the common Turkish name; no unsourced regional '
                  'names given.',
            confusion='⚠️ It is confused with fennel in look and scent; separate '
                      'genus, separate monograph. Umbellifer seeds should not '
                      'be gathered from the wild; the family contains lethal '
                      'species such as hemlock.',
        ),
        etk_en=[
            ['WHO: no interaction data',
             'The monograph states plainly that no information is available '
             'on drug interactions, teratogenic effects or paediatric use. As '
             'a supplement affecting blood glucose and LDL, the possibility of '
             'stacking on antidiabetics is a theoretical note.'],
        ],
    ),


]
