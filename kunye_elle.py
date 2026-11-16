# -*- coding: utf-8 -*-
"""Otomatik çözülemeyen künyelerin APA 7 karşılıkları.

Makale olmayan kaynaklar (kurum sayfaları, monograflar, veri tabanı kayıtları,
kitap) burada. Makaleler tools/apa.py ile yayıncı üstverisinden üretilir ve
kunye_apa.json'a yazılır; oraya elle bir şey yazılmaz.

Biçim: APA 7. Eser adları özgün dilinde bırakılır (çeviri yapılmaz), yapısal
ekler Türkçedir — tarihsiz kaynaklar için "t.y.", köşeli parantez içindeki
tür açıklamaları Türkçe.
"""
import json
import os
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
 'https://dergipark.org.tr/tr/download/article-file/176576':
   'Atay, İ. (1984). Tâli türlerimizden dişbudağın önemi ve silvikültürel özellikleri. '
   'İstanbul Üniversitesi Orman Fakültesi Dergisi, B 34(3), 17–31.',

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
 'https://doi.org/10.48070/erusosbilder.711330':
   'Hayırsever, B. (2020). Geleneksel el sanatlarında kullanılan çintemani motifi ve '
   'seramik sanatına yansımaları. Erciyes Üniversitesi Sosyal Bilimler Enstitüsü Dergisi, '
   '50(3), 9–22.',
 'https://dergipark.org.tr/tr/pub/tubar/article/177215':
   'Üstün, Ç. (2009). Eski bir Türk içeceği: Kımız (koumiss). '
   'Türklük Bilimi Araştırmaları, 26, 247–255.',
 'https://dergipark.org.tr/tr/download/article-file/162641':
   'Doğanay, A. (2003). XVI. yüzyıl İznik duvar çinilerinde meyve tasvirleri. '
   'Marmara Üniversitesi İlâhiyat Fakültesi Dergisi, 24, 43–63.',
 'https://dergipark.org.tr/tr/download/article-file/193311':
   'Ölmez, F. N. (2009). “Death” symbolism in Turkish weavings. '
   'Süleyman Demirel Üniversitesi Güzel Sanatlar Fakültesi Hakemli Dergisi ART-E, '
   '2009(4), 1–21.',
 'https://doi.org/10.21602/sduarte.1059623':
   'Karaçay, Ç. (2022). Boteh motifinin kökenine kısa bir bakış ve Anadolu Türk halı '
   'sanatında boteh tasvirleri. Süleyman Demirel Üniversitesi Güzel Sanatlar Fakültesi '
   'Sanat Dergisi ART-E, 15(29), 128–148.',
 'https://dergipark.org.tr/tr/download/article-file/29048':
   'Tali, Ş. (t.y.). Kayseri Tavlusun köyü mezarlığında bezemeli mezar taşları-II. '
   'Atatürk Üniversitesi Güzel Sanatlar Fakültesi Sanat Dergisi, 20, 97–124.',
 'https://doi.org/10.69787/bitigefd.1562376':
   'Seçilmiş, B. (2024). Ereğli ve çevresinin Hitit ve Geç Hitit dönemlerindeki dinî '
   'kültürü. bitig Edebiyat Fakültesi Dergisi, 4(8), 234–246.',
 'https://doi.org/10.53568/yyusbed.1597330':
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


# EMA bitkisel ilaç envanteri (ema_monograf.json): monografın adresi, ilk
# yayın tarihi, tedavi alanı ve değerlendirme sonucu. Tablo EMA'nın kendi
# "Download medicine data" çıktısından geliyor. Monograf sayfasının tarihi
# JavaScript'le yüklendiği için ham HTML'den okunamıyordu; tarih buradan.
EMA_MONOGRAF = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           'ema_monograf.json'), encoding='utf-8'))


def _ema_yil(url):
    """Monografın ilk yayın yılı; adres tabloda yoksa None."""
    if not url:
        return None
    slug = url.rstrip('/').rsplit('/', 1)[-1]
    return (EMA_MONOGRAF.get(slug) or {}).get('yil')


