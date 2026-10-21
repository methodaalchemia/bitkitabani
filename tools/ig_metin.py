# Instagram için elle yazılmış, sade ve sohbet diliyle metinler.
# Her bitki: kapak sorusu, kısaca (3 satır), hikâye, gelenek, bilim, dikkat, nasıl, kayıt cümlesi, yorum sorusu.
# Metni olmayan bitkiler tools/ig.py içinde katalog verisinden otomatik sadeleştirilir.

M = {
'zencefil': dict(
    kapak='Bulantıya gerçekten iyi gelir mi?', emoji='🫚',
    kisaca=[('Nereden', 'Hindistan ve Çin; Osmanlı mutfağında da baş baharat'), ('Ne için', 'Bulantı, soğuk algınlığı, hazımsızlık'), ('Kanıt', 'Bulantıda iyi. Gerisinde zayıf')],
    hikaye=('Kimse onu yabanda görmedi', 'Zencefilin yabani hâli bilinmiyor. Binlerce yıldır yalnızca insan eliyle, kök parçalarından çoğaltılıyor.'),
    gelenek=('Ayurveda’da adı: “evrensel ilaç”', 'Çin’de taze kökü kaynatılıp soğuk algınlığında içilir. Osmanlı macunlarında da hep vardı.'),
    bilim=('İşe yaradığı yer: bulantı', 'Avrupa İlaç Ajansı taşıt tutmasında kullanımını kabul ediyor. Hamilelik bulantısında küçük çalışmalar olumlu. Eklem ağrısı ve zayıflama iddiaları ise kanıtlanmış değil.'),
    dikkat=['Kan sulandırıcı kullanıyorsan', 'Safra taşın varsa', 'Yüksek doz takviye alacaksan'], dikkat_not='Yemekteki miktar güvenli.',
    nasil=('Zencefil çayı', '3–4 ince dilim taze zencefili bir bardak suda 10 dakika kaynat. Limon ve bal ekle.'),
    kaydet='Kaydet, kışın lazım olacak.', soru='Sen zencefili en çok nasıl kullanıyorsun?'),
}
