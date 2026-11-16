# Latihan 5.4 - NumPy dan Pandas
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).parent.parent / "data" / "penjualan_tokoku.csv"
qty = np.array([2, 5, 1, 3, 4])
harga = np.array([25000, 22000, 28000, 18000, 32000])
# TODO A1-A3: total = qty * harga; sum, mean, max, std; total[total > 80000]

df = pd.read_csv(DATA, parse_dates=["tanggal"])
print(df.head())
# TODO B1: df.shape                     TODO B2: df["total"].sum()
# TODO B3: groupby cabang idxmax        TODO B4: groupby menu, sum qty
# TODO B5: groupby channel mean         TODO B6: df["tanggal"].dt.to_period("M")
# TODO B7: value_counts(normalize=True) TODO B8: simpan ke output/omzet_cabang.csv
