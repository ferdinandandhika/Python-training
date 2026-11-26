# Latihan 5.5 - Grafik Penjualan Sederhana
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

# TODO: buat grafik batang dari omzet_cabang.
# Tambahkan judul dan label sumbu, lalu simpan sebagai output/omzet_cabang.png.
