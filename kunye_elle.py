# -*- coding: utf-8 -*-
"""Otomatik çözülemeyen künyelerin APA 7 karşılıkları.

Makale olmayan kaynaklar (kurum sayfaları, monograflar, veri tabanı kayıtları,
kitap) burada. Makaleler tools/apa.py ile yayıncı üstverisinden üretilir ve
kunye_apa.json'a yazılır; oraya elle bir şey yazılmaz.

Biçim: APA 7. Eser adları özgün dilinde bırakılır (çeviri yapılmaz), yapısal
ekler Türkçedir — tarihsiz kaynaklar için "t.y.", köşeli parantez içindeki
tür açıklamaları Türkçe.
"""

# Adres -> APA. Tek tek yazıldı, her biri kaynağın kendi sayfasından doğrulandı.
ELLE = {
 'https://www.unodc.org/unodc/en/frontpage/2013/January/bolivia-to-re-accede-to-un-drug-convention-while-making-exception-on-coca-leaf-chewing.html':
   'United Nations Office on Drugs and Crime. (2013). Bolivia to re-accede to UN drug convention, '
   'while making exception on coca leaf chewing [Basın açıklaması].',
 'https://www.accessdata.fda.gov/spl/data/bfd52d5f-2c7c-4bbe-8aed-b88d1f409907/bfd52d5f-2c7c-4bbe-8aed-b88d1f409907.xml':
   'Mytesi (crofelemer) delayed-release tablets: Prescribing information. (t.y.). '
   'ABD Gıda ve İlaç Dairesi [Ürün bilgisi].',
 'https://www.nobelprize.org/prizes/medicine/2015/summary/':
   'Nobel Prize Outreach. (2015). The Nobel Prize in Physiology or Medicine 2015.',
 'https://nanps.org/native_plants_know/hierochloe-odorata-sweetgrass-2-2/':
   'North American Native Plant Society. (t.y.). Hierochloe odorata (sweetgrass).',
 'https://medlineplus.gov/druginfo/natural/978.html':
   'MedlinePlus. (t.y.). Slippery elm. ABD Ulusal Tıp Kütüphanesi.',

 # --- EMA değerlendirme raporları ve görüşleri (tarih ve başlık PDF kapağından) ---
 'https://www.ema.europa.eu/en/documents/herbal-report/final-assessment-report-allium-sativum-l-bulbus_en.pdf':
   'European Medicines Agency. (2017). Assessment report on Allium sativum L., bulbus '
   '(EMA/HMPC/7686/2013). Committee on Herbal Medicinal Products.',
 'https://www.ema.europa.eu/en/documents/herbal-report/draft-assessment-report-althaea-officinalis-l-radix_en.pdf':
   'European Medicines Agency. (2015). Assessment report on Althaea officinalis L., radix '
   '(Taslak; EMA/HMPC/436680/2015). Committee on Herbal Medicinal Products.',
 'https://www.ema.europa.eu/en/documents/herbal-report/final-assessment-report-echinacea-purpurea-l-moench-herba-recens_en.pdf':
   'European Medicines Agency. (2014). Assessment report on Echinacea purpurea (L.) Moench., '
   'herba recens (EMA/HMPC/557979/2013). Committee on Herbal Medicinal Products.',
 'https://www.ema.europa.eu/en/documents/herbal-report/final-assessment-report-fraxinus-excelsior-l-or-fraxinus-angustifolia-vahl-folium_en.pdf':
   'European Medicines Agency. (2012). Assessment report on Fraxinus excelsior L. or '
   'Fraxinus angustifolia Vahl, folium (EMA/HMPC/239269/2011). Committee on Herbal Medicinal Products.',
 'https://www.ema.europa.eu/en/documents/herbal-report/final-assessment-report-quercus-robur-l-quercus-petraea-matt-liebl-quercus-pubescens-willd-cortex_en.pdf':
   'European Medicines Agency. (2010). Assessment report on Quercus robur L., Quercus petraea '
   '(Matt.) Liebl., Quercus pubescens Willd., cortex (EMA/HMPC/3206/2009). '
   'Committee on Herbal Medicinal Products.',
 'https://www.ema.europa.eu/en/documents/herbal-report/superseded-assessment-report-verbascum-thapsus-l-v-densiflorum-bertol-v-phlomoides-l-flos-traditional-use_en.pdf':
   'European Medicines Agency. (2008). Assessment report on Verbascum thapsus L., '
   'V. densiflorum Bertol., V. phlomoides L., flos with traditional use '
   '(EMEA/HMPC/395206/2007 Corr.). Committee on Herbal Medicinal Products.',
 'https://www.ema.europa.eu/en/documents/herbal-opinion/final-opinion-hmpc-european-union-herbal-monograph-pistacia-lentiscus-l-resin-mastic_en.pdf':
   'European Medicines Agency. (2016). Opinion of the HMPC on a European Union herbal monograph '
   'on Pistacia lentiscus L., resin (mastic) (EMA/HMPC/74864/2016). '
   'Committee on Herbal Medicinal Products.',

 # --- Kurum sayfaları ve düzenlemeler ---
 'https://www.cancer.gov/about-cancer/treatment/cam/hp/mushrooms-pdq':
   'National Cancer Institute. (t.y.). Medicinal mushrooms (PDQ) – Health professional version. '
   'ABD Ulusal Sağlık Enstitüleri.',
 'https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-189/subpart-C/section-189.180':
   'Substances prohibited from use in human food: Safrole, 21 C.F.R. § 189.180. (t.y.). '
   'ABD Federal Düzenlemeler Kanunu.',
 'https://inchem.org/documents/pims/plant/thevetia.htm':
   'International Programme on Chemical Safety. (t.y.). Thevetia peruviana '
   '(Poisons Information Monograph No. 527). Dünya Sağlık Örgütü.',
 'https://www.legislation.gov.uk/eur/2012/432/annex':
   'Commission Regulation (EU) No 432/2012 of 16 May 2012 establishing a list of permitted '
   'health claims made on foods, other than those referring to the reduction of disease risk '
   'and to children’s development and health [Ek]. (2012). '
   'Official Journal of the European Union, L 136, 1–40.',
 'https://www.gov.uk/guidance/managing-ash-dieback-in-england':
   'Forestry Commission. (2025). Managing ash dieback in England [Rehber]. GOV.UK.',
 'https://gd.eppo.int/taxon/CHAAFR/distribution/TR':
   'EPPO. (t.y.). Hymenoscyphus fraxineus: Türkiye [Dağılım kaydı]. EPPO Global Database.',
 'https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/british-trees/a-z-of-british-trees/rowan/':
   'Woodland Trust. (t.y.). Rowan (Sorbus aucuparia).',
 'https://www.museum.ie/en-IE/Collections-Research/Folklife-Collections/Folklife-Collections-List-(1)/Religion-and-Calendar-Customs/May-Day':
   'National Museum of Ireland. (t.y.). May Day. Folklife Collections.',
 'https://england.prm.ox.ac.uk/englishness-loop-of-rowan-tree.html':
   'Modh, S. (t.y.). A loop of rowan tree: Amulets against witchcraft. '
   'Pitt Rivers Museum, University of Oxford.',

 # --- Makaleler (yayıncı sayfası çözülemedi; künye PDF kapağından) ---
 'https://ethnobotanyjournal.org/index.php/era/article/view/1283':
   'Bussmann, R. W., & Sharon, D. (2016). Medicinal plants of the Andes and the Amazon: '
   'The magic and medicinal flora of Northern Peru. '
   'Ethnobotany Research and Applications, 15, 1–295.',
 'https://www.exoriente.org/docs/00046.pdf':
   'Neef, R. (2003). Overlooking the steppe-forest: A preliminary report on the botanical '
   'remains from Early Neolithic Göbekli Tepe (Southeastern Turkey). Neo-Lithics, 2003(2), 13–16.',
 'https://dergipark.org.tr/en/download/article-file/2704500':
   'Macit, M., Ahıskalı, M., & Özbay, N. (2022). A review on the botanical and phytochemical '
   'properties of some species belonging to Sorbus sp. Uluslararası Gıda, Tarım ve Hayvan '
   'Bilimleri Dergisi, 2(1), 31–37.',
 'https://dergipark.org.tr/en/download/article-file/451448':
   'Bulut, İ. (2011). Anadolu’da inanışların ve geleneklerin doğa korunması açısından önemi '
   'üzerine örnekler. Atatürk Üniversitesi Edebiyat Fakültesi Sosyal Bilimler Dergisi, 11(46), '
   '119–134.',
 'https://dergipark.org.tr/tr/download/article-file/176576':
   'Atay, İ. (1984). Tâli türlerimizden dişbudağın önemi ve silvikültürel özellikleri. '
   'İstanbul Üniversitesi Orman Fakültesi Dergisi, B 34(3), 17–31.',
 'https://dergipark.org.tr/tr/download/article-file/2231021':
   'Oymak, İ. (2001). Eski Türk inanışlarından ağaç kültünün Malatya’daki izleri. '
   'İlahiyat Fakültesi Dergisi, 6, 55–74.',

 # --- Kaynak metinler (kamu malı baskılar) ---
 'https://www.gutenberg.org/files/24886/24886-h/24886-h.htm':
   'Withering, W. (1785). An account of the foxglove and some of its medical uses. '
   'M. Swinney. Project Gutenberg.',
 'https://www.gutenberg.org/ebooks/59131':
   'Plinius. (1855–1857). The natural history of Pliny (J. Bostock & H. T. Riley, Çev.; '
   '16. kitap). H. G. Bohn. Project Gutenberg. (Özgün eser y. MS 77)',
 'https://www.gutenberg.org/ebooks/60688':
   'Plinius. (1855–1857). The natural history of Pliny (J. Bostock & H. T. Riley, Çev.; '
   '25. kitap). H. G. Bohn. Project Gutenberg. (Özgün eser y. MS 77)',
 'https://www.gutenberg.org/ebooks/62704':
   'Plinius. (1855–1857). The natural history of Pliny (J. Bostock & H. T. Riley, Çev.; '
   '8. ve 33. kitaplar). H. G. Bohn. Project Gutenberg. (Özgün eser y. MS 77)',
 'https://www.gutenberg.org/ebooks/3623':
   'Frazer, J. G. (1922). The golden bough: A study in magic and religion (Kısaltılmış baskı). '
   'Macmillan. Project Gutenberg.',
 'https://www.gutenberg.org/ebooks/73533':
   'Bellows, H. A. (Çev.). (1923). The poetic Edda. American-Scandinavian Foundation. '
   'Project Gutenberg.',
 'https://www.gutenberg.org/ebooks/1408':
   'White, G. (1789). The natural history of Selborne. B. White and Son. Project Gutenberg.',
 'https://archive.org/details/proseedda01brodgoog':
   'Sturluson, S. (1916). The prose Edda (A. G. Brodeur, Çev.). American-Scandinavian '
   'Foundation. (Özgün eser y. 1220)',
 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/12E*.html':
   'Strabon. (1928). The geography of Strabo (H. L. Jones, Çev.). Harvard University Press. '
   '(Özgün eser y. MS 23)',

 # --- TDV İslâm Ansiklopedisi ---
 'https://islamansiklopedisi.org.tr/gul-u-bulbul':
   'Özkan, M. (1996). Gül ü Bülbül. TDV İslâm Ansiklopedisi (C. 14). Türkiye Diyanet Vakfı.',
 'https://islamansiklopedisi.org.tr/hidrellez':
   'Ocak, A. Y. (1998). Hıdrellez. TDV İslâm Ansiklopedisi (C. 17). Türkiye Diyanet Vakfı.',
 'https://islamansiklopedisi.org.tr/kina':
   'Pişkin, H. N. (2019). Kına. TDV İslâm Ansiklopedisi (Ek 2. C.). Türkiye Diyanet Vakfı.',
 'https://islamansiklopedisi.org.tr/lale':
   'Lâle. (2003). TDV İslâm Ansiklopedisi (C. 27). Türkiye Diyanet Vakfı.',
 'https://islamansiklopedisi.org.tr/nazar':
   'Nazar. (t.y.). TDV İslâm Ansiklopedisi. Türkiye Diyanet Vakfı.',
 'https://islamansiklopedisi.org.tr/nevruz':
   'Gündüz, Ş. (2007). Nevruz. TDV İslâm Ansiklopedisi (C. 33). Türkiye Diyanet Vakfı.',
 'https://islamansiklopedisi.org.tr/samanizm':
   'Güngör, H. (2010). Şamanizm. TDV İslâm Ansiklopedisi (C. 38). Türkiye Diyanet Vakfı.',
 'https://islamansiklopedisi.org.tr/tibb-i-nebevi':
   'Özkan, H. (2012). Tıbb-ı Nebevî. TDV İslâm Ansiklopedisi (C. 41). Türkiye Diyanet Vakfı.',

 # --- Encyclopaedia Britannica ---
 'https://www.britannica.com/EBchecked/topic/233978/ginseng':
   'Encyclopaedia Britannica. (t.y.). Ginseng.',
 'https://www.britannica.com/EBchecked/topic/405965/Native-American-Church':
   'Encyclopaedia Britannica. (t.y.). Native American Church.',
 'https://www.britannica.com/science/Ayurveda':
   'Encyclopaedia Britannica. (t.y.). Ayurveda.',
 'https://www.britannica.com/science/traditional-Chinese-medicine/Herbal-therapy':
   'Encyclopaedia Britannica. (t.y.). Traditional Chinese medicine: Herbal therapy.',
 'https://www.britannica.com/topic/Pachamama':
   'Encyclopaedia Britannica. (t.y.). Pachamama.',
 'https://www.britannica.com/topic/animism':
   'Encyclopaedia Britannica. (t.y.). Animism.',
 'https://www.britannica.com/topic/haoma':
   'Encyclopaedia Britannica. (t.y.). Haoma.',
 'https://www.britannica.com/topic/shamanism':
   'Encyclopaedia Britannica. (t.y.). Shamanism.',
 'https://www.britannica.com/topic/traditional-Chinese-medicine':
   'Encyclopaedia Britannica. (t.y.). Traditional Chinese medicine.',

 # --- UNESCO Somut Olmayan Kültürel Miras ---
 'https://ich.unesco.org/en/RL/dragon-boat-festival-00225':
   'UNESCO. (2009). Dragon Boat festival [İnsanlığın Somut Olmayan Kültürel Mirasının '
   'Temsilî Listesi].',
 'https://ich.unesco.org/en/RL/indigenous-festivity-dedicated-to-the-dead-00054':
   'UNESCO. (2008). Indigenous festivity dedicated to the dead [İnsanlığın Somut Olmayan '
   'Kültürel Mirasının Temsilî Listesi].',
 'https://ich.unesco.org/en/RL/mehregan-02144':
   'UNESCO. (2024). Ceremony of Mehregan [İnsanlığın Somut Olmayan Kültürel Mirasının '
   'Temsilî Listesi].',
 'https://ich.unesco.org/en/RL/yalda-chella-01877':
   'UNESCO. (2022). Yaldā/Chella [İnsanlığın Somut Olmayan Kültürel Mirasının '
   'Temsilî Listesi].',

 # --- Coğrafi işaret tescil belgeleri ---
 'https://ci.turkpatent.gov.tr/Files/GeographicalSigns/50b20279-353a-4a37-b33a-52607f2c62ea.pdf':
   'Türk Patent ve Marka Kurumu. (2017). Kahramanmaraş oyma çeyiz sandığı '
   '[Coğrafi işaret tescil belgesi No. 305].',
 'https://ci.turkpatent.gov.tr/Files/GeographicalSigns/8e84210c-6bca-452c-9cf8-17e8df9da440.pdf':
   'Türk Patent ve Marka Kurumu. (2023). Hakkâri kilimi [Coğrafi işaret tescil belgesi].',
 'https://ci.turkpatent.gov.tr/Files/GeographicalSigns/b67d120c-1f61-44c1-9cb6-9a4148a49eec.pdf':
   'Türk Patent ve Marka Kurumu. (2020). Dazkırı halısı '
   '[Coğrafi işaret tescil belgesi No. 629].',
 'https://ci.turkpatent.gov.tr/Files/GeographicalSigns/d2eb94c9-33de-4b54-8404-b5cbb67d13d5.pdf':
   'Türk Patent ve Marka Kurumu. (2024). Beytüşşebap Jirki kilimi '
   '[Coğrafi işaret tescil belgesi No. 1568].',

 # --- Müze koleksiyonları ---
 'https://col.rct.uk/collection/23692/ruyi-sceptre':
   'Royal Collection Trust. (t.y.). Ruyi sceptre (RCIN 23692) [Müze nesnesi].',
 'https://collections.lacma.org/object/33910':
   'Los Angeles County Museum of Art. (t.y.). Textile fragment, Nasca (M.74.151.14) '
   '[Müze nesnesi].',
 'https://www.horniman.ac.uk/object/25.203':
   'Horniman Museum and Gardens. (t.y.). Object 25.203 [Müze nesnesi].',
 'https://www.horniman.ac.uk/object/HC.1999.1406':
   'Horniman Museum and Gardens. (t.y.). Sikuli, ojo de dios (HC.1999.1406) [Müze nesnesi].',
 'https://www.museum.ie/en-IE/Collections-Research/Folklife-Collections/Folklife-Collections-List-(1)/Religion-and-Calendar-Customs/Hallowe-en-Samhain':
   'National Museum of Ireland. (t.y.). Hallowe’en / Samhain. Folklife Collections.',
 'https://www.museum.ie/getmedia/6044d82b-1b27-4475-ae45-aec38747c0eb/Hawthorn-Information-Sheet.pdf':
   'National Museum of Ireland – Country Life. (t.y.). Sceach gheal / hawthorn '
   '[Bilgi föyü]. Fairies and Fairy Folk.',

 # --- Makaleler ve kitaplar (bağlantılı) ---
 'https://divandergisi.com/pdf/170.pdf':
   'Doğanay, A. (2004). Türk sanatında pelengî ve şâhî benek nakışları ya da çintamani '
   'yanılgısı. Dîvân: Disiplinlerarası Çalışmalar Dergisi, 17, 177–196.',
 'https://zenodo.org/records/15401202':
   'Boratav, O., & Kılıçaslan, M. (2025). Osmanlı çini ve seramiklerinde kullanılan ağaç '
   'motifleri. Zenodo.',
 'https://palaeobotanicalsociety.org/geophytology/vol6_1976/15vol6_11976.pdf':
   'Sitholey, R. V. (1976). Plants represented in ancient Indian sculpture. '
   'Geophytology, 6(1), 97–103.',
 'https://revistas.unal.edu.co/index.php/imanimundo/article/view/28715':
   'Belaunde, L. E. (2012). Diseños materiales e inmateriales: La patrimonialización del '
   'kene shipibo-konibo y de la ayahuasca en el Perú. Mundo Amazónico, 3, 123–146.',
 'https://tdkbelleten.gov.tr/ozet/718/eng':
   'Korkmaz, Z. (2003). Eski Türklerdeki ağaç kültünün İslami devirlerdeki devamı. '
   'Türk Dili Araştırmaları Yıllığı – Belleten, 51(1), 85–92.',
 'https://www.archaeopresspublishing.com/ojs/index.php/ash-sharq/article/view/1760':
   'Franklin, N. (2021). The Assyrian stylized tree: A date palm plantation and '
   'Aššurnaṣirpal II’s stemma. Ash-sharq, 5(2), 1–14.',
 'https://link.springer.com/article/10.1663/0013-0001(2007)61[246:DOSAEO]2.0.CO;2':
   'Bennett, B. C. (2007). Doctrine of signatures: An explanation of medicinal plant '
   'discovery or dissemination of knowledge? Economic Botany, 61(3), 246–255.',
 'https://discovery.ucl.ac.uk/id/eprint/10141249/':
   'Berlowitz, I., Torres, E. G., Walt, H., Wolf, U., Maake, C., & Martin-Soelch, C. (2022). '
   '“Teacher plants” – Indigenous Peruvian-Amazonian dietary practices as a method for '
   'using psychoactives. Journal of Ethnopharmacology, 286, 114910.',
 'https://library.oapen.org/handle/20.500.12657/58977':
   'Dietrich, L. (2021). Plant food processing tools at Early Neolithic Göbekli Tepe. '
   'Archaeopress.',
 'https://northernwoodlands.org/articles/article/doctrine-signatures':
   'Diamond, A. (2014). That signature look: An introduction to the doctrine of signatures. '
   'Northern Woodlands.',
 'https://nyamcenterforhistory.org/tag/flowers/':
   'Miranker, E. (t.y.). The other language of flowers: The doctrine of signatures. '
   'New York Academy of Medicine.',
 'https://www.maya-archaeology.org/FLAAR_Reports_on_Mayan_archaeology_Iconography_publications_books_articles/49_Flowering-of-the-National-tree-REVUE-article-FLAAR-Nicholas-Hellmuth.pdf':
   'Hellmuth, N. M. (2013). Flowering of the national tree [Revue Magazine sütunu]. '
   'FLAAR Reports.',
 'https://www.bialabate.net/blog-archive/news/“plantas-conmadre”-plants-that-teach-and-guide-in-the-shamanic-initiation':
   'Jauregui, X., Clavo, Z. M., Jovel, E. M., & Pardo-de-Santayana, M. (2011). '
   '“Plantas con madre”: Plants that teach and guide in the shamanic initiation process '
   'in the East-Central Peruvian Amazon. Journal of Ethnopharmacology, 134(3), 739–752.',
 'https://www.dainst.blog/the-tepe-telegrams/2017/07/03/more-than-a-vulture-a-response-to-sweatman-and-tsikritsis/':
   'Notroff, J., Dietrich, O., Peters, J., Pöllath, N., & Clare, L. (2017). More than a '
   'vulture: A response to Sweatman and Tsikritsis. Mediterranean Archaeology and '
   'Archaeometry, 17(2), 57–63.',
 'https://cultural.kz/en/nature-as-a-symbolic-system/celestial-bodies-time-of-day-natural-phenomena/qymyz-muryndyq/':
   'Shaigozova, Zh. N., & Naurzbaeva, A. B. (2023). Qymyz muryndyq. '
   'Brief encyclopedia of signs and symbols of Kazakh culture. KazNIIK.',

 # --- Kurum ve devlet sayfaları, haber ---
 'https://andina.pe/agencia/noticia-en-consiste-inti-raymi-cual-es-su-historia-y-que-lugares-cusco-ocurre-989247.aspx':
   'Agencia Andina. (2025). ¿En qué consiste el Inti Raymi? [Haber].',
 'https://elperuano.pe/noticia/197142-declaran-patrimonio-cultural-de-la-nacion-a-los-conocimientos-saberes-y-usos-del-cactus-san-pedro':
   'Declaran Patrimonio Cultural de la Nación a los conocimientos, saberes y usos del '
   'cactus San Pedro. (2022). El Peruano.',
 'https://english.beijing.gov.cn/beijinginfo/culture/beijingfolklore/festivals/202110/t20211018_2514759.html':
   'Beijing Municipal Government. (2021). Customs related to the Dragon Boat Festival.',
 'https://english.shanghai.gov.cn/en-LearnChinese/20251029/a6ce1a9f9f2645e2b1b8312dc7af2858.html':
   'Shanghai Municipal Government. (2025). Share blessings and good fortune on '
   'Chongyang Festival.',
 'https://ethnomuseum.ru/files/PDF/PrssReliz/2024/rem_press-reliz_ysyah.pdf':
   'Rossiyskiy Etnograficheskiy Muzey. (2024). Ysyakh [Basın bülteni].',
 'https://festival.si.edu/blog/2015/an-offering-to-pachamama/':
   'Turpo, R. (2015). An offering to the Pachamama. Smithsonian Folklife Festival.',
 'https://nuevaescuelamexicana.sep.gob.mx/contenido/recurso/elementos-basicos-para-la-ofrenda-de-dia-de-muertos/':
   'Secretaría de Educación Pública. (t.y.). Elementos básicos para la ofrenda de '
   'Día de Muertos.',
 'https://obs.agenda21culture.net/en/good-practices/national-holiday-yssyakh-tuymaada-summer-festival':
   'Dorofeeva, A. (t.y.). National holiday “Yssyakh of Tuymaada” (summer festival). '
   'UCLG Committee on Culture.',
 'https://www.belarus.by/en/travel/ethno-tourism/kupalle':
   'Republic of Belarus. (t.y.). Kupala Night in Belarus.',
 'https://www.latvia.eu/?p=35586':
   'Latvia.eu. (2026). Inside a traditional Latvian summer solstice celebration.',
 'https://www.rte.ie/brainstorm/2025/0725/1525282-bilberries-bilberry-sunday-ireland-folklore-lughnasa-festival':
   'Sexton, R. (2025). It’s Bilberry Sunday this weekend but have you ever eaten one? '
   'RTÉ Brainstorm.',
 'https://www.uu.nl/en/news/new-age-ritual-sends-bad-energies-and-foreign-wild-plants-up-in-smoke':
   'Utrecht University. (2024). New Age ritual sends “bad energies” and foreign wild '
   'plants up in smoke [Haber].',
 'https://www.eomega.org/articles/what-limpia-exploring-ancient-spiritual-cleansing-ritual':
   'Omega Institute. (t.y.). What is a limpia? Exploring an ancient spiritual '
   'cleansing ritual.',

 # --- Project Gutenberg'in diğer adres biçimleri ---
 'https://gutenberg.org/cache/epub/73533/pg73533-images.html':
   'Bellows, H. A. (Çev.). (1923). The poetic Edda. American-Scandinavian Foundation. '
   'Project Gutenberg.',
 'https://www.gutenberg.org/cache/epub/59131/pg59131-images.html':
   'Plinius. (1855–1857). The natural history of Pliny (J. Bostock & H. T. Riley, Çev.). '
   'H. G. Bohn. Project Gutenberg. (Özgün eser y. MS 77)',}

