# Solusi 5.2 - Decorator
import time
from datetime import datetime
from functools import wraps
from pathlib import Path

LOG = Path(__file__).parent / "aktivitas.log"


def catat_waktu(fungsi):
    @wraps(fungsi)
    def pembungkus(*args, **kwargs):
        mulai = time.perf_counter()
        hasil = fungsi(*args, **kwargs)
        print(f"[waktu] {fungsi.__name__} selesai dalam {time.perf_counter() - mulai:.3f} detik")
        return hasil
    return pembungkus


def log_aktivitas(fungsi):
    @wraps(fungsi)
    def pembungkus(*args, **kwargs):
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} {fungsi.__name__} args={args} kwargs={kwargs}\n")
        return fungsi(*args, **kwargs)
    return pembungkus


def hanya_admin(fungsi):
    @wraps(fungsi)
    def pembungkus(*args, **kwargs):
        if kwargs.get("peran") != "admin":
            print(f"[akses] Ditolak: {fungsi.__name__} hanya untuk admin.")
            return None
        return fungsi(*args, **kwargs)
    return pembungkus


@catat_waktu
def laporan_besar():
    return sum(range(5_000_000))


@catat_waktu
@log_aktivitas
@hanya_admin
def hapus_transaksi(id_trx, peran="kasir"):
    print(f"Transaksi {id_trx} dihapus.")
    return True


print("Total:", laporan_besar())
hapus_transaksi("TRX001", peran="kasir")
hapus_transaksi("TRX002", peran="admin")
print("Lihat isi file aktivitas.log")
