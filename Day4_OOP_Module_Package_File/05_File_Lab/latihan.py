# Latihan 4.5 - File Lab
import csv
import json
from pathlib import Path

FOLDER = Path(__file__).parent
SUMBER = FOLDER / "data" / "penjualan_harian.txt"
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)
rekap = {}  # {menu: {"qty": .., "total": ..}}

# TODO 1: buka SUMBER dengan with open(..., encoding="utf-8")
# TODO 2: lewati baris kosong dan baris yang diawali "#"
# TODO 3: pecah baris dengan .split(";"), ubah qty dan harga ke int
# TODO 4: tambahkan ke dictionary rekap
# TODO 5: tulis rekap ke OUTPUT / "rekap_menu.csv" memakai csv.writer
# TODO 6: tulis ringkasan (total_omzet, menu_terlaris) ke OUTPUT / "ringkasan.json"
