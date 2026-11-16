# Latihan 4.3 - Inheritance dan Polymorphism


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def harga_akhir(self, qty=1):
        return self.harga * qty

    def deskripsi(self):
        return self.nama


class Minuman(Produk):
    TAMBAHAN = {"S": 0, "M": 3000, "L": 6000}

    def __init__(self, kode, nama, harga, ukuran="M", es=True):
        pass  # TODO 1: panggil super().__init__ lalu simpan ukuran dan es

    # TODO 2: override harga_akhir -> (harga + TAMBAHAN[ukuran]) * qty
    # TODO 3: override deskripsi -> "Kopi Susu Aren (L, es)"


class Makanan(Produk):
    pass  # TODO 4: attribute dihangatkan, +2000 per porsi bila True


class Merchandise(Produk):
    pass  # TODO 5: diskon 10% bila qty >= 3 (pakai super().harga_akhir(qty))


pesanan = [
    (Minuman("K01", "Kopi Susu Aren", 25000, "L", es=True), 2),
    (Minuman("T01", "Matcha Latte", 28000, "S", es=False), 1),
    (Makanan("F01", "Croissant", 18000, dihangatkan=True), 3),
    (Merchandise("M01", "Tumbler TokoKu", 85000), 3),
]
# TODO 6: loop pesanan, tampilkan deskripsi, qty, harga_akhir
# TODO 7: hitung total dan jumlah item per jenis dengan isinstance()
