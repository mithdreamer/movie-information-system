# Film Bilgi Sistemi - Master Doküman

Bu doküman, Film Bilgi Sistemi projesinin ana kontrol merkezi olarak kullanılır. Projenin amacı, kapsamı, kararları, sürüm hedefleri ve dokümantasyon bağlantıları burada özetlenir.

## Proje Özeti

Film Bilgi Sistemi, Excel dosyasındaki Türkçe film adlarını okuyarak TMDb ve isteğe bağlı OMDb API üzerinden film bilgilerini çeken Python tabanlı bir otomasyon projesidir.

İlk fazda odak, web arayüzü değil; çalışan, sade ve öğrenmeye uygun bir veri akışıdır.

## Ana Hedef

```txt
Türkçe film adı -> Python -> REST API -> JSON verisi -> Excel sonucu
```

## Kapsam

| Alan | Durum | Açıklama |
|---|---|---|
| Excel okuma | Tamamlandı | A kolonundan film adları okunur. |
| TMDb entegrasyonu | Başlangıç hazır | Film arama, detay, credits ve external IDs fonksiyonları eklendi. |
| OMDb entegrasyonu | Başlangıç hazır | IMDb ID ile ek bilgi çekme fonksiyonu eklendi. |
| Excel yazma | Tamamlandı | B-J kolonlarına sonuç yazılır. |
| Hata yönetimi | Başlangıç hazır | Eksik API key, API hatası ve bulunamayan film durumları işlenir. |
| Cache | Planlandı | Faz 2 kapsamında ele alınacak. |
| SQLite | Planlandı | Faz 3 kapsamında ele alınacak. |
| Web arayüzü | Planlandı | Faz 4 kapsamında ele alınacak. |

## Proje Prensipleri

- Kod başlangıç seviyesine uygun, okunabilir ve açıklayıcı olmalıdır.
- API key değerleri asla repoya eklenmemelidir.
- IMDb sayfalarından scraping yapılmamalı, API kullanılmalıdır.
- Her faz sonunda öğrenme notu tutulmalıdır.
- Büyük değişiklikler `CHANGELOG.md` dosyasına SemVer mantığıyla yazılmalıdır.

## Ana Dosyalar

| Dosya | Amaç |
|---|---|
| `README.md` | Genel proje tanıtımı ve kullanım rehberi |
| `ROADMAP.md` | Sürüm bazlı geliştirme planı |
| `TODO.md` | Öncelik sırasına göre görev listesi |
| `CHANGELOG.md` | Sürüm değişiklikleri |
| `CONTRIBUTING.md` | Katkı ve çalışma kuralları |
| `LEARNING.md` | Öğrenme hedefleri ve ilerleme takibi |

## Karar Kayıtları

| Tarih | Karar | Gerekçe |
|---|---|---|
| 2026-07-06 | İlk fazda web arayüzü yapılmayacak. | Önce Excel + API akışı öğrenilecek ve sağlamlaştırılacak. |
| 2026-07-06 | Ana veri kaynağı TMDb olacak. | Türkçe film adıyla arama için uygundur. |
| 2026-07-06 | OMDb opsiyonel destek olarak kullanılacak. | IMDb puanı gibi ek bilgiler için faydalıdır ancak zorunlu değildir. |
| 2026-07-06 | API key değerleri `.env` dosyasında saklanacak. | Güvenli ve taşınabilir yapı sağlar. |

## Mevcut Çalıştırma Komutu

```powershell
python src\main.py
```

## Başarı Kriterleri

- Program Excel dosyasındaki film adlarını okuyabilmeli.
- TMDb API key girildiğinde film bilgilerini çekebilmeli.
- Sonuçlar `data/film_bilgi_sonuc.xlsx` dosyasına yazılmalı.
- Hata durumlarında program kapanmadan kullanıcıya anlaşılır durum yazmalı.
- Dokümantasyon proje ilerledikçe güncel tutulmalı.
