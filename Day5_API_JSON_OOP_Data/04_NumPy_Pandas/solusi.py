# Solusi 5.4 - NumPy dan Pandas
from pathlib import Path
import numpy as np
import pandas as pd

FOLDER = Path(__file__).parent
DATA = FOLDER.parent / "data" / "penjualan_tokoku.csv"
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)

print("=== NumPy ===")
qty = np.array([2, 5, 1, 3, 4])
harga = np.array([25000, 22000, 28000, 18000, 32000])
total = qty * harga
print("Total per item :", total)
print(f"Sum {total.sum():,} | Mean {total.mean():,.0f} | Max {total.max():,} | Std {total.std():,.0f}")
print("Total > 80.000 :", total[total > 80_000])

print("\n=== Pandas ===")
df = pd.read_csv(DATA, parse_dates=["tanggal"])
print("1. Ukuran data         :", df.shape)
print(f"2. Total omzet         : Rp {df['total'].sum():,}")
omzet_cabang = df.groupby("cabang")["total"].sum().sort_values(ascending=False)
print("3. Cabang tertinggi    :", omzet_cabang.idxmax())
print("4. Menu terlaris (qty) :", df.groupby("menu")["qty"].sum().idxmax())
print("5. Rata-rata per channel:")
print(df.groupby("channel")["total"].mean().round(0).to_string())
df["bulan"] = df["tanggal"].dt.to_period("M")
print("6. Bulan tertinggi     :", df.groupby("bulan")["total"].sum().idxmax())
print(f"7. Persen member       : {df['status_member'].value_counts(normalize=True)['Member']:.1%}")
omzet_cabang.to_csv(OUTPUT / "omzet_cabang.csv", header=["omzet"])
print("8. Tersimpan           : output/omzet_cabang.csv")
