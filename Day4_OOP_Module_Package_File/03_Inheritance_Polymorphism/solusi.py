# Solusi 4.3 - Inheritance dan Polymorphism


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
        super().__init__(kode, nama, harga)
        if ukuran not in self.TAMBAHAN:
            raise ValueError("Ukuran harus S, M, atau L")
        self.ukuran = ukuran
        self.es = es

    def harga_akhir(self, qty=1):
        return (self.harga + self.TAMBAHAN[self.ukuran]) * qty

    def deskripsi(self):
        return f"{self.nama} ({self.ukuran}, {'es' if self.es else 'panas'})"


class Makanan(Produk):
    BIAYA_HANGAT = 2000

    def __init__(self, kode, nama, harga, dihangatkan=False):
        super().__init__(kode, nama, harga)
        self.dihangatkan = dihangatkan

    def harga_akhir(self, qty=1):
        return (self.harga + (self.BIAYA_HANGAT if self.dihangatkan else 0)) * qty

    def deskripsi(self):
        return self.nama + (" (hangat)" if self.dihangatkan else "")


class Merchandise(Produk):
    def harga_akhir(self, qty=1):
        total = super().harga_akhir(qty)
        return total * 0.9 if qty >= 3 else total

    def deskripsi(self):
        return f"{self.nama} [merch]"


pesanan = [
    (Minuman("K01", "Kopi Susu Aren", 25000, "L", es=True), 2),
    (Minuman("T01", "Matcha Latte", 28000, "S", es=False), 1),
    (Makanan("F01", "Croissant", 18000, dihangatkan=True), 3),
    (Merchandise("M01", "Tumbler TokoKu", 85000), 3),
]
total = 0
for produk, qty in pesanan:            # polymorphism: method sama, perilaku beda
    subtotal = produk.harga_akhir(qty)
    total += subtotal
    print(f"{produk.deskripsi():<28} x{qty}  {rupiah(subtotal):>12}")
print(f"{'TOTAL':<32}{rupiah(total):>12}\n")
for jenis in (Minuman, Makanan, Merchandise):
    jumlah = sum(qty for p, qty in pesanan if isinstance(p, jenis))
    print(f"{jenis.__name__:<12}: {jumlah} item")
print("Minuman adalah Produk?", issubclass(Minuman, Produk))
