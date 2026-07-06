"""TMDb ve OMDb verilerini tek bir temiz film sonucunda birleştirir."""

import config
from omdb_client import get_movie_by_imdb_id
from tmdb_client import (
    get_movie_credits,
    get_movie_details,
    get_movie_external_ids,
    search_movie_by_turkish_name,
)


def _empty_result(movie_name, status):
    """Bulunamayan veya hata alan filmler için standart sonuç üretir."""
    return {
        "input_name": movie_name,
        "original_title": "",
        "year": "",
        "director": "",
        "actors": "",
        "genres": "",
        "overview": "",
        "imdb_id": "",
        "imdb_rating": "",
        "status": status,
    }


def _join_names(items, limit=None):
    """Sözlük listesindeki name alanlarını virgülle birleştirir."""
    names = []

    for item in items:
        name = item.get("name")

        if name and name not in names:
            names.append(name)

    if limit:
        names = names[:limit]

    return ", ".join(names)


def _get_directors(credits):
    """Credits cevabından yönetmen adlarını çıkarır."""
    crew = credits.get("crew", [])
    directors = [person for person in crew if person.get("job") == "Director"]
    return _join_names(directors)


def _get_actors(credits):
    """Credits cevabından ilk üç oyuncuyu çıkarır."""
    cast = credits.get("cast", [])
    return _join_names(cast, limit=3)


def _get_year(release_date):
    """YYYY-AA-GG formatındaki tarihten yılı alır."""
    if not release_date:
        return ""

    return release_date[:4]


def _get_imdb_rating(omdb_data):
    """OMDb cevabındaki IMDb puanını temiz şekilde döndürür."""
    rating = omdb_data.get("imdbRating", "")

    if rating == "N/A":
        return ""

    return rating


def get_movie_info(movie_name):
    """Tek bir film adı için Excel'e yazılacak film bilgisini hazırlar."""
    if not config.has_tmdb_api_key():
        return _empty_result(movie_name, "Eksik API key")

    try:
        search_result = search_movie_by_turkish_name(movie_name)

        if search_result is None:
            return _empty_result(movie_name, "Film bulunamadı")

        tmdb_movie_id = search_result["id"]
        details = get_movie_details(tmdb_movie_id)
        credits = get_movie_credits(tmdb_movie_id)
        external_ids = get_movie_external_ids(tmdb_movie_id)
    except RuntimeError:
        return _empty_result(movie_name, "API hatası")

    imdb_id = external_ids.get("imdb_id", "")
    omdb_data = get_movie_by_imdb_id(imdb_id)

    genres = [genre.get("name", "") for genre in details.get("genres", [])]
    genres = [genre for genre in genres if genre]

    status = "Bulundu"

    if imdb_id and config.has_omdb_api_key() and not omdb_data:
        status = "OMDb bilgisi alınamadı"

    return {
        "input_name": movie_name,
        "original_title": details.get("original_title") or details.get("title", ""),
        "year": _get_year(details.get("release_date", "")),
        "director": _get_directors(credits),
        "actors": _get_actors(credits),
        "genres": ", ".join(genres),
        "overview": details.get("overview", ""),
        "imdb_id": imdb_id,
        "imdb_rating": _get_imdb_rating(omdb_data),
        "status": status,
    }
