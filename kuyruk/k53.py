# Boşluk kapatma partisi (16–18 Ocak 2027): tıbbi adaçayı (AB), huang lian ve
# ya dan zi (DSÖ Cilt 1).
from kunye_elle import who_url
E = 'https://www.ema.europa.eu/en/medicines/herbal/'
Q = [

    dict(
        yayin='2027-01-21',
        id='tibbiadacayi',
        foto='',
        tr='Tıbbi adaçayı',
        la='Salvia officinalis L.',
        fam='Lamiaceae (ballıbabagiller)',
        diger='AB monografı Salviae officinalis folium (yaprak); TİTCK listesinde '
              'de var. İngilizce sage, common sage; Latince salvare, "kurtarmak". '
              'Kataloğumuzdaki **adaçayı** kaydı Anadolu adaçayıdır (S. '
              'fruticosa, elma çayı); bu kayıt Avrupa’nın ilaç adaçayına ait — '
              'Türkiye’de daha az yetişir, aktarda "tıbbi adaçayı" ya da '
              '"Dalmaçya adaçayı" diye ayrılır. Tujon içerir; monograf bunu '
              'ayrıca düzenliyor.',
        bolge=['avrupa', 'anadolu'],
        kat=['sifa', 'besin'],
        kisim='Yaprakları; uçucu yağı (ayrı AB kamu açıklaması)',
        taxon='Salvia officinalis',
        kul=[
            ['Avrupa — dört endikasyon', 'AB monografı yaprağı dört geleneksel '
             'endikasyonda tanıyor: (1) hafif hazımsızlık şikâyetleri (mide '
             'yanması, şişkinlik); (2) **aşırı terleme**; (3) ağız ve boğaz '
             'iltihabı (gargara); (4) hafif deri iltihabı (dış). Dozlar: çay '
             '1–2 g yaprak 150 ml kaynar suda günde üç kez; terleme için 2 g; '
             'gargara için 2,5 g/100 ml; gece terlemesi için sıvı ekstre '
             'yatmadan bir saat önce. Süreler: hazımsızlıkta iki hafta, '
             'terlemede altı hafta (uzun kullanım mümkün), boğazda bir hafta. '
             '18 yaş altında önerilmiyor; gebelik ve emzirmede önerilmiyor; '
             'etkileşim ve yan etki "bildirilmedi". Aşırı doz: 15 g yaprağa '
             'eşdeğer uçucu yağ sıcaklık hissi, taşikardi, baş dönmesi ve '
             '**epileptiform nöbet** yapar.'],
            ['Akdeniz — "bahçesinde adaçayı olan neden ölsün?"', 'Salerno tıp '
             'okulunun ortaçağ özdeyişi: "Cur moriatur homo cui salvia crescit '
             'in horto?" Romalılar "kutsal ot" diye hasat etti; Karolenj '
             'manastır bahçelerinin zorunlu bitkisi; Rönesans’ta hafıza ve '
             'uzun ömür otu. Dalmaçya kıyıları (Hırvatistan) en kaliteli '
             'yaprağın kaynağı. Anadolu’da ise "adaçayı" deyince S. fruticosa '
             'anlaşılır; tıbbi adaçayı bahçe bitkisi ve mutfak otudur '
             '(saltimbocca, tereyağında adaçayı).'],
            ['Bellek — klinik çalışmalar', '2014 CNS Neuroscience & '
             'Therapeutics sistematik derlemesi S. officinalis ve S. '
             'lavandulaefolia’nın bilişsel işlev üzerine sekiz klinik '
             'çalışmasını topladı: sağlıklı gönüllülerde tek dozla dikkat ve '
             'bellek skorlarında iyileşme, Alzheimer’da iki küçük çalışmada '
             'yarar; yazarlar "umut verici ama yöntemsel sorunlarla gölgeli" '
             'diyor. AB monografı bu endikasyonu tanımıyor; kolinesteraz '
             'inhibisyonu mekanizması laboratuvarda gösterilmiş.'],
        ],
        haz='AB: çay 1–2 g kuru yaprak 150 ml kaynar suda, günde üç kez '
            '(hazımsızlık); 2 g (terleme); gargara 2,5 g/100 ml, ılık, günde üç '
            'kez. Tujon nedeniyle sürekli yüksek doz çay içilmez; uçucu yağ '
            'ağızdan alınmaz. 18 yaş altında, gebelikte ve emzirirken '
            'önerilmiyor. Mutfak dozu (birkaç yaprak) ayrı.',
        bilim='Tıbbi adaçayının AB monografı dört endikasyonu da "geleneksel '
              'kullanım" statüsünde tanıyor — otuz yıllık kullanım, klinik '
              'kanıt aranmıyor; terleme endikasyonu için küçük Alman '
              'çalışmaları (menopoz sıcak basması) var ama monograf bunları '
              '"iyi bilinen" saymıyor. Biliş için 2014 derlemesi sekiz '
              'çalışmada olumlu ama tutarsız preparatlarla elde edilmiş '
              'sonuçlar bildiriyor. Güvenlik tarafında tujon düzenlemesi '
              '(EMA 2010 kamu açıklaması) var: düşük tujonlu kemotipler '
              'tercih edilmeli. Kanıt düzeyi "geleneksel" — AB '
              'sınıflamasıyla.',
        kanit='geleneksel',
        guv='orta',
        guvNot='**Tujon** — yaprak çayı ölçülü ve süreli içilir; uçucu yağ '
               'ağızdan alınmaz: 15 g yaprağa eşdeğer yağ nöbet yapar (AB). '
               'Epilepsisi olanlar kaçınmalı. **Gebelikte ve emzirirken '
               'önerilmiyor**; geleneksel olarak süt kesici sayılır (sütten '
               'kesme döneminde kullanılır — aynı nedenle emzirenler '
               'kullanmaz). 18 yaş altında önerilmiyor. Ballıbabagil alerjisi. '
               'Etkileşim ve yan etki AB’de "bildirilmedi". Mutfak dozunda '
               'güvenli. Güvenlik düzeyi "orta".',
        etk=[
            ['Bilinen etkileşim yok (AB)',
             'Monograf "bildirilmedi" diyor. Tujon nedeniyle nöbet eşiğini '
             'düşüren ilaçlarla kuramsal risk; kan şekeri düşürücü küçük '
             'çalışmalar nedeniyle diyabet ilacıyla izlem.'],
            ['Sedatifler (kuramsal)',
             'Laboratuvarda GABA etkisi; birlikte uyku hali artabilir.'],
        ],
        ilginc='"Bahçesinde adaçayı olan neden ölsün?" — ortaçağın sorusu. '
               'AB’nin cevabı dört mütevazı endikasyon ve bir uyarı: on beş '
               'gram yaprağa eşdeğer yağ nöbet yapar. Türkiye’de "adaçayı" '
               'deyince başka tür (S. fruticosa) anlaşılır; ikisi aynı '
               'kavanozda satılır, biri tujonlu biri değil. Kataloğumuz bu '
               'yüzden iki ayrı kayıt tutuyor.',
        ek=dict(
            mevsim='Mayıs–Haziran’da mor-mavi çiçekler; yaprak çiçeklenmeden '
                   'önce toplanır, gölgede kurutulur.',
            yetisme='Akdeniz kökenli (Dalmaçya, İtalya, İspanya); kuru, kireçli '
                    'yamaçlar. Türkiye’de bahçe bitkisi; Ege’de yetişir.',
            yoresel='Tıbbi adaçayı, Dalmaçya adaçayı, bahçe adaçayı; yöresel ad '
                    'yok (Anadolu "adaçayı" S. fruticosa’dır).',
            karisma='⚠️ Anadolu adaçayı (S. fruticosa, elma çayı) ayrı tür ve '
                    'ayrı kayıt — daha az tujon. İspanyol adaçayı (S. '
                    'lavandulaefolia) tujonsuz, biliş çalışmalarında kullanıldı. '
                    'Beyaz adaçayı (S. apiana) ritüel bitkisi, ayrı kayıt. '
                    'Danshen (S. miltiorrhiza) Çin tıbbı, ilgisiz kullanım.',
        ),
        ema=[('Salviae officinalis folium', E + 'salviae-officinalis-folium')],
        kaynak=[
            ['M. Miroddi ve ark., “Systematic review of clinical trials '
             'assessing pharmacological properties of Salvia species on memory, '
             'cognitive impairment and Alzheimer’s disease”, CNS Neuroscience & '
             'Therapeutics 20(6), 2014',
             'https://pubmed.ncbi.nlm.nih.gov/24836739/'],
        ],
        rel=['adacayi', 'akadacayi', 'biberiye', 'kekik'],
        en=dict(
            name='Common sage',
            other='The EU monograph Salviae officinalis folium (leaf); also on '
                  'the Turkish list. English sage, common sage; Latin salvare, '
                  '"to save". The **adaçayı** record in this catalog is the '
                  'Anatolian sage (S. fruticosa, Greek sage); this record '
                  'belongs to Europe’s medicinal sage — less grown in Turkey, '
                  'and set apart at the herbalist as "tıbbi adaçayı" or '
                  '"Dalmatian sage". It contains thujone; the monograph '
                  'regulates that separately.',
            part='The leaves; the essential oil (a separate EU public '
                 'statement)',
            uses=[
                ['Europe — four indications', 'The EU monograph recognises the '
                 'leaf in four traditional indications: (1) mild dyspeptic '
                 'complaints (heartburn, bloating); (2) **excessive sweating**; '
                 '(3) inflammation of the mouth and throat (gargle); (4) minor '
                 'skin inflammation (external). Doses: tea 1–2 g of leaf in 150 '
                 'ml of boiling water three times a day; 2 g for sweating; '
                 'gargle 2.5 g/100 ml; liquid extract an hour before bed for '
                 'night sweats. Durations: two weeks for dyspepsia, six weeks '
                 'for sweating (long-term use possible), one week for the '
                 'throat. Not recommended under 18; not recommended in '
                 'pregnancy or lactation; interactions and adverse effects '
                 '"none reported". Overdose: essential oil equivalent to 15 g '
                 'of leaf causes sensation of heat, tachycardia, vertigo and '
                 '**epileptiform convulsions**.'],
                ['The Mediterranean — "why should a man die who has sage in '
                 'his garden?"', 'The medieval maxim of the Salerno school: '
                 '"Cur moriatur homo cui salvia crescit in horto?" The Romans '
                 'harvested it as a "holy herb"; the obligatory plant of '
                 'Carolingian monastery gardens; the herb of memory and long '
                 'life in the Renaissance. The Dalmatian coast (Croatia) is the '
                 'source of the finest leaf. In Anatolia "adaçayı" means S. '
                 'fruticosa; common sage is a garden plant and kitchen herb '
                 '(saltimbocca, sage in butter).'],
                ['Memory — clinical trials', 'The 2014 CNS Neuroscience & '
                 'Therapeutics systematic review pooled eight clinical trials '
                 'of S. officinalis and S. lavandulaefolia on cognitive '
                 'function: improvement in attention and memory scores with a '
                 'single dose in healthy volunteers, benefit in two small '
                 'Alzheimer’s trials; the authors call it "promising but '
                 'debased by methodological issues". The EU monograph does not '
                 'recognise this indication; the cholinesterase-inhibition '
                 'mechanism has been shown in the laboratory.'],
            ],
            prep='EU: tea 1–2 g of dried leaf in 150 ml of boiling water, three '
                 'times a day (dyspepsia); 2 g (sweating); gargle 2.5 g/100 ml, '
                 'warm, three times a day. Because of thujone, high-dose tea is '
                 'not drunk continuously; the essential oil is not taken by '
                 'mouth. Not recommended under 18, in pregnancy or lactation. '
                 'Kitchen doses (a few leaves) are another matter.',
            science='The EU monograph recognises all four indications of '
                    'common sage as "traditional use" — thirty years of use, no '
                    'clinical evidence required; small German trials '
                    '(menopausal hot flushes) exist for the sweating '
                    'indication, but the monograph does not count them as '
                    '"well-established". For cognition the 2014 review reports '
                    'positive but inconsistent results across eight trials with '
                    'differing preparations. On the safety side there is the '
                    'thujone regulation (EMA 2010 public statement): '
                    'low-thujone chemotypes should be preferred. Evidence level '
                    'Traditional — by the EU classification.',
            safety='**Thujone** — leaf tea is drunk in moderation and for '
                   'limited periods; the essential oil is not taken by mouth: '
                   'oil equivalent to 15 g of leaf causes seizures (EU). Anyone '
                   'with epilepsy should avoid it. **Not recommended in '
                   'pregnancy or lactation**; traditionally counted a '
                   'lactation suppressant (used at weaning — for the same reason '
                   'not used while breastfeeding). Not recommended under 18. '
                   'Mint-family allergy. Interactions and adverse effects "none '
                   'reported" in the EU. Safe at kitchen doses. Safety level '
                   'Medium.',
            fact='"Why should a man die who has sage in his garden?" — the '
                 'Middle Ages’ question. The EU’s answer is four modest '
                 'indications and a warning: oil equivalent to fifteen grams of '
                 'leaf causes seizures. In Turkey "adaçayı" means another '
                 'species (S. fruticosa); the two are sold in the same jar, one '
                 'with thujone and one without. That is why this catalog keeps '
                 'two separate records.',
            season='Purple-blue flowers in May–June; the leaf is picked before '
                   'flowering and dried in the shade.',
            habitat='Native to the Mediterranean (Dalmatia, Italy, Spain); dry, '
                    'chalky slopes. A garden plant in Turkey; grows in the '
                    'Aegean.',
            local='Tıbbi adaçayı, Dalmaçya adaçayı, bahçe adaçayı; no regional '
                  'names (the Anatolian "adaçayı" is S. fruticosa).',
            confusion='⚠️ Anatolian sage (S. fruticosa, Greek sage) is a '
                      'separate species and record — less thujone. Spanish sage '
                      '(S. lavandulaefolia) is thujone-free and was used in the '
                      'cognition trials. White sage (S. apiana) is a ritual '
                      'plant, a separate record. Danshen (S. miltiorrhiza) is '
                      'Chinese medicine, an unrelated use.',
        ),
        etk_en=[
            ['No known interaction (EU)',
             'The monograph says "none reported". A theoretical risk with '
             'drugs that lower the seizure threshold because of thujone; '
             'monitoring with diabetes drugs because of small '
             'blood-sugar-lowering studies.'],
            ['Sedatives (theoretical)',
             'A GABA effect in the laboratory; drowsiness may increase '
             'together.'],
        ],
    ),

    dict(
        yayin='2027-01-22',
        id='huanglian',
        foto='',
        tr='Huang lian (Çin altın ipliği)',
        la='Coptis chinensis Franch.',
        fam='Ranunculaceae (düğünçiçeğigiller)',
        diger='DSÖ monografı Rhizoma Coptidis (Cilt 1) Coptis chinensis, C. '
              'deltoidea ve C. japonica’yı kapsıyor. Çince huang lian ("sarı '
              'bağlantı"), Japonca ōren; İngilizce Chinese goldthread. '
              'Kullanılan kısım **kurutulmuş rizom**. TİTCK ve AB monografı '
              'yok. Berberin içeriği yüzde 4–9 ile berberinli bitkilerin en '
              'zengini; Amur mantar ağacı ve altın mühürle aynı alkaloit. '
              'Türkiye’de bilinmez; berberin takviyelerinin bir kaynağı.',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Kurutulmuş rizomu',
        taxon='Coptis chinensis',
        kul=[
            ['DSÖ — bakteriyel ishal', 'DSÖ monografı "klinik verilerle '
             'desteklenen kullanım: yok" diyor; farmakope kullanımı (Çin ve '
             'Japon farmakopeleri): **bakteriyel ishalin yönetimi**; ayrıca '
             'akut konjonktivit, gastroenterit, çıban, deri ve iç organ '
             'leishmaniasis’i ("şark çıbanı"). Halk kullanımı (kanıtsız): '
             'artrit, yanık, diyabet, adet ağrısı, diş ağrısı, sıtma, gut, '
             'böbrek. Doz: günde en çok 1,5–6 g kuru rizom. **Gebelikte '
             'kontrendike** (berberin güvenliği kurulmamış); emzirmede '
             'önerilmiyor; çocuklarda güvenlik kurulmamış. Berberin 500 mg '
             'dozda iyi tolere edilir.'],
            ['Çin — "üç sarı"nın en acısı', 'Huang lian Çin tıbbının en acı '
             'drogu — "huang lian kadar acı" deyimi dile yerleşmiş. Shennong '
             'Bencao Jing’den (MS 1–2. yy) beri "kalbin ateşini" ve "nem-ısı"yı '
             'temizleyen, ishal, dizanteri, ağız yarası ve uykusuzluk için '
             'kullanılan rizom; Sichuan’ın dağ tarımı (Shizhu county coğrafi '
             'işaretli). Japon Kampo’sunda ōren-gedoku-tō formülünün '
             'bileşeni. Yabani popülasyon tükenmiş, tamamı kültür.'],
            ['Berberin — ortak molekül', 'Kataloğumuzdaki Amur mantar ağacı '
             'kaydıyla aynı molekül dosyası: berberin için tip 2 diyabette '
             'meta-analiz düzeyinde kan şekeri verisi var (2022, 37 çalışma); '
             'ishalde 1980’lerin çalışmaları. DSÖ monografı (1999) bu '
             'ayrımı daha o zaman yapıyor: etki berberine, bitkiye değil. 2019 '
             'Pharmaceutical Biology derlemesi Coptis’in 100’den fazla '
             'bileşenini ve toksikolojisini topluyor.'],
        ],
        haz='DSÖ: günde en çok 1,5–6 g kuru rizom, dekoksiyon (çoğunlukla Çin '
            'reçetelerinde karışım). Çok acıdır. Gebelikte kullanılmaz; '
            'emzirme ve çocukta önerilmiyor. Berberin takviyesi ayrı ürün '
            '(Amur mantar ağacı kaydına bakın). Türkiye’de ürün yok.',
        bilim='Huang lian, berberinli üçlünün (altın mühür, Amur mantar ağacı, '
              'bu rizom) en yüksek berberinli üyesi ve DSÖ’nün ilk cildinde '
              '(1999) yer alan kayıt. Monograf rizom için klinik veri '
              'bulamıyor, antibakteriyel laboratuvar verisini "çok sayıda" '
              'diye niteliyor, mutajenite verisini "çelişkili" diye not '
              'ediyor. Sonraki yirmi yılın berberin meta-analizleri (kan '
              'şekeri, lipitler) moleküle ait; Coptis dekoksiyonuyla yapılan '
              'Çin çalışmaları karışım ve kontrolsüz. Kanıt düzeyi '
              '"geleneksel".',
        kanit='geleneksel',
        guv='orta',
        guvNot='**Gebelikte kontrendike** — DSÖ; berberin yenidoğanda '
               'kernikterus riski (Amur mantar ağacı kaydıyla aynı gerekçe). '
               'Emzirmede ve çocukta kullanılmaz. Mutajenite verisi çelişkili '
               '(DSÖ). Yan etki olgusu: bulantı, kusma, karın ağrısı, ishal, '
               'çok idrar. **CYP3A4/P-gp inhibisyonu** — siklosporin ve '
               'kemoterapi ilaçlarıyla etkileşim (Amur mantar ağacı kaydı). '
               'G6PD eksikliğinde berberin hemoliz yapabilir. Güvenlik düzeyi '
               '"orta".',
        etk=[
            ['Siklosporin ve CYP3A4 substratları',
             'Berberin siklosporin düzeyini yükseltir (randomize çalışma); '
             'nakil hastaları kullanmamalı.'],
            ['Antidiyabetikler',
             'Berberin kan şekerini düşürür; insülin ve sülfonilüre ile '
             'izlem.'],
            ['Tetrasiklinler (kuramsal)',
             'Berberinin tetrasiklin emilimini azalttığına dair eski veri; '
             'aralık bırakılmalı.'],
        ],
        ilginc='Çincede acılığın ölçüsü bu rizom: "huang lian yiyen dilsiz, '
               'acısını anlatamaz" atasözü. Berberinli bitkilerin en '
               'yoğunu, DSÖ’nün ilk cildinde, kataloğumuza 313. sırada — '
               've bugün Batı’da "berberin" kapsülü diye satılan molekülün '
               'bir kaynağı. Kapsülün etiketinde hangi bitkiden geldiği '
               'çoğu zaman yazmaz; üç bitki, bir molekül, tek uyarı: '
               'gebelikte yasak.',
        ek=dict(
            mevsim='Rizom 5–6 yaşında sonbaharda sökülür, kurutulur.',
            yetisme='Orta ve batı Çin’in dağ ormanları (Sichuan, Hubei, '
                    'Yunnan), 500–2000 m gölgeli yamaçlar; tamamen kültür. '
                    'Türkiye’de yetişmez.',
            yoresel='Huang lian (Çince), ōren (Japonca), Çin altın ipliği. '
                    'Yöresel ad yok.',
            karisma='⚠️ Hu huang lian (kutki, Picrorhiza) adı benzer, ayrı '
                    'bitki ve kayıt. Altın mühür (Hydrastis, "goldenseal") '
                    'Kuzey Amerika akrabası, ayrı kayıt. Huang bai '
                    '(Phellodendron) ve huang qin (Scutellaria) "üç sarı"nın '
                    'ötekileri.',
        ),
        ema=[],
        kaynak=[
            ['Rhizoma Coptidis, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 1, 1999',
             who_url(1, 'rhizoma-coptidis')],
            ['J. Wang ve ark., “Coptidis Rhizoma: a comprehensive review of its '
             'traditional uses, botany, phytochemistry, pharmacology and '
             'toxicology”, Pharmaceutical Biology 57(1), 2019',
             'https://pubmed.ncbi.nlm.nih.gov/30963783/'],
        ],
        rel=['amurmantaragaci', 'altinmuhur', 'kutki'],
        en=dict(
            name='Huang lian (Chinese goldthread)',
            other='The WHO monograph Rhizoma Coptidis (Volume 1) covers Coptis '
                  'chinensis, C. deltoidea and C. japonica. Chinese huang lian '
                  '("yellow link"), Japanese ōren. The part is **the dried '
                  'rhizome**. No Turkish or EU monograph. With 4–9% berberine the '
                  'richest of the berberine plants; the same alkaloid as the '
                  'Amur cork tree and goldenseal. Unknown in Turkey; one source '
                  'of berberine supplements.',
            part='The dried rhizome',
            uses=[
                ['WHO — bacterial diarrhoea', 'The WHO monograph says "uses '
                 'supported by clinical data: none"; the pharmacopoeial use '
                 '(Chinese and Japanese pharmacopoeias): **management of '
                 'bacterial diarrhoeas**; also acute conjunctivitis, '
                 'gastroenteritis, boils, cutaneous and visceral leishmaniasis '
                 '("oriental sore"). Folk uses (without evidence): arthritis, '
                 'burns, diabetes, dysmenorrhoea, toothache, malaria, gout, '
                 'kidney disease. Dose: at most 1.5–6 g of dried rhizome a day. '
                 '**Contraindicated in pregnancy** (berberine safety not '
                 'established); not recommended in lactation; safety in '
                 'children not established. Berberine is well tolerated at 500 '
                 'mg.'],
                ['China — the bitterest of the "three yellows"', 'Huang lian '
                 'is the bitterest drug of Chinese medicine — "as bitter as '
                 'huang lian" is a fixed phrase. Since the Shennong Bencao Jing '
                 '(1st–2nd century CE) the rhizome that "clears heart fire" and '
                 '"damp-heat", for diarrhoea, dysentery, mouth sores and '
                 'insomnia; the mountain crop of Sichuan (Shizhu county, '
                 'geographically marked). An ingredient of the ōren-gedoku-tō '
                 'formula in Japanese Kampo. The wild population is exhausted; '
                 'all is cultivated.'],
                ['Berberine — the shared molecule', 'The same molecule file as '
                 'the Amur cork tree record in this catalog: meta-analysis-level '
                 'blood-sugar data for berberine in type 2 diabetes (2022, 37 '
                 'trials); 1980s trials in diarrhoea. The WHO monograph (1999) '
                 'drew that line even then: the effect belongs to berberine, '
                 'not the plant. The 2019 Pharmaceutical Biology review '
                 'collects more than 100 constituents of Coptis and its '
                 'toxicology.'],
            ],
            prep='WHO: at most 1.5–6 g of dried rhizome a day as decoction '
                 '(mostly within mixtures in Chinese prescriptions). Very '
                 'bitter. Not used in pregnancy; not recommended in lactation '
                 'or children. Berberine supplements are a separate product '
                 '(see the Amur cork tree record). No product in Turkey.',
            science='Huang lian is the richest-in-berberine member of the '
                    'berberine trio (goldenseal, Amur cork tree, this rhizome) '
                    'and the record in the WHO’s first volume (1999). The '
                    'monograph finds no clinical data for the rhizome, calls '
                    'the antibacterial laboratory data "numerous", and notes '
                    'the mutagenicity data as "conflicting". The berberine '
                    'meta-analyses of the following twenty years (blood sugar, '
                    'lipids) belong to the molecule; Chinese trials with Coptis '
                    'decoction are mixtures and uncontrolled. Evidence level '
                    'Traditional.',
            safety='**Contraindicated in pregnancy** — WHO; berberine carries a '
                   'kernicterus risk in the newborn (the same reasoning as the '
                   'Amur cork tree record). Not used in lactation or children. '
                   'Mutagenicity data conflicting (WHO). An adverse-event case: '
                   'nausea, vomiting, abdominal pain, diarrhoea, polyuria. '
                   '**CYP3A4/P-gp inhibition** — interaction with ciclosporin '
                   'and chemotherapy drugs (Amur cork tree record). Berberine '
                   'can cause haemolysis in G6PD deficiency. Safety level '
                   'Medium.',
            fact='In Chinese this rhizome is the measure of bitterness: the '
                 'proverb "a mute who eats huang lian cannot tell his '
                 'bitterness". The densest of the berberine plants, in the '
                 'WHO’s first volume, 313th in this catalog — and one source of '
                 'the molecule sold in the West as a "berberine" capsule. The '
                 'capsule label mostly does not say which plant it came from; '
                 'three plants, one molecule, one warning: forbidden in '
                 'pregnancy.',
            season='The rhizome is lifted in autumn at 5–6 years and dried.',
            habitat='The mountain forests of central and western China '
                    '(Sichuan, Hubei, Yunnan), shady slopes at 500–2,000 m; '
                    'wholly cultivated. Does not grow in Turkey.',
            local='Huang lian (Chinese), ōren (Japanese), Chinese goldthread. '
                  'No regional names.',
            confusion='⚠️ Hu huang lian (kutki, Picrorhiza) is similar in name, '
                      'a separate plant and record. Goldenseal (Hydrastis) is '
                      'the North American relative, a separate record. Huang '
                      'bai (Phellodendron) and huang qin (Scutellaria) are the '
                      'other "three yellows".',
        ),
        etk_en=[
            ['Ciclosporin and CYP3A4 substrates',
             'Berberine raises ciclosporin levels (randomised trial); '
             'transplant patients should not use it.'],
            ['Antidiabetics',
             'Berberine lowers blood sugar; monitoring with insulin and '
             'sulphonylureas.'],
            ['Tetracyclines (theoretical)',
             'Old data that berberine reduces tetracycline absorption; '
             'spacing needed.'],
        ],
    ),

    dict(
        yayin='2027-01-23',
        id='yadanzi',
        foto='',
        tr='Ya dan zi (Cava bruseası)',
        la='Brucea javanica (L.) Merr.',
        fam='Simaroubaceae',
        diger='DSÖ monografı Fructus Bruceae (Cilt 1); Çince ya dan zi ("ördek '
              'safrası tohumu"), Endonezce biji makassar, İngilizce Java '
              'brucea. Kullanılan kısım **kurutulmuş olgun meyve**. TİTCK ve AB '
              'monografı yok. Türkiye’de bilinmez; kataloğumuzda DSÖ listesini '
              'tamamlayan Güneydoğu Asya kaydı. ⚠️ Çok acı ve toksik '
              'kassinoitler içerir; çocuk ve gebeye verilmez.',
        bolge=['asya', 'okyanusya'],
        kat=['sifa', 'zehir'],
        kisim='Kurutulmuş olgun meyvesi; tohum yağı (Çin onkolojisinde '
              'emülsiyon)',
        taxon='Brucea javanica',
        kul=[
            ['DSÖ — amipli dizanteri ve sıtma', 'DSÖ monografı "klinik '
             'verilerle desteklenen kullanım: yok" diyor; farmakope kullanımı '
             '(Çin, Vietnam): **amipli dizanteri ve sıtma**. Halk kullanımı '
             '(kanıtsız): çıban lapası, mantar, kıl kurdu, solucan, şerit, '
             'basur, dalak büyümesi; tohum yağı siğil ve nasıra. Doz: '
             'amipli dizanteride günde 4–16 g, 3–7 gün; sıtmada 3–6 g, 4–5 '
             'gün, yemekten sonra. **Kontrendike: çocuklar ve gebeler**; '
             'emzirmede verilmez. Yan etki: dış uygulamada anafilaksi '
             'olguları.'],
            ['Güneydoğu Asya ve Çin — acı tohum', 'Çalı Güney Çin’den '
             'Endonezya ve Kuzey Avustralya’ya yerli; Çin tıbbında ya dan zi '
             '"ısıyı temizleyen, zehri gideren" acı meyve, 16. yüzyıl Bencao '
             'Gangmu’da. Endonezya ve Malezya’da (makassar tohumu) dizanteri '
             've sıtma için. Meyve o kadar acıdır ki longan meyvesi kabuğuna '
             'sarılarak yutulur — Çin reçetelerinin klasik yöntemi.'],
            ['Modern Çin onkolojisi — yağ emülsiyonu', 'Tohum yağından yapılan '
             'damar içi emülsiyon (BJOE) Çin’de 1980’lerden beri kanser '
             'kemoterapisine ek olarak ruhsatlı. 2021 Frontiers in Nutrition '
             'meta-analizi mide kanserinde 18 randomize çalışmayı (1210 hasta) '
             'topladı: kemoterapiye eklendiğinde yanıt oranı ve performans '
             'skoru yükseldi, kemoterapinin yan etkileri (nötropeni, bulantı) '
             'azaldı — ama çalışmaların tamamı Çin kaynaklı, çoğu kör değil, '
             'kalite düşük. Bu veri meyveye değil, standardize yağ emülsiyonuna '
             'ait.'],
        ],
        haz='Bu kayıt doz önermiyor; DSÖ dozları Çin farmakope geleneğinin '
            'kaydıdır ve hekim gözetimi ister. Meyve çiğnenmez (aşırı acı ve '
            'tahriş edici); Çin geleneğinde kapsül ya da longan kabuğunda '
            'yutulur. Çocuk ve gebeye verilmez. Deriye uygulamada anafilaksi '
            'bildirilmiştir. Türkiye’de ürün yok.',
        bilim='Ya dan zi, DSÖ’nün ilk cildinde "klinik veri yok" ile yer alan '
              've farmakolojisi kassinoitlere (bruceantin, brusatol) dayanan '
              'bitki: laboratuvarda amip öldürücü ve antitümör etki güçlü, '
              'insanda dizanteri ve sıtma için kontrollü çalışma yok. '
              'Bruceantin 1970–80’lerde ABD Ulusal Kanser Enstitüsü’nde faz II '
              'denemelere girdi, etkisizlik ve toksisite nedeniyle bırakıldı. '
              'Çin’in yağ emülsiyonu meta-analizleri olumlu ama metodolojik '
              'olarak zayıf. Kanıt düzeyi "geleneksel"; güvenlik "düşük" — '
              'DSÖ’nün çocuk ve gebe yasağı, anafilaksi ve kassinoit '
              'toksisitesi.',
        kanit='geleneksel',
        guv='dusuk',
        guvNot='**Çocuklara ve gebelere verilmez** — DSÖ kontrendikasyonu; '
               'emzirmede verilmez. Kassinoitler sitotoksiktir: aşırı dozda '
               'bulantı, kusma, karın ağrısı, karaciğer ve böbrek hasarı '
               'bildirilmiştir (Çin literatürü). **Dış uygulamada anafilaksi** '
               '(DSÖ). Mide-bağırsak tahrişi; mide ülserinde kullanılmaz. '
               'Kısa süreli kullanım (DSÖ: 3–7 gün). Güvenlik düzeyi "düşük".',
        etk=[
            ['Bilinen etkileşim verisi yok (DSÖ)',
             'Monograf "bilgi yok" diyor. Yağ emülsiyonu kemoterapiyle '
             'birlikte çalışılmış; ağızdan meyvenin ilaçlarla etkileşimi '
             'bilinmiyor. Hepatotoksik ilaçlarla kuramsal risk.'],
        ],
        ilginc='Adı "ördek safrası tohumu" — safra kadar acı. Çinli hasta onu '
               'longan kabuğuna sarıp yutar; Amerikan Kanser Enstitüsü aynı '
               'tohumun molekülünü 1970’lerde kanser ilacı diye denedi, '
               'vazgeçti; Çin aynı tohumun yağını kemoterapiye ekliyor ve '
               'on sekiz çalışmada "işe yarıyor" diyor. DSÖ ise 1999’da '
               '"klinik veri yok" yazdı. Kataloğumuzun en acı ve en az bilinen '
               'kaydı.',
        ek=dict(
            mevsim='Meyve Ağustos–Ekim’de siyaha dönünce toplanıp kurutulur.',
            yetisme='Güney Çin, Hindiçin, Endonezya, Filipinler ve Kuzey '
                    'Avustralya; çalılıklar ve orman kenarları. Türkiye’de '
                    'yetişmez.',
            yoresel='Ya dan zi (Çince), biji makassar (Endonezce), Cava '
                    'bruseası. Yöresel ad yok.',
            karisma='⚠️ Aynı familyadan (Simaroubaceae) kuassia ve cennet '
                    'ağacı (Ailanthus) da acı ve kassinoitli; ayrı bitkiler. '
                    '"Makassar tohumu" adı başka tohumlar için de kullanılır.',
        ),
        ema=[],
        kaynak=[
            ['Fructus Bruceae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 1, 1999',
             who_url(1, 'fructus-bruceae')],
            ['X. Wang ve ark., “Efficacy and Safety of Brucea javanica Oil Emulsion Injection '
             'in the Treatment of Gastric Cancer: A Systematic Review and '
             'Meta-Analysis”, Frontiers in Nutrition 8, 2021',
             'https://pubmed.ncbi.nlm.nih.gov/34957186/'],
        ],
        rel=['kinin', 'pelin', 'huanglian'],
        en=dict(
            name='Ya dan zi (Java brucea)',
            other='The WHO monograph Fructus Bruceae (Volume 1); Chinese ya dan '
                  'zi ("duck-gall seed"), Indonesian biji makassar, English Java '
                  'brucea. The part is **the dried ripe fruit**. No Turkish or '
                  'EU monograph. Unknown in Turkey; the South-East Asian record '
                  'completing the WHO list in this catalog. ⚠️ Contains very '
                  'bitter, toxic quassinoids; not given to children or pregnant '
                  'women.',
            part='The dried ripe fruit; the seed oil (an emulsion in Chinese '
                 'oncology)',
            uses=[
                ['WHO — amoebic dysentery and malaria', 'The WHO monograph says '
                 '"uses supported by clinical data: none"; the pharmacopoeial '
                 'use (China, Viet Nam): **amoebic dysentery and malaria**. '
                 'Folk uses (without evidence): poultice on boils, ringworm, '
                 'whipworm, roundworm, tapeworm, haemorrhoids, enlarged spleen; '
                 'seed oil for warts and corns. Dose: 4–16 g a day for 3–7 days '
                 'in amoebiasis; 3–6 g for 4–5 days after meals in malaria. '
                 '**Contraindicated: children and pregnant women**; not given '
                 'in lactation. Adverse reaction: cases of anaphylaxis after '
                 'external application.'],
                ['South-East Asia and China — the bitter seed', 'The shrub is '
                 'native from southern China to Indonesia and northern '
                 'Australia; in Chinese medicine ya dan zi is the bitter fruit '
                 'that "clears heat and resolves toxin", in the 16th-century '
                 'Bencao Gangmu. In Indonesia and Malaysia (Makassar seed) for '
                 'dysentery and malaria. The fruit is so bitter that it is '
                 'swallowed wrapped in longan fruit skin — the classic method '
                 'of Chinese prescriptions.'],
                ['Modern Chinese oncology — the oil emulsion', 'An intravenous '
                 'emulsion made from the seed oil (BJOE) has been licensed in '
                 'China since the 1980s as an adjunct to cancer chemotherapy. '
                 'The 2021 Frontiers in Nutrition meta-analysis pooled 18 '
                 'randomised trials (1,210 patients) in gastric cancer: added to '
                 'chemotherapy it raised response rate and performance score '
                 'and reduced chemotherapy’s side effects (neutropenia, '
                 'nausea) — but all the trials are Chinese, most unblinded, '
                 'quality low. Those data belong to the standardised oil '
                 'emulsion, not the fruit.'],
            ],
            prep='This record recommends no dose; the WHO doses are a record of '
                 'the Chinese pharmacopoeial tradition and require medical '
                 'supervision. The fruit is not chewed (extremely bitter and '
                 'irritant); in Chinese tradition it is swallowed in a capsule '
                 'or longan skin. Not given to children or pregnant women. '
                 'Anaphylaxis has been reported on skin application. No product '
                 'in Turkey.',
            science='Ya dan zi is the plant in the WHO’s first volume marked '
                    '"no clinical data", with a pharmacology resting on '
                    'quassinoids (bruceantin, brusatol): strong amoebicidal and '
                    'antitumour activity in the laboratory, no controlled trial '
                    'in humans for dysentery or malaria. Bruceantin entered '
                    'phase II trials at the US National Cancer Institute in the '
                    '1970s–80s and was dropped for inefficacy and toxicity. '
                    'China’s oil-emulsion meta-analyses are positive but '
                    'methodologically weak. Evidence level Traditional; safety '
                    'Low — the WHO’s ban in children and pregnancy, '
                    'anaphylaxis and quassinoid toxicity.',
            safety='**Not given to children or pregnant women** — WHO '
                   'contraindication; not given in lactation. Quassinoids are '
                   'cytotoxic: nausea, vomiting, abdominal pain, liver and '
                   'kidney damage reported in overdose (Chinese literature). '
                   '**Anaphylaxis on external application** (WHO). '
                   'Gastrointestinal irritation; not used in gastric ulcer. '
                   'Short-term use (WHO: 3–7 days). Safety level Low.',
            fact='Its name is "duck-gall seed" — as bitter as gall. The Chinese '
                 'patient swallows it wrapped in longan skin; the US National '
                 'Cancer Institute tried the same seed’s molecule as a cancer '
                 'drug in the 1970s and gave up; China adds the same seed’s oil '
                 'to chemotherapy and says "it works" in eighteen trials. The '
                 'WHO, in 1999, wrote "no clinical data". The bitterest and '
                 'least known record in this catalog.',
            season='The fruit is picked and dried in August–October when it '
                   'turns black.',
            habitat='Southern China, Indochina, Indonesia, the Philippines and '
                    'northern Australia; scrub and forest edges. Does not grow '
                    'in Turkey.',
            local='Ya dan zi (Chinese), biji makassar (Indonesian), Java '
                  'brucea. No regional names.',
            confusion='⚠️ Quassia and the tree of heaven (Ailanthus) in the same '
                      'family (Simaroubaceae) are bitter and quassinoid-bearing '
                      'too; separate plants. The name "Makassar seed" is used '
                      'for other seeds as well.',
        ),
        etk_en=[
            ['No known interaction data (WHO)',
             'The monograph says "no information". The oil emulsion has been '
             'studied with chemotherapy; the oral fruit’s interactions with '
             'drugs are unknown. A theoretical risk with hepatotoxic drugs.'],
        ],
    ),

]
