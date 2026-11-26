# Solusi 5.1 - Kurs dari API
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
    kurs_usd = data["rates"]["USD"]
    sumber = "API online"
except (requests.RequestException, ValueError, KeyError):
    print("API tidak bisa diakses. Menggunakan data cadangan.")
    with open(CADANGAN, encoding="utf-8") as file:
        data = json.load(file)
    kurs_usd = data["rates"]["USD"]
    sumber = "data cadangan"

jumlah_usd = jumlah_idr * kurs_usd
print("Sumber kurs:", sumber)
print(f"Jumlah rupiah: Rp{jumlah_idr:,}")
print(f"Jumlah USD: ${jumlah_usd:.2f}")
