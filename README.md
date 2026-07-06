# Film Bilgi Sistemi

Python ile geliştirilen Film Bilgi Sistemi, Excel dosyasına yazılan Türkçe film adlarını okuyarak TMDb ve isteğe bağlı OMDb API üzerinden film bilgilerini çeker. Sonuçları yeni bir Excel dosyasına düzenli şekilde yazar.

> **English summary:** Film Bilgi Sistemi is a Python-based movie information automation project. It reads movie names from an Excel file, fetches metadata from TMDb and optional IMDb ratings from OMDb, then writes the results back to an Excel output file.

## Proje Amacı

Bu projenin ilk hedefi sade, öğretici ve çalışır bir veri akışı kurmaktır:

```txt
Excel input -> Python script -> TMDb / OMDb API -> Excel output
```

Kullanıcı yalnızca Excel dosyasındaki A kolonuna film adlarını yazar. Program diğer kolonları API verileriyle doldurur.

## Temel Özellikler

- Excel dosyasından Türkçe film adı okuma
- TMDb API ile film arama
- Film yılı, orijinal ad, konu, tür, yönetmen ve oyuncu bilgisi çekme
- TMDb external IDs üzerinden IMDb ID alma
- OMDb API varsa IMDb puanı ekleme
- Sonuçları yeni Excel dosyasına yazma
- Eksik API key, bulunamayan film ve API hataları için durum bilgisi üretme

## Teknolojiler

| Teknoloji | Kullanım Amacı |
|---|---|
| Python | Ana uygulama dili |
| requests | REST API istekleri |
| openpyxl | Excel okuma ve yazma |
| python-dotenv | `.env` dosyasından API key okuma |
| TMDb API | Ana film veri kaynağı |
| OMDb API | IMDb puanı ve ek bilgiler |

## Proje Mimarisi

Uygulama modüler bir yapıda tasarlanmıştır. Her dosya tek bir ana sorumluluğa sahiptir.

```txt
film-bilgi-sistemi/
|
|-- README.md
|-- MASTER.md
|-- ROADMAP.md
|-- TODO.md
|-- CHANGELOG.md
|-- CONTRIBUTING.md
|-- LEARNING.md
|-- requirements.txt
|-- .env.example
|-- .gitignore
|
|-- data/
|   |-- film_bilgi_sablonu.xlsx
|   |-- film_bilgi_sonuc.xlsx
|
|-- src/
|   |-- main.py
|   |-- config.py
|   |-- excel_handler.py
|   |-- tmdb_client.py
|   |-- omdb_client.py
|   |-- movie_service.py
|   |-- __init__.py
|
|-- docs/
|   |-- OGRENME_NOTLARI.md
|   |-- GELISTIRME_PLANI.md
```

## Modül Açıklamaları

| Dosya | Sorumluluk |
|---|---|
| `src/main.py` | Programın ana giriş noktasıdır. Excel okuma, sorgulama ve yazma akışını başlatır. |
| `src/config.py` | `.env` dosyasını okur ve API key değerlerini merkezi olarak sağlar. |
| `src/excel_handler.py` | Excel şablonunu okur, film adlarını alır ve sonuçları yazar. |
| `src/tmdb_client.py` | TMDb API ile arama, detay, credits ve external IDs isteklerini yapar. |
| `src/omdb_client.py` | IMDb ID ile OMDb API üzerinden ek bilgi almaya çalışır. |
| `src/movie_service.py` | TMDb ve OMDb verilerini tek bir temiz sonuç sözlüğünde birleştirir. |

## Kurulum

Proje klasörüne girin:

```powershell
cd "C:\Users\korhan.ors\Desktop\Flashdisk Korhan\GitHub\arsiv\Projeler\Değişik Sorgular\Film Bilgisi Çekme\film-bilgi-sistemi"
```

Sanal ortam oluşturun:

```powershell
python -m venv .venv
```

Sanal ortamı aktif edin:

```powershell
.\.venv\Scripts\Activate.ps1
```

Bağımlılıkları kurun:

```powershell
pip install -r requirements.txt
```

PowerShell script çalıştırmayı engellerse sanal ortamı açmadan da şu komutu kullanabilirsiniz:

```powershell
.\.venv\Scripts\python.exe src\main.py
```

## API Key Ayarları

`.env.example` dosyasını `.env` adıyla kopyalayın:

```powershell
Copy-Item .env.example .env
```

`.env` dosyasını düzenleyin:

```env
TMDB_API_KEY=your_tmdb_api_key_here
OMDB_API_KEY=your_omdb_api_key_here
```

TMDb API key zorunludur. OMDb API key opsiyoneldir; girilmezse sistem IMDb puanı olmadan devam eder.

## Excel Şablonu

Giriş dosyası:

```txt
data/film_bilgi_sablonu.xlsx
```

Çıkış dosyası:

```txt
data/film_bilgi_sonuc.xlsx
```

Excel kolonları:

| Kolon | Alan |
|---|---|
| A | Türkçe Film Adı |
| B | İngilizce / Orijinal Ad |
| C | Yapım Yılı |
| D | Yönetmen |
| E | Başrol Oyuncuları |
| F | Tür |
| G | Konu |
| H | IMDb ID |
| I | IMDb Puanı |
| J | Durum |

## Kullanım

`data/film_bilgi_sablonu.xlsx` dosyasını açın ve A kolonuna film adlarını yazın:

```txt
A2: Esaretin Bedeli
A3: Yeşil Yol
A4: Babam ve Oğlum
A5: Inception
A6: Interstellar
```

Programı çalıştırın:

```powershell
python src\main.py
```

Sonuçlar `data/film_bilgi_sonuc.xlsx` dosyasına yazılır.

## Durum Değerleri

| Durum | Anlamı |
|---|---|
| `Bulundu` | Film bilgisi başarıyla alındı. |
| `Film bulunamadı` | TMDb aramasında sonuç bulunamadı. |
| `API hatası` | API isteği sırasında hata oluştu. |
| `Eksik API key` | TMDb API key değeri girilmedi. |
| `OMDb bilgisi alınamadı` | TMDb sonucu bulundu ancak OMDb ek bilgisi alınamadı. |

## Gelecek Hedefleri

- JSON cache ile aynı filmleri tekrar sorgulamayı önlemek
- Daha ayrıntılı hata logları eklemek
- SQLite veritabanı ile kalıcı kayıt sistemi kurmak
- Flask veya FastAPI ile web arayüzü geliştirmek
- Excel dışa aktarma seçeneklerini genişletmek
- Kişisel portföy sitesine proje tanıtımı eklemek

## Dokümantasyon

- [MASTER.md](MASTER.md): Proje ana kontrol dokümanı
- [ROADMAP.md](ROADMAP.md): Sürüm bazlı geliştirme planı
- [TODO.md](TODO.md): Önceliklendirilmiş görev listesi
- [CHANGELOG.md](CHANGELOG.md): SemVer uyumlu değişiklik geçmişi
- [CONTRIBUTING.md](CONTRIBUTING.md): Katkı kuralları
- [LEARNING.md](LEARNING.md): Öğrenme ve ilerleme takip planı

## Lisans

Bu proje öğrenme ve kişisel geliştirme amacıyla hazırlanmıştır. Lisans bilgisi daha sonra netleştirilecektir.
