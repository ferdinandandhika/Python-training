# TokoKu Day 4 OOP - versi satu file untuk latihan
import csv
from pathlib import Path

FOLDER = Path(__file__).parent
PAJAK = 0.11


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


# TODO 1: class Produk, Minuman (ukuran S/M/L, harga_satuan), Makanan  -> lihat 4.1 dan 4.3
# TODO 2: class ItemKeranjang (produk, qty, subtotal)
# TODO 3: class Keranjang dengan tambah(), subtotal(), __len__, __iter__, __contains__, __bool__


class Toko:
    def __init__(self, nama, produk_list):
        self.nama = nama
        self.katalog = {p.kode: p for p in produk_list}

    @classmethod
    def dari_csv(cls, path):
        pass  # TODO 4: baca menu.csv, buat Minuman atau Makanan sesuai kolom jenis

    @staticmethod
    def persen_diskon(subtotal, member=False):
        pass  # TODO 5: aturan diskon TokoKu

    def checkout(self, keranjang, member=False):
        pass  # TODO 6: hitung subtotal, diskon, pajak, total; simpan ke transaksi.csv


# TODO 7: program utama
# toko = Toko.dari_csv(FOLDER / "menu.csv")
# k = Keranjang(); k.tambah(toko.katalog["K01"], 2) ...