# Bağlantısız kitap ve tez künyeleri: eski etiketten APA'ya eşleme.
METIN = {
 'Abdülkadir İnan, Tarihte ve Bugün Şamanizm, Ankara, 1954':
   'İnan, A. (1954). Tarihte ve bugün Şamanizm: Materyaller ve araştırmalar. '
   'Türk Tarih Kurumu.',
 'Ali Berat Alptekin, “Türk Halk Hikâyelerinde Ağaç Motifi Üzerine”, Millî Folklor 76, 2007':
   'Alptekin, A. B. (2007). Türk halk hikâyelerinde ağaç motifi üzerine. '
   'Millî Folklor, 19(76), 33–45.',
 'Reyhan Değirmenci, Türk Mitolojisinde Yüce Ana Arketipi: Umay Üzerine Arketipsel Bir İnceleme, yüksek lisans tezi, Ege Üniversitesi, 2024':
   'Değirmenci, R. (2024). Türk mitolojisinde yüce ana arketipi: Umay üzerine arketipsel '
   'bir inceleme [Yüksek lisans tezi, Ege Üniversitesi].',
}

# DergiPark'ın doğrudan PDF bağlantıları ve Crossref'ten çözülemeyen DOI'ler;
# künyeler makalenin kendi kapak sayfasından yazıldı.
ELLE.update({
 'https://dergipark.org.tr/tr/download/article-file/1028026':
   'Hayırsever, B. (2020). Geleneksel el sanatlarında kullanılan çintemani motifi ve '
   'seramik sanatına yansımaları. Erciyes Üniversitesi Sosyal Bilimler Enstitüsü Dergisi, '
   '50(3), 9–22.',
 'https://dergipark.org.tr/tr/download/article-file/156974':
   'Üstün, Ç. (2009). Eski bir Türk içeceği: Kımız (koumiss). '
   'Türklük Bilimi Araştırmaları, 26, 247–255.',
 'https://dergipark.org.tr/tr/download/article-file/162641':
   'Doğanay, A. (2003). XVI. yüzyıl İznik duvar çinilerinde meyve tasvirleri. '
   'Marmara Üniversitesi İlâhiyat Fakültesi Dergisi, 24, 43–63.',
 'https://dergipark.org.tr/tr/download/article-file/193311':
   'Ölmez, F. N. (2009). “Death” symbolism in Turkish weavings. '
   'Süleyman Demirel Üniversitesi Güzel Sanatlar Fakültesi Hakemli Dergisi ART-E, '
   '2009(4), 1–21.',
 'https://dergipark.org.tr/tr/download/article-file/2199319':
   'Karaçay, Ç. (2022). Boteh motifinin kökenine kısa bir bakış ve Anadolu Türk halı '
   'sanatında boteh tasvirleri. Süleyman Demirel Üniversitesi Güzel Sanatlar Fakültesi '
   'Sanat Dergisi ART-E, 15(29), 128–148.',
 'https://dergipark.org.tr/tr/download/article-file/29048':
   'Tali, Ş. (t.y.). Kayseri Tavlusun köyü mezarlığında bezemeli mezar taşları-II. '
   'Atatürk Üniversitesi Güzel Sanatlar Fakültesi Sanat Dergisi, 20, 97–124.',
 'https://dergipark.org.tr/tr/download/article-file/4267765':
   'Seçilmiş, B. (2024). Ereğli ve çevresinin Hitit ve Geç Hitit dönemlerindeki dinî '
   'kültürü. bitig Edebiyat Fakültesi Dergisi, 4(8), 234–246.',
 'https://dergipark.org.tr/tr/download/article-file/4421411':
   'Ender, K. N., & Demirel, Ş. (2025). Orta Asya Şamanizminde evrenin tezahürü. '
   'Van Yüzüncü Yıl Üniversitesi Sosyal Bilimler Enstitüsü Dergisi, 67, 231–243.',
 'https://dergipark.org.tr/tr/download/article-file/681504':
   'Sağ, M., & Çetin Büyüktunca, M. (2019). Şamanların göğe yükseliş ritlerinin ağaç '
   'simgesi bağlamında incelenmesi. Van Yüzüncü Yıl Üniversitesi Sosyal Bilimler '
   'Enstitüsü Dergisi, 43, 217–230.',
 'https://dergipark.org.tr/tr/download/article-file/989056':
   'Özarslan, M. (2003). Türk kültüründe ağaç ve orman kültü. Türkbilig, 5, 94–102.',
 'https://dergipark.org.tr/tr/pub/mutftd/issue/92009':
   'Türkmen, İ. (2025). Doğayla özdeşleşen Şamanizm’de şifacılık kültürü. '
   'Lokman Hekim Dergisi, 15(3).',
 'https://doi.org/10.47089/iuad.797850':
   'Aksoy, Ö. (2020). Tataristan’ın Kukmara Rayonu Mamaşir köyünde Sabantuy bayramı. '
   'İdil Ural Araştırmaları Dergisi, 2(2), 225–237. https://doi.org/10.47089/iuad.797850',
 'https://doi.org/10.55666/folklor.1637963':
   'Özşahin, M. (2025). Başkurt halk yaşamında, sanatında ve tıbbında kımız. '
   'Folklor Akademi Dergisi, 8(1), 8–16. https://doi.org/10.55666/folklor.1637963'
})


