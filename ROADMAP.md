# Roadmap

Bu yol haritası Film Bilgi Sistemi için sürüm bazlı geliştirme planını gösterir. Sürümler Semantic Versioning yaklaşımına uygun şekilde planlanır.

## Sürüm Mantığı

| Sürüm Tipi | Anlamı |
|---|---|
| `MAJOR` | Büyük mimari değişiklikler veya geriye dönük uyumsuz değişiklikler |
| `MINOR` | Yeni özellikler |
| `PATCH` | Hata düzeltmeleri ve küçük iyileştirmeler |

## v0.1.0 - Faz 1: Excel + API Temeli

Hedef: Excel'den film adı okuyup API üzerinden bilgi çekerek sonuç Excel dosyası üretmek.

- [x] Proje klasör yapısını oluştur
- [x] `requirements.txt`, `.env.example`, `.gitignore` dosyalarını ekle
- [x] Excel şablonunu oluştur
- [x] `config.py` ile `.env` okuma yapısını kur
- [x] `excel_handler.py` ile Excel okuma ve yazma akışını ekle
- [x] `tmdb_client.py` ile TMDb arama ve detay fonksiyonlarını ekle
- [x] `omdb_client.py` ile OMDb destek fonksiyonunu ekle
- [x] `movie_service.py` ile film verisini birleştir
- [x] `main.py` ile uçtan uca çalışma akışını kur
- [ ] Gerçek TMDb API key ile canlı test yap
- [ ] OMDb API key ile IMDb puanı testini tamamla

## v0.2.0 - Faz 2: Dayanıklılık ve Cache

Hedef: Aynı film adları için gereksiz API çağrılarını azaltmak ve hata görünürlüğünü artırmak.

- [ ] JSON tabanlı basit cache sistemi ekle
- [ ] Aynı film tekrar sorgulandığında cache sonucunu kullan
- [ ] Hata loglarını `logs/` klasörüne yaz
- [ ] API timeout ve bağlantı hataları için daha ayrıntılı mesaj üret
- [ ] Excel sonuçlarında kaynak bilgisi alanı eklemeyi değerlendir

## v0.3.0 - Faz 3: SQLite Veri Katmanı

Hedef: Çekilen film bilgilerini yerel veritabanında saklamak.

- [ ] SQLite veritabanı şeması oluştur
- [ ] Film bilgilerini veritabanına kaydet
- [ ] Daha önce sorgulanan filmi veritabanından getir
- [ ] Basit migration yaklaşımı belirle
- [ ] Excel çıktısını veritabanı kayıtlarıyla uyumlu hale getir

## v0.4.0 - Faz 4: Web Arayüzü

Hedef: Excel dışındaki kullanım senaryoları için basit bir web arayüzü hazırlamak.

- [ ] Flask veya FastAPI tercihini netleştir
- [ ] Film adı giriş formu oluştur
- [ ] Sonuçları web sayfasında göster
- [ ] Excel'e aktar butonu ekle
- [ ] Kullanıcı dostu hata ekranları hazırla

## v0.5.0 - Faz 5: Portföy ve Yayın Hazırlığı

Hedef: Projeyi kişisel portföyde gösterilebilir bir öğrenme projesi haline getirmek.

- [ ] Ekran görüntüleri hazırla
- [ ] Proje açıklamasını portföy formatına dönüştür
- [ ] Demo kullanım videosu veya GIF eklemeyi değerlendir
- [ ] GitHub README görsel düzenini iyileştir
- [ ] Lisans bilgisini netleştir

## v1.0.0 - İlk Kararlı Sürüm

Hedef: Excel + API + cache + veritabanı + temel web arayüzünün kararlı hale gelmesi.

- [ ] Kurulum adımları yeni kullanıcı için baştan sona doğrulanmış olmalı
- [ ] Temel test senaryoları yazılmış olmalı
- [ ] Bilinen kritik hata kalmamalı
- [ ] Dokümantasyon güncel olmalı
- [ ] Örnek veri ve örnek çıktı net şekilde sunulmalı
