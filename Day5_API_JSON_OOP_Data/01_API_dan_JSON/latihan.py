# Latihan 5.1 - Kurs dari API
import json
import os
from pathlib import Path

import requests

URL = "https://open.er-api.com/v6/latest/IDR"
CADANGAN = Path(__file__).parent / "kurs_cadangan.json"
MENU = {"Kopi Susu Aren": 25000, "Matcha Latte": 28000, "Cheesecake": 32000}

# TODO 1: from dotenv import load_dotenv; load_dotenv(); baca os.getenv("TOKOKU_API_KEY"),
#         tampilkan 4 karakter awal saja
# TODO 2: requests.get(URL, timeout=10) di dalam try/except requests.RequestException
# TODO 3: bila gagal, baca CADANGAN dengan json.load
# TODO 4: ambil rates USD, SGD, JPY
# TODO 5: tampilkan tabel harga menu dalam IDR, USD, SGD, JPY
