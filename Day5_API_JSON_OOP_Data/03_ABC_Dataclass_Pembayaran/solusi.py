# Solusi 5.3 - ABC dan Dataclass
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
        if self.uang_diterima >= total:
            return HasilBayar("Tunai", total, True, "Pembayaran tunai berhasil.")
        return HasilBayar("Tunai", total, False, "Uang yang diterima masih kurang.")


class QRIS(MetodePembayaran):
    def proses(self, total):
        pesan = "QRIS berhasil (simulasi; belum terhubung ke pembayaran nyata)."
        return HasilBayar("QRIS", total, True, pesan)


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
