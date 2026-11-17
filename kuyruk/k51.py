# DSÖ partisi II (10–12 Ocak 2027): guggul, ipeka, kutki.
from kunye_elle import who_url
Q = [

    dict(
        yayin='2027-01-10',
        id='guggul',
        foto='',
        tr='Guggul (Hint mürü)',
        la='Commiphora wightii (Arn.) Bhandari',
        fam='Burseraceae',
        diger='DSÖ monografı Gummi Gugguli (Cilt 3) türü Commiphora mukul '
              'adıyla veriyor; POWO kabul edilen adı C. wightii. Sanskritçe '
              'guggulu; İngilizce guggul, Indian bdellium, Indian myrrh. '
              'Kullanılan kısım **gövde ve dallardan akan oleo-sakız reçine**. '
              'TİTCK ve AB monografı yok. Kataloğumuzdaki mür (C. myrrha) aynı '
              'cins; Hint günlüğü (Boswellia) adlar listesinde "guggul" diye de '
              'anılır — karışma. Tür IUCN’de "kritik tehlikede".',
        bolge=['asya'],
        kat=['sifa', 'tutsu'],
        kisim='Oleo-sakız reçinesi (ham ve standardize özüt, "guggulipid")',
        taxon='Commiphora wightii',
        kul=[
            ['DSÖ — kolesterol', 'DSÖ monografı guggulu "klinik verilerle '
             'desteklenen kullanım" başlığında veriyor: **hiperlipidemi ve '
             'hiperkolesterolemi tedavisi** — Hindistan’da 1980’lerde yapılan '
             'çalışmalara dayanarak. Farmakope kullanımları: ateroskleroz, '
             'romatizma, öksürük, boğaz ağrısı, menopoz belirtileri, adet '
             'söktürücü. Geleneksel: balgam söktürücü, ishal, halsizlik, '
             'sarılık; deriye yanıkta; böcek kovucu. Doz: reçine günde 3–4,5 g '
             'iki-üç dozda; petrol eteri özütü 500 mg günde iki-üç kez. '
             'Kontrendikasyon: gebelik (adet söktürücü). Yan etki: hafif ishal, '
             'huzursuzluk; bir çalışmada yüzde 17,5 mide şikâyeti.'],
            ['Hindistan — Ayurveda’nın reçinesi', 'Guggul Hindistan’ın '
             'kuzeybatı çöllerine (Rajasthan, Gujarat) yerli; Ayurveda’da '
             'Sushruta Samhita’dan beri (MÖ 600) "medoroga" (yağ bozukluğu, '
             'şişmanlık) ve eklem için; tapınak tütsüsü ve Vedik ateş '
             'ritüelinin (yajna) yakıtı. Aşırı reçine hasadı ağacı 2015’te '
             'IUCN "kritik tehlikede" listesine soktu; Hindistan dikim '
             'programları yürütüyor — kataloğumuzda ilaç olmanın bedelini '
             'ödeyen bitkilerden.'],
            ['JAMA 2003 — ters sonuç', 'DSÖ monografının yayımından önce, 2003’te '
             'JAMA’da Pennsylvania Üniversitesi’nin randomize çalışması (103 '
             'kişi, 8 hafta) standart ve yüksek doz guggulipidin LDL '
             'kolesterolü düşürmediğini, tersine plaseboya göre yüzde 4–5 '
             '**yükselttiğini** ve altı katılımcıda aşırı duyarlılık döküntüsü '
             'yaptığını buldu. Yazarlar Hindistan çalışmalarıyla farkı diyet '
             've popülasyona bağlıyor. DSÖ monografı (2007) bu çalışmayı '
             'Batı’daki olumsuz veriyi not ederek anıyor.'],
        ],
        haz='DSÖ: ham reçine günde 3–4,5 g bölünmüş; standardize özüt 500 mg '
            'günde iki-üç kez. Gebelikte kullanılmaz. Türkiye’de ürün yok; '
            'ithal kapsüller standardize olmayabilir. Tütsü olarak yakılması '
            'tıbbi kullanım değildir.',
        bilim='Guggul, kataloğumuzda DSÖ ile JAMA’nın çeliştiği kayıt. DSÖ '
              '"klinik veri" statüsünü Hindistan’da 1980’lerde yapılan '
              'çalışmalara veriyor; 2003 JAMA çalışması — Batı’daki tek büyük '
              'randomize çalışma — LDL’nin düşmediğini, hatta yükseldiğini '
              'buldu. Mekanizma (guggulsteronların FXR reseptörünü engellemesi) '
              'sağlam, etki çelişkili; diyetin (Hint vejetaryen diyeti ile Batı '
              'diyeti) farkı bir açıklama. Sonraki küçük çalışmalar iki yönde. '
              'Kanıt düzeyini "sınırlı" yazdık: DSÖ’nün "klinik"ini JAMA’nın '
              'olumsuz sonucu dengeliyor.',
        kanit='sinirli',
        guv='orta',
        guvNot='**Gebelikte kontrendike** — DSÖ; geleneksel adet söktürücü. '
               'Emzirme ve çocuk için DSÖ "bilgi yok". **Aşırı duyarlılık '
               'döküntüsü** — JAMA çalışmasında katılımcıların yaklaşık yüzde '
               '6’sında. Mide-bağırsak şikâyeti (ishal, bulantı), huzursuzluk, '
               'baş ağrısı. Tiroid üzerine hayvan verisi (uyarıcı) — tiroid '
               'hastaları hekime söylemeli. Kanama eğilimini artırabilir '
               '(trombosit etkisi); cerrahi öncesi kesilmeli. Güvenlik düzeyi '
               '"orta".',
        etk=[
            ['Propranolol ve diltiazem',
             'İnsan çalışmasında guggulipid bu iki ilacın biyoyararlanımını '
             'azalttı; DSÖ monografında değil, literatürden. Kalp ilacı '
             'kullananlar dikkat.'],
            ['Antikoagülanlar ve antiplatelet ilaçlar (kuramsal)',
             'Trombosit agregasyonunu azalttığına dair veri; kanama riski.'],
            ['Statinler ve tiroid ilaçları (kuramsal)',
             'Aynı amaçla birlikte kullanım izlenmeli; tiroid uyarıcı hayvan '
             'verisi levotiroksin dozunu etkileyebilir.'],
        ],
        ilginc='Vedik ateşin yakıtı, Ayurveda’nın yağ ilacı, DSÖ’nün '
               '"klinik kanıtlı" kolesterol düşürücüsü — ve JAMA’da LDL’yi '
               'yükselten reçine. İki sonuç da doğru olabilir: Hint '
               'diyetinde işleyen, Amerikan diyetinde ters tepen bir molekül. '
               'Bu arada ağaç "kritik tehlikede": reçinesi için o kadar '
               'çizildi ki çölden kaybolmak üzere. Kanıt kadar hasat da '
               'tartışmalı.',
        ek=dict(
            mevsim='Reçine kış aylarında (Kasım–Ocak) gövde çizilerek alınır; '
                   'sürdürülebilir sağım için ağaç 8–10 yaşında olmalı.',
            yetisme='Hindistan’ın kuzeybatı kurak bölgeleri (Rajasthan, '
                    'Gujarat) ve Pakistan; çalı ya da küçük ağaç. Türkiye’de '
                    'yetişmez.',
            yoresel='Guggul, Hint mürü, bdellium; Sanskritçe guggulu. Yöresel ad '
                    'yok.',
            karisma='⚠️ Mür (C. myrrha) aynı cins, ayrı reçine ve kayıt. Hint '
                    'günlüğü (Boswellia serrata) "guggul" adıyla da satılır — '
                    'DSÖ her ikisinin adlar listesine almış; ayrı kayıt. '
                    'Piyasadaki "guggul" özütleri tağşişe açık.',
        ),
        ema=[],
        kaynak=[
            ['Gummi Gugguli, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 3, 2007',
             who_url(3, 'gummi-gugguli')],
            ['P. O. Szapary ve ark., “Guggulipid for the treatment of '
             'hypercholesterolemia: a randomized controlled trial”, JAMA '
             '290(6), 2003',
             'https://pubmed.ncbi.nlm.nih.gov/12915429/'],
        ],
        rel=['mur', 'hintgunlugu', 'akgunluk', 'enginar'],
        en=dict(
            name='Guggul (Indian myrrh)',
            other='The WHO monograph Gummi Gugguli (Volume 3) gives the species '
                  'as Commiphora mukul; POWO’s accepted name is C. wightii. '
                  'Sanskrit guggulu; English guggul, Indian bdellium, Indian '
                  'myrrh. The part is **the oleo-gum resin exuded from stems and '
                  'branches**. No Turkish or EU monograph. The myrrh (C. myrrha) '
                  'in this catalog is the same genus; Indian frankincense '
                  '(Boswellia) is also called "guggul" in its name list — '
                  'confusion. The species is "critically endangered" on the '
                  'IUCN list.',
            part='The oleo-gum resin (crude, and standardised extract, '
                 '"guggulipid")',
            uses=[
                ['WHO — cholesterol', 'The WHO monograph places guggul under '
                 '"uses supported by clinical data": **treatment of '
                 'hyperlipidaemia and hypercholesterolaemia** — on the basis of '
                 'Indian trials of the 1980s. Pharmacopoeial uses: '
                 'atherosclerosis, rheumatism, cough, sore throat, menopausal '
                 'symptoms, emmenagogue. Traditional: expectorant, diarrhoea, '
                 'fatigue, jaundice; topically for burns; insect repellent. '
                 'Dose: resin 3–4.5 g a day in two or three doses; petroleum '
                 'ether extract 500 mg two or three times a day. '
                 'Contraindication: pregnancy (emmenagogue). Adverse effects: '
                 'mild diarrhoea, restlessness; 17.5% stomach complaints in one '
                 'trial.'],
                ['India — Ayurveda’s resin', 'Guggul is native to the '
                 'north-western deserts of India (Rajasthan, Gujarat); in '
                 'Ayurveda since the Sushruta Samhita (600 BCE) for "medoroga" '
                 '(fat disorder, obesity) and the joints; a temple incense and '
                 'the fuel of the Vedic fire ritual (yajna). Over-tapping of the '
                 'resin put the tree on the IUCN "critically endangered" list in '
                 '2015; India runs planting programmes — one of the plants in '
                 'this catalog paying the price of being a drug.'],
                ['JAMA 2003 — the reverse result', 'Before the WHO monograph '
                 'was published, a 2003 University of Pennsylvania randomised '
                 'trial in JAMA (103 people, 8 weeks) found that standard- and '
                 'high-dose guggulipid did not lower LDL cholesterol but '
                 '**raised** it 4–5% against placebo, and caused a '
                 'hypersensitivity rash in six participants. The authors '
                 'attribute the difference from the Indian trials to diet and '
                 'population. The WHO monograph (2007) cites this trial, noting '
                 'the negative Western data.'],
            ],
            prep='WHO: crude resin 3–4.5 g a day divided; standardised extract '
                 '500 mg two or three times a day. Not used in pregnancy. No '
                 'product in Turkey; imported capsules may not be standardised. '
                 'Burning it as incense is not medicinal use.',
            science='Guggul is the record in this catalog where the WHO and '
                    'JAMA disagree. The WHO gives "clinical data" status on the '
                    'basis of Indian trials of the 1980s; the 2003 JAMA trial — '
                    'the one large randomised trial in the West — found that '
                    'LDL did not fall and even rose. The mechanism '
                    '(guggulsterones blocking the FXR receptor) is solid, the '
                    'effect contradictory; the difference in diet (Indian '
                    'vegetarian versus Western) is one explanation. Later small '
                    'trials go both ways. We record the evidence level as '
                    'Limited: the WHO’s "clinical" is balanced by JAMA’s '
                    'negative result.',
            safety='**Contraindicated in pregnancy** — WHO; a traditional '
                   'emmenagogue. For lactation and children the WHO says "no '
                   'information". **Hypersensitivity rash** — in about 6% of '
                   'participants in the JAMA trial. Gastrointestinal complaints '
                   '(diarrhoea, nausea), restlessness, headache. Animal data on '
                   'the thyroid (stimulant) — thyroid patients should tell their '
                   'doctor. It may increase bleeding tendency (platelet effect); '
                   'stop before surgery. Safety level Medium.',
            fact='Fuel of the Vedic fire, Ayurveda’s fat remedy, the WHO’s '
                 '"clinically evidenced" cholesterol-lowerer — and the resin '
                 'that raised LDL in JAMA. Both results may be true: a molecule '
                 'that works on an Indian diet and backfires on an American one. '
                 'Meanwhile the tree is "critically endangered": scored so often '
                 'for its resin that it is about to vanish from the desert. The '
                 'harvest is as contested as the evidence.',
            season='The resin is taken in the winter months (November–January) '
                   'by scoring the trunk; for sustainable tapping the tree must '
                   'be 8–10 years old.',
            habitat='The arid north-west of India (Rajasthan, Gujarat) and '
                    'Pakistan; a shrub or small tree. Does not grow in Turkey.',
            local='Guggul, Hint mürü, bdellium; Sanskrit guggulu. No regional '
                  'names.',
            confusion='⚠️ Myrrh (C. myrrha) is the same genus, a separate resin '
                      'and record. Indian frankincense (Boswellia serrata) is '
                      'also sold as "guggul" — the WHO lists the name under '
                      'both; a separate record. Market "guggul" extracts are '
                      'open to adulteration.',
        ),
        etk_en=[
            ['Propranolol and diltiazem',
             'In a human study guggulipid reduced the bioavailability of both '
             'drugs; not in the WHO monograph, from the literature. Care for '
             'anyone on heart medication.'],
            ['Anticoagulants and antiplatelet drugs (theoretical)',
             'Data that it reduces platelet aggregation; bleeding risk.'],
            ['Statins and thyroid drugs (theoretical)',
             'Combined use for the same purpose should be monitored; the '
             'thyroid-stimulant animal data may affect levothyroxine dosing.'],
        ],
    ),

    dict(
        yayin='2027-01-11',
        id='ipeka',
        foto='',
        tr='İpeka (kusturucu kök)',
        la='Carapichea ipecacuanha (Brot.) L.Andersson',
        fam='Rubiaceae (kökboyasıgiller)',
        diger='DSÖ monografı Radix Ipecacuanhae (Cilt 3) türü Cephaelis '
              'ipecacuanha adıyla veriyor; POWO kabul edilen adı Carapichea '
              'ipecacuanha. Tupi i-pe-kaa-guéne, "yol kenarında kusturan '
              'bitki"; İngilizce ipecac. Kullanılan kısım **kurutulmuş kök ve '
              'rizom**. TİTCK ve AB monografı yok. Bir asır boyunca her evin '
              'ecza dolabındaki "ipeka şurubu"; bugün toksikoloji dernekleri '
              '"rutin kullanılmasın" diyor.',
        bolge=['amazon', 'kamerika'],
        kat=['sifa', 'zehir'],
        kisim='Kurutulmuş kökü ve rizomu (şurup olarak)',
        taxon='Carapichea ipecacuanha',
        kul=[
            ['DSÖ — zehirlenmede kusturucu', 'DSÖ monografı ipekayı "klinik '
             'verilerle desteklenen kullanım" başlığında veriyor: kökten '
             'yapılan şurup **zehir yutulduğunda mideyi boşaltmak için '
             'kusturucu**. Geleneksel: parazit, soğuk algınlığı, ishal; rahim '
             'kasılması ve düşük. Kontrendikasyonlar ayrıntılı: aşındırıcı '
             'zehir (asit, alkali), petrol ürünleri, bilinç bulanıklığı ya da '
             'koma (aspirasyon), merkezi sinir sistemi uyarıcısı yutulması '
             '(kusma nöbet tetikler), striknin. **Uyarı: sıvı ekstre şurubun 14 '
             'katı güçlüdür ve şurup yerine verildiğinde ölümler olmuştur.** '
             'Doz: erişkin şurup 15–30 ml, 20–30 dakikada kusma olmazsa bir '
             'kez tekrar; bol su ile. 6 aydan küçükte yalnızca hekim '
             'gözetiminde.'],
            ['Brezilya — Tupi bilgisi ve Paris’in sırrı', 'Bitki Brezilya’nın '
             'Atlantik ormanına yerli; Tupi-Guarani halkları kökünü ishal ve '
             'dizanteri için kullanırdı — adı Tupi dilinden. 1680’lerde '
             'Paris’e geldi; Hollandalı hekim Helvetius kökü "dizanterinin '
             'gizli ilacı" olarak XIV. Louis’ye sattı; 18. yüzyılda Dover '
             'tozunun (ipeka + afyon) bileşeni oldu. Emetin alkaloidi 1817’de '
             'izole edildi ve 20. yüzyılda amipli dizanteri ilacı olarak '
             'kullanıldı; bugün yerini güvenli ilaçlara bıraktı.'],
            ['Toksikolojinin dönüşü', 'ABD’de 1965’ten sonra her evin ecza '
             'dolabında ipeka şurubu bulundurulması önerildi. 2004 ve 2013 '
             'Amerikan ve Avrupa klinik toksikoloji derneklerinin ortak '
             'pozisyon belgesi tabloyu tersine çevirdi: ipekanın zehirlenen '
             'hastanın sonucunu iyileştirdiğine dair ikna edici kanıt yok; '
             'aktif kömürü ve antidotları geciktiriyor; **"olay yerinde ya da '
             'acil serviste rutin uygulanmasından kesinlikle kaçınılmalı"**. '
             'Amerikan Pediatri Akademisi 2003’te evlerdeki şurupların '
             'atılmasını önerdi.'],
        ],
        haz='Bu kayıt doz vermiyor: ipeka ancak zehir danışma merkezi ya da '
            'hekim talimatıyla ve yalnızca şurup biçiminde kullanılır. Evde '
            'bulundurulması artık önerilmiyor (2003 AAP, 2013 pozisyon '
            'belgesi). Kök çayı, toz ya da tentür ağızdan alınmaz — emetin '
            'kalbe toksiktir. Bulimia ve kilo verme amaçlı kullanım ölümcül '
            'kardiyomiyopati yapmıştır.',
        bilim='İpeka, kataloğumuzda DSÖ’nün "klinik kanıt" dediği ama uzmanlık '
              'derneklerinin "kullanmayın" dediği kayıt — ikisi de doğru: '
              'kusturduğu kesin (klinik kanıt), kusturmanın hastaya yararı '
              'kanıtlanamadı (pozisyon belgesi). 2013 güncellemesi literatürde '
              '"anlamlı makale sayısının sınırlı" olduğunu, ipekanın aktif '
              'kömür ve antidotların etkisini azalttığını ve ürünün piyasadan '
              'çekildiğini yazıyor. DSÖ monografı (2007) uyarılarında bu '
              'tartışmayı yansıtıyor. Kanıt düzeyi "klinik" — etki için; '
              'güvenlik "düşük".',
        kanit='klinik',
        guv='dusuk',
        guvNot='**Yalnızca zehir danışma/hekim talimatıyla, yalnızca şurup.** '
               'Sıvı ekstre 14 kat güçlüdür — ölümcül karışıklık (DSÖ). '
               'Kontrendike: aşındırıcı ve petrol türevi zehirler, bilinç '
               'bulanıklığı/koma, nöbet yapabilecek zehirler, striknin, '
               'kanama eğilimi, kalp hastalığı. Büyük dozda kanlı kusma ve '
               'ishal, tüm sindirim kanalında mukoza erozyonu; kusma olmazsa '
               'emilen emetin **kalp iletim bozukluğu ve kardiyomiyopati** '
               'yapar. **Kronik kötüye kullanım (yeme bozukluğu) ölümcül.** '
               'Gebelikte kullanılmaz (geleneksel düşük yapıcı); 6 aydan '
               'küçükte hekim gözetimi. Aspirasyon pnömonisi riski. Güvenlik '
               'düzeyi "düşük".',
        etk=[
            ['Aktif kömür',
             'DSÖ: kömürle birlikte ya da kömürden sonra verilirse kusturucu '
             'etki gecikir ya da azalır; pozisyon belgesi: ipeka kömürün '
             'etkisini azaltır — iki tedavi birbirini bozar.'],
            ['Ağızdan antidotlar',
             'Pozisyon belgesi: ipeka ağızdan verilen panzehirleri kusturarak '
             'etkisizleştirir.'],
            ['Süt',
             'DSÖ: sütün kusmayı azalttığı sanılırdı; 500 çocukluk çalışmada '
             'fark bulunmadı.'],
            ['Kalbe etkili ilaçlar (kuramsal)',
             'Emetin kalp iletimini bozar; antiaritmik ve QT uzatan ilaçlarla '
             'risk artar.'],
        ],
        ilginc='Tupi halkının "yol kenarında kusturan" kökü, XIV. Louis’nin '
               'dizanteri sırrı, Amerikan evlerinin kırk yıllık ecza dolabı '
               'şurubu — ve 2013’te toksikologların "kesinlikle kaçının" '
               'dediği ilaç. DSÖ "klinik kanıt" diyor: evet, kusturur. '
               'Pozisyon belgesi: kusturmak işe yaramıyor. Kataloğumuzda bir '
               'ilacın etkili olup yararsız olabileceğinin en net örneği.',
        ek=dict(
            mevsim='Kök yıl boyu sökülür; bitki 3–4 yaşında hasat olgunluğuna '
                   'gelir. Küçük beyaz çiçekler, mor-siyah meyveler.',
            yetisme='Brezilya’nın Atlantik ormanı ve Orta Amerika’nın nemli '
                    'gölgeli ormanları; Hindistan ve Malezya’da tarımı. '
                    'Türkiye’de yetişmez.',
            yoresel='İpeka, ipekakuana, kusturucu kök; Tupi i-pe-kaa-guéne. '
                    'Yöresel ad yok.',
            karisma='⚠️ Şurup ile sıvı ekstre (fluidextract) karıştırılmamalı — '
                    'DSÖ ölümcül olduğunu yazıyor. Kartagena ipekası (C. '
                    'acuminata) DSÖ’de aynı drog. "Yalancı ipeka" adıyla '
                    'satılan başka kökler var.',
        ),
        ema=[],
        kaynak=[
            ['Radix Ipecacuanhae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 3, 2007',
             who_url(3, 'radix-ipecacuanhae')],
            ['J. Höjer ve ark., “Position paper update: ipecac syrup for '
             'gastrointestinal decontamination”, Clinical Toxicology 51(3), '
             '2013',
             'https://pubmed.ncbi.nlm.nih.gov/23406298/'],
        ],
        rel=['senega', 'hintyagi', 'kahve'],
        en=dict(
            name='Ipecac',
            other='The WHO monograph Radix Ipecacuanhae (Volume 3) gives the '
                  'species as Cephaelis ipecacuanha; POWO’s accepted name is '
                  'Carapichea ipecacuanha. Tupi i-pe-kaa-guéne, "roadside plant '
                  'that makes you vomit". The part is **the dried root and '
                  'rhizome**. No Turkish or EU monograph. For a century the '
                  '"ipecac syrup" in every home medicine cabinet; today the '
                  'toxicology societies say "not for routine use".',
            part='The dried root and rhizome (as syrup)',
            uses=[
                ['WHO — emetic in poisoning', 'The WHO monograph places ipecac '
                 'under "uses supported by clinical data": a syrup made from '
                 'the root **as an emetic to empty the stomach after poison '
                 'ingestion**. Traditional: parasites, colds, diarrhoea; '
                 'uterine contractions and abortion. Contraindications are '
                 'detailed: corrosive poisons (acid, alkali), petroleum '
                 'products, impaired consciousness or coma (aspiration), '
                 'ingestion of a central nervous stimulant (vomiting triggers '
                 'convulsions), strychnine. **Warning: the fluidextract is 14 '
                 'times stronger than the syrup, and deaths have occurred when '
                 'it was given in its place.** Dose: adults 15–30 ml of syrup, '
                 'repeated once if no vomiting in 20–30 minutes; with copious '
                 'water. Under 6 months only under medical supervision.'],
                ['Brazil — Tupi knowledge and the secret of Paris', 'The plant '
                 'is native to Brazil’s Atlantic forest; the Tupi-Guarani '
                 'peoples used its root for diarrhoea and dysentery — the name '
                 'is from Tupi. It reached Paris in the 1680s; the Dutch '
                 'physician Helvetius sold the root to Louis XIV as the '
                 '"secret remedy for dysentery"; in the 18th century it became '
                 'an ingredient of Dover’s powder (ipecac + opium). The '
                 'alkaloid emetine was isolated in 1817 and used in the 20th '
                 'century as a drug for amoebic dysentery; it has since given '
                 'way to safer drugs.'],
                ['Toxicology’s reversal', 'In the US after 1965 every home '
                 'was advised to keep ipecac syrup in the medicine cabinet. The '
                 '2004 and 2013 joint position papers of the American and '
                 'European clinical toxicology societies reversed the picture: '
                 'no convincing evidence that ipecac improves the outcome of '
                 'poisoned patients; it delays activated charcoal and '
                 'antidotes; **"routine administration at the site of '
                 'ingestion or in the emergency department should definitely '
                 'be avoided"**. The American Academy of Pediatrics advised in '
                 '2003 that home syrups be discarded.'],
            ],
            prep='This record gives no dose: ipecac is used only on the '
                 'instruction of a poison centre or doctor, and only as syrup. '
                 'Keeping it at home is no longer recommended (AAP 2003, 2013 '
                 'position paper). Root tea, powder or tincture are not taken by '
                 'mouth — emetine is cardiotoxic. Use for bulimia or weight loss '
                 'has caused fatal cardiomyopathy.',
            science='Ipecac is the record in this catalog where the WHO says '
                    '"clinical evidence" and the specialist societies say "do '
                    'not use" — both are right: that it causes vomiting is '
                    'certain (clinical evidence); that vomiting benefits the '
                    'patient could not be proven (position paper). The 2013 '
                    'update writes that "meaningful articles" in the literature '
                    'are few, that ipecac reduces the effectiveness of activated '
                    'charcoal and antidotes, and that the product is '
                    'disappearing from the market. The WHO monograph (2007) '
                    'reflects this debate in its warnings. Evidence level '
                    'Clinical — for the effect; safety Low.',
            safety='**Only on poison-centre/doctor instruction, only as '
                   'syrup.** The fluidextract is 14 times stronger — a fatal '
                   'mix-up (WHO). Contraindicated: corrosive and petroleum '
                   'poisons, impaired consciousness/coma, poisons that may '
                   'cause seizures, strychnine, bleeding tendency, heart '
                   'disease. Bloody vomiting and diarrhoea in large doses, '
                   'mucosal erosion of the whole gut; if vomiting fails, '
                   'absorbed emetine causes **cardiac conduction disturbance '
                   'and cardiomyopathy**. **Chronic misuse (eating disorders) '
                   'is fatal.** Not used in pregnancy (a traditional '
                   'abortifacient); medical supervision under 6 months. Risk of '
                   'aspiration pneumonia. Safety level Low.',
            fact='The Tupi’s "roadside root that makes you vomit", Louis '
                 'XIV’s dysentery secret, forty years of the American home '
                 'medicine cabinet — and in 2013 the drug toxicologists said to '
                 '"definitely avoid". The WHO says "clinical evidence": yes, it '
                 'makes you vomit. The position paper: vomiting does not help. '
                 'The clearest example in this catalog that a drug can be '
                 'effective and useless at once.',
            season='The root is lifted year-round; the plant reaches harvest '
                   'maturity at 3–4 years. Small white flowers, purple-black '
                   'fruit.',
            habitat='Brazil’s Atlantic forest and the damp shady forests of '
                    'Central America; cultivated in India and Malaysia. Does '
                    'not grow in Turkey.',
            local='İpeka, ipekakuana, kusturucu kök; Tupi i-pe-kaa-guéne. No '
                  'regional names.',
            confusion='⚠️ Syrup and fluidextract must not be confused — the WHO '
                      'writes that it is fatal. Cartagena ipecac (C. acuminata) '
                      'is the same drug in the WHO. Other roots are sold as '
                      '"false ipecac".',
        ),
        etk_en=[
            ['Activated charcoal',
             'WHO: given with or after charcoal, the emetic effect is delayed '
             'or reduced; position paper: ipecac reduces charcoal’s '
             'effectiveness — the two treatments spoil each other.'],
            ['Oral antidotes',
             'Position paper: ipecac neutralises oral antidotes by causing '
             'vomiting.'],
            ['Milk',
             'WHO: milk was believed to reduce vomiting; no difference was '
             'found in a study of 500 children.'],
            ['Cardioactive drugs (theoretical)',
             'Emetine disturbs cardiac conduction; risk rises with '
             'antiarrhythmics and QT-prolonging drugs.'],
        ],
    ),

    dict(
        yayin='2027-01-12',
        id='kutki',
        foto='',
        tr='Kutki (Himalaya centiyanı)',
        la='Picrorhiza kurroa Royle ex Benth.',
        fam='Plantaginaceae (sinirotugiller; DSÖ Scrophulariaceae yazıyor)',
        diger='DSÖ monografı Rhizoma Picrorhizae (Cilt 4) iki türü birlikte '
              'kapsıyor: Picrorhiza kurroa ve Neopicrorhiza scrophulariiflora. '
              'Hintçe kutki, kutaki; Sanskritçe katuka ("acı"); Çince hu huang '
              'lian. Kullanılan kısım **kurutulmuş rizom ve kök**. TİTCK ve AB '
              'monografı yok. Himalaya’nın 3000–5000 m’sinden; aşırı hasatla '
              'tehlike altında (CITES Ek II).',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Kurutulmuş rizomu ve kökü',
        taxon='Picrorhiza kurroa',
        kul=[
            ['DSÖ — ateş, bağışıklık, deri', 'DSÖ monografı "klinik verilerle '
             'desteklenen kullanım: yok" diyor; farmakope kullanımı (Hindistan '
             'Ayurveda Farmakopesi, Çin Farmakopesi): ağızdan **ateş, bağışıklık '
             'bozuklukları ve deri hastalıkları**. Monograf, bronşiyal astım ve '
             'viral hepatit için iki çalışmanın "olası rol" gösterdiğini ama '
             'randomize kontrollü çalışma yapılmadığını açıkça yazıyor. Doz: '
             'günde 1–3 g toz rizom. Kontrendikasyon, uyarı, yan etki: "bilgi '
             'bulunamadı". Gebelikte hayvan verisi düşük yapmadığını '
             'gösteriyor; insan verisi yok.'],
            ['Himalaya — Ayurveda’nın acı kökü', 'Kutki Hindistan, Nepal ve '
             'Tibet’in yüksek Himalaya’sına yerli; Ayurveda’da karaciğer ve '
             'safra için "acı tonik", ateş düşürücü ve müshil; Tibet tıbbında '
             '(hong len) ateş ve iltihap; Çin tıbbında hu huang lian ("yabancı '
             'huang lian" — Coptis’in ikamesi). Yabani toplama türü tehlikeye '
             'soktu; Hindistan ve Nepal’de tarımı deneniyor. Kataloğumuzda '
             'guggul ve Afrika eriği gibi, ilaç olmanın bedelini ödeyen '
             'bitki.'],
            ['Modern derleme', '2022 Molecules derlemesi geleneksel '
             'kullanımları (kabızlık, deri, ateş, sarılık, solunum, alerji) '
             've iridoit glikozitlerinin (pikrozit I–II, kutkin) laboratuvar '
             'etkilerini topluyor: karaciğer koruyucu, antienflamatuvar, '
             'bağışıklık düzenleyici; "silimarin benzeri" karaciğer etkisi '
             'hayvanda belgelenmiş. Hindistan’da küçük insan çalışmaları '
             '(akut viral hepatit, vitiligo, astım) 1980–90’lardan ve '
             'tekrarlanmamış.'],
        ],
        haz='DSÖ: günde 1–3 g toz rizom. Çok acıdır; Ayurveda’da bal ya da '
            'şekerle verilir. Gebelik, emzirme ve çocuk için DSÖ veri '
            'vermiyor — kullanılmaz. Türkiye’de ürün yok; ithal Ayurveda '
            'preparatlarında ("Kutki", "Katuki") bulunur. Yabani kökenli '
            'ürün tehlike altındaki türden toplanmıştır; kültür kaynağı '
            'tercih edilmeli.',
        bilim='Kutki, DSÖ’nün "klinik veri yok" dediği ama 1980–90’ların '
              'Hindistan çalışmalarını (astım, hepatit) "olası rol" diye not '
              'ettiği bitki. 2022 derlemesi geniş bir laboratuvar literatürü '
              'topluyor; karaciğer koruyucu etkisi hayvanda tutarlı, insanda '
              'küçük ve eski çalışmalarla sınırlı. Pikrozitlerin '
              'farmakolojisi ilgi çekici, kanıt henüz yok. Kanıt düzeyi '
              '"geleneksel". Güvenlik "orta" — DSÖ’nün "bilgi yok"ları '
              'güvenli demek değil, çalışılmadı demek.',
        kanit='geleneksel',
        guv='orta',
        guvNot='DSÖ monografı kontrendikasyon, uyarı ve yan etki için "bilgi '
               'bulunamadı" diyor — veri yokluğu. Gebelik, emzirme ve çocukta '
               'kullanılmaz (veri yok). Çok acı; mide hassasiyetinde bulantı, '
               'yüksek dozda ishal (müshil geleneği). Ayurveda preparatlarında '
               'ağır metal kirliliği bildirilmiştir — kaynak belgeli olmalı. '
               'Karaciğer hastalığında "karaciğer koruyucu" diye hekimsiz '
               'kullanılmaz. Güvenlik düzeyi "orta".',
        etk=[
            ['Bilinen etkileşim verisi yok (DSÖ)',
             'Monograf etkileşim bölümü boş. Bağışıklık düzenleyici laboratuvar '
             'etkisi nedeniyle immünsüpresanlarla kuramsal çelişki; '
             'karaciğerde metabolize olan ilaçlarla veri yok.'],
        ],
        ilginc='Himalaya’nın 4000 metresinden toplanan acı kök Ayurveda’nın '
               'karaciğer tonigi, Tibet’in ateş ilacı, Çin’in "yabancı '
               'Coptis"i — ve DSÖ monografının neredeyse her güvenlik '
               'başlığında "bilgi bulunamadı". Üç tıp geleneği binlerce '
               'yıldır kullanıyor, bilim henüz bakmamış. Kök ise bakılmayı '
               'bekleyemeyecek kadar hızlı tükeniyor: CITES listesinde.',
        ek=dict(
            mevsim='Kısa yaz; rizom Eylül–Ekim’de, bitki tohum verdikten '
                   'sonra sökülür.',
            yetisme='Himalaya’nın alpin çayırları ve kaya yarıkları, 3000–5000 '
                    'm (Hindistan, Nepal, Butan, Tibet). Türkiye’de yetişmez.',
            yoresel='Kutki, kutaki, katuki (Hintçe); hong len (Tibetçe); hu '
                    'huang lian (Çince). Yöresel ad yok.',
            karisma='⚠️ Neopicrorhiza scrophulariiflora DSÖ’de aynı drog, ayrı '
                    'tür. Huang lian (Coptis) Çin’de ayrı drog; "hu huang lian" '
                    'onun ikamesi. Centiyan (Gentiana) ile "acı kök" olarak '
                    'karışabilir — ayrı familya, ayrı kayıt.',
        ),
        ema=[],
        kaynak=[
            ['Rhizoma Picrorhizae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 4, 2009',
             who_url(4, 'rhizoma-picrorhizae')],
            ['T. M. Almeleebia ve ark., “Pharmacological and Clinical Efficacy of Picrorhiza kurroa and '
             'Its Secondary Metabolites: A Comprehensive Review”, Molecules '
             '27(23), 2022',
             'https://pubmed.ncbi.nlm.nih.gov/36500409/'],
        ],
        rel=['centiyan', 'devedikeni', 'karahindiba'],
        en=dict(
            name='Kutki (Himalayan gentian)',
            other='The WHO monograph Rhizoma Picrorhizae (Volume 4) covers two '
                  'species together: Picrorhiza kurroa and Neopicrorhiza '
                  'scrophulariiflora. Hindi kutki, kutaki; Sanskrit katuka '
                  '("bitter"); Chinese hu huang lian. The part is **the dried '
                  'rhizome and root**. No Turkish or EU monograph. From the '
                  'Himalaya at 3,000–5,000 m; endangered by over-harvesting '
                  '(CITES Appendix II).',
            part='The dried rhizome and root',
            uses=[
                ['WHO — fever, immunity, skin', 'The WHO monograph says "uses '
                 'supported by clinical data: none"; the pharmacopoeial use '
                 '(Ayurvedic Pharmacopoeia of India, Chinese Pharmacopoeia): '
                 'orally for **fever, immune disorders and skin diseases**. '
                 'The monograph writes plainly that two studies suggested a '
                 '"possible role" in bronchial asthma and viral hepatitis but '
                 'that no randomised controlled trial has been done. Dose: 1–3 '
                 'g of powdered rhizome a day. Contraindications, warnings, '
                 'adverse reactions: "no information was found". Animal data '
                 'show no abortion in pregnancy; no human data.'],
                ['The Himalaya — Ayurveda’s bitter root', 'Kutki is native to '
                 'the high Himalaya of India, Nepal and Tibet; in Ayurveda a '
                 '"bitter tonic" for liver and bile, febrifuge and laxative; in '
                 'Tibetan medicine (hong len) for fever and inflammation; in '
                 'Chinese medicine hu huang lian ("foreign huang lian" — the '
                 'substitute for Coptis). Wild collection has endangered the '
                 'species; cultivation is being tried in India and Nepal. Like '
                 'guggul and African cherry in this catalog, a plant paying the '
                 'price of being a drug.'],
                ['Modern review', 'The 2022 Molecules review collects the '
                 'traditional uses (constipation, skin, fever, jaundice, '
                 'breathing, allergy) and the laboratory effects of its '
                 'iridoid glycosides (picroside I–II, kutkin): '
                 'hepatoprotective, anti-inflammatory, immunomodulatory; a '
                 '"silymarin-like" liver effect is documented in animals. The '
                 'small human studies in India (acute viral hepatitis, '
                 'vitiligo, asthma) are from the 1980s–90s and unreplicated.'],
            ],
            prep='WHO: 1–3 g of powdered rhizome a day. Very bitter; given with '
                 'honey or sugar in Ayurveda. The WHO gives no data for '
                 'pregnancy, lactation or children — not used. No product in '
                 'Turkey; found in imported Ayurvedic preparations ("Kutki", '
                 '"Katuki"). Wild-sourced product is gathered from an '
                 'endangered species; cultivated sources should be preferred.',
            science='Kutki is the plant the WHO marks "no clinical data" while '
                    'noting the Indian studies of the 1980s–90s (asthma, '
                    'hepatitis) as a "possible role". The 2022 review collects a '
                    'wide laboratory literature; the hepatoprotective effect is '
                    'consistent in animals, in humans limited to small, old '
                    'studies. The pharmacology of the picrosides is '
                    'interesting; the evidence is not yet there. Evidence level '
                    'Traditional. Safety Medium — the WHO’s "no information" '
                    'entries do not mean safe, they mean unstudied.',
            safety='The WHO monograph says "no information was found" for '
                   'contraindications, warnings and adverse reactions — an '
                   'absence of data. Not used in pregnancy, lactation or '
                   'children (no data). Very bitter; nausea in a sensitive '
                   'stomach, diarrhoea at high dose (the laxative tradition). '
                   'Heavy-metal contamination has been reported in Ayurvedic '
                   'preparations — the source must be documented. Not used '
                   'without a doctor as a "liver protector" in liver disease. '
                   'Safety level Medium.',
            fact='The bitter root gathered at 4,000 metres in the Himalaya is '
                 'Ayurveda’s liver tonic, Tibet’s fever remedy, China’s '
                 '"foreign Coptis" — and "no information was found" under '
                 'nearly every safety heading of the WHO monograph. Three '
                 'medical traditions have used it for thousands of years; '
                 'science has not yet looked. The root, though, is running out '
                 'too fast to wait to be looked at: it is on the CITES list.',
            season='A short summer; the rhizome is lifted in September–October '
                   'after the plant has set seed.',
            habitat='The alpine meadows and rock crevices of the Himalaya at '
                    '3,000–5,000 m (India, Nepal, Bhutan, Tibet). Does not grow '
                    'in Turkey.',
            local='Kutki, kutaki, katuki (Hindi); hong len (Tibetan); hu huang '
                  'lian (Chinese). No regional names.',
            confusion='⚠️ Neopicrorhiza scrophulariiflora is the same drug in '
                      'the WHO, a separate species. Huang lian (Coptis) is a '
                      'separate drug in China; "hu huang lian" is its '
                      'substitute. It can be confused with gentian (Gentiana) as '
                      'a "bitter root" — separate family, separate record.',
        ),
        etk_en=[
            ['No known interaction data (WHO)',
             'The monograph’s interaction section is empty. A theoretical '
             'conflict with immunosuppressants because of the immunomodulatory '
             'laboratory effect; no data with drugs metabolised in the liver.'],
        ],
    ),

]
