# Latihan 5.5 - Visualisasi
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

FOLDER = Path(__file__).parent
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)
df = pd.read_csv(FOLDER.parent / "data" / "penjualan_tokoku.csv", parse_dates=["tanggal"])
df["bulan"] = df["tanggal"].dt.strftime("%Y-%m")

# Contoh grafik 1:
# data = df.groupby("bulan")["total"].sum() / 1_000_000
# plt.figure(figsize=(8, 4)); plt.plot(list(data.index), data.values, marker="o")
# plt.title("Omzet bulanan"); plt.ylabel("Juta Rupiah"); plt.savefig(OUTPUT / "1.png"); plt.close()
# TODO 2: bar omzet per cabang  TODO 3: pie kategori  TODO 4: barh top 5 menu  BONUS: dashboard 2x2
