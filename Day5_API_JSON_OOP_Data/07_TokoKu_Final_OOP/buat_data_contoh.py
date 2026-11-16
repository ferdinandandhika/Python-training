"""Isi transaksi.csv dengan 300 transaksi contoh agar laporan dan dashboard langsung bisa dicoba."""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

FOLDER = Path(__file__).parent
with open(FOLDER / "menu.csv", encoding="utf-8") as f:
    menu = list(csv.DictReader(f))
TAMBAHAN = {"S": 0, "M": 3000, "L": 6000}
KOLOM = ["id_transaksi", "waktu", "metode", "kode", "nama", "jenis", "qty", "harga", "subtotal"]
random.seed(7)
with open(FOLDER / "transaksi.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=KOLOM)
    w.writeheader()
    for i in range(1, 301):
        waktu = datetime(2026, 6, 1, 8) + timedelta(days=random.randint(0, 29), minutes=random.randint(0, 780))
        metode = random.choices(["Tunai", "QRIS", "Kartu Debit"], [35, 50, 15])[0]
        for m in random.sample(menu, random.randint(1, 3)):
            harga, kode = int(m["harga"]), m["kode"]
            if m["jenis"] == "minuman":
                ukuran = random.choice("SML")
                harga += TAMBAHAN[ukuran]
                kode = f"{kode}-{ukuran}"
            qty = random.randint(1, 3)
            w.writerow({"id_transaksi": f"TRX{i:05}", "waktu": f"{waktu:%Y-%m-%d %H:%M:%S}", "metode": metode,
                        "kode": kode, "nama": m["nama"], "jenis": m["jenis"].title(), "qty": qty,
                        "harga": harga, "subtotal": qty * harga})
print("transaksi.csv berisi 300 transaksi contoh.")
