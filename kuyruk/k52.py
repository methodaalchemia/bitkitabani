# DSÖ partisi III (13–15 Ocak 2027): Amur mantar ağacı, manolya kabuğu,
# kara kartopu — üçü DSÖ Cilt 4.
from kunye_elle import who_url
Q = [

    dict(
        yayin='2027-01-13',
        id='amurmantaragaci',
        foto='',
        tr='Amur mantar ağacı (huang bai)',
        la='Phellodendron amurense Rupr.',
        fam='Rutaceae (sedefotugiller)',
        diger='DSÖ monografı Cortex Phellodendron (Cilt 4) iki türü kapsıyor: '
              'Phellodendron amurense ve P. chinense. Çince huang bai ("sarı '
              'kabuk"), Japonca ōbaku; İngilizce Amur cork tree. Kullanılan '
              'kısım **kurutulmuş kabuk**. TİTCK ve AB monografı yok. Ana '
              'maddesi berberin — kataloğumuzdaki altın mühür (Hydrastis) ve '
              'kadıntuzluğu (Berberis) ile aynı alkaloit; Çin tıbbının üç '
              '"sarı" drogundan biri.',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Kurutulmuş kabuğu',
        taxon='Phellodendron amurense',
        kul=[
            ['DSÖ — ishal ve idrar yolu', 'DSÖ monografı "klinik verilerle '
             'desteklenen kullanım: yok" diyor; farmakope kullanımı (Çin ve '
             'Japon farmakopeleri): ağızdan **karın ağrısı, ishal, '
             'gastroenterit ve idrar yolu enfeksiyonu**. Monograf dürüst bir '
             'ayrım yapıyor: kabuğun kendisi için klinik çalışma yok, ama ana '
             'bileşeni **berberin** için ishal, göz trahomu ve deri '
             'leishmaniasis’inde klinik çalışmalar var. Geleneksel: yanık, '
             'öksürük, ateş, sarılık, sıtma, deri yarası. Doz: günde 3–10 g. '
             'Kontrendikasyon: alerji. Emzirmede önerilmiyor; çocuk için '
             'bilgi yok. Berberin günde 0,5 g dozda iyi tolere ediliyor.'],
            ['Çin — "üç sarı"', 'Huang bai, huang lian (Coptis) ve huang qin '
             '(Scutellaria) ile birlikte Çin tıbbının "üç sarı" acı-soğuk '
             'drogunu oluşturur; "nem-ısı"yı temizleyen, alt bedenin (idrar '
             'yolu, bağırsak, bacak) iltihabına yönelen kabuk. Japonya’da '
             'ōbaku adıyla mide ilacı (Hyakusō) ve geleneksel bir sarı boya '
             'kaynağı; Amur havzasının (Çin–Rusya sınırı) ağacı, mantarımsı '
             'kalın kabuğundan adını alır.'],
            ['Berberin — molekülün dosyası', 'Berberin bugün Batı’da takviye '
             'olarak "bitkisel metformin" diye satılıyor; 2022 Frontiers in '
             'Pharmacology meta-analizi (37 çalışma, 3048 hasta, çoğu Çin) '
             'berberinin tip 2 diyabette açlık şekerini 0,82 mmol/L ve HbA1c’yi '
             'yüzde 0,63 düşürdüğünü, hipoglisemi riskini artırmadığını buldu. '
             'Bu veri saflaştırılmış berberine aittir; kabuktaki berberin '
             'miktarı değişken, emilimi düşük — DSÖ’nün ayrımı burada önemli.'],
        ],
        haz='DSÖ: günde 3–10 g kuru kabuk, dekoksiyon (Çin reçetelerinde '
            'çoğunlukla karışım içinde). Berberin takviyeleri standardize ve '
            'ayrı ürün; günde 0,5–1,5 g aralığında çalışılmış. Gebelikte '
            'kullanılmaz (berberin — aşağıda). Türkiye’de kabuk yok; berberin '
            'kapsülleri var.',
        bilim='Amur mantar ağacı, DSÖ monografının bitki ile molekülü en net '
              'ayırdığı kayıt: kabuk için klinik çalışma yok, berberin için '
              'var. Berberinin meta-analizleri (2015 J Ethnopharmacol; 2022 '
              'Frontiers) kan şekeri ve lipitlerde tutarlı etki gösteriyor — '
              'ama çalışmalar küçük, çoğu Çin kaynaklı ve tek merkezli; '
              'metformin karşılaştırmaları "eşdeğer" demiyor, "benzer yönde" '
              'diyor. Berberinin DSÖ’nün andığı ishal çalışmaları 1980’lerden. '
              'Kabuğun kendisine atfedilebilecek kanıt "geleneksel"; berberin '
              'takviyesi ayrı değerlendirilmeli. Kanıt düzeyi "geleneksel".',
        kanit='geleneksel',
        guv='orta',
        guvNot='**Gebelikte kullanılmaz** — berberin plasentayı geçer ve '
               'yenidoğanda kernikterus (bilirubin birikimi) riski taşır; DSÖ '
               'emzirmede de önermiyor. Yenidoğan ve bebeklere verilmez (aynı '
               'gerekçe). Berberin mide-bağırsak şikâyeti (kabızlık, ishal, '
               'şişkinlik) yapar. **CYP3A4 ve P-glikoprotein inhibitörü** — '
               'ilaç etkileşimleri ciddi (aşağıda). Uzun süreli kabuk '
               'kullanımı için veri yok. Güvenlik düzeyi "orta".',
        etk=[
            ['Siklosporin',
             'DSÖ monografının andığı randomize çalışma: böbrek nakli '
             'hastalarında berberin siklosporin kan düzeyini anlamlı yükseltti '
             '(CYP3A4 inhibisyonu). Nakil hastaları kullanmamalı.'],
            ['Kemoterapi ilaçları (paklitaksel)',
             'DSÖ: berberin çoklu ilaç direnci genini (P-gp) artırır, '
             'paklitakselin hücrede tutulmasını azaltabilir. Kemoterapi '
             'sırasında kullanılmaz.'],
            ['Antidiyabetikler',
             'Meta-analiz berberinin kan şekerini düşürdüğünü gösteriyor; '
             'insülin ve sülfonilüre ile birlikte izlem.'],
            ['CYP3A4 ile metabolize olan ilaçlar (statinler, kalsiyum kanal '
             'blokerleri, bazı antidepresanlar)',
             'Berberin CYP3A4 ve CYP2D6’yı engeller; dar aralıklı ilaçlarla '
             'kan düzeyi yükselir. Metformin ile birlikte metformin düzeyi de '
             'artabilir.'],
        ],
        ilginc='Çin tıbbının "sarı kabuğu", Japonya’nın mide tozu, Batı’nın '
               '"bitkisel metformin"i — ve DSÖ’nün en dikkatli cümlelerinden '
               'biri: "kabuk için klinik çalışma yok; berberin için var." '
               'Aynı molekül kataloğumuzda üç bitkide (altın mühür, '
               'kadıntuzluğu, bu kabuk) ve hiçbirinde kabuğun kendisi '
               'sınanmış değil. Berberin kapsülü alanın bilmesi gereken: '
               'siklosporinin düzeyini yükseltiyor, gebelikte yasak.',
        ek=dict(
            mevsim='Kabuk Mayıs–Haziran’da 10 yaşını geçmiş ağaçlardan '
                   'soyulur; dış mantar tabakası atılır, sarı iç kabuk '
                   'kurutulur.',
            yetisme='Kuzeydoğu Çin, Amur havzası, Kore ve Japonya; nemli '
                    'vadiler. Avrupa ve Türkiye’de park ağacı olarak '
                    'dikiliyor.',
            yoresel='Huang bai (Çince), ōbaku (Japonca), Amur mantar ağacı. '
                    'Yöresel ad yok.',
            karisma='⚠️ Huang lian (Coptis) ve huang qin (Scutellaria) ayrı '
                    'droglar. Altın mühür (Hydrastis) ve kadıntuzluğu '
                    '(Berberis) aynı alkaloidi taşır, ayrı kayıtlar. Mantar '
                    'meşesi (Quercus suber) ilgisiz.',
        ),
        ema=[],
        kaynak=[
            ['Cortex Phellodendron, DSÖ Monographs on Selected Medicinal '
             'Plants, Cilt 4, 2009',
             who_url(4, 'cortex-phellodendron')],
            ['W. Xie ve ark., “Glucose-lowering effect of berberine on type 2 '
             'diabetes: A systematic review and meta-analysis”, Frontiers in '
             'Pharmacology 13, 2022',
             'https://pubmed.ncbi.nlm.nih.gov/36467075/'],
        ],
        rel=['altinmuhur', 'zerdecal', 'nane'],
        en=dict(
            name='Amur cork tree (huang bai)',
            other='The WHO monograph Cortex Phellodendron (Volume 4) covers two '
                  'species: Phellodendron amurense and P. chinense. Chinese '
                  'huang bai ("yellow bark"), Japanese ōbaku. The part is **the '
                  'dried bark**. No Turkish or EU monograph. Its main '
                  'constituent is berberine — the same alkaloid as the '
                  'goldenseal (Hydrastis) and barberry (Berberis) in this '
                  'catalog; one of the three "yellow" drugs of Chinese '
                  'medicine.',
            part='The dried bark',
            uses=[
                ['WHO — diarrhoea and urinary tract', 'The WHO monograph says '
                 '"uses supported by clinical data: none"; the pharmacopoeial '
                 'use (Chinese and Japanese pharmacopoeias): orally for '
                 '**abdominal pain, diarrhoea, gastroenteritis and urinary '
                 'tract infection**. The monograph draws an honest line: no '
                 'clinical study of the bark itself, but clinical studies of '
                 'its main constituent **berberine** in diarrhoea, ocular '
                 'trachoma and cutaneous leishmaniasis. Traditional: burns, '
                 'cough, fever, jaundice, malaria, skin wounds. Dose: 3–10 g a '
                 'day. Contraindication: allergy. Not recommended in '
                 'lactation; no information for children. Berberine is well '
                 'tolerated at 0.5 g a day.'],
                ['China — the "three yellows"', 'Huang bai forms, with huang '
                 'lian (Coptis) and huang qin (Scutellaria), the "three '
                 'yellows" of Chinese medicine, the bitter-cold drugs that '
                 '"clear damp-heat"; the bark aimed at inflammation of the '
                 'lower body (urinary tract, bowel, legs). In Japan a stomach '
                 'remedy as ōbaku (Hyakusō) and a traditional source of yellow '
                 'dye; the tree of the Amur basin (China–Russia border), named '
                 'for its thick, corky bark.'],
                ['Berberine — the molecule’s file', 'Berberine is sold in the '
                 'West today as a supplement, "herbal metformin"; the 2022 '
                 'Frontiers in Pharmacology meta-analysis (37 trials, 3,048 '
                 'patients, mostly Chinese) found that berberine lowered '
                 'fasting glucose by 0.82 mmol/L and HbA1c by 0.63% in type 2 '
                 'diabetes without raising the risk of hypoglycaemia. Those '
                 'data belong to purified berberine; the berberine content of '
                 'the bark is variable and its absorption poor — the WHO’s '
                 'distinction matters here.'],
            ],
            prep='WHO: 3–10 g of dried bark a day as decoction (mostly within '
                 'mixtures in Chinese prescriptions). Berberine supplements are '
                 'a standardised, separate product, studied at 0.5–1.5 g a day. '
                 'Not used in pregnancy (berberine — below). No bark in Turkey; '
                 'berberine capsules exist.',
            science='The Amur cork tree is the record where the WHO monograph '
                    'most clearly separates plant from molecule: no clinical '
                    'trial of the bark, trials of berberine. The berberine '
                    'meta-analyses (2015 J Ethnopharmacol; 2022 Frontiers) show '
                    'a consistent effect on blood sugar and lipids — but the '
                    'trials are small, mostly Chinese and single-centre; the '
                    'metformin comparisons say "a similar direction", not '
                    '"equivalent". The berberine diarrhoea trials the WHO cites '
                    'are from the 1980s. The evidence attributable to the bark '
                    'itself is Traditional; berberine supplements should be '
                    'assessed separately. Evidence level Traditional.',
            safety='**Not used in pregnancy** — berberine crosses the placenta '
                   'and carries a risk of kernicterus (bilirubin accumulation) '
                   'in the newborn; the WHO does not recommend it in lactation '
                   'either. Not given to newborns and infants (same reason). '
                   'Berberine causes gastrointestinal complaints '
                   '(constipation, diarrhoea, bloating). **A CYP3A4 and '
                   'P-glycoprotein inhibitor** — serious drug interactions '
                   '(below). No data on long-term bark use. Safety level '
                   'Medium.',
            fact='Chinese medicine’s "yellow bark", Japan’s stomach powder, '
                 'the West’s "herbal metformin" — and one of the WHO’s most '
                 'careful sentences: "no clinical study of the bark; studies '
                 'of berberine." The same molecule sits in three plants of '
                 'this catalog (goldenseal, barberry, this bark), and in none '
                 'has the bark itself been tested. What anyone taking a '
                 'berberine capsule needs to know: it raises ciclosporin '
                 'levels, and it is forbidden in pregnancy.',
            season='The bark is stripped in May–June from trees over 10 years '
                   'old; the outer cork layer is discarded, the yellow inner '
                   'bark dried.',
            habitat='North-eastern China, the Amur basin, Korea and Japan; damp '
                    'valleys. Planted as a park tree in Europe and Turkey.',
            local='Huang bai (Chinese), ōbaku (Japanese), Amur cork tree. No '
                  'regional names.',
            confusion='⚠️ Huang lian (Coptis) and huang qin (Scutellaria) are '
                      'separate drugs. Goldenseal (Hydrastis) and barberry '
                      '(Berberis) carry the same alkaloid, separate records. '
                      'The cork oak (Quercus suber) is unrelated.',
        ),
        etk_en=[
            ['Ciclosporin',
             'The randomised trial the WHO monograph cites: in kidney '
             'transplant patients berberine significantly raised ciclosporin '
             'blood levels (CYP3A4 inhibition). Transplant patients should not '
             'use it.'],
            ['Chemotherapy drugs (paclitaxel)',
             'WHO: berberine up-regulates the multidrug resistance gene '
             '(P-gp) and may reduce cellular retention of paclitaxel. Not used '
             'during chemotherapy.'],
            ['Antidiabetics',
             'The meta-analysis shows berberine lowers blood sugar; '
             'monitoring with insulin and sulphonylureas.'],
            ['Drugs metabolised by CYP3A4 (statins, calcium-channel blockers, '
             'some antidepressants)',
             'Berberine inhibits CYP3A4 and CYP2D6; blood levels of '
             'narrow-margin drugs rise. Metformin levels may also rise when '
             'taken together.'],
        ],
    ),

    dict(
        yayin='2027-01-14',
        id='manolyakabugu',
        foto='',
        tr='Manolya kabuğu (hou po)',
        la='Magnolia officinalis Rehder & E.H.Wilson',
        fam='Magnoliaceae (manolyagiller)',
        diger='DSÖ monografı Cortex Magnoliae (Cilt 4) Magnolia officinalis, '
              'var. biloba ve M. obovata’yı kapsıyor. Çince hou po, Japonca '
              'kōboku, Korece hubak; İngilizce magnolia bark. Kullanılan kısım '
              '**gövde, dal ya da kök kabuğu**. TİTCK ve AB monografı yok. '
              'Türkiye’nin park manolyası (M. grandiflora) ayrı tür ve tıbbi '
              'kayıt değil; bu kayıt Çin’in ilaç manolyasına ait.',
        bolge=['asya'],
        kat=['sifa'],
        kisim='Kurutulmuş gövde, dal ya da kök kabuğu',
        taxon='Magnolia officinalis',
        kul=[
            ['DSÖ — sindirim ve kaygı', 'DSÖ monografı "klinik verilerle '
             'desteklenen kullanım: bilgi yok" diyor; farmakope kullanımı (Çin '
             'Farmakopesi): ağızdan **kabızlık, hazımsızlık, gastrit, bulantı '
             've kusma**; ayrıca **kaygı, öksürük ve nefes darlığı**. '
             'Geleneksel: alerjik rinit, baş ağrısı, iştahsızlık, solunum '
             'tıkanıklığı, nevroz, ateş; rahim uyarıcı. Doz: günde 3–9 g '
             'dekoksiyon, bölünmüş. Kontrendikasyon: alerji. Etkileşim, yan '
             'etki: "bildirilmedi / bilgi yok". Gebelik, emzirme ve 12 yaş '
             'altında veri yokluğu nedeniyle önerilmiyor. Monograf, '
             'farmakolojinin neredeyse tamamının kabuğa değil ana bileşeni '
             'magnolole ait olduğunu açıkça yazıyor.'],
            ['Çin ve Japonya — hou po ve saiboku-to', 'Hou po Çin tıbbında iki '
             'bin yıldır "qi hareket ettirici" kabuk: şişkinlik, dolgunluk, '
             'boğazda "erik çekirdeği" hissi (globus — kaygının bedensel '
             'belirtisi). Japon Kampo’sunda saiboku-to (astım) ve hange-koboku-to '
             '(kaygı, globus) formüllerinin bileşeni. Ağaç Çin’in orta '
             'dağlarına yerli ve yabani popülasyonu kabuk hasadıyla '
             'tükendiğinden ekiliyor.'],
            ['Magnolol ve honokiol — molekül dosyası', 'Kabuğun iki neolignanı '
             '(magnolol, honokiol) laboratuvarda GABA-A reseptörüne bağlanıyor, '
             'kaygı giderici ve sinir koruyucu etki gösteriyor; 2018 Planta '
             'Medica güvenlik derlemesi gıda otoritelerinin iki molekülü '
             '"güvenli" değerlendirdiğini ve bir yıla kadar süren '
             'çalışmalarda yan etki bildirilmediğini yazıyor. Batı’da '
             '"manolya kabuğu özütü" kaygı ve uyku takviyesi olarak satılıyor; '
             'insan çalışmaları küçük ve çoğu karışım (magnolya + '
             'phellodendron).'],
        ],
        haz='DSÖ: günde 3–9 g kuru kabuk, dekoksiyon, bölünmüş dozlarda. '
            'Standardize özütler (magnolol + honokiol) takviyelerde 200–500 '
            'mg; çalışmalar kısa. Gebelikte kullanılmaz (geleneksel rahim '
            'uyarıcı); emzirme ve 12 yaş altında önerilmiyor. Türkiye’de '
            'kabuk yok; özüt kapsülleri ithal.',
        bilim='Manolya kabuğu DSÖ’nün "kabuk için klinik çalışma yok, '
              'farmakoloji molekülden" dediği ikinci kayıt (Amur mantar '
              'ağacıyla aynı yapı). Magnolol ve honokiol üzerine geniş '
              'laboratuvar literatürü var — kaygı, nöroproteksiyon, kanser '
              'hücreleri; insan çalışmaları küçük ve çoğu Phellodendron ile '
              'karışım (Relora) ya da Kampo formülü içinde. 2018 güvenlik '
              'derlemesi molekülleri güvenli buluyor ama "ilaç etkileşimi '
              'dışlanamaz" diyor. Kabuğun kendisi için kanıt "geleneksel".',
        kanit='geleneksel',
        guv='orta',
        guvNot='**Gebelikte kullanılmaz** — geleneksel rahim uyarıcı; DSÖ veri '
               'yokluğuyla önermiyor. Emzirme ve 12 yaş altında önerilmiyor. '
               'DSÖ yan etki bildirmiyor; özüt çalışmalarında uyku hali ve '
               'baş dönmesi — araç kullanırken dikkat. Sakinleştirici '
               'ilaçlarla birlikte etki toplanır. Cerrahi öncesi kesilmeli '
               '(anestezi ile etkileşim kuramsal). Güvenlik düzeyi "orta".',
        etk=[
            ['Sedatifler, benzodiazepinler, alkol',
             'DSÖ "bildirilmedi" diyor; magnololün GABA-A etkisi nedeniyle '
             'sakinleştiricilerle toplanma kuramsal ve olası. Birlikte '
             'alınmaz.'],
            ['Anestezikler (kuramsal)',
             'Aynı mekanizma; cerrahiden iki hafta önce kesilmesi önerilir.'],
            ['Antikoagülanlar (kuramsal)',
             'Honokiolün trombosit agregasyonunu azalttığına dair laboratuvar '
             'verisi; insan olgusu yok.'],
        ],
        ilginc='Boğazda "erik çekirdeği" hissi — Çin tıbbı kaygının bedensel '
               'belirtisini iki bin yıl önce adlandırmış ve bu kabuğu ona '
               'yazmış. Bugün aynı kabuğun molekülleri GABA reseptörüne '
               'bağlanıyor ve Batı’da uyku takviyesi diye satılıyor. DSÖ ise '
               'dürüst: kabuk sınanmadı, molekül sınandı. Türkiye’nin '
               'parklarındaki manolya ise başka tür — çiçeği için dikilir, '
               'kabuğu ilaç değildir.',
        ek=dict(
            mevsim='Kabuk Nisan–Haziran’da 15–20 yaşındaki ağaçlardan soyulur, '
                   'gölgede "terletilerek" kurutulur. Büyük beyaz kokulu '
                   'çiçekler Mayıs’ta.',
            yetisme='Orta Çin’in dağ ormanları (Sichuan, Hubei), 300–1500 m; '
                    'yabani popülasyon azaldı, tarımı yapılıyor. Türkiye’de '
                    'yetişmez.',
            yoresel='Hou po (Çince), kōboku (Japonca), manolya kabuğu. Yöresel '
                    'ad yok.',
            karisma='⚠️ Park manolyası (M. grandiflora) ve Japon manolyası (M. '
                    'liliiflora, M. × soulangeana) ayrı türler, tıbbi kayıt '
                    'değil. Manolya çiçeği tomurcuğu (xin yi, M. biondii) Çin '
                    'tıbbında ayrı drog (burun için).',
        ),
        ema=[],
        kaynak=[
            ['Cortex Magnoliae, DSÖ Monographs on Selected Medicinal Plants, '
             'Cilt 4, 2009',
             who_url(4, 'cortex-magnoliae')],
            ['A. Sarrica ve ark., “Safety and Toxicology of Magnolol and '
             'Honokiol”, Planta Medica 84(16), 2018',
             'https://pubmed.ncbi.nlm.nih.gov/29925102/'],
        ],
        rel=['amurmantaragaci', 'kediotu', 'ihlamur'],
        en=dict(
            name='Magnolia bark (hou po)',
            other='The WHO monograph Cortex Magnoliae (Volume 4) covers '
                  'Magnolia officinalis, var. biloba and M. obovata. Chinese hou '
                  'po, Japanese kōboku, Korean hubak. The part is **the stem, '
                  'branch or root bark**. No Turkish or EU monograph. Turkey’s '
                  'park magnolia (M. grandiflora) is a separate species and not '
                  'a medicinal record; this record belongs to China’s medicinal '
                  'magnolia.',
            part='The dried stem, branch or root bark',
            uses=[
                ['WHO — digestion and anxiety', 'The WHO monograph says "uses '
                 'supported by clinical data: no information was found"; the '
                 'pharmacopoeial use (Chinese Pharmacopoeia): orally for '
                 '**constipation, dyspepsia, gastritis, nausea and vomiting**; '
                 'also **anxiety, cough and shortness of breath**. '
                 'Traditional: allergic rhinitis, headache, loss of appetite, '
                 'respiratory congestion, neurosis, fever; uterine stimulant. '
                 'Dose: 3–9 g a day as decoction, divided. Contraindication: '
                 'allergy. Interactions, adverse effects: "none reported / no '
                 'information". Not recommended in pregnancy, lactation or '
                 'under 12 for lack of data. The monograph writes plainly that '
                 'nearly all the pharmacology belongs not to the bark but to '
                 'its main constituent magnolol.'],
                ['China and Japan — hou po and saiboku-to', 'Hou po has been '
                 'the "qi-moving" bark of Chinese medicine for two thousand '
                 'years: bloating, fullness, the "plum-stone" feeling in the '
                 'throat (globus — the bodily sign of anxiety). In Japanese '
                 'Kampo an ingredient of the saiboku-to (asthma) and '
                 'hange-koboku-to (anxiety, globus) formulae. The tree is '
                 'native to the mountains of central China and is cultivated, '
                 'the wild population having been depleted by bark harvest.'],
                ['Magnolol and honokiol — the molecule file', 'The bark’s two '
                 'neolignans (magnolol, honokiol) bind the GABA-A receptor in '
                 'the laboratory and show anxiolytic and neuroprotective '
                 'effects; the 2018 Planta Medica safety review writes that '
                 'food safety authorities assessed both molecules as "safe" '
                 'and that trials lasting up to a year reported no adverse '
                 'effects. In the West "magnolia bark extract" is sold as an '
                 'anxiety and sleep supplement; the human studies are small '
                 'and mostly blends (magnolia + phellodendron).'],
            ],
            prep='WHO: 3–9 g of dried bark a day as decoction in divided doses. '
                 'Standardised extracts (magnolol + honokiol) 200–500 mg in '
                 'supplements; the trials are short. Not used in pregnancy (a '
                 'traditional uterine stimulant); not recommended in lactation '
                 'or under 12. No bark in Turkey; extract capsules are '
                 'imported.',
            science='Magnolia bark is the second record where the WHO says "no '
                    'clinical study of the bark, the pharmacology is from the '
                    'molecule" (the same structure as the Amur cork tree). '
                    'There is a wide laboratory literature on magnolol and '
                    'honokiol — anxiety, neuroprotection, cancer cells; human '
                    'studies are small and mostly in a blend with Phellodendron '
                    '(Relora) or a Kampo formula. The 2018 safety review finds '
                    'the molecules safe but says "a drug interaction cannot be '
                    'excluded". For the bark itself the evidence is '
                    'Traditional.',
            safety='**Not used in pregnancy** — a traditional uterine '
                   'stimulant; the WHO does not recommend it for lack of data. '
                   'Not recommended in lactation or under 12. The WHO reports '
                   'no adverse effects; drowsiness and dizziness in extract '
                   'trials — care when driving. Effects add up with sedative '
                   'drugs. Stop before surgery (interaction with anaesthesia '
                   'theoretical). Safety level Medium.',
            fact='The "plum-stone" feeling in the throat — Chinese medicine '
                 'named the bodily sign of anxiety two thousand years ago and '
                 'prescribed this bark for it. Today the same bark’s molecules '
                 'bind the GABA receptor and are sold in the West as a sleep '
                 'supplement. The WHO, though, is honest: the bark was not '
                 'tested, the molecule was. The magnolia in Turkey’s parks is '
                 'another species — planted for its flower, its bark no '
                 'medicine.',
            season='The bark is stripped in April–June from 15–20-year-old '
                   'trees and dried by "sweating" in the shade. Large fragrant '
                   'white flowers in May.',
            habitat='The mountain forests of central China (Sichuan, Hubei), '
                    '300–1,500 m; the wild population has declined, and it is '
                    'cultivated. Does not grow in Turkey.',
            local='Hou po (Chinese), kōboku (Japanese), magnolia bark. No '
                  'regional names.',
            confusion='⚠️ The park magnolia (M. grandiflora) and the Japanese '
                      'magnolias (M. liliiflora, M. × soulangeana) are separate '
                      'species, not medicinal records. Magnolia flower bud (xin '
                      'yi, M. biondii) is a separate drug in Chinese medicine '
                      '(for the nose).',
        ),
        etk_en=[
            ['Sedatives, benzodiazepines, alcohol',
             'The WHO says "none reported"; stacking with sedatives is '
             'theoretical and likely because of magnolol’s GABA-A effect. Not '
             'taken together.'],
            ['Anaesthetics (theoretical)',
             'The same mechanism; stopping two weeks before surgery is '
             'advised.'],
            ['Anticoagulants (theoretical)',
             'Laboratory data that honokiol reduces platelet aggregation; no '
             'human case.'],
        ],
    ),

    dict(
        yayin='2027-01-15',
        id='karakartopu',
        foto='',
        tr='Kara kartopu (black haw)',
        la='Viburnum prunifolium L.',
        fam='Adoxaceae (mürvergiller; DSÖ Caprifoliaceae yazıyor)',
        diger='DSÖ monografı Cortex Viburni Prunifolii (Cilt 4); İngilizce black '
              'haw, stag bush, sweet viburnum. Kullanılan kısım **kurutulmuş kök '
              'ya da gövde kabuğu**. TİTCK ve AB monografı yok. Gilaburunun '
              '(V. opulus, "cramp bark") Kuzey Amerikalı akrabası ve aynı '
              'geleneksel kullanım: adet ağrısı. Türkiye’de bilinmez; '
              'kataloğumuza DSÖ listesini tamamlamak ve gilaburuyla köprü '
              'kurmak için girdi.',
        bolge=['kamerika'],
        kat=['sifa'],
        kisim='Kurutulmuş kök ya da gövde kabuğu',
        taxon='Viburnum prunifolium',
        kul=[
            ['DSÖ — adet ağrısı ve astım', 'DSÖ monografı "klinik verilerle '
             'desteklenen kullanım: bilgi yok" diyor; farmakope kullanımı '
             '(İngiliz Bitkisel Farmakopesi): ağızdan **dismenore (adet '
             'ağrısı) ve astım**. Geleneksel: adet düzensizliği, sinir '
             'gerginliği; spazm çözücü, idrar söktürücü, tonik. Doz: toz '
             'kabuk 2,5–5 g infüzyon ya da dekoksiyon günde üç kez; sıvı '
             'ekstre 4–8 ml, tentür 5–10 ml günde üç kez. Kontrendikasyon: '
             'alerji. **Uyarı: gebelikte yalnızca sağlık profesyoneli '
             'gözetiminde.** Emzirme ve 12 yaş altında önerilmiyor. Yan etki, '
             'etkileşim: bilgi yok. Ames testinde mutajen değil.'],
            ['Kuzey Amerika — yerli bilgi ve eklektikler', 'Çalı ABD’nin '
             'doğusuna yerli; Çeroki, Delaware ve diğer yerli halklar '
             'kabuğunu rahim krampı, düşük tehdidi ve doğum sonrası için '
             'kullanmış. 19. yüzyıl Amerikan eklektik hekimleri "black haw"u '
             'düşük önleyici ve adet ağrısı ilacı olarak farmakopeye soktu '
             '(1882 tıp dergilerinde sayfalarca); 1960’a kadar ABD Ulusal '
             'Formüleri’nde kaldı. Kölelik döneminde köle sahiplerinin '
             'kadınların düşük yapmasını engellemek için verdiği — bitkinin '
             'karanlık tarihsel kaydı — tarihçilerce belgelenmiştir.'],
            ['Gilaburu ile köprü', 'DSÖ monografı spazm çözücü verinin '
             '"çelişkili" olduğunu yazıyor: bazı hayvan çalışmalarında kabuk '
             'özütü rahim ve bağırsak düz kasını gevşetiyor, bazılarında '
             'etkisiz. Aynı belirsizlik gilaburunun "cramp bark" '
             'geleneğinde. İki Viburnum, iki kıta, aynı iddia, aynı kanıt '
             'boşluğu.'],
        ],
        haz='DSÖ: toz kabuk 2,5–5 g günde üç kez infüzyon/dekoksiyon; sıvı '
            'ekstre (1:1) 4–8 ml ya da tentür (1:5) 5–10 ml günde üç kez. '
            'Gebelikte yalnızca sağlık profesyoneli gözetiminde; emzirme ve '
            '12 yaş altında kullanılmaz. Türkiye’de ürün yok.',
        bilim='Kara kartopunun insan çalışması yok; DSÖ monografı hayvan '
              've doku verisini "çelişkili" diye niteliyor ve klinik veri '
              'bulamıyor. PubMed’deki kayıtların çoğu 1880’lerin tıp '
              'dergileri — tarihsel ilgi. Kabuğun kumarin türevleri '
              '(skopoletin) ve salisin benzeri bileşikleri spazm çözücü '
              'hipotezin kaynağı. Kanıt düzeyi "geleneksel"; güvenlik "orta" '
              '— DSÖ’nün gebelik uyarısı ve veri yokluğu.',
        kanit='geleneksel',
        guv='orta',
        guvNot='**Gebelikte yalnızca sağlık profesyoneli gözetiminde** — DSÖ; '
               'geleneksel "düşük önleyici" iddiası kanıtsızdır ve gebelikte '
               'kendi başına kullanılmaz. Emzirme ve 12 yaş altında önerilmiyor. '
               'Salisilat benzeri bileşikler içerdiğinden aspirin alerjisi ve '
               'kanama bozukluğunda dikkat (kuramsal). Yan etki verisi yok; '
               'yüksek dozda bulantı. Güvenlik düzeyi "orta".',
        etk=[
            ['Bilinen etkileşim verisi yok (DSÖ)',
             'Monograf "bilgi yok" diyor. Salisin benzeri bileşikler '
             'nedeniyle antikoagülanlarla kuramsal risk; okzalat içeriği böbrek '
             'taşı öyküsünde dikkat.'],
        ],
        ilginc='Çeroki kadınlarının rahim kabuğu, eklektik hekimlerin "düşük '
               'önleyici"si, Amerikan Formüleri’nin 1960’a kadar süren '
               'maddesi — ve kölelik döneminin karanlık kaydı. DSÖ 2009’da '
               'baktı: insan çalışması yok, hayvan verisi çelişkili. '
               'Anadolu’nun gilaburusuyla aynı cins ve aynı iddia; iki '
               'kabuk, iki kıta, sıfır randomize çalışma.',
        ek=dict(
            mevsim='Nisan–Mayıs’ta beyaz çiçek tablaları; sonbaharda mavi-siyah, '
                   'yenilebilir tatlı meyveler. Kabuk sonbaharda soyulur.',
            yetisme='ABD’nin doğusu ve orta batısı; orman kenarları, çitler. '
                    'Türkiye’de yetişmez.',
            yoresel='Kara kartopu, black haw; yöresel ad yok.',
            karisma='⚠️ Gilaburu (V. opulus, cramp bark) aynı cins, ayrı kayıt; '
                    'kabukları ticarette karışır. Meyvesi yenir (gilaburunun '
                    'aksine olgunlaşmamışı sorunsuz). Alıç (Crataegus, "haw") '
                    'ilgisiz — ad benzerliği.',
        ),
        ema=[],
        kaynak=[
            ['Cortex Viburni Prunifolii, DSÖ Monographs on Selected Medicinal '
             'Plants, Cilt 4, 2009',
             who_url(4, 'cortex-viburni-prunifolii')],
        ],
        rel=['gilaburu', 'murver', 'yabanmersini'],
        en=dict(
            name='Black haw',
            other='The WHO monograph Cortex Viburni Prunifolii (Volume 4); '
                  'English black haw, stag bush, sweet viburnum. The part is '
                  '**the dried root or stem bark**. No Turkish or EU monograph. '
                  'The North American relative of the guelder rose (V. opulus, '
                  '"cramp bark") with the same traditional use: period pain. '
                  'Unknown in Turkey; it entered this catalog to complete the '
                  'WHO list and to bridge to the guelder rose.',
            part='The dried root or stem bark',
            uses=[
                ['WHO — period pain and asthma', 'The WHO monograph says "uses '
                 'supported by clinical data: no information was found"; the '
                 'pharmacopoeial use (British Herbal Pharmacopoeia): orally for '
                 '**dysmenorrhoea and asthma**. Traditional: menstrual '
                 'irregularity, nervous tension; antispasmodic, diuretic, '
                 'tonic. Dose: powdered bark 2.5–5 g as infusion or decoction '
                 'three times a day; liquid extract 4–8 ml, tincture 5–10 ml '
                 'three times a day. Contraindication: allergy. **Warning: in '
                 'pregnancy only under the supervision of a health '
                 'professional.** Not recommended in lactation or under 12. '
                 'Adverse effects, interactions: no information. Not mutagenic '
                 'in the Ames test.'],
                ['North America — Indigenous knowledge and the Eclectics', 'The '
                 'shrub is native to the eastern US; the Cherokee, Delaware and '
                 'other Indigenous peoples used its bark for uterine cramps, '
                 'threatened miscarriage and the postpartum. The 19th-century '
                 'American Eclectic physicians brought "black haw" into the '
                 'pharmacopoeia as an anti-abortifacient and period-pain remedy '
                 '(pages of it in the medical journals of 1882); it stayed in '
                 'the US National Formulary until 1960. That slaveholders gave '
                 'it to prevent enslaved women from miscarrying — the plant’s '
                 'dark historical record — has been documented by historians.'],
                ['Bridge to the guelder rose', 'The WHO monograph writes that '
                 'the antispasmodic data are "contradictory": in some animal '
                 'studies bark extract relaxes uterine and intestinal smooth '
                 'muscle, in others it has no effect. The same uncertainty '
                 'hangs over the guelder rose’s "cramp bark" tradition. Two '
                 'Viburnums, two continents, the same claim, the same evidence '
                 'gap.'],
            ],
            prep='WHO: powdered bark 2.5–5 g three times a day as '
                 'infusion/decoction; liquid extract (1:1) 4–8 ml or tincture '
                 '(1:5) 5–10 ml three times a day. In pregnancy only under a '
                 'health professional’s supervision; not used in lactation or '
                 'under 12. No product in Turkey.',
            science='There is no human study of black haw; the WHO monograph '
                    'calls the animal and tissue data "contradictory" and finds '
                    'no clinical data. Most of the PubMed records are medical '
                    'journals of the 1880s — historical interest. The bark’s '
                    'coumarin derivatives (scopoletin) and salicin-like '
                    'compounds are the source of the antispasmodic hypothesis. '
                    'Evidence level Traditional; safety Medium — the WHO’s '
                    'pregnancy warning and the absence of data.',
            safety='**In pregnancy only under a health professional’s '
                   'supervision** — WHO; the traditional "anti-miscarriage" '
                   'claim is unproven, and it is not used on one’s own in '
                   'pregnancy. Not recommended in lactation or under 12. As it '
                   'contains salicylate-like compounds, care in aspirin allergy '
                   'and bleeding disorders (theoretical). No adverse-effect '
                   'data; nausea at high dose. Safety level Medium.',
            fact='The Cherokee women’s uterine bark, the Eclectics’ '
                 '"anti-abortifacient", an item of the American Formulary until '
                 '1960 — and the dark record of the slavery era. The WHO looked '
                 'in 2009: no human study, contradictory animal data. The same '
                 'genus and the same claim as Anatolia’s guelder rose; two '
                 'barks, two continents, zero randomised trials.',
            season='White flower plates in April–May; blue-black, edible sweet '
                   'fruit in autumn. The bark is stripped in autumn.',
            habitat='The eastern and midwestern US; forest edges, hedgerows. '
                    'Does not grow in Turkey.',
            local='Kara kartopu, black haw; no regional names.',
            confusion='⚠️ The guelder rose (V. opulus, cramp bark) is the same '
                      'genus, a separate record; the barks are confused in '
                      'trade. Its fruit is eaten (unlike the guelder rose, the '
                      'unripe fruit is no problem). Hawthorn (Crataegus, "haw") '
                      'is unrelated — a name likeness.',
        ),
        etk_en=[
            ['No known interaction data (WHO)',
             'The monograph says "no information". A theoretical risk with '
             'anticoagulants because of salicin-like compounds; care with its '
             'oxalate content in a history of kidney stones.'],
        ],
    ),

]
