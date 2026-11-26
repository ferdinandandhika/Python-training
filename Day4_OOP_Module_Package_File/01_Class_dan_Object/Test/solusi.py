# Solusi 4.1B - Pesanan Sederhana


class Pesanan:
    def __init__(self, nama_menu, harga, jumlah):  # Konstruktor menerima data pesanan agar langsung dapat disimpan pada objek.
        self.nama_menu = nama_menu  # Simpan nama menu sebagai atribut agar dapat diakses melalui objek pesanan.
        self.harga = harga  # Simpan harga satu item untuk perhitungan total.
        self.jumlah = jumlah  # Simpan banyaknya item yang dipesan.

    def hitung_total(self):  # Definisikan perilaku objek untuk menghitung biaya seluruh item.
        return self.harga * self.jumlah  # Kalikan harga satu item dengan jumlah dan kembalikan hasilnya kepada pemanggil.


pesanan = Pesanan("Kopi Susu Aren", 25000, 2)  # Buat objek pesanan berisi menu, harga per item, dan jumlah.
total_rupiah = f"Rp {pesanan.hitung_total():,}".replace(",", ".")  # Hitung total dari metode objek lalu format sebagai nilai rupiah.

print(f"Pesanan: {pesanan.nama_menu} x{pesanan.jumlah}")  # Tampilkan nama menu dan jumlah yang dipesan.
print(f"Total  : {total_rupiah}")  # Tampilkan nilai total yang sudah diformat.
