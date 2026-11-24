# 1000 bitki hedefi: toplu kayıt yazma yönergesi (24 Kasım 2026)

Bu yönerge, `veri/parti/pNNN.txt` dosyasındaki bitkiler için tam derinlikte kayıt yazan herkes içindir.
Site: bitkitabani.com, Türkçe + İngilizce, kaynaklı şifalı ve ritüel bitkiler veritabanı. Sitenin bütün değeri her iddianın gerçek bir kaynağa dayanmasıdır.

## Çıktı
Tek dosya: `kuyruk/aNNN.py` (NNN parti numarası). İçinde `Q = [ {...}, {...} ]` listesi. Başka hiçbir dosyaya dokunma; `build.py` çalıştırma; git komutu çalıştırma.
Örnek kayıt biçimi için `kuyruk/k58.py` ve `kuyruk/k57.py` dosyalarını oku (alan adları ve uzunluk için ölçü bunlar). Alanların açıklaması `kuyruk/README.md` içinde.

Her kayıtta şu alanlar olmalı:
- `yayin`: `'2026-11-24'`, `arsiv`: `True`, `foto`: `''`
- `id`: parti dosyasında verilen id (değiştirme)
- `tr`: Türkçe ad. Parti dosyasındaki ad bir öneridir; güvenilir bir kaynakta daha doğru bir Türkçe ad bulursan onu yaz. Türkçede yerleşik adı yoksa özgün adı (örn. "Muira puama") kullan.
- `la`: Kabul edilen bilimsel ad, yazar kısaltmasıyla (POWO'ya göre: https://powo.science.kew.org). Parti dosyasındaki ad eş adsa kabul edilen adı yaz, eski adı `diger` içinde an.
- `taxon`: Yazar kısaltması olmadan kabul edilen ad (POWO bağlantısı için).
- `fam`: `Latince (Türkçe)` biçiminde; Türkçe karşılık için `veri/familya_tr.json` dosyasına bak, orada yoksa yalnızca Latince yaz.
- `diger`: yalnızca adlar: eş ad(lar), İngilizce ad, kaynakta geçen başka adlar; virgülle ayrılmış kısa bir satır, en çok 200 karakter (düz metin, `**` yok). Açıklama ve tarihçe buraya değil `ilginc` ya da `kul` içine.
- `bolge`: liste; yalnızca şunlar: anadolu, avrupa, asya, afrika, kamerika, amazon, and, okyanusya
- `kat`: liste; yalnızca şunlar: sifa, besin, ritual, zehir, tutsu
- `kisim`: kullanılan kısım.
- `kul`: `[[başlık, metin], ...]` en az 2, tercihen 3-4 bölüm. Başlık "Bölge/kültür — konu" biçiminde. Her bölüm 2-5 cümle.
- `haz`: hazırlama (bkz. kurallar). 3-6 cümle.
- `bilim`: araştırmaların ne gösterdiği, hangi tür çalışma olduğu (hücre, hayvan, klinik, derleme), sayılarla. 4-8 cümle. Kanıtı olduğundan büyük gösterme.
- `kanit`: `klinik` (insan çalışmalarıyla desteklenen), `sinirli` (az sayıda/küçük insan çalışması ya da yalnızca laboratuvar), `geleneksel` (yalnızca geleneksel kullanım)
- `guv`: `dusuk`, `orta`, `yuksek`
- `guvNot`: açık güvenlik notu: hamilelik, emzirme, çocuklar, ilaç kullananlar, zehirlenme belirtisi. Zehirli bitkide zehirlenme şüphesinde 114 (Ulusal Zehir Danışma Merkezi) ya da 112 aranması yazılır.
- `etk`: `guv` orta ya da yuksek ise zorunlu: `[[ilaç ya da madde, neden önemli], ...]`. Etkileşim verisi yoksa bunu açıkça yazan tek madde.
- `ilginc`: kaynaklı bir ilginç bilgi (ad kökeni, tarih, kültür). 1-3 cümle.
- `ek`: `{'mevsim':..., 'yetisme':..., 'yoresel':..., 'karisma':...}`. `yoresel`: yalnızca kaynakta geçen yöresel adlar; yoksa "Türkçede yerleşik bir yöresel adı yok." `karisma`: karıştırılabileceği türler ve ayırt etme; yoksa alanı yazma.
- `ema`: varsa `[[Latince drog adı, EMA adresi]]` (adresi açıp doğrula). Yoksa alanı yazma.
- `nccih`: varsa NCCIH sayfa adı (https://www.nccih.nih.gov/health/<ad>); adresi açıp doğrula. Yoksa yazma.
- `kaynak`: `[[künye, adres], ...]` en az 3, tercihen 4-8.
- `rel`: katalogda zaten olan ilgili bitkilerin id'leri (0-4 tane). Geçerli id'ler: `veri/mevcut_id.txt`.
- `en`: `name, other, part, uses, prep, science, safety, fact, season, habitat, local, confusion` (karisma yoksa confusion da yok).
- `etk_en`: `etk` varsa onun çevirisi.

## Çalışma sırası (kullanım sınırı yüzünden zorunlu)
Bitkileri TEK TEK bitir: bir bitkinin araştırmasını yap, kaydını hemen `kuyruk/aNNN.py` dosyasına ekle (dosya her an geçerli Python olsun), sonra sıradakine geç. Sekiz bitkinin araştırmasını biriktirip sona yazma; oturum yarıda kesilirse yazılmamış araştırma kaybolur. Bitki başına en fazla 6-8 arama/sayfa açma yeter.

## Kaynak kuralları (en önemli bölüm)
1. **Her adres bu oturumda WebSearch sonucunda görülmüş ya da WebFetch ile açılmış olmalı.** Bellekten PMID, DOI ya da adres yazma. Açamadığın, doğrulayamadığın kaynağı kayda koyma.
2. Künyedeki yazar, başlık, dergi, yıl kaynağın kendi sayfasından alınır; tahmin edilmez.
3. Kabul edilen kaynaklar: PubMed / PMC, Cochrane, EMA (HMPC monografları), WHO monografları, NCCIH, TİTCK, Kew POWO, IUCN Red List, FAO, DergiPark ve hakemli dergiler (yayıncının kendi sayfası ya da doi.org), üniversite açık erişim arşivleri, resmî kurum sayfaları (FDA, EFSA, Türk Patent, bakanlıklar), müze ve botanik bahçesi sayfaları.
4. **Yasak:** Wikipedia ve diğer wiki siteleri, bloglar, satış siteleri, sağlık içerik siteleri (WebMD, Healthline vb.), yapay zekâ özetleri, korsan kitap kopyaları.
5. Metinde yazdığın her sağlık, doz, zehirlilik ve tarih iddiası `kaynak`/`ema`/`nccih` listesindeki bir kaynakta gerçekten yazıyor olmalı. Kaynağın özetini okumadan sonuç yazma. Kaynakta olmayan sayı yazma.
6. Bir bitki için 3 sağlam kaynak bulamıyorsan o bitkiyi YAZMA; raporunda "atlandı: <id> — neden" diye bildir. İnce ya da uydurma kayıt, eksik kayıttan kötüdür.
7. Kaynak metnini kopyalama; kendi cümlelerinle aktar. Etnobotanik kaynaklardaki kaynak kişi ve köy adlarını yazma (il ve ilçe düzeyi yeter).
8. Metin içinde `[1]` gibi numara kullanma; kaynağı cümlede adıyla an ("2019 tarihli bir sistematik derleme…", "EMA monografı…").

## İçerik kuralları
- Ton: düz, kısa, resmî Türkçe cümleler. "Mucize", "şifa deposu", "kesin çözüm" gibi dil yok. Tavsiye verme; kaynağın söylediğini aktar.
- Geleneksel kullanım ile kanıtlanmış etki ayrı tutulur: "geleneksel olarak … için kullanılır" ile "… gösterilmiştir" aynı şey değil.
- Hazırlama: resmî monografta (EMA, WHO, TİTCK) doz varsa onu kaynağıyla ver. Yoksa "kabul edilmiş bir doz yoktur" yaz; doz uydurma. Zehirli (`guv: yuksek`) ve yasa dışı / psikoaktif bitkilerde hazırlama ve doz ANLATILMAZ: "Hazırlanması ve kullanılması önerilmez; bu sayfa bilerek tarif vermiyor." ve nedenini yaz.
- Vurgu için en fazla bir-iki yerde `**kalın**` (yalnızca `kul`, `haz`, `bilim`, `guvNot` içinde); ciddi uyarının başında `⚠️` kullanılabilir.
- Türkiye yazımı: "Türkiye" (İngilizcede de "Türkiye").
- **İngilizce, Türkçenin birebir çevirisidir:** alan alan, cümle cümle; ekleme, çıkarma, özetleme yok. Sayılar, uyarılar, `**` ve `⚠️` işaretleri aynen korunur. `en.name` İngilizce yaygın ad.
- Python sözdizimi: metinlerde tek tırnak yerine tipografik `’` kullan ya da dizgeleri çift tırnakla yaz; dosya `python3 -c "import ..."` ile yüklenebilmeli.

## Bitirmeden önce
`python3 tools/arsiv_denetle.py kuyruk/aNNN.py` çalıştır; hata kalmayana kadar düzelt.

## Rapor (son mesajın)
Kısa: yazılan id'ler, atlanan id'ler ve nedenleri, emin olamadığın ve insan gözünün bakması gereken noktalar (ad, doz, güvenlik düzeyi).