def titck_apa(latin_ad, yil=None):
    """TİTCK Tıbbi Bitki Listesi monografının APA künyesi.

    Monograf PDF'inde ayrı bir yayın tarihi yazılı değil; listedeki
    yayım tarihi sütunu bazı satırlarda var, bazılarında yok. Tarih
    bilinmiyorsa APA'nın tarihsiz biçimi kullanılır.
    """
    return (f'Türkiye İlaç ve Tıbbi Cihaz Kurumu. ({yil if yil else "t.y."}). '
            f'{latin_ad} [Tıbbi bitki monografı]. Tıbbi Bitki Listesi.')


def titck_apa_en(latin_ad, yil=None):
    return (f'Turkish Medicines and Medical Devices Agency. '
            f'({yil if yil else "n.d."}). {latin_ad} '
            '[Medicinal plant monograph]. Medicinal Plant List.')


def ema_apa(ad, url=None):
    """EMA bitkisel monografı künyesi."""
    yil = _ema_yil(url)
    return (f'European Medicines Agency. ({yil if yil else "t.y."}). {ad} '
            '[Bitkisel tıbbi ürün monografı].')


def ema_apa_en(ad, url=None):
    yil = _ema_yil(url)
    return (f'European Medicines Agency. ({yil if yil else "n.d."}). {ad} '
            '[Herbal medicinal product monograph].')


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


def powo_apa(ad, yazar=None):
    """POWO kaydının APA künyesi. Yazar kısaltması varsa adla birlikte yazılır.

    Yazar kısaltmaları çoğu kez noktayla bitiyor (L., Mill., Burm.f.);
    ardına bir nokta daha konmaz.
    """
    tam = f'{ad} {yazar}'.strip() if yazar else ad
    nokta = '' if tam.endswith('.') else '.'
    return (f'Plants of the World Online. (t.y.). {tam}{nokta} '
            'Royal Botanic Gardens, Kew.')


def powo_adres(kimlik):
    """Kalıcı POWO kayıt adresi."""
    return 'https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:' + kimlik



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

# 13 Kasım sonrası eklenen motif/yazı kaynakları.
ELLE.update({
 'https://doi.org/10.1501/antro_0000000358':
   'Demren, Ö. (2018). Türk kültüründe bir korku kültü olarak Sivas’ta Alkarısı ve '
   'Albasması inanışı. Antropoloji, 36, 1–27.',
 'https://dergipark.org.tr/tr/download/article-file/643813':
   'Acar, H. V. (2017). Türk halk hekimliğindeki ocak çeşitleri. '
   'Lokman Hekim Dergisi, 7(2), 54–72.',
 'https://doi.org/10.24155/tdk.2022.199':
   'Dilek, İ. (2022). Güney Sibirya’da (Altay bölgesi) bir aydınlanma hareketi olarak '
   'Ak Cañ / Süt Cañ (Burhanizm): Teşekkülü, temel ilkeleri ve tarihî seyri. '
   'Türk Dünyası Dil ve Edebiyat Dergisi, 53. https://doi.org/10.24155/tdk.2022.199',
 'https://islamansiklopedisi.org.tr/alkarisi':
   'Küçük, A. (1989). Alkarısı. TDV İslâm Ansiklopedisi (C. 2). Türkiye Diyanet Vakfı.',
})

# Makale sayfası bulundu ama üstverisi eksik ya da bozuk olan ikisi.
# Oymak: başlık BÜYÜK HARF, sayfa aralığı üstveride yok (PDF kapağında
# "S.55-74" yazıyor). Bulut: DergiPark başlığı Türkçe/İngilizce birlikte
# tutuyor, APA özgün dildeki başlığı ister.
ELLE.update({
 'https://dergipark.org.tr/tr/pub/firatilahiyat/article/1067778':
   'Oymak, İ. (2001). Eski Türk inanışlarından ağaç kültünün Malatya’daki izleri. '
   'Fırat Üniversitesi İlahiyat Fakültesi Dergisi, 6, 55–74.',
 'https://dergipark.org.tr/tr/pub/ataunisosbd/article/411741':
   'Bulut, İ. (2018). Anadolu’da inanışların ve geleneklerin doğa korunması açısından '
   'önemi üzerine örnekler. Atatürk Üniversitesi Sosyal Bilimler Dergisi, 11(46), '
   '119–134.',
})

