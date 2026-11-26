# Latihan 4.3B - Mengubah Tampilan Info Produk


class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        # TODO 1: tampilkan nama dan harga produk
        pass


class Minuman(Produk):
    def tampilkan_info(self):
        # TODO 2: tampilkan jenis "Minuman", nama, dan harga
        # Method ini menggantikan tampilkan_info() dari Produk
        pass


nama = input("Nama minuman: ").strip()
harga = int(input("Harga: "))

# TODO 3: buat object Minuman lalu panggil tampilkan_info()
