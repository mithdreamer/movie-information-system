# Changelog

Film Bilgi Sistemi projesindeki tüm anlamlı değişiklikler bu dosyada takip edilir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) yaklaşımını temel alır ve sürümleme [Semantic Versioning](https://semver.org/) mantığına göre yapılır.

## [Unreleased]

### Added

- Profesyonel proje dokümantasyonu eklendi.
- `MASTER.md`, `ROADMAP.md`, `TODO.md`, `CHANGELOG.md`, `CONTRIBUTING.md` ve `LEARNING.md` dosyaları hazırlandı.

### Changed

- `README.md` dosyası proje mimarisi, kurulum, kullanım, klasör yapısı ve gelecek hedefleriyle genişletildi.

## [0.1.0] - 2026-07-06

### Added

- İlk Python proje iskeleti oluşturuldu.
- `requirements.txt` dosyası eklendi.
- `.env.example` dosyası eklendi.
- `.gitignore` dosyası eklendi.
- Excel şablonu `data/film_bilgi_sablonu.xlsx` olarak oluşturuldu.
- `src/config.py` ile API key okuma yapısı eklendi.
- `src/excel_handler.py` ile Excel okuma ve yazma fonksiyonları eklendi.
- `src/tmdb_client.py` ile TMDb arama, detay, credits ve external IDs fonksiyonları eklendi.
- `src/omdb_client.py` ile IMDb ID üzerinden OMDb sorgu fonksiyonu eklendi.
- `src/movie_service.py` ile film verisini birleştiren servis katmanı eklendi.
- `src/main.py` ile uçtan uca çalışma akışı eklendi.
- `docs/OGRENME_NOTLARI.md` ve `docs/GELISTIRME_PLANI.md` başlangıç dokümanları eklendi.

### Verified

- `python -m compileall src` komutu başarıyla çalıştırıldı.
- API key olmadan çalışma senaryosu test edildi ve sonuç dosyasında `Eksik API key` durumu üretildi.

## Sürüm Etiketleri

- `[Unreleased]`: Henüz sürüm olarak yayınlanmamış değişiklikler.
- `[0.1.0]`: Faz 1 başlangıç iskeleti.
