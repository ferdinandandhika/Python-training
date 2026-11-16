"""Class produk TokoKu (inheritance)."""


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


class Produk:
    jenis = "Produk"

    def __init__(self, kode, nama, harga):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari nol")
        self.kode = kode
        self.nama = nama
        self.harga = int(harga)

    def harga_satuan(self):
        return self.harga

    def deskripsi(self):
        return self.nama

    def __repr__(self):
        return f"{type(self).__name__}({self.kode!r}, {self.nama!r}, {self.harga})"


class Minuman(Produk):
    jenis = "Minuman"
    TAMBAHAN = {"S": 0, "M": 3000, "L": 6000}

    def __init__(self, kode, nama, harga, ukuran="M"):
        super().__init__(kode, nama, harga)
        if ukuran not in self.TAMBAHAN:
            raise ValueError("Ukuran harus S, M, atau L")
        self.ukuran = ukuran

    def dengan_ukuran(self, ukuran):
        """Object baru dengan ukuran lain. Kode diberi akhiran agar tidak tergabung di keranjang."""
        baru = Minuman(self.kode, self.nama, self.harga, ukuran)
        baru.kode = f"{self.kode}-{ukuran}"
        return baru

    def harga_satuan(self):
        return self.harga + self.TAMBAHAN[self.ukuran]

    def deskripsi(self):
        return f"{self.nama} ({self.ukuran})"


class Makanan(Produk):
    jenis = "Makanan"
