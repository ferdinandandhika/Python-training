# TokoKu Day 3 - Keranjang Belanja
PAJAK = 0.11
MENU = {
    "K01": {"nama": "Kopi Susu Aren", "harga": 25000},
    "K02": {"nama": "Americano", "harga": 22000},
    "T01": {"nama": "Matcha Latte", "harga": 28000},
    "F01": {"nama": "Croissant", "harga": 18000},
    "F02": {"nama": "Cheesecake", "harga": 32000},
}


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


def tampilkan_menu():
    pass  # TODO 1


def tambah_ke_keranjang(keranjang, kode, qty):
    pass  # TODO 2: gabungkan qty bila kode sudah ada


def hitung_total(keranjang, member=False):
    pass  # TODO 3: return dict subtotal, persen, diskon, pajak, total


def cetak_struk(keranjang, ringkasan):
    pass  # TODO 4

# TODO 5: program utama dengan while loop sampai kasir mengetik "selesai"
