# Talep sırası partisi IV (11–13 Aralık 2026): papaya, guava, karabiber.
# Türkçe Vikipedi yıllık görüntülenme: 16 / 4,9 / 4,6 bin.
from kunye_elle import who_url
Q = [

    dict(
        yayin='2026-12-10',
        id='papaya',
        foto='',
        tr='Papaya',
        la='Carica papaya L.',
        fam='Caricaceae',
        diger='Türkçe papaya, ağaç kavunu (Akdeniz’de); İngilizce papaya, pawpaw; '
              'Nahuatl kökenli değil, Karayip Arawak adından. TİTCK, AB ve DSÖ '
              'monografı yok. Kayıt, dang humması için yaprak özütünü sınayan '
              '2019 meta-analizine ve 2021 güvenlik derlemesine dayanıyor. '
              'Meyvesi besin; **yaprağı** tıbbi iddiaların konusu; **lateksi** '
              '(papain) sindirim enzimi kaynağı.',
        bolge=['kamerika', 'asya', 'anadolu'],
        kat=['besin', 'sifa'],
        kisim='Meyvesi (besin); yaprakları (özüt, suyu); olgunlaşmamış meyvenin '
              'lateksi (papain)',
        taxon='Carica papaya',
        kul=[
            ['Güney Asya — dang humması ve trombosit', 'Papaya yaprağının suyu '
             've standardize özütü Hindistan, Pakistan, Malezya ve '
             'Endonezya’da dang hummasında trombosit sayısını yükselttiği '
             'inancıyla yaygın kullanılıyor; Malezya ve Sri Lanka’da '
             'hastanelerde bile. 2019’da BMC Complementary and Alternative '
             'Medicine dergisinde yayımlanan Sri Lanka kaynaklı meta-analiz '
             '(9 çalışma) bu kullanımı sınadı — aşağıda.'],
            ['Orta Amerika — anavatan ve papain', 'Papaya Meksika ve Orta '
             'Amerika kökenli; Maya ve Karayip halkları meyvesini yiyip '
             'olgunlaşmamış meyvenin sütünü (lateks) et yumuşatmakta ve yara '
             'temizliğinde kullanmış. Bu lateksin enzimi papain bugün '
             'sindirim enzimi preparatlarında, et yumuşatıcıda ve yara '
             'debridman merhemlerinde kullanılıyor — bitkinin modern tıbba '
             'en somut katkısı.'],
            ['Türkiye', 'Papaya Türkiye’de Akdeniz kıyısında (Antalya, Mersin) '
             'seralarda yetiştirilmeye başlandı; meyvesi marketlerde. "Papaya '
             'yaprağı çayı" ve "papaya enzimi" kapsülleri aktarlarda '
             'satılıyor; TİTCK listesinde olmadığı için resmî bir uyarı '
             'metni yok. Yılda 16 bin arama çoğunlukla meyve ve "faydaları" '
             'için.'],
        ],
        haz='Meyve besin olarak yenir. Yaprak özütü için monograf dozu yok; '
            'dang çalışmalarında standardize özüt kısa süreli (3–5 gün) '
            'kullanılmış. Yaprak suyu çok acıdır ve uzun süreli kullanımı '
            'için güvenlik verisi yoktur. Papain preparatları eczane ürünü; '
            'ham lateks deriye ve ağza sürülmez — tahriş eder.',
        bilim='Papayanın tek sağlam klinik dosyası dang humması, ve o da '
              'belirsiz. 2019 meta-analizi dokuz çalışmada (çoğu Hindistan) '
              'yaprak özütünün trombosit sayısını yükselttiğini ve hastanede '
              'kalışı yaklaşık iki gün kısalttığını buldu — ama her iki bulguyu '
              'da "düşük kaliteli kanıt" diye niteliyor ve asıl sonuçlar '
              '(plazma sızıntısı, ağır komplikasyon, ölüm) için veri olmadığını '
              'yazıyor: "mevcut kanıt papayanın dangdaki rolü hakkında yorum '
              'yapmaya yetmiyor". 2021’de Malezya Sağlık Bakanlığı ekibinin '
              'güvenlik derlemesi (41 makale) kısa süreli kullanımı '
              'erişkinde iyi tolere edilir buluyor; uzun süreli kullanımda '
              'karaciğer ve üreme toksisitesi kaygısı (hayvan verisi) ve '
              'metformin, glimepirid, digoksin, siprofloksasin ile etkileşim '
              'bildiriyor. Kanıt düzeyi "sınırlı" — randomize veri var ama '
              'düşük kaliteli ve klinik anlamı belirsiz.',
        kanit='sinirli',
        guv='orta',
        guvNot='Meyve besin olarak güvenli; **lateks alerjisi** olanlar papaya '
               've papaine tepki verebilir (lateks-meyve sendromu). **Yaprak '
               'özütü kısa süreli (<5 gün) erişkinde iyi tolere ediliyor**; '
               'uzun kullanım için hayvan çalışmalarında karaciğer ve üreme '
               'toksisitesi kaygısı var. **Gebelikte yaprak ve olgunlaşmamış '
               'meyve kullanılmaz** — lateks rahim kasılması yapabilir (hayvan '
               'verisi; geleneksel kullanımda düşük yapıcı sayılır). Karaciğer '
               'hastalığı olanlar yaprak özütünden kaçınmalı. Olgun meyve '
               'gebelikte sorun değil. Dang hummasında papaya, tıbbi izlemin '
               'yerine geçmez.',
        etk=[
            ['Metformin ve glimepirid (ağızdan diyabet ilaçları)',
             '2021 güvenlik derlemesi yaprak özütünün kan şekerini düşürücü '
             'ilaçlarla olumsuz etkileşimini bildiriyor; birlikte hipoglisemi '
             'riski.'],
            ['Digoksin ve P-glikoprotein substratları',
             'Derleme digoksinle etkileşimi ve P-glikoprotein üzerinden '
             'genel bir riski kaydediyor; dar aralıklı ilaç kullananlar '
             'yaprak özütünden kaçınmalı.'],
            ['Siprofloksasin ve katyon bağlayan antibiyotikler',
             'Derleme siprofloksasin ve artemisininle etkileşim bildiriyor; '
             'antibiyotik emilimi azalabilir.'],
            ['Varfarin (papain)',
             'Papain preparatlarının kanamaya eğilimi artırabileceği '
             'bildirilmiş; antikoagülan kullananlar hekime söylemeli.'],
        ],
        ilginc='Güney Asya’da dang salgınlarında hastaneler papaya yaprağı '
               'suyuna yöneliyor; meta-analiz trombositin yükseldiğini '
               'doğruluyor ama hastanın daha az öldüğünü doğrulayamıyor — '
               'çünkü kimse ölçmemiş. Türkiye’de dang yok; papaya yaprağı '
               'yine de aktarda. Bitkinin tıbba en somut armağanı ise '
               'yaprağı değil, olgunlaşmamış meyvesinin sütü: et yumuşatan ve '
               'yara temizleyen papain.',
        ek=dict(
            mevsim='Tropiklerde yıl boyu meyve; Antalya seralarında yaz sonu–'
                   'sonbahar.',
            yetisme='Meksika ve Orta Amerika kökenli; tüm tropik kuşakta '
                    'ekiliyor. Türkiye’de Akdeniz kıyısında sera tarımı.',
            yoresel='Papaya, ağaç kavunu; yöresel ad yok.',
            karisma='"Pawpaw" adı Kuzey Amerika’da Asimina triloba için de '
                    'kullanılır — ilgisiz bitki. "Dağ papayası" (Vasconcellea) '
                    'ayrı cins.',
        ),
        ema=[],
        kaynak=[
            ['S. Rajapakse ve ark., “Carica papaya extract in dengue: a '
             'systematic review and meta-analysis”, BMC Complementary and '
             'Alternative Medicine 19, 2019',
             'https://pubmed.ncbi.nlm.nih.gov/31601215/'],
            ['X. Y. Lim ve ark., “Carica papaya L. Leaf: A Systematic Scoping '
             'Review on Biological Safety and Herb-Drug Interactions”, '
             'Evidence-Based Complementary and Alternative Medicine, 2021',
             'https://pubmed.ncbi.nlm.nih.gov/34040647/'],
        ],
        rel=['incir', 'nar', 'avokado'],
        en=dict(
            name='Papaya',
            other='Turkish papaya, ağaç kavunu (in the Mediterranean); English '
                  'papaya, pawpaw; the name is from Caribbean Arawak, not '
                  'Nahuatl. No Turkish, EU or WHO monograph. The record rests on '
                  'a 2019 meta-analysis of leaf extract in dengue and a 2021 '
                  'safety review. The fruit is food; **the leaf** is the subject '
                  'of medicinal claims; **the latex** (papain) is the source of '
                  'a digestive enzyme.',
            part='The fruit (food); the leaves (extract, juice); the latex of '
                 'unripe fruit (papain)',
            uses=[
                ['South Asia — dengue and platelets', 'Papaya leaf juice and '
                 'standardised extract are widely used in India, Pakistan, '
                 'Malaysia and Indonesia in the belief that they raise the '
                 'platelet count in dengue fever; even in hospitals in '
                 'Malaysia and Sri Lanka. A 2019 Sri Lankan meta-analysis (9 '
                 'studies) in BMC Complementary and Alternative Medicine tested '
                 'that use — below.'],
                ['Central America — homeland and papain', 'Papaya is native '
                 'to Mexico and Central America; the Maya and Caribbean '
                 'peoples ate the fruit and used the milk (latex) of the unripe '
                 'fruit to tenderise meat and clean wounds. Papain, the enzyme '
                 'of that latex, is used today in digestive enzyme '
                 'preparations, meat tenderiser and wound-debridement ointments '
                 '— the plant’s most concrete contribution to modern '
                 'medicine.'],
                ['Turkey', 'Papaya has begun to be grown under glass on the '
                 'Turkish Mediterranean coast (Antalya, Mersin); the fruit is '
                 'in supermarkets. "Papaya leaf tea" and "papaya enzyme" '
                 'capsules are sold by herbalists; as it is not on the Turkish '
                 'list there is no official warning text. The 16,000 searches '
                 'a year are mostly for the fruit and its "benefits".'],
            ],
            prep='The fruit is eaten as food. There is no monograph dose for '
                 'leaf extract; the dengue trials used a standardised extract '
                 'short-term (3–5 days). Leaf juice is very bitter and there '
                 'are no safety data for long-term use. Papain preparations '
                 'are pharmacy products; raw latex is not applied to skin or '
                 'mouth — it irritates.',
            science='Papaya’s one substantial clinical file is dengue fever, '
                    'and that is inconclusive. The 2019 meta-analysis found, '
                    'across nine studies (mostly Indian), that leaf extract '
                    'raised platelet counts and shortened hospital stay by about '
                    'two days — but grades both findings "low quality evidence" '
                    'and writes that there are no data on the outcomes that '
                    'matter (plasma leakage, severe complications, death): '
                    '"current evidence is insufficient to comment on the role '
                    'of papaya in dengue". The 2021 safety review by a Malaysian '
                    'Ministry of Health team (41 papers) finds short-term use '
                    'well tolerated in adults; concerns about liver and '
                    'reproductive toxicity in long-term use (animal data) and '
                    'interactions with metformin, glimepiride, digoxin and '
                    'ciprofloxacin. Evidence level Limited — randomised data '
                    'exist, but of low quality and uncertain clinical meaning.',
            safety='The fruit is safe as food; anyone with **latex allergy** '
                   'may react to papaya and papain (latex-fruit syndrome). '
                   '**Leaf extract is well tolerated short-term (<5 days) in '
                   'adults**; for long use there are liver and reproductive '
                   'toxicity concerns from animal studies. **Leaf and unripe '
                   'fruit are not used in pregnancy** — the latex may cause '
                   'uterine contractions (animal data; counted abortifacient in '
                   'traditional use). Anyone with liver disease should avoid '
                   'leaf extract. Ripe fruit is no problem in pregnancy. In '
                   'dengue, papaya is no substitute for medical monitoring.',
            fact='In South Asian dengue epidemics hospitals turn to papaya '
                 'leaf juice; the meta-analysis confirms that platelets rise '
                 'but cannot confirm that fewer patients die — because nobody '
                 'measured it. There is no dengue in Turkey; papaya leaf is '
                 'at the herbalist all the same. The plant’s most concrete '
                 'gift to medicine is not its leaf but the milk of its unripe '
                 'fruit: papain, which tenderises meat and cleans wounds.',
            season='Fruit year-round in the tropics; late summer–autumn in the '
                   'Antalya greenhouses.',
            habitat='Native to Mexico and Central America; grown throughout '
                    'the tropics. In Turkey, greenhouse cultivation on the '
                    'Mediterranean coast.',
            local='Papaya, ağaç kavunu; no regional names.',
            confusion='The name "pawpaw" is also used in North America for '
                      'Asimina triloba — an unrelated plant. "Mountain papaya" '
                      '(Vasconcellea) is a separate genus.',
        ),
        etk_en=[
            ['Metformin and glimepiride (oral diabetes drugs)',
             'The 2021 safety review reports unfavourable interaction of leaf '
             'extract with blood-sugar-lowering drugs; risk of hypoglycaemia '
             'together.'],
            ['Digoxin and P-glycoprotein substrates',
             'The review records an interaction with digoxin and a general '
             'risk via P-glycoprotein; anyone on narrow-margin drugs should '
             'avoid leaf extract.'],
            ['Ciprofloxacin and cation-chelating antibiotics',
             'The review reports interaction with ciprofloxacin and '
             'artemisinin; antibiotic absorption may fall.'],
            ['Warfarin (papain)',
             'Papain preparations have been reported to increase bleeding '
             'tendency; anyone on anticoagulants should tell their doctor.'],
        ],
    ),

    dict(
        yayin='2026-12-11',
        id='guava',
        foto='',
        tr='Guava',
        la='Psidium guajava L.',
        fam='Myrtaceae (mersingiller)',
        diger='DSÖ monografı (Folium Guavae, Cilt 4) sinonimleri Psidium '
              'aromaticum L., P. pomiferum L., P. pyriferum L. diye veriyor; '
              'adlar arasında guava, goiaba, amrood, amrud, djambu, bayabas var. '
              'Türkçe guava, guyava. Monografın kullanılan kısmı **kurutulmuş '
              've/veya genç yaprak** — meyve değil. TİTCK ve AB monografı yok. '
              'Kataloğumuzun mersingillerden üyesi; mersin ve karanfil ile '
              'aynı familya.',
        bolge=['kamerika', 'asya', 'afrika'],
        kat=['sifa', 'besin'],
        kisim='Yaprakları (monograf); meyvesi (besin)',
        taxon='Psidium guajava',
        kul=[
            ['DSÖ — ishal ve diş eti', 'DSÖ monografı guava yaprağını "klinik '
             'verilerle desteklenen kullanım" başlığında veriyor: **akut '
             'ishal, diş eti iltihabı (gingivit) ve rotavirüs enteriti** '
             '(ağızdan). Monografın aktardığı çalışmalar: 70 kişide yaprak '
             'dekoksiyonlu gargara diş eti iltihabını plaseboya göre azalttı; '
             '62 çocukta rotavirüs ishalinde dekoksiyon iyileşmeyi hızlandırdı '
             '(3 günde yüzde 87’ye karşı 58); 100 erişkinde kersetin '
             'standardize özüt karın ağrısı süresini kısalttı; 122 hastada '
             'toz yaprak tetrasiklinle benzer sonuç verdi. Geleneksel '
             'kullanımlar: karın ağrısı, diş eti kanaması, öksürük, gastrit, '
             'yara, solucan.'],
            ['Orta ve Güney Amerika — anavatan', 'Guava tropik Amerika '
             'kökenli; Meksika’dan Peru’ya yaprağı ishal ve mide için çay, '
             'meyvesi besin. Portekizliler ve İspanyollar 16. yüzyılda Asya ve '
             'Afrika’ya taşıdı; bugün Hindistan dünyanın en büyük '
             'üreticisi.'],
            ['Türkiye', 'Guava Türkiye’de yetişmiyor; meyvesi ithal, yaprağı '
             'aktarlarda nadiren. Yılda beş bin arama meyve ve "guava yaprağı '
             'çayı" için. Monograf meyve için hiçbir şey söylemiyor — meyveye '
             'atfedilen "şeker düşürücü" iddiaların kaynağı monograf değil.'],
        ],
        haz='DSÖ monografı: ishal için **günde üç-dört kez 500 mg toz '
            'yaprak**; gargara için günde üç kez 15 ml sulu özüt, en az bir '
            'dakika. Önerilen doz ve süre aşılmamalı. 12 yaş altında, '
            'gebelikte ve emzirirken veri yokluğu nedeniyle önerilmiyor '
            '(monograf; rotavirüs çalışmasının çocuklarda yapılmış olmasına '
            'karşın).',
        bilim='Guava yaprağı, kataloğumuzda DSÖ’nün "klinik verilerle '
              'desteklenen" dediği az sayıda bitkiden. Monografın dayandığı '
              'dört çalışma randomize ve kontrollü ama küçük (62–122 kişi), '
              'tek merkezli ve çoğu 1990–2000’lerden; rotavirüs çalışması '
              'Çin’den, ishal çalışmaları Meksika’dan. Tetrasiklinle '
              '"fark yok" bulgusu etkiyi kanıtlamaz, yalnızca ayırt '
              'edemediğini söyler. Sonraki yıllarda meyve ve yaprağın kan '
              'şekerine etkisi üzerine küçük çalışmalar yapıldı ama monograf '
              'bunu kapsamıyor. Kanıt düzeyini "sınırlı" yazdık: randomize '
              'veri var, bağımsız tekrar yok.',
        kanit='sinirli',
        guv='orta',
        guvNot='DSÖ monografı tek yan etki bildiriyor: yaprak çayının deriye '
               'sürülmesinden sonra bir alerjik dermatit olgusu. '
               'Kontrendikasyon: bitkiye aşırı duyarlılık. **Önerilen doz ve '
               'süre aşılmamalı**; yaprak tanenlidir, uzun kullanımda kabızlık '
               've demir emiliminde azalma kuramsal risk. 12 yaş altında, '
               'gebelikte ve emzirirken önerilmiyor. İshal kanlıysa, ateşliyse '
               'ya da iki günü aşıyorsa guava değil hekim. Meyve besin olarak '
               'güvenli.',
        etk=[
            ['Antidiyabetikler (kuramsal)',
             'DSÖ monografı etkileşim vermiyor. Yaprak özütünün kan şekerini '
             'düşürebildiğine dair küçük çalışmalar var; diyabet ilacı '
             'kullananlar hekime söylemeli.'],
            ['Demir preparatları (kuramsal)',
             'Tanenli yapraklar için genel kural; monografta yazmıyor.'],
        ],
        ilginc='Meyvesi için aranan bir bitkinin monografı yalnızca yaprağına '
               'ait ve meyvesi hakkında tek kelime etmiyor. Yaprak ise DSÖ’nün '
               '"klinik veri" dediği nadir bitkilerden: 62 Çinli çocukta '
               'rotavirüs ishali bir gün erken kesildi. Türkiye’de ne guava '
               'yetişir ne rotavirüs için guava verilir — ama aşı var, ve '
               'yaprak çayı aktarda.',
        ek=dict(
            mevsim='Tropiklerde yıl boyu çiçek ve meyve; yaprak her zaman '
                   'toplanır, genç yaprak tercih edilir.',
            yetisme='Tropik Amerika kökenli; tüm tropik ve subtropik kuşakta '
                    'ekiliyor. Türkiye’de yetişmez.',
            yoresel='Guava, guyava; yöresel ad yok.',
            karisma='Çilek guavası (Psidium cattleyanum) ayrı tür; "feijoa" '
                    '(Acca sellowiana) aynı familya, ayrı cins. Monograf '
                    'yalnızca P. guajava yaprağı içindir.',
        ),
        ema=[],
        kaynak=[
            ['Folium Guavae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 4, 2009',
             who_url(4, 'folium-guavae')],
        ],
        rel=['karanfil', 'nar', 'cay'],
        en=dict(
            name='Guava',
            other='The WHO monograph (Folium Guavae, Volume 4) gives the '
                  'synonyms Psidium aromaticum L., P. pomiferum L., P. '
                  'pyriferum L.; among its names guava, goiaba, amrood, amrud, '
                  'djambu, bayabas. Turkish guava, guyava. The monograph’s part '
                  'is **the dried and/or young leaf** — not the fruit. No '
                  'Turkish or EU monograph. The myrtle-family member of this '
                  'catalog; the same family as myrtle and clove.',
            part='The leaves (monograph); the fruit (food)',
            uses=[
                ['WHO — diarrhoea and gums', 'The WHO monograph places guava '
                 'leaf under "uses supported by clinical data": **acute '
                 'diarrhoea, gingivitis and rotaviral enteritis** (orally). The '
                 'studies the monograph reports: in 70 people a mouthwash of '
                 'leaf decoction reduced gum inflammation against placebo; in '
                 '62 children with rotaviral diarrhoea a decoction hastened '
                 'recovery (87% versus 58% at 3 days); in 100 adults a '
                 'quercetin-standardised extract shortened the duration of '
                 'abdominal pain; in 122 patients powdered leaf gave results '
                 'similar to tetracycline. Traditional uses: abdominal pain, '
                 'bleeding gums, cough, gastritis, wounds, worms.'],
                ['Central and South America — the homeland', 'Guava is native '
                 'to tropical America; from Mexico to Peru the leaf is a tea '
                 'for diarrhoea and stomach, the fruit a food. The Portuguese '
                 'and Spanish carried it to Asia and Africa in the 16th '
                 'century; India is now the world’s largest producer.'],
                ['Turkey', 'Guava does not grow in Turkey; the fruit is '
                 'imported, the leaf rarely at herbalists. The five thousand '
                 'searches a year are for the fruit and "guava leaf tea". The '
                 'monograph says nothing about the fruit — the "blood-sugar '
                 'lowering" claims attached to the fruit do not come from the '
                 'monograph.'],
            ],
            prep='WHO monograph: for diarrhoea, **500 mg of powdered leaf '
                 'three or four times daily**; as a mouthwash, 15 ml of aqueous '
                 'extract three times daily for at least one minute. Do not '
                 'exceed the recommended dose or duration. Not recommended '
                 'under 12, in pregnancy or lactation for lack of data (the '
                 'monograph, despite the rotavirus trial having been done in '
                 'children).',
            science='Guava leaf is one of the few plants in this catalog the '
                    'WHO calls "supported by clinical data". The four trials the '
                    'monograph rests on are randomised and controlled but small '
                    '(62–122 people), single-centre and mostly from the '
                    '1990s–2000s; the rotavirus trial is from China, the '
                    'diarrhoea trials from Mexico. The "no difference" finding '
                    'against tetracycline does not prove an effect, only that '
                    'the trial could not tell them apart. Small studies of the '
                    'fruit and leaf on blood sugar followed in later years, but '
                    'the monograph does not cover them. We record the evidence '
                    'level as Limited: randomised data exist, with no '
                    'independent replication.',
            safety='The WHO monograph reports one adverse reaction: a case of '
                   'allergic dermatitis after applying leaf tea to the skin. '
                   'Contraindication: hypersensitivity to the plant. **Do not '
                   'exceed the recommended dose or duration**; the leaf is '
                   'tannin-rich, with a theoretical risk of constipation and '
                   'reduced iron absorption in long use. Not recommended under '
                   '12, in pregnancy or lactation. If diarrhoea is bloody, '
                   'feverish or lasts beyond two days, a doctor, not guava. The '
                   'fruit is safe as food.',
            fact='A plant searched for its fruit has a monograph that belongs '
                 'only to its leaf and says not a word about the fruit. The '
                 'leaf, meanwhile, is one of the rare plants the WHO credits '
                 'with "clinical data": in 62 Chinese children rotaviral '
                 'diarrhoea stopped a day early. In Turkey guava neither grows '
                 'nor is given for rotavirus — but there is a vaccine, and leaf '
                 'tea at the herbalist.',
            season='Flowers and fruit year-round in the tropics; the leaf is '
                   'picked at any time, young leaf preferred.',
            habitat='Native to tropical America; grown throughout the tropics '
                    'and subtropics. Does not grow in Turkey.',
            local='Guava, guyava; no regional names.',
            confusion='Strawberry guava (Psidium cattleyanum) is a separate '
                      'species; "feijoa" (Acca sellowiana) is the same family, '
                      'separate genus. The monograph is for the P. guajava leaf '
                      'only.',
        ),
        etk_en=[
            ['Antidiabetics (theoretical)',
             'The WHO monograph gives no interaction. Small studies suggest '
             'leaf extract can lower blood sugar; anyone on diabetes '
             'medication should tell their doctor.'],
            ['Iron preparations (theoretical)',
             'The general rule for tannin-rich leaves; not in the '
             'monograph.'],
        ],
    ),

    dict(
        yayin='2026-12-12',
        id='karabiber',
        foto='',
        tr='Karabiber',
        la='Piper nigrum L.',
        fam='Piperaceae (karabibergiller)',
        diger='TİTCK monografı Türkçe adı "karabiber" diye veriyor, sinonim '
              'göstermiyor. İngilizce black pepper; Sanskritçe pippali '
              'akrabası; "biber" sözcüğü Türkçeye Yunanca piperi’den, o da '
              'Sanskritçeden. Monografın kullanılan kısmı **olgunlaşmadan '
              'toplanıp kurutulmuş meyve ve uçucu yağ**. AB ve DSÖ monografı '
              'yok. Kırmızı biber (Capsicum) başka familyadandır; "biber" adı '
              'ortak ama bitki değil.',
        bolge=['asya', 'anadolu'],
        kat=['besin', 'sifa'],
        kisim='Olgunlaşmadan toplanıp kurutulmuş meyveleri; uçucu yağı',
        taxon='Piper nigrum',
        kul=[
            ['Türkiye — resmî liste', 'TİTCK monografı kurutulmuş meyveyi ve '
             'uçucu yağı listeliyor; uyarıları: aşırı duyarlılık; uzun süreli '
             'ağızdan ya da deriye kullanımda duyarlı kişilerde egzama ve '
             'dermatit; 12 yaş altı, gebelik ve emzirmede önerilmiyor. '
             'Etkileşim bölümü kataloğumuzun en iyi gerekçelendirilmişlerinden: '
             'etken madde **piperin**, propranolol, teofilin, beta-laktam '
             'antibiyotikler ve fenitoinin biyoyararlanımını değiştirebilir — '
             'monograf her biri için insan ya da hayvan çalışmasını künye '
             'olarak veriyor. Kaynakları arasında 2019 Critical Reviews in '
             'Food Science and Nutrition sistematik derlemesi var.'],
            ['Hindistan — Malabar’ın kara altını', 'Karabiber Hindistan’ın '
             'Malabar kıyısına (Kerala) yerli; Roma İmparatorluğu’nun '
             'Hindistan’dan aldığı başlıca mal, Orta Çağ’ın "kara altını", '
             'Portekiz’in Hint Okyanusu’na açılma nedeni. Ayurveda’da '
             '"trikatu"nun (üç acı: karabiber, uzun biber, zencefil) bileşeni; '
             'sindirimi uyarıcı ve "ilaçların taşıyıcısı" sayılır — '
             'piperinin emilimi artırıcı etkisi bu geleneksel iddianın modern '
             'karşılığı.'],
            ['Anadolu ve Osmanlı', 'Baharat Yolu’nun Anadolu’dan geçişi '
             'karabiberi Osmanlı mutfağının ve eczacılığının temel maddesi '
             'yaptı; "biber" sözcüğü Türkçeye önce bu bitki için girdi, '
             'Amerika’dan gelen Capsicum sonradan aynı adı aldı. Halk '
             'hekimliğinde soğuk algınlığında bal ve karabiber, hazımsızlıkta '
             'yemeklere fazladan karabiber — mutfak ve ilaç ayrımı belirsiz.'],
        ],
        haz='TİTCK monografı doz vermiyor. Mutfak dozunda baharat olarak '
            'kullanılır. Uçucu yağ ağızdan alınmaz, deriye seyreltilmeden '
            'sürülmez. Piperin kapsülleri (çoğu zerdeçal ürünlerinde "emilim '
            'artırıcı" olarak) ölçülü ve ilaç etkileşimleri göz önünde '
            'tutularak. 12 yaş altı, gebelik ve emzirmede tıbbi doz '
            'önerilmiyor; baharat dozu ayrı.',
        bilim='Karabiberin bilimsel dosyası tek bir molekül etrafında dönüyor: '
              'piperin. 1991’de European Journal of Clinical Pharmacology '
              'dergisinde sağlıklı gönüllülerde piperinin propranolol ve '
              'teofilin kan düzeylerini yükselttiği gösterildi; 1998’de Planta '
              'Medica’da piperinin kürkümin biyoyararlanımını insanda '
              'yaklaşık yirmi kat artırdığı bildirildi — bugün her '
              '"zerdeçal + karabiber" ürününün dayandığı çalışma. 2019’da '
              'Critical Reviews in Food Science and Nutrition dergisinde '
              'yayımlanan sistematik derleme (TİTCK’nin de kaynağı) halk '
              'kullanımlarından farmakolojiye kadar literatürü topluyor ve '
              'karabiberin kendisine ait randomize klinik sonlanım '
              'çalışmasının azlığını teslim ediyor. Yani kanıt, karabiberin '
              'bir hastalığı iyileştirdiğine değil, **başka ilaçların kan '
              'düzeyini değiştirdiğine** dair — ve bu kanıt sağlam. Kanıt '
              'düzeyi "sınırlı".',
        kanit='sinirli',
        guv='orta',
        guvNot='Mutfak dozunda güvenli ve evrensel. **Piperin ilaçların emilimini '
               've metabolizmasını değiştirir** — monografın saydığı '
               'propranolol, teofilin, beta-laktam antibiyotikler ve fenitoin '
               'için kan düzeyi yükselebilir; dar güvenlik aralıklı ilaç '
               'kullananlar piperin takviyesi almamalı. Uzun süreli ya da '
               'yüksek doz kullanımda egzama ve dermatit; uçucu yağ deriyi '
               'tahriş eder. Reflü ve mide ülserinde fazlası rahatsız eder. '
               '12 yaş altı, gebelik ve emzirmede tıbbi doz önerilmiyor. '
               'Güvenlik "orta" — baharat için yüksek, piperin takviyesi için '
               'orta.',
        etk=[
            ['Propranolol ve teofilin',
             'TİTCK monografının künye verdiği 1991 insan çalışması: piperin '
             'her iki ilacın kan düzeyini ve etkisini artırdı. Beta bloker ya '
             'da teofilin kullananlar piperin takviyesinden kaçınmalı.'],
            ['Fenitoin',
             'TİTCK’nin künye verdiği 2001 çalışması: besindeki piperin '
             'fenitoinin farmakokinetiğini değiştiriyor. Epilepsi ilacı '
             'kullananlar için dikkat.'],
            ['Beta-laktam antibiyotikler',
             'TİTCK’nin künye verdiği 2002 sıçan çalışması: piperin '
             'amoksisilin ve sefalosporinlerin kan düzeyini artırdı. İnsan '
             'verisi sınırlı.'],
            ['Kürkümin ve diğer takviyeler',
             'Piperin kürkümin emilimini çarpıcı biçimde artırır (1998 insan '
             'çalışması); aynı mekanizma — CYP3A4 ve P-glikoprotein inhibisyonu '
             '— başka ilaçlar için de geçerlidir. Piperin "emilim artırıcı" '
             'olarak satılan her ürün, etkileşim potansiyeli taşır.'],
        ],
        ilginc='Roma’nın altınını Hindistan’a akıtan, Vasco da Gama’yı Ümit '
               'Burnu’ndan dolaştıran baharat, bugün tıpta kendi etkisiyle '
               'değil başkalarının etkisini değiştirmesiyle anılıyor: piperin, '
               'kürkümini yirmi kat, propranololü ölçülebilir ölçüde '
               'yükseltiyor. TİTCK monografı bu yüzden bir ilaç kitabı gibi '
               'yazılmış — on üç künye, dört ilaç. Her sofrada duran, '
               'kataloğumuza 275. sırada giren bitki.',
        ek=dict(
            mevsim='Tropiklerde yılda iki hasat; meyve salkımları yeşilken '
                   'toplanıp güneşte kurutulur, kararır. Beyaz biber aynı '
                   'meyvenin kabuğu soyulmuş hâli, yeşil biber olgunlaşmamış '
                   'tazesi.',
            yetisme='Güney Hindistan (Malabar) kökenli tırmanıcı; Vietnam, '
                    'Brezilya, Endonezya ve Hindistan başlıca üreticiler. '
                    'Türkiye’de yetişmez.',
            yoresel='Karabiber — TİTCK adı. Beyaz biber, yeşil biber aynı '
                    'bitkinin işlenmiş biçimleri.',
            karisma='Kırmızı biber ve acı biber (Capsicum, patlıcangiller) '
                    'ayrı bitki, ayrı kayıt. Pembe biber (Schinus) sumakgil, '
                    'ilgisiz. Uzun biber (Piper longum) aynı cins, ayrı tür.',
        ),
        ema=[],
        kaynak=[
            ['Piper nigrum L. monografı, TİTCK Tıbbi Bitki Listesi',
             'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/PipernigrumL_8b64c042-a99e-4d71-9cd3-c7b33a4836da.pdf'],
            ['H. Takooree ve ark., “A systematic review on black pepper (Piper '
             'nigrum L.): from folk uses to pharmacological applications”, '
             'Critical Reviews in Food Science and Nutrition 59(sup1), 2019',
             'https://pubmed.ncbi.nlm.nih.gov/30740986/'],
            ['G. Shoba ve ark., “Influence of piperine on the pharmacokinetics '
             'of curcumin in animals and human volunteers”, Planta Medica '
             '64(4), 1998',
             'https://pubmed.ncbi.nlm.nih.gov/9619120/'],
        ],
        rel=['zerdecal', 'zencefil', 'acibiber', 'kakule'],
        en=dict(
            name='Black pepper',
            other='The Turkish monograph gives the name "karabiber" and lists '
                  'no synonyms. The Turkish word "biber" entered via Greek '
                  'piperi, itself from Sanskrit. The monograph’s part is **the '
                  'fruit picked unripe and dried, and the essential oil**. No '
                  'EU or WHO monograph. Red pepper (Capsicum) is another family; '
                  'the name "biber" is shared, the plant is not.',
            part='The fruit, picked unripe and dried; the essential oil',
            uses=[
                ['Turkey — official list', 'The Turkish monograph lists the '
                 'dried fruit and the essential oil; its warnings: '
                 'hypersensitivity; eczema and dermatitis in sensitive people '
                 'with long oral or topical use; not recommended under 12, in '
                 'pregnancy or lactation. Its interaction section is among the '
                 'best-justified in this catalog: the active constituent '
                 '**piperine** may alter the bioavailability of propranolol, '
                 'theophylline, beta-lactam antibiotics and phenytoin — and the '
                 'monograph cites a human or animal study for each. Among its '
                 'sources is the 2019 systematic review in Critical Reviews in '
                 'Food Science and Nutrition.'],
                ['India — the black gold of Malabar', 'Black pepper is native '
                 'to India’s Malabar coast (Kerala); the chief good the Roman '
                 'Empire bought from India, the "black gold" of the Middle '
                 'Ages, the reason Portugal sailed into the Indian Ocean. In '
                 'Ayurveda an ingredient of "trikatu" (three pungents: black '
                 'pepper, long pepper, ginger), counted a digestive stimulant '
                 'and "carrier of medicines" — piperine’s '
                 'absorption-enhancing effect is the modern counterpart of '
                 'that traditional claim.'],
                ['Anatolia and the Ottomans', 'The Spice Route’s passage '
                 'through Anatolia made black pepper a staple of Ottoman '
                 'cooking and pharmacy; the word "biber" entered Turkish first '
                 'for this plant, and the Capsicum that came from the Americas '
                 'took the same name later. In folk medicine honey and black '
                 'pepper for colds, extra pepper on food for indigestion — the '
                 'line between kitchen and medicine is blurred.'],
            ],
            prep='The Turkish monograph gives no dose. Used as a spice at '
                 'kitchen doses. The essential oil is not taken by mouth or '
                 'applied undiluted to the skin. Piperine capsules (mostly as '
                 '"absorption enhancer" in turmeric products) in moderation and '
                 'with drug interactions in mind. Medicinal doses not '
                 'recommended under 12, in pregnancy or lactation; spice doses '
                 'are a separate matter.',
            science='Black pepper’s scientific file turns on a single molecule: '
                    'piperine. In 1991 the European Journal of Clinical '
                    'Pharmacology showed piperine raising blood levels of '
                    'propranolol and theophylline in healthy volunteers; in '
                    '1998 Planta Medica reported piperine increasing curcumin '
                    'bioavailability in humans about twentyfold — the study '
                    'every "turmeric + black pepper" product rests on today. '
                    'The 2019 systematic review in Critical Reviews in Food '
                    'Science and Nutrition (also a Turkish monograph source) '
                    'collects the literature from folk uses to pharmacology and '
                    'concedes the scarcity of randomised clinical outcome '
                    'trials of black pepper itself. So the evidence is not that '
                    'black pepper cures a disease but that **it changes the '
                    'blood levels of other drugs** — and that evidence is '
                    'solid. Evidence level Limited.',
            safety='Safe and universal at kitchen doses. **Piperine alters the '
                   'absorption and metabolism of drugs** — blood levels may '
                   'rise for the propranolol, theophylline, beta-lactam '
                   'antibiotics and phenytoin the monograph names; anyone on '
                   'narrow-margin drugs should not take piperine supplements. '
                   'Eczema and dermatitis with long or high-dose use; the '
                   'essential oil irritates skin. Excess aggravates reflux and '
                   'gastric ulcer. Medicinal doses not recommended under 12, in '
                   'pregnancy or lactation. Safety Medium — high as a spice, '
                   'medium for piperine supplements.',
            fact='The spice that drained Rome’s gold to India and sent Vasco '
                 'da Gama round the Cape is remembered in medicine today not '
                 'for its own effect but for changing the effects of others: '
                 'piperine raises curcumin twentyfold and propranolol '
                 'measurably. That is why the Turkish monograph reads like a '
                 'drug handbook — thirteen references, four drugs. A plant on '
                 'every table, entering this catalog in 275th place.',
            season='Two harvests a year in the tropics; the fruit spikes are '
                   'picked green and sun-dried, turning black. White pepper is '
                   'the same fruit with the skin removed, green pepper the '
                   'fresh unripe fruit.',
            habitat='A climber native to south India (Malabar); Vietnam, '
                    'Brazil, Indonesia and India the main producers. Does not '
                    'grow in Turkey.',
            local='Karabiber — the Turkish monograph name. White and green '
                  'pepper are processed forms of the same plant.',
            confusion='Red pepper and chilli (Capsicum, nightshade family) are '
                      'a separate plant, separate record. Pink pepper (Schinus) '
                      'is cashew family, unrelated. Long pepper (Piper longum) '
                      'is the same genus, separate species.',
        ),
        etk_en=[
            ['Propranolol and theophylline',
             'The 1991 human study the Turkish monograph cites: piperine '
             'increased the blood levels and effects of both drugs. Anyone on '
             'a beta-blocker or theophylline should avoid piperine '
             'supplements.'],
            ['Phenytoin',
             'The 2001 study the Turkish monograph cites: dietary piperine '
             'alters phenytoin pharmacokinetics. Care for anyone on epilepsy '
             'medication.'],
            ['Beta-lactam antibiotics',
             'The 2002 rat study the Turkish monograph cites: piperine raised '
             'blood levels of amoxicillin and cephalosporins. Human data '
             'limited.'],
            ['Curcumin and other supplements',
             'Piperine strikingly increases curcumin absorption (1998 human '
             'study); the same mechanism — CYP3A4 and P-glycoprotein '
             'inhibition — applies to other drugs. Every product sold with '
             'piperine as an "absorption enhancer" carries interaction '
             'potential.'],
        ],
    ),

]
