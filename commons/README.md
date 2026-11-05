# Commons için motif çizimleri

`motifler.py` içindeki 48 motif, site dışında da kullanılabilsin diye bağımsız SVG dosyalarına aktarıldı.
Site içinde motifler `build.py` tarafından `currentColor` ile satır içi çiziliyor; buradaki dosyalar
aynı çizimin sabit renkli (#1b1b1b), `xmlns` taşıyan, tek başına açılabilen sürümü.

- `motif_export.py` — SVG'leri üretir (`svg/` klasörüne yazar) ve `motifler.json` çıkarır.
  Çizimdeki el titremesi `random.Random(slug)` ile tohumlandığı için çıktı her çalıştırmada aynıdır.
- `commons_desc.py` — her dosya için Wikimedia Commons açıklama metnini (`{{Information}}` + CC BY-SA 4.0
  + kategoriler) üretir, `aciklamalar.json` olarak yazar.
- `svg/` — 48 dosya.

Lisans: çizimler Edanaz Tınmazlar'a ait, CC BY-SA 4.0.
