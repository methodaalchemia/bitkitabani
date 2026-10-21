# Yayın kuyruğu: her gün bir yeni bitki

Bu klasördeki bitkiler, `yayin` tarihlerinde siteye kendiliğinden eklenir. GitHub Actions her gece 00:05'te (Türkiye saati) siteyi yeniden derler. `build.py`, tarihi gelmiş kayıtları kataloğa katar. Tarihi gelmemiş kayıtlar sitede hiç görünmez; ana sayfada yalnızca "Yarın: … bölgesinden yeni bir bitki geliyor" diye anılır.

## Yeni kayıt eklemek

1. Yeni bir `kN.py` dosyası aç ve `kuyruk/__init__.py` içindeki `FILES` listesine ekle.
2. Tarihler son kaydın ertesi gününden başlayıp birer gün artmalı. Aynı tarih iki kez kullanılamaz; `__init__.py` bunu denetler.
3. `id` küçük harfli, Türkçe karaktersiz olmalı ve katalogda (`data.json`) ya da kuyrukta zaten bulunmamalı.
4. Sırayı Türkiye'de en çok arananlardan başlat.
5. Kayıt alanları (örnek için `k1.py`):
   - Katalogla aynı alanlar: `tr, la, fam, diger, bolge, kat, kisim, kul, haz, bilim, kanit, guv, guvNot, ilginc`
   - `ek` (mevsim, yetisme, yoresel, karisma)
   - `taxon` (POWO bağlantısı için)
   - `foto`: Wikimedia Commons dosya adı. Fotoğrafta böcek olmamalı; tür adı doğru olmalı. `tools/cand.txt` ile aday topla.
   - Kaynaklar:
     - `ema`: EMA monografı; adres önce doğrulanmalı.
     - `nccih`: sayfa adı.
     - `kaynak`: PubMed/PMC bağlantıları. PMID'ler `tools/research.txt` + "Kaynak araştırması" iş akışıyla bulunur. **Bellekten PMID yazma.**
   - Etkileşimler: `guv` 'orta' ya da 'yuksek' ise `etk` ve `etk_en` (ilaç etkileşimleri).
   - `rel`: ilgili bitki id'leri.
   - `en`: İngilizce sürüm. Alanlar: name, other, part, uses, prep, science, safety, fact, season, habitat, local, confusion.
6. İçerik kuralları:
   - Her sağlık iddiası bir kaynağa dayanmalı. Emin olunmayan yöresel adlar yazılmaz.
   - Ton: düz, kısa cümleler; "mucize" dili yok.
   - Güvenlik notu açık olmalı: hamilelik, çocuklar, ilaç etkileşimleri.
   - Yasa dışı maddelerin hazırlanışı anlatılmaz.
7. `python3 build.py` ve `BT_DAY=<son tarih> python3 build.py` ikisi de hatasız çalışmalı. Sonra `rm -rf site && python3 build.py` ile temiz derle; gelecekteki bitkilerin sayfaları `site/` içinde kalmamalı.

## Instagram

`tools/ig.py`, her gün bir bitki için 6 slayt ve açıklama metni üretir. Paylaşımı `worker.js` yapar: her akşam 19:00'da, `IG_TOKEN` gizli değişkeni Cloudflare'de tanımlıysa.

- Sıra `IG_ORDER`'dadır: önce en çok arananlar, sonra kataloğun geri kalanı.
- Yüksek riskli ve yasal kısıtlı bitkiler Instagram'a konmaz.
- Durum: https://bitkitabani.com/api/ig-durum
- Önizleme: https://bitkitabani.com/ig/
