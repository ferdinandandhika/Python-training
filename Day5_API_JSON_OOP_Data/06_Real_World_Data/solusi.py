# Solusi 5.6 - Real World Data
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FOLDER = Path(__file__).parent
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)
df = pd.read_csv(FOLDER.parent / "data" / "penjualan_cabang_kotor.csv", dtype=str,
                 keep_default_na=False, na_values=[""])

print("=== INSPEKSI ===")
print("Ukuran       :", df.shape)
print("Duplikat     :", df.duplicated().sum())
print(df.isna().sum()[df.isna().sum() > 0].to_string())
print("Variasi cabang:", sorted(df["cabang"].unique()))

print("\n=== PEMBERSIHAN ===")
df["cabang"] = df["cabang"].str.strip().str.title()
for kolom in ["qty", "harga", "total", "rating"]:
    df[kolom] = pd.to_numeric(df[kolom], errors="coerce")
df["tanggal"] = pd.to_datetime(df["tanggal"], format="mixed", dayfirst=True)
df["qty"] = df["qty"].fillna(df["total"] / df["harga"]).astype(int)
df["total"] = df["total"].fillna(df["qty"] * df["harga"])
df["rating"] = df["rating"].fillna(df["rating"].median())
sebelum = len(df)
df = df.drop_duplicates()
print(f"Duplikat dihapus : {sebelum - len(df)}")
print(f"Nilai kosong sisa: {int(df.isna().sum().sum())}")

cabang = df.groupby("cabang")["total"].sum().sort_values(ascending=False)
bulanan = df.groupby(df["tanggal"].dt.strftime("%Y-%m"))["total"].sum() / 1e6
print("\n=== ANALISIS ===")
print(cabang.apply(lambda x: f"Rp {x:,.0f}".replace(",", ".")).to_string())
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].bar(list(cabang.index), cabang.values / 1e6, color="#1F6F78"); ax[0].set_title("Omzet per cabang (juta)")
ax[1].plot(list(bulanan.index), bulanan.values, marker="o", color="#1F3864"); ax[1].set_title("Omzet bulanan (juta)")
plt.tight_layout()
plt.savefig(OUTPUT / "analisis_data_bersih.png", dpi=120)
df.to_csv(OUTPUT / "penjualan_bersih.csv", index=False)
print("\nTersimpan: output/penjualan_bersih.csv dan output/analisis_data_bersih.png")
