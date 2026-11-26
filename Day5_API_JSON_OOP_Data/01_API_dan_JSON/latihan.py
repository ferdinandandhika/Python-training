# Latihan 5.1 - Kurs dari API
import json
from pathlib import Path

import requests

URL = "https://open.er-api.com/v6/latest/IDR"
CADANGAN = Path(__file__).parent / "kurs_cadangan.json"
jumlah_idr = int(input("Masukkan jumlah dalam rupiah: "))

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    # TODO 1: ambil kurs USD dari data["rates"].
    kurs_usd = 0
    sumber = "API online"
except (requests.RequestException, ValueError, KeyError):
    print("API tidak bisa diakses. Menggunakan data cadangan.")
    with open(CADANGAN, encoding="utf-8") as file:
        data = json.load(file)
    # TODO 2: ambil kurs USD dari data cadangan.
    kurs_usd = 0
    sumber = "data cadangan"

# TODO 3: hitung jumlah USD dan tampilkan sumber kurs, jumlah IDR, dan jumlah USD.
