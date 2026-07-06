"""OMDb API ile IMDb ID üzerinden ek film bilgisi çeker."""

import requests

import config


BASE_URL = "https://www.omdbapi.com/"


def get_movie_by_imdb_id(imdb_id):
    """IMDb ID ile OMDb'den film bilgisini alır."""
    if not config.has_omdb_api_key() or not imdb_id:
        return {}

    params = {
        "apikey": config.OMDB_API_KEY,
        "i": imdb_id,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=15)
        response.raise_for_status()
    except requests.RequestException:
        return {}

    data = response.json()

    if data.get("Response") == "False":
        return {}

    return data
