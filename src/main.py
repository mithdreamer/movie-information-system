"""Film Bilgi Sistemi ana çalışma dosyası."""

from pathlib import Path

from excel_handler import load_movie_names, write_movie_results
from movie_service import get_movie_info


PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "data" / "film_bilgi_sablonu.xlsx"
OUTPUT_FILE = PROJECT_DIR / "data" / "film_bilgi_sonuc.xlsx"


def main():
    """Excel'den film adlarını okur, API'den bilgileri alır ve sonucu yazar."""
    print("Film Bilgi Sistemi başlatıldı.")
    print(f"Giriş dosyası: {INPUT_FILE}")

    try:
        movie_names = load_movie_names(INPUT_FILE)
    except FileNotFoundError:
        print("Excel şablonu bulunamadı.")
        print("Beklenen dosya: data/film_bilgi_sablonu.xlsx")
        return

    if not movie_names:
        print("Excel dosyasında film adı bulunamadı.")
        print("Lütfen A2 hücresinden başlayarak film adlarını yazın.")
        return

    results = []

    for index, movie_name in enumerate(movie_names, start=1):
        print(f"{index}. film sorgulanıyor: {movie_name}")
        result = get_movie_info(movie_name)
        results.append(result)
        print(f"Durum: {result['status']}")

    try:
        write_movie_results(INPUT_FILE, OUTPUT_FILE, results)
    except PermissionError:
        print("Sonuç dosyası kaydedilemedi.")
        print("Excel dosyası açıksa kapatıp tekrar deneyin.")
        return

    print("İşlem tamamlandı.")
    print(f"Sonuç dosyası: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
