# Latihan 4.3A - Inheritance dengan Input


class Produk:
    def __init__(self, nama, harga):
        # TODO 1: simpan nama dan harga sebagai attribute
        pass

    def tampilkan_info(self):
        # TODO 2: tampilkan nama dan harga produk
        pass


class Minuman(Produk):
    pass


nama = input("Nama minuman: ").strip()
harga = int(input("Harga: "))

# TODO 3: buat object Minuman dari nama dan harga
# TODO 4: panggil method tampilkan_info()