# Kitaplar (elde doğrulanmış künyeler)
EVANS_APA = ('Evans, W. C. (2009). Trease and Evans’ pharmacognosy (16. baskı). '
             'Saunders/Elsevier.')
FITO_APA = ('Tekin, A., Tatlı Çankaya, İ., & Zeybek, A. U. (Ed.). (2022). '
            'Fitoterapi uygulaması kitabı. T.C. Sağlık Bakanlığı Sağlık Hizmetleri '
            'Genel Müdürlüğü.')
ZEHIR_APA = ('Baytop, T., Baytop, A., Mat, A., & Sun, S. (1989). Türkiye’de zehirli '
             'bitkiler, bitki zehirlenmeleri ve tedavi yöntemleri. İstanbul Üniversitesi.')
SECMEN_APA = ('Seçmen, Ö., & Leblebici, E. (1987). Yurdumuzun zehirli bitkileri. '
              'Ege Üniversitesi Fen Fakültesi.')
NELSON_APA = ('Nelson, L. S., Shih, R. D., & Balick, M. J. (2007). Handbook of poisonous '
              'and injurious plants (2. baskı). Springer.')

# Kitap
BAYTOP_APA = ('Baytop, T. (2021). Türkiye’de bitkiler ile tedavi: Geçmişte ve bugün '
              '(3. baskı; F. Baytop Günergun, Yay. haz.). Nobel Tıp Kitabevleri.')


