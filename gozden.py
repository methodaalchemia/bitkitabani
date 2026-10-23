# Uzman gözden geçirmesi. Eczacı ya da başka bir uzman bir bitki sayfasını kontrol ettiğinde buraya eklenir;
# sayfada "Gözden geçiren" satırı ve arama motorları için reviewedBy / lastReviewed bilgisi çıkar.
# KISI boş kaldıkça hiçbir şey gösterilmez. Kişinin adı yalnızca kendi yazılı onayıyla yazılır.
KISI = None   # örnek: dict(ad='Ecz. Ad Soyad', unvan='Eczacı', aciklama='… Üniversitesi Eczacılık Fakültesi mezunu', url=None)
SAYFALAR = {}  # bitki id -> gözden geçirme tarihi, örnek: {'ihlamur': '2026-11-02'}
