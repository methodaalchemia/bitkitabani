# Bitki Tabanı

Şifalı ve ritüel bitkiler için Türkçe etnobotanik veri tabanı: https://bitkitabani.com

- `data.json`: bitki kayıtları, bölgeler, kültür köprüleri
- `refs.py`: kaynak bağlantıları ve Wikipedia/Commons görsel eşleşmeleri
- `assets/`: stil ve tarayıcı betikleri
- `build.py`: `python3 build.py` komutu `site/` klasörünü yeniden üretir

Cloudflare Workers: `wrangler.jsonc` siteyi `site/` klasöründen yayınlar; GitHub’a her gönderimde otomatik yayın.
