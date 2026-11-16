"""Class Toko (Day 4): menu dari CSV, checkout, simpan transaksi ke CSV."""
import csv
from datetime import datetime
from pathlib import Path

from .produk import Makanan, Minuman, Produk


class Toko:
    PAJAK = 0.11
    KOLOM = ["id_transaksi", "waktu", "kode", "nama", "jenis", "qty", "harga", "subtotal"]

    def __init__(self, nama, produk_list, file_transaksi=None):
        self.nama = nama
        self.katalog = {p.kode: p for p in produk_list}
        self.file_transaksi = Path(file_transaksi) if file_transaksi else None

    @classmethod
    def dari_csv(cls, path_menu, nama="TokoKu", file_transaksi=None):
        """Alternative constructor: membuat Toko langsung dari file menu."""
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

    def checkout(self, keranjang, member=False):
        if not keranjang:
            raise ValueError("Keranjang kosong")
        rincian = self.hitung(keranjang, member)
        self._simpan(keranjang)
        return rincian

    def _simpan(self, keranjang):
        if not self.file_transaksi:
            return
        baru = not self.file_transaksi.exists()
        sekarang = datetime.now()
        id_trx = sekarang.strftime("TRX%Y%m%d%H%M%S%f")
        with open(self.file_transaksi, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=self.KOLOM)
            if baru:
                w.writeheader()
            for item in keranjang:
                p = item.produk
                w.writerow({"id_transaksi": id_trx, "waktu": f"{sekarang:%Y-%m-%d %H:%M:%S}", "kode": p.kode,
                            "nama": p.nama, "jenis": p.jenis, "qty": item.qty,
                            "harga": p.harga_satuan(), "subtotal": item.subtotal()})

    def laporan(self):
        if not self.file_transaksi or not self.file_transaksi.exists():
            return {"jumlah": 0, "omzet": 0}
        with open(self.file_transaksi, encoding="utf-8") as f:
            data = list(csv.DictReader(f))
        return {"jumlah": len({d["id_transaksi"] for d in data}), "omzet": sum(int(d["subtotal"]) for d in data)}
