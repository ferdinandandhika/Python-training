# Solusi 4.5 - File Lab
import csv
import json
from pathlib import Path

FOLDER = Path(__file__).parent
SUMBER = FOLDER / "data" / "penjualan_harian.txt"
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)

rekap = {}
try:
    with open(SUMBER, encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue
            tanggal, menu, qty, harga = baris.split(";")
            data = rekap.setdefault(menu, {"qty": 0, "total": 0})
            data["qty"] += int(qty)
            data["total"] += int(qty) * int(harga)
except FileNotFoundError:
    print(f"File {SUMBER} tidak ditemukan.")
    raise SystemExit(1)

with open(OUTPUT / "rekap_menu.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Menu", "Qty", "Total"])
    for menu, data in sorted(rekap.items(), key=lambda x: x[1]["total"], reverse=True):
        writer.writerow([menu, data["qty"], data["total"]])

ringkasan = {
    "total_omzet": sum(d["total"] for d in rekap.values()),
    "total_cup": sum(d["qty"] for d in rekap.values()),
    "menu_terlaris": max(rekap, key=lambda m: rekap[m]["qty"]),
}
with open(OUTPUT / "ringkasan.json", "w", encoding="utf-8") as f:
    json.dump(ringkasan, f, indent=2, ensure_ascii=False)
for menu, data in rekap.items():
    print(f"{menu:<16} {data['qty']:>3}  Rp {data['total']:>9,}")
print(json.dumps(ringkasan, indent=2))
