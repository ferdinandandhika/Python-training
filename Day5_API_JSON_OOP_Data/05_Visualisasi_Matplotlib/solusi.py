# Solusi 5.5 - Grafik Penjualan Sederhana
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt

FOLDER = Path(__file__).parent
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)
DATA = FOLDER.parent / "data" / "penjualan_tokoku.csv"
df = pd.read_csv(DATA)
omzet_cabang = df.groupby("cabang")["total"].sum()

plt.bar(omzet_cabang.index, omzet_cabang.values, color="#1F6F78")
plt.title("Total Penjualan per Cabang")
plt.xlabel("Cabang")
plt.ylabel("Total Penjualan (Rp)")
plt.tight_layout()
plt.savefig(OUTPUT / "omzet_cabang.png")
plt.close()
print("Grafik tersimpan di output/omzet_cabang.png")
