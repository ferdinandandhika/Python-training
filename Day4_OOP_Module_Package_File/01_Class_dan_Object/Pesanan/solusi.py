# Solusi 4.1 - Class dan Object


class Produk:
    def __init__(self, nama, harga):  # Konstruktor otomatis berjalan saat objek Produk dibuat agar data awal tersimpan pada objek.
        self.nama = nama  # Simpan nama sebagai atribut instance supaya setiap produk dapat memiliki nama sendiri.
        self.harga = harga  # Simpan harga sebagai atribut instance untuk digunakan saat informasi produk ditampilkan.

    def tampilkan_info(self):  # Sediakan perilaku untuk menampilkan informasi milik objek produk ini.
        harga_rupiah = f"Rp {self.harga:,}".replace(",", ".")  # Format angka dengan pemisah ribuan lalu ubah koma menjadi titik sesuai penulisan rupiah.
        print(f"Nama produk : {self.nama}")  # Tampilkan atribut nama agar pengguna mengetahui produk yang sedang dilihat.
        print(f"Harga       : {harga_rupiah}")  # Tampilkan harga yang sudah diformat agar lebih mudah dibaca.


kopi = Produk("Kopi Susu Aren", 25000)  # Buat satu objek Produk dengan nama dan harga contoh.
kopi.tampilkan_info()  # Panggil metode objek untuk menampilkan data kopi.
