# Öğrenme Takip Planı

Bu dosya Film Bilgi Sistemi projesi boyunca öğrenilecek konuları takip etmek için hazırlanmıştır. Her çalışma oturumundan sonra ilgili maddeler işaretlenebilir ve kısa not eklenebilir.

## İlerleme Durumları

| İşaret | Anlamı |
|---|---|
| `[ ]` | Başlanmadı |
| `[~]` | Devam ediyor |
| `[x]` | Tamamlandı |

## Python Temelleri

- [x] Proje klasör yapısını anlamak
- [x] Python dosyalarını modüllere ayırmak
- [x] Fonksiyon tanımlamak ve çağırmak
- [x] `Path` ile dosya yollarını yönetmek
- [x] Liste ve sözlük veri yapılarını kullanmak
- [ ] Hata yakalama yapısını daha ayrıntılı öğrenmek
- [ ] Komut satırı argümanları ile dosya yolu almak
- [ ] Basit test yazımı öğrenmek

### Notlar

```md
Tarih:
Konu:
Ne öğrendim:
Zorlandığım nokta:
Sonraki adım:
```

## REST API

- [x] API key kavramını öğrenmek
- [x] HTTP GET isteği mantığını anlamak
- [x] `requests.get()` ile API çağrısı yapmak
- [x] Query parametrelerinin nasıl gönderildiğini görmek
- [ ] HTTP status code değerlerini daha detaylı öğrenmek
- [ ] Timeout ve bağlantı hatalarını yönetmek
- [ ] Rate limit kavramını öğrenmek
- [ ] API dokümantasyonu okuyarak endpoint seçmek

### Uygulama Notu

TMDb API ana veri kaynağıdır. OMDb API opsiyonel ek kaynak olarak kullanılacaktır.

## JSON Verisi

- [x] API cevabının JSON formatında geldiğini görmek
- [x] JSON verisini Python sözlüğü gibi okumak
- [x] İç içe alanlardan değer almak
- [ ] Boş veya eksik JSON alanlarını güvenli okumak
- [ ] JSON cache dosyası yazmak
- [ ] JSON cache dosyasından veri okumak
- [ ] JSON verisini okunabilir biçimde kaydetmek

### Örnek Takip

| Konu | Durum | Not |
|---|---|---|
| `results` listesini okuma | Tamamlandı | TMDb arama sonucunda kullanılıyor. |
| `genres` listesini işleme | Tamamlandı | Tür adları virgülle birleştiriliyor. |
| Cache JSON yapısı | Planlandı | Faz 2 kapsamında yapılacak. |

## Excel Otomasyonu

- [x] `openpyxl` paketini kullanmak
- [x] Excel dosyasını açmak
- [x] A kolonundan film adlarını okumak
- [x] B-J kolonlarına sonuç yazmak
- [x] Yeni sonuç dosyası kaydetmek
- [ ] Hücre stillerini daha iyi düzenlemek
- [ ] Kolon genişliklerini otomatik ayarlamak
- [ ] Kullanıcının boş satırlarını daha akıllı yönetmek
- [ ] Excel dosyası açıkken oluşan hatayı iyileştirmek

### Excel Kontrol Listesi

- [ ] Şablon dosyası açılıyor mu?
- [ ] A2'den başlayan film adları okunuyor mu?
- [ ] Sonuç dosyası oluşuyor mu?
- [ ] Uzun konu metinleri okunabilir görünüyor mu?
- [ ] Boş satırlar sorun çıkarmıyor mu?

## Web Geliştirme

Bu başlık Faz 4 için hazırlık amacıyla tutulur.

- [ ] Flask ve FastAPI farklarını öğrenmek
- [ ] Basit route yapısı kurmak
- [ ] HTML form ile film adı almak
- [ ] API sonucunu web sayfasında göstermek
- [ ] Excel çıktısı indirme butonu eklemek
- [ ] Basit kullanıcı hata mesajları tasarlamak
- [ ] Web projesi için klasör yapısı belirlemek

### Web Fazı İçin Sorular

- Flask mı FastAPI mi daha uygun?
- Web arayüzü Excel akışını tamamlayıcı mı olacak, alternatif mi olacak?
- Kullanıcı tek film mi sorgulayacak, liste halinde mi sorgulayacak?
- Sonuçlar veritabanına kaydedilecek mi?

## Proje Yönetimi

- [x] README dosyasını düzenlemek
- [x] Roadmap hazırlamak
- [x] TODO listesi oluşturmak
- [x] Changelog formatı belirlemek
- [x] Katkı rehberi hazırlamak
- [ ] Her faz sonunda kısa retrospektif yazmak
- [ ] Sürüm etiketleriyle çalışma alışkanlığı kazanmak

## Çalışma Günlüğü

Yeni çalışma notları bu alana eklenebilir.

### 2026-07-06

- Proje iskeleti oluşturuldu.
- Excel + API akışı için modüller hazırlandı.
- Profesyonel dokümantasyon seti oluşturuldu.
- Sonraki adım gerçek TMDb API key ile canlı veri testi yapmak.
