"""Class Toko final: katalog, checkout dengan pembayaran, laporan Pandas, dashboard."""
import csv
import time
from datetime import datetime
from functools import wraps
from pathlib import Path

from .produk import Makanan, Minuman, Produk


def catat_waktu(fungsi):
    """Decorator dari Latihan 5.2, dipakai pada method."""
    @wraps(fungsi)
    def pembungkus(*args, **kwargs):
        mulai = time.perf_counter()
        hasil = fungsi(*args, **kwargs)
        print(f"  [{fungsi.__name__} {time.perf_counter() - mulai:.2f} detik]")
        return hasil
    return pembungkus


class Toko:
    PAJAK = 0.11
    KOLOM = ["id_transaksi", "waktu", "metode", "kode", "nama", "jenis", "qty", "harga", "subtotal"]

    def __init__(self, nama, produk_list, file_transaksi=None):
        self.nama = nama
        self.katalog = {p.kode: p for p in produk_list}
        self.file_transaksi = Path(file_transaksi) if file_transaksi else None
        self._nomor = 0

    @classmethod
    def dari_csv(cls, path_menu, nama="TokoKu", file_transaksi=None):
        kelas = {"minuman": Minuman, "makanan": Makanan}
        with open(path_menu, encoding="utf-8") as f:
            produk = [kelas.get(r["jenis"], Produk)(r["kode"], r["nama"], int(r["harga"]))
                      for r in csv.DictReader(f)]
        return cls(nama, produk, file_transaksi)

    def cari(self, kode):
        kode = kode.upper()
        if kode not in self.katalog:
            raise KeyError(f"Kode {kode} tidak ada di menu")
        return self.katalog[kode]

    @staticmethod
    def persen_diskon(subtotal, member=False):
        persen = 0.15 if subtotal >= 200_000 else 0.10 if subtotal >= 100_000 else 0.0
        return persen + (0.05 if member else 0)

    def hitung(self, keranjang, member=False):
        subtotal = keranjang.subtotal()
        diskon = round(subtotal * self.persen_diskon(subtotal, member))
        pajak = round((subtotal - diskon) * self.PAJAK)
        return {"subtotal": subtotal, "diskon": diskon, "pajak": pajak, "total": subtotal - diskon + pajak}

    def checkout(self, keranjang, metode, member=False):
        """metode adalah object turunan MetodePembayaran (polymorphism)."""
        if not keranjang:
            raise ValueError("Keranjang kosong")
        rincian = self.hitung(keranjang, member)
        hasil = metode.proses(rincian["total"])
        if hasil.berhasil:
            self._simpan(keranjang, hasil.metode)
        return rincian, hasil

    def _simpan(self, keranjang, metode):
        if not self.file_transaksi:
            return
        self._nomor += 1
        baru = not self.file_transaksi.exists()
        sekarang = datetime.now()
        id_trx = f"TRX{sekarang:%Y%m%d%H%M%S}-{self._nomor}"
        with open(self.file_transaksi, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=self.KOLOM)
            if baru:
                w.writeheader()
            for item in keranjang:
                p = item.produk
                w.writerow({"id_transaksi": id_trx, "waktu": f"{sekarang:%Y-%m-%d %H:%M:%S}", "metode": metode,
                            "kode": p.kode, "nama": p.nama, "jenis": p.jenis, "qty": item.qty,
                            "harga": p.harga_satuan(), "subtotal": item.subtotal()})

    def data_transaksi(self):
        import pandas as pd
        if not self.file_transaksi or not self.file_transaksi.exists():
            return None
        return pd.read_csv(self.file_transaksi, parse_dates=["waktu"])

    @catat_waktu
    def laporan(self):
        df = self.data_transaksi()
        if df is None or df.empty:
            return {"jumlah": 0, "omzet": 0}
        return {
            "jumlah": int(df["id_transaksi"].nunique()),
            "omzet": int(df["subtotal"].sum()),
            "menu_terlaris": df.groupby("nama")["qty"].sum().idxmax(),
            "per_jenis": df.groupby("jenis")["subtotal"].sum().to_dict(),
            "per_metode": df.groupby("metode")["id_transaksi"].nunique().to_dict(),
            "jam_tersibuk": int(df["waktu"].dt.hour.value_counts().idxmax()),
        }

    @catat_waktu
    def dashboard(self, folder):
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        df = self.data_transaksi()
        if df is None or df.empty:
            return None
        folder = Path(folder)
        folder.mkdir(exist_ok=True)
        harian = df.groupby(df["waktu"].dt.date)["subtotal"].sum() / 1e6
        jenis = df.groupby("jenis")["subtotal"].sum()
        menu = df.groupby("nama")["qty"].sum().sort_values()
        metode = df.groupby("metode")["id_transaksi"].nunique()
        fig, ax = plt.subplots(2, 2, figsize=(12, 8))
        ax[0, 0].plot(list(harian.index), harian.values, color="#1F6F78")
        ax[0, 0].set_title("Omzet harian (juta)")
        ax[0, 0].tick_params(axis="x", rotation=45)
        ax[0, 1].pie(jenis.values, labels=list(jenis.index), autopct="%1.0f%%", colors=["#B26B00", "#1F6F78"])
        ax[0, 1].set_title("Omzet per jenis produk")
        ax[1, 0].barh(list(menu.index), menu.values, color="#1F6F78")
        ax[1, 0].set_title("Qty terjual per menu")
        ax[1, 1].bar(list(metode.index), metode.values, color="#1F3864")
        ax[1, 1].set_title("Transaksi per metode bayar")
        fig.suptitle(f"Dashboard {self.nama}", fontsize=15, fontweight="bold")
        plt.tight_layout()
        path = folder / f"dashboard_{datetime.now():%Y%m%d_%H%M%S}.png"
        plt.savefig(path, dpi=120)
        plt.close()
        return path
