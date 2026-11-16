# Solusi 4.1 - Class dan Object


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


class Produk:
    jumlah_produk = 0  # class attribute: dipakai bersama semua object

    def __init__(self, kode, nama, harga, stok=0):
        self.kode = kode            # instance attribute: milik tiap object
        self.nama = nama
        self.harga = harga
        self.stok = stok
        Produk.jumlah_produk += 1

    def info(self):
        return f"{self.kode} | {self.nama:<16} | {rupiah(self.harga)} | stok {self.stok}"

    def jual(self, qty):
        if qty > self.stok:
            return False
        self.stok -= qty
        return True

    def restock(self, qty):
        self.stok += qty

    def __str__(self):
        return self.info()


kopi = Produk("K01", "Kopi Susu Aren", 25000, 20)
matcha = Produk("T01", "Matcha Latte", 28000, 12)
croissant = Produk("F01", "Croissant", 18000, 10)
cheesecake = Produk("F02", "Cheesecake", 32000, 5)

print(f"Jumlah produk dibuat: {Produk.jumlah_produk}")
for p in [kopi, matcha, croissant, cheesecake]:
    print(p)
print()
for produk, qty in [(kopi, 5), (croissant, 50), (cheesecake, 5)]:
    if produk.jual(qty):
        print(f"Jual {qty:>2} {produk.nama:<16}: berhasil, sisa {produk.stok}")
    else:
        print(f"Jual {qty:>2} {produk.nama:<16}: GAGAL, stok hanya {produk.stok}")
cheesecake.restock(8)
print(f"\nSetelah restock: {cheesecake}")
