# Solusi 5.3 - Abstract Class dan Dataclass
from abc import ABC, abstractmethod
from dataclasses import dataclass


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


@dataclass
class HasilBayar:
    metode: str
    total: int
    dibayar: int = 0
    kembalian: int = 0
    biaya: float = 0
    berhasil: bool = True
    pesan: str = "OK"


class MetodePembayaran(ABC):
    nama = "Pembayaran"

    @abstractmethod
    def proses(self, total):
        """Wajib dibuat ulang oleh setiap class turunan."""

    def gagal(self, total, pesan):
        return HasilBayar(self.nama, total, berhasil=False, pesan=pesan)


class Tunai(MetodePembayaran):
    nama = "Tunai"

    def __init__(self, uang_diterima):
        self.uang_diterima = uang_diterima

    def proses(self, total):
        if self.uang_diterima < total:
            return self.gagal(total, f"Uang kurang {rupiah(total - self.uang_diterima)}")
        return HasilBayar(self.nama, total, self.uang_diterima, self.uang_diterima - total)


class QRIS(MetodePembayaran):
    nama = "QRIS"
    MDR = 0.007

    def proses(self, total):
        return HasilBayar(self.nama, total, total, biaya=round(total * self.MDR))


class KartuDebit(MetodePembayaran):
    nama = "Kartu Debit"
    LIMIT = 5_000_000

    def __init__(self, pin):
        self.pin = str(pin)

    def proses(self, total):
        if not (self.pin.isdigit() and len(self.pin) == 6):
            return self.gagal(total, "PIN harus 6 digit angka")
        if total > self.LIMIT:
            return self.gagal(total, f"Melebihi limit {rupiah(self.LIMIT)}")
        return HasilBayar(self.nama, total, total)


try:
    MetodePembayaran()
except TypeError as e:
    print("Tidak bisa membuat object abstrak:", e, "\n")

skenario = [(Tunai(100_000), 87_000), (Tunai(50_000), 87_000), (QRIS(), 87_000),
            (KartuDebit("12ab"), 87_000), (KartuDebit("123456"), 6_500_000), (KartuDebit("123456"), 87_000)]
for metode, total in skenario:                 # polymorphism lewat kontrak ABC
    h = metode.proses(total)
    status = "BERHASIL" if h.berhasil else "GAGAL"
    detail = (f"kembalian {rupiah(h.kembalian)}" if h.kembalian
              else f"biaya toko {rupiah(h.biaya)}" if h.biaya else h.pesan)
    print(f"{h.metode:<12} {rupiah(total):>13}  {status:<8} {detail}")
print("\nrepr dataclass :", QRIS().proses(50_000))
print("Dua hasil sama?", QRIS().proses(50_000) == QRIS().proses(50_000))
