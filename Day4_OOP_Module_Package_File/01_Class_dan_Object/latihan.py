# Latihan 4.1 - Class dan Object


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


class Produk:
    # TODO 1: class attribute jumlah_produk = 0

    def __init__(self, kode, nama, harga, stok=0):
        # TODO 2: simpan semua parameter sebagai attribute (self.kode = kode, dst)
        # TODO 3: tambah Produk.jumlah_produk sebanyak 1
        pass

    def info(self):
        # TODO 4: return "K01 | Kopi Susu Aren | Rp 25.000 | stok 20"
        pass

    def jual(self, qty):
        # TODO 5: bila qty > stok return False; bila cukup kurangi stok dan return True
        pass

    def restock(self, qty):
        # TODO 6: tambah stok
        pass

    # TODO 7: method __str__ yang mengembalikan self.info()


# TODO 8: buat 4 object, misalnya kopi = Produk("K01", "Kopi Susu Aren", 25000, 20)
# TODO 9: tampilkan jumlah produk, jual, restock, lalu print semua object
