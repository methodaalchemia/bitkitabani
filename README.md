# Bitki Tabanı

Şifalı ve ritüel bitkiler için Türkçe etnobotanik veri tabanı: https://bitkitabani.com

- `data.json`: bitki kayıtları, bölgeler, kültür köprüleri
- `refs.py`: kaynak bağlantıları ve Wikipedia/Commons görsel eşleşmeleri
- `assets/`: stil ve tarayıcı betikleri
- `build.py`: `python3 build.py` komutu `site/` klasörünü yeniden üretir

Cloudflare Workers: `wrangler.jsonc` siteyi `site/` klasöründen yayınlar; GitHub’a her gönderimde otomatik yayın.
- `mapgeo.py` + `map_land.txt`: kültür köprüleri haritası (Natural Earth 1:110m, kamu malı)
- `extra.py`: doğada, karıştırma riski, koruma, Türkiye yasal durumu, harita koordinatları
- `tools/fetch_images.py`: GitHub Actions ile Commons görsellerini `img/` klasörüne indirir
