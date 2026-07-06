"""Proje ayarları ve API key okuma işlemleri."""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv(_env_path):
        """python-dotenv kurulu değilse programın kapanmasını engeller."""
        return False


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

TMDB_API_KEY = os.getenv("TMDB_API_KEY", "").strip()
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "").strip()


def has_tmdb_api_key():
    """TMDb API key girilmiş mi kontrol eder."""
    return bool(TMDB_API_KEY)


def has_omdb_api_key():
    """OMDb API key girilmiş mi kontrol eder."""
    return bool(OMDB_API_KEY)
