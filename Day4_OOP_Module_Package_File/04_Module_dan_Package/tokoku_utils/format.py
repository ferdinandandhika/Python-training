"""Module untuk format tampilan angka."""


def rupiah(angka):
    """rupiah(1250000) -> 'Rp 1.250.000'"""
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


def persen(angka):
    """persen(0.15) -> '15%'"""
    return f"{angka:.0%}"