# TİTCK monograf PDF'leri (kuyruk/k8.py'deki ilk parti).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/HederahelixL.46da4ab6263f4179b100319e18963e6b_a66612a6-308e-4ce9-b1be-3e24d66a74b6.pdf':
   titck_apa('Hedera helix L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/PlantagoovataForssk..pdf13db3a84bb1f466ab06f79db489eca8e_d021c0b3-2cbe-46b2-8738-8295f105ee52.pdf':
   titck_apa('Plantago ovata Forssk.'),
 'https://titck.gov.tr/storage/Archive/2026/dynamicModulesAttachment/VitisviniferaL.v1_f066e76f-99ff-46ca-8e28-91b751022bac.pdf':
   titck_apa('Vitis vinifera L.'),
})

# Kalan künyeler: UNESCO kayıtları ve üstverisi çözülemeyen üç makale.
# Makale künyeleri PDF'in kapak sayfasından yazıldı.
ELLE.update({
 'https://dergipark.org.tr/tr/pub/firatsbed/article/565652':
   'İpek, B. (2012). Kırgızistan’da bir Nevruz geleneği: Sümölök. '
   'Fırat Üniversitesi Sosyal Bilimler Dergisi, 22(2), 34–44.',
 'https://dergipark.org.tr/tr/download/article-file/3785644':
   'Ercan, H. (2023). İslamiyet’ten önce Türklerde kurban kavramı üzerine bir '
   'araştırma. Journal of Turkic Civilization Studies, 4(2), 132–145.',
 'https://dergipark.org.tr/tr/download/article-file/3020611':
   'Akkuş, Ö., & Altunöz, A. (2023). Simgesel anlatım bağlamında Saha yeri Isıah '
   'Güneşi karşılama alanı heykelleri. Sanat ve Sosyal Bilimler Dergisi, 1(1), '
   '6–16.',
 'https://ich.unesco.org/en/RL/spring-celebration-hdrellez-01284':
   'UNESCO. (2017). Spring celebration, Hıdrellez [İnsanlığın Somut Olmayan '
   'Kültürel Mirasının Temsilî Listesi].',
 'https://ich.unesco.org/doc/src/33887.pdf':
   'Türkiye Cumhuriyeti Kültür ve Turizm Bakanlığı. (t.y.). Hıdrellez '
   '[Ulusal envanter formu]. UNESCO.',
 'https://ich.unesco.org/en/decisions/11.COM/10.B.1':
   'UNESCO Hükümetlerarası Komite. (2016). Karar 11.COM 10.B.1: Nawrouz '
   '[Somut Olmayan Kültürel Mirasın Korunması Sözleşmesi kararı].',
})

METIN.update({
 'Turhan Baytop, Türkiye’de Bitkiler ile Tedavi: Geçmişte ve Bugün, 3. baskı, Nobel Tıp Kitabevleri, 2021':
   BAYTOP_APA,
})

ELLE.update({
 # Başlık Her Kelimesi Büyük yazılı ve sonunda dipnot yıldızı var; APA
 # cümle düzeni ister. Sayfa aralığı yayıncı üstverisinden (derginin
 # sürekli numaralandırması: 1802–1815).
 'https://dergipark.org.tr/tr/pub/atdd/article/632476':
   'Moldosultanova Avcı, G., & Borubayeva, E. (2019). Kırgızlarda “Albarstı” ile '
   'ilgili inançlar (Narın ve Isık-Köl bölgeleri örneğinde). Akademik Tarih ve '
   'Düşünce Dergisi, 6(3), 1802–1815.',
})

# TİTCK monograf PDF'leri (kuyruk/k9.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/CapsicumannuumL.var.minimumMillerHeiser1a57bc84143e4c25b2e555ecd599bd21_99b288ba-247e-4ba1-ae8a-843b17243ce7.pdf':
   titck_apa('Capsicum annuum L. var. minimum (Miller) Heiser'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/RhamnusfrangulaL.f0b77d85298d45fa994898cd3a153f98_08815d4a-e4d9-46fe-914b-3b811878457d.pdf':
   titck_apa('Rhamnus frangula L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/RheumpalmatumL.642ddc44bab44773a6e92ce3c5da5e7f_cfa59f56-7695-4dec-9a3d-081393fa0081.pdf':
   titck_apa('Rheum palmatum L.'),
})

