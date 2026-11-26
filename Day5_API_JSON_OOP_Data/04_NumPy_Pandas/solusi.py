# Solusi 5.4 - NumPy dan Pandas Dasar
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).parent.parent / "data" / "penjualan_tokoku.csv"

print("=== NumPy ===")
qty = np.array([2, 1, 3])
harga = np.array([25000, 18000, 32000])
total_barang = qty * harga
print("Total setiap barang:", total_barang)
print("Jumlah seluruhnya:", total_barang.sum())

print("\n=== Pandas ===")
df = pd.read_csv(DATA)
print(df.head())
print("Ukuran data:", df.shape)
print("Total penjualan:", df["total"].sum())

omzet_cabang = df.groupby("cabang")["total"].sum()
print("\nTotal penjualan per cabang:")
print(omzet_cabang)
