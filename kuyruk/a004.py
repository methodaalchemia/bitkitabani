# Parti 004 (24 Kasım 2026): Kuzey ve Orta Amerika kökenli sekiz bitki.
# Kaynak notu: PubMed ve PMC sayfaları WebFetch'e reCAPTCHA döndürdüğü için
# özetler ve tam metinler NCBI'nin kendi E-utilities servisi üzerinden okundu;
# adresler aynı kayıtların pubmed.ncbi.nlm.nih.gov / PMC adresleridir.
POWO = 'https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:'
Q = [

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='chia',
        foto='',
        tr='Chia',
        la='Salvia hispanica L.',
        taxon='Salvia hispanica',
        fam='Lamiaceae (ballıbabagiller)',
        diger='Chia tohumu; İspanyolca chía; İngilizce chia, chia seed. Kew '
              'POWO adı kabul edilmiş ad olarak verir ve eş ad listelemez. '
              'Kullanılan kısım tohumdur. Avrupa Birliği’nde bitkisel ilaç '
              'olarak değil, "yeni gıda" olarak değerlendirilmiştir (EFSA).',
        bolge=['kamerika'],
        kat=['besin'],
        kisim='Tohum (bütün ya da öğütülmüş)',
        kul=[
            ['Mezoamerika — temel besin ve ilaç bitkisi',
             'Economic Botany dergisinde 2003’te yayımlanan etnobotanik '
             'derleme, chia’yı Kolomb öncesi Mezoamerika’nın önemli bir temel '
             'besini ve ilaç bitkisi olarak tanımlar. Aynı derleme, bitkinin '
             'horozibiği (amarant) ve kazayağı türlerine göre çok daha az '
             'araştırıldığını belirtir. Yazar, 16. yüzyıl Meksika '
             'kodekslerindeki kayıtları sonraki yayınlarla karşılaştırmıştır.'],
            ['Meksika ve Guatemala — sömürge döneminden sonra değişen kullanım',
             'Aynı derlemeye göre İspanyol sömürgeleştirmesinden sonra '
             'chia’nın tıbbi, mutfak, sanat ve dinî kullanımlarında küçük '
             'ama izlenebilir kaymalar olmuştur. Yazar bu değişimi Meksika’nın '
             'batısında ve Guatemala yaylalarında yaptığı saha çalışmasıyla '
             'sınamıştır. Derleme, etnobotanik bilginin azalmasının ve '
             'yaşam alanı kaybının hem tohum kaynaklarını hem de bitkiye '
             'ilişkin bilgiyi zayıflattığı sonucuna varır.'],
            ['Avrupa Birliği — "yeni gıda" olarak izin',
             'EFSA’nın 2019 tarihli görüşüne göre chia tohumunun AB pazarına '
             'ilk izni 2009’da, yalnızca ekmek ürünleri için verilmiştir; '
             'o değerlendirmede ekmekte %5 oranı ele alınmıştı. İzin sonraki '
             'yıllarda unlu mamuller, kahvaltılık tahıllar, meyve-kuruyemiş-'
             'tohum karışımları, meyve suları, yoğurt ve ön ambalajlı tohum '
             'gibi kategorilere genişletilmiştir. EFSA, tohumun Latin '
             'Amerika’da yüzlerce yıllık bir tüketim geçmişi olduğunu da '
             'kaydeder.'],
            ['Günümüz — takviye olarak tüketim',
             'Nutrition Reviews’ta 2018’de yayımlanan sistematik derleme, '
             'chia tohumunun bugün yaygın bir besin takviyesi olduğunu ve '
             'başlıca alfa-linolenik asit, bitkisel protein ve diyet lifi '
             'içeriği için alındığını yazar. Aynı derleme, klinik etkilerine '
             'ilişkin bilginin yetersiz olduğunu da belirtir.'],
        ],
        haz='Resmî bir monografta kabul edilmiş bir doz yoktur; chia bir '
            'gıdadır. EFSA görüşünde tohumun bütün ya da öğütülmüş hâlde '
            'ekmeğe, yoğurda, meyve sularına ve tahıl karışımlarına katıldığı '
            'anlatılır. Aynı görüşteki AB kullanım geçmişi tablosunda tek '
            'başına satılan tohum için **günde 15 g** miktarı geçer. EFSA, '
            'chia unu katılıp 190 °C’de pişirilen bisküvilerde akrilamid '
            'oluşumunun arttığını gösteren bir çalışmaya dikkat çekmiş ve '
            'yüksek ısıda pişirilen ürünleri ayrıca değerlendirmeye '
            'bırakmıştır.',
        bilim='Nutrition Reviews’taki 2018 tarihli sistematik derleme ve '
              'meta-analiz 12 randomize kontrollü çalışmayı incelemiştir; '
              'katılımcılar sağlıklı kişiler, sporcular, diyabet hastaları ve '
              'metabolik sendromlu kişilerdi. Birleştirilmiş sonuçlarda '
              'anlamlı fark bulunmamış, yalnızca yüksek dozlu alt grup '
              'analizlerinde yemek sonrası kan şekerinde düşüş, HDL’de '
              '0,10 mmol/L azalma ve diyastolik tansiyonda 7,14 mmHg düşüş '
              'görülmüştür. Yazarlar **bütün kanıtın kalitesini düşük ya da '
              'çok düşük** bulmuş, çalışmaların yalnızca dolaylı göstergeleri '
              'ölçtüğünü vurgulamıştır. Aynı dergide 2025’te yayımlanan ve '
              '8 çalışmayı kapsayan meta-analiz sistolik tansiyonda '
              '7,19 mmHg, diyastolik tansiyonda 6,04 mmHg düşüş bildirmiş; '
              'vücut ağırlığı, bel çevresi, açlık kan şekeri ve HbA1c üzerinde '
              'anlamlı etki bulmamıştır. Bu derleme de verinin sınırlı '
              'olduğunu belirtir. Kalp hastalığı ya da ölüm gibi klinik '
              'sonuçları ölçen bir çalışma bu kaynaklarda yoktur.',
        kanit='sinirli',
        guv='dusuk',
        guvNot='EFSA 2019 görüşünde chia tohumunu değerlendirilen kullanım '
               'koşullarında güvenli bulmuştur; günde 50 g’ın 12 hafta '
               'verildiği 76 kişilik çalışmada tohuma bağlı istenmeyen etki '
               'bildirilmemiştir. EFSA’nın belirlediği tek tehlike '
               '**alerjidir**: iki olgu sunumunda ağızda kaşıntı, yaygın '
               'kurdeşen, yüzde şişme, nefes darlığı ve el egzaması '
               'tanımlanmıştır. Yer fıstığı ve susam alerjisi olanların '
               'serumlarıyla çapraz tepkime de kaydedilmiştir; bu alerjileri '
               'olanlar dikkatli olmalıdır. Dayanak alınan kaynaklarda '
               'gebelik, emzirme ve çocuklar için ayrı bir değerlendirme '
               'yoktur; gıda miktarlarının üzerindeki kullanım için veri '
               'bulunmaz. Meta-analizlerde tansiyonda düşüş bildirildiğinden, '
               'tansiyon ilacı kullananların düzenli ve yüksek miktarda '
               'tüketimi hekimine söylemesi uygun olur; bu konuda bir '
               'etkileşim çalışması yoktur.',
        ilginc='Latin Amerika’da yüzlerce yıldır yenen bu tohum, Avrupa '
               'Birliği hukukunda "yeni gıda" sayılır. EFSA’ya göre AB '
               'pazarına ilk izin 2009’da ve yalnızca ekmek ürünleri için '
               'verilmiştir.',
        ek=dict(
            mevsim='EFSA görüşü bitkiyi yazlık, tek yıllık otsu bir bitki '
                   'olarak tanımlar. Türkiye için güvenilir bir ekim ve hasat '
                   'takvimi dayanak alınan kaynaklarda yoktur.',
            yetisme='Kew POWO’ya göre doğal yayılışı Meksika’dan Guatemala’ya '
                    'uzanır; tek yıllıktır ve çoğunlukla subtropikal kuşakta '
                    'yetişir. EFSA’ya göre AB’ye gelen tohum Güney ve Orta '
                    'Amerika, Afrika ve Avustralya’daki üretici ülkelerden '
                    'ithal edilir.',
            yoresel='Türkçede yerleşik bir yöresel adı yok.',
        ),
        kaynak=[
            ['Salvia hispanica L., Plants of the World Online, Royal Botanic '
             'Gardens, Kew',
             POWO + '456385-1'],
            ['J. P. Cahill, “Ethnobotany of chia, Salvia hispanica L. '
             '(Lamiaceae)”, Economic Botany 57(4): 604–618, 2003',
             'https://link.springer.com/article/10.1663/0013-0001(2003)057%5b0604:EOCSHL%5d2.0.CO;2'],
            ['EFSA NDA Panel (D. Turck ve ark.), “Safety of chia seeds '
             '(Salvia hispanica L.) as a novel food for extended uses '
             'pursuant to Regulation (EU) 2015/2283”, EFSA Journal, 2019',
             'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7009096/'],
            ['S. L. Teoh, N. M. Lai, P. Vanichkulpitak, V. Vuksan, H. Ho, '
             'N. Chaiyakunapruk, “Clinical evidence on dietary '
             'supplementation with chia seed (Salvia hispanica L.): a '
             'systematic review and meta-analysis”, Nutrition Reviews '
             '76(4): 219–242, 2018',
             'https://pubmed.ncbi.nlm.nih.gov/29452425/'],
            ['F. TaghipourSheshdeh, M. Behzadi, S. Bashiri, '
             'M. Mohammadi-Sartang, “The Effect of Chia Seed on Blood '
             'Pressure, Body Composition, and Glycemic Control: A '
             'GRADE-Assessed Systematic Review and Dose-Response '
             'Meta-Analysis of Randomized Controlled Trials”, Nutrition '
             'Reviews 83(3): 448–465, 2025',
             'https://pubmed.ncbi.nlm.nih.gov/39225983/'],
        ],
        rel=['keten', 'kiwicha', 'kinoa', 'adacayi'],
        en=dict(
            name='Chia',
            other='Chia seed; Spanish chía; English chia, chia seed. Kew POWO '
                  'gives the name as accepted and lists no synonyms. The part '
                  'used is the seed. In the European Union it has been '
                  'assessed not as a herbal medicine but as a "novel food" '
                  '(EFSA).',
            part='Seed (whole or ground)',
            uses=[
                ['Mesoamerica — a staple food and medicinal plant',
                 'An ethnobotanical review published in Economic Botany in '
                 '2003 describes chia as an important staple food and '
                 'medicinal plant of pre-Columbian Mesoamerica. The same '
                 'review notes that the plant has been studied far less than '
                 'amaranth and the chenopods. The author compared the records '
                 'in sixteenth-century Mexican codices with later '
                 'publications.'],
                ['Mexico and Guatemala — use that shifted after the colonial '
                 'period',
                 'According to the same review, after Spanish colonisation '
                 'there were small but traceable shifts in the medicinal, '
                 'culinary, artistic and religious uses of chia. The author '
                 'tested this change through fieldwork in western Mexico and '
                 'the Guatemalan highlands. The review concludes that the '
                 'decline of ethnobotanical knowledge and the loss of habitat '
                 'have weakened both the seed resources and the knowledge '
                 'about the plant.'],
                ['European Union — authorised as a "novel food"',
                 'According to EFSA’s 2019 opinion, chia seed was first '
                 'authorised for the EU market in 2009, for bread products '
                 'only; that assessment considered a level of 5% in bread. In '
                 'later years the authorisation was extended to categories '
                 'such as baked products, breakfast cereals, fruit, nut and '
                 'seed mixes, fruit juices, yoghurt and pre-packaged seed. '
                 'EFSA also records that the seed has a history of consumption '
                 'in Latin America going back hundreds of years.'],
                ['Today — consumed as a supplement',
                 'A systematic review published in Nutrition Reviews in 2018 '
                 'writes that chia seed is now a popular dietary supplement, '
                 'taken mainly for its content of alpha-linolenic acid, '
                 'vegetable protein and dietary fibre. The same review also '
                 'states that information on its clinical effects is lacking.'],
            ],
            prep='No official monograph sets an accepted dose; chia is a '
                 'food. The EFSA opinion describes the seed being added, '
                 'whole or ground, to bread, yoghurt, fruit juices and cereal '
                 'mixes. The table of EU history of use in the same opinion '
                 'gives **15 g a day** for the seed sold on its own. EFSA drew '
                 'attention to a study showing increased acrylamide formation '
                 'in biscuits made with chia flour and baked at 190 °C, and '
                 'left products cooked at high heat for separate assessment.',
            science='The 2018 systematic review and meta-analysis in '
                    'Nutrition Reviews examined 12 randomised controlled '
                    'trials; participants were healthy people, athletes, '
                    'people with diabetes and people with metabolic syndrome. '
                    'The pooled results showed no significant difference; '
                    'only in subgroup analyses at higher doses were there a '
                    'fall in blood glucose after meals, a 0.10 mmol/L '
                    'reduction in HDL and a 7.14 mmHg fall in diastolic blood '
                    'pressure. The authors rated **the quality of all the '
                    'evidence as low or very low** and stressed that the '
                    'trials measured surrogate markers only. A meta-analysis '
                    'of 8 trials published in the same journal in 2025 '
                    'reported a fall of 7.19 mmHg in systolic and 6.04 mmHg '
                    'in diastolic blood pressure; it found no significant '
                    'effect on body weight, waist circumference, fasting '
                    'blood glucose or HbA1c. That review also notes that the '
                    'data are limited. None of these sources includes a trial '
                    'measuring clinical outcomes such as heart disease or '
                    'death.',
            safety='In its 2019 opinion EFSA found chia seed safe under the '
                   'assessed conditions of use; in a 76-person trial giving '
                   '50 g a day for 12 weeks no adverse event related to the '
                   'seed was reported. The one hazard EFSA identified is '
                   '**allergy**: two case reports describe itching in the '
                   'mouth, generalised hives, facial swelling, shortness of '
                   'breath and hand eczema. Cross-reactivity with the sera of '
                   'people allergic to peanut and sesame has also been '
                   'recorded; people with those allergies should be careful. '
                   'The sources relied on here contain no separate assessment '
                   'for pregnancy, breastfeeding or children; there are no '
                   'data for use above food amounts. Because meta-analyses '
                   'report a fall in blood pressure, people taking blood '
                   'pressure medicines would do well to tell their doctor '
                   'about regular, high intake; there is no interaction study '
                   'on this.',
            fact='Eaten in Latin America for hundreds of years, this seed '
                 'counts as a "novel food" in European Union law. According '
                 'to EFSA, the first authorisation for the EU market came in '
                 '2009 and only for bread products.',
            season='The EFSA opinion describes the plant as a summer annual '
                   'herb. The sources relied on here give no reliable sowing '
                   'and harvest calendar for Türkiye.',
            habitat='According to Kew POWO its native range runs from Mexico '
                    'to Guatemala; it is an annual and grows mainly in the '
                    'subtropical zone. According to EFSA, the seed reaching '
                    'the EU is imported from producing countries in South and '
                    'Central America, Africa and Australia.',
            local='It has no established local name in Turkish.',
        ),
    ),

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='amerikankasidesi',
        foto='',
        tr='Amerikan kasidesi',
        la='Scutellaria lateriflora L.',
        taxon='Scutellaria lateriflora',
        fam='Lamiaceae (ballıbabagiller)',
        diger='İngilizce American skullcap, blue skullcap, mad-dog skullcap. '
              'Cins ilk kez Tournefort tarafından 1716’da Cassida adıyla '
              'adlandırılmış, sonra Scutellaria adını almıştır. Kullanılan '
              'kısım kurutulmuş yaprak ve gövdelerdir. Çin tıbbının Baykal '
              'takkesi (Scutellaria baicalensis) ayrı bir türdür.',
        bolge=['kamerika'],
        kat=['sifa'],
        kisim='Kurutulmuş toprak üstü kısımları (yaprak ve gövde)',
        kul=[
            ['Çeroki ve İrokua — kadın sağlığı ve boğaz şikâyetleri',
             'Journal of Medicinally Active Plants’ta yayımlanan derleme, '
             'Çerokilerin bitkinin demlemesini ya da kaynatmasını meme '
             'ağrısı için, doğumdan sonra plasentanın atılması için ve adet '
             'söktürücü olarak kullandığını aktarır. Aynı derlemeye göre '
             'İrokualar kökten hazırladıkları karışımı çiçek hastalığından '
             'korunmak ve boğaz rahatsızlıkları için kullanmıştır. Bu '
             'kullanımlar yalnızca gelenekseldir; hiçbiri klinik olarak '
             'sınanmamıştır.'],
            ['Kuzey Amerika — hafif yatıştırıcı',
             'Derleme, bitkinin yaklaşık 200 yıldır hafif bir yatıştırıcı '
             'olarak kullanıldığını yazar. LiverTox, kurutulmuş yaprak ve '
             'gövdelerin bitkisel ilaç ve çay olarak kaygı, stres ve '
             'uykusuzluk için kullanıldığını belirtir. Phytomedicine’de '
             '2003’te yayımlanan çalışma da bitkiyi geleneksel bir '
             'yatıştırıcı ve kaygı gibi sinirsel rahatsızlıkların ilacı '
             'olarak tanımlar.'],
            ['Tıp tarihi — kuduz iddiası',
             'Derlemeye göre bitkinin tıp literatüründeki ilk anılışı köpek '
             'kuduzuna karşı kullanımıdır ve "mad-dog" (kuduz köpek) adı '
             'buradan gelir. Aynı derleme bu iddianın sonradan çürütüldüğünü '
             'belirtir.'],
            ['Günümüz — takviye pazarı',
             'Bitki bugün çay, kapsül, özüt, tentür ve granül biçiminde '
             'satılır. Derleme, dünya hasadının 1997’de yaklaşık 6.364 kg '
             'iken 2001’de 15.910 kg’a çıktığını aktarır. Aynı kaynak, '
             'piyasadaki ürünlerin başka türlerle karıştırılması sorununa '
             'dikkat çeker.'],
        ],
        haz='EMA, DSÖ ya da TİTCK monografı bulunamadı; kabul edilmiş bir '
            'doz yoktur. Derlemeye göre bitki çay, kapsül, özüt ve tentür '
            'olarak hazırlanır; tentürlerde kullanılan %40–60 etanol '
            'flavonoitlerin yaklaşık %70’ini özütler. Klinik çalışmalarda '
            'kullanılan miktarlar birer araştırma dozudur, öneri değildir: '
            '2014 tarihli çalışmada günde üç kez 350 mg, 2025 tarihli '
            'çalışmada günde 400 mg özüt temelli takviye verilmiştir. '
            '**Ürünün gerçekten bu türü içerdiği etiketten anlaşılamaz**; '
            'karıştırma sorunu aşağıda anlatılmıştır.',
        bilim='Phytomedicine’deki 2003 tarihli hayvan çalışmasında ağızdan '
              'verilen özüt sıçanlarda açık alan ve yükseltilmiş artı '
              'labirent testlerinde kaygıyı azaltan davranış değişiklikleri '
              'yapmıştır. Aynı çalışma %50 etanol özütünde 40 mg/g baikalin, '
              '%95 etanol özütünde 33 mg/g baikalein ölçmüş ve bu '
              'flavonoitlerin GABA-A reseptörünün benzodiazepin bölgesine '
              'bağlandığının bilindiğini hatırlatmıştır. İnsanda kanıt azdır. '
              '2003 tarihli çift kör, plasebo kontrollü bir çalışma sağlıklı '
              'gönüllülerde kaygı azaltıcı etki bildirmiştir. 2014’te '
              'Phytotherapy Research’te yayımlanan çapraz çalışmada 43 '
              'sağlıklı gönüllüde **kaygı ölçeğinde plasebodan anlamlı fark '
              'bulunmamış** (p = 0,191), yalnızca genel duygudurum puanı '
              'iyileşmiştir; yazarlar taşma etkisini ve katılımcıların zaten '
              'az kaygılı olmasını sınırlılık olarak sayar. 2025’te '
              'Nutrients’ta yayımlanan 66 kişilik çapraz çalışmada 56 gün '
              'süren kullanım, hafif-orta birincil uykusuzlukta uyku kalitesi '
              'puanını anlamlı biçimde iyileştirmiştir. Çalışmalar küçük ve '
              'kısa sürelidir.',
        kanit='sinirli',
        guv='orta',
        guvNot='⚠️ ABD Ulusal Sağlık Enstitüleri’nin LiverTox veri tabanı, '
               'bu bitkinin **klinik olarak belirgin karaciğer hasarı** '
               'olgularıyla ilişkilendirildiğini, ancak bunların çoğunda '
               'başka bitkilerle birlikte kullanıldığını yazar. Phytochemical '
               'Analysis’teki 2009 tarihli çalışmaya göre ürünler zaman zaman '
               'karaciğere zarar verebilen diterpenler içeren **Teucrium '
               '(germander) türleriyle karıştırılmıştır**. Karaciğer hastalığı '
               'olanlar kullanmamalıdır; kullanım sırasında sarılık, koyu '
               'idrar, bulantı ya da halsizlik olursa ürün bırakılıp hekime '
               'başvurulmalıdır. Gebelik, emzirme ve çocuklar için güvenlik '
               'verisi yoktur; geleneksel kayıtlarda adet söktürücü olarak '
               'geçtiği için gebelikte kullanılmamalıdır. Yatıştırıcı ilaç '
               'kullananlar hekimine danışmalıdır. 2025 tarihli çalışmada 56 '
               'günlük kullanımda istenmeyen etki bildirilmemiştir.',
        etk=[
            ['Yatıştırıcılar, uyku ilaçları ve benzodiazepinler (kuramsal)',
             'Bitkideki baikalin ve baikaleinin GABA-A reseptörünün '
             'benzodiazepin bölgesine bağlandığı bilinir (Phytomedicine, '
             '2003). Aynı yönde etki eden ilaçlarla birlikte uyuşukluk '
             'artabilir; insanda yapılmış bir etkileşim çalışması yoktur.'],
            ['Karaciğere yük bindiren ilaçlar ve başka bitkisel ürünler',
             'LiverTox’a göre bildirilen karaciğer hasarı olgularının çoğu '
             'bitkinin başka bitkilerle birlikte alındığı ürünlerdedir. '
             'Karaciğeri etkileyen ilaç kullananlar bu bitkiyi hekimine '
             'sormadan kullanmamalıdır.'],
        ],
        ilginc='İngilizcedeki "mad-dog skullcap" adı, bitkinin tıp '
               'literatürüne köpek kuduzuna karşı bir ilaç olarak girmesinden '
               'kalmıştır. Journal of Medicinally Active Plants’taki derleme '
               'bu iddianın sonradan çürütüldüğünü yazar; ad ise kalmıştır.',
        ek=dict(
            mevsim='Mavi çiçeklerinin taç yaprağı 6–8 mm boyundadır. Dayanak '
                   'alınan kaynaklar çiçeklenme ve toplama zamanı için bir '
                   'takvim vermez.',
            yetisme='Derlemeye göre bir sulak alan bitkisidir; dere '
                    'kıyılarında, bataklıklarda, ıslak çayırlarda ve nemli '
                    'ormanlık alanlarda yetişir. Kuzey Amerika’nın büyük '
                    'bölümünde, Kanada’dan Florida’ya, batıda Britanya '
                    'Kolumbiyası, Oregon ve New Mexico’ya kadar bulunur. '
                    'Türkiye’de doğal yayılışı yoktur.',
            yoresel='Türkçede yerleşik bir yöresel adı yok.',
            karisma='⚠️ Teucrium türleri (Teucrium canadense ve Teucrium '
                    'chamaedrys) görünüşçe bu bitkiye benzer ve ticari '
                    'ürünlere karışmıştır. 2009 tarihli çalışma, iki cinsin '
                    'fenolik bileşik profilleriyle ayırt edilebildiğini ve '
                    'kütle spektrometrisiyle %1 oranındaki karışımın bile '
                    'ölçülebildiğini göstermiştir. Baykal takkesi '
                    '(Scutellaria baicalensis) ayrı bir türdür ve bu sitede '
                    'ayrı kaydı vardır.',
        ),
        kaynak=[
            ['S. H. Sherman, N. Joshee, “Current status of research on the '
             'medicinal plant American skullcap (Scutellaria lateriflora): A '
             'review”, Journal of Medicinally Active Plants, University of '
             'Massachusetts Amherst ScholarWorks (dergiye geliş: 23 Mart 2022)',
             'https://scholarworks.umass.edu/server/api/core/bitstreams/3e9477b9-1bf6-4b3f-94e5-cc165a966201/content'],
            ['“Skullcap”, LiverTox: Clinical and Research Information on '
             'Drug-Induced Liver Injury, National Institute of Diabetes and '
             'Digestive and Kidney Diseases (güncelleme: 28 Mart 2020)',
             'https://www.ncbi.nlm.nih.gov/books/NBK548757/'],
            ['R. Awad, J. T. Arnason, V. Trudeau, C. Bergeron, '
             'J. W. Budzinski, B. C. Foster, Z. Merali, “Phytochemical and '
             'biological analysis of skullcap (Scutellaria lateriflora L.): a '
             'medicinal plant with anxiolytic properties”, Phytomedicine '
             '10(8): 640–649, 2003',
             'https://pubmed.ncbi.nlm.nih.gov/14692724/'],
            ['P. Wolfson, D. L. Hoffmann, “An investigation into the efficacy '
             'of Scutellaria lateriflora in healthy volunteers”, Alternative '
             'Therapies in Health and Medicine 9(2): 74–78, 2003',
             'https://pubmed.ncbi.nlm.nih.gov/12652886/'],
            ['C. Brock, J. Whitehouse, I. Tewfik, T. Towell, “American '
             'Skullcap (Scutellaria lateriflora): a randomised, double-blind '
             'placebo-controlled crossover study of its effects on mood in '
             'healthy volunteers”, Phytotherapy Research 28(5): 692–698, 2014',
             'https://pubmed.ncbi.nlm.nih.gov/23878109/'],
            ['A. Di Minno ve ark., “Efficacy and Tolerability of a Chemically '
             'Characterized Scutellaria lateriflora L. Extract-Based Food '
             'Supplement for Sleep Management: A Single-Center, Controlled, '
             'Randomized, Crossover, Double-Blind Clinical Trial”, Nutrients '
             '17(9): 1491, 2025',
             'https://pubmed.ncbi.nlm.nih.gov/40362800/'],
            ['L. Z. Lin, J. M. Harnly, R. Upton, “Comparison of the phenolic '
             'component profiles of skullcap (Scutellaria lateriflora) and '
             'germander (Teucrium canadense and T. chamaedrys), a potentially '
             'hepatotoxic adulterant”, Phytochemical Analysis 20(4): 298–306, '
             '2009',
             'https://pubmed.ncbi.nlm.nih.gov/19402188/'],
        ],
        rel=['baykaltakkesi', 'kediotu', 'pasiflora', 'melisa'],
        en=dict(
            name='American skullcap',
            other='English American skullcap, blue skullcap, mad-dog '
                  'skullcap. The genus was first named Cassida by Tournefort '
                  'in 1716 and later took the name Scutellaria. The part used '
                  'is the dried leaves and stems. The Baikal skullcap of '
                  'Chinese medicine (Scutellaria baicalensis) is a different '
                  'species.',
            part='Dried aerial parts (leaves and stems)',
            uses=[
                ['Cherokee and Iroquois — women’s health and throat '
                 'complaints',
                 'A review published in the Journal of Medicinally Active '
                 'Plants reports that the Cherokee used an infusion or '
                 'decoction of the plant for breast pain, to expel the '
                 'afterbirth and to bring on menstruation. According to the '
                 'same review, the Iroquois used a preparation of the root to '
                 'prevent smallpox and for throat ailments. These uses are '
                 'traditional only; none has been tested clinically.'],
                ['North America — a mild sedative',
                 'The review writes that the plant has been used as a mild '
                 'sedative for about 200 years. LiverTox states that the '
                 'dried leaves and stems are used as a herbal medicine and as '
                 'tea for anxiety, stress and insomnia. A study published in '
                 'Phytomedicine in 2003 likewise describes the plant as a '
                 'traditional sedative and a remedy for nervous disorders '
                 'such as anxiety.'],
                ['Medical history — the rabies claim',
                 'According to the review, the plant’s first mention in the '
                 'medical literature was its use against canine rabies, and '
                 'the name "mad-dog" comes from this. The same review notes '
                 'that the claim was later disproven.'],
                ['Today — the supplement market',
                 'The plant is now sold as tea, capsules, extracts, tinctures '
                 'and granules. The review reports that the world harvest '
                 'rose from about 6,364 kg in 1997 to 15,910 kg in 2001. The '
                 'same source draws attention to the problem of products on '
                 'the market being adulterated with other species.'],
            ],
            prep='No EMA, WHO or Turkish (TİTCK) monograph could be found; '
                 'there is no accepted dose. According to the review the '
                 'plant is prepared as tea, capsules, extracts and tinctures; '
                 'the 40–60% ethanol used in tinctures extracts about 70% of '
                 'the flavonoids. The amounts used in clinical trials are '
                 'research doses, not recommendations: the 2014 trial gave '
                 '350 mg three times a day, the 2025 trial 400 mg a day of an '
                 'extract-based supplement. **The label cannot show that a '
                 'product really contains this species**; the adulteration '
                 'problem is described below.',
            science='In the 2003 animal study in Phytomedicine, an extract '
                    'given by mouth produced behavioural changes in rats '
                    'that indicate reduced anxiety in the open-field and '
                    'elevated plus-maze tests. The same study measured '
                    '40 mg/g of baicalin in a 50% ethanol extract and 33 mg/g '
                    'of baicalein in a 95% ethanol extract, and recalled that '
                    'these flavonoids are known to bind to the benzodiazepine '
                    'site of the GABA-A receptor. Evidence in humans is thin. '
                    'A double-blind, placebo-controlled study from 2003 '
                    'reported an anxiety-reducing effect in healthy '
                    'volunteers. In a crossover trial published in '
                    'Phytotherapy Research in 2014, in 43 healthy volunteers '
                    '**no significant difference from placebo was found on '
                    'the anxiety scale** (p = 0.191); only the overall mood '
                    'score improved, and the authors list a carryover effect '
                    'and the participants’ already low anxiety as '
                    'limitations. In a 66-person crossover trial published in '
                    'Nutrients in 2025, 56 days of use significantly improved '
                    'the sleep quality score in mild to moderate primary '
                    'insomnia. The trials are small and short.',
            safety='⚠️ LiverTox, the database of the US National Institutes '
                   'of Health, writes that this plant has been linked to '
                   'cases of **clinically apparent liver injury**, though in '
                   'most of them it was used together with other botanicals. '
                   'According to the 2009 study in Phytochemical Analysis, '
                   'products have occasionally been **adulterated with '
                   'germander (Teucrium) species**, which contain diterpenes '
                   'that can harm the liver. People with liver disease should '
                   'not use it; if jaundice, dark urine, nausea or weakness '
                   'appear during use, the product should be stopped and a '
                   'doctor consulted. There are no safety data for pregnancy, '
                   'breastfeeding or children; because traditional records '
                   'list it as a means of bringing on menstruation, it should '
                   'not be used in pregnancy. People taking sedative '
                   'medicines should consult their doctor. In the 2025 trial '
                   'no adverse effect was reported over 56 days of use.',
            fact='The English name "mad-dog skullcap" survives from the '
                 'plant’s entry into the medical literature as a remedy '
                 'against canine rabies. The review in the Journal of '
                 'Medicinally Active Plants writes that the claim was later '
                 'disproven; the name stayed.',
            season='The corolla of its blue flowers is 6–8 mm long. The '
                   'sources relied on here give no calendar for flowering or '
                   'gathering.',
            habitat='According to the review it is a wetland plant; it grows '
                    'on stream banks, in marshes, in wet meadows and in moist '
                    'wooded areas. It occurs across most of North America, '
                    'from Canada to Florida and west to British Columbia, '
                    'Oregon and New Mexico. It is not native to Türkiye.',
            local='It has no established local name in Turkish.',
            confusion='⚠️ Germander species (Teucrium canadense and Teucrium '
                      'chamaedrys) look similar to this plant and have found '
                      'their way into commercial products. The 2009 study '
                      'showed that the two genera can be told apart by their '
                      'phenolic profiles and that even a 1% admixture can be '
                      'measured by mass spectrometry. Baikal skullcap '
                      '(Scutellaria baicalensis) is a different species and '
                      'has its own record on this site.',
        ),
        etk_en=[
            ['Sedatives, sleep medicines and benzodiazepines (theoretical)',
             'The baicalin and baicalein in the plant are known to bind to '
             'the benzodiazepine site of the GABA-A receptor (Phytomedicine, '
             '2003). Drowsiness may increase with medicines acting in the '
             'same direction; no interaction study has been done in humans.'],
            ['Medicines that burden the liver and other herbal products',
             'According to LiverTox, most of the reported cases of liver '
             'injury involved products in which the plant was taken together '
             'with other botanicals. People taking medicines that affect the '
             'liver should not use this plant without asking their doctor.'],
        ],
    ),

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='ananaspapatyasi',
        foto='',
        tr='Ananas papatyası',
        la='Matricaria discoidea DC.',
        taxon='Matricaria discoidea',
        fam='Asteraceae (papatyagiller)',
        diger='İngilizce pineapple weed, rayless chamomile. Kew POWO’daki eş '
              'adları arasında Chamomilla suaveolens (Pursh) Rydb. ve '
              'Matricaria suaveolens (Pursh) Buchenau vardır; bazı floralarda '
              'Matricaria matricarioides adıyla geçer. "Ananas papatyası" '
              'İngilizce adın çevirisidir. Kullanılan kısım çiçekli toprak '
              'üstü kısımlarıdır.',
        bolge=['kamerika', 'avrupa'],
        kat=['sifa'],
        kisim='Çiçekli toprak üstü kısımları',
        kul=[
            ['Kuzey Amerika yerlileri — böcek kovucu ve koku',
             'PLoS One’da 2018’de yayımlanan çalışma, bitkinin Karaayak '
             '(Blackfoot) halkı ve Kuzey Amerika’nın başka yerli '
             'toplulukları tarafından böcek kovucu olarak kullanıldığının '
             'belgelendiğini yazar. Aynı çalışmaya göre çeşitli yerli halklar '
             'bitkiyi tıbbi amaçla ve güzel koku olarak da kullanmıştır. '
             'Native Plant Trust’ın flora sayfası da bitkiyi yerlilerin '
             'kullandığı tıbbi ve aromatik bir bitki olarak anar.'],
            ['Estonya — halk hekimliğinin en çok anılan bitkilerinden',
             'Plants dergisinde 2022’de yayımlanan çalışma, Estonya’nın '
             'güneydoğusundaki üç bölgeye ait 1888–1996 arası halkbilim '
             'kayıtlarını incelemiştir. Bu kayıtlarda ananas papatyası 51 '
             'kullanım bildirimiyle sarıçamdan (57) sonra en sık anılan '
             'ikinci şifalı bitkidir. Kuzey Amerika kökenli bir yol kenarı '
             'otunun Avrupa’da halk ilacına dönüşmesinin örneğidir.'],
            ['Avrupa — papatyanın yerine',
             'Biomolecules’ta 2024’te yayımlanan çalışmaya göre bitkinin '
             'halk hekimliğindeki geçmişi 19. yüzyıla uzanır; çoğunlukla çay '
             'ya da tentür olarak, iltihap giderici ve kramp çözücü diye '
             'kullanılmıştır. Aynı çalışma, SSCB farmakopesinin ananas '
             'papatyasını tıbbi papatya çiçeğine ek ham madde olarak, '
             'yalnızca haricen kullanım için onayladığını aktarır.'],
        ],
        haz='EMA, DSÖ ya da TİTCK monografı bulunamadı; kabul edilmiş bir '
            'doz yoktur. Biomolecules’taki 2024 tarihli çalışma, halk '
            'kullanımında bitkinin çay ya da tentür olarak hazırlandığını '
            'yazar. Aynı çalışmada toprak üstü kısımlar temmuzda, çiçeklenme '
            'döneminde toplanmış ve oda sıcaklığında, havadar bir yerde bir '
            'hafta kurutulmuştur. EMA’nın papatya çiçeği monografındaki '
            'dozlar yalnızca tıbbi papatya içindir; **bu türe aktarılamaz**.',
        bilim='Bu bitkiyle insanda yapılmış bir klinik çalışma dayanak '
              'alınan kaynaklarda yoktur; kanıt laboratuvar ve hayvan '
              'düzeyindedir. Biomolecules’taki 2024 tarihli çalışma kuru '
              'özütlerde 16 fenolik bileşik, uçucu yağda 9 ana terpenoit '
              'saptamıştır. Aynı çalışmada 25, 50 ve 100 mg/kg dozlarında '
              'verilen özütler farelerde ağrı kesici etki göstermiş, '
              'sıçanlarda uykuyu iyileştirmiştir; hücre testlerinde kuru '
              'özütler toksik bulunmamıştır. Phytochemical Analysis’teki 2007 '
              'tarihli çalışma çiçeklerde bol miktarda spiroeter izomeri, '
              'yapraklarda ise en yüksek düzeyde herniarin (bir kumarin) '
              'ölçmüştür. PLoS One’daki 2018 tarihli çalışmada bitkinin uçucu '
              'yağı ve bileşenlerinden alfa-terpineol, laboratuvar düzeneğinde '
              'Aedes aegypti sivrisineğinin ısırmasını caydırmıştır; yazarlar '
              'bunun geleneksel böcek kovucu kullanımı desteklediğini yazar. '
              'Bu bulguların hiçbiri **insanda sınanmamıştır**.',
        kanit='sinirli',
        guv='dusuk',
        guvNot='İnsanda yapılmış bir güvenlik çalışması yoktur; 2024 tarihli '
               'çalışmada kuru özütler hücre testlerinde ve hayvan '
               'deneylerinde toksik bulunmamıştır. Bitki papatyagiller '
               'familyasındandır. EMA’nın tıbbi papatya monografı, '
               'papatyagillere aşırı duyarlılığı olanlarda kullanımı '
               'kontrendike sayar; bu uyarı yakın akraba olan bu tür için de '
               'akılda tutulmalıdır. **Papatya, pelin ya da başka '
               'papatyagillere alerjisi olanlar kullanmamalıdır.** Gebelik, '
               'emzirme ve çocuklar için veri yoktur; bu dönemlerde '
               'kullanılması için dayanak bulunmaz. Yol kenarından ve '
               'ilaçlanmış alanlardan toplanan bitki kullanılmamalıdır. '
               'Bilinen bir ilaç etkileşimi çalışması yoktur; düzenli ilaç '
               'kullananlar hekimine danışmalıdır.',
        ilginc='Estonya’nın güneydoğusuna ait 1888–1996 arası halkbilim '
               'kayıtlarında, Kuzey Amerika kökenli bu yabancı ot, sarıçamdan '
               'sonra en çok anılan ikinci şifalı bitkidir (Plants, 2022). '
               'Tür adı discoidea, çiçek başında dil biçimli beyaz çiçeklerin '
               'bulunmayıp yalnızca disk çiçeklerinin olmasını anlatır.',
        ek=dict(
            mevsim='Biomolecules’taki 2024 tarihli çalışmada bitki Estonya’da '
                   'temmuz ayında, çiçeklenme döneminde toplanmıştır. Türkiye '
                   'için dayanak alınan kaynaklarda bir takvim yoktur.',
            yetisme='Kew POWO’ya göre tek yıllıktır; doğal yayılışı Kuzey '
                    'Amerika’nın kutup altı bölgelerinden ABD’ye uzanır. '
                    'Native Plant Trust’a göre Kuzey Amerika’nın '
                    'kuzeybatısından doğuya ve Avrupa’ya yayılmıştır; yol '
                    'kenarlarında, avlularda ve bozulmuş topraklarda yetişir. '
                    '2019 tarihli bir revizyon, Türkiye florasında tanınan '
                    'dört Matricaria taksonu arasında bu türü Matricaria '
                    'matricarioides adıyla sayar.',
            yoresel='Türkçede yerleşik bir yöresel adı yok.',
            karisma='Tıbbi papatya (Matricaria chamomilla, eş adı Matricaria '
                    'recutita) ile karıştırılabilir. Native Plant Trust’a '
                    'göre ananas papatyasının çiçek başında yalnızca disk '
                    'çiçekleri vardır, dil biçimli çiçek yoktur; tıbbi '
                    'papatyadan bu özelliğiyle ayrılır. EMA monografı '
                    'yalnızca tıbbi papatyayı kapsar.',
        ),
        kaynak=[
            ['Matricaria discoidea DC., Plants of the World Online, Royal '
             'Botanic Gardens, Kew',
             POWO + '154716-2'],
            ['J. Sepp, O. Koshovyi, V. Jakštas ve ark., “Phytochemical, '
             'Pharmacological, and Molecular Docking Study of Dry Extracts of '
             'Matricaria discoidea DC. with Analgesic and Soporific '
             'Activities”, Biomolecules 14(3): 361, 2024',
             'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10968509/'],
            ['C. L. Cantrell, A. Ali, A. M. P. Jones, “Isolation and '
             'identification of mosquito biting deterrents from the North '
             'American mosquito repelling folk remedy plant, Matricaria '
             'discoidea DC.”, PLoS One 13(10): e0206594, 2018',
             'https://pubmed.ncbi.nlm.nih.gov/30379955/'],
            ['R. Sõukand, R. Kalle, “The Appeal of Ethnobotanical Folklore '
             'Records: Medicinal Plant Use in Setomaa, Räpina and Vastseliina '
             'Parishes, Estonia (1888–1996)”, Plants (Basel) 11(20): 2698, '
             '2022',
             'https://pubmed.ncbi.nlm.nih.gov/36297723/'],
            ['C. M. Ma, L. Winsor, M. Daneshtalab, “Quantification of '
             'spiroether isomers and herniarin of different parts of '
             'Matricaria matricarioides and flowers of Chamaemelum nobile”, '
             'Phytochemical Analysis 18(1): 42–49, 2007',
             'https://pubmed.ncbi.nlm.nih.gov/17260697/'],
            ['H. Inceer, “The genus Matricaria L. (Asteraceae) in Turkey”, '
             'Biodiversity: Research and Conservation 54: 1–6, 2019',
             'https://pressto.amu.edu.pl/index.php/biorc/article/view/biorc-2019-0006'],
            ['Matricaria discoidea (rayless chamomile), Go Botany, Native '
             'Plant Trust',
             'https://gobotany.nativeplanttrust.org/species/matricaria/discoidea/'],
            ['European Union herbal monograph on Matricaria recutita L., '
             'flos, EMA/HMPC/55843/2011 (yakın tür; aşırı duyarlılık uyarısı '
             'için)',
             'https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-matricaria-recutita-l-flos-first-version_en.pdf'],
        ],
        rel=['papatya', 'romenpapatyasi', 'civanpercemi', 'pelin'],
        en=dict(
            name='Pineapple weed',
            other='English pineapple weed, rayless chamomile. The synonyms '
                  'in Kew POWO include Chamomilla suaveolens (Pursh) Rydb. '
                  'and Matricaria suaveolens (Pursh) Buchenau; some floras '
                  'list it as Matricaria matricarioides. The Turkish name '
                  '"ananas papatyası" is a translation of the English name. '
                  'The part used is the flowering aerial parts.',
            part='Flowering aerial parts',
            uses=[
                ['Native peoples of North America — insect repellent and '
                 'scent',
                 'A study published in PLoS One in 2018 writes that the use '
                 'of the plant as an insect repellent by the Blackfoot and '
                 'other indigenous groups of North America is documented. '
                 'According to the same study, various indigenous peoples '
                 'also used the plant medicinally and as a perfume. The flora '
                 'page of the Native Plant Trust likewise mentions it as a '
                 'medicinal and aromatic plant used by Native Americans.'],
                ['Estonia — among the most cited plants of folk medicine',
                 'A study published in the journal Plants in 2022 examined '
                 'folklore records from 1888 to 1996 for three districts in '
                 'south-eastern Estonia. In these records pineapple weed, '
                 'with 51 use reports, is the second most frequently '
                 'mentioned medicinal plant after Scots pine (57). It is an '
                 'example of a North American roadside weed turning into a '
                 'folk remedy in Europe.'],
                ['Europe — in place of chamomile',
                 'According to a study published in Biomolecules in 2024, '
                 'the plant’s history in folk medicine goes back to the 19th '
                 'century; it was used mostly as a tea or tincture, as an '
                 'anti-inflammatory and antispasmodic. The same study reports '
                 'that the USSR pharmacopoeia approved pineapple weed as an '
                 'additional raw material alongside chamomile flower, for '
                 'external use only.'],
            ],
            prep='No EMA, WHO or Turkish (TİTCK) monograph could be found; '
                 'there is no accepted dose. The 2024 study in Biomolecules '
                 'writes that in folk use the plant is prepared as a tea or '
                 'tincture. In the same study the aerial parts were gathered '
                 'in July, during flowering, and dried for a week at room '
                 'temperature in a well-ventilated place. The doses in the '
                 'EMA monograph on matricaria flower are for German chamomile '
                 'only; **they cannot be transferred to this species**.',
            science='The sources relied on here contain no clinical trial of '
                    'this plant in humans; the evidence is at the laboratory '
                    'and animal level. The 2024 study in Biomolecules '
                    'identified 16 phenolic compounds in the dry extracts and '
                    '9 main terpenoids in the essential oil. In the same '
                    'study, extracts given at doses of 25, 50 and 100 mg/kg '
                    'showed a pain-relieving effect in mice and improved '
                    'sleep in rats; in cell tests the dry extracts were not '
                    'found to be toxic. The 2007 study in Phytochemical '
                    'Analysis measured large amounts of spiroether isomers in '
                    'the flowers and the highest level of herniarin (a '
                    'coumarin) in the leaves. In the 2018 study in PLoS One, '
                    'the plant’s essential oil and, among its components, '
                    'alpha-terpineol deterred biting by the mosquito Aedes '
                    'aegypti in a laboratory set-up; the authors write that '
                    'this supports the traditional insect-repellent use. None '
                    'of these findings **has been tested in humans**.',
            safety='No safety study has been done in humans; in the 2024 '
                   'study the dry extracts were not found to be toxic in cell '
                   'tests or animal experiments. The plant belongs to the '
                   'daisy family. The EMA monograph on German chamomile '
                   'treats hypersensitivity to the daisy family as a '
                   'contraindication; that warning should be kept in mind for '
                   'this closely related species as well. **People allergic '
                   'to chamomile, wormwood or other members of the daisy '
                   'family should not use it.** There are no data for '
                   'pregnancy, breastfeeding or children; nothing supports '
                   'its use in these periods. Plants gathered from roadsides '
                   'and sprayed areas should not be used. No drug interaction '
                   'study is known; people on regular medication should '
                   'consult their doctor.',
            fact='In the folklore records of south-eastern Estonia from 1888 '
                 'to 1996, this weed of North American origin is the second '
                 'most cited medicinal plant after Scots pine (Plants, 2022). '
                 'The species name discoidea describes a flower head that has '
                 'no strap-shaped white florets, only disc florets.',
            season='In the 2024 study in Biomolecules the plant was gathered '
                   'in Estonia in July, during flowering. The sources relied '
                   'on here give no calendar for Türkiye.',
            habitat='According to Kew POWO it is an annual; its native range '
                    'runs from subarctic North America to the USA. According '
                    'to the Native Plant Trust it has spread from '
                    'north-western North America eastward and to Europe; it '
                    'grows on roadsides, in yards and on disturbed soil. A '
                    '2019 revision counts this species, under the name '
                    'Matricaria matricarioides, among the four Matricaria '
                    'taxa recognised in the flora of Türkiye.',
            local='It has no established local name in Turkish.',
            confusion='It can be confused with German chamomile (Matricaria '
                      'chamomilla, synonym Matricaria recutita). According to '
                      'the Native Plant Trust, the flower head of pineapple '
                      'weed has disc florets only and no strap-shaped '
                      'florets; this sets it apart from German chamomile. '
                      'The EMA monograph covers German chamomile only.',
        ),
    ),

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='aycicegi',
        foto='',
        tr='Ayçiçeği',
        la='Helianthus annuus L.',
        taxon='Helianthus annuus',
        fam='Asteraceae (papatyagiller)',
        diger='Günebakan, gündöndü (Trakya ve Marmara); tohumuna ay çekirdeği '
              'denir; İngilizce sunflower, '
              'common sunflower. Kullanılan kısım tohum (çekirdek) ve '
              'tohumdan elde edilen yağdır. Aynı cinsten yer elması '
              '(Helianthus tuberosus) ayrı bir türdür.',
        bolge=['kamerika', 'anadolu'],
        kat=['besin'],
        kisim='Tohum (çekirdek) ve tohum yağı; yağı alınmış küspesi hayvan yemi',
        kul=[
            ['Kuzey Amerika — yerli tarımın evcilleştirdiği bitki',
             'PNAS’ta 2006’da yayımlanan değerlendirme, ayçiçeğini '
             'Iva annua (İngilizce marshelder), kazayağı ve kabakla birlikte '
             'Amerika Birleşik Devletleri’nin doğusunda bağımsız olarak '
             'evcilleştirilen dört bitkiden biri sayar. Aynı yazı bu bölgeyi '
             'dünyanın bağımsız evcilleştirme merkezlerinden biri olarak '
             'doğrular. Ayçiçeği bugün yağ bitkisi olarak bütün dünyaya '
             'yayılmıştır.'],
            ['Halk hekimliği — kalp ve solunum yolu şikâyetleri',
             'Chemistry Central Journal’da 2017’de yayımlanan derleme, '
             'ayçiçeği tohumunun halk hekimliğinde kalp hastalığı ile '
             'bronş, gırtlak ve akciğer rahatsızlıkları gibi durumlarda '
             'kullanıldığını aktarır. Aynı derleme tohumun besin ve tıbbi '
             'değerinin bilindiğini ama yeterince araştırılmadığını yazar. '
             'Bu kullanımlar gelenekseldir; klinik olarak doğrulanmamıştır.'],
            ['Trakya ve Marmara — yağlık ve çerezlik',
             'Tarım ve Orman Bakanlığı Trakya Tarımsal Araştırma '
             'Enstitüsü’ne göre Türkiye’deki ayçiçeği ekim alanlarının %73’ü '
             'Trakya-Marmara bölgesindedir; bitki hem yağlık hem çerezlik '
             'olarak yetiştirilir. OCL dergisinde 2019’da yayımlanan yazı, '
             '2017’de yağlık ve çerezlik ayçiçeğinin toplam 779.622 hektarda '
             'ekildiğini ve 1.964.385 ton tohum alındığını bildirir. Aynı '
             'yazıya göre Ulusal Tohum Gen Bankası’nda 932 ayçiçeği örneği '
             'korunmaktadır.'],
            ['Tarım — küspe ve yem',
             'Enstitünün sayfasına göre yağı alındıktan sonra kalan küspe '
             '%44 protein içerir. Aynı kaynak ayçiçeği yağının oleik ve '
             'linoleik asit bakımından zengin olduğunu yazar.'],
        ],
        haz='Ayçiçeği bir gıdadır; resmî bir monografta kabul edilmiş bir '
            'doz yoktur. Tohum kavrulmuş ya da çiğ olarak çerez diye yenir, '
            'iç tohum ekmek ve salatalara katılır, tohumdan sıkılan yağ '
            'yemeklik yağ olarak kullanılır. Trakya Tarımsal Araştırma '
            'Enstitüsü’ne göre ekim bölgeye göre mart ile mayıs arasında '
            'yapılır ve bitki çiçeklenmeden 45–60 gün sonra hasat olgunluğuna '
            'gelir. **Kabuğuyla yutulan çekirdek** çocuklarda bağırsak '
            'tıkanmasına yol açabildiği için kabuk yenmez.',
        bilim='Chemistry Central Journal’daki 2017 tarihli derlemeye göre '
              'tohum %35–42 yağ içerir; yağın %55–70’i linoleik, %20–25’i '
              'oleik asittir. Aynı derleme tohumda 100 g’da 37,8 mg E '
              'vitamini bulunduğunu, bunun yer fıstığındaki 10,1 mg’dan '
              'yüksek olduğunu ve tohumun klorojenik asit gibi fenolik '
              'asitler ile flavonoitler taşıdığını yazar. Derlemede anılan '
              'antioksidan, antimikrobiyal, antidiyabetik ve iltihap giderici '
              'etkiler çoğunlukla laboratuvar ve hayvan çalışmalarına '
              'dayanır; yazarlar konunun **yeterince araştırılmadığını** '
              'belirtir. İnsan verisi yağ üzerinedir: 2026’da yayımlanan ve '
              '13 randomize kontrollü çalışmayı (771 katılımcı) kapsayan '
              'meta-analiz, ayçiçeği yağı ile kanola yağı arasında toplam '
              'kolesterol, LDL, HDL ve trigliserit açısından anlamlı fark '
              'bulmamıştır. Ayçiçeği tohumunun bir hastalığı tedavi ettiğini '
              'gösteren klinik çalışma bu kaynaklarda yoktur.',
        kanit='sinirli',
        guv='dusuk',
        guvNot='Gıda olarak yaygın biçimde tüketilir. Allergy dergisindeki '
               '2016 tarihli derleme, ayçiçeği tohumunun da aralarında '
               'bulunduğu yenebilir tohumlara karşı aşırı duyarlılık '
               'tepkilerinin **çoğu zaman şiddetli** olduğunu, yayınların '
               'ise daha çok olgu sunumlarından oluştuğunu yazar; alerjisi '
               'olanlar için tek yönetim tohumdan kaçınmaktır. ⚠️ Çocuklar '
               'için ayrı bir risk vardır: Journal of Pediatric Surgery’deki '
               '2007 tarihli çalışmada dışkı tıkanması olan çocuklarda '
               'saptanan 53 tohum bezoarının 3’ü ayçiçeği çekirdeğindendi ve '
               'çocukların çoğu genel anestezi altında tedavi edildi. Küçük '
               'çocuklara **kabuklu çekirdek verilmemelidir**. Gebelik ve '
               'emzirmede gıda miktarlarında tüketim için bir uyarı dayanak '
               'alınan kaynaklarda yoktur. Bilinen bir ilaç etkileşimi '
               'çalışması bulunamadı.',
        ilginc='Meksika’daki kazı alanlarında Kolomb öncesi ayçiçeği '
               'kalıntıları bulununca ikinci bir evcilleştirme merkezi '
               'önerilmişti. PNAS’ta 2011’de yayımlanan genetik çalışma, '
               'bugünkü kültür ayçiçeğinin Kuzey Amerika’nın doğusunda tek '
               'bir kez evcilleştirildiğini destekler.',
        ek=dict(
            mevsim='Trakya Tarımsal Araştırma Enstitüsü’ne göre Ege ve '
                   'Güneydoğu Anadolu’da martta, Marmara, Orta Anadolu ve '
                   'Karadeniz’de nisanda, Doğu Anadolu’da mayısta ekilir. '
                   'Hasat olgunluğuna çiçeklenmeden 45–60 gün sonra gelir.',
            yetisme='Kew POWO’ya göre tek yıllıktır; doğal yayılışı ABD’nin '
                    'güneybatısından Meksika’ya uzanır ve çoğunlukla ılıman '
                    'kuşakta yetişir. Türkiye’de tarla bitkisidir; ekim '
                    'alanlarının %73’ü Trakya-Marmara bölgesindedir. Ekim '
                    'için toprak sıcaklığının en az 8–10 °C olması istenir.',
            yoresel='Günebakan, gündöndü (Trakya ve Marmara Bölgesi; Trakya '
                    'Tarımsal Araştırma Enstitüsü).',
        ),
        kaynak=[
            ['Helianthus annuus L., Plants of the World Online, Royal '
             'Botanic Gardens, Kew',
             POWO + '119003-2'],
            ['S. Guo, Y. Ge, K. Na Jom, “A review of phytochemistry, '
             'metabolite changes, and medicinal uses of the common sunflower '
             'seed and sprouts (Helianthus annuus L.)”, Chemistry Central '
             'Journal 11(1): 95, 2017',
             'https://pubmed.ncbi.nlm.nih.gov/29086881/'],
            ['B. D. Smith, “Eastern North America as an independent center '
             'of plant domestication”, Proceedings of the National Academy of '
             'Sciences 103(33): 12223–12228, 2006',
             'https://pubmed.ncbi.nlm.nih.gov/16894156/'],
            ['B. K. Blackman, M. Scascitelli, N. C. Kane ve ark., “Sunflower '
             'domestication alleles support single domestication center in '
             'eastern North America”, Proceedings of the National Academy of '
             'Sciences 108(34): 14360–14365, 2011',
             'https://pubmed.ncbi.nlm.nih.gov/21844335/'],
            ['F. Vafa, M. Arab-Zozani, S. Jafari, S. Karbasi, F. Ghaderi, '
             'T. Kazemi, “Comparison of sunflower oil and canola oil '
             'consumption on serum lipid profile in adults: a systematic '
             'review and meta-analysis”, Journal of Health, Population and '
             'Nutrition 45(1): 249, 2026',
             'https://pubmed.ncbi.nlm.nih.gov/43015922/'],
            ['A. Patel, S. L. Bahna, “Hypersensitivities to sesame and other '
             'common edible seeds”, Allergy 71(10): 1405–1413, 2016',
             'https://pubmed.ncbi.nlm.nih.gov/27332789/'],
            ['A. Eitan, I. M. Katz, Y. Sweed, A. Bickel, “Fecal impaction in '
             'children: report of 53 cases of rectal seed bezoars”, Journal '
             'of Pediatric Surgery 42(6): 1114–1117, 2007',
             'https://pubmed.ncbi.nlm.nih.gov/17560231/'],
            ['S. Süzer, “Ekolojik Ayçiçeği Tarımı”, T.C. Tarım ve Orman '
             'Bakanlığı Trakya Tarımsal Araştırma Enstitüsü Müdürlüğü',
             'https://arastirma.tarimorman.gov.tr/ttae/Sayfalar/Detay.aspx?SayfaId=56'],
            ['A. S. Tan, Y. Kaya, “Sunflower (Helianthus annuus L.) genetic '
             'resources, production and researches in Turkey”, OCL: Oilseeds '
             'and Fats, Crops and Lipids 26, 2019 (Trakya Üniversitesi açık '
             'erişim arşivi)',
             'https://dspace.trakya.edu.tr/items/1cbab253-6ea7-4aa8-a943-be652fba5971/full'],
        ],
        rel=['yerelmasi', 'kabakcekirdegi', 'susam', 'aspir'],
        en=dict(
            name='Sunflower',
            other='Günebakan, gündöndü (Thrace and Marmara); its seed is '
                  'commonly called ay çekirdeği in Turkish; English '
                  'sunflower, common sunflower. The parts used are the seed '
                  'and the oil obtained from the seed. Jerusalem artichoke '
                  '(Helianthus tuberosus), of the same genus, is a different '
                  'species.',
            part='Seed and seed oil; the press cake left after the oil is '
                 'taken is animal feed',
            uses=[
                ['North America — a plant domesticated by indigenous farming',
                 'A synthesis published in PNAS in 2006 counts sunflower, '
                 'together with marshelder (Iva annua), chenopod and squash, '
                 'among the four plants domesticated independently in the '
                 'eastern United States. The same paper confirms this region '
                 'as one of the world’s independent centres of domestication. '
                 'Today sunflower has spread across the whole world as an oil '
                 'crop.'],
                ['Folk medicine — heart and respiratory complaints',
                 'A review published in Chemistry Central Journal in 2017 '
                 'reports that sunflower seed is used in folk medicine for '
                 'conditions such as heart disease and bronchial, laryngeal '
                 'and pulmonary complaints. The same review writes that the '
                 'nutritional and medical value of the seed is recognised but '
                 'under-researched. These uses are traditional; they have not '
                 'been confirmed clinically.'],
                ['Thrace and Marmara — for oil and as a snack',
                 'According to the Thrace Agricultural Research Institute of '
                 'the Ministry of Agriculture and Forestry, 73% of the '
                 'sunflower area of Türkiye is in the Thrace-Marmara region; '
                 'the plant is grown both for oil and for snack seed. A paper '
                 'published in the journal OCL in 2019 reports that in 2017 '
                 'oilseed and confectionery sunflower together were sown on '
                 '779,622 hectares and yielded 1,964,385 tonnes of seed. '
                 'According to the same paper, 932 sunflower accessions are '
                 'conserved in the National Seed Gene Bank.'],
                ['Farming — press cake and feed',
                 'According to the institute’s page, the cake left after the '
                 'oil is extracted contains 44% protein. The same source '
                 'writes that sunflower oil is rich in oleic and linoleic '
                 'acid.'],
            ],
            prep='Sunflower is a food; no official monograph sets an accepted '
                 'dose. The seed is eaten roasted or raw as a snack, the '
                 'kernel is added to bread and salads, and the oil pressed '
                 'from the seed is used as cooking oil. According to the '
                 'Thrace Agricultural Research Institute, sowing takes place '
                 'between March and May depending on the region, and the '
                 'plant reaches harvest maturity 45–60 days after flowering. '
                 'Because **seed swallowed with its shell** can cause bowel '
                 'blockage in children, the shell is not eaten.',
            science='According to the 2017 review in Chemistry Central '
                    'Journal, the seed contains 35–42% oil; 55–70% of the '
                    'oil is linoleic and 20–25% oleic acid. The same review '
                    'writes that the seed has 37.8 mg of vitamin E per 100 g, '
                    'higher than the 10.1 mg in peanut, and that it carries '
                    'phenolic acids such as chlorogenic acid as well as '
                    'flavonoids. The antioxidant, antimicrobial, antidiabetic '
                    'and anti-inflammatory effects cited in the review rest '
                    'mostly on laboratory and animal studies; the authors '
                    'note that the subject is **under-researched**. The human '
                    'data concern the oil: a meta-analysis published in 2026, '
                    'covering 13 randomised controlled trials (771 '
                    'participants), found no significant difference between '
                    'sunflower oil and canola oil in total cholesterol, LDL, '
                    'HDL or triglycerides. None of these sources contains a '
                    'clinical trial showing that sunflower seed treats a '
                    'disease.',
            safety='It is widely consumed as food. The 2016 review in the '
                   'journal Allergy writes that hypersensitivity reactions '
                   'to edible seeds, sunflower seed among them, are **often '
                   'severe**, while the publications are mostly case '
                   'reports; for people with the allergy the only management '
                   'is to avoid the seed. ⚠️ There is a separate risk for '
                   'children: in the 2007 study in the Journal of Pediatric '
                   'Surgery, 3 of the 53 seed bezoars found in children with '
                   'faecal impaction were of sunflower seeds, and most of the '
                   'children were treated under general anaesthesia. Small '
                   'children **should not be given seeds in the shell**. The '
                   'sources relied on here contain no warning about '
                   'consumption in food amounts in pregnancy and '
                   'breastfeeding. No drug interaction study could be found.',
            fact='When pre-Columbian sunflower remains were found at '
                 'excavation sites in Mexico, a second centre of '
                 'domestication was proposed. A genetic study published in '
                 'PNAS in 2011 supports a single domestication of today’s '
                 'cultivated sunflower, in eastern North America.',
            season='According to the Thrace Agricultural Research Institute '
                   'it is sown in March in the Aegean and south-eastern '
                   'Anatolia, in April in Marmara, central Anatolia and the '
                   'Black Sea region, and in May in eastern Anatolia. It '
                   'reaches harvest maturity 45–60 days after flowering.',
            habitat='According to Kew POWO it is an annual; its native range '
                    'runs from the south-western USA to Mexico and it grows '
                    'mainly in the temperate zone. In Türkiye it is a field '
                    'crop; 73% of the sown area is in the Thrace-Marmara '
                    'region. For sowing, a soil temperature of at least '
                    '8–10 °C is wanted.',
            local='Günebakan, gündöndü (Thrace and the Marmara Region; '
                  'Thrace Agricultural Research Institute).',
        ),
    ),

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='mahonya',
        foto='',
        tr='Mahonya',
        la='Berberis aquifolium Pursh',
        taxon='Berberis aquifolium',
        fam='Berberidaceae (karamukgiller)',
        diger='Eş adı Mahonia aquifolium (Pursh) Nutt.; Kew POWO bu adı '
              'Berberis aquifolium’un eş adı sayar, klinik yayınlar ise '
              'çoğunlukla Mahonia adını kullanır. İngilizce Oregon grape. '
              'Kullanılan kısım kök ve kökten hazırlanan özütlerdir; '
              'haricen krem ve merhem olarak uygulanır. Berberin içeren '
              'bitkilerdendir.',
        bolge=['kamerika'],
        kat=['sifa'],
        kisim='Kök; haricen kullanılan krem ve merhemlerde bitki özütü',
        kul=[
            ['Britanya Kolumbiyası — hayvan sağaltımında kök çayı',
             'Journal of Ethnobiology and Ethnomedicine’de 2007’de '
             'yayımlanan çalışma, Kanada’nın Britanya Kolumbiyası '
             'eyaletinde çiftçilerle yapılan görüşmelere dayanır. Buna göre '
             'bitki geviş getiren hayvanlarda apse, yara ve incinmeler için '
             'kullanılır; kurutulmuş kökün kaynatılmasıyla elde edilen koyu '
             'çay, enfeksiyona karşı içme suyuna katılır. Yazarlar bu '
             'kullanımı solunum ve yara için "orta düzeyde geçerli" diye '
             'derecelendirmiştir.'],
            ['Dermatoloji — sedef hastalığında haricen',
             'Journal of Clinical and Aesthetic Dermatology’deki 2018 '
             'tarihli derleme, bitkiyi Amerika Birleşik Devletleri’ne özgü '
             've iltihap giderici özellikleri deri hastalıklarında işe '
             'yarayabilecek bir tür olarak tanıtır. Bitki özütü içeren krem '
             've merhemler başlıca sedef hastalığında, bir çalışmada da '
             'atopik dermatitte denenmiştir. Derleme, başka hiçbir deri '
             'hastalığında klinik çalışma bulunmadığını belirtir.'],
            ['Berberin kaynağı — takviye pazarı',
             'ABD Ulusal Tamamlayıcı ve Bütünleştirici Sağlık Merkezi '
             '(NCCIH), berberinin altın mühür, karamuk ve Oregon üzümü gibi '
             'bitkilerde bulunan bir bileşik olduğunu yazar. Berberin '
             'takviyeleri kilo verme iddiasıyla satılmaktadır. NCCIH’nin '
             'berberinle ilgili güvenlik uyarıları bu bitkinin ağızdan '
             'alınan ürünleri için de geçerlidir.'],
        ],
        haz='EMA, DSÖ ya da TİTCK monografı bulunamadı; kabul edilmiş bir '
            'doz yoktur. Klinik çalışmalarda bitki **yalnızca haricen** '
            'kullanılmıştır: %10 özüt içeren krem ya da tescilli bir özüt '
            'içeren krem günde iki kez, 12 haftaya kadar sürülmüştür. Bunlar '
            'araştırma koşullarıdır, öneri değildir. Kökün kaynatılarak '
            'içilmesi etnoveteriner kayıtlarda geçer; insanda ağızdan '
            'kullanım için güvenilir bir doz yoktur ve berberin nedeniyle '
            'aşağıdaki uyarılar geçerlidir.',
        bilim='Kanıt haricen kullanım ve sedef hastalığı üzerinedir. 2018 '
              'tarihli derleme 502 yayından ölçütlere uyan 8 klinik '
              'çalışmayı incelemiştir; sedef hastalığındaki 7 çalışmanın '
              '5’inde istatistiksel olarak anlamlı iyileşme bildirilmiş, '
              'yanlılık riski düşük ya da belirsiz bulunmuştur. Bunların en '
              'büyüğü olan 2006 tarihli çift kör çalışmada 200 hasta 12 hafta '
              'boyunca günde iki kez krem ya da plasebo sürmüş, bitki '
              'grubunda hastalık şiddeti (PASI) ve yaşam kalitesi puanları '
              'plaseboya göre anlamlı biçimde iyileşmiştir (P < 0,05). 2005 '
              'tarihli bir raporda 32 hastanın %84’ü yanıtı iyi ya da çok iyi '
              'diye değerlendirmiştir; bu çalışma kör değildir. 2025 tarihli '
              'sistematik derleme (20 randomize çalışma, 1115 hasta) bitkiyi '
              '"umut verici" bulur, ancak bitkisel tedavilerin **gerçek '
              'etkinliği ve güvenliği için daha fazla araştırma** gerektiğini '
              'yazar. Ağızdan kullanım için klinik kanıt bu kaynaklarda '
              'yoktur.',
        kanit='sinirli',
        guv='orta',
        guvNot='Haricen kullanımda 2006 tarihli çalışmada yan etkiler '
               'seyrek (%1’den az) ve hafif olmuştur: döküntü, sürerken '
               'yanma hissi ve giysilerin boyanması. ⚠️ Ağızdan kullanımda '
               'durum farklıdır, çünkü bitki berberin içerir. NCCIH’ye göre '
               'berberin **gebelikte ve emzirmede güvenli olmayabilir** ve '
               '**bebekler için büyük olasılıkla güvensizdir**; bebeklerde '
               'beyin hasarına yol açabilen bilirubin birikimiyle '
               'ilişkilendirilmiştir. Bu nedenle gebeler, emzirenler ve '
               'bebekler kullanmamalı, emziren anneler göğüs bölgesine '
               'sürmemelidir. Berberinle yapılan çalışmalarda bulantı, karın '
               'ağrısı, şişkinlik, kabızlık ve ishal bildirilmiştir. Düzenli '
               'ilaç kullananlar, özellikle organ nakli hastaları, hekimine '
               'danışmadan kullanmamalıdır.',
        etk=[
            ['Siklosporin',
             'NCCIH’ye göre berberinin, organ naklinde reddi önlemek için '
             'kullanılan siklosporinle etkileştiği gösterilmiştir. Berberin '
             'içeren bu bitkinin ağızdan alınan ürünleri siklosporin '
             'kullananlarda kullanılmamalıdır.'],
            ['Diğer ilaçlar — veri yok',
             'Bu bitkinin kendisiyle yapılmış bir ilaç etkileşimi çalışması '
             'dayanak alınan kaynaklarda yoktur. Düzenli ilaç kullananlar '
             'ağızdan alınan ürünleri hekimine sormadan kullanmamalıdır.'],
        ],
        ilginc='Kew bu türü karamukla aynı cinse, Berberis’e yerleştirir; '
               'dermatoloji yayınları ise eski cins adı Mahonia’yı '
               'kullanmayı sürdürür. 2006 tarihli çalışmada kremin en sık '
               'bildirilen yan etkilerinden biri giysileri boyamasıdır.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklar çiçeklenme ve toplama zamanı '
                   'için bir takvim vermez. Etnoveteriner kayıtlarda '
                   'kurutulmuş kök kullanılır.',
            yetisme='Kew POWO’ya göre çalı ya da yarı çalıdır; doğal yayılışı '
                    'Kanada’nın güneybatısından Kaliforniya’nın kuzeyine '
                    'uzanır (Britanya Kolumbiyası, Washington, Oregon, Idaho, '
                    'Montana, Kaliforniya) ve çoğunlukla ılıman kuşakta '
                    'yetişir. Türkiye’de doğal yayılışı yoktur.',
            yoresel='Türkçede yerleşik bir yöresel adı yok.',
            karisma='Karamuk (Berberis vulgaris) aynı cinsten ayrı bir '
                    'türdür ve bu sitede ayrı kaydı vardır. NCCIH’ye göre '
                    'altın mühür ve karamuk da berberin içerir; berberin '
                    'uyarıları ortaktır, ama klinik çalışmalar türden türe '
                    'aktarılamaz. Ürün etiketlerinde bitki Mahonia aquifolium '
                    'ya da Berberis aquifolium adıyla geçebilir; ikisi aynı '
                    'türdür.',
        ),
        kaynak=[
            ['Berberis aquifolium Pursh, Plants of the World Online, Royal '
             'Botanic Gardens, Kew',
             POWO + '31334-2'],
            ['M. Janeczek, L. Moy, E. P. Lake, J. Swan, “Review of the '
             'Efficacy and Safety of Topical Mahonia aquifolium for the '
             'Treatment of Psoriasis and Atopic Dermatitis”, Journal of '
             'Clinical and Aesthetic Dermatology 11(12): 42–47, 2018',
             'https://pubmed.ncbi.nlm.nih.gov/30666279/'],
            ['S. Bernstein, H. Donsky, W. Gulliver, D. Hamilton, S. Nobel, '
             'R. Norman, “Treatment of mild to moderate psoriasis with '
             'Reliéva, a Mahonia aquifolium extract — a double-blind, '
             'placebo-controlled study”, American Journal of Therapeutics '
             '13(2): 121–126, 2006',
             'https://pubmed.ncbi.nlm.nih.gov/16645428/'],
            ['W. P. Gulliver, H. J. Donsky, “A report on three recent '
             'clinical trials using Mahonia aquifolium 10% topical cream and '
             'a review of the worldwide clinical experience with Mahonia '
             'aquifolium for the treatment of plaque psoriasis”, American '
             'Journal of Therapeutics 12(5): 398–406, 2005',
             'https://pubmed.ncbi.nlm.nih.gov/16148424/'],
            ['M. Anheyer, H. Cramer, T. Ostermann, A. Längler, D. Anheyer, '
             '“Herbal medicine for treating psoriasis: A systematic review”, '
             'Complementary Therapies in Medicine 90: 103173, 2025',
             'https://pubmed.ncbi.nlm.nih.gov/40210174/'],
            ['C. Lans, N. Turner, T. Khan, G. Brauer, W. Boepple, '
             '“Ethnoveterinary medicines used for ruminants in British '
             'Columbia, Canada”, Journal of Ethnobiology and Ethnomedicine '
             '3: 11, 2007',
             'https://pubmed.ncbi.nlm.nih.gov/17324258/'],
            ['“Berberine and Weight Loss: What You Need To Know”, National '
             'Center for Complementary and Integrative Health (NCCIH), son '
             'güncelleme Kasım 2023',
             'https://www.nccih.nih.gov/health/berberine-and-weight-loss-what-you-need-to-know'],
        ],
        rel=['karamuk', 'altinmuhur', 'huanglian'],
        en=dict(
            name='Oregon grape',
            other='Synonym Mahonia aquifolium (Pursh) Nutt.; Kew POWO treats '
                  'this name as a synonym of Berberis aquifolium, while '
                  'clinical publications mostly use the name Mahonia. English '
                  'Oregon grape. The part used is the root and extracts '
                  'prepared from it; it is applied externally as a cream or '
                  'ointment. It is one of the berberine-containing plants.',
            part='Root; plant extract in creams and ointments for external '
                 'use',
            uses=[
                ['British Columbia — root tea in animal care',
                 'A study published in the Journal of Ethnobiology and '
                 'Ethnomedicine in 2007 is based on interviews with farmers '
                 'in the Canadian province of British Columbia. According to '
                 'it, the plant is used for abscesses, wounds and injuries in '
                 'ruminants; a strong tea made by simmering the dried root is '
                 'added to the drinking water against infection. The authors '
                 'graded this use as of "mid-level validity" for respiratory '
                 'support and for wounds.'],
                ['Dermatology — externally in psoriasis',
                 'The 2018 review in the Journal of Clinical and Aesthetic '
                 'Dermatology presents the plant as a species native to the '
                 'United States whose anti-inflammatory properties may be '
                 'useful in skin disorders. Creams and ointments containing '
                 'the plant extract have been tried mainly in psoriasis and, '
                 'in one trial, in atopic dermatitis. The review notes that '
                 'no clinical trial was found in any other skin disorder.'],
                ['A source of berberine — the supplement market',
                 'The US National Center for Complementary and Integrative '
                 'Health (NCCIH) writes that berberine is a compound found in '
                 'plants such as goldenseal, barberry and Oregon grape. '
                 'Berberine supplements are sold on a weight-loss claim. '
                 'NCCIH’s safety warnings about berberine also apply to '
                 'products of this plant taken by mouth.'],
            ],
            prep='No EMA, WHO or Turkish (TİTCK) monograph could be found; '
                 'there is no accepted dose. In clinical trials the plant '
                 'was used **externally only**: a cream containing 10% '
                 'extract, or a cream containing a proprietary extract, was '
                 'applied twice a day for up to 12 weeks. These are research '
                 'conditions, not recommendations. Simmering the root as a '
                 'drink appears in ethnoveterinary records; there is no '
                 'reliable dose for use by mouth in humans, and because of '
                 'berberine the warnings below apply.',
            science='The evidence concerns external use and psoriasis. The '
                    '2018 review examined 8 clinical trials meeting its '
                    'criteria out of 502 publications; in 5 of the 7 trials '
                    'in psoriasis a statistically significant improvement was '
                    'reported, and the risk of bias was judged low or '
                    'unclear. In the largest of these, a double-blind trial '
                    'from 2006, 200 patients applied cream or placebo twice a '
                    'day for 12 weeks, and disease severity (PASI) and '
                    'quality-of-life scores improved significantly in the '
                    'plant group compared with placebo (P < 0.05). In a 2005 '
                    'report, 84% of 32 patients rated the response as good to '
                    'excellent; that study was not blinded. A 2025 systematic '
                    'review (20 randomised trials, 1115 patients) finds the '
                    'plant "promising" but writes that **more research is '
                    'needed on the true effectiveness and safety** of herbal '
                    'treatments. These sources contain no clinical evidence '
                    'for use by mouth.',
            safety='In external use, side effects in the 2006 trial were '
                   'infrequent (under 1%) and minor: rash, a burning '
                   'sensation on application and staining of clothes. ⚠️ Use '
                   'by mouth is a different matter, because the plant '
                   'contains berberine. According to NCCIH, berberine **may '
                   'be unsafe in pregnancy and while breastfeeding** and is '
                   '**likely to be unsafe for infants**; in infants it has '
                   'been linked to a build-up of bilirubin that can cause '
                   'brain damage. For this reason pregnant and breastfeeding '
                   'women and infants should not use it, and breastfeeding '
                   'mothers should not apply it to the breast area. Nausea, '
                   'abdominal pain, bloating, constipation and diarrhoea have '
                   'been reported in studies of berberine. People on regular '
                   'medication, transplant patients in particular, should not '
                   'use it without consulting their doctor.',
            fact='Kew places this species in Berberis, the same genus as '
                 'barberry; dermatology publications go on using the old '
                 'genus name Mahonia. In the 2006 trial one of the most '
                 'frequently reported side effects of the cream was that it '
                 'stained clothes.',
            season='The sources relied on here give no calendar for '
                   'flowering or gathering. In ethnoveterinary records the '
                   'dried root is used.',
            habitat='According to Kew POWO it is a shrub or subshrub; its '
                    'native range runs from south-western Canada to northern '
                    'California (British Columbia, Washington, Oregon, Idaho, '
                    'Montana, California) and it grows mainly in the '
                    'temperate zone. It is not native to Türkiye.',
            local='It has no established local name in Turkish.',
            confusion='Barberry (Berberis vulgaris) is a different species '
                      'of the same genus and has its own record on this '
                      'site. According to NCCIH, goldenseal and barberry '
                      'also contain berberine; the berberine warnings are '
                      'shared, but clinical trials cannot be transferred '
                      'from one species to another. On product labels the '
                      'plant may appear as Mahonia aquifolium or as Berberis '
                      'aquifolium; the two are the same species.',
        ),
        etk_en=[
            ['Ciclosporin',
             'According to NCCIH, berberine has been shown to interact with '
             'ciclosporin, which is used to prevent rejection in organ '
             'transplantation. Products of this berberine-containing plant '
             'taken by mouth should not be used by people taking '
             'ciclosporin.'],
            ['Other medicines — no data',
             'The sources relied on here contain no drug interaction study '
             'done with this plant itself. People on regular medication '
             'should not use products taken by mouth without asking their '
             'doctor.'],
        ],
    ),

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='yalanciakasya',
        foto='',
        tr='Yalancı akasya',
        la='Robinia pseudoacacia L.',
        taxon='Robinia pseudoacacia',
        fam='Fabaceae (baklagiller)',
        diger='İngilizce black locust, false acacia; yayınlarda çoğu kez '
              'yalnızca Robinia diye anılır. Cornutus bitkiyi 1635’te Jean '
              'Robin onuruna Acacia Americana Robini adıyla tanımlamıştır. '
              'Besin değeri taşıyan ürünü çiçek nektarından yapılan baldır; '
              'kabuk, tohum ve yapraklar zehirlidir. Gerçek akasyalar '
              '(Acacia) ayrı bir cinstir.',
        bolge=['kamerika', 'avrupa'],
        kat=['besin', 'zehir'],
        kisim='Çiçek nektarından elde edilen bal; kabuk, tohum ve yapraklar '
              'zehirlidir, kullanılmaz',
        kul=[
            ['Orta Avrupa — bal ağacı',
             'Forest Ecology and Management’ta 2017’de yayımlanan derleme, '
             'ağacın yüksek nektar verimi nedeniyle arıcılıkta değer '
             'gördüğünü yazar. Derlemeye göre bal verimi ağacın yaşına göre '
             'değişir ve Macaristan’da 15 yaşındaki meşcerelerde hektar '
             'başına yılda 418 kg’a ulaşır. Orta Avrupa’da en çok Robinia '
             'balını yılda yaklaşık 25.000 tonla Macaristan üretir. '
             'Piyasada "akasya balı" diye satılan bal bu ağacın balıdır.'],
            ['Macaristan — ağaçlandırma ve "ulusal ağaç"',
             'Aynı derlemeye göre ilk büyük ağaçlandırma 1750’de '
             'Macaristan’da, bir tahkimatı korumak için 290 hektarlık '
             'alanda yapılmıştır. Bugün Macaristan ormanlarının yaklaşık '
             '%24’ü bu ağaçtan oluşur ve ağaç ülkenin resmî olmayan ulusal '
             'ağacı sayılır. Hızlı büyümesi, suya ve çürümeye dayanıklı '
             'odunu, yakacak odun, yaprak yemi ve erozyon kontrolü başlıca '
             'kullanım nedenleridir.'],
            ['Avrupa — sevilen ve istenmeyen istilacı',
             'Veterinární medicína’daki 2024 tarihli yazı, yalancı akasyanın '
             'Avrupa’ya getirilen ilk Kuzey Amerika ağaç türü olduğunu '
             'aktarır. 2017 tarihli derleme ağacın ekonomik yararı ile '
             'çevreye verdiği zarar arasındaki çatışmayı anlatır: azot '
             'bağlayan bu öncü tür Macaristan’da 33.000 hektar açık kumul '
             'çayırına zarar vermiş, Avusturya’da kuru ve yarı kuru '
             'çayırların %40’ına yerleşmiştir.'],
            ['Çiçekler — zehirli sayılmayan tek kısım',
             '2024 tarihli veteriner olgu sunumuna göre çiçek durumları '
             'dışında bitkinin bütün kısımları, özellikle kabuk ve tohumlar '
             'zehirlidir. Çiçek özütünün polifenol içeriği son yıllarda '
             'laboratuvar çalışmalarına konu olmuştur. Çiçeklerin insanda '
             'güvenli tüketim miktarını belirleyen bir çalışma dayanak '
             'alınan kaynaklarda yoktur.'],
        ],
        haz='Hazırlanması ve kullanılması önerilmez; bu sayfa bilerek tarif '
            'vermiyor. Nedeni, kabuk, tohum ve yaprakların insanda ve '
            'hayvanda zehirlenmeye yol açması ve çiçekler dışındaki hiçbir '
            'kısmın güvenli sayılmamasıdır. Kabul edilmiş bir doz yoktur; '
            'EMA, DSÖ ya da TİTCK monografı bulunamadı. Besin olarak '
            'tüketilen ürün, arıların çiçek nektarından yaptığı baldır.',
        bilim='Bu ağaçla ilgili tıbbi yayınlar tedavi değil zehirlenme '
              'üzerinedir. İspanya’dan 1989 tarihli bir çalışmada okul '
              'bahçesinde kabuğu emen ya da çiğneyen altı kız çocuğunda '
              '(ortalama yaş 6,5) karın ağrısı, bulantı, kusma, kas '
              'güçsüzlüğü, göz bebeği genişlemesi, baş dönmesi ve ishal '
              'görülmüş; kabuğu tadanların %31,6’sı hastalanmış, tedaviyle '
              'hepsi iyileşmiştir. 1990 tarihli bir başka olgu dizisinde yedi '
              'erkek çocuğun üçünde **koma dahil nörolojik belirtiler** '
              'gelişmiş, hepsi düzelmiştir. 2024 tarihli veteriner olgu '
              'sunumunda kabuğu yiyen iki kısraktan biri ölmüş, diğerinde '
              'ağır ensefalopati gelişmiştir. 2020 tarihli bir olgu sunumu, '
              'ağaçtaki robin adlı toksalbüminin protein sentezini '
              'engelleyerek hücre ölümüne yol açtığını ve kıymık batması '
              'sonrası bir hastada doku nekrozu geliştiğini bildirir. '
              'Çiçek özütleriyle yapılan çalışmalar laboratuvar düzeyindedir; '
              'insanda tedavi edici bir etki gösterilmemiştir.',
        kanit='geleneksel',
        guv='yuksek',
        guvNot='⚠️ **Kabuk, tohum ve yapraklar zehirlidir.** Olgu '
               'bildirimlerinde çocuklar kabuğu emdikten ya da çiğnedikten '
               'sonra karın ağrısı, susama, bulantı, kusma, boğaz kuruluğu, '
               'kas güçsüzlüğü, göz bebeği genişlemesi, baş ağrısı, baş '
               'dönmesi ve ishal yaşamış; bir olgu dizisinde koma '
               'görülmüştür. Çocuklar en büyük risk grubudur; okul bahçesi '
               've parklardaki ağaçların kabuğu ve bakla içindeki tohumları '
               'ağza alınmamalıdır. Atlar için ölümcül olabilir. Kıymıkları da zararsız değildir: batma sonrası ağır doku '
               'nekrozu bildirilmiştir. Gebelik, emzirme ve ilaç kullananlar '
               'için güvenli bir kullanım yoktur. **Zehirlenme şüphesinde '
               '114 (Ulusal Zehir Danışma Merkezi) ya da 112 aranmalıdır.** '
               'Bu uyarılar bal için değil, ağacın kendisi içindir.',
        etk=[
            ['İlaç etkileşimi — veri yok',
             'Bu ağaç için ilaç etkileşimi verisi yoktur. Zehirli olduğu '
             'için herhangi bir ilaçla birlikte ya da tek başına '
             'kullanılması önerilmez.'],
        ],
        ilginc='Ağacın Paris’e 1601’de Jean Robin tarafından getirildiği sık '
               'sık yazılır. Forest Ecology and Management’taki derleme, '
               'eski bir kaynağa dayanarak bu tarihi reddeder; Robin’in adı '
               'bitkiye 1635’te Cornutus’un verdiği Acacia Americana Robini '
               'adıyla girmiştir.',
        ek=dict(
            mevsim='Derlemeye göre Orta Avrupa’da ağacı sınırlayan başlıca '
                   'etken geç ilkbahar donlarıdır. Dayanak alınan kaynaklar '
                   'Türkiye için bir çiçeklenme takvimi vermez.',
            yetisme='Kew POWO’ya göre doğal yayılışı ABD’nin orta-doğu ve '
                    'doğu kesimleridir; çalı ya da ağaç biçimindedir ve '
                    'çoğunlukla ılıman kuşakta yetişir. Avrupa’da bahçelere, '
                    'yol kenarlarına ve ağaçlandırma alanlarına dikilmiş, '
                    'buralardan kendiliğinden yayılmıştır. Kurak ve fakir '
                    'topraklara dayanır; yüksek taban suyuna ve gölgeye '
                    'dayanmaz.',
            yoresel='Türkçede yalancı akasya adıyla bilinir; dayanak alınan '
                    'kaynaklarda başka bir yöresel ad geçmez.',
            karisma='Adındaki "akasya" yanıltıcıdır: gerçek akasyalar '
                    '(Acacia) ayrı bir cinstir. Tür adı pseudoacacia da '
                    '"yalancı akasya" demektir. "Akasya balı" ise gerçek '
                    'akasyadan değil, bu ağacın nektarından elde edilir.',
        ),
        kaynak=[
            ['Robinia pseudoacacia L., Plants of the World Online, Royal '
             'Botanic Gardens, Kew',
             POWO + '30034699-2'],
            ['M. Vítková, J. Müllerová, J. Sádlo, J. Pergl, P. Pyšek, “Black '
             'locust (Robinia pseudoacacia) beloved and despised: a story of '
             'an invasive tree in Central Europe”, Forest Ecology and '
             'Management 384: 287–302, 2017',
             'https://pubmed.ncbi.nlm.nih.gov/30237654/'],
            ['A. Artero Sivera, A. Arnedo Pena, A. Pastor Cubo, '
             '“Clinico-epidemiologic study of accidental poisoning with '
             'Robinia pseudoacacia L. in school children” (İspanyolca), '
             'Anales Españoles de Pediatría 30(3): 191–194, 1989',
             'https://pubmed.ncbi.nlm.nih.gov/2658707/'],
            ['X. Costa Bou, J. M. Soler i Ros, J. L. Seculi Palacios, '
             '“Poisoning by Robinia pseudoacacia” (İspanyolca), Anales '
             'Españoles de Pediatría 32(1): 68–69, 1990',
             'https://pubmed.ncbi.nlm.nih.gov/2327667/'],
            ['T. Novotna, E. Samonilova, J. Klan ve ark., “Robinia '
             'pseudoacacia poisoning in two horses: A case report”, '
             'Veterinární medicína 69(11): 395–400, 2024',
             'https://pubmed.ncbi.nlm.nih.gov/39810820/'],
            ['D. T. Browne, G. Aguilo-Seara, A. DeFranzo Jr, “The Black '
             'Locust Tree: Toxalbumin-Induced Tissue Necrosis of the Upper '
             'Extremity”, Cureus 12(11): e11758, 2020',
             'https://pubmed.ncbi.nlm.nih.gov/33409007/'],
            ['I. A. Boškov, I. M. Savić ve ark., “Stabilization of Black '
             'Locust Flower Extract via Encapsulation Using Alginate and '
             'Alginate-Chitosan Microparticles”, Polymers (Basel) 16(5): 688, '
             '2024',
             'https://pubmed.ncbi.nlm.nih.gov/38475369/'],
        ],
        rel=['hintyagi', 'porsuk', 'meyan'],
        en=dict(
            name='Black locust',
            other='English black locust, false acacia; in publications often '
                  'simply Robinia. Cornutus described the plant in 1635 as '
                  'Acacia Americana Robini in honour of Jean Robin. The '
                  'product of food value is the honey made from the flower '
                  'nectar; the bark, seeds and leaves are poisonous. The true '
                  'acacias (Acacia) are a different genus.',
            part='Honey made from the flower nectar; the bark, seeds and '
                 'leaves are poisonous and are not used',
            uses=[
                ['Central Europe — a honey tree',
                 'A review published in Forest Ecology and Management in '
                 '2017 writes that the tree is valued in beekeeping for its '
                 'high nectar yield. According to the review, honey yield '
                 'changes with the age of the tree and reaches 418 kg per '
                 'hectare a year in 15-year-old stands in Hungary. In Central '
                 'Europe the largest producer of Robinia honey is Hungary, '
                 'with about 25,000 tonnes a year. The honey sold on the '
                 'market as "acacia honey" is the honey of this tree.'],
                ['Hungary — afforestation and a "national tree"',
                 'According to the same review, the first large afforestation '
                 'was carried out in Hungary in 1750, on 290 hectares, to '
                 'protect a fortification. Today about 24% of Hungary’s '
                 'forests consist of this tree, and it is regarded as the '
                 'country’s unofficial national tree. Its fast growth, its '
                 'water- and rot-resistant wood, firewood, leaf fodder and '
                 'erosion control are the main reasons for its use.'],
                ['Europe — a beloved and unwanted invader',
                 'A 2024 paper in Veterinární medicína reports that black '
                 'locust was the first North American tree species brought '
                 'to Europe. The 2017 review describes the conflict between '
                 'the tree’s economic benefit and the harm it does to the '
                 'environment: this nitrogen-fixing pioneer species has '
                 'damaged 33,000 hectares of open sandy grassland in Hungary '
                 'and has colonised 40% of the dry and semi-dry grassland in '
                 'Austria.'],
                ['The flowers — the only part not considered poisonous',
                 'According to the 2024 veterinary case report, all parts of '
                 'the plant except the inflorescences are toxic, the bark and '
                 'seeds especially. The polyphenol content of the flower '
                 'extract has been the subject of laboratory studies in '
                 'recent years. The sources relied on here contain no study '
                 'establishing a safe amount of the flowers for human '
                 'consumption.'],
            ],
            prep='Preparing and using it is not recommended; this page '
                 'deliberately gives no recipe. The reason is that the bark, '
                 'seeds and leaves cause poisoning in humans and animals and '
                 'that no part other than the flowers is considered safe. '
                 'There is no accepted dose; no EMA, WHO or Turkish (TİTCK) '
                 'monograph could be found. The product consumed as food is '
                 'the honey that bees make from the flower nectar.',
            science='The medical literature on this tree concerns poisoning, '
                    'not treatment. In a 1989 study from Spain, six girls '
                    '(mean age 6.5) who sucked or chewed the bark in a school '
                    'yard had abdominal pain, nausea, vomiting, muscle '
                    'weakness, dilated pupils, dizziness and diarrhoea; 31.6% '
                    'of those who tasted the bark fell ill, and all recovered '
                    'with treatment. In another case series from 1990, three '
                    'of seven boys developed **neurological symptoms '
                    'including coma**, and all recovered. In a 2024 '
                    'veterinary case report, one of two mares that ate the '
                    'bark died and the other developed severe '
                    'encephalopathy. A 2020 case report states that the '
                    'toxalbumin in the tree, called robin, causes cell death '
                    'by inhibiting protein synthesis, and that a patient '
                    'developed tissue necrosis after a splinter injury. The '
                    'studies with flower extracts are at the laboratory '
                    'level; no therapeutic effect has been shown in humans.',
            safety='⚠️ **The bark, seeds and leaves are poisonous.** In case '
                   'reports, children who sucked or chewed the bark had '
                   'abdominal pain, thirst, nausea, vomiting, a dry throat, '
                   'muscle weakness, dilated pupils, headache, dizziness and '
                   'diarrhoea; coma was seen in one case series. Children '
                   'are the group most at risk; the bark of trees in school '
                   'yards and parks, and the seeds inside the pods, should '
                   'not be put in the mouth. It can be fatal to horses. Its splinters are not harmless either: severe '
                   'tissue necrosis has been reported after a puncture. '
                   'There is no safe use for pregnant or breastfeeding women '
                   'or people on medication. **If poisoning is suspected, '
                   'call 114 (the National Poison Information Centre in '
                   'Türkiye) or 112.** These warnings concern the tree '
                   'itself, not the honey.',
            fact='It is often written that the tree was brought to Paris in '
                 '1601 by Jean Robin. The review in Forest Ecology and '
                 'Management, relying on an older source, rejects that date; '
                 'Robin’s name entered the plant through the name Acacia '
                 'Americana Robini given by Cornutus in 1635.',
            season='According to the review, the main factor limiting the '
                   'tree in Central Europe is late spring frost. The sources '
                   'relied on here give no flowering calendar for Türkiye.',
            habitat='According to Kew POWO its native range is the '
                    'east-central and eastern USA; it is a shrub or tree and '
                    'grows mainly in the temperate zone. In Europe it has '
                    'been planted in gardens, along roads and in '
                    'afforestation areas, and has spread from these on its '
                    'own. It tolerates dry and poor soils; it does not '
                    'tolerate a high water table or shade.',
            local='In Turkish it is known as yalancı akasya ("false '
                  'acacia"); the sources relied on here give no other local '
                  'name.',
            confusion='The "acacia" in its name is misleading: the true '
                      'acacias (Acacia) are a different genus. The species '
                      'name pseudoacacia also means "false acacia". "Acacia '
                      'honey", in turn, comes not from true acacia but from '
                      'the nectar of this tree.',
        ),
        etk_en=[
            ['Drug interactions — no data',
             'There are no drug interaction data for this tree. Because it '
             'is poisonous, using it with any medicine or on its own is not '
             'recommended.'],
        ],
    ),

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='greyfurt',
        foto='',
        tr='Greyfurt',
        la='Citrus × paradisi Macfad.',
        taxon='Citrus × paradisi',
        fam='Rutaceae (sedefotugiller)',
        diger='İngilizce grapefruit; eski adları forbidden fruit ("yasak '
              'meyve") ve pomelo. Macfadyen 1830’da "yasak meyve"yi Citrus × '
              'paradisi adıyla sınıflandırmıştır. HortTechnology’deki 2021 '
              'tarihli derleme türü Citrus × aurantium adı altında verir ve '
              'Citrus × paradisi’yi eş ad sayar; bu sitede turunçtan ayırmak '
              'için yerleşik ad korunmuştur. Kullanılan kısım meyve ve meyve '
              'suyudur.',
        bolge=['kamerika', 'anadolu'],
        kat=['besin'],
        kisim='Meyve ve meyve suyu',
        kul=[
            ['Barbados — "yasak meyve"',
             'HortTechnology’de 2021’de yayımlanan derlemeye göre greyfurt '
             '17. yüzyılda Barbados’ta ortaya çıkmıştır ve şadok (pomelo) ile '
             'portakalın kendiliğinden oluşmuş bir melezi olduğu kabul '
             'edilir; kimyasal ve moleküler veriler bunu destekler. Hughes '
             '1750’de Barbados’ta "yasak meyve" veren bir ağaçtan söz etmiş, '
             'Browne 1756’da onu "küçük şadok" diye tanımlamıştır.'],
            ['Florida ve Teksas — ticari meyveye dönüşüm',
             'Aynı derlemeye göre Kont Odette Philippe 1823’te tohumları '
             'Florida’ya getirmiş, ağaç yetiştirip tohum dağıtmıştır. Meyve '
             '1909’a gelindiğinde ticarette "grapefruit" adıyla biliniyordu. '
             'Kırmızı etli çeşitler Teksas’ta ortaya çıkmıştır: Ruby Red '
             '1929’da bulunmuş ve 1934’te patentlenmiş, Star Ruby 1970’te '
             'piyasaya verilmiştir.'],
            ['Dünya ve Türkiye — üretim',
             'Derleme 2019–20 sezonunda dünya üretimini 6,7 milyon ton '
             'olarak verir. En büyük üretici, şadok dahil 4,9 milyon tonla '
             'Çin’dir; onu Güney Afrika (387.000 ton), Meksika (350.000 ton) '
             've **270.000 tonla Türkiye** izler. Türkiye aynı zamanda Star '
             'Ruby ve Rio Red çeşitlerinin yetiştirildiği ülkeler arasında '
             'anılır.'],
            ['Eczacılık — ilaç etkileşiminin ders kitabı örneği',
             'British Journal of Clinical Pharmacology’deki 1998 tarihli '
             'yazıya göre etki tesadüfen bulunmuştur: felodipin ile alkol '
             'arasındaki etkileşimi inceleyen bir çalışmada alkolün tadını '
             'örtmek için greyfurt suyu kullanılmış ve ilacın kandaki '
             'düzeyinin beklenmedik biçimde arttığı görülmüştür. '
             'HortTechnology derlemesi ilk bildirimin 1989’da yapıldığını '
             'yazar.'],
        ],
        haz='Greyfurt bir gıdadır; kabul edilmiş bir tıbbi doz yoktur. '
            'Meyve taze yenir ya da suyu sıkılarak içilir. İlaç kullananlar '
            'için "güvenli miktar" genel olarak verilemez: FDA, greyfurt '
            'suyunun ilaçla etkileşip etkileşmediğinin ve varsa ne kadarının '
            'güvenli olduğunun **hekime ya da eczacıya sorulmasını** önerir. '
            'FDA’ya göre meyve suyu karışımlarının ve meyve aromalı '
            'içeceklerin etiketi de greyfurt suyu bakımından okunmalıdır.',
        bilim='En sağlam bilimsel bulgu bir tedavi etkisi değil, ilaç '
              'etkileşimidir. Greyfurt suyu ince bağırsak duvarındaki CYP3A4 '
              'enzimini baskılar; bu enzimle yıkılan ilaçların kana geçen '
              'miktarı artar. 1998 tarihli derlemelere göre etki 24 saat '
              'sürebilir, kişiden kişiye çok değişir ve felodipin, '
              'nitrendipin, nisoldipin ve sakinavir için kandaki düzey '
              'ölçütlerinde ortanca artış **%70’i aşmıştır**. HortTechnology '
              'derlemesi etkinin sorumlusu olarak furanokumarinleri '
              '(bergamottin ve dihidroksibergamottin) gösterir. Sağlık '
              'iddiaları tarafında kanıt zayıftır: 2017 tarihli sistematik '
              'derleme ve meta-analiz, fazla kilolu ve obez 250 katılımcılı 3 '
              'randomize çalışmayı incelemiş, vücut ağırlığında anlamlı fark '
              'bulmamış (ortalama fark −0,45 kg), sistolik tansiyonda ise '
              '2,43 mmHg’lik küçük bir düşüş saptamıştır. Yazarlar çalışma '
              'sayısının azlığı ve sürelerin kısalığı nedeniyle sonuç '
              'çıkarmanın güç olduğunu belirtir.',
        kanit='sinirli',
        guv='orta',
        guvNot='Sağlıklı ve ilaç kullanmayan kişilerde gıda olarak '
               'tüketimine ilişkin bir uyarı dayanak alınan kaynaklarda '
               'yoktur. ⚠️ **Asıl risk ilaç kullananlar içindir.** FDA’ya '
               'göre greyfurt suyu birçok ilacın kandaki miktarını artırır; '
               'örneğin statin düzeyinin yükselmesi karaciğer ve kas '
               'hasarı, bunun sonucunda böbrek yetmezliği riskini büyütür. '
               'Bazı ilaçlarda ise (feksofenadin) etki tersinedir: ilacın '
               'kana geçişi azalır ve ilaç daha az işe yarar. FDA, ilacı '
               'greyfurtla etkileşen kişilerin **turunç, şadok (pomelo) ve '
               'tangelo da yememesini** söyler. Yaşlılar, çok sayıda ilaç '
               'kullananlar, gebeler ve emzirenler ilaç kullanıyorsa aynı '
               'kural geçerlidir: ilacın prospektüsüne bakılmalı, hekime ya '
               'da eczacıya sorulmalıdır. Çocuklar için ayrı bir veri yoktur.',
        etk=[
            ['Statinler (simvastatin, atorvastatin)',
             'FDA listesinde. İlacın kandaki düzeyi yükselir; karaciğer ve '
             'kas hasarı, buna bağlı böbrek yetmezliği riski artar.'],
            ['Kalsiyum kanal blokerleri (nifedipin, felodipin, nisoldipin)',
             'Etkileşimin ilk gösterildiği ilaç grubu. 1998 tarihli '
             'derlemeye göre felodipin ve nisoldipinde kan düzeyi '
             'ölçütlerinde ortanca artış %70’i aşmıştır; etki 24 saat '
             'sürebilir.'],
            ['Siklosporin',
             'FDA listesinde; organ nakli sonrası kullanılan bu ilacın kan '
             'düzeyi yükselir. Nakil hastaları hekimine sormadan '
             'greyfurt tüketmemelidir.'],
            ['Buspiron, budesonid, amiodaron',
             'FDA’nın saydığı diğer örnekler: kaygı ilacı buspiron, Crohn '
             'hastalığı ve ülseratif kolitte kullanılan budesonid ve ritim '
             'bozukluğu ilacı amiodaron.'],
            ['Feksofenadin',
             'FDA’ya göre burada etki terstir: greyfurt suyu taşıyıcı '
             'proteinleri etkiler, ilacın kana geçişi azalır ve ilaç daha az '
             'işe yarar. Portakal ve elma suyu da aynı etkiyi yapabilir.'],
        ],
        ilginc='Greyfurt–ilaç etkileşimi tesadüfen bulunmuştur: '
               'araştırmacılar felodipin ile alkol arasındaki etkileşimi '
               'incelerken alkolün tadını örtmek için greyfurt suyu '
               'kullanmış, beklenmedik sonucu meyve suyu vermiştir (British '
               'Journal of Clinical Pharmacology, 1998).',
        ek=dict(
            mevsim='Dayanak alınan kaynaklar hasat ayları için bir takvim '
                   'vermez. HortTechnology derlemesi soğuk havanın kabuktaki '
                   'kırmızı rengi artırdığını yazar.',
            yetisme='Derlemeye göre Barbados kökenli bir melezdir ve bugün '
                    'Çin, ABD, Güney Afrika, Meksika, Türkiye ve İsrail’de '
                    'yetiştirilir. Dona duyarlıdır: derleme, Şubat 2021’de '
                    'Teksas’ta bazı bahçelerde sıcaklığın saatlerce −7,2 '
                    '°C’ye düştüğünü ve donların üretim alanını azalttığını '
                    'aktarır.',
            yoresel='Dayanak alınan kaynaklarda Türkçe yöresel ad geçmez.',
            karisma='Şadok (pomelo, Citrus maxima) greyfurdun atalarından '
                    'biridir ve ayrı bir türdür; "pomelo" adı bir dönem '
                    'greyfurt için de kullanılmıştır. Turunç (Citrus × '
                    'aurantium) bu sitede ayrı kayıttır. FDA’ya göre turunç, '
                    'şadok ve tangelo ilaçlarla greyfurda benzer biçimde '
                    'etkileşebilir.',
        ),
        kaynak=[
            ['“Grapefruit: History, Use, and Breeding”, HortTechnology '
             '31(3), 2021 (sorumlu yazar E. S. Louzada), American Society '
             'for Horticultural Science',
             'https://journals.ashs.org/view/journals/horttech/31/3/article-p243.xml'],
            ['“Grapefruit Juice and Some Drugs Don’t Mix”, U.S. Food and '
             'Drug Administration (FDA), Consumer Updates, içerik tarihi '
             '1 Temmuz 2021',
             'https://www.fda.gov/consumers/consumer-updates/grapefruit-juice-and-some-drugs-dont-mix'],
            ['D. G. Bailey, J. Malcolm, O. Arnold, J. D. Spence, “Grapefruit '
             'juice-drug interactions”, British Journal of Clinical '
             'Pharmacology 46(2): 101–110, 1998',
             'https://pubmed.ncbi.nlm.nih.gov/9723817/'],
            ['U. Fuhr, “Drug interactions with grapefruit juice. Extent, '
             'probable mechanism and clinical relevance”, Drug Safety 18(4): '
             '251–272, 1998',
             'https://pubmed.ncbi.nlm.nih.gov/9565737/'],
            ['I. Onakpoya, J. O’Sullivan, C. Heneghan, M. Thompson, “The '
             'effect of grapefruits (Citrus paradisi) on body weight and '
             'cardiovascular risk factors: A systematic review and '
             'meta-analysis of randomized clinical trials”, Critical Reviews '
             'in Food Science and Nutrition 57(3): 602–612, 2017',
             'https://pubmed.ncbi.nlm.nih.gov/25880021/'],
        ],
        rel=['turunc', 'kantaron'],
        en=dict(
            name='Grapefruit',
            other='English grapefruit; older names are forbidden fruit and '
                  'pomelo. In 1830 Macfadyen classified the "forbidden '
                  'fruit" as Citrus × paradisi. The 2021 review in '
                  'HortTechnology gives the species under the name Citrus × '
                  'aurantium and treats Citrus × paradisi as a synonym; on '
                  'this site the established name is kept to separate it '
                  'from bitter orange. The parts used are the fruit and the '
                  'juice.',
            part='Fruit and fruit juice',
            uses=[
                ['Barbados — the "forbidden fruit"',
                 'According to a review published in HortTechnology in '
                 '2021, grapefruit arose in Barbados in the 17th century and '
                 'is taken to be a chance hybrid of pummelo and sweet '
                 'orange; chemical and molecular data support this. In 1750 '
                 'Hughes mentioned a tree in Barbados bearing the "forbidden '
                 'fruit", and in 1756 Browne described it as a "smaller '
                 'shaddock".'],
                ['Florida and Texas — becoming a commercial fruit',
                 'According to the same review, Count Odette Philippe '
                 'brought seeds to Florida in 1823, raised trees and '
                 'distributed seed. By 1909 the fruit was known in commerce '
                 'as "grapefruit". The red-fleshed varieties arose in Texas: '
                 'Ruby Red was found in 1929 and patented in 1934, and Star '
                 'Ruby was released in 1970.'],
                ['The world and Türkiye — production',
                 'The review gives world production in the 2019–20 season '
                 'as 6.7 million tonnes. The largest producer is China, with '
                 '4.9 million tonnes including pummelo; it is followed by '
                 'South Africa (387,000 tonnes), Mexico (350,000 tonnes) and '
                 '**Türkiye with 270,000 tonnes**. Türkiye is also named '
                 'among the countries where the Star Ruby and Rio Red '
                 'varieties are grown.'],
                ['Pharmacy — the textbook example of a drug interaction',
                 'According to a 1998 paper in the British Journal of '
                 'Clinical Pharmacology, the effect was found by chance: in '
                 'a study of the interaction between felodipine and alcohol, '
                 'grapefruit juice was used to mask the taste of the '
                 'alcohol, and the level of the drug in the blood was seen '
                 'to rise unexpectedly. The HortTechnology review writes '
                 'that the first report was made in 1989.'],
            ],
            prep='Grapefruit is a food; there is no accepted medicinal dose. '
                 'The fruit is eaten fresh or its juice is pressed and '
                 'drunk. For people taking medicines no general "safe '
                 'amount" can be given: the FDA advises **asking a doctor or '
                 'pharmacist** whether grapefruit juice interacts with the '
                 'medicine and, if so, how much is safe. According to the '
                 'FDA, the labels of fruit juice blends and fruit-flavoured '
                 'drinks should also be read for grapefruit juice.',
            science='The most solid scientific finding is not a therapeutic '
                    'effect but a drug interaction. Grapefruit juice '
                    'suppresses the enzyme CYP3A4 in the wall of the small '
                    'intestine; the amount of drugs broken down by this '
                    'enzyme that reaches the blood increases. According to '
                    'the 1998 reviews the effect can last 24 hours, varies '
                    'greatly between individuals, and for felodipine, '
                    'nitrendipine, nisoldipine and saquinavir the median '
                    'increase in measures of blood level **exceeded 70%**. '
                    'The HortTechnology review names the furanocoumarins '
                    '(bergamottin and dihydroxybergamottin) as responsible '
                    'for the effect. On the side of health claims the '
                    'evidence is weak: a 2017 systematic review and '
                    'meta-analysis examined 3 randomised trials with 250 '
                    'overweight and obese participants, found no significant '
                    'difference in body weight (mean difference −0.45 kg) '
                    'and detected a small fall of 2.43 mmHg in systolic '
                    'blood pressure. The authors note that the small number '
                    'of trials and their short duration make it hard to draw '
                    'conclusions.',
            safety='The sources relied on here contain no warning about its '
                   'consumption as food by healthy people who take no '
                   'medicines. ⚠️ **The real risk is for people on '
                   'medication.** According to the FDA, grapefruit juice '
                   'raises the amount of many drugs in the blood; a higher '
                   'statin level, for example, increases the risk of liver '
                   'and muscle damage and, as a result, kidney failure. With '
                   'some drugs (fexofenadine) the effect is the opposite: '
                   'less of the drug reaches the blood and it works less '
                   'well. The FDA says that people whose medicine interacts '
                   'with grapefruit should **not eat Seville oranges, '
                   'pomelos or tangelos either**. For older people, people '
                   'taking many medicines, and pregnant or breastfeeding '
                   'women who take medicines, the same rule applies: read '
                   'the patient information leaflet and ask a doctor or '
                   'pharmacist. There are no separate data for children.',
            fact='The grapefruit–drug interaction was found by chance: while '
                 'studying the interaction between felodipine and alcohol, '
                 'the researchers used grapefruit juice to mask the taste of '
                 'the alcohol, and the unexpected result came from the juice '
                 '(British Journal of Clinical Pharmacology, 1998).',
            season='The sources relied on here give no calendar of harvest '
                   'months. The HortTechnology review writes that cold '
                   'weather enhances the red colour of the peel.',
            habitat='According to the review it is a hybrid of Barbadian '
                    'origin and is grown today in China, the USA, South '
                    'Africa, Mexico, Türkiye and Israel. It is sensitive to '
                    'frost: the review reports that in February 2021 the '
                    'temperature in some Texas groves fell to −7.2 °C for '
                    'hours and that freezes have reduced the bearing area.',
            local='The sources relied on here give no Turkish local name.',
            confusion='Pummelo (pomelo, Citrus maxima) is one of the '
                      'ancestors of grapefruit and is a different species; '
                      'the name "pomelo" was for a time also used for '
                      'grapefruit. Bitter orange (Citrus × aurantium) is a '
                      'separate record on this site. According to the FDA, '
                      'Seville oranges, pomelos and tangelos may interact '
                      'with medicines in a similar way to grapefruit.',
        ),
        etk_en=[
            ['Statins (simvastatin, atorvastatin)',
             'On the FDA list. The level of the drug in the blood rises; the '
             'risk of liver and muscle damage, and of kidney failure as a '
             'result, increases.'],
            ['Calcium channel blockers (nifedipine, felodipine, nisoldipine)',
             'The drug group in which the interaction was first shown. '
             'According to the 1998 review, the median increase in measures '
             'of blood level exceeded 70% for felodipine and nisoldipine; the '
             'effect can last 24 hours.'],
            ['Ciclosporin',
             'On the FDA list; the blood level of this drug, used after '
             'organ transplantation, rises. Transplant patients should '
             'not consume grapefruit without asking their doctor.'],
            ['Buspirone, budesonide, amiodarone',
             'Other examples listed by the FDA: the anti-anxiety drug '
             'buspirone, budesonide used in Crohn’s disease and ulcerative '
             'colitis, and the heart rhythm drug amiodarone.'],
            ['Fexofenadine',
             'According to the FDA the effect here is the reverse: '
             'grapefruit juice affects transporter proteins, less of the '
             'drug reaches the blood and it works less well. Orange and '
             'apple juice may have the same effect.'],
        ],
    ),

    dict(
        yayin='2026-11-24',
        arsiv=True,
        id='arnavutbiberi',
        foto='',
        tr='Arnavut biberi',
        la='Capsicum frutescens L.',
        taxon='Capsicum frutescens',
        fam='Solanaceae (patlıcangiller)',
        diger='İngilizce chili pepper, bird pepper; Brezilya’da malagueta '
              '(pimenta malagueta). Kew POWO adı kabul edilmiş ad olarak '
              'verir; bazı kaynaklar türü Capsicum annuum içinde sayar. '
              'Kullanılan kısım olgun meyvedir. AB monografı (Capsici '
              'fructus) Capsicum annuum var. minimum ile birlikte bu türün '
              'küçük meyveli çeşitlerini kapsar; bu sitedeki acı biber kaydı '
              'Capsicum annuum içindir.',
        bolge=['kamerika', 'amazon'],
        kat=['besin', 'sifa'],
        kisim='Olgun meyve (taze ya da kurutulmuş)',
        kul=[
            ['Neotropik Amerika — mısırla birlikte en eski besinlerden',
             'Science dergisinde 2007’de yayımlanan çalışma, biber cinsine '
             'özgü nişasta tanelerini Bahamalar’dan Peru’nun güneyine uzanan '
             'yedi kazı alanında saptamıştır. En eski buluntular günümüzden '
             '6000 yıl öncesine tarihlenir. Yazarlara göre mısır ve biber '
             'birlikte, bazı bölgelerde çömlekçilikten bile eski, yaygın '
             'bir besin bütünü oluşturuyordu. Bu bulgu cins düzeyindedir; '
             'tek tek türleri ayırmaz.'],
            ['Brezilya — malagueta biberi',
             'Molecules dergisindeki 2017 tarihli çalışma Capsicum '
             'frutescens’i malagueta biberi adıyla inceler. Meyvenin '
             'acılığını veren kapsaisinoitler olgunlaşma sırasında birikir; '
             'başlıca bileşik kapsaisin, ikincisi dihidrokapsaisindir. Biber '
             'bütün dünyada mutfaklara girmiş bir baharat ve sebzedir.'],
            ['Avrupa — kas ağrısında haricen',
             'EMA monografı, bu türün küçük meyveli çeşitlerinin ve Capsicum '
             'annuum var. minimum’un meyvesinden hazırlanan ürünleri, '
             '**bel ağrısı gibi kas ağrılarının giderilmesinde** yerleşik '
             'kullanım temelinde kabul eder. Ürün ilaçlı yakı ya da cilde '
             'sürülen yarı katı bir preparat (krem) biçimindedir ve yalnızca '
             '18 yaş üstü yetişkinler içindir.'],
            ['Kozmetik ve gıda sanayii',
             'International Journal of Toxicology’deki 2007 tarihli güvenlik '
             'değerlendirmesine göre biberden elde edilen bileşenler '
             'kozmetikte cilt bakım maddesi, haricî ağrı kesici, tatlandırıcı '
             've koku bileşeni olarak, %5’e varan derişimlerde kullanılır. '
             'Aynı rapor biberin ABD Gıda ve İlaç Dairesi tarafından gıdada '
             'kullanım için genel olarak güvenli kabul edildiğini aktarır.'],
        ],
        haz='Gıda olarak taze, kurutulmuş ya da sos hâlinde kullanılır; '
            'gıda kullanımı için bir doz tanımlanmamıştır. Tıbbi kullanım '
            'yalnızca haricendir ve EMA monografına göre şöyledir: ilaçlı '
            'yakı günde en fazla 1 kez, en az 4, en çok 12 saat süreyle '
            'uygulanır (22 x 14 cm’lik yakıda 11 mg, 12 x 18 cm’lik yakıda '
            '4,8 mg kapsaisinoit); yarı katı preparatlar (100 g’da 40–53 mg '
            'kapsaisinoit) günde 2–4 kez ince tabaka hâlinde sürülür. '
            '**Kullanım en çok 3 hafta sürer, ardından en az 2 hafta ara '
            'verilir.** Evde biberden hazırlanan karışımlar bu ürünlerin '
            'yerini tutmaz; kapsaisinoit miktarı bilinemez.',
        bilim='Kanıt biberin kendisinden çok etken maddesi kapsaisin '
              'üzerinedir ve haricen kullanımı ilgilendirir. EMA, bel ağrısı '
              'gibi kas ağrılarındaki kullanımı "yerleşik kullanım" sayacak '
              'kadar klinik veri bulunduğunu kabul etmiştir. Nöropatik ağrıda '
              'kullanılan **%8’lik kapsaisin yaması** ayrı bir ilaçtır: '
              'Cochrane’in 2017 tarihli derlemesi 8 çalışmayı (2488 '
              'katılımcı) incelemiş, zona sonrası sinir ağrısında 8 ve 12. '
              'haftalarda yama grubunda kontrol grubuna göre yaklaşık %10 '
              'daha fazla hastanın belirgin iyileşme bildirdiğini bulmuştur; '
              'kanıt kalitesi orta ile çok düşük arasında değişir. Ciddi '
              'istenmeyen olaylar yama (%3,5) ve kontrol (%3,2) gruplarında '
              'benzerdir. Bu yama biberden hazırlanan krem ve yakılardan '
              'yaklaşık 100 kat yoğundur ve yalnızca sağlık kuruluşunda '
              'uygulanır. Biberi yemekle bir hastalığın tedavi edildiğini '
              'gösteren klinik kanıt bu kaynaklarda yoktur.',
        kanit='klinik',
        guv='orta',
        guvNot='Gıda miktarlarında yaygın olarak tüketilir. Haricen '
               'kullanımda EMA monografı şu uyarıları verir: **göz çevresine '
               've mukozalara sürülmez; yaralı, tahriş olmuş ya da egzamalı '
               'cilde uygulanmaz**; uygulama yeri kaşınmaz; güneş, kızılötesi '
               'ışın, ısıtıcı yastık ve sıcak su gibi ek ısı kaynaklarından '
               'kaçınılır. Kızarıklık ve sıcaklık hissi beklenen etkilerdir; '
               'kurdeşen ya da su toplaması gibi aşırı duyarlılık tepkileri '
               'seyrektir ve görülürse tedavi hemen bırakılır. **18 yaş '
               'altında kullanımı önerilmez.** Gebelikte kullanım verisi '
               'yoktur; kapsaisin plasentayı geçer ve anne sütüne geçebilir, '
               'bu nedenle ancak yarar-risk değerlendirmesinden sonra '
               'kullanılır. 2007 tarihli güvenlik değerlendirmesi, bu türün '
               'meyve özütlerinin 200 mg/kg dozda farelerin tümünü '
               'öldürdüğünü ve ürünlerde aflatoksin bulaşması saptandığını '
               'bildirir; derişik özütler ağızdan alınmamalıdır.',
        etk=[
            ['Aynı bölgeye sürülen diğer haricî ürünler (ısıtıcı merhemler, '
             'ağrı kesici jeller)',
             'EMA monografına göre aynı yere aynı anda uygulanmamalıdır; '
             'etkileşim yakı çıkarıldıktan sonra 12 saate kadar '
             'görülebilir.'],
            ['Diğer ilaçlar — veri yok',
             'EMA monografı etkileşim çalışması yapılmadığını belirtir. '
             'Düzenli ilaç kullananlar haricî ürünü kullanmadan önce '
             'hekimine ya da eczacısına danışmalıdır.'],
        ],
        ilginc='Science’taki 2007 tarihli çalışmaya göre biber nişastasının '
               'izleri Bahamalar’dan Peru’ya yedi kazı alanında bulunmuştur; '
               'en eskisi 6000 yıllıktır. Bazı bölgelerde biber ve mısır, '
               'çömlek yapımından önce de birlikte tüketiliyordu.',
        ek=dict(
            mevsim='Molecules’taki 2017 tarihli çalışmada kapsaisinoit '
                   'miktarı meyve gelişiminin 12. ile 33. günleri arasında '
                   'belirgin biçimde artmış, 33. ile 40. günler arasında '
                   '%3,3 azalmıştır. Dayanak alınan kaynaklar Türkiye için '
                   'bir hasat takvimi vermez.',
            yetisme='Kew POWO’ya göre doğal yayılışı Meksika’nın güneyinden '
                    'tropikal Amerika’ya uzanır; çalı ya da yarı çalıdır ve '
                    'çoğunlukla mevsimsel kurak tropikal kuşakta yetişir. '
                    'Molecules’taki çalışmada bitkiler '
                    'serada yetiştirilmiştir.',
            yoresel='Dayanak alınan kaynaklarda Türkçe yöresel ad geçmez.',
            karisma='Acı biber (Capsicum annuum var. minimum) yakın bir '
                    'türdür ve bu sitede ayrı kaydı vardır; EMA monografı '
                    'ikisini aynı drog (Capsici fructus) altında toplar. Kew '
                    'POWO’nun notuna göre bazı kaynaklar Capsicum '
                    'frutescens’i Capsicum annuum’un içinde sayar.',
        ),
        ema=[('Capsici fructus',
              'https://www.ema.europa.eu/en/medicines/herbal/capsici-fructus')],
        kaynak=[
            ['Capsicum frutescens L., Plants of the World Online, Royal '
             'Botanic Gardens, Kew',
             POWO + '316959-2'],
            ['European Union herbal monograph on Capsicum annuum L. var. '
             'minimum (Miller) Heiser and small fruited varieties of '
             'Capsicum frutescens L., fructus, EMA/HMPC/674139/2013, 5 Mayıs '
             '2015',
             'https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-capsicum-annuum-l-var-minimum-miller-heiser-and-small-fruited-varieties-capsicum-frutescens-l-fructus_en.pdf'],
            ['L. Perry, R. Dickau, S. Zarrillo ve ark., “Starch fossils and '
             'the domestication and dispersal of chili peppers (Capsicum '
             'spp. L.) in the Americas”, Science 315(5814): 986–988, 2007',
             'https://pubmed.ncbi.nlm.nih.gov/17303753/'],
            ['S. Derry, A. S. Rice, P. Cole, T. Tan, R. A. Moore, “Topical '
             'capsaicin (high concentration) for chronic neuropathic pain in '
             'adults”, Cochrane Database of Systematic Reviews 2017(1): '
             'CD007393',
             'https://pubmed.ncbi.nlm.nih.gov/28085183/'],
            ['“Final report on the safety assessment of capsicum annuum '
             'extract, capsicum annuum fruit extract, capsicum annuum resin, '
             'capsicum annuum fruit powder, capsicum frutescens fruit, '
             'capsicum frutescens fruit extract, capsicum frutescens resin, '
             'and capsaicin”, International Journal of Toxicology 26 '
             '(Suppl 1): 3–106, 2007',
             'https://pubmed.ncbi.nlm.nih.gov/17365137/'],
            ['O. Fayos, A. C. de Aguiar, A. Jiménez-Cantizano ve ark., '
             '“Ontogenetic Variation of Individual and Total Capsaicinoids '
             'in Malagueta Peppers (Capsicum frutescens) during Fruit '
             'Maturation”, Molecules 22(5): 736, 2017',
             'https://pubmed.ncbi.nlm.nih.gov/28467391/'],
        ],
        rel=['acibiber', 'karabiber', 'patlican', 'zencefil'],
        en=dict(
            name='Chili pepper (Capsicum frutescens)',
            other='English chili pepper, bird pepper; in Brazil malagueta '
                  '(pimenta malagueta). Kew POWO gives the name as accepted; '
                  'some sources include the species in Capsicum annuum. The '
                  'part used is the ripe fruit. The EU monograph (Capsici '
                  'fructus) covers the small-fruited varieties of this '
                  'species together with Capsicum annuum var. minimum; the '
                  'hot pepper record on this site is for Capsicum annuum.',
            part='Ripe fruit (fresh or dried)',
            uses=[
                ['Neotropical America — among the oldest foods, with maize',
                 'A study published in the journal Science in 2007 '
                 'identified starch grains specific to the chili pepper '
                 'genus at seven excavation sites stretching from the '
                 'Bahamas to southern Peru. The oldest finds date to 6000 '
                 'years before present. According to the authors, maize and '
                 'chilies together formed a widespread food complex that in '
                 'some regions is older even than pottery. The finding is at '
                 'the level of the genus; it does not separate individual '
                 'species.'],
                ['Brazil — the malagueta pepper',
                 'A 2017 study in the journal Molecules examines Capsicum '
                 'frutescens under the name malagueta pepper. The '
                 'capsaicinoids that give the fruit its heat accumulate '
                 'during ripening; the main compound is capsaicin, the '
                 'second dihydrocapsaicin. Chili is a spice and vegetable '
                 'that has entered cuisines all over the world.'],
                ['Europe — externally for muscle pain',
                 'The EMA monograph accepts products prepared from the fruit '
                 'of the small-fruited varieties of this species and of '
                 'Capsicum annuum var. minimum, on the basis of '
                 'well-established use, **for the relief of muscle pain such '
                 'as low back pain**. The product takes the form of a '
                 'medicated plaster or a semi-solid preparation (cream) '
                 'applied to the skin, and is for adults over 18 only.'],
                ['The cosmetics and food industries',
                 'According to a 2007 safety assessment in the International '
                 'Journal of Toxicology, ingredients derived from capsicum '
                 'are used in cosmetics as skin-conditioning agents, '
                 'external analgesics, flavourings and fragrance components, '
                 'at concentrations of up to 5%. The same report notes that '
                 'capsicum is generally recognised as safe for use in food '
                 'by the US Food and Drug Administration.'],
            ],
            prep='As food it is used fresh, dried or as a sauce; no dose is '
                 'defined for food use. Medicinal use is external only and, '
                 'according to the EMA monograph, is as follows: a medicated '
                 'plaster is applied at most once a day, for at least 4 and '
                 'at most 12 hours (11 mg of capsaicinoids in the 22 x 14 cm '
                 'plaster, 4.8 mg in the 12 x 18 cm plaster); semi-solid '
                 'preparations (40–53 mg of capsaicinoids per 100 g) are '
                 'applied as a thin layer 2–4 times a day. **Use lasts at '
                 'most 3 weeks, followed by a break of at least 2 weeks.** '
                 'Mixtures made from chili at home are no substitute for '
                 'these products; their capsaicinoid content cannot be '
                 'known.',
            science='The evidence concerns capsaicin, the active substance, '
                    'more than the pepper itself, and it relates to external '
                    'use. The EMA has accepted that there are enough '
                    'clinical data to count the use in muscle pain such as '
                    'low back pain as "well-established use". The **8% '
                    'capsaicin patch** used in neuropathic pain is a '
                    'separate medicine: the 2017 Cochrane review examined 8 '
                    'studies (2488 participants) and found that in '
                    'postherpetic neuralgia, at 8 and 12 weeks, about 10% '
                    'more patients in the patch group than in the control '
                    'group reported marked improvement; the quality of the '
                    'evidence ranges from moderate to very low. Serious '
                    'adverse events were similar in the patch (3.5%) and '
                    'control (3.2%) groups. This patch is about 100 times '
                    'more concentrated than the creams and plasters made '
                    'from chili and is applied only in a healthcare setting. '
                    'These sources contain no clinical evidence that eating '
                    'chili treats a disease.',
            safety='It is widely consumed in food amounts. For external use '
                   'the EMA monograph gives these warnings: **it is not '
                   'applied near the eyes or to mucous membranes; it is not '
                   'applied to broken, irritated or eczematous skin**; the '
                   'application site is not scratched; additional sources '
                   'of heat such as sun, infrared radiation, heating pads '
                   'and warm water are avoided. Redness and a feeling of '
                   'warmth are expected effects; hypersensitivity reactions '
                   'such as hives or blistering are rare, and if they occur '
                   'treatment is stopped at once. **Use under the age of 18 '
                   'is not recommended.** There are no data on use in '
                   'pregnancy; capsaicin crosses the placenta and may pass '
                   'into breast milk, so it is used only after a '
                   'benefit-risk assessment. The 2007 safety assessment '
                   'reports that fruit extracts of this species killed all '
                   'mice at a dose of 200 mg/kg and that aflatoxin '
                   'contamination has been detected in products; '
                   'concentrated extracts should not be taken by mouth.',
            fact='According to the 2007 study in Science, traces of chili '
                 'starch have been found at seven excavation sites from the '
                 'Bahamas to Peru; the oldest is 6000 years old. In some '
                 'regions chili and maize were being eaten together even '
                 'before pottery was made.',
            season='In the 2017 study in Molecules, the capsaicinoid content '
                   'rose markedly between days 12 and 33 of fruit '
                   'development and fell by 3.3% between days 33 and 40. '
                   'The sources relied on here give no harvest calendar for '
                   'Türkiye.',
            habitat='According to Kew POWO its native range runs from '
                    'southern Mexico through tropical America; it is a shrub '
                    'or subshrub and grows mainly in the seasonally dry '
                    'tropical zone. In the study in Molecules the '
                    'plants were grown in a greenhouse.',
            local='The sources relied on here give no Turkish local name.',
            confusion='Hot pepper (Capsicum annuum var. minimum) is a '
                      'closely related species and has its own record on '
                      'this site; the EMA monograph brings the two together '
                      'under one herbal substance (Capsici fructus). '
                      'According to a note in Kew POWO, some sources include '
                      'Capsicum frutescens in Capsicum annuum.',
        ),
        etk_en=[
            ['Other external products applied to the same area (warming '
             'ointments, pain-relief gels)',
             'According to the EMA monograph they should not be applied to '
             'the same site at the same time; an interaction may occur up to '
             '12 hours after the plaster is removed.'],
            ['Other medicines — no data',
             'The EMA monograph states that no interaction studies have '
             'been performed. People on regular medication should consult '
             'their doctor or pharmacist before using the external '
             'product.'],
        ],
    ),

]

# arnavutbiberi çıkarıldı: katalogdaki 'acibiber' kaydı aynı EMA monografını (Capsici fructus, C. frutescens dahil) zaten kapsıyor; mükerrer olmasın.
Q = [q for q in Q if q['id'] != 'arnavutbiberi']
