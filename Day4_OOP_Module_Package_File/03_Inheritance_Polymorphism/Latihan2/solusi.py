# Solusi 4.3B - Mengubah Tampilan Info Produk


class Produk:
    def __init__(self, nama, harga):  # Konstruktor kelas induk menyimpan data yang umum bagi semua produk.
        self.nama = nama  # Simpan nama pada instance supaya metode milik kelas maupun turunannya dapat menggunakannya.
        self.harga = harga  # Simpan harga sebagai data instance yang dapat diformat ketika ditampilkan.

    def tampilkan_info(self):  # Definisikan tampilan umum; kelas turunan boleh menimpa metode ini sesuai kebutuhan.
        harga_rupiah = f"Rp {self.harga:,}".replace(",", ".")  # Bentuk teks harga dengan pemisah ribuan bergaya rupiah.
        print(f"Nama   : {self.nama}")  # Cetak nama yang tersimpan di objek produk.
        print(f"Harga  : {harga_rupiah}")  # Cetak harga dalam format yang mudah dibaca.


class Minuman(Produk):  # Buat kelas turunan yang mewarisi data dan perilaku dasar dari Produk.
    def tampilkan_info(self):  # Timpa metode induk untuk memberi keluaran khusus bagi objek Minuman.
        harga_rupiah = f"Rp {self.harga:,}".replace(",", ".")  # Format harga milik instance minuman sebagai nilai rupiah.
        print("Jenis  : Minuman")  # Tambahkan label jenis yang khusus untuk semua objek Minuman.
        print(f"Nama   : {self.nama}")  # Tampilkan nama minuman yang diwarisi dari data Produk.
        print(f"Harga  : {harga_rupiah}")  # Tampilkan harga minuman yang sudah diformat.


nama = input("Nama minuman: ").strip()  # Minta nama minuman kepada pengguna dan hilangkan spasi luar.
harga = int(input("Harga: "))  # Minta harga dan konversi masukan teks ke bilangan bulat.

minuman = Minuman(nama, harga)  # Buat objek Minuman menggunakan konstruktor yang diwarisi dari Produk.
minuman.tampilkan_info()  # Pemanggilan ini memilih versi metode Minuman karena metode induknya ditimpa.
