# Solusi 4.3A - Inheritance dengan Input


class Produk:
    def __init__(self, nama, harga):  # Konstruktor kelas dasar menyimpan informasi umum yang dimiliki produk.
        self.nama = nama  # Simpan nama produk pada instance agar dapat dipakai metode kelas dan turunannya.
        self.harga = harga  # Simpan harga produk sebagai atribut instance.

    def tampilkan_info(self):  # Definisikan perilaku umum yang diwarisi oleh jenis produk lainnya.
        harga_rupiah = f"Rp {self.harga:,}".replace(",", ".")  # Format harga memakai pemisah ribuan lalu titik untuk gaya rupiah.
        print(f"Produk: {self.nama}")  # Tampilkan nama produk yang disimpan pada objek.
        print(f"Harga : {harga_rupiah}")  # Tampilkan harga yang telah disiapkan dalam format rupiah.


class Minuman(Produk):  # Turunkan kelas Minuman dari Produk agar atribut dan perilaku umum diwarisi.
    pass  # Tidak menambahkan perilaku baru; kelas ini tetap dapat memakai konstruktor dan metode dari Produk.


nama = input("Nama minuman: ").strip()  # Minta nama minuman lalu rapikan spasi di ujung masukan.
harga = int(input("Harga: "))  # Minta harga dan ubah teks masukan menjadi bilangan bulat.

minuman = Minuman(nama, harga)  # Buat objek Minuman; konstruktor yang diwarisi dari Produk mengisi nama dan harga.
minuman.tampilkan_info()  # Panggil metode warisan untuk menampilkan informasi minuman.
