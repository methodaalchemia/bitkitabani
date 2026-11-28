# Parti 009 (28 Kasım 2026): Anadolu'nun ballıbabagillerinden sekiz bitki.
#
# Kardeş tür denetimi (yordamın 3. adımı) bu partide üç adayı işaretledi;
# ikisi Eda'nın kararıyla partiden düştü:
#   · Bahçe nanesi (Mentha spicata) — katalogdaki `nane` kaydının `la` alanı
#     zaten 'Mentha × piperita, M. spicata', `diger` alanı zaten "Bahçe nanesi"
#     diyor. Önerilen Türkçe ad var olan bir kaydın takma adıydı. Yazılmadı.
#   · Büyük çiçekli adaçayı (Salvia tomentosa) — ölçütün üçünü de geçemedi:
#     monografı yok, dört künyesinin hepsi fitokimya/tüp içi, hikâyesi
#     katalogdaki `adacayi` (S. fruticosa) ile aynı. Şimdilik düştü.
#   · Misk adaçayı (Salvia sclarea) — KALDI. Monografı yok, ama kendi klinik
#     literatürü var (dört aromaterapi deneyi) ve katalogdaki hiçbir adaçayı
#     bunları paylaşmıyor; ayrıca kendi uçucu yağı ve kendi ticareti var.
# Düşenlerin yerine liste sırasındaki ilk iki işaretsiz Anadolu adayı alındı:
# mayasilotu (Ajuga chamaepitys) ve dagnanesi (Cyclotrichium niveum).
#
# Sekizinin de ne EMA'da ne TİTCK'de monografı vardır. Bu, iki resmî listeye
# tür düzeyinde bakılarak doğrulanmıştır: EMA'nın 206 satırlık bitkisel
# monograf tablosu (28 Kasım 2026'da indirildi) ve depodaki TİTCK derlemesi
# (143 monograf). Çıkan tek yakın eşleşmeler akrabalara aittir ve katalogda
# zaten kayıtlıdırlar: Salviae officinalis ve Salviae trilobae (EMA),
# Salvia triloba ve Mentha x piperita (TİTCK). Hiçbiri bu sekizin biri değil.
#
# Araç uyarısı: tools/kayit_iskeleti.py bu sekizin hepsinde "EMA: 1 eşleşme"
# yazdı. ema_index.json üretilmemiş olduğu için bu sayı anlamsızdır —
# eşleşmeler yukarıdaki tablodan tür düzeyinde elle doğrulandı ve hepsi boş
# çıktı. Kayıtlardaki monograf yokluğu cümlesi o doğrulamaya dayanır.
Q = [
    dict(
        yayin='2026-11-28',
        arsiv=True,
        id='aciyavsan',
        foto='Teucrium polium kz06.jpg',
        tr='Acı yavşan',
        la='Teucrium polium L.',
        taxon='Teucrium polium',
        fam='Lamiaceae (ballıbabagiller)',
        diger='İngilizce felty germander, poley germander. Türkçede acı '
              'yavşan, yavşan otu. **Bu türün ne Avrupa İlaç Ajansı’nda ne '
              'TİTCK’de monografı vardır** (iki listeye tür düzeyinde '
              'bakıldı). **Adın hangi bitkiyi gösterdiği bu kayıtta '
              'çözülmemiş bir sorundur:** Kew’in kontrol listesine '
              'göre kabul edilen *Teucrium polium*’un **doğal** '
              'yayılışı altı bölgedir ve **Türkiye bunların arasında '
              'yoktur** (Cezayir, Korsika, Fransa, Fas, İspanya, '
              'Tunus; Çekya-Slovakya aynı listede ama **sonradan '
              'gelme** olarak işaretlidir). Oysa bu adla yapılan '
              'etnobotanik ve klinik çalışmaların neredeyse tamamı '
              'Türkiye ve İran kaynaklıdır. **Dayanak alınan '
              'kaynaklar bu ikiliğe bir aday veriyor:** 2022 tarihli '
              'derleme türü "*Teucrium polium* L. (eş ad *Teucrium '
              'capitatum* L.)" diye verir, oysa Kew *T. capitatum* '
              'L.’yi **ayrı ve kabul edilmiş bir tür** sayar ve '
              'doğal yayılışını Türkiye dahil 34 bölge olarak '
              'gösterir. Yani Anadolu ve İran’da "acı yavşan" denen '
              'bitkilerin bir kısmı, botanik adlandırmada *T. '
              'polium* değil *T. capitatum* olabilir — iki kaynak bu '
              'noktada birbiriyle uyuşmuyor ve bu kayıt aralarında '
              'hüküm vermez. Aşağıdaki kullanım ve çalışma '
              'özetleri kaynaklarının kendi tür adlandırmasıyla '
              'aktarılmıştır; derlemenin aktardığı bazı '
              'çalışmaların *T. polium* ssp. *capitatum* '
              'materyaliyle yapıldığı da derlemenin kendisinde '
              'yazılıdır.',
        bolge=['anadolu'],
        kat=['sifa', 'zehir'],
        kisim='Çiçekli dallar ve yaprak',
        kul=[
            ['Geleneksel İran tıbbında — karın ağrısı, hazımsızlık, şeker',
             'Avicenna Journal of Phytomedicine’da 2022’de yayımlanan '
              'Bahramikia derlemesi, geleneksel İran tıbbında türün karın '
              'ağrısı, hazımsızlık ve tip 2 diyabet dahil birçok '
              'rahatsızlıkta kullanıldığını yazar. Derlemenin kendi '
              'sonucu, 2011–2020 arasındaki yüz kadar çalışmanın '
              'çoğunun antioksidan ve şeker düşürücü etkilere '
              'odaklandığıdır.'],
            ['Türkiye’de — halk arasında bildirilen kullanımlar',
             'Aynı derleme, Türkiye’den iki saha çalışmasını aktarır: '
              'Elazığ’da yüksek kolesterol, soğuk algınlığı ve grip '
              'için kullanıldığı; yaprağın şeker hastalığı, böbrek ve '
              'karaciğer rahatsızlıkları, mide ve bağırsak ağrısı ile '
              'basur için kullanıldığı bildirilmiştir. Edremit '
              'Körfezi’nde yapılan bir araştırmanın sonucu ise türün '
              'ticari amaçla yaygın biçimde toplandığıdır. '
              '**Bunlar halk kullanımı kayıtlarıdır, etkinlik kanıtı '
              'değildir** — ve yukarıda yazılan ad sorunu yüzünden '
              'bu kayıtlardaki bitkinin Kew’in kabul ettiği '
              '*T. polium* olduğu kesin değildir.'],
        ],
        haz='**Resmî bir monografta kabul edilmiş doz yoktur;** iki '
            'resmî listede de monografı bulunmadığı için kabul '
            'edilmiş bir ölçü, süre ya da üst sınır yoktur. Buna '
            'karşılık dayanak alınan kaynaklar insanda **denenmiş** '
            'üç ölçü bildirir; bunlar bir öneri değil, çalışmaların '
            'kendi tasarımıdır: Abadian 2016’da adetin ilk üç günü '
            'altı saatte bir 250 mg toz, iki döngü boyunca; Fallah '
            'Huseini 2024’te merhem günde iki kez, dört hafta, '
            'standart tedaviye ek olarak; 2022 derlemesinin '
            'aktardığı geleneksel kullanımda ise çiçekli dalların '
            'demlenmesiyle günde iki fincan, bir hafta boyunca '
            '(derlemenin andığı Polat ve Satıl 2012). **Bu ölçüler '
            'burada bir ev dozu olarak verilmemiştir** ve aşağıdaki '
            'güvenlik notu okunmadan hiçbiri kullanılmamalıdır: '
            'kaynakta bildirilen karaciğer hasarı, **yaklaşık bir '
            'aydan sonra** ortaya çıkan kolestatik hepatitle '
            'ilişkilendirilmiştir — yani bir ay bir üst sınır '
            'değil, zararın görülmeye başladığı eşiktir; dört '
            'haftalık denemenin bu eşiğin tam üzerinde olduğu '
            'görülmelidir.',
        bilim='Elimizdeki kaynaklarda **insanda yapılmış üç çalışma '
              'vardır, hepsi küçük ve hepsi tek merkezli.** '
              'Complementary Therapies in Clinical Practice’ta 2016’da '
              'yayımlanan Abadian çalışması üç kör, randomize bir '
              'denemedir: yetmiş öğrenci iki kola ayrılmış, bir kol '
              'adetin ilk üç günü altı saatte bir 250 mg *T. polium* '
              'tozu, öteki kol 250 mg mefenamik asit almış, ağrı '
              'şiddeti görsel analog ölçekle ölçülmüştür. **Bu '
              'denemede plasebo kolu yoktur** — karşılaştırma bir '
              'ilaçladır; sonuç, türün ağrı şiddetini azaltmakta '
              'mefenamik asit kadar etkili olduğudur ve iki kolda da '
              'yan etki bildirilmemiştir. **Dayanak alınan 2022 '
              'derlemesi bu denemeyi ilk yazarın adını yanlış '
              'yazarak ("Khadige 2016") ikinci kez aktarır ve ona '
              'adet kanamasının süresi ile miktarını azalttığını '
              'atfeder; birincil makalede böyle bir ölçüm yoktur, '
              'ölçülen tek şey ağrı şiddetidir.** Bu kayıt birincil '
              'makaleyi esas alır ve denemeyi bir kez sayar. '
              'International Journal of Lower Extremity Wounds’da '
              '2024’te yayımlanan Fallah Huseini çalışması, türden '
              'hazırlanan merhemin **standart tedaviye ek olarak** '
              'deriye uygulanmasının diyabetik ayak yaralarında '
              'iyileşmeyi hızlandırdığını bildirir. BMC Oral '
              'Health’te 2020’de yayımlanan Khoramian Tusi '
              'çalışması, randomize çapraz geçişli bir denemede '
              'ağızdaki *Streptococcus mutans* üzerindeki etkiyi '
              'ölçmüştür. '
              '**Geri kalan literatürün tamamı hayvan ya da tüp içi '
              'çalışmadır:** şeker düşürücü, kan yağı düşürücü ve '
              'kalp-damar etkileri sıçanlarda ölçülmüştür; '
              'Obstetrics & Gynecology Science’ta 2023’te yayımlanan '
              'Khosrowpour çalışması polikistik over üzerindeki '
              'etkiyi **letrozolle oluşturulmuş sıçan modelinde** '
              'ölçmüştür. BioFactors’ta 2021’de yayımlanan '
              'Rahmouni derlemesi türün tedavi çalışmalarını ve '
              'biyolojik özelliklerini derler; **derlemedir.** '
              'Bunlar insanda etki göstermez.',
        kanit='geleneksel',
        guv='yuksek',
        guvNot='**Bu cins karaciğer için tehlikelidir ve bu tür de o '
               'cinstendir.** Avicenna Journal of Phytomedicine’daki '
               '2022 derlemesi, *T. polium* dahil Teucrium türlerinin '
               'kemirgenlerde orta düzeyde karaciğer hasarı yaptığını '
               'yazar; ekstrenin toksik bileşenleri furan taşıyan '
               'diterpenoitlerdir ve derlemenin kendi ifadesiyle bunlar '
               '**yaklaşık bir ay sonra kolestatik hepatite yol '
               'açabilir.** Derleme ayrıca iki insan bulgusu aktarır: '
               'Lin ve arkadaşlarının 2019’da Yunanistan’dan gelen '
               '*T. polium*’un karaciğer hasarına yol açtığını '
               'bildirmesi, ve türün karaciğer hasarına (çoğu kez '
               'kolestatik bir imzayla) yol açabildiğinin '
               'bildirilmesi. Toksisite düzeneği, aşırı tepkin '
               'epoksitleri karaciğer hücresinde apoptoza yol açan '
               'furano neoklerodan diterpenoitler **teucrin A ve '
               'teuchamaedryn A**’ya bağlanmıştır (derlemenin '
               'andığı Vilas-Boas 2020). Bunlar, katalogdaki '
               '[[kisamahmutotu]] kaydında Fransa’nın 1992’de '
               'piyasadan çekilmesine yol açan bileşiklerin '
               'aynısıdır. **Gebelikte kullanılmamalıdır:** aynı '
               'derleme, Al-Qahdi ve arkadaşlarının 2019’da '
               'kadınların gebelikte bu bitkiyi almaktan kaçınması '
               'gerektiğini, çünkü bitkinin embriyonun erken '
               'evresinde çok toksik etkileri olabileceğini '
               'bildirdiğini aktarır. **Doğum sonrası dönem de '
               'ayrıca işaretlenmiştir:** aynı derleme, Dağ ve '
               'arkadaşlarının 2014’te türün karaciğer zehirleyici '
               'etkisi olabileceğini belirttiğini ve **gebelik ile '
               'doğum sonrası dönemdeki fizyolojik değişikliklerin '
               'bu zehirliliğin şiddetini artırabileceğini** '
               'yazdığını aktarır. Emzirme ve çocuklar için '
               'dayanak alınan kaynaklarda ayrı bir değerlendirme '
               'yoktur; bu bir güvenlik kaydı değil, bilginin '
               'yokluğudur.',
        ilginc='Aynı bitkinin hem şeker düşürücü diye içilmesi hem '
               'karaciğeri bozması bir çelişki gibi görünür, ama '
               'kaynaklar ikisini birlikte veriyor: 2022 derlemesinin '
               'kendi tablosunda "hepatotoksisite" başlığı altında '
               'sekiz çalışma, "karaciğer koruyucu" sonuçlar '
               'arasında ise ayrı çalışmalar sıralanır — bazı '
               'ekstrelerin sıçanlarda parasetamol hasarına karşı '
               'koruduğu, buna karşılık ekstredeki alkaloit '
               'kesiminin karaciğeri bozduğu bildirilmiştir. '
               'Yani zarar da yarar da bitkinin bütününde değil, '
               'hangi kesimin alındığında aranıyor. Bu, bir bitki '
               'çayında kimsenin denetleyemediği bir ayrımdır.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklarda Türkiye için bir toplama '
                   'takvimi verilmemiştir.',
            yetisme='Kew’in kayıtlarına göre kabul edilen türün '
                    '**doğal** yayılışı altı bölgedir: Cezayir, '
                    'Korsika, Fransa, Fas, İspanya ve Tunus — yani '
                    'batı Akdeniz; Çekya-Slovakya listede sonradan '
                    'gelme olarak işaretlidir. Türkiye bu listede '
                    'yoktur. Buna karşılık bu adla yürütülen saha '
                    'çalışmaları Türkiye ve İran’dandır ve '
                    'kaynakların eş ad saydığı *T. capitatum* '
                    'Kew’de Türkiye dahil 34 bölgede doğal '
                    'gösterilir; `diger` alanındaki ad sorununa '
                    'bakın.',
            yoresel='acı yavşan, yavşan otu',
            karisma='Aynı cinsten [[kisamahmutotu]] (*Teucrium '
                    'chamaedrys*) ile karışır ve **karışmanın '
                    'sonucu önemsiz değildir:** o türün çiçekli '
                    'dalları İtalya’da zehir sayılmış, Fransa’da '
                    '1992’de piyasadan çekilmiştir. İki türü '
                    'karaciğer açısından tehlikeli kılan bileşikler '
                    'aynıdır. Ayrıca "yavşan" adı Türkçede '
                    '*Artemisia* türleri (pelin) için de '
                    'kullanılır; bunlar ayrı bir cinstir ve '
                    'kısıtlamaları da ayrıdır.',
        ),
        kaynak=[
            ('Teucrium polium L., World Checklist of Vascular Plants, '
             'Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'),
            ('Teucrium capitatum L., World Checklist of Vascular '
             'Plants, Royal Botanic Gardens, Kew (ayrı ve kabul '
             'edilmiş tür; doğal yayılışı Türkiye dahil 34 bölge)',
             'https://powo.science.kew.org/'),
            ('S. Bahramikia, R. Yazdanparast, “Teucrium polium L: An '
             'updated review of phytochemicals and biological '
             'activities”, Avicenna Journal of Phytomedicine 12(3), 224–240, 2022 '
             '(tam metin PMC9482711 üzerinden okundu)',
             'https://pubmed.ncbi.nlm.nih.gov/36186937/'),
            ('K. Abadian ve ark., “Comparison the effect of mefenamic '
             'acid and Teucrium polium on the severity and systemic '
             'symptoms of dysmenorrhea”, Complementary Therapies in '
             'Clinical Practice 22, 2016',
             'https://pubmed.ncbi.nlm.nih.gov/26850798/'),
            ('H. Fallah Huseini ve ark., “Topical Administration of '
             'Teucrium polium on Diabetic Foot Ulcers Accelerates '
             'Healing: A Placebo-Controlled Randomized Clinical Trial”, '
             'International Journal of Lower Extremity Wounds, 2024 '
             '(künyede “Clinical Study”)',
             'https://pubmed.ncbi.nlm.nih.gov/34719966/'),
            ('S. Khoramian Tusi ve ark., “The effect of antimicrobial '
             'activity of Teucrium Polium on Oral Streptococcus Mutans: '
             'a randomized cross-over clinical trial study”, '
             'BMC Oral Health 20, 2020',
             'https://pubmed.ncbi.nlm.nih.gov/32357889/'),
            ('Z. Khosrowpour ve ark., “Beneficial effects of Teucrium '
             'polium hydroalcoholic extract on letrozole-induced '
             'polycystic ovary syndrome in rats”, Obstetrics & '
             'Gynecology Science, 2023',
             'https://pubmed.ncbi.nlm.nih.gov/36575561/'),
            ('F. Rahmouni ve ark., “Therapeutics studies and biological '
             'properties of Teucrium polium (Lamiaceae)”, BioFactors '
             '47(6), 2021',
             'https://pubmed.ncbi.nlm.nih.gov/34850466/'),
        ],
        rel=['kisamahmutotu', 'pelin'],
        en=dict(
            name='Felty germander',
            other='English felty germander, poley germander. Turkish acı '
                  'yavşan, yavşan otu. **Neither the European Medicines '
                  'Agency nor the Turkish agency has a monograph for this '
                  'species** (both lists were checked at species level). '
                  '**Which plant the name denotes is an unresolved '
                  'problem in this record:** according to Kew’s checklist '
                  'the **native** range of the accepted *Teucrium '
                  'polium* covers six regions, and **Türkiye is not '
                  'among them** (Algeria, Corsica, France, Morocco, '
                  'Spain, Tunisia; Czechia-Slovakia is on the same '
                  'list but marked **introduced**). Yet almost all '
                  'the ethnobotanical and clinical work carried out '
                  'under this name comes from Türkiye and Iran. '
                  '**The sources relied on here offer a candidate '
                  'for this discrepancy:** the 2022 review gives the '
                  'species as "*Teucrium polium* L. (syn *Teucrium '
                  'capitatum* L.)", whereas Kew treats *T. '
                  'capitatum* L. as a **separate, accepted species** '
                  'and gives its native range as 34 regions, Türkiye '
                  'included. So some of the plants called "acı '
                  'yavşan" in Anatolia and Iran may be, in botanical '
                  'naming, not *T. polium* but *T. capitatum* — the '
                  'two sources disagree at this point and this '
                  'record does not adjudicate between them. The '
                  'summaries below are given with their own sources’ '
                  'species naming; the review itself also states '
                  'that some of the studies it relays were done with '
                  '*T. polium* ssp. *capitatum* material.',
            part='Flowering branches and leaf',
            uses=[
                ['In traditional Iranian medicine — abdominal pain, '
                 'indigestion, diabetes',
                 'The Bahramikia review published in the Avicenna '
                  'Journal of Phytomedicine in 2022 writes that in '
                  'traditional Iranian medicine the species is used for '
                  'many conditions including abdominal pain, '
                  'indigestion and type 2 diabetes. The review’s own '
                  'conclusion is that most of the hundred or so studies '
                  'from 2011 to 2020 focused on antioxidant and '
                  'blood-sugar-lowering effects.'],
                ['In Türkiye — uses reported among the public',
                 'The same review relays two field studies from '
                  'Türkiye: that in Elazığ it is used for high '
                  'cholesterol, colds and flu; and that the leaf is '
                  'used for diabetes, kidney and liver complaints, '
                  'stomach and intestinal pain and haemorrhoids. The '
                  'result of a study in Edremit Bay was that the '
                  'species was extensively gathered for commercial '
                  'purposes. **These are records of folk use, not '
                  'evidence of efficacy** — and because of the naming '
                  'problem written above it is not certain that the '
                  'plant in these records is the *T. polium* Kew '
                  'accepts.'],
            ],
            prep='**No dose is accepted in an official monograph;** '
                 'because neither official list carries a monograph, '
                 'there is no accepted measure, duration or upper '
                 'limit. The sources relied on here do, however, '
                 'report three measures **tested** in humans; these '
                 'are not a recommendation but the studies’ own '
                 'designs: in Abadian 2016, 250 mg of powder every '
                 'six hours for the first three days of '
                 'menstruation, over two cycles; in Fallah Huseini '
                 '2024, an ointment twice daily for four weeks in '
                 'addition to standard treatment; and in the '
                 'traditional use relayed by the 2022 review, an '
                 'infusion of the flowering branches, one teacup '
                 'twice a day for one week (Polat and Satıl 2012, '
                 'cited by the review). **These measures are not '
                 'given here as a home dose**, and none should be '
                 'used without reading the safety note below: the '
                 'liver damage reported in the source is associated '
                 'with cholestatic hepatitis appearing **after about '
                 'a month** — so a month is not an upper limit but '
                 'the threshold at which harm begins to be seen, and '
                 'it should be noticed that the four-week trial sits '
                 'just above that threshold.',
            science='In the sources available to us there are **three '
                    'studies in humans, all small and all '
                    'single-centre.** The Abadian study published in '
                    'Complementary Therapies in Clinical Practice in '
                    '2016 is a triple-blind randomized trial: '
                    'seventy students were split into two arms, one '
                    'taking 250 mg of *T. polium* powder every six '
                    'hours for the first three days of menstruation '
                    'and the other 250 mg of mefenamic acid, with '
                    'pain severity measured on a visual analogue '
                    'scale. **There was no placebo arm in this '
                    'trial** — the comparison is against a drug; the '
                    'conclusion is that the species was as effective '
                    'as mefenamic acid in decreasing pain severity, '
                    'and no side effects were reported in either arm. '
                    '**The 2022 review relied on here relays this '
                    'same trial a second time under a misspelt first '
                    'author ("Khadige 2016") and attributes to it a '
                    'reduction in the duration and amount of '
                    'menstrual bleeding; the primary paper contains '
                    'no such measurement — the only thing measured '
                    'was pain severity.** This record follows the '
                    'primary paper and counts the trial once. The '
                    'Fallah Huseini study published in the '
                    'International Journal of Lower Extremity Wounds '
                    'in 2024 reports that an ointment made from the '
                    'species, applied to the skin **in addition to '
                    'standard treatment**, accelerated healing in '
                    'diabetic foot ulcers. The Khoramian Tusi study '
                    'published in BMC Oral Health in 2020 measured '
                    'the effect on oral *Streptococcus mutans* in a '
                    'randomized cross-over trial. '
                    '**All the remaining literature is '
                    'animal or in vitro:** blood-sugar-lowering, '
                    'lipid-lowering and cardiovascular effects were '
                    'measured in rats; the Khosrowpour study published '
                    'in Obstetrics & Gynecology Science in 2023 '
                    'measured the effect on polycystic ovary **in a '
                    'letrozole-induced rat model.** The Rahmouni '
                    'review published in BioFactors in 2021 '
                    'compiles therapeutic studies and biological '
                    'properties of the species; **it is a review.** '
                    'These show no effect in humans.',
            safety='**This genus is dangerous to the liver, and this '
                   'species belongs to that genus.** The 2022 review in '
                   'the Avicenna Journal of Phytomedicine writes that '
                   'species of the genus Teucrium, including *T. '
                   'polium*, cause moderate liver damage in rodents; '
                   'the toxic components of the extract are '
                   'furan-containing diterpenoids, and in the review’s '
                   'own words these **can lead to cholestatic hepatitis '
                   'after about a month.** The review also relays two '
                   'findings in humans: that Lin and colleagues in 2019 '
                   'reported that *T. polium* from Greece induced liver '
                   'injury, and that the species has been reported to '
                   'be able to cause liver injury, often with a '
                   'cholestatic signature. The mechanism of toxicity '
                   'has been attributed to the furano neoclerodane '
                   'diterpenoids **teucrin A and teuchamaedryn A**, '
                   'whose highly reactive epoxides induce apoptosis in '
                   'liver cells (Vilas-Boas 2020, cited by the review). '
                   'These are the same compounds that, in the '
                   '[[kisamahmutotu]] record in this catalogue, led '
                   'France to withdraw that species from the market in '
                   '1992. **It must not be used in pregnancy:** the '
                   'same review relays that Al-Qahdi and colleagues in '
                   '2019 reported that women should avoid taking this '
                   'plant during pregnancy, because it can have very '
                   'toxic effects on the early stage of the embryo. '
                   '**The postpartum period is also specifically '
                   'flagged:** the same review relays that Dağ and '
                   'colleagues in 2014 indicated the species has a '
                   'potential hepatotoxic effect and wrote that '
                   '**physiological changes during pregnancy and '
                   'the postpartum period may increase the severity '
                   'of such toxicity.** For breastfeeding and '
                   'children the sources relied on here contain no '
                   'separate assessment; that is an absence of '
                   'information, not a safety record.',
            fact='That the same plant is both drunk to lower blood sugar '
                 'and harmful to the liver looks like a contradiction, '
                 'but the sources give both together: in the 2022 '
                 'review’s own table eight studies are listed under '
                 '"hepatotoxicity", while separate studies appear among '
                 'the liver-protective results — some extracts were '
                 'reported to protect rats against paracetamol damage, '
                 'whereas the alkaloid fraction of the extract was '
                 'reported to harm the liver. So both the harm and the '
                 'benefit are sought not in the whole plant but in '
                 'which fraction is taken. In a herbal tea that is a '
                 'distinction no one can control.',
            season='The sources relied on here give no collection '
                   'calendar for Türkiye.',
            local='acı yavşan, yavşan otu',
            habitat='According to Kew’s records the **native** range '
                    'of the accepted species covers six regions: '
                    'Algeria, Corsica, France, Morocco, Spain and '
                    'Tunisia — the western Mediterranean; '
                    'Czechia-Slovakia is marked introduced on the '
                    'same list. Türkiye is not on it. The field '
                    'studies conducted under this name, by contrast, '
                    'are from Türkiye and Iran, and *T. capitatum*, '
                    'which the sources treat as a synonym, is shown '
                    'by Kew as native in 34 regions including '
                    'Türkiye; see the naming problem in the "other '
                    'names" field.',
            confusion='It is confused with [[kisamahmutotu]] '
                      '(*Teucrium chamaedrys*) of the same genus, and '
                      '**the consequence of that confusion is not '
                      'immaterial:** that species’ flowering tops were '
                      'classed as a poison in Italy and withdrawn from '
                      'the market in France in 1992. The compounds that '
                      'make both species dangerous to the liver are the '
                      'same. The Turkish name "yavşan" is also used for '
                      '*Artemisia* species (wormwood); those are a '
                      'separate genus with separate restrictions.',
        ),
    ),
    dict(
        yayin='2026-11-28',
        arsiv=True,
        id='kisamahmutotu',
        foto='Teucrium chamaedrys kz07.jpg',
        tr='Kısamahmut otu',
        la='Teucrium chamaedrys L.',
        taxon='Teucrium chamaedrys',
        fam='Lamiaceae (ballıbabagiller)',
        diger='İngilizce wall germander. Türkçede kısamahmut otu, '
              'mahmut otu, dalak otu. **Bu türün ne Avrupa İlaç '
              'Ajansı’nda ne TİTCK’de monografı vardır** (iki listeye '
              'tür düzeyinde bakıldı) — ama bu, "düzenlenmemiş" '
              'demek değildir: aşağıda yazıldığı gibi Fransa 1992’de '
              'bitkiyi piyasadan çektirmiş, İtalya Sağlık Bakanlığı '
              'ise çiçekli dallarını zehir saymıştır. Dayanak alınan '
              '2021 tarihli çalışma, bitkiyi *Teucrium chamaedrys* L. '
              'subsp. *chamaedrys* alt türü düzeyinde inceler.',
        bolge=['anadolu', 'avrupa'],
        kat=['sifa', 'zehir'],
        kisim='Çiçekli dallar ve yaprak — **kullanımı kısıtlanmış '
              'bir drogdur**',
        kul=[
            ['İçki ve baharat olarak — tarihsel kullanım',
             'Biomolecules dergisinde 2021’de yayımlanan Piccolella '
              'çalışması, bitkinin baharat olarak ve vermut ile başka '
              'likörlerin yapımında şaraba aromasını vermek için '
              'kullanıldığını yazar.'],
            ['Zayıflama kapsülü olarak — ve sonuçları',
             'Aynı çalışma, geçen yüzyılın 1980’lerinin ortasından '
              'başlayarak bitkinin bitki çayı poşetleri ve '
              '**zayıflamaya yönelik kapsüller** hâlinde '
              'hazırlandığını yazar. Bunun sonucu güvenlik notunda '
              'yazılıdır: elli yedi değil, **elliden fazla '
              'karaciğer zehirlenmesi bildirimi.** Bu kayıt bu '
              'kullanımı aktarır, önermez.'],
            ['Laboratuvarda — yapraktaki fenolleri zehirden ayırma '
             'denemesi',
             '2021 tarihli çalışmanın kendi amacı bir kullanım '
              'önerisi değil, tam tersidir: furan taşıyan '
              'neoklerodan bileşenlerinin zehirliliği yüzünden '
              'yasaklanmış olan bitkinin yaprağındaki fenollerden '
              'yararlanılıp yararlanılamayacağını sınamaktır. '
              'Biyoetkinlik güdümlü ayırmayla yedi kısmen '
              'saflaştırılmış ekstre elde edilmiştir. Bunlar '
              '**tüp içi** çalışmalardır ve bir kullanım izni '
              'değildir. Aynı çalışmanın andığı Antognoni 2012, '
              'uyarılmış hücre kültürlerinin bol miktarda '
              'teukriosit ürettiğini, ama **karaciğeri zehirleyen '
              'neoklerodan diterpenoitleri üretmediğini** '
              'bildirir — yani zehirsiz bir üretim yolu aranıyor.'],
        ],
        haz='**Bu bitki için verilecek bir hazırlama ölçüsü yoktur ve '
            'bu kayıt bir hazırlama tarifi vermez.** Resmî bir '
            'monografta kabul edilmiş doz bulunmadığı gibi, dayanak '
            'alınan kaynağa göre Fransa 1992’de bitkiyi piyasadan '
            'çektirmiş, İtalya Sağlık Bakanlığı ise çiçekli '
            'dallarını ve **ondan elde edilen bütün hazırlıkları '
            '(toz, ekstre, tentür vb.)** zehir saymıştır. '
            '2021 tarihli kaynağın kendi ifadesiyle Teucrium '
            'türlerinin, özellikle *T. chamaedrys*’in '
            'kullanılması yasaktır.',
        bilim='Elimizdeki kaynaklarda **insanda etkinlik için '
              'yapılmış hiçbir çalışma yoktur.** İnsana ait veriler '
              'etkinlik değil **zarar** verileridir ve güvenlik '
              'notunda yazılıdır. Veterinary Research Forum’da '
              '2020’de yayımlanan Özel çalışması türün ekstresinin '
              'endometriyotik odakların gerilemesi üzerindeki '
              'etkisini ölçmüştür; bu bir **sıçan** çalışmasıdır ve '
              'insanda etki göstermez. Natural Product Research’te '
              '2018’de yayımlanan Frezza çalışması iridoit '
              'glikozitleri ve polifenolik bileşikleri tanımlar; '
              'bir **fitokimya** çalışmasıdır. Biomolecules’deki '
              '2021 çalışmasının ölçümleri **tüp içidir.** Public '
              'Health Nutrition’da 2000’de yayımlanan Stickel '
              'derlemesi ile Presse Médicale’de 1994’te yayımlanan '
              'Larrey derlemesi, türü bitkisel ürünlerin karaciğer '
              'zehirliliği bağlamında ele alır. Natural Product '
              'Research’te 2022’de yayımlanan Sadeghi derlemesi '
              'ise Teucrium cinsinin fitokimyasını, '
              'etnofarmakolojisini ve biyolojik etkinliklerini '
              'topluca gözden geçirir; **cins düzeyinde bir '
              'derlemedir ve bulguları tek tek türlere ait '
              'değildir.**',
        kanit='geleneksel',
        guv='yuksek',
        guvNot='**Bu bitki iki Avrupa ülkesinde kısıtlanmıştır ve '
               'ölümle sonuçlanan bir vakası vardır.** Biomolecules '
               'dergisindeki 2021 tarihli Piccolella çalışmasının tam '
               'metni şunları yazar: bitkiye dayalı takviyelerin '
               'ardından **elliden fazla karaciğer zehirlenmesi '
               'bildirimi** kaydedilmiştir — başlıca hepatit ve '
               'karaciğer sirozu, **aralarında bir ani ölüm vakası '
               'da vardır.** Bu nedenle **Fransız Farmakovijilans '
               'Otoriteleri 1992’de bitkinin piyasadan '
               'çekilmesini zorunlu kılmıştır**; birkaç yıl sonra '
               '**İtalya Sağlık Bakanlığı bitkinin çiçekli '
               'dallarını ve ondan elde edilen bütün hazırlıkları '
               '(toz, ekstre, tentür vb.) zehir saymıştır.** '
               'Sorumlu bileşikler furan taşıyan neoklerodan '
               'diterpenoitlerdir: **teucrin A ve teuchamaedryn '
               'A.** Aynı kaynağın ifadesiyle bunlar karaciğer '
               'yetmezliğine yol açar ve Teucrium türlerinin, '
               'özellikle *T. chamaedrys*’in kullanılması '
               'yasaktır. Bu kısıtlama bu kayıtta '
               'yumuşatılmamıştır ve yumuşatılmamalıdır: '
               '"dikkatli kullanılır" demek kuralı '
               'değiştirmek olur. Gebelik, emzirme ve çocuklar '
               'için dayanak alınan kaynaklarda ayrı bir '
               'değerlendirme yoktur — kısıtlama zaten herkes '
               'için geçerlidir. Aynı cinsten [[aciyavsan]] '
               '(*T. polium*) için de aynı bileşikler '
               'bildirilmiştir.',
        ilginc='Vermutun acı tadını veren bitkilerden biri, '
               'otuz yıl sonra bir ilaç güvenliği dersine '
               'dönüştü. Dayanak alınan 2021 tarihli çalışmaya '
               'göre bitki yüzyıllarca baharat ve likör '
               'aroması olarak kullanıldı; zarar, 1980’lerin '
               'ortasında zayıflama kapsülü hâline getirilip '
               'günlük ve derişik biçimde alınmaya '
               'başlandığında göründü. Aynı yaprak, aynı '
               'bileşik — değişen şey miktar ve süreydi. '
               'Çalışmanın bugünkü amacı da buradan çıkıyor: '
               'yapraktaki fenolleri, karaciğeri bozan furanlı '
               'diterpenoitlerden ayırabilmek.',
        ek=dict(
            mevsim='**Toplanması önerilmez.** Dayanak alınan '
                   'kaynaklarda Türkiye için bir toplama takvimi '
                   'yoktur ve bitkinin kullanımı kısıtlanmıştır.',
            yetisme='Kew’in kayıtlarına göre yayılışı 39 bölgeyi '
                    'kapsar; Türkiye de bunların arasındadır. '
                    '2021 tarihli kaynak bitkiyi Akdeniz '
                    'bölgesine özgü, yaprak dökmeyen küçük bir '
                    'çalı olarak tanımlar.',
            yoresel='kısamahmut otu, mahmut otu, dalak otu',
            karisma='Aynı cinsten [[aciyavsan]] (*Teucrium '
                    'polium*) ile karışır; o türde de aynı '
                    'furanlı diterpenoitler bildirilmiştir, '
                    'yani karışmak riski azaltmaz. Adında '
                    '"mahmut" geçmesi bir bitki ailesi '
                    'göstermez.',
        ),
        kaynak=[
            ('Teucrium chamaedrys L., World Checklist of Vascular '
             'Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'),
            ('S. Piccolella ve ark., “Chemical Fractionation Joint to '
             'In-Mixture NMR Analysis for Avoiding the Hepatotoxicity '
             'of Teucrium chamaedrys L. subsp. chamaedrys”, '
             'Biomolecules 11(5): 690, 2021 (tam metin PMC8148020 '
             'üzerinden okundu)',
             'https://pubmed.ncbi.nlm.nih.gov/34063021/'),
            ('Ş. Özel ve ark., “The effectiveness of Teucrium '
             'chamaedrys L. extracts on endometriotic implant '
             'regression in rat endometriosis model”, Veterinary '
             'Research Forum 11(4), 2020',
             'https://pubmed.ncbi.nlm.nih.gov/33643581/'),
            ('C. Frezza ve ark., “Iridoid glycosides and polyphenolic '
             'compounds from Teucrium chamaedrys L.”, Natural Product '
             'Research 32(13), 1583–1589, 2018',
             'https://pubmed.ncbi.nlm.nih.gov/29058476/'),
            ('F. Stickel ve ark., “Hepatotoxicity of botanicals”, '
             'Public Health Nutrition 3(2), 2000',
             'https://pubmed.ncbi.nlm.nih.gov/10948380/'),
            ('D. Larrey, “[Liver involvement in the course of '
             'phytotherapy]”, Presse Médicale 23(15), 1994',
             'https://pubmed.ncbi.nlm.nih.gov/8072973/'),
            ('Z. Sadeghi ve ark., “A review of the phytochemistry, '
             'ethnopharmacology and biological activities of Teucrium '
             'genus”, Natural Product Research, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/34986708/'),
        ],
        rel=['aciyavsan'],
        en=dict(
            name='Wall germander',
            other='English wall germander. Turkish kısamahmut otu, '
                  'mahmut otu, dalak otu. **Neither the European '
                  'Medicines Agency nor the Turkish agency has a '
                  'monograph for this species** (both lists were '
                  'checked at species level) — but that does not mean '
                  '"unregulated": as written below, France forced the '
                  'plant off the market in 1992 and the Italian '
                  'Ministry of Health classed its flowering tops as a '
                  'poison. The 2021 source relied on here studies the '
                  'plant at the level of the subspecies *Teucrium '
                  'chamaedrys* L. subsp. *chamaedrys*.',
            part='Flowering branches and leaf — **this is a restricted '
                 'drug**',
            uses=[
                ['As a drink flavouring and spice — historical use',
                 'The Piccolella study published in Biomolecules in '
                  '2021 writes that the plant was used as a spice and '
                  'to impart its aroma to base wine in the production '
                  'of vermouth and other liqueurs.'],
                ['As a weight-loss capsule — and its consequences',
                 'The same study writes that from the mid-1980s of the '
                  'last century the plant was prepared as herbal tea '
                  'bags and **capsules for weight loss.** The '
                  'consequence is written in the safety note: **more '
                  'than fifty reports of liver toxicity.** This record '
                  'relays that use; it does not recommend it.'],
                ['In the laboratory — an attempt to separate the leaf’s '
                 'phenolics from the poison',
                 'The 2021 study’s own aim is not a recommendation to '
                  'use the plant but the opposite: to test whether the '
                  'phenolics in the leaf of a plant banned because of '
                  'the toxicity of its furan-containing neo-clerodane '
                  'constituents could still be exploited. Seven '
                  'partially purified extracts were obtained by '
                  'bioassay-guided fractionation. These are **in '
                  'vitro** studies and not a permission to use. '
                  'Antognoni 2012, cited by the same study, reports '
                  'that elicited cell cultures produce high amounts of '
                  'teucrioside but **not the hepatotoxic '
                  'neo-clerodane diterpenoids** — that is, a '
                  'non-toxic production route is being sought.'],
            ],
            prep='**There is no preparation measure to give for this '
                 'plant and this record gives no preparation '
                 'instructions.** Not only is no dose accepted in an '
                 'official monograph, but according to the source '
                 'relied on here France forced the plant off the '
                 'market in 1992 and the Italian Ministry of Health '
                 'classed its flowering tops, **as well as all '
                 'preparations obtained from it (powder, extract, '
                 'tincture, etc.), as a poison.** In the 2021 '
                 'source’s own words, Teucrium species, especially '
                 '*T. chamaedrys*, are prohibited to be used.',
            science='In the sources available to us there is **no study '
                    'of efficacy in humans at all.** The human data are '
                    'not about efficacy but about **harm**, and are '
                    'written in the safety note. The Özel study '
                    'published in Veterinary Research Forum in 2020 '
                    'measured the effect of the species’ extracts on '
                    'the regression of endometriotic implants; it is a '
                    '**rat** study and shows no effect in humans. The '
                    'Frezza study published in Natural Product '
                    'Research in 2018 characterises iridoid glycosides '
                    'and polyphenolic compounds; it is a '
                    '**phytochemistry** study. The measurements in the '
                    '2021 Biomolecules study are **in vitro.** The '
                    'Stickel review published in Public Health '
                    'Nutrition in 2000 and the Larrey review published '
                    'in La Presse Médicale in 1994 treat the species in '
                    'the context of the liver toxicity of herbal '
                    'products. The Sadeghi review published in '
                    'Natural Product Research in 2022 surveys the '
                    'phytochemistry, ethnopharmacology and '
                    'biological activities of the genus Teucrium as '
                    'a whole; **it is a genus-level review and its '
                    'findings do not belong to individual '
                    'species.**',
            safety='**This plant is restricted in two European '
                   'countries and has a case that ended in death.** The '
                   'full text of the 2021 Piccolella study in '
                   'Biomolecules writes the following: **more than '
                   'fifty reports of liver toxicity** were recorded '
                   'following supplementation based on the plant — '
                   'mainly hepatitis and liver cirrhosis, **including '
                   'a sudden death case.** For this reason **the '
                   'French Pharmacovigilance Authorities in 1992 '
                   'forced its withdrawal from the market**; some '
                   'years later **the Italian Ministry of Health '
                   'considered the plant’s flowering tops, as well as '
                   'all preparations obtained from it (powder, '
                   'extract, tincture, etc.), as a poison.** The '
                   'compounds responsible are furan-containing '
                   'neo-clerodane diterpenoids: **teucrin A and '
                   'teuchamaedryn A.** In the same source’s words '
                   'these cause liver failure, and Teucrium species, '
                   'especially *T. chamaedrys*, are prohibited to be '
                   'used. That restriction is not softened in this '
                   'record and must not be: writing "use with care" '
                   'would be changing the rule. For pregnancy, '
                   'breastfeeding and children the sources relied on '
                   'here contain no separate assessment — the '
                   'restriction already applies to everyone. The same '
                   'compounds have also been reported for '
                   '[[aciyavsan]] (*T. polium*) of the same genus.',
            fact='One of the plants that gave vermouth its bitter taste '
                 'became, thirty years later, a lesson in drug safety. '
                 'According to the 2021 source relied on here the '
                 'plant was used for centuries as a spice and liqueur '
                 'flavouring; the harm appeared when, in the '
                 'mid-1980s, it was turned into weight-loss capsules '
                 'and began to be taken daily and in concentrated '
                 'form. The same leaf, the same compound — what '
                 'changed was the amount and the duration. The '
                 'study’s present aim follows from this: to separate '
                 'the leaf’s phenolics from the furan-bearing '
                 'diterpenoids that harm the liver.',
            season='**Gathering is not advised.** The sources relied on '
                   'here give no collection calendar for Türkiye, and '
                   'use of the plant is restricted.',
            habitat='According to Kew’s records its range covers 39 '
                    'regions, Türkiye among them. The 2021 source '
                    'describes it as an evergreen small shrub native '
                    'to the Mediterranean region.',
            local='kısamahmut otu, mahmut otu, dalak otu',
            confusion='It is confused with [[aciyavsan]] (*Teucrium '
                      'polium*) of the same genus; the same '
                      'furan-bearing diterpenoids have been reported '
                      'in that species too, so confusing them does '
                      'not reduce the risk.',
        ),
    ),
    dict(
        yayin='2026-11-28', arsiv=True, id='dagcayistachys', foto='Stachys lavandulifolia, Nature of Iran.jpg',
        tr='Dağ çayı (tüylü)', la='Stachys lavandulifolia Vahl',
        taxon='Stachys lavandulifolia', fam='Lamiaceae (ballıbabagiller)',
        diger='İngilizce literatürde wood betony adıyla da anılır. '
              '**Bu türün ne Avrupa İlaç Ajansı’nda ne TİTCK’de '
              'monografı vardır** (iki listeye tür düzeyinde '
              'bakıldı). Türkçede "dağ çayı" adı birçok ayrı bitki '
              'için kullanıldığından burada "tüylü" ayırt edici '
              'olarak eklenmiştir; `karisma` alanına bakın.',
        bolge=['anadolu'], kat=['sifa'], kisim='Çiçekli dallar (toprak üstü kısım)',
        kul=[
            ['Geleneksel İran tıbbında — "marmazad"',
             'Iranian Red Crescent Medical Journal’da 2015’te '
              'yayımlanan Minae çalışması türü geleneksel İran '
              'tıbbındaki "marmazad" ile ilişkisi içinde ele alır. '
              'Bu, türün katalogdaki akrabalarından ayrı, **adı '
              'konmuş bir geleneğe ait** kendi kullanım '
              'hikâyesidir.'],
            ['Kadın sağlığında — İran’da yürütülen denemelerin konusu',
             'Dayanak alınan üç insan çalışmasının ikisi bu '
              'alandadır: adet sancısı ve polikistik over. '
              'Ayrıntısı ve sınırları `bilim` alanında yazılıdır.'],
        ],
        haz='Resmî bir monografta kabul edilmiş doz yoktur; iki '
            'resmî listede de monografı bulunmadığı için kabul '
            'edilmiş bir ölçü ya da süre yoktur. Dayanak alınan '
            'insan çalışmalarının ikisi kendi ölçüsünü bildirir ve '
            'bunlar bir öneri değil, çalışmaların tasarımıdır: '
            'Jalilian 2013’te toprak üstü kısım günde üç kez 5 '
            'gram, üç ay boyunca; Monji 2018’de ise '
            '"standardize edilmiş bir formülasyon" '
            '(randomize, çift kör, çapraz geçişli, plasebo '
            'kontrollü bir pilot çalışma, 29 kişi). **Monji '
            'formülasyonunun içeriği ve miktarı burada '
            'yazılmamıştır, çünkü o çalışmanın tam metni '
            'okunmamıştır** ve sayı taşıyan bir iddia özetten '
            'yazılmaz. Jalilian denemesinde bildirilen yan etki '
            'oranı için güvenlik notuna bakın.',
        bilim='Elimizdeki kaynaklarda **insanda yapılmış üç çalışma '
              'vardır ve hepsi İran’da, küçük gruplarda '
              'yürütülmüştür.** Journal of Alternative and '
              'Complementary Medicine’da 2018’de yayımlanan Monji '
              'çalışması türün standardize edilmiş bir '
              'formülasyonunun birincil adet sancısındaki etkisini '
              'ölçmüştür. Phytotherapy Research’te 2013’te '
              'yayımlanan Jalilian çalışması polikistik over '
              'sendromunda toprak üstü kısmın rolünü incelemiştir. '
              'Explore dergisinde 2023’te yayımlanan Jadidi '
              'çalışması acil sağlık teknisyenlerinde mesleki '
              'stres üzerindeki etkiyi ölçmüştür. JBRA Assisted '
              'Reproduction’da 2023’te yayımlanan Manouchehri '
              'sistematik derlemesi türü polikistik over ve '
              'bitkisel ürünler bağlamında anar; **derlemedir.** '
              'Basic and Clinical Neuroscience’ta 2022’de '
              'yayımlanan Behzadnia çalışması pentilentetrazolle '
              'oluşturulmuş nöbetler üzerindeki etkiyi **erkek '
              'farelerde** ölçmüş ve GABA ile opioit '
              'düzeneklerinin rolünü incelemiştir; insanda etki '
              'göstermez.',
        kanit='geleneksel', guv='orta',
        guvNot='⚠️ **Dayanak alınan insan çalışmalarından biri bu '
               'tür için bir yan etki sinyali bildirir.** '
               'Phytotherapy Research’te 2013’te yayımlanan Jalilian '
               'denemesi, polikistik overe bağlı anormal rahim '
               'kanaması olan 66 kadında türün toprak üstü kısmını '
               '(günde üç kez 5 gram, üç ay) medroksiprogesteron '
               'asetatla karşılaştırmıştır. Kanama örüntülerindeki '
               'düzelme iki kolda benzer bulunmuş, ama **yan etki '
               'bitki kolunda yüzde 45,5, ilaç kolunda yüzde 24,2 '
               'oranında görülmüştür** — yani bitki kolunda '
               'neredeyse iki katı. Çalışmanın kendi sonucu türün '
               'bir seçenek olarak kullanılabileceğidir; bu kayıt o '
               'sonucu değil, bildirilen yan etki oranını da '
               'okurun önüne koyar. Bunun dışında tür için '
               '**insanda yapılmış ayrı bir güvenlilik '
               'değerlendirmesi yoktur.** '
               'Phytotherapy Research’te 2021’de yayımlanan '
               'Bernstein derlemesi, geleneksel tıbbi bitkilerin '
               'gebelikte tüketilmesinin güvenli olup olmadığı '
               'sorusunu ele alır ve türü bu bağlamda anar; **bu '
               'bir derlemedir ve bu tür için gebelikte bir '
               'güvenlik kararı vermez.** Elimizdeki kaynaklarda '
               'emzirme, çocuklar ve ilaç etkileşimleri için ayrı '
               'bir değerlendirme bulunmamaktadır. Bu, bitkinin '
               'güvenli olduğu anlamına gelmez; bilginin '
               'yokluğudur. İnsan çalışmalarının üçü de kadın '
               'sağlığı ve stres alanında olduğu için, '
               'gebelikte kullanımın özellikle '
               'değerlendirilmemiş olması önemsiz değildir.',
        ilginc='Türkçede "dağ çayı" denen bitkilerin sayısı, bu '
               'adın neyi gösterdiğini tek başına belirsiz '
               'kılıyor: aynı ad Sideritis türleri için de, '
               'Stachys türleri için de kullanılıyor. Bu kayıttaki '
               'tür, üzerine insan çalışması yapılmış olanı — ama '
               'çalışmaların hepsi İran’dan geliyor, oysa bitkinin '
               'yayılışı Türkiye’yi de kapsıyor.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklarda Türkiye için bir '
                   'toplama takvimi verilmemiştir.',
            yetisme='Kew’in kayıtlarına göre doğal yayılışı beş '
                    'bölgedir: İran, Irak, Transkafkasya, '
                    'Türkmenistan ve Türkiye.',
            yoresel='dağ çayı; "dağ çayı" adı başka cinsler için de '
                    'kullanılır',
            karisma='**"Dağ çayı" adı Türkiye’de en çok Sideritis '
                    'türleri için kullanılır**, bu tür ise '
                    '*Stachys* cinsindendir — ayrı bir cinstir ve '
                    'üzerine yapılmış çalışmalar birbirine ait '
                    'değildir. Bu kayıttaki insan çalışmaları '
                    'yalnız *Stachys lavandulifolia* içindir. '
                    'Ayrıca [[dagnanesi]] (*Cyclotrichium '
                    'niveum*) da dağlardan toplanıp çay olarak '
                    'içilir ve o da ayrı bir cinstir.',
        ),
        kaynak=[
            ('Stachys lavandulifolia Vahl, World Checklist of Vascular '
             'Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'),
            ('F. Monji ve ark., “Therapeutic Effects of Standardized '
             'Formulation of Stachys lavandulifolia Vahl on Primary '
             'Dysmenorrhea”, Journal of Alternative and Complementary '
             'Medicine 24(11), 1092–1098, 2018 (randomize, çift kör, '
             'çapraz geçişli, plasebo kontrollü pilot çalışma)',
             'https://pubmed.ncbi.nlm.nih.gov/29741912/'),
            ('N. Jalilian ve ark., “Phytotherapeutic management of '
             'polycystic ovary syndrome: role of aerial parts of wood '
             'betony (Stachys lavandulifolia)”, Phytotherapy Research '
             '27(11), 2013',
             'https://pubmed.ncbi.nlm.nih.gov/23307315/'),
            ('A. Jadidi ve ark., “Effect of stachys lavandulifolia on '
             'occupational stress in emergency medical technicians”, '
             'Explore (NY), 2023',
             'https://pubmed.ncbi.nlm.nih.gov/37061348/'),
            ('B. Minae ve ark., “Stachys lavandulifolia Vahl. and its '
             'Relation With Marmazad Activities in Traditional '
             'Manuscripts”, Iranian Red Crescent Medical Journal '
             '17(11), 2015',
             'https://pubmed.ncbi.nlm.nih.gov/26734474/'),
            ('A. Manouchehri ve ark., “Polycystic ovaries and herbal '
             'remedies: A systematic review”, JBRA Assisted '
             'Reproduction 27(1), 2023',
             'https://pubmed.ncbi.nlm.nih.gov/35916457/'),
            ('N. Bernstein ve ark., “Is it safe to consume traditional '
             'medicinal plants during pregnancy?”, Phytotherapy '
             'Research 35(4), 2021',
             'https://pubmed.ncbi.nlm.nih.gov/33164294/'),
            ('H. Behzadnia ve ark., “Effect of Hydroalcoholic Extract '
             'of Stachys lavandulifolia on Pentylenetetrazole-induced '
             'Seizures in Male Mice: The Role of GABAergic and '
             'Opioidergic Systems”, Basic and Clinical Neuroscience '
             '13(1), 107–116, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/36589024/'),
        ],
        rel=['dagnanesi'],
        en=dict(
            name='Wood betony (woolly mountain tea)',
            other='Also called wood betony in the English literature. '
                  '**Neither the European Medicines Agency nor the '
                  'Turkish agency has a monograph for this species** '
                  '(both lists were checked at species level). Because '
                  'the Turkish name "dağ çayı" (mountain tea) is used '
                  'for many separate plants, "tüylü" (woolly) is added '
                  'here as a distinguishing word; see the confusion '
                  'field.',
            part='Flowering branches (aerial parts)',
            uses=[
                ['In traditional Iranian medicine — "marmazad"',
                 'The Minae study published in the Iranian Red '
                  'Crescent Medical Journal in 2015 treats the species '
                  'in relation to "marmazad" in traditional Iranian '
                  'medicine. This is its own history of use, '
                  '**belonging to a named tradition**, separate from '
                  'its relatives in this catalogue.'],
                ['In women’s health — the subject of trials conducted '
                 'in Iran',
                 'Two of the three human studies relied on here are in '
                  'this area: period pain and polycystic ovary. The '
                  'detail and the limits are written in the science '
                  'field.'],
            ],
            prep='No dose is accepted in an official monograph; '
                 'because neither official list carries a monograph, '
                 'there is no accepted measure or duration. Two of '
                 'the human studies relied on here report their own '
                 'measure, and these are not a recommendation but '
                 'the studies’ designs: in Jalilian 2013 the aerial '
                 'parts at 5 g three times a day for three months; '
                 'in Monji 2018 a "standardized formulation" (a '
                 'randomized, double-blind, crossover, '
                 'placebo-controlled pilot study in 29 people). '
                 '**The content and amount of the Monji formulation '
                 'are not written here, because the full text of '
                 'that study was not read** and a claim carrying a '
                 'number is not written from an abstract. For the '
                 'adverse-effect rate reported in the Jalilian '
                 'trial see the safety note.',
            science='In the sources available to us there are **three '
                    'studies in humans, all conducted in Iran in small '
                    'groups.** The Monji study published in the Journal '
                    'of Alternative and Complementary Medicine in 2018 '
                    'measured the effect of a standardized formulation '
                    'of the species in primary dysmenorrhoea. The '
                    'Jalilian study published in Phytotherapy Research '
                    'in 2013 examined the role of the aerial parts in '
                    'polycystic ovary syndrome. The Jadidi study '
                    'published in Explore in 2023 measured the effect '
                    'on occupational stress in emergency medical '
                    'technicians. The Manouchehri systematic review '
                    'published in JBRA Assisted Reproduction in 2023 '
                    'mentions the species in the context of polycystic '
                    'ovary and herbal remedies; **it is a review.** '
                    'The Behzadnia study published in Basic and '
                    'Clinical Neuroscience in 2022 measured the '
                    'effect on pentylenetetrazole-induced seizures '
                    '**in male mice** and examined the role of the '
                    'GABAergic and opioidergic systems; it shows no '
                    'effect in humans.',
            safety='⚠️ **One of the human studies relied on here '
                   'reports an adverse-effect signal for this '
                   'species.** The Jalilian trial published in '
                   'Phytotherapy Research in 2013 compared the '
                   'species’ aerial parts (5 g three times a day for '
                   'three months) against medroxyprogesterone '
                   'acetate in 66 women with abnormal uterine '
                   'bleeding due to polycystic ovary syndrome. The '
                   'improvement in bleeding patterns was similar in '
                   'both arms, but **adverse effects were observed '
                   'in 45.5 per cent of the herb arm against 24.2 '
                   'per cent of the drug arm** — nearly twice as '
                   'often in the herb arm. The study’s own '
                   'conclusion is that the species may be used as an '
                   'alternative; this record puts not that '
                   'conclusion but the reported adverse-effect rate '
                   'in front of the reader as well. Beyond this '
                   'there is **no separate safety assessment in '
                   'humans** for the species. The '
                   'Bernstein review published in Phytotherapy '
                   'Research in 2021 addresses the question of whether '
                   'traditional medicinal plants are safe to consume '
                   'during pregnancy and mentions the species in that '
                   'context; **it is a review and does not give a '
                   'safety decision for this species in pregnancy.** '
                   'In the sources available to us there is no '
                   'separate assessment for breastfeeding, children or '
                   'drug interactions. That does not mean the plant is '
                   'safe; it is an absence of information. Since all '
                   'three human studies are in women’s health and '
                   'stress, the fact that use in pregnancy has not '
                   'specifically been assessed is not immaterial.',
            fact='The number of plants called "dağ çayı" (mountain '
                 'tea) in Turkish makes the name alone ambiguous: it '
                 'is used for Sideritis species and for Stachys '
                 'species alike. The species in this record is the one '
                 'that has had human studies done on it — but all the '
                 'studies come from Iran, even though the plant’s '
                 'range includes Türkiye.',
            season='The sources relied on here give no collection '
                   'calendar for Türkiye.',
            habitat='According to Kew’s records its natural range '
                    'covers five regions: Iran, Iraq, Transcaucasia, '
                    'Turkmenistan and Türkiye.',
            local='dağ çayı; the name "dağ çayı" is also used for '
                  'other genera',
            confusion='**In Türkiye the name "dağ çayı" is most often '
                      'used for Sideritis species**, whereas this '
                      'species belongs to the genus *Stachys* — a '
                      'separate genus, and studies done on one do not '
                      'belong to the other. The human studies in this '
                      'record are for *Stachys lavandulifolia* only. '
                      '[[dagnanesi]] (*Cyclotrichium niveum*) is also '
                      'gathered in the mountains and drunk as a tea, '
                      'and it too is a separate genus.',
        ),
    ),
    dict(
        yayin='2026-11-28', arsiv=True, id='calba', foto='',
        tr='Çalba', la='Phlomis grandiflora H.S.Thomps.',
        taxon='Phlomis grandiflora', fam='Lamiaceae (ballıbabagiller)',
        diger='Türkçede çalba, şalba, ayı kulağı. **Bu türün ne '
              'Avrupa İlaç Ajansı’nda ne TİTCK’de monografı vardır** '
              '(iki listeye tür düzeyinde bakıldı). Kew’in '
              'kayıtlarına göre doğal yayılışı yalnız iki bölgedir — '
              'Türkiye ve Doğu Ege adaları — yani **neredeyse '
              'Türkiye’ye özgü bir bitkidir.**',
        bolge=['anadolu'], kat=['sifa'], kisim='Yaprak',
        kul=[
            ['Halk hekimliğinde — Muğla’dan bir saha kaydı',
             'Journal of Ethnopharmacology’de 2013’te yayımlanan '
              'Gürdal çalışması Marmaris (Muğla) yöresinin tıbbi '
              'bitkileri üzerine bir etnobotanik araştırmadır ve '
              'türü bu derlemede anar. **Bu bir halk kullanımı '
              'kaydıdır, etkinlik kanıtı değildir;** muhbir adı ya '
              'da köy adı bu kayda yazılmamıştır.'],
            ['Mide yarası üzerine bir hayvan ölçümü',
             'Journal of Ethnopharmacology’de 2003’te yayımlanan '
              'Gürbüz çalışması, Türkiye’de halk ilacı olarak '
              'kullanılan bazı bitkilerin mide yarası karşıtı '
              'etkinliğini ölçmüş ve türü bu bitkiler arasında ele '
              'almıştır. **Bu bir hayvan çalışmasıdır** ve insanda '
              'etki göstermez.'],
        ],
        haz='Resmî bir monografta kabul edilmiş doz yoktur; iki '
            'resmî listede de monografı bulunmadığı için kabul '
            'edilmiş bir ölçü, süre ya da üst sınır yoktur. '
            'Dayanak alınan kaynaklarda insanda kullanım için bir '
            'ölçü verilmemiştir.',
        bilim='Elimizdeki kaynaklarda **insanda yapılmış hiçbir '
              'çalışma yoktur.** En sağlam veri 2003 tarihli mide '
              'yarası ölçümüdür ve o bir **hayvan** çalışmasıdır. '
              '2013 tarihli çalışma bir **etnobotanik saha '
              'çalışmasıdır** ve bitkinin ne için kullanıldığını '
              'kaydeder, işe yarayıp yaramadığını ölçmez. Chemistry & '
              'Biodiversity’de 2022’de yayımlanan Koca-Caliskan '
              'çalışması türü bakır nanoçiçeklerin sentezinde '
              'kullanır; bu bir **malzeme kimyası** çalışmasıdır '
              've bir sağlık iddiası taşımaz.',
        kanit='geleneksel', guv='orta',
        guvNot='Dayanak alınan kaynaklarda bu tür için **insanda '
               'yapılmış bir güvenlilik değerlendirmesi yoktur** ve '
               'gebelik, emzirme, çocuklar ile ilaç etkileşimleri '
               'için ayrı bir değerlendirme bulunmamaktadır. '
               'Bu, bitkinin güvenli olduğu anlamına gelmez; '
               'bilginin yokluğudur. Bitkinin yayılışı çok dar '
               'olduğu için (Kew’e göre yalnız Türkiye ve Doğu Ege '
               'adaları), **yabandan toplamanın koruma açısından '
               'sakıncası ayrıca düşünülmelidir;** dayanak alınan '
               'kaynaklarda türün koruma durumunu veren bir '
               'değerlendirme yoktur.',
        ilginc='Neredeyse yalnız Türkiye’de yetişen bir bitkinin '
               'bilimsel izi, üzerine yapılmış bir sağlık '
               'çalışmasından değil, bir malzeme kimyası '
               'çalışmasından geçiyor: 2022’de tür, bakır '
               'nanoçiçeklerin sentezinde bitki kaynağı olarak '
               'kullanılmış. Bu, dar yayılışlı Anadolu '
               'bitkilerinin ne kadar az çalışıldığını '
               'gösteriyor — kayıttaki üç künyeden yalnız biri '
               'bitkinin kendi kullanımına bakıyor.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklarda Türkiye için bir '
                   'toplama takvimi verilmemiştir.',
            yetisme='Kew’in kayıtlarına göre doğal yayılışı iki '
                    'bölgedir: Türkiye ve Doğu Ege adaları. Bu '
                    'kadar dar bir yayılış türü neredeyse '
                    'Türkiye’ye özgü kılar.',
            yoresel='çalba, şalba, ayı kulağı',
            karisma='Aynı cinsten başka Phlomis türleri Türkiye’de '
                    'de bulunur ve benzer adlarla anılır; bir türün '
                    'üzerine yapılan çalışma akrabasına ait '
                    'değildir. "Ayı kulağı" adı Türkçede '
                    'sığırkuyruğu (*Verbascum*) için de '
                    'kullanılır; o ayrı bir familyadandır.',
        ),
        kaynak=[
            ('Phlomis grandiflora H.S.Thomps., World Checklist of '
             'Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'),
            ('B. Gürdal, S. Kültür, “An ethnobotanical study of '
             'medicinal plants in Marmaris (Muğla, Turkey)”, Journal '
             'of Ethnopharmacology 146(1), 2013',
             'https://pubmed.ncbi.nlm.nih.gov/23261486/'),
            ('I. Gürbüz ve ark., “Anti-ulcerogenic activity of some '
             'plants used as folk remedy in Turkey”, Journal of '
             'Ethnopharmacology 88(1), 2003',
             'https://pubmed.ncbi.nlm.nih.gov/12902057/'),
            ('U. Koca-Caliskan ve ark., “Synthesis and '
             'Characterization of Copper-Nanoflowers with the '
             'Utilization of Medicinal Plant Extracts”, Chemistry & '
             'Biodiversity 19(11), e202200476, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/36149402/'),
        ],
        rel=['mayasilotu'],
        en=dict(
            name='Large-flowered phlomis',
            other='Turkish çalba, şalba, ayı kulağı. **Neither the '
                  'European Medicines Agency nor the Turkish agency '
                  'has a monograph for this species** (both lists '
                  'were checked at species level). According to Kew’s '
                  'records its natural range covers only two regions '
                  '— Türkiye and the East Aegean Islands — making it '
                  '**very nearly endemic to Türkiye.**',
            part='Leaf',
            uses=[
                ['In folk medicine — a field record from Muğla',
                 'The Gürdal study published in the Journal of '
                  'Ethnopharmacology in 2013 is an ethnobotanical '
                  'survey of the medicinal plants of the Marmaris '
                  '(Muğla) district and mentions the species in that '
                  'survey. **This is a record of folk use, not '
                  'evidence of efficacy;** no informant’s name or '
                  'village name is written into this record.'],
                ['An animal measurement on gastric ulcer',
                 'The Gürbüz study published in the Journal of '
                  'Ethnopharmacology in 2003 measured the '
                  'anti-ulcerogenic activity of some plants used as '
                  'folk remedies in Turkey and included the species '
                  'among them. **This is an animal study** and shows '
                  'no effect in humans.'],
            ],
            prep='No dose is accepted in an official monograph; '
                 'because neither official list carries a monograph, '
                 'there is no accepted measure, duration or upper '
                 'limit. The sources relied on here give no measure '
                 'for use in humans.',
            science='In the sources available to us there is **no '
                    'study in humans at all.** The soundest datum is '
                    'the 2003 gastric-ulcer measurement, and that is '
                    'an **animal** study. The 2013 study is an '
                    '**ethnobotanical survey** and records what the '
                    'plant is used for, not whether it works. The '
                    'Koca-Caliskan study published in Chemistry & '
                    'Biodiversity in 2022 uses the species in the '
                    'synthesis of copper nanoflowers; that is a '
                    '**materials chemistry** study and carries no '
                    'health claim.',
            safety='In the sources relied on here there is **no safety '
                   'assessment in humans** for this species, and no '
                   'separate assessment for pregnancy, '
                   'breastfeeding, children or drug interactions. '
                   'That does not mean the plant is safe; it is an '
                   'absence of information. Because the plant’s range '
                   'is very narrow (according to Kew only Türkiye and '
                   'the East Aegean Islands), **the conservation '
                   'implications of wild gathering should also be '
                   'considered;** the sources relied on here contain '
                   'no assessment giving the species’ conservation '
                   'status.',
            fact='The scientific trace of a plant that grows almost '
                 'only in Türkiye runs not through a health study but '
                 'through a materials chemistry one: in 2022 the '
                 'species was used as a plant source in the synthesis '
                 'of copper nanoflowers. That shows how little '
                 'narrowly distributed Anatolian plants have been '
                 'studied — of the three citations in this record, '
                 'only one looks at the plant’s own use.',
            season='The sources relied on here give no collection '
                   'calendar for Türkiye.',
            habitat='According to Kew’s records its natural range '
                    'covers two regions: Türkiye and the East Aegean '
                    'Islands. A range this narrow makes the species '
                    'very nearly endemic to Türkiye.',
            local='çalba, şalba, ayı kulağı',
            confusion='Other Phlomis species of the same genus also '
                      'occur in Türkiye and go by similar names; a '
                      'study done on one species does not belong to '
                      'its relative. The Turkish name "ayı kulağı" is '
                      'also used for mullein (*Verbascum*), which is '
                      'in a separate family.',
        ),
    ),
    dict(
        yayin='2026-11-28', arsiv=True, id='miskadacayi', foto="Salvia sclarea 'Vatican White' (clary sage) (SaatPilot).jpg",
        tr='Misk adaçayı', la='Salvia sclarea L.',
        taxon='Salvia sclarea', fam='Lamiaceae (ballıbabagiller)',
        diger='İngilizce clary sage, clary. Türkçede misk adaçayı, '
              'misk otu. **Bu türün ne Avrupa İlaç Ajansı’nda ne '
              'TİTCK’de monografı vardır** (iki listeye tür düzeyinde '
              'bakıldı). **Katalogdaki adaçayı kayıtlarının '
              'monografları bu türe ait değildir:** EMA’nın adaçayı '
              'monografları *Salvia officinalis* (bkz. '
              '[[tibbiadacayi]]) ve *Salviae trilobae* = *S. '
              'fruticosa* (bkz. [[adacayi]]) içindir, TİTCK’nin '
              'adaçayı monografı ise *Salvia triloba* içindir. '
              'Bu tür o monografların hiçbirinin kapsamında '
              'değildir.',
        bolge=['anadolu'], kat=['sifa', 'tutsu'],
        kisim='Çiçekli dallar; çiçekten damıtılan uçucu yağ',
        kul=[
            ['Parfümeride — kendi ticareti olan bir hammadde',
             'Advances in Biochemical Engineering/Biotechnology’de '
              '2015’te yayımlanan Zerbe derlemesi, ambroksit ile '
              'ilgili diterpenoit koku bileşiklerinin sentetik '
              'biyolojisinde kullanılan enzimleri ele alır; bu '
              'bileşiklerin çıkış maddesi türün verdiği '
              '**sklareol**dür. Frontiers in Pharmacology’de '
              '2022’de yayımlanan Zhou derlemesi sklareolün '
              'biyoetkinliklerini derler. Bu, türü katalogdaki '
              'öteki adaçaylarından ayıran **kendi ürünü ve '
              'kendi ticaretidir;** ambroksit parfümeride '
              'amber yerine kullanılır.'],
            ['Aromaterapide — kokusunun denendiği insan çalışmaları',
             'Türün uçucu yağı dört insan çalışmasında '
              'denenmiştir; ayrıntısı ve **önemli sınırları** '
              '`bilim` alanında yazılıdır.'],
            ['Uçucu yağın laboratuvar ölçümleri',
             'International Journal of Molecular Sciences’ta '
              '2023’te yayımlanan Kačániová çalışması uçucu '
              'yağın kimyasal bileşimini ve biyolojik '
              'etkinliklerini ölçmüştür. Plants dergisinde aynı '
              'yıl yayımlanan Ben Akacha çalışması *S. '
              'officinalis* ile *S. sclarea* uçucu yağlarını '
              'karşılaştırmalı olarak inceler. Phytochemistry’de '
              '1994’te yayımlanan Ulubelen çalışması türün '
              'terpenoitlerini tanımlar. Bunlar **tüp içi ve '
              'fitokimya** çalışmalarıdır.'],
        ],
        haz='Resmî bir monografta kabul edilmiş doz yoktur; iki resmî '
            'listede de monografı bulunmadığı için kabul edilmiş bir '
            'ölçü, süre ya da üst sınır yoktur. **Uçucu yağ derişik '
            'bir üründür ve dayanak alınan insan çalışmalarında '
            'seyreltilerek, deriye masajla ya da koklatılarak '
            'kullanılmıştır — ağızdan alınmamıştır.** Bu '
            'çalışmalarda kullanılan karışım oranları burada '
            'yazılmamıştır, çünkü çalışmaların tam metinleri '
            'okunmamıştır ve sayı taşıyan bir iddia özetten '
            'yazılmaz.',
        bilim='Elimizdeki kaynaklarda **insanda yapılmış dört '
              'çalışma vardır, ama hepsinin ortak ve ağır bir '
              'sınırı var: üçünde tür tek başına değil, başka '
              'uçucu yağlarla karıştırılarak ve masaj gibi bir '
              'uygulamayla birlikte denenmiştir — bu yüzden '
              'görülen etki bu türe atfedilemez.** Journal of '
              'Alternative and Complementary Medicine’da 2013’te '
              'yayımlanan Seol çalışması bir randomize kontrollü '
              'denemedir ve *Salvia sclarea* ile *Lavandula '
              'angustifolia*’nın **birbirinden farklı** etkilerini '
              'karşılaştırır; bu, türü tek başına ele alan '
              'çalışmaya en yakın olanıdır. Journal of '
              'Alternative and Complementary Medicine’da 2006’da '
              'yayımlanan Han çalışması üniversite '
              'öğrencilerinde adet sancısında aromaterapiyi '
              'plasebo kontrollü olarak denemiştir. Journal of '
              'Obstetrics and Gynaecology Research’te 2012’de '
              'yayımlanan Ou çalışması adet sancısında aromatik '
              'uçucu yağ masajını değerlendirmiştir. Journal of '
              'Alternative and Complementary Medicine’da 2017’de '
              'yayımlanan Kao çalışması aromaterapi ile '
              'akupressür masajını yaşam kalitesi açısından '
              'karşılaştırmıştır. Natural Product '
              'Communications’ta 2009’da yayımlanan Setzer '
              'derlemesi uçucu yağları ve kaygı giderici '
              'aromaterapiyi ele alır; **derlemedir.** '
              'Geri kalan kaynaklar **tüp içi ve fitokimya** '
              'çalışmalarıdır.',
        kanit='geleneksel', guv='orta',
        guvNot='Dayanak alınan kaynaklarda bu tür için **insanda '
               'yapılmış bir güvenlilik değerlendirmesi yoktur** ve '
               'gebelik, emzirme, çocuklar ile ilaç etkileşimleri '
               'için ayrı bir değerlendirme bulunmamaktadır; bu, '
               'bilginin yokluğudur. **Katalogdaki adaçayı '
               'kayıtlarının güvenlik kuralları bu türe ait '
               'değildir:** adaçayı için yazılan tuyon kısıtlamaları '
               '*Salvia officinalis* ve *S. fruticosa* '
               'monograflarından gelir, bu türün monografı yoktur ve '
               'elimizdeki kaynaklarda bu tür için tuyon içeriğine '
               'dayalı bir sınır verilmemiştir — bu, "bu türde tuyon '
               'sorunu yoktur" demek değildir, ölçülmemiş demektir. '
               'Uçucu yağ derişik bir üründür; dayanak alınan insan '
               'çalışmalarında seyreltilerek ve deri ya da koku '
               'yoluyla kullanılmıştır, ağızdan alınmamıştır.',
        ilginc='Bu türün en sağlam izi tıpta değil parfümeride: '
               'verdiği sklareol, amberin yerine kullanılan '
               'ambroksitin çıkış maddesi, ve 2015 tarihli '
               'derlemenin konusu bu dönüşümü enzimlerle '
               'yapabilmek. Yani bitkinin kataloga kendi '
               'kaydıyla girmesinin sebebi bir şifa iddiası '
               'değil, kendine ait bir sanayi.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklarda Türkiye için bir '
                   'toplama takvimi verilmemiştir.',
            yetisme='Kew’in kayıtlarına göre yayılışı 52 bölgeyi '
                    'kapsar; Türkiye de bunların arasındadır.',
            yoresel='misk adaçayı, misk otu',
            karisma='**Katalogdaki öteki Salvia kayıtlarıyla karışır ve '
                    'karışmanın sonucu güvenlik kuralının yanlış '
                    'türe geçmesidir:** [[tibbiadacayi]] (*S. '
                    'officinalis*), [[adacayi]] (*S. fruticosa*), '
                    '[[biberiye]] (*S. rosmarinus*), [[akadacayi]] '
                    '(*S. apiana*), [[chia]] (*S. hispanica*) ve '
                    '[[salviadivinorum]] (*S. divinorum*) ve aynı '
                    'partide yazılan [[kurtreyhani]] (*S. '
                    'multicaulis*). Bir türün monografı ve '
                    'kısıtlamaları akrabasına ait değildir.',
        ),
        kaynak=[
            ('Salvia sclarea L., World Checklist of Vascular Plants, '
             'Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'),
            ('G. H. Seol ve ark., “Randomized controlled trial for '
             'Salvia sclarea or Lavandula angustifolia: differential '
             'effects on blood pressure in female patients with '
             'urinary incontinence undergoing urodynamic '
             'examination”, Journal of Alternative and Complementary '
             'Medicine 19(7), 2013',
             'https://pubmed.ncbi.nlm.nih.gov/23360656/'),
            ('S. H. Han ve ark., “Effect of aromatherapy on symptoms '
             'of dysmenorrhea in college students: A randomized '
             'placebo-controlled clinical trial”, Journal of '
             'Alternative and Complementary Medicine 12(6), 2006',
             'https://pubmed.ncbi.nlm.nih.gov/16884344/'),
            ('M. C. Ou ve ark., “Pain relief assessment by aromatic '
             'essential oil massage on outpatients with primary '
             'dysmenorrhea”, Journal of Obstetrics and Gynaecology '
             'Research 38(5), 2012',
             'https://pubmed.ncbi.nlm.nih.gov/22435409/'),
            ('Y. H. Kao ve ark., “Comparisons for Effectiveness of '
             'Aromatherapy and Acupressure Massage on Quality of Life '
             'in Career Women: A Randomized Controlled Trial”, '
             'Journal of Alternative and Complementary Medicine '
             '23(6), 2017',
             'https://pubmed.ncbi.nlm.nih.gov/28504569/'),
            ('J. Zhou ve ark., “The bioactivities of sclareol: A mini '
             'review”, Frontiers in Pharmacology 13, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/36263135/'),
            ('P. Zerbe, J. Bohlmann, “Enzymes for synthetic biology '
             'of ambroxide-related diterpenoid fragrance compounds”, '
             'Advances in Biochemical Engineering/Biotechnology 148, '
             '2015',
             'https://pubmed.ncbi.nlm.nih.gov/25846965/'),
            ('M. Kačániová ve ark., “Salvia sclarea Essential Oil '
             'Chemical Composition and Biological Activities”, '
             'International Journal of Molecular Sciences 24(6), '
             '2023',
             'https://pubmed.ncbi.nlm.nih.gov/36982252/'),
            ('A. Ulubelen ve ark., “Terpenoids from Salvia sclarea”, '
             'Phytochemistry 36(4), 1994',
             'https://pubmed.ncbi.nlm.nih.gov/7765213/'),
            ('W. N. Setzer, “Essential oils and anxiolytic '
             'aromatherapy”, Natural Product Communications 4(9), '
             '2009',
             'https://pubmed.ncbi.nlm.nih.gov/19831048/'),
            ('B. Ben Akacha ve ark., “Salvia officinalis L. and '
             'Salvia sclarea Essential Oils: Chemical Composition, '
             'Biological Activities and Preservative Effects against '
             'Listeria monocytogenes”, Plants 12(19): 3425, 2023',
             'https://pubmed.ncbi.nlm.nih.gov/37836125/'),
        ],
        rel=['tibbiadacayi', 'adacayi', 'kurtreyhani'],
        en=dict(
            name='Clary sage',
            other='English clary sage, clary. Turkish misk adaçayı, '
                  'misk otu. **Neither the European Medicines Agency '
                  'nor the Turkish agency has a monograph for this '
                  'species** (both lists were checked at species '
                  'level). **The monographs behind the sage records in '
                  'this catalogue do not belong to this species:** the '
                  'EMA sage monographs are for *Salvia officinalis* '
                  '(see [[tibbiadacayi]]) and *Salviae trilobae* = '
                  '*S. fruticosa* (see [[adacayi]]), and the Turkish '
                  'agency’s sage monograph is for *Salvia triloba*. '
                  'This species falls under none of them.',
            part='Flowering branches; the essential oil distilled from '
                 'the flowers',
            uses=[
                ['In perfumery — a raw material with a trade of its '
                 'own',
                 'The Zerbe review published in Advances in '
                  'Biochemical Engineering/Biotechnology in 2015 '
                  'treats the enzymes used in the synthetic biology of '
                  'ambroxide-related diterpenoid fragrance compounds; '
                  'the starting material for these compounds is '
                  '**sclareol**, which this species yields. The Zhou '
                  'review published in Frontiers in Pharmacology in '
                  '2022 reviews the bioactivities of sclareol. This is '
                  'the **product and the trade of its own** that '
                  'separate the species from the other sages in this '
                  'catalogue; ambroxide is used in place of ambergris '
                  'in perfumery.'],
                ['In aromatherapy — human studies testing its scent',
                 'The species’ essential oil has been tested in four '
                  'human studies; the detail and the **important '
                  'limits** are written in the science field.'],
                ['Laboratory measurements of the essential oil',
                 'The Kačániová study published in the International '
                  'Journal of Molecular Sciences in 2023 measured the '
                  'oil’s chemical composition and biological '
                  'activities. The Ben Akacha study published in '
                  'Plants the same year examines the essential oils of '
                  '*S. officinalis* and *S. sclarea* comparatively. '
                  'The Ulubelen study published in Phytochemistry in '
                  '1994 characterises the species’ terpenoids. These '
                  'are **in vitro and phytochemistry** studies.'],
            ],
            prep='No dose is accepted in an official monograph; '
                 'because neither official list carries a monograph, '
                 'there is no accepted measure, duration or upper '
                 'limit. **The essential oil is a concentrated '
                 'product, and in the human studies relied on here it '
                 'was used diluted, by massage on the skin or by '
                 'inhalation — it was not taken by mouth.** The '
                 'blend proportions used in those studies are not '
                 'written here, because their full texts were not '
                 'read and a claim carrying a number is not written '
                 'from an abstract.',
            science='In the sources available to us there are **four '
                    'studies in humans, but all share one heavy '
                    'limitation: in three of them the species was '
                    'tested not on its own but blended with other '
                    'essential oils and combined with an application '
                    'such as massage — so the effect observed cannot '
                    'be attributed to this species.** The Seol study '
                    'published in the Journal of Alternative and '
                    'Complementary Medicine in 2013 is a randomized '
                    'controlled trial and compares the **differential** '
                    'effects of *Salvia sclarea* and *Lavandula '
                    'angustifolia*; it is the closest thing here to a '
                    'study treating the species on its own. The Han '
                    'study published in the Journal of Alternative and '
                    'Complementary Medicine in 2006 tested '
                    'aromatherapy in dysmenorrhoea in college '
                    'students, placebo-controlled. The Ou study '
                    'published in the Journal of Obstetrics and '
                    'Gynaecology Research in 2012 assessed aromatic '
                    'essential oil massage in dysmenorrhoea. The Kao '
                    'study published in the Journal of Alternative and '
                    'Complementary Medicine in 2017 compared '
                    'aromatherapy with acupressure massage for '
                    'quality of life. The Setzer review published in '
                    'Natural Product Communications in 2009 treats '
                    'essential oils and anxiolytic aromatherapy; **it '
                    'is a review.** The remaining sources are **in '
                    'vitro and phytochemistry** studies.',
            safety='In the sources relied on here there is **no safety '
                   'assessment in humans** for this species, and no '
                   'separate assessment for pregnancy, '
                   'breastfeeding, children or drug interactions; '
                   'that is an absence of information. **The safety '
                   'rules of the sage records in this catalogue do not '
                   'belong to this species:** the thujone '
                   'restrictions written for sage come from the *Salvia '
                   'officinalis* and *S. fruticosa* monographs. This '
                   'species has no monograph, and the sources '
                   'available to us give no limit for it based on '
                   'thujone content — which does not mean "this '
                   'species has no thujone problem", it means it has '
                   'not been measured. The essential oil is a '
                   'concentrated product; in the human studies relied '
                   'on here it was used diluted and by the skin or by '
                   'scent, not taken by mouth.',
            fact='This species’ soundest trace is not in medicine but '
                 'in perfumery: the sclareol it yields is the starting '
                 'material for ambroxide, used in place of ambergris, '
                 'and the subject of the 2015 review is carrying out '
                 'that conversion with enzymes. So the reason the '
                 'plant enters this catalogue with a record of its own '
                 'is not a healing claim but an industry of its own.',
            season='The sources relied on here give no collection '
                   'calendar for Türkiye.',
            habitat='According to Kew’s records its range covers 52 '
                    'regions, Türkiye among them.',
            local='misk adaçayı, misk otu',
            confusion='**It is confused with the other Salvia records in '
                      'this catalogue, and the consequence of that '
                      'confusion is a safety rule passing to the '
                      'wrong species:** [[tibbiadacayi]] (*S. '
                      'officinalis*), [[adacayi]] (*S. fruticosa*), '
                      '[[biberiye]] (*S. rosmarinus*), [[akadacayi]] '
                      '(*S. apiana*), [[chia]] (*S. hispanica*) and '
                      '[[salviadivinorum]] (*S. divinorum*) and '
                      '[[kurtreyhani]] (*S. multicaulis*), written '
                      'in the same batch. One species’ monograph and '
                      'restrictions do not belong to its relative.',
        ),
    ),
    dict(
        yayin='2026-11-28', arsiv=True, id='kurtreyhani', foto='',
        tr='Kürt reyhanı', la='Salvia multicaulis Vahl',
        taxon='Salvia multicaulis', fam='Lamiaceae (ballıbabagiller)',
        diger='Türkçede kürt reyhanı. **Bu türün ne Avrupa İlaç '
              'Ajansı’nda ne TİTCK’de monografı vardır** (iki listeye '
              'tür düzeyinde bakıldı) ve **katalogdaki adaçayı '
              'monografları bu türe ait değildir** — ayrıntısı '
              '[[miskadacayi]] kaydındaki gibidir. Adında "reyhan" '
              'geçse de fesleğen (*Ocimum basilicum*) değildir; '
              'aynı familyadan ayrı bir cinstir.',
        bolge=['anadolu'], kat=['sifa'], kisim='Kök ve toprak üstü kısım',
        kul=[
            ['Kullanım kaydı — elimizdeki kaynaklarda yok',
             '**Dayanak alınan dört künyenin hiçbiri bu türün halk '
              'arasındaki kullanımını kaydetmez;** dördü de '
              'laboratuvar çalışmasıdır. Türkçe adı yerleşik '
              'olduğu hâlde, bu kayıt için taranan kaynaklarda '
              'adı konmuş bir kullanım bulunamamıştır — bu, '
              'böyle bir kullanım olmadığı değil, **taranan '
              'kaynaklarda (Kew kaydı ve aşağıdaki dört künye) '
              'belgelenmediği** anlamına gelir.'],
            ['Laboratuvarda ayrılmış bileşikler',
             'Türden ayrılan bileşikler üzerine dört çalışma '
              'vardır; hepsi **tüp içidir** ve `bilim` alanında '
              'yazılıdır.'],
        ],
        haz='Resmî bir monografta kabul edilmiş doz yoktur; iki resmî '
            'listede de monografı bulunmadığı için kabul edilmiş bir '
            'ölçü, süre ya da üst sınır yoktur. **Dayanak alınan '
            'kaynaklarda insanda kullanım için hiçbir ölçü '
            'verilmemiştir ve bir hazırlama biçimi de '
            'kaydedilmemiştir.**',
        bilim='Elimizdeki kaynaklarda **insanda yapılmış hiçbir '
              'çalışma yoktur; dört künyenin dördü de tüp içi '
              'ölçümdür.** 3 Biotech’te 2024’te yayımlanan Hamed '
              'çalışması türden ayrılan salvimultikanolün '
              'lipopolisakkaritle uyarılmış iltihabı '
              '**RAW264.7 hücre hattında** baskıladığını '
              'bildirir. Pharmaceuticals dergisinde 2022’de '
              'yayımlanan Yigitkan çalışması türden ayrılan '
              '7-asetoksiharminonu HMG-CoA redüktaz '
              'baskılayıcısı olarak **tüp içinde** ölçmüştür. '
              'Fitoterapia’da 2018’de yayımlanan Hegazy '
              'çalışması abietan diterpenoitlerin çok ilaca '
              'dirençli **hücre hatlarına** karşı '
              'sitotoksikliğini ölçmüştür. Natural Product '
              'Research’te 2022’de yayımlanan Tavan çalışması '
              'yabani popülasyonlar arasındaki fenolik '
              'çeşitliliği ölçer. **Hücre hattında ölçülen '
              'iltihap baskılanması ya da sitotoksiklik, '
              'insanda bir etki değildir;** bu kayıtta '
              'bunlardan bir kullanım çıkarılmamıştır.',
        kanit='geleneksel', guv='orta',
        guvNot='Dayanak alınan kaynaklarda bu tür için **insanda '
               'yapılmış bir güvenlilik değerlendirmesi yoktur** ve '
               'gebelik, emzirme, çocuklar ile ilaç etkileşimleri '
               'için ayrı bir değerlendirme bulunmamaktadır. '
               'Bu, bitkinin güvenli olduğu anlamına gelmez; '
               'bilginin yokluğudur — ve bu türde yokluk '
               'ötekilerden daha geniştir, çünkü insanda hiçbir '
               'çalışma yoktur. **Katalogdaki adaçayı '
               'kayıtlarının tuyon kısıtlamaları bu türe ait '
               'değildir;** bu tür için tuyon içeriğine dayalı '
               'bir sınır elimizdeki kaynaklarda verilmemiştir.',
        ilginc='Türkçede yerleşik bir adı olan bir bitkinin, '
               'taranan kaynaklarda kayıtlı tek bir kullanımı '
               'bile bulunmaması bu kataloğun sık rastladığı '
               'bir boşluk: ad halkın, literatür ise '
               'laboratuvarın. Dört çalışmanın dördü de '
               'bitkiden bileşik ayırmakla ilgili — biri '
               'kolesterol enzimini, biri iltihabı, biri '
               'dirençli hücreleri hedefliyor; hiçbiri '
               'bitkinin neden "kürt reyhanı" diye '
               'bilindiğini sormuyor.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklarda Türkiye için bir '
                   'toplama takvimi verilmemiştir.',
            yetisme='Kew’in kayıtlarına göre doğal yayılışı altı '
                    'bölgedir: İran, Irak, Lübnan-Suriye, '
                    'Filistin, Sina ve Türkiye.',
            yoresel='kürt reyhanı',
            karisma='Adında "reyhan" geçmesine karşın fesleğen '
                    '(*Ocimum basilicum*) değildir. Katalogdaki '
                    'öteki Salvia kayıtlarıyla da karışır; bir türün '
                    'monografı ve kısıtlamaları akrabasına ait '
                    'değildir — bkz. [[miskadacayi]].',
        ),
        kaynak=[
            ('Salvia multicaulis Vahl, World Checklist of Vascular '
             'Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'),
            ('A. R. Hamed ve ark., “Salvimulticanol from Salvia '
             'multicaulis suppresses LPS-induced inflammation in '
             'RAW264.7 macrophages: in vitro and in silico studies”, '
             '3 Biotech 14(5), 2024',
             'https://pubmed.ncbi.nlm.nih.gov/38706927/'),
            ('S. Yigitkan ve ark., “7-Acetoxyhorminone from Salvia '
             'multicaulis Vahl. as Promising Inhibitor of '
             '3-Hydroxy-3-methylglutaryl Coenzyme A Reductase”, '
             'Pharmaceuticals 15(2), 2022',
             'https://pubmed.ncbi.nlm.nih.gov/35215310/'),
            ('M. F. Hegazy ve ark., “Cytotoxicity of abietane '
             'diterpenoids from Salvia multicaulis towards '
             'multidrug-resistant cancer cells”, Fitoterapia 130, '
             '2018',
             'https://pubmed.ncbi.nlm.nih.gov/30114467/'),
            ('M. Tavan ve ark., “Phenolics diversity among wild '
             'populations of Salvia multicaulis”, Natural Product '
             'Research 36(5), 1332–1336, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/33356575/'),
        ],
        rel=['miskadacayi', 'adacayi'],
        en=dict(
            name='Many-stemmed sage',
            other='Turkish kürt reyhanı. **Neither the European '
                  'Medicines Agency nor the Turkish agency has a '
                  'monograph for this species** (both lists were '
                  'checked at species level), and **the sage '
                  'monographs behind this catalogue’s records do not '
                  'belong to this species** — the detail is as in the '
                  '[[miskadacayi]] record. Although its Turkish name '
                  'contains "reyhan" (basil) it is not basil '
                  '(*Ocimum basilicum*); it is a separate genus in '
                  'the same family.',
            part='Root and aerial parts',
            uses=[
                ['A record of use — absent from the sources available '
                 'to us',
                 '**None of the four citations relied on here records '
                  'any folk use of this species;** all four are '
                  'laboratory studies. Although its Turkish name is '
                  'well established, no named use was found in the '
                  'sources searched for this record — which means '
                  'not that no such use exists, but that it is '
                  '**not documented in the sources searched (the Kew '
                  'record and the four citations below).**'],
                ['Compounds isolated in the laboratory',
                 'There are four studies on compounds isolated from '
                  'the species; all are **in vitro** and are written '
                  'in the science field.'],
            ],
            prep='No dose is accepted in an official monograph; '
                 'because neither official list carries a monograph, '
                 'there is no accepted measure, duration or upper '
                 'limit. **The sources relied on here give no measure '
                 'whatsoever for use in humans, and record no method '
                 'of preparation either.**',
            science='In the sources available to us there is **no '
                    'study in humans at all; all four citations are '
                    'in vitro measurements.** The Hamed study '
                    'published in 3 Biotech in 2024 reports that '
                    'salvimulticanol, isolated from the species, '
                    'suppressed lipopolysaccharide-induced '
                    'inflammation **in the RAW264.7 cell line.** The '
                    'Yigitkan study published in Pharmaceuticals in '
                    '2022 measured 7-acetoxyhorminone, isolated from '
                    'the species, as an inhibitor of HMG-CoA '
                    'reductase **in vitro.** The Hegazy study '
                    'published in Fitoterapia in 2018 measured the '
                    'cytotoxicity of abietane diterpenoids towards '
                    'multidrug-resistant **cell lines.** The Tavan '
                    'study published in Natural Product Research in '
                    '2022 measures phenolic diversity among wild '
                    'populations. **Inflammation suppression or '
                    'cytotoxicity measured in a cell line is not an '
                    'effect in a human being;** no use is derived '
                    'from them in this record.',
            safety='In the sources relied on here there is **no safety '
                   'assessment in humans** for this species, and no '
                   'separate assessment for pregnancy, '
                   'breastfeeding, children or drug interactions. '
                   'That does not mean the plant is safe; it is an '
                   'absence of information — and in this species the '
                   'absence is wider than in the others, because '
                   'there is no study in humans at all. **The thujone '
                   'restrictions of the sage records in this '
                   'catalogue do not belong to this species;** the '
                   'sources available to us give no limit for it '
                   'based on thujone content.',
            fact='That a plant with an established Turkish name has '
                 'not a single documented use in the sources searched '
                 'is a gap this catalogue meets often: the name '
                 'belongs to the people, the literature to the '
                 'laboratory. All four studies concern isolating '
                 'compounds from the plant — one targets a '
                 'cholesterol enzyme, one inflammation, one resistant '
                 'cells; none asks why the plant is known as "kürt '
                 'reyhanı".',
            season='The sources relied on here give no collection '
                   'calendar for Türkiye.',
            habitat='According to Kew’s records its natural range '
                    'covers six regions: Iran, Iraq, '
                    'Lebanon-Syria, Palestine, Sinai and Türkiye.',
            local='kürt reyhanı',
            confusion='Despite the "reyhan" in its name it is not '
                      'basil (*Ocimum basilicum*). It is also '
                      'confused with the other Salvia records in this '
                      'catalogue; one species’ monograph and '
                      'restrictions do not belong to its relative — '
                      'see [[miskadacayi]].',
        ),
    ),
    dict(
        yayin='2026-11-28', arsiv=True, id='mayasilotu', foto='',
        tr='Mayasıl otu', la='Ajuga chamaepitys (L.) Schreb.',
        taxon='Ajuga chamaepitys', fam='Lamiaceae (ballıbabagiller)',
        diger='İngilizce ground pine, yellow bugle. Türkçede mayasıl '
              'otu, dalak otu. **Bu türün ne Avrupa İlaç Ajansı’nda '
              'ne TİTCK’de monografı vardır** (iki listeye tür '
              'düzeyinde bakıldı). **Dayanak alınan en ayrıntılı '
              'çalışma türün tamamına değil, *A. chamaepitys* subsp. '
              '*chia* alt türüne aittir;** alt tür düzeyindeki bir '
              'bulgu türün bütününe genellenmemiştir. Adında "çam" '
              'geçen İngilizce adı (ground pine) kokusundan gelir, '
              'çamla akrabalığı yoktur.',
        bolge=['anadolu'], kat=['sifa'], kisim='Toprak üstü kısım',
        kul=[
            ['Halk hekimliğinde — ishal',
             'Food and Chemical Toxicology’de 2020’de yayımlanan '
              'Küpeli Akkol çalışması, **Türk halk hekimliğinde** '
              '*A. chamaepitys* subsp. *chia* alt türünün toprak '
              'üstü kısımlarının **ishal tedavisinde** '
              'kullanıldığını yazar. Kullanım kaydı alt tür '
              'düzeyindedir.'],
            ['Halk hekimliğinde — ağrı kesici, kuvvet verici ve '
             'mayasıl',
             'Food Science & Nutrition’da 2025’te yayımlanan Aydın '
              'çalışması, *A. chamaepitys* subsp. *chia*’nın '
              '**Türkiye’de geleneksel olarak** ağrı kesici ve '
              'kuvvet verici olarak, ayrıca **basurun ve yaraların '
              'dıştan tedavisinde** kullanıldığını yazar. '
              'Türkçe "mayasıl otu" adının karşılığı bu son '
              'kullanımdır; yani adın işaret ettiği kullanım '
              'kaynakta da duruyor. Aynı çalışmanın başlığı türü '
              '"bitki çayından bilime" diye çerçeveler, yani çay '
              'olarak içildiği çalışmanın kendi çıkış '
              'noktasıdır. **Bu kayıtların ikisi de alt tür '
              'düzeyindedir ve hiçbiri bir etkinlik kanıtı '
              'değildir.**'],
            ['Alt tür düzeyinde bir hayvan çalışması',
             'Food and Chemical Toxicology’de 2020’de yayımlanan '
              'Küpeli Akkol çalışması *A. chamaepitys* subsp. '
              '*chia* alt türünün ve ondan ayrılan iridoitlerin '
              'yararlı etkilerini bildirir. **Bu bulgu alt türe '
              'aittir ve bir hayvan/laboratuvar çalışmasıdır;** '
              'insanda etki göstermez.'],
        ],
        haz='Resmî bir monografta kabul edilmiş doz yoktur; iki resmî '
            'listede de monografı bulunmadığı için kabul edilmiş bir '
            'ölçü, süre ya da üst sınır yoktur. Dayanak alınan '
            'kaynaklarda insanda kullanım için bir ölçü '
            'verilmemiştir.',
        bilim='Elimizdeki kaynaklarda **insanda yapılmış hiçbir '
              'çalışma yoktur.** Food and Chemical Toxicology’deki '
              '2020 tarihli Küpeli Akkol çalışması **alt tür '
              'düzeyinde** (*subsp. chia*) yararlı etkiler ve '
              'iridoitler bildirir. Fitoterapia’da 2016’da '
              'yayımlanan Venditti çalışması türün fitokimyasını, '
              'mikromorfolojisini ve biyoetkinliklerini inceler. '
              'Food Science & Nutrition’da 2025’te yayımlanan '
              'Aydın çalışması fitokimyasal ve biyolojik bir '
              'incelemedir. Chemistry & Biodiversity’de 2022’de '
              'yayımlanan Koca-Caliskan çalışması türü bakır '
              'nanoçiçek sentezinde kullanır; bu bir **malzeme '
              'kimyası** çalışmasıdır. **Bu kayıtta bir '
              'hastalıkta etki iddiası yoktur.**',
        kanit='geleneksel', guv='orta',
        guvNot='Dayanak alınan kaynaklarda bu tür için **insanda '
               'yapılmış bir güvenlilik değerlendirmesi yoktur** ve '
               'gebelik, emzirme, çocuklar ile ilaç etkileşimleri '
               'için ayrı bir değerlendirme bulunmamaktadır; bu, '
               'bilginin yokluğudur. **Alt türler arasındaki fark '
               'burada önemsiz değildir:** elimizdeki en ayrıntılı '
               'çalışma *subsp. chia* alt türüne aittir ve o alt '
               'tür için bildirilenler türün bütününe ait '
               'değildir.',
        ilginc='Türkçe ad bir rahatsızlığı anıyor — "mayasıl", '
               'yani basur — ve kaynaklar bu kez adı doğruluyor: '
               '2025 tarihli çalışma bitkinin Türkiye’de basurun '
               'dıştan tedavisinde kullanıldığını yazıyor. İlginç '
               'olan, literatürün bu kullanımı türe değil '
               '**alt türe** (*subsp. chia*) bağlaması: dört '
               'künyeden üçü alt tür adını taşıyor. Yani halkın '
               'tek bir adla andığı bitki, botanikte bir basamak '
               'daha aşağıda tanımlanıyor — ve aynı adla '
               'toplanan başka bir alt tür için bu bulguların '
               'geçerli olup olmadığı bilinmiyor.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklarda Türkiye için bir '
                   'toplama takvimi verilmemiştir.',
            yetisme='Kew’in kayıtlarına göre yayılışı 45 bölgeyi '
                    'kapsar; Türkiye de bunların arasındadır.',
            yoresel='mayasıl otu, dalak otu',
            karisma='"Dalak otu" adı Türkçede [[kisamahmutotu]] '
                    '(*Teucrium chamaedrys*) için de kullanılır ve '
                    '**bu karışma tehlikelidir:** o tür karaciğer '
                    'zehirliliği yüzünden Fransa’da piyasadan '
                    'çekilmiş, İtalya’da zehir sayılmıştır. İki '
                    'bitki aynı familyadandır ama ayrı '
                    'cinslerdendir. İngilizce adı "ground pine" '
                    'olmasına karşın çamla akraba değildir.',
        ),
        kaynak=[
            ('Ajuga chamaepitys (L.) Schreb., World Checklist of '
             'Vascular Plants, Royal Botanic Gardens, Kew',
             'https://powo.science.kew.org/'),
            ('E. Küpeli Akkol ve ark., “Beneficial effects of Ajuga '
             'chamaepitys (L.) Schreber subsp. chia (Schreber) and '
             'its iridoids on the colitis model: Histopathological '
             'and biochemical evidence”, Food and Chemical '
             'Toxicology 144: 111589, 2020',
             'https://pubmed.ncbi.nlm.nih.gov/32726593/'),
            ('A. Venditti ve ark., “Phytochemistry, micromorphology '
             'and bioactivities of Ajuga chamaepitys (L.) Schreb. '
             '(Lamiaceae)”, Fitoterapia 113, 2016',
             'https://pubmed.ncbi.nlm.nih.gov/27373875/'),
            ('B. Aydın ve ark., “From Herbal Tea to Science: '
             'Phytochemical and Biological Investigation of Ajuga '
             'chamaepitys subsp. chia (Lamiaceae) With Molecular '
             'Docking Analysis”, Food Science & Nutrition 13(8): '
             'e70749, 2025',
             'https://pubmed.ncbi.nlm.nih.gov/40808707/'),
            ('U. Koca-Caliskan ve ark., “Synthesis and '
             'Characterization of Copper-Nanoflowers with the '
             'Utilization of Medicinal Plant Extracts”, Chemistry & '
             'Biodiversity 19(11), e202200476, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/36149402/'),
        ],
        rel=['kisamahmutotu', 'calba'],
        en=dict(
            name='Ground pine',
            other='English ground pine, yellow bugle. Turkish mayasıl '
                  'otu, dalak otu. **Neither the European Medicines '
                  'Agency nor the Turkish agency has a monograph for '
                  'this species** (both lists were checked at species '
                  'level). **The most detailed study relied on here '
                  'belongs not to the species as a whole but to the '
                  'subspecies *A. chamaepitys* subsp. *chia*;** a '
                  'finding at subspecies level has not been '
                  'generalised to the whole species. Its English name '
                  '"ground pine" comes from its scent; it is not '
                  'related to pine.',
            part='Aerial parts',
            uses=[
                ['In folk medicine — diarrhoea',
                 'The Küpeli Akkol study published in Food and '
                  'Chemical Toxicology in 2020 writes that **in '
                  'Turkish folk medicine** the aerial parts of *A. '
                  'chamaepitys* subsp. *chia* are used **for the '
                  'treatment of diarrhoea.** The record of use is at '
                  'subspecies level.'],
                ['In folk medicine — analgesic, tonic and '
                 'haemorrhoids',
                 'The Aydın study published in Food Science & '
                  'Nutrition in 2025 writes that *A. chamaepitys* '
                  'subsp. *chia* is **traditionally used in '
                  'Türkiye** as an analgesic and a tonic, and for '
                  'the **external treatment of haemorrhoids and '
                  'wounds.** That last use is what the Turkish name '
                  '"mayasıl otu" refers to; so the use the name '
                  'points to is present in the source as well. The '
                  'same study’s title frames the species as going '
                  '"from herbal tea to science", so that it is drunk '
                  'as a tea is the study’s own starting point. '
                  '**Both records of use are at subspecies level and '
                  'neither is evidence of efficacy.**'],
                ['An animal study at subspecies level',
                 'The Küpeli Akkol study published in Food and '
                  'Chemical Toxicology in 2020 reports beneficial '
                  'effects of *A. chamaepitys* subsp. *chia* and the '
                  'iridoids isolated from it. **That finding belongs '
                  'to the subspecies and is an animal/laboratory '
                  'study;** it shows no effect in humans.'],
            ],
            prep='No dose is accepted in an official monograph; '
                 'because neither official list carries a monograph, '
                 'there is no accepted measure, duration or upper '
                 'limit. The sources relied on here give no measure '
                 'for use in humans.',
            science='In the sources available to us there is **no '
                    'study in humans at all.** The 2020 Küpeli Akkol '
                    'study in Food and Chemical Toxicology reports '
                    'beneficial effects and iridoids **at subspecies '
                    'level** (*subsp. chia*). The Venditti study '
                    'published in Fitoterapia in 2016 examines the '
                    'species’ phytochemistry, micromorphology and '
                    'bioactivities. The Aydın study published in Food '
                    'Science & Nutrition in 2025 is a phytochemical '
                    'and biological investigation. The Koca-Caliskan '
                    'study published in Chemistry & Biodiversity in '
                    '2022 uses the species in copper-nanoflower '
                    'synthesis; that is a **materials chemistry** '
                    'study. **There is no claim of effect in any '
                    'disease in this record.**',
            safety='In the sources relied on here there is **no safety '
                   'assessment in humans** for this species, and no '
                   'separate assessment for pregnancy, '
                   'breastfeeding, children or drug interactions; '
                   'that is an absence of information. **The '
                   'difference between subspecies is not immaterial '
                   'here:** the most detailed study available to us '
                   'belongs to *subsp. chia*, and what is reported '
                   'for that subspecies does not belong to the whole '
                   'species.',
            fact='The Turkish name invokes a complaint — "mayasıl", '
                 'meaning haemorrhoids — and this time the sources '
                 'bear the name out: the 2025 study writes that the '
                 'plant is used in Türkiye for the external '
                 'treatment of haemorrhoids. What is interesting is '
                 'that the literature ties this use not to the '
                 'species but to the **subspecies** (*subsp. '
                 'chia*): three of the four citations carry the '
                 'subspecies name. So a plant the public calls by a '
                 'single name is defined one rank lower in botany — '
                 'and whether these findings hold for another '
                 'subspecies gathered under the same name is not '
                 'known.',
            season='The sources relied on here give no collection '
                   'calendar for Türkiye.',
            habitat='According to Kew’s records its range covers 45 '
                    'regions, Türkiye among them.',
            local='mayasıl otu, dalak otu',
            confusion='The Turkish name "dalak otu" is also used for '
                      '[[kisamahmutotu]] (*Teucrium chamaedrys*), and '
                      '**that confusion is dangerous:** that species '
                      'was withdrawn from the market in France and '
                      'classed as a poison in Italy because of liver '
                      'toxicity. The two plants are in the same '
                      'family but separate genera. Despite its '
                      'English name "ground pine" it is not related '
                      'to pine.',
        ),
    ),
    dict(
        yayin='2026-11-28', arsiv=True, id='dagnanesi', foto='',
        tr='Dağ nanesi', la='Cyclotrichium niveum (Boiss.) Manden. & Scheng.',
        taxon='Cyclotrichium niveum', fam='Lamiaceae (ballıbabagiller)',
        diger='Türkçede dağ nanesi, dağ reyhanı. **Bu türün ne Avrupa '
              'İlaç Ajansı’nda ne TİTCK’de monografı vardır** (iki '
              'listeye tür düzeyinde bakıldı). Kew’in kayıtlarına '
              'göre doğal yayılışı **tek bir bölgedir: Türkiye** — '
              'yani bu kataloğun en dar yayılışlı kayıtlarından '
              'biridir. **Adında "nane" geçse de *Mentha* '
              'cinsinden değildir;** `karisma` alanına bakın.',
        bolge=['anadolu'], kat=['sifa'], kisim='Toprak üstü kısım (çay olarak yaprak ve çiçek). **Uçucu yağı içilmez** — aşağıdaki pulegon notuna bakın',
        kul=[
            ['Çay olarak — ve kaynakların sessizliği',
             '**Bu kayıt için taranan kaynaklarda türün halk '
              'arasındaki kullanımını belgeleyen bir saha '
              'çalışması bulunmamıştır.** Dört künyenin dördü de '
              'laboratuvar çalışmasıdır. Türkçe adı ve kokusu '
              'bir çay kullanımına işaret etse de, bir kullanım '
              'iddiası buraya ancak kaynağıyla yazılabilirdi; '
              'taranan kaynaklar (Kew kaydı ve aşağıdaki dört '
              'künye) bunu vermemektedir.'],
            ['Laboratuvar ölçümleri',
             'Dört çalışmanın hepsi hayvan ya da tüp içidir ve '
              '`bilim` alanında yazılıdır.'],
        ],
        haz='Resmî bir monografta kabul edilmiş doz yoktur; iki resmî '
            'listede de monografı bulunmadığı için kabul edilmiş bir '
            'ölçü, süre ya da üst sınır yoktur. Dayanak alınan '
            'kaynaklarda insanda kullanım için bir ölçü '
            'verilmemiştir.',
        bilim='Elimizdeki kaynaklarda **insanda yapılmış hiçbir '
              'çalışma yoktur.** Antioxidants dergisinde 2026’da '
              'yayımlanan Özsayın çalışması türün gentamisinle '
              'oluşturulan böbrek hasarına karşı koruyucu '
              'etkisini **sıçanlarda** ölçmüştür. Food and '
              'Chemical Toxicology’de 2017’de yayımlanan Özdemir '
              'çalışması tür ekstrelerinin kanser karşıtı '
              'etkinliğini **tüp içinde** ölçmüştür. Cellular and '
              'Molecular Biology’de 2019’da yayımlanan Sahin '
              'çalışması beyindeki asetilkolinesteraz etkinliğini '
              've oksidatif stresi **kurşun asetata ağız yoluyla '
              'maruz bırakılmış erkek sıçanlarda** '
              'değerlendirmiştir. Chemistry & '
              'Biodiversity’de 2023’te yayımlanan Güzel '
              'çalışması LC/MS/MS ile ölçülen fenolik içerik ile '
              'antioksidan kapasite arasındaki ilişkiyi '
              'inceler. **Sıçanda ölçülen böbrek koruyuculuğu '
              'ya da tüp içinde ölçülen kanser karşıtı etkinlik '
              'insanda bir etki değildir;** bu kayıtta '
              'bunlardan bir kullanım çıkarılmamıştır.',
        kanit='geleneksel', guv='orta',
        guvNot='⚠️ **Bu türün uçucu yağı pulegon bakımından çok '
               'zengindir ve bu, kaydın en önemli güvenlik '
               'bilgisidir.** Antioxidants dergisinde 2026’da '
               'yayımlanan Özsayın çalışması türün uçucu yağını '
               'GC-MS ile çözümlemiş ve **ana bileşeni pulegon '
               'olarak, yüzde 79,6 oranında** belirlemiştir; aynı '
               'çalışmanın hayvan kolu doğrudan izole pulegonla '
               'yürütülmüştür. Bu oran, katalogdaki '
               '[[tasnanesi]] kaydında ölçülen oranlardan (yüzde '
               '42,81 ve yüzde 58,5) **daha yüksektir.** EMA’nın '
               'pulegon ve mentofuran hakkındaki kamu görüşüne '
               '(2016) göre bu maddelerin başlıca hedef organı '
               'karaciğerdir; Uluslararası Kanser Araştırmaları '
               'Ajansı pulegonu 2B grubunda (insanlar için olası '
               'kanserojen) sınıflandırır ve EMA bitkisel '
               'ilaçlarda pulegon ile mentofuran toplamı için '
               'kabul edilebilir sınırı **günde 0,75 mg/kg vücut '
               'ağırlığı** olarak önerir — 50 kg’lık bir yetişkin '
               'için günde 37,5 mg, çocuklarda vücut ağırlığına '
               'göre daha az. **Uçucu yağ içilmemelidir;** pulegon '
               'oranı yüksek yarpuz yağından yaklaşık 10 ml '
               'içilmesi orta-ağır zehirlenmeye, 15 ml’den fazlası '
               'ölüme yol açmıştır. Gebelikte, emzirirken ve '
               'çocuklarda bitkinin tıbbi amaçla kullanımından '
               'kaçınılmalıdır; karaciğer hastalığı olanlar yoğun '
               'çay ve ekstrelerden uzak durmalıdır. Uçucu yağ '
               'yutulduysa 114 (Ulusal Zehir Danışma Merkezi) ya '
               'da 112 aranmalıdır. **Bu kısıtlama bileşen '
               'temellidir, cins temelli değildir:** pulegon '
               'sınırı bitkinin hangi cinsten olduğuna değil, '
               'yağında ne kadar pulegon bulunduğuna bağlıdır. '
               'Bunun dışında, tür için insanda yapılmış bir '
               'güvenlilik değerlendirmesi ve gebelik, emzirme, '
               'çocuklar ile ilaç etkileşimleri için ayrı bir '
               'çalışma dayanak alınan kaynaklarda yoktur. '
               '**Nane için yazılanlar da bu türe ait '
               'değildir:** katalogdaki [[nane]] kaydının '
               'dayandığı EMA monografı *Mentha × piperita* '
               'içindir ve bu tür ayrı bir cinstendir — ama '
               'pulegon konusunda bu tür naneden değil '
               '[[yarpuz]]dan yanadır. Türün '
               'yayılışı Kew’e göre yalnız Türkiye olduğu için '
               '**yabandan toplamanın koruma açısından sakıncası '
               'ayrıca düşünülmelidir;** dayanak alınan '
               'kaynaklarda türün koruma durumunu veren bir '
               'değerlendirme yoktur.',
        ilginc='Yalnız Türkiye’de yetişen bir bitki, adını '
               'yetişmediği bir cinsten alıyor: "dağ nanesi" '
               'deniyor, ama *Mentha* değil, *Cyclotrichium*. '
               'Ne var ki cinsin ayrı olması bu bitkiyi naneden '
               'daha güvenli yapmıyor, tersine: nanenin '
               'monografı buraya geçmiyor, ama nanede '
               'bulunmayan pulegon bu türün yağının yüzde '
               '79,6’sını tutuyor. Yani adın yanlış gösterdiği '
               'şey cins değil risk — bu bitki kokusuyla '
               'naneyi, kimyasıyla [[yarpuz]]u andırıyor.',
        ek=dict(
            mevsim='Dayanak alınan kaynaklarda Türkiye için bir '
                   'toplama takvimi verilmemiştir.',
            yetisme='Kew’in kayıtlarına göre doğal yayılışı tek bir '
                    'bölgedir: Türkiye. Bu kadar dar bir yayılış '
                    'türü Türkiye’ye özgü kılar.',
            yoresel='dağ nanesi',
            karisma='**Adında "nane" geçmesine karşın *Mentha* '
                    'cinsinden değildir;** katalogdaki [[nane]], '
                    '[[yarpuz]], [[sunanesi]] ve [[japonnanesi]] '
                    'kayıtları *Mentha* türleridir ve onların '
                    'monografları, dozları ve kısıtlamaları bu '
                    'türe ait değildir. "Dağ çayı" adıyla '
                    'toplanan [[dagcayistachys]] (*Stachys '
                    'lavandulifolia*) da ayrı bir cinstir. '
                    '**Katalogdaki [[dagreyhani]] (*Ziziphora '
                    'clinopodioides*) ile de karışır** — o da '
                    'pulegon taşıyan ayrı bir cinstir; "dağ" '
                    'önekli bu adların hiçbiri bir cins '
                    'göstermez.',
        ),
        kaynak=[
            ('Cyclotrichium niveum (Boiss.) Manden. & Scheng., World '
             'Checklist of Vascular Plants, Royal Botanic Gardens, '
             'Kew',
             'https://powo.science.kew.org/'),
            ('Bitkisel Tıbbi Ürünler Komitesi (HMPC), “Public '
             'statement on the use of herbal medicinal products '
             'containing pulegone and menthofuran”, '
             'EMA/HMPC/138386/2005 Rev. 1, Avrupa İlaç Ajansı, '
             '12 Temmuz 2016',
             'https://www.ema.europa.eu/en/documents/scientific-guideline/public-statement-use-herbal-medicinal-products-containing-pulegone-and-menthofuran-revision-1_en.pdf'),
            ('G. H. Özsayın ve ark., “Protective Effect of '
             'Cyclotrichium niveum on Gentamicin-Induced '
             'Nephrotoxicity in Rats”, Antioxidants 15(10): 1322, 2026',
             'https://pubmed.ncbi.nlm.nih.gov/42939896/'),
            ('A. Özdemir ve ark., “Promising anticancer activity of '
             'Cyclotrichium niveum L. extracts through induction of '
             'both apoptosis and necrosis”, Food and Chemical '
             'Toxicology 109(Pt 2): 898–909, 2017',
             'https://pubmed.ncbi.nlm.nih.gov/28366842/'),
            ('Z. Sahin ve ark., “Evaluation of the effects of '
             'Cyclotrichium niveum on brain acetylcholinesterase '
             'activity and oxidative stress in male rats orally '
             'exposed to lead acetate”, Cellular and Molecular '
             'Biology 65(5), 2019',
             'https://pubmed.ncbi.nlm.nih.gov/31304900/'),
            ('A. Güzel ve ark., “Relationship Between Phenolic '
             'Content Determined by LC/MS/MS and Antioxidant '
             'Capacity and Enzyme Inhibition of Cyclotrichium niveum '
             'L.”, Chemistry & Biodiversity 20(4), 2023',
             'https://pubmed.ncbi.nlm.nih.gov/36891984/'),
        ],
        rel=['nane', 'dagcayistachys'],
        en=dict(
            name='Cyclotrichium niveum',
            other='Turkish dağ nanesi, dağ reyhanı. **Neither the '
                  'European Medicines Agency nor the Turkish agency '
                  'has a monograph for this species** (both lists '
                  'were checked at species level). According to Kew’s '
                  'records its natural range covers **a single '
                  'region: Türkiye** — making it one of the most '
                  'narrowly distributed records in this catalogue. '
                  '**Although its Turkish name contains "nane" '
                  '(mint) it is not in the genus *Mentha*;** see the '
                  'confusion field.',
            part='Aerial parts (leaf and flower as a tea)',
            uses=[
                ['As a tea — and the silence of the sources',
                 '**In the sources searched for this record there is '
                  'no field study documenting folk use of the '
                  'species.** All four citations are laboratory '
                  'studies. Although its Turkish name and its scent '
                  'point to use as a tea, a claim of use could only '
                  'be written here with its source; the sources '
                  'searched (the Kew record and the four citations '
                  'below) do not provide one.'],
                ['Laboratory measurements',
                 'All four studies are animal or in vitro and are '
                  'written in the science field.'],
            ],
            prep='No dose is accepted in an official monograph; '
                 'because neither official list carries a monograph, '
                 'there is no accepted measure, duration or upper '
                 'limit. The sources relied on here give no measure '
                 'for use in humans.',
            science='In the sources available to us there is **no '
                    'study in humans at all.** The Özsayın study '
                    'published in Antioxidants in 2026 measured the '
                    'species’ protective effect against '
                    'gentamicin-induced kidney damage **in rats.** '
                    'The Özdemir study published in Food and Chemical '
                    'Toxicology in 2017 measured the anticancer '
                    'activity of the species’ extracts **in vitro.** '
                    'The Sahin study published in Cellular and '
                    'Molecular Biology in 2019 evaluated brain '
                    'acetylcholinesterase activity and oxidative '
                    'stress **in male rats orally exposed to lead '
                    'acetate.** The Güzel '
                    'study published in Chemistry & Biodiversity in '
                    '2023 examines the relationship between phenolic '
                    'content determined by LC/MS/MS and antioxidant '
                    'capacity. **Kidney protection measured in a rat '
                    'or anticancer activity measured in vitro is not '
                    'an effect in a human being;** no use is derived '
                    'from them in this record.',
            safety='⚠️ **This species’ essential oil is very rich in '
                   'pulegone, and that is the most important safety '
                   'fact in this record.** The Özsayın study '
                   'published in Antioxidants in 2026 analysed the '
                   'oil by GC-MS and identified **pulegone as its '
                   'major constituent, at 79.6 per cent**; the same '
                   'study’s animal arm was carried out with isolated '
                   'pulegone itself. That proportion is **higher** '
                   'than those measured in this catalogue’s '
                   '[[tasnanesi]] record (42.81 and 58.5 per cent). '
                   'According to the EMA’s public statement on '
                   'pulegone and menthofuran (2016) the principal '
                   'target organ of these substances is the liver; '
                   'the International Agency for Research on Cancer '
                   'classifies pulegone in group 2B (possibly '
                   'carcinogenic to humans), and the EMA recommends '
                   'an acceptable limit for the sum of pulegone and '
                   'menthofuran in herbal medicines of **0.75 mg/kg '
                   'body weight per day** — 37.5 mg a day for a '
                   '50 kg adult, and less in children by body '
                   'weight. **The essential oil must not be '
                   'drunk;** drinking about 10 ml of pennyroyal oil, '
                   'which is high in pulegone, has caused moderate '
                   'to severe poisoning, and more than 15 ml has '
                   'caused death. Medicinal use of the plant should '
                   'be avoided in pregnancy, while breastfeeding and '
                   'in children; people with liver disease should '
                   'stay away from strong teas and extracts. If the '
                   'essential oil has been swallowed, call 114 (the '
                   'National Poison Information Centre of Türkiye) '
                   'or 112. '
                   '**This restriction is component-based, not '
                   'genus-based:** the pulegone limit depends not on '
                   'which genus the plant belongs to but on how much '
                   'pulegone its oil contains. Beyond this, the '
                   'sources relied on here contain no safety '
                   'assessment in humans for the species and no '
                   'separate study for pregnancy, breastfeeding, '
                   'children or drug interactions. **What is written '
                   'for mint does not belong to this species '
                   'either:** the EMA monograph behind this '
                   'catalogue’s [[nane]] record is for *Mentha × '
                   'piperita*, and this species is in a separate '
                   'genus — but on pulegone this species sides not '
                   'with mint but with [[yarpuz]]. Because the species’ range is, according '
                   'to Kew, Türkiye alone, **the conservation '
                   'implications of wild gathering should also be '
                   'considered;** the sources relied on here contain '
                   'no assessment giving the species’ conservation '
                   'status.',
            fact='A plant that grows only in Türkiye takes its name '
                 'from a genus it does not belong to: it is called '
                 '"dağ nanesi" (mountain mint), but it is '
                 '*Cyclotrichium*, not *Mentha*. Yet the genus being '
                 'separate does not make this plant safer than mint '
                 '— the opposite: mint’s monograph does not carry '
                 'over, but pulegone, which mint does not contain, '
                 'makes up 79.6 per cent of this species’ oil. So '
                 'what the name misreports is not the genus but the '
                 'risk: this plant resembles mint in its scent and '
                 '[[yarpuz]] in its chemistry.',
            season='The sources relied on here give no collection '
                   'calendar for Türkiye.',
            habitat='According to Kew’s records its natural range '
                    'covers a single region: Türkiye. A range this '
                    'narrow makes the species endemic to Türkiye.',
            local='dağ nanesi',
            confusion='**Despite the "nane" (mint) in its name it is '
                      'not in the genus *Mentha*;** this catalogue’s '
                      '[[nane]], [[yarpuz]], [[sunanesi]] and '
                      '[[japonnanesi]] records are *Mentha* species, '
                      'and their monographs, doses and restrictions '
                      'do not belong to this species. '
                      '[[dagcayistachys]] (*Stachys '
                      'lavandulifolia*), gathered under the name '
                      '"dağ çayı", is also a separate genus. '
                      '**It is also confused with this '
                      'catalogue’s [[dagreyhani]] (*Ziziphora '
                      'clinopodioides*)** — another separate genus '
                      'that also carries pulegone; none of these '
                      '"dağ"-prefixed names denotes a genus.',
        ),
    ),
]
