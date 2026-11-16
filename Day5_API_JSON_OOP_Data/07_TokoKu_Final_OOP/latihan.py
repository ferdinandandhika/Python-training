# TokoKu FINAL OOP - kerangka
# 1. Salin package tokoku_oop dari Day4/07_TokoKu_Day4_OOP.
# 2. Tambahkan pembayaran.py (Latihan 5.3) dan kurs.py (Latihan 5.1).
# 3. Ubah Toko.checkout(keranjang, metode, member) agar memanggil metode.proses(total).
# 4. Tambahkan Toko.laporan() dengan Pandas (Latihan 5.4) dan @catat_waktu (Latihan 5.2).
# 5. Tambahkan Toko.dashboard(folder) dengan Matplotlib (Latihan 5.5).
# 6. Jalankan buat_data_contoh.py, lalu lengkapi menu di bawah.
# 7. Jalankan python -m unittest -v


def main():
    while True:
        print("\n=== TOKOKU ===")
        print("1. Transaksi baru\n2. Laporan penjualan\n3. Buat grafik dashboard")
        print("4. Lihat harga dalam USD\n5. Keluar")
        pilihan = input("Pilih: ").strip()
        # TODO: hubungkan setiap pilihan ke method Toko
        if pilihan == "5":
            break


if __name__ == "__main__":
    main()