# TİTCK monograf dosyaları (kuyruk/k10.py). Symphytum'unki .docx olarak
# yayımlanmış, diğerleri PDF.
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/HarpagophytumprocumbensDC.1f3aee27592549acbd161c86d382a2dd_e7eae39e-2b11-4ed6-a834-e758c16b8ef6.pdf':
   titck_apa('Harpagophytum procumbens DC.'),
 'https://titck.gov.tr/storage/Archive/2025/dynamicModulesAttachment/SymphytumofficinaleLv230.12.2025_369925b8-5621-4050-b510-f1da49766dca.docx':
   titck_apa('Symphytum officinale L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/PelargoniumsidoidesDC.V3_7feee38d-2a52-4217-bdc8-a923af40b8b3.pdf':
   titck_apa('Pelargonium sidoides DC.'),
})

# TİTCK monograf dosyaları (kuyruk/k11.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/TanacetumpartheniumL.SchultzBip6feaabf306b745419e4dde78b88bdf2d_010170a8-552c-4e1c-b7a9-73d336220a9e.pdf':
   titck_apa('Tanacetum parthenium (L.) Schultz Bip.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/MelaleucaalternifoliaMaidenandBetcheCheel58eddbd56bce4f8bb63fa177ca084ff3_5fcf1cfd-fb3b-424c-928d-c7dedf441141.pdf':
   titck_apa('Melaleuca alternifolia (Maiden & Betche) Cheel'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/EquisetumarvenseL.18854d9cb7fa43aab7fa97051497a1fa_c9bbb2db-9b3b-4f66-8ff0-714a51a79b3f.pdf':
   titck_apa('Equisetum arvense L.'),
})

# TİTCK monograf dosyaları (kuyruk/k12.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/CucurbitapepoL.v2_6a1790e8-b9ce-4b13-acb7-2892c9c24092.pdf':
   titck_apa('Cucurbita pepo L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/ArnicamontanaL.V2_3222564f-40c5-40fd-9dd2-be57aea057ad.pdf':
   titck_apa('Arnica montana L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/Vaccinummyrtillus5d08f485590d4249a3583081a086c7b1_5b750c9a-75a3-456e-b72a-6c304ce8d3a1.pdf':
   titck_apa('Vaccinium myrtillus L.'),
})

# TİTCK monograf dosyaları (kuyruk/k13.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/CalendulaofficinalisL.yaymlV2_ed72c61f-78da-474e-a20a-3fa6219b8964.pdf':
   titck_apa('Calendula officinalis L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/Centauriumerythraea99b92d0018da4d85ac5c6a293ffa570e_79c1e367-885c-47eb-91ee-664dfca60d2d.pdf':
   titck_apa('Centaurium erythraea Rafn s. l.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/HelichrysumarenariumL.Moench0b223e9429d04db0910b96618c8e9dae_6cc89fd4-9f6c-43fd-bbbe-adabc83e64e7.pdf':
   titck_apa('Helichrysum arenarium (L.) Moench'),
})

# TİTCK monograf dosyaları (kuyruk/k14.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/CapsellabursapastorisL.b70dff321ef6465ca8a12954dc8f64c3_923331a2-924d-4201-9cb4-232b00146934.pdf':
   titck_apa('Capsella bursa-pastoris (L.) Medikus'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/FumariaofficinalisL.aee311f77d9b47f18fe1305a30edcef0_8560bcc8-9297-4200-a6f7-b80ef5ee2c39.pdf':
   titck_apa('Fumaria officinalis L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/PlantagolanceolataL_26554602-5f71-4c75-b153-018e3f2ce8f1.pdf':
   titck_apa('Plantago lanceolata L.'),
})

# TİTCK monograf dosyaları (kuyruk/k15.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/RubusidaeusL.yaymlv1_d5fc123b-8b58-4e41-b143-6dc1bee880d4.pdf':
   titck_apa('Rubus idaeus L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/RuscusaculeatusL.dzenlenen_d9a6ed47-210c-4ef0-956c-f9277113d6a9.pdf':
   titck_apa('Ruscus aculeatus L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/EpilobiumangustifoliumL_26b9b54d-a7d1-4855-89f3-f910a6479257.pdf':
   titck_apa('Epilobium angustifolium L. / E. parviflorum Schreb.'),
})

