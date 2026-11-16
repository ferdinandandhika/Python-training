# Solusi 4.4
from tokoku_utils import rupiah, persen, hitung_diskon

for subtotal in [50_000, 120_000, 250_000]:
    p = hitung_diskon(subtotal, member=True)
    print(f"{rupiah(subtotal):>12}  diskon {persen(p):>4}  bayar {rupiah(subtotal * (1 - p))}")
