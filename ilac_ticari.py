"""İlaç gruplarının Türkiye'de yaygın ticari adları — yalnızca ARAMA kolaylığı için.

Kullanıcı "varfarin" değil "Coumadin", "metoprolol" değil "Beloc" bilir; etkileşim
aracında ilaç adıyla arama bu adlar olmadan işe yaramıyor. Buradaki adlar bir
etkileşim iddiası değildir: iddia grup düzeyinde ve kaynağıyla tabloda durur.
Liste eksiksiz değildir; eczacı gözden geçirmesinde güncellenecek.
"""

TICARI = {
    'kan':        ['Coumadin', 'Aspirin', 'Coraspin', 'Ecopirin', 'Plavix', 'Xarelto', 'Eliquis', 'Pradaxa', 'Clexane'],
    'seker':      ['Glucophage', 'Glifor', 'Diamicron', 'Amaryl', 'Lantus', 'Januvia', 'Jardiance'],
    'tansiyon':   ['Norvasc', 'Beloc', 'Concor', 'Delix', 'Coversyl', 'Diovan', 'Atacand'],
    'kalp':       ['Lanoxin', 'Digoxin', 'Cordarone'],
    'antidep':    ['Lustral', 'Prozac', 'Cipralex', 'Efexor', 'Cymbalta', 'Imigran'],
    'uyku':       ['Xanax', 'Rivotril', 'Diazem'],
    'hormon':     ['Yasmin', 'Yaz', 'Diane-35'],
    'bagisiklik': ['Sandimmun Neoral', 'Prograf', 'Cellcept'],
    'diuretik':   ['Lasix', 'Aldactone'],
    'lityum':     ['Lithuril'],
    'nobet':      ['Tegretol', 'Depakin', 'Lamictal', 'Keppra'],
    'karaciger':  ['Parol', 'Minoset'],
    'kortizon':   ['Prednol', 'Deltacortril'],
    'antibiyotik':['Augmentin', 'Cipro', 'Klacid'],
    'demir':      ['Ferro Sanol', 'Maltofer'],
    'mide':       ['Nexium', 'Lansor'],
}

# Etken madde adları da aranabilsin (ticari adı bilmeyen için)
ETKEN = {
    'kan':        ['varfarin', 'asetilsalisilik asit', 'klopidogrel', 'rivaroksaban', 'apiksaban', 'dabigatran', 'enoksaparin', 'heparin'],
    'seker':      ['metformin', 'gliklazid', 'glimepirid', 'insülin', 'sitagliptin', 'empagliflozin'],
    'tansiyon':   ['amlodipin', 'metoprolol', 'bisoprolol', 'ramipril', 'perindopril', 'valsartan', 'kandesartan'],
    'kalp':       ['digoksin', 'amiodaron'],
    'antidep':    ['sertralin', 'fluoksetin', 'essitalopram', 'venlafaksin', 'duloksetin', 'sumatriptan'],
    'uyku':       ['alprazolam', 'klonazepam', 'diazepam', 'zolpidem'],
    'hormon':     ['etinilestradiol', 'drospirenon', 'levonorgestrel'],
    'bagisiklik': ['siklosporin', 'takrolimus', 'mikofenolat'],
    'diuretik':   ['furosemid', 'spironolakton', 'hidroklorotiyazid'],
    'lityum':     ['lityum karbonat'],
    'nobet':      ['karbamazepin', 'valproat', 'lamotrijin', 'levetirasetam', 'fenitoin'],
    'karaciger':  ['parasetamol'],
    'kortizon':   ['metilprednizolon', 'prednizolon', 'deksametazon'],
    'uyarici':    ['kafein'],
    'antibiyotik':['amoksisilin', 'siprofloksasin', 'klaritromisin'],
    'mide':       ['esomeprazol', 'lansoprazol', 'pantoprazol'],
    'demir':      ['demir sülfat'],
}
