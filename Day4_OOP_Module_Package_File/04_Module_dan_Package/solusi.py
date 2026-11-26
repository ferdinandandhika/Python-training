# Solusi 4.4
from tokoku_utils import rupiah, persen, hitung_diskon  # Impor fungsi dari modul agar dapat digunakan kembali tanpa menyalin implementasinya.

for subtotal in [50_000, 120_000, 250_000]:  # Ulangi contoh untuk tiga nilai subtotal yang berbeda.
    p = hitung_diskon(subtotal, member=True)  # Minta modul menghitung tingkat diskon untuk pelanggan member pada subtotal ini.
    print(f"{rupiah(subtotal):>12}  diskon {persen(p):>4}  bayar {rupiah(subtotal * (1 - p))}")  # Format dan tampilkan subtotal, persentase diskon, serta jumlah yang harus dibayar.
