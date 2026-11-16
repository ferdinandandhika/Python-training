# Solusi 5.1 - Kurs dari API
import json
import os
from pathlib import Path

import requests

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

URL = "https://open.er-api.com/v6/latest/IDR"
CADANGAN = Path(__file__).parent / "kurs_cadangan.json"
MENU = {"Kopi Susu Aren": 25000, "Matcha Latte": 28000, "Cheesecake": 32000}

key = os.getenv("TOKOKU_API_KEY")
print("API key:", key[:4] + "*" * max(len(key) - 4, 0) if key else "belum diatur (tidak wajib untuk API ini)")


def ambil_kurs():
    try:
        r = requests.get(URL, timeout=10)
        r.raise_for_status()
        data = r.json()
        if data.get("result") != "success":
            raise ValueError("respons API tidak sukses")
        print("Sumber kurs: API online,", data.get("time_last_update_utc"))
        return data["rates"]
    except (requests.RequestException, ValueError) as e:
        print(f"API gagal ({type(e).__name__}), memakai data cadangan.")
        with open(CADANGAN, encoding="utf-8") as f:
            return json.load(f)["rates"]


rates = ambil_kurs()
print(f"\n{'Menu':<16}{'IDR':>10}{'USD':>8}{'SGD':>8}{'JPY':>8}")
for nama, harga in MENU.items():
    print(f"{nama:<16}{harga:>10,}{harga * rates['USD']:>8.2f}{harga * rates['SGD']:>8.2f}{harga * rates['JPY']:>8.0f}")
