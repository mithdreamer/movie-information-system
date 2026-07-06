"""TMDb API ile film arama ve detay çekme işlemleri."""

import requests

import config


BASE_URL = "https://api.themoviedb.org/3"


def _get(endpoint, params=None):
    """TMDb API'ye GET isteği gönderir ve JSON cevabını döndürür."""
    if not config.has_tmdb_api_key():
        raise RuntimeError("Eksik API key")

    request_params = dict(params or {})
    request_params["api_key"] = config.TMDB_API_KEY
    request_params.setdefault("language", "tr-TR")

    try:
        response = requests.get(
            BASE_URL + endpoint,
            params=request_params,
            timeout=15,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise RuntimeError(f"TMDb API hatası: {error}") from error

    return response.json()


def search_movie_by_turkish_name(movie_name):
    """Türkçe film adına göre TMDb üzerinde arama yapar."""
    data = _get(
        "/search/movie",
        {
            "query": movie_name,
            "include_adult": "false",
            "region": "TR",
        },
    )

    results = data.get("results", [])

    if not results:
        return None

    return results[0]


def get_movie_details(tmdb_movie_id):
    """TMDb film ID'si ile detay bilgilerini alır."""
    return _get(f"/movie/{tmdb_movie_id}")


def get_movie_credits(tmdb_movie_id):
    """TMDb film ID'si ile yönetmen ve oyuncu bilgilerini alır."""
    return _get(f"/movie/{tmdb_movie_id}/credits")


def get_movie_external_ids(tmdb_movie_id):
    """TMDb film ID'si ile IMDb ID gibi dış kimlikleri alır."""
    return _get(f"/movie/{tmdb_movie_id}/external_ids")