def ema_apa(ad):
    """EMA bitkisel monografı. Yayın tarihi sayfada JavaScript ile geldiği için
    ham HTML'den okunamıyor; APA'nın tarihsiz biçimi kullanılıyor."""
    return f'European Medicines Agency. (t.y.). {ad} [Bitkisel tıbbi ürün monografı].'


# NCCIH sayfa başlıkları. Adres kısaltmasından türetilemiyor ("st-johns-wort"
# -> "St johns wort" olurdu), bu yüzden her biri sayfanın kendi başlığından yazıldı.
NCCIH_BASLIK = {
 'acai': 'Acai', 'aloe-vera': 'Aloe vera', 'ashwagandha': 'Ashwagandha',
 'asian-ginseng': 'Asian ginseng', 'black-cohosh': 'Black cohosh',
 'cats-claw': 'Cat’s claw', 'chamomile': 'Chamomile', 'chasteberry': 'Chasteberry',
 'cinnamon': 'Cinnamon', 'dandelion': 'Dandelion', 'echinacea': 'Echinacea',
 'elderberry': 'Elderberry', 'ephedra': 'Ephedra', 'european-mistletoe': 'European mistletoe',
 'fenugreek': 'Fenugreek', 'flaxseed-and-flaxseed-oil': 'Flaxseed and flaxseed oil',
 'garlic': 'Garlic', 'ginger': 'Ginger', 'ginkgo': 'Ginkgo', 'goldenseal': 'Goldenseal',
 'green-tea': 'Green tea', 'hawthorn': 'Hawthorn', 'lavender': 'Lavender',
 'licorice-root': 'Licorice root', 'milk-thistle': 'Milk thistle', 'mugwort': 'Mugwort',
 'peppermint-oil': 'Peppermint oil', 'pomegranate': 'Pomegranate', 'rhodiola': 'Rhodiola',
 'sage': 'Sage', 'saw-palmetto': 'Saw palmetto', 'st-johns-wort': 'St. John’s wort',
 'turmeric': 'Turmeric', 'valerian': 'Valerian',
}


