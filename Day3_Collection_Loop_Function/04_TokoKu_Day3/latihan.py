# TokoKu Day 3 - Keranjang Belanja
PAJAK = 0.11
LEBAR = 38
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
    # TODO 1: gunakan for untuk menampilkan kode, nama, dan harga dari MENU
    pass


def tambah_ke_keranjang(keranjang, kode, qty):
    # TODO 2: ambil info barang dari MENU dan tambahkan ke keranjang
    pass


def cetak_struk(keranjang):
    # TODO 3: gunakan for untuk menampilkan barang dan menghitung subtotal
    # TODO 4: tentukan diskon dengan if/elif, lalu hitung pajak dan total
    # TODO 5: tampilkan ringkasan pembayaran
    pass


keranjang = []
tampilkan_menu()

# TODO 6: gunakan while untuk meminta kode dan jumlah sampai kode "selesai"
#         kode tidak valid atau jumlah tidak valid: tampilkan pesan
#         kode valid dan jumlah positif: panggil tambah_ke_keranjang()

# TODO 7: jika keranjang berisi barang, panggil cetak_struk()
#         jika kosong, tampilkan pesan transaksi dibatalkan
