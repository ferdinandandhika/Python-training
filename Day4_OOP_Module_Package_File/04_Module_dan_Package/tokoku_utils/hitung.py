"""Module untuk aturan bisnis TokoKu."""


def hitung_diskon(subtotal, member=False):
    """>= 200.000 -> 15%, >= 100.000 -> 10%, member tambah 5%."""
    if subtotal >= 200_000:
        persen = 0.15
    elif subtotal >= 100_000:
        persen = 0.10
    else:
        persen = 0.0
    if member:
        persen += 0.05
    return persen