def nccih_apa(ad):
    baslik = NCCIH_BASLIK.get(ad) or (ad.replace('-', ' ').capitalize())
    return (f'National Center for Complementary and Integrative Health. (t.y.). {baslik}. '
            'ABD Ulusal Sağlık Enstitüleri.')


def powo_apa(ad):
    return (f'Plants of the World Online. (t.y.). {ad}. Royal Botanic Gardens, Kew.')


METIN.update({
 'Turhan Baytop, Türkiye’de Bitkiler ile Tedavi: Geçmişte ve Bugün, 3rd ed. (yay. haz. Feza Baytop Günergun), Nobel Tıp Kitabevleri, 2021, “Tarih ve gelişim” bölümü':
   BAYTOP_APA + ' (“Tarih ve gelişim” bölümü)',
 'Baytop T., Türkiye’de Bitkiler ile Tedavi: Geçmişte ve Bugün (Plant Healing in Turkey: Past and Present), 3rd ed., Nobel Tıp Kitabevleri, 2021':
   BAYTOP_APA,
 'Turkish Ministry of Health, Fitoterapi Uygulaması Kitabı (Phytotherapy Practice Book), 2022 (chapter on poisonous plants)':
   FITO_APA + ' (“Zehirli bitkiler” bölümü)',
 'Baytop T., Baytop A., Mat A., Sun S., Türkiye’de zehirli bitkiler, bitki zehirlenmeleri ve tedavi yöntemleri (Poisonous plants, plant poisonings and their treatment in Turkey), Istanbul University, 1989 (as cited in the phytotherapy book)':
   ZEHIR_APA + ' (Fitoterapi kitabındaki atıfla)',
 'Seçmen Ö., Leblebici E., Yurdumuzun zehirli bitkileri (The poisonous plants of our country), Ege University Faculty of Science, İzmir, 1987 (as cited in the phytotherapy book)':
   SECMEN_APA + ' (Fitoterapi kitabındaki atıfla)',
 'Nelson L. S., Shih R. D., Balick M. J., Handbook of Poisonous and Injurious Plants, 2nd ed., Springer (as cited in the phytotherapy book; house plant data)':
   NELSON_APA + ' (Fitoterapi kitabındaki atıfla; ev bitkileri verisi)',
 'Mircea Eliade, Shamanism: Archaic Techniques of Ecstasy (Radloff 1884’ten aktararak), s. 190-197':
   'Eliade, M. (1964). Shamanism: Archaic techniques of ecstasy (W. R. Trask, Çev.; '
   'ss. 190–197). Princeton University Press. (Özgün eser y. 1951)',
 '“Declaran Patrimonio Cultural de la Nación a los conocimientos, saberes y usos del cactus San Pedro”, El Peruano, 2022':
   'Declaran Patrimonio Cultural de la Nación a los conocimientos, saberes y usos del '
   'cactus San Pedro. (2022). El Peruano.',
})

