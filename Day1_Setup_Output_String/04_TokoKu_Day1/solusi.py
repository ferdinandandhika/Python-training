# TokoKu Day 1 - Struk Sederhana
LEBAR = 30  # Tetapkan lebar struk agar judul dan garis memiliki ukuran yang konsisten.

nama = input("Nama pelanggan : ").strip().title()  # Minta nama pelanggan, buang spasi tepi, dan rapikan huruf kapitalnya.
menu = input("Menu           : ").strip().title()  # Minta nama menu, buang spasi tepi, dan rapikan huruf kapitalnya.
harga = int(input("Harga          : "))  # Minta harga lalu ubah jawaban teks menjadi bilangan bulat agar dapat dihitung.
jumlah = int(input("Jumlah         : "))  # Minta banyak barang lalu ubah jawaban menjadi bilangan bulat untuk perhitungan.
total = harga * jumlah  # Kalikan harga satu barang dengan jumlah barang untuk mendapatkan total pembayaran.


def rupiah(angka):  # Buat fungsi agar nilai angka dapat ditampilkan dengan awalan Rp dan pemisah ribuan yang sesuai.
    return "Rp " + f"{angka:,}".replace(",", ".")  # Format angka dengan pemisah ribuan, ganti koma menjadi titik, lalu tambahkan label Rupiah.


print()  # Sisipkan baris kosong supaya struk tidak menempel pada teks input sebelumnya.
print("=" * LEBAR)  # Cetak garis pembuka sepanjang nilai lebar struk.
print("STRUK TOKOKU".center(LEBAR))  # Pusatkan judul struk di dalam lebar yang sudah ditetapkan.
print("=" * LEBAR)  # Cetak garis pemisah di bawah judul.
print(f"Pelanggan : {nama}")  # Tampilkan nama pelanggan yang tadi dimasukkan.
print(f"Menu      : {menu}")  # Tampilkan nama menu yang dipesan.
print(f"Harga     : {rupiah(harga)}")  # Format harga satuan sebagai Rupiah lalu tampilkan pada struk.
print(f"Jumlah    : {jumlah}")  # Tampilkan jumlah barang yang dibeli.
print("-" * LEBAR)  # Cetak garis untuk memisahkan rincian pesanan dari total.
print(f"TOTAL     : {rupiah(total)}")  # Format dan tampilkan total pembayaran dalam bentuk Rupiah.
print("=" * LEBAR)  # Cetak garis penutup bagian rincian struk.
print(f"Terima kasih, {nama}!".center(LEBAR))  # Pusatkan pesan terima kasih yang menyebut nama pelanggan.
