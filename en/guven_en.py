# English versions of the safety pages: drug interactions, pregnancy, poisonous plants.

# Drug groups, same keys and order as ILAC in build.py
ILAC_EN = {
    'kan': 'Blood thinners (warfarin, aspirin and others)', 'seker': 'Diabetes medicines and insulin',
    'tansiyon': 'Blood pressure medicines', 'kalp': 'Heart medicines (digoxin, heart rhythm drugs)',
    'antidep': 'Antidepressants and migraine medicines (triptans)', 'uyku': 'Sleeping pills, sedatives and alcohol',
    'hormon': 'Birth control pills and hormone therapy', 'bagisiklik': 'Immunosuppressants and transplant medicines',
    'diuretik': 'Diuretics (water pills)', 'lityum': 'Lithium', 'nobet': 'Seizure (epilepsy) medicines',
    'karaciger': 'Medicines broken down by, or straining, the liver', 'kortizon': 'Corticosteroids',
    'uyarici': 'Stimulants and caffeine', 'antibiyotik': 'Antibiotics', 'kanser': 'Cancer and HIV medicines',
    'demir': 'Iron supplements', 'mide': 'Stomach acid reducers', 'tum': 'All oral medicines (absorption effects)',
}

# Pregnancy page: table from the Turkish Ministry of Health phytotherapy book
FITO_PREG = [
    ('yarpuz', 'Pennyroyal (Mentha pulegium)', 'Listed among emmenagogue herbs (herbs that bring on menstruation); most of these can cause miscarriage and are contraindicated in pregnancy.'),
    ('sedef', 'Rue (Ruta graveolens)', 'Listed among emmenagogue herbs; contraindicated in pregnancy.'),
    ('adacayi', 'Sage (Salvia officinalis)', 'Listed among emmenagogue herbs; an oestrogenic effect is also reported. Contraindicated in pregnancy.'),
    ('pelin', 'Mugwort and wormwood (Artemisia)', 'Listed among emmenagogue herbs; contraindicated in pregnancy.'),
    ('tarcin', 'Cinnamon (Cinnamomum cassia)', 'Listed among herbs that stimulate uterine circulation; herbs in this group are mostly contraindicated in pregnancy.'),
    ('hayit', 'Chaste tree', 'Should not be used in pregnancy or while breastfeeding; the book notes it may be used only under medical supervision in one specific situation in early pregnancy.'),
    ('cemen', 'Fenugreek', 'Not suitable throughout pregnancy; not recommended while breastfeeding either, because there are not enough data.'),
    ('meyan', 'Licorice root', 'Although used as a galactagogue in folk practice, the book states it carries risk and should not be used in pregnancy or while breastfeeding.'),
    ('keten', 'Flaxseed', 'Because there are not enough data, it should not be used in pregnancy or while breastfeeding without medical advice.'),
    ('kediotu', 'Valerian', 'Not recommended in pregnancy or while breastfeeding without medical supervision.'),
]
FITO_PREG_NOTE = ('The same book lists ginger both among herbs that stimulate uterine circulation and as supported by clinical data for nausea in pregnancy, so ginger should also be used after talking to a doctor. '
                  'Fennel tea is reported to be usable in pregnancy and while breastfeeding at recommended doses, though some sources say for no longer than two weeks; anise tea when it does not greatly exceed amounts used in food.')
FITO_SRC = 'Turkish Ministry of Health, General Directorate of Health Services, Fitoterapi Uygulaması Kitabı (Phytotherapy Practice Book; eds. A. Tekin, İ. Tatlı Çankaya, A. U. Zeybek), Ankara, 2022; chapters on phytotherapy in gynaecology and obstetrics, and in pregnancy, the postpartum period and breastfeeding.'

