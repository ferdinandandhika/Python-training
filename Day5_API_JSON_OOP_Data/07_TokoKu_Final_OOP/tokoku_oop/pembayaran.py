"""Metode pembayaran: abstract base class + dataclass."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class HasilBayar:
    metode: str
    total: int
    dibayar: int = 0
    kembalian: int = 0
    berhasil: bool = True
    pesan: str = "OK"


class MetodePembayaran(ABC):
    nama = "Pembayaran"

    @abstractmethod
    def proses(self, total):
        ...

    def gagal(self, total, pesan):
        return HasilBayar(self.nama, total, berhasil=False, pesan=pesan)


class Tunai(MetodePembayaran):
    nama = "Tunai"

    def __init__(self, uang_diterima):
        self.uang_diterima = uang_diterima

    def proses(self, total):
        if self.uang_diterima < total:
            return self.gagal(total, "Uang kurang")
        return HasilBayar(self.nama, total, self.uang_diterima, self.uang_diterima - total)


class QRIS(MetodePembayaran):
    nama = "QRIS"

    def proses(self, total):
        return HasilBayar(self.nama, total, total)


class KartuDebit(MetodePembayaran):
    nama = "Kartu Debit"
    LIMIT = 5_000_000

    def __init__(self, pin):
        self.pin = str(pin)

    def proses(self, total):
        if not (self.pin.isdigit() and len(self.pin) == 6):
            return self.gagal(total, "PIN harus 6 digit angka")
        if total > self.LIMIT:
            return self.gagal(total, "Melebihi limit Rp 5.000.000")
        return HasilBayar(self.nama, total, total)