# Aynı kaynağın yazılarda geçen öteki yazım biçimleri.
METIN.update({
 'Turhan Baytop, Türkiye’de Bitkiler ile Tedavi: Geçmişte ve Bugün, 3. baskı (yay. haz. Feza Baytop Günergun), Nobel Tıp Kitabevleri, 2021, “Tarih ve gelişim” bölümü':
   BAYTOP_APA + ' (“Tarih ve gelişim” bölümü)',
 "Mircea Eliade, Shamanism: Archaic Techniques of Ecstasy (Radloff 1884'ten aktararak), s. 190-197":
   'Eliade, M. (1964). Shamanism: Archaic techniques of ecstasy (W. R. Trask, Çev.; '
   'ss. 190–197). Princeton University Press. (Özgün eser y. 1951)',
})

# Başlığı BÜYÜK HARFLE kayıtlı makaleler. APA başlığı cümle düzeninde ister;
# Latince tür adları ve özel adlar korunarak elle yazıldı. Bu katman
# otomatik önbelleğin önünde gelir.
ELLE.update({
 'https://dergipark.org.tr/tr/pub/aris/article/581882':
   'Oyman, N. R. (2019). Bazı Anadolu kilim motiflerinin sembolik çözümlemesi. '
   'Arış Dergisi, 14, 4–22.',
 'https://dergipark.org.tr/tr/pub/gida/article/1604084':
   'Topçu, K. Ç., Anlar, P., Çakır, Ö., & Sefalı, A. (2025). Sorbus aucuparia ve '
   'Sorbus kusnetzovii’den elde edilen etanol ekstraktlarının antioksidan kapasitesi, '
   'fenolik bileşik içeriği ve mineral kompozisyonu. Gıda, 50(2), 223–234.',
 'https://dergipark.org.tr/tr/pub/gtatder/article/767950':
   'Ovalı, F., Almaghrebi, E., Akat, F., & Vatansev, H. (2020). Dracaena cinnabari '
   'reçinesi ve tıbbi olarak kullanımı. Geleneksel ve Tamamlayıcı Anadolu Tıbbı '
   'Dergisi, 2(2), 16–21.',
 'https://dergipark.org.tr/tr/pub/kalemisi/article/123908':
   'Ateşok, E. (2014). Karakeçili ilçesinde dokunan kilimlerin geleneksel motif '
   'özellikleri. Kalemişi Geleneksel Türk Sanatları Dergisi, 2(3), 23–38.',
 'https://dergipark.org.tr/tr/pub/millifolklor/article/819200':
   'Dağ, Ü. (2021). Türk ve İskandinav mitolojisinde ağaç sembolizmi. '
   'Millî Folklor, 17(132), 63–74.',
 'https://dergipark.org.tr/tr/pub/mutftd/article/523667':
   'Paşayeva, L., & Tekiner, H. (2014). Türk-İslam tıbbında safranın yeri. '
   'Lokman Hekim Dergisi, 4(3), 11–15.',
 'https://dergipark.org.tr/tr/pub/tkhcbva/article/1157366':
   'Gürsoy, Ü. (2013). Türk kültüründe ağaç kültü ve dut ağacı. Türk Kültürü ve '
   'Hacı Bektaş Veli Araştırma Dergisi, 66, 43–54.',
 'https://doi.org/10.16953/deusosbil.1676276':
   'Kocael, T. (2026). Antik dönem hayat ağacı: Kültürler arası bir inanışın izinde. '
   'Dokuz Eylül Üniversitesi Sosyal Bilimler Enstitüsü Dergisi, 28(1), 381–401. '
   'https://doi.org/10.16953/deusosbil.1676276',
 'https://doi.org/10.30794/pausbed.450535':
   'Balkanal, Z. (2019). Türk kültürünün değer yargılarını yansıtan kilim motiflerine '
   'tasarım açısından alternatif bir yaklaşım: Kaat’ı sanatında uygulamaları. '
   'Pamukkale Üniversitesi Sosyal Bilimler Enstitüsü Dergisi, 34, 1–14. '
   'https://doi.org/10.30794/pausbed.450535',
 'https://doi.org/10.47089/iuad.797850':
   'Aksoy, Ö. (2020). Tataristan’ın Kukmara Rayonu Mamaşir köyünde Sabantuy bayramı. '
   'İdil Ural Araştırmaları Dergisi, 2(2), 225–237. https://doi.org/10.47089/iuad.797850',
 'https://doi.org/10.53718/gttad.940879':
   'Büyükcan Sayılır, Ş. (2021). Türklerin ağaç ile mitolojik ve tarihî bağları üzerine '
   'bir değerlendirme. Genel Türk Tarihi Araştırmaları Dergisi, 3(6), 187–198. '
   'https://doi.org/10.53718/gttad.940879',
 'https://doi.org/10.55666/folklor.1637963':
   'Özşahin, M. (2025). Başkurt halk yaşamında, sanatında ve tıbbında kımız. '
   'Folklor Akademi Dergisi, 8(1), 8–16. https://doi.org/10.55666/folklor.1637963',
})

