"""images.json ile refs.FILES uyuşuyor mu?

24-25 Kasım 2026: elle seçilen dört görsel yayına çıkmadı. refs.py doğruydu,
img/ dosyaları yenilenmişti, ama images.json eski dosya adlarını tutuyordu;
sayfada görünen fotoğraf ile altındaki kaynak-lisans satırı farklı dosyaları
gösteriyordu. Sebep iş akışının push döngüsündeki `git pull --rebase -X ours`:
çakışmada karşı taraf korunduğu için botun yazdığı images.json geri alınabiliyor.

Bu kontrol elle seçilmiş her kayıt için images.json'daki 'file' alanının
refs.FILES ile aynı olmasını ve küçük/büyük boy dosyaların bulunmasını ister.
Uyuşmazlık bulursa 1 ile çıkar; derlemeden önce çalıştırılır.
"""
import json, os, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KOK)
from refs import FILES

meta = json.load(open(os.path.join(KOK, 'images.json'), encoding='utf-8'))
hata = []
for pid, dosya in FILES.items():
    k = meta.get(pid)
    if not k:
        continue                      # henüz indirilmemiş: iş akışı indirecek
    if k.get('file') != dosya:
        hata.append(f'{pid}: images.json "{k.get("file")}" diyor, refs.py "{dosya}" diyor')
        continue
    for boy in (500, 960):
        if not os.path.exists(os.path.join(KOK, 'img', f'{pid}-{boy}.jpg')):
            hata.append(f'{pid}: img/{pid}-{boy}.jpg yok')

for h in hata:
    print('UYUŞMAZLIK', h)
print(f'{len(FILES)} elle seçim denetlendi, {len(hata)} uyuşmazlık')
sys.exit(1 if hata else 0)
