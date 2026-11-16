# Latihan 5.2 - Decorator
import time
from functools import wraps


def catat_waktu(fungsi):
    @wraps(fungsi)
    def pembungkus(*args, **kwargs):
        mulai = time.perf_counter()
        hasil = fungsi(*args, **kwargs)
        print(f"[waktu] {fungsi.__name__} selesai dalam {time.perf_counter() - mulai:.3f} detik")
        return hasil
    return pembungkus


def log_aktivitas(fungsi):
    pass  # TODO 1: tulis nama fungsi dan args ke aktivitas.log (mode "a")


def hanya_admin(fungsi):
    pass  # TODO 2: bila kwargs.get("peran") != "admin" tampilkan "Akses ditolak" dan return None


@catat_waktu
def laporan_besar():
    return sum(range(5_000_000))


print(laporan_besar())
# TODO 3: buat hapus_transaksi(id_trx, peran="kasir") dan pasang ketiga decorator
