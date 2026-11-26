# Latihan 5.3 - ABC dan Dataclass
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class HasilBayar:
    metode: str
    total: int
    berhasil: bool
    pesan: str


class MetodePembayaran(ABC):
    @abstractmethod
    def proses(self, total):
        pass


class Tunai(MetodePembayaran):
    def __init__(self, uang_diterima):
        self.uang_diterima = uang_diterima

    def proses(self, total):
        # TODO 1: jika uang cukup, kembalikan hasil berhasil.
        # Jika kurang, kembalikan hasil gagal dengan pesan yang sesuai.
        pass


class QRIS(MetodePembayaran):
    def proses(self, total):
        # TODO 2: kembalikan hasil berhasil dengan pesan bahwa QRIS hanya simulasi.
        pass


def main():
    total = int(input("Masukkan total belanja: Rp"))
    print("1. Tunai")
    print("2. QRIS (simulasi)")
    pilihan = input("Pilih metode pembayaran: ").strip()

    if pilihan == "1":
        uang_diterima = int(input("Masukkan uang yang diterima: Rp"))
        metode = Tunai(uang_diterima)
    elif pilihan == "2":
        metode = QRIS()
    else:
        print("Pilihan tidak tersedia.")
        return

    hasil = metode.proses(total)
    print("Status:", "Berhasil" if hasil.berhasil else "Gagal")
    print(hasil.pesan)


main()
