# TODO

Bu dosya Film Bilgi Sistemi için önceliklendirilmiş görev listesidir. Öncelikler proje akışına göre güncellenebilir.

## P0 - Kritik

- [ ] `.env` dosyasına gerçek `TMDB_API_KEY` eklenerek canlı API testi yapılacak.
- [ ] `data/film_bilgi_sonuc.xlsx` çıktısı gerçek verilerle kontrol edilecek.
- [ ] TMDb aramasında yanlış film eşleşmesi olduğunda nasıl seçim yapılacağı belirlenecek.
- [ ] Excel dosyası açıkken kaydetme hatasının kullanıcı mesajı test edilecek.

## P1 - Yüksek Öncelik

- [ ] OMDb API key ile IMDb puanı doğrulanacak.
- [ ] Film bulunamadığında Excel satırında önceki veri kalmaması garanti edilecek.
- [ ] API hata mesajları terminalde daha açıklayıcı gösterilecek.
- [ ] `README.md` kurulum adımları farklı bir temiz klasörde yeniden test edilecek.
- [ ] Kod içinde başlangıç seviyesine uygun kısa yorumlar gözden geçirilecek.

## P2 - Orta Öncelik

- [ ] Basit JSON cache yapısı tasarlanacak.
- [ ] Cache dosyasının `.gitignore` kapsamına alınması değerlendirilecek.
- [ ] `logs/` klasörü ve hata log formatı belirlenecek.
- [ ] Excel kolon genişlikleri sonuç dosyasında otomatik iyileştirilecek.
- [ ] Çok uzun konu metinleri için hücre biçimlendirmesi geliştirilecek.

## P3 - Düşük Öncelik

- [ ] SQLite fazı için tablo taslağı hazırlanacak.
- [ ] Flask ve FastAPI karşılaştırması yapılacak.
- [ ] Web arayüzü için ilk ekran taslağı çıkarılacak.
- [ ] Portföy sayfası için proje açıklaması hazırlanacak.
- [ ] Örnek ekran görüntüleri eklenecek.

## Bakım Görevleri

- [ ] `CHANGELOG.md` her anlamlı değişiklikten sonra güncellenecek.
- [ ] `LEARNING.md` her çalışma oturumundan sonra işaretlenecek.
- [ ] `ROADMAP.md` tamamlanan sürüm hedeflerine göre güncellenecek.
- [ ] Gereksiz çıktı dosyalarının repoya eklenmediği kontrol edilecek.
