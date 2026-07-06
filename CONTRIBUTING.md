# Katkı Rehberi

Film Bilgi Sistemi kişisel öğrenme odaklı bir projedir. Katkı süreci sade, anlaşılır ve sürdürülebilir olmalıdır.

## Katkı İlkeleri

- Kod okunabilir ve başlangıç seviyesine uygun olmalıdır.
- Her modül tek bir ana sorumluluğa sahip olmalıdır.
- API key, şifre veya kişisel veri repoya eklenmemelidir.
- IMDb web sitesinden scraping yapılmamalıdır; API kaynakları kullanılmalıdır.
- Değişiklikler mümkün olduğunca küçük ve anlamlı parçalara ayrılmalıdır.

## Çalışma Ortamı

Projeyi çalıştırmak için:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`.env` dosyası oluşturmak için:

```powershell
Copy-Item .env.example .env
```

## Kod Standartları

- Fonksiyon adları açık ve anlaşılır olmalıdır.
- Gereksiz karmaşık soyutlamalardan kaçınılmalıdır.
- Hata mesajları kullanıcı için anlaşılır olmalıdır.
- Uzun fonksiyonlar gerektiğinde daha küçük parçalara bölünmelidir.
- Yeni özelliklerde ilgili dokümantasyon güncellenmelidir.

## Commit Mesajı Önerisi

Commit mesajları kısa ve açıklayıcı olmalıdır:

```txt
feat: add movie cache layer
fix: handle empty TMDb response
docs: update roadmap for sqlite phase
refactor: simplify excel writing flow
```

## Değişiklik Kontrol Listesi

Bir değişiklik tamamlandığında şu maddeler kontrol edilmelidir:

- [ ] Kod çalışıyor mu?
- [ ] Excel girdi ve çıktı akışı bozulmadı mı?
- [ ] API key veya kişisel veri eklenmedi mi?
- [ ] README veya ilgili doküman güncellendi mi?
- [ ] CHANGELOG dosyasına not eklendi mi?
- [ ] Yeni öğrenilen konu LEARNING dosyasına işaretlendi mi?

## Test Önerileri

Şimdilik resmi test paketi yoktur. Minimum doğrulama:

```powershell
python -m compileall src
python src\main.py
```

Gerçek API key ile test yapılırken Excel şablonunda şu filmler kullanılabilir:

```txt
Esaretin Bedeli
Yeşil Yol
Babam ve Oğlum
Inception
Interstellar
```

## Dokümantasyon Güncelleme

- Yeni özellik eklendiyse `README.md` ve `ROADMAP.md` kontrol edilmelidir.
- Görev tamamlandıysa `TODO.md` güncellenmelidir.
- Sürüm değişikliği varsa `CHANGELOG.md` güncellenmelidir.
- Öğrenme hedefi tamamlandıysa `LEARNING.md` işaretlenmelidir.
