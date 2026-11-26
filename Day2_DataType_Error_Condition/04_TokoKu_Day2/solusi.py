# Solusi TokoKu Day 2 - Validasi dan Diskon

nama = input("Nama pelanggan : ").strip().title()  # Meminta nama, menghapus spasi di tepi, lalu merapikan huruf kapital setiap kata.
menu = input("Nama barang    : ").strip().title()  # Meminta nama barang lalu merapikan spasi dan kapitalisasi untuk struk.
harga_teks = input("Harga satuan   : ")  # Menerima harga satuan sebagai teks sebelum validasi angka.
jumlah_teks = input("Jumlah         : ")  # Menerima banyak barang sebagai teks sebelum validasi angka.

try:  # Mencoba mengubah kedua masukan menjadi angka bulat sebelum perhitungan dilakukan.
    harga = int(harga_teks)  # Mengonversi harga menjadi bilangan bulat agar bisa dipakai dalam perhitungan.
    jumlah = int(jumlah_teks)  # Mengonversi jumlah barang menjadi bilangan bulat.
except ValueError:  # Menangani kegagalan konversi jika harga atau jumlah bukan angka bulat.
    print("Harga dan jumlah harus berupa angka bulat. Transaksi dibatalkan.")  # Menangani input yang tidak bisa dikonversi dan membatalkan perhitungan.
else:  # Melanjutkan validasi hanya jika kedua konversi berhasil.
    if harga <= 0 or jumlah <= 0:  # Memastikan harga dan jumlah keduanya positif sebelum transaksi dihitung.
        print("Harga dan jumlah harus lebih dari nol. Transaksi dibatalkan.")  # Memberi alasan transaksi tidak dilanjutkan.
    else:  # Menghitung transaksi ketika harga dan jumlah memenuhi syarat.
        subtotal = harga * jumlah  # Menghitung biaya sebelum diskon dengan mengalikan harga dan jumlah.

        if subtotal >= 200_000:  # Memeriksa ambang diskon terbesar terlebih dahulu.
            persen_diskon = 0.15  # Menetapkan diskon 15 persen untuk subtotal minimal 200.000.
        elif subtotal >= 100_000:  # Memeriksa ambang diskon berikutnya jika ambang terbesar tidak tercapai.
            persen_diskon = 0.10  # Menetapkan diskon 10 persen untuk subtotal minimal 100.000.
        else:  # Menggunakan tarif nol jika subtotal tidak memenuhi ambang diskon.
            persen_diskon = 0  # Tidak memberi diskon jika subtotal belum mencapai ambang pertama.

        diskon = subtotal * persen_diskon  # Menghitung nilai rupiah diskon dari subtotal dan persentasenya.
        subtotal_setelah_diskon = subtotal - diskon  # Mengurangi diskon dari subtotal sebelum menghitung pajak.
        pajak = subtotal_setelah_diskon * 0.11  # Menghitung pajak 11 persen berdasarkan subtotal setelah diskon.
        total = subtotal_setelah_diskon + pajak  # Menambahkan pajak untuk memperoleh jumlah yang harus dibayar.

        print()  # Mencetak baris kosong agar struk terpisah dari keluaran sebelumnya.
        print("=" * 36)  # Membuat garis pemisah sepanjang 36 karakter.
        print("STRUK TOKOKU".center(36))  # Menempatkan judul struk di tengah lebar 36 karakter.
        print("=" * 36)  # Menutup bagian judul dengan garis pemisah yang sama.
        print(f"Pelanggan       : {nama}")  # Mencetak nama pelanggan pada struk.
        print(f"{menu} x{jumlah}")  # Mencetak nama barang dan jumlah yang dibeli.
        print(f"Harga satuan    : Rp {harga:,.0f}".replace(",", "."))  # Memformat harga tanpa angka desimal lalu mengubah pemisah ribuan ke titik.
        print(f"Subtotal        : Rp {subtotal:,.0f}".replace(",", "."))  # Menampilkan subtotal dengan format rupiah dan titik pemisah ribuan.
        print(
            f"Diskon ({persen_diskon:.0%})    : -Rp {diskon:,.0f}".replace(",", ".")  # Menyusun diskon sebagai persentase bulat dan nominal rupiah.
        )  # Mencetak baris diskon yang sudah diformat.
        print(f"Pajak (11%)     : Rp {pajak:,.0f}".replace(",", "."))  # Menampilkan pajak dengan format rupiah tanpa angka desimal.
        print("-" * 36)  # Memisahkan rincian transaksi dari total pembayaran.
        print(f"TOTAL BAYAR     : Rp {total:,.0f}".replace(",", "."))  # Menampilkan jumlah akhir yang harus dibayar.
        print("=" * 36)  # Mengakhiri struk dengan garis pembatas.
        print(f"Terima kasih, {nama}!")  # Menutup struk dengan ucapan terima kasih kepada pelanggan.
