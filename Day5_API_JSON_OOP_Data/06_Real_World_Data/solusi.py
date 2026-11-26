# Solusi 5.6 - Membersihkan Data Penjualan
from pathlib import Path
import pandas as pd

FOLDER = Path(__file__).parent
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)
DATA = FOLDER.parent / "data" / "penjualan_cabang_kotor.csv"
df = pd.read_csv(
    DATA,
    usecols=["id_transaksi", "cabang", "qty", "harga", "total"],
    dtype=str,
)
jumlah_awal = len(df)

df["cabang"] = df["cabang"].str.strip().str.title()
df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
df["harga"] = pd.to_numeric(df["harga"], errors="coerce")
df["total"] = pd.to_numeric(df["total"], errors="coerce")

df = df.drop_duplicates()
df = df.dropna(subset=["qty", "harga", "total"])
df[["qty", "harga", "total"]] = df[["qty", "harga", "total"]].astype(int)

omzet_cabang = df.groupby("cabang")["total"].sum()
print("Jumlah baris awal:", jumlah_awal)
print("Jumlah baris bersih:", len(df))
print("\nTotal penjualan per cabang:")
print(omzet_cabang)

df.to_csv(OUTPUT / "penjualan_bersih.csv", index=False)
print("\nData bersih tersimpan di output/penjualan_bersih.csv")
