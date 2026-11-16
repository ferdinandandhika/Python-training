"""Ambil kurs IDR ke USD dari API, dengan cadangan offline."""
import json
from pathlib import Path

import requests

URL = "https://open.er-api.com/v6/latest/IDR"
CADANGAN = Path(__file__).resolve().parents[2] / "01_API_dan_JSON" / "kurs_cadangan.json"


def ambil_kurs_usd(url=URL, cadangan=CADANGAN, timeout=8):
    """Kembalikan (kurs, sumber)."""
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return r.json()["rates"]["USD"], "API online"
    except (requests.RequestException, KeyError, ValueError):
        with open(cadangan, encoding="utf-8") as f:
            return json.load(f)["rates"]["USD"], "data cadangan"