# APA künyesindeki yapısal ekler Türkçe yazılır. İngilizce sayfalarda aynı
# künye kullanılır, yalnızca bu ekler değiştirilir; eser adlarına dokunulmaz.
_EN = [
 ('(t.y.)', '(n.d.)'),
 ('Çev.;', 'Trans.;'), (', Çev.)', ', Trans.)'), ('Çev.).', 'Trans.).'),
 ('(Çev.).', '(Trans.).'),
 ('Yay. haz.', 'Ed.'), ('(Ed.).', '(Ed.).'),
 ('Özgün eser y.', 'Original work published'),
 ('. baskı)', 'rd ed.)'),
 ('[Bitkisel tıbbi ürün monografı]', '[Herbal medicinal product monograph]'),
 ('[Basın açıklaması]', '[Press release]'),
 ('[Ürün bilgisi]', '[Prescribing information]'),
 ('[Dağılım kaydı]', '[Distribution record]'),
 ('[Rehber]', '[Guidance]'), ('[Ek]', '[Annex]'),
 ('(Taslak;', '(Draft;'), ('(Kısaltılmış baskı)', '(Abridged ed.)'),
 ('ABD Ulusal Sağlık Enstitüleri', 'US National Institutes of Health'),
 ('ABD Ulusal Tıp Kütüphanesi', 'US National Library of Medicine'),
 ('ABD Gıda ve İlaç Dairesi', 'US Food and Drug Administration'),
 ('ABD Federal Düzenlemeler Kanunu', 'US Code of Federal Regulations'),
 ('Dünya Sağlık Örgütü', 'World Health Organization'),
 ('Fitoterapi kitabındaki atıfla; ev bitkileri verisi',
  'as cited in the phytotherapy book; house plant data'),
 ('Fitoterapi kitabındaki atıfla', 'as cited in the phytotherapy book'),
 ('(“Zehirli bitkiler” bölümü)', '(chapter on poisonous plants)'),
 ('T.C. Sağlık Bakanlığı Sağlık Hizmetleri Genel Müdürlüğü',
  'Turkish Ministry of Health, General Directorate of Health Services'),
 (' ve ark.', ' et al.'),
]
# Ordinal düzeltmesi: "3. baskı" gibi Türkçe sıra sayıları
_ORD = {'1': 'st', '2': 'nd', '3': 'rd'}


def ingilizce(apa):
    """Künyenin İngilizce sayfalar için uyarlanmış hâli."""
    import re as _re
    def _bask(m):
        n = m.group(1)
        return f'{n}{_ORD.get(n[-1], "th") if not n.endswith(("11","12","13")) else "th"} ed.'
    apa = _re.sub(r'(\d+)\. baskı', _bask, apa)
    for a, b in _EN:
        apa = apa.replace(a, b)
    return apa


def ema_apa_en(ad):
    return f'European Medicines Agency. (n.d.). {ad} [Herbal medicinal product monograph].'


def nccih_apa_en(ad):
    baslik = NCCIH_BASLIK.get(ad) or (ad.replace('-', ' ').capitalize())
    return (f'National Center for Complementary and Integrative Health. (n.d.). {baslik}. '
            'US National Institutes of Health.')


def powo_apa_en(ad):
    return f'Plants of the World Online. (n.d.). {ad}. Royal Botanic Gardens, Kew.'
