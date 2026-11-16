# Solusi 5.5 - Visualisasi
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FOLDER = Path(__file__).parent
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)
df = pd.read_csv(FOLDER.parent / "data" / "penjualan_tokoku.csv", parse_dates=["tanggal"])
df["bulan"] = df["tanggal"].dt.strftime("%Y-%m")
WARNA, PALET = "#1F6F78", ["#1F3864", "#1F6F78", "#B26B00"]

bulanan = df.groupby("bulan")["total"].sum() / 1e6
cabang = df.groupby("cabang")["total"].sum().sort_values(ascending=False) / 1e6
kategori = df.groupby("kategori")["total"].sum()
top = df.groupby("menu")["qty"].sum().nlargest(5).sort_values()


def simpan(nama):
    plt.tight_layout()
    plt.savefig(OUTPUT / nama, dpi=120)
    plt.close()


plt.figure(figsize=(8, 4)); plt.plot(list(bulanan.index), bulanan.values, marker="o", color=WARNA)
plt.title("Omzet bulanan TokoKu"); plt.ylabel("Juta Rupiah"); simpan("1_omzet_bulanan.png")
plt.figure(figsize=(8, 4)); plt.bar(list(cabang.index), cabang.values, color=WARNA)
plt.title("Omzet per cabang"); plt.ylabel("Juta Rupiah"); simpan("2_omzet_cabang.png")
plt.figure(figsize=(5, 5)); plt.pie(kategori.values, labels=list(kategori.index), autopct="%1.0f%%", colors=PALET)
plt.title("Komposisi omzet per kategori"); simpan("3_kategori.png")
plt.figure(figsize=(8, 4)); plt.barh(list(top.index), top.values, color=WARNA)
plt.title("5 menu terlaris"); simpan("4_top_menu.png")

fig, ax = plt.subplots(2, 2, figsize=(12, 8))
ax[0, 0].plot(list(bulanan.index), bulanan.values, marker="o", color=WARNA); ax[0, 0].set_title("Omzet bulanan (juta)")
ax[0, 1].bar(list(cabang.index), cabang.values, color=WARNA); ax[0, 1].set_title("Omzet per cabang (juta)")
ax[1, 0].pie(kategori.values, labels=list(kategori.index), autopct="%1.0f%%", colors=PALET); ax[1, 0].set_title("Kategori")
ax[1, 1].barh(list(top.index), top.values, color=WARNA); ax[1, 1].set_title("Top 5 menu")
fig.suptitle("Dashboard Penjualan TokoKu Jan - Jun 2026", fontsize=14, fontweight="bold")
simpan("5_dashboard.png")
print("5 grafik tersimpan di folder output/")