# Poisonous plants page (mirrors zehirli.py)
Z_KARIS = {
 'gucigdemi': dict(ad='Autumn crocus', lat='Colchicum species',
     benzer='Edible crocus (Crocus) corms; in spring, wild garlic (ramsons) leaves',
     ayirt='According to Baytop, in the edible crocus the stem rises from the very centre of the corm, in autumn crocus from its side. Crushed wild garlic leaves smell strongly of garlic; autumn crocus leaves have no smell.',
     belirti='Colchicine poisoning: vomiting and severe diarrhoea starting a few hours later, followed by organ failure. Because symptoms start late, do not assume “nothing happened”.'),
 'baldiran': dict(ad='Poison hemlock', lat='Conium maculatum',
     benzer='Edible umbellifers such as parsley, wild carrot and fennel',
     ayirt='The stem is hairless, hollow and spotted purple-brown (Baytop). Crushed leaves give off an unpleasant smell like cat urine. Do not gather an umbellifer you cannot identify with certainty.',
     belirti='Burning in the mouth, muscle weakness, paralysis rising from the legs; breathing can stop. This is the plant that killed Socrates.'),
 'tatula': dict(ad='Thorn apple (jimsonweed)', lat='Datura stramonium',
     benzer='Its seeds can contaminate grain and pulses; its spiny fruit attracts children',
     ayirt='A spiny seed capsule the size of a walnut, containing black, kidney-shaped seeds. Crushed leaves have a heavy, unpleasant smell.',
     belirti='Dry mouth, dilated pupils, flushed face, fever, racing heart, agitation and hallucinations.'),
 'banotu': dict(ad='Henbane', lat='Hyoscyamus niger',
     benzer='Known locally in Turkey also as “gavurhaşhaşı” or “dağdağan”; the same names are given to other plants (Baytop)',
     ayirt='Sticky, hairy leaves, pale yellow flowers with purple veins and a heavy smell. Do not trust a local name; look at the plant itself.',
     belirti='The same picture as thorn apple: dry mouth, dilated pupils, racing heart, confusion.'),
 'yuksukotu': dict(ad='Foxglove', lat='Digitalis species',
     benzer='Before flowering, its leaves resemble comfrey and mullein leaves',
     ayirt='In flower: drooping, thimble-shaped flowers arranged on one side of the stem. Do not make tea from a flowerless leaf rosette you cannot identify with certainty.',
     belirti='Cardiac glycosides: nausea, vomiting, yellow-green vision, heart rhythm disorders.'),
}
Z_HALK = {
 'ormangulu': ('Mad honey (Pontic rhododendron)', 'Honey made by bees in the eastern Black Sea region from the flowers of Rhododendron ponticum (locally komar, kara ağu) and the yellow-flowered R. luteum (sarı ağu). Xenophon of Athens tells how Greek soldiers passing through the region around 400 BCE were poisoned by it. Today eating it by the spoonful as a “cure” is the main cause of poisoning: dizziness, nausea, sweating, a slow pulse and low blood pressure. It is treated in hospital (Baytop).'),
 'zakkum': ('Oleander', 'Grown everywhere in parks and gardens. Boiling its leaves and drinking the liquid for diabetes or cancer causes serious heart poisoning; even a small amount is dangerous.'),
 'hashas': ('Opium poppy', 'According to the Turkish Ministry of Health phytotherapy book, ethnobotanical studies still record opium being used to put children to sleep, a practice that goes back to Ottoman times. It can stop breathing in babies.'),
 '_badem': ('Bitter almond and apricot kernels', 'The amygdalin they contain turns into cyanide in the body. Even a few can be dangerous for children; bitter apricot kernels sold as a “cancer treatment” carry the same risk.'),
}
Z_NEDEN = ['Taking too much of a plant used for treatment',
           'Using a poisonous look-alike instead of a medicinal plant',
           'Eating a poisonous species by mistake instead of a plant gathered as a vegetable or herb',
           'Eating a part of a plant without knowing that it is poisonous',
           'Using poisonous plants to induce miscarriage']
Z_KAYNAK = ['Baytop T., Türkiye’de Bitkiler ile Tedavi: Geçmişte ve Bugün (Plant Healing in Turkey: Past and Present), 3rd ed., Nobel Tıp Kitabevleri, 2021',
            'Turkish Ministry of Health, Fitoterapi Uygulaması Kitabı (Phytotherapy Practice Book), 2022 (chapter on poisonous plants)',
            'Baytop T., Baytop A., Mat A., Sun S., Türkiye’de zehirli bitkiler, bitki zehirlenmeleri ve tedavi yöntemleri (Poisonous plants, plant poisonings and their treatment in Turkey), Istanbul University, 1989 (as cited in the phytotherapy book)']

# Baytop mix-up notes (mirrors baytop_kar.py)
BKAR_EN = {
 'hatmi': 'According to Baytop, although medicinal marshmallow grows in Anatolia, its flower is rarely found in trade; what herbalists sell as “marshmallow flower” is mostly hollyhock (Alcea) and other related species.',
 'salep': 'According to Baytop, because salep is expensive, the powder is often mixed with wheat flour or starch; other powders are also sold in its place under names such as “common salep” or “artificial salep”. In Konya, the powdered bulbs of some star-of-Bethlehem (Ornithogalum) species have been recorded as a substitute for salep in ice cream.',
 'safran': 'According to Baytop, because saffron is so valuable it has long been fraudulently weighted with wax, oil, syrup or honey. Safflower is sometimes sold in its place because of its similar colour.',
 'adamotu': 'According to Baytop, in Istanbul’s street markets the roots of black bryony (Tamus communis) or squirting cucumber (Ecballium elaterium) are sometimes sold as mandrake root.',
 'ardic': 'According to Baytop, herbalists mostly sell the cones of prickly juniper (Juniperus oxycedrus) in place of common juniper berries.',
 'keten': 'According to Baytop, sellers have sometimes been found to supply defatted flaxseed meal instead of ground flaxseed.',
 'tarcin': 'According to Baytop, some herbalists sell cubeb pepper in place of cinnamon because they look somewhat alike.',
 'papatya': 'According to Baytop, the flowers of some Anatolian Anthemis species are also used as “chamomile”; Istanbul herbalists sell these larger flowers, which do not fall apart, in place of true chamomile, and buyers prefer them because they look showier.',
 'meyan': 'According to Baytop, the roots of bitter licorice (Glycyrrhiza echinata) are not valued because of their bitter compounds, but they are gathered and sold mixed with true licorice root.',
 'nane': 'According to Baytop, pennyroyal (Mentha pulegium) is sold as “mint” in the markets of Mediterranean towns.',
 'gucigdemi': 'According to Baytop, eating an autumn crocus corm by mistake in place of an edible crocus (Crocus) corm causes dangerous poisoning, especially in children. To tell them apart, look at where the stem leaves the corm: in the edible crocus it rises from the very centre, in autumn crocus from the side.',
}