# TİTCK monograf dosyaları (kuyruk/k16.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/CichoriumintybusL._aefa3f9b-53c8-48ab-91be-c8f8211ba5e7.pdf':
   titck_apa('Cichorium intybus L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/GentianaluteaL.V4_f6bbefa6-e09b-4c5c-bc38-1d08a5de67b1.pdf':
   titck_apa('Gentiana lutea L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/CistuscreticusL.v2_86e4e3d0-17c0-4579-8565-56d26569a180.pdf':
   titck_apa('Cistus creticus L.'),
})

# TİTCK monograf dosyaları (kuyruk/k17.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/SolidagovirgaureaL..pdfb279ef8596e34f17b127529054915c2a_bfcf2947-9179-490c-89a6-e3397a3e0d8d.pdf':
   titck_apa('Solidago virgaurea L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/OnonisspinosaL.900a25caf22c491691ce15a5bd305571_c15f9564-9cf5-4284-b1a9-f725e270b30a.pdf':
   titck_apa('Ononis spinosa L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/PeumusboldusMolina_23225ecb-beb0-4a4a-9a75-00f7c7e74940.pdf':
   titck_apa('Peumus boldus Molina'),
})

# TİTCK monograf dosyaları (kuyruk/k18.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/FilipendulaulmariaL.Maximcd0874ec02cc4a82867e8efdbbb1de37_67c91cf3-53a4-46c1-b04b-d50ef208aba7.pdf':
   titck_apa('Filipendula ulmariae (L.) Maxim.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/MarrubiumvulgareL.V1_feba4058-a88a-4176-b958-ba2484d3b8ed.pdf':
   titck_apa('Marrubium vulgare L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/LeonuruscardiacaL.7522b4e8ae384b16b4e9766dfcf45a8e_d1786ca7-5a4f-4061-8a65-d79eb5c72b14.pdf':
   titck_apa('Leonurus cardiaca L.'),
})

# TİTCK monograf dosyaları (kuyruk/k19.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/FucusvesiculosusL.v3_107a094e-671b-4bf4-b6a7-2d89514765ef.pdf':
   titck_apa('Fucus vesiculosus L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/CetrariaislandicaL.Achariuss.l_a6aaec19-153c-4518-a814-c10239409af6.pdf':
   titck_apa('Cetraria islandica (L.) Acharius s.l.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/IlexparaguariensisSt.Hilaire6d6b83817b114509a49eaec8add91541_dd66941a-c63b-43d1-b9e8-e0bdb2b248e2.pdf':
   titck_apa('Ilex paraguariensis St.-Hil.'),
})

