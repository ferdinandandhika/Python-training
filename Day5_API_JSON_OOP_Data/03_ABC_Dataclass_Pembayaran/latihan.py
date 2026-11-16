# Latihan 5.3 - Abstract Class dan Dataclass
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class HasilBayar:
    # TODO 1: metode: str, total: int, dibayar: int = 0, kembalian: int = 0,
    #         biaya: float = 0, berhasil: bool = True, pesan: str = "OK"
    pass


class MetodePembayaran(ABC):
    nama = "Pembayaran"

    @abstractmethod
    def proses(self, total):
        """Wajib dibuat ulang oleh setiap class turunan."""


class Tunai(MetodePembayaran):
    nama = "Tunai"

    def __init__(self, uang_diterima):
        self.uang_diterima = uang_diterima

    def proses(self, total):
        pass  # TODO 2: gagal bila uang kurang, berhasil dengan kembalian bila cukup


class QRIS(MetodePembayaran):
    pass  # TODO 3: biaya 0.7% dari total, berhasil, dibayar = total


class KartuDebit(MetodePembayaran):
    pass  # TODO 4: __init__(pin); gagal bila pin bukan 6 digit atau total > 5.000.000

# TODO 5: coba MetodePembayaran() di dalam try/except TypeError
# TODO 6: jalankan 6 skenario dan print hasilnya
