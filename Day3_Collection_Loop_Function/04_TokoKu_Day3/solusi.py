# TokoKu Day 3 - Keranjang Belanja
PAJAK = 0.11  # Simpan tarif pajak 11% dalam konstanta agar perhitungan memakai nilai yang sama.
LEBAR = 38  # Tetapkan lebar struk agar garis dan judul dicetak dengan ukuran seragam.
MENU = {  # Simpan kode produk beserta nama dan harga dalam kamus untuk pencarian saat transaksi.
    "K01": {"nama": "Kopi Susu Aren", "harga": 25000},  # Catat kopi susu aren dengan kode K01 dan harganya.
    "K02": {"nama": "Americano", "harga": 22000},  # Catat americano dengan kode K02 dan harganya.
    "T01": {"nama": "Matcha Latte", "harga": 28000},  # Catat matcha latte dengan kode T01 dan harganya.
    "F01": {"nama": "Croissant", "harga": 18000},  # Catat croissant dengan kode F01 dan harganya.
    "F02": {"nama": "Cheesecake", "harga": 32000},  # Catat cheesecake dengan kode F02 dan harganya.
}  # Akhiri kamus yang menjadi daftar produk toko.


def rupiah(angka):  # Buat fungsi untuk mengubah angka menjadi teks berformat rupiah.
    return "Rp " + f"{angka:,.0f}".replace(",", ".")  # Tambahkan awalan Rp dan gunakan titik sebagai pemisah ribuan.


def tampilkan_menu():  # Buat fungsi yang menampilkan semua produk beserta kode dan harganya.
    print("MENU TOKOKU")  # Tampilkan judul daftar produk.
    for kode, info in MENU.items():  # Ambil kode dan data setiap produk dari kamus MENU.
        print(f"  {kode}  {info['nama']:<16} {rupiah(info['harga'])}")  # Tampilkan kode, nama berlebar 16 karakter, dan harga.


def tambah_ke_keranjang(keranjang, kode, qty):  # Buat fungsi untuk menambahkan produk terpilih ke keranjang.
    info = MENU[kode]  # Cari data produk menggunakan kode yang sudah dipastikan ada di MENU.
    barang = {"nama": info["nama"], "harga": info["harga"], "qty": qty}  # Salin nama, harga, dan jumlah ke data barang transaksi.
    keranjang.append(barang)  # Masukkan data barang baru ke akhir list keranjang.


def cetak_struk(keranjang):  # Buat fungsi untuk menghitung total belanja dan mencetak struk.
    subtotal = 0  # Mulai jumlah harga barang sebelum diskon dan pajak dari nol.

    print("\n" + "=" * LEBAR)  # Cetak baris kosong dan garis pemisah sepanjang nilai LEBAR.
    print("STRUK TOKOKU".center(LEBAR))  # Letakkan judul struk di tengah lebar yang sudah ditetapkan.
    print("=" * LEBAR)  # Cetak garis pemisah kedua di bawah judul.

    for barang in keranjang:  # Proses satu per satu barang yang ada dalam keranjang.
        total_barang = barang["harga"] * barang["qty"]  # Hitung biaya setiap jenis barang dari harga dikali jumlah.
        subtotal += total_barang  # Tambahkan biaya barang ke subtotal semua belanja.
        print(f"{barang['nama']:<20} x{barang['qty']:<3} {rupiah(total_barang):>12}")  # Cetak nama, jumlah, dan biaya barang dengan kolom rata.

    if subtotal >= 200_000:  # Periksa lebih dulu apakah subtotal mencapai batas diskon tertinggi.
        persen_diskon = 0.15  # Terapkan diskon 15% untuk subtotal minimal 200.000.
    elif subtotal >= 100_000:  # Jika belum mencapai batas tertinggi, periksa batas diskon berikutnya.
        persen_diskon = 0.10  # Terapkan diskon 10% untuk subtotal minimal 100.000.
    else:  # Gunakan cabang ini jika subtotal di bawah kedua batas diskon.
        persen_diskon = 0  # Tetapkan diskon nol untuk belanja yang belum memenuhi syarat.

    diskon = subtotal * persen_diskon  # Hitung nilai uang diskon dari subtotal dan persentase yang berlaku.
    setelah_diskon = subtotal - diskon  # Kurangi diskon sebelum menghitung pajak.
    pajak = setelah_diskon * PAJAK  # Hitung pajak dari nilai belanja setelah diskon.
    total = setelah_diskon + pajak  # Tambahkan pajak untuk memperoleh jumlah yang harus dibayar.

    print("-" * LEBAR)  # Cetak pemisah sebelum rincian perhitungan.
    print(f"Subtotal     : {rupiah(subtotal)}")  # Cetak subtotal dalam format rupiah.
    print(f"Diskon       : -{rupiah(diskon)}")  # Cetak nilai diskon dengan tanda minus.
    print(f"Pajak (11%)  : {rupiah(pajak)}")  # Cetak nilai pajak dalam format rupiah.
    print(f"TOTAL BAYAR  : {rupiah(total)}")  # Cetak jumlah akhir yang harus dibayar.
    print("=" * LEBAR)  # Tutup struk dengan garis selebar yang ditentukan.


keranjang = []  # Buat list kosong untuk menyimpan barang yang dipilih selama transaksi.
tampilkan_menu()  # Tampilkan katalog sebelum meminta kode produk dari pengguna.

while True:  # Terus minta produk sampai pengguna memberi perintah selesai.
    kode = input("\nKode barang (atau selesai): ").strip().upper()  # Baca kode, rapikan spasi, dan samakan huruf menjadi kapital.
    if kode == "SELESAI":  # Periksa apakah pengguna ingin mengakhiri pemilihan produk.
        break  # Keluar dari perulangan input barang.

    if kode not in MENU:  # Periksa apakah kode yang dimasukkan tersedia di kamus MENU.
        print("Kode barang tidak ditemukan.")  # Beri tahu pengguna bahwa kode tersebut tidak dikenal.
        continue  # Mulai putaran baru agar pengguna dapat memasukkan kode yang benar.

    try:  # Coba membaca jumlah dan mengubahnya menjadi bilangan bulat.
        qty = int(input("Jumlah: "))  # Minta jumlah barang dan konversi masukan teks ke integer.
    except ValueError:  # Tangani masukan yang tidak dapat diubah menjadi bilangan bulat.
        print("Jumlah harus berupa angka bulat.")  # Jelaskan format jumlah yang diterima.
        continue  # Kembali ke awal supaya pengguna bisa mencoba lagi.

    if qty <= 0:  # Tolak jumlah nol atau negatif karena tidak menambah barang yang valid.
        print("Jumlah harus lebih dari nol.")  # Beri tahu bahwa jumlah harus berupa bilangan positif.
        continue  # Kembali ke awal untuk meminta pilihan barang dan jumlah lagi.

    tambah_ke_keranjang(keranjang, kode, qty)  # Simpan produk dan jumlah yang sudah lolos pemeriksaan ke keranjang.

if keranjang:  # Periksa apakah pengguna berhasil memasukkan setidaknya satu barang.
    cetak_struk(keranjang)  # Hitung dan tampilkan struk ketika keranjang berisi barang.
else:  # Jalankan cabang ini jika tidak ada barang yang dipilih.
    print("Keranjang kosong. Transaksi dibatalkan.")  # Beri tahu bahwa transaksi kosong tidak akan dicetak.