# TİTCK monograf dosyaları (kuyruk/k20.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/PrimulaverisL._1db4d1c0-0eeb-40c6-90ce-4600dd95cf95.pdf':
   titck_apa('Primula veris L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/PrimulaelatiorL.Hill_b90ba805-ae98-4da2-840d-03d590857f89.pdf':
   titck_apa('Primula elatior (L.) Hill.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/PotentillaerectaL.Raeusch.v2_7104afdd-0181-46d5-a72f-549a5817cd17.pdf':
   titck_apa('Potentilla erecta (L.) Raeusch.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/AgrimoniaeupatoriaL.yaymlV2_33336722-c034-4c27-b528-d071e8ed3146.pdf':
   titck_apa('Agrimonia eupatoria L.'),
})

# TİTCK monograf dosyaları (kuyruk/k21.py).
ELLE.update({
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/HerniariaglabraL.v2_92203b68-9afb-4408-a482-d3bbd6df7888.pdf':
   titck_apa('Herniaria glabra L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/HerniariaglabraL.v2_e639c046-4574-49df-ad3e-7b795d58672b.pdf':
   titck_apa('Herniaria hirsuta L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/HerniariaincanaLam.v2_9892060a-f885-4491-92e3-6fde39c358bb.pdf':
   titck_apa('Herniaria incana Lam.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/ArctiumlappaL._b3576af0-4bbf-4f6b-b241-57f4f5f604f6.pdf':
   titck_apa('Arctium lappa L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/AgropyronrepensL.P.Beauv.v3_e9326d84-dea4-4d8f-ab8b-b6b8a71334f0.pdf':
   titck_apa('Agropyron repens (L.) P. Beauv.'),
})

ELLE.update({
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/EschscholziacaliforniaCham.V2_d331fb1b-294f-4e7e-a287-9e85cedab0cd.pdf':
   titck_apa('Eschscholzia california Cham.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/MelilotusofficinalisL.Lam25f3329baa35428bb04b2e9b194de6de_ae125682-b4fb-4dd3-a5df-fafbca70b485.pdf':
   titck_apa('Melilotus officinalis (L.) Lam.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/MenyanthestrifoliataL._c46f522d-f224-470d-b23c-0e6c196da59c.pdf':
   titck_apa('Menyanthes trifoliata L.'),
})

ELLE.update({
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/AvenasativaL._4e1fe68a-0ecb-4053-be4e-b84750043c5b.pdf':
   titck_apa('Avena sativa L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/CarumcarviL.v3_7efc8888-88eb-46cb-9645-a41c07b94efd.pdf':
   titck_apa('Carum carvi L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/ChamaemelumnobileL.AllV3_7130f392-0628-4f8d-8995-1a860e26ca3e.pdf':
   titck_apa('Chamaemelum nobile (L.) All.'),
})

ELLE.update({
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/ColanitidaVent.SchottetEndl._ac17e3c0-a16a-48ce-860c-65c3b58e4ba8.pdf':
   titck_apa('Cola nitida (Vent.) Schott et Endl. ve varyeteleri, '
             'Cola acuminata (P. Beauv.) Schott et Endl.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/Curcumaxanthorriza3e907b05928b4967a97d3cf474f0dd23_ab8cf9a4-24da-4888-a29f-3536b6e4205e.pdf':
   titck_apa('Curcuma xanthorrhiza Roxb.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/EleutherococcussenticosusRupr.EtMaximMaxim.6b1b514b6aba4677b491d1083caa2238_469bf25b-5ec2-4704-9ba2-122c0d06b7d0.pdf':
   titck_apa('Eleutherococcus senticosus (Rupr. et Maxim.) Maxim.'),
})

ELLE.update({
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/FragariamonografV2_9c978def-5f39-4a1e-808c-6522e28b0426.pdf':
   titck_apa('Fragaria vesca L., F. moschata Weston, F. viridis Weston, '
             'F. x ananassa (Duchesne ex Weston) Duchesne ex Rozier'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/GlycinemaxL.Merr.pdf09cd7736af7644089259ce38e73ec4d4_05c16cd8-57e8-4e8c-8a33-08b5dfeb640d.pdf':
   titck_apa('Glycine max (L.) Merr.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/PhaseolusvulgarisL._3bb46bf8-5ad6-48d6-9d24-104e5f9f7287.pdf':
   titck_apa('Phaseolus vulgaris L.'),
})

ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/GrindeliarobustaNutt_475dbd6b-0a04-4718-bf93-b35dd0f2cdb8.pdf':
   titck_apa('Grindelia robusta Nutt.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/PolypodiumvulgareL.v2_b6ff05b0-0ffd-4181-894e-4b0c5fa728db.pdf':
   titck_apa('Polypodium vulgare L.'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/SisymbriumofficinaleL.Scop_60a728f6-e428-4dfd-9a5c-85d4f40464a5.pdf':
   titck_apa('Sisymbrium officinale (L.) Scop.'),
})

ELLE.update({
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/LevisticumofficinaleW.D.J.Koch.376b692c333241c3aa52850f97183aeb_8472fc9b-c7c0-473e-9d79-9a530bf411da.pdf':
   titck_apa('Levisticum officinale W.D.J. Koch'),
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/Ribesnigrum_8f334f04-6a87-44c3-9c16-b7c2ed2fdd7d.pdf':
   titck_apa('Ribes nigrum L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/OenotherabiennisL.91ffe26a0be94bdc8723c9f806d8f09e_cb526320-64a9-42ad-8721-edfa6667a3e2.pdf':
   titck_apa('Oenothera biennis L.'),
 'https://titck.gov.tr/storage/Archive/2022/dynamicModulesAttachment/OenotheralamarckianaL.8dd2e9638daa4f26807b9890775b083d_6e75295c-b3ff-4894-a97c-387129832c32.pdf':
   titck_apa('Oenothera lamarckiana L.'),
})

ELLE.update({
 'https://titck.gov.tr/storage/Archive/2023/dynamicModulesAttachment/OriganumdictamnusL.v1_f08d6086-b3a7-4735-864d-9ec71a34df62.pdf':
   titck_apa('Origanum dictamnus L.'),
 'https://titck.gov.tr/storage/Archive/2024/dynamicModulesAttachment/PolygonumaviculareLv3_f6a639b3-d31f-4f59-8ca2-42ddc0fd244d.pdf':
   titck_apa('Polygonum aviculare L.'),
})

# Kurum yayını: APA'da kurumsal yazar ve yayın türü köşeli ayraçta.
ELLE['https://www.iarc.who.int/wp-content/uploads/2018/07/pr244_E.pdf'] = (
    'Uluslararası Kanser Araştırmaları Ajansı. (2016). IARC Monographs '
    'evaluate drinking coffee, maté, and very hot beverages '
    '[Basın açıklaması]. Dünya Sağlık Örgütü.')

# Kola cevizinin Igbo kültüründeki yerini belgeleyen dergi yazısı.
ELLE['https://ajol.info/index.php/ijah/article/view/157097/146708'] = (
    'Obineche, J. O. (2017). Kola nut: Revisiting the Igbo '
    'socio-cultural values and identity. International Journal of Arts '
    'and Humanities, 6(2), 94–107.')

# Bilim tarihi yazıları: biri dergi yazısı, biri podcast bölümü.
ELLE['https://www.sciencehistory.org/stories/magazine/aspirin-turn-of-the-century-miracle-drug/'] = (
    'Goldberg, D. R. (2009, 3 Haziran). Aspirin: Turn-of-the-century '
    'miracle drug. Distillations. Science History Institute.')
ELLE['https://www.sciencehistory.org/stories/disappearing-pod/the-life-saving-rat-poison/'] = (
    'Kean, S. (Sunucu). (2022, 4 Ekim). The lifesaving rat poison '
    '[Podcast bölümü]. The Disappearing Spoon. Science History Institute.')

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
 ('[Tıbbi bitki monografı]', '[Medicinal plant monograph]'),
 ('Tıbbi Bitki Listesi.', 'Medicinal Plant List.'),
 ('Türkiye İlaç ve Tıbbi Cihaz Kurumu',
  'Turkish Medicines and Medical Devices Agency'),
 ('[Basın açıklaması]', '[Press release]'),
 ('[Ürün bilgisi]', '[Prescribing information]'),
 ('[Dağılım kaydı]', '[Distribution record]'),
 ('[Rehber]', '[Guidance]'), ('[Ek]', '[Annex]'),
 ('(Taslak;', '(Draft;'), ('(Kısaltılmış baskı)', '(Abridged ed.)'),
 ('ABD Ulusal Sağlık Enstitüleri', 'US National Institutes of Health'),
 ('ABD Ulusal Tıp Kütüphanesi', 'US National Library of Medicine'),
 ('ABD Gıda ve İlaç Dairesi', 'US Food and Drug Administration'),
 ('ABD Federal Düzenlemeler Kanunu', 'US Code of Federal Regulations'),
 ('Uluslararası Kanser Araştırmaları Ajansı',
  'International Agency for Research on Cancer'),
 ('Dünya Sağlık Örgütü', 'World Health Organization'),
 ('Fitoterapi kitabındaki atıfla; ev bitkileri verisi',
  'as cited in the phytotherapy book; house plant data'),
 ('Fitoterapi kitabındaki atıfla', 'as cited in the phytotherapy book'),
 ('(“Zehirli bitkiler” bölümü)', '(chapter on poisonous plants)'),
 ('T.C. Sağlık Bakanlığı Sağlık Hizmetleri Genel Müdürlüğü',
  'Turkish Ministry of Health, General Directorate of Health Services'),
 ('(Sunucu)', '(Host)'),
 ('[Podcast bölümü]', '[Audio podcast episode]'),
 ('3 Haziran', 'June 3'), ('4 Ekim', 'October 4'),
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


def nccih_apa_en(ad):
    baslik = NCCIH_BASLIK.get(ad) or (ad.replace('-', ' ').capitalize())
    return (f'National Center for Complementary and Integrative Health. (n.d.). {baslik}. '
            'US National Institutes of Health.')


def powo_apa_en(ad, yazar=None):
    tam = f'{ad} {yazar}'.strip() if yazar else ad
    nokta = '' if tam.endswith('.') else '.'
    return (f'Plants of the World Online. (n.d.). {tam}{nokta} '
            'Royal Botanic Gardens, Kew.')
