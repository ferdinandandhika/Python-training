# TokoKu Day 4 OOP - aplikasi kasir yang memakai package tokoku_oop
from pathlib import Path  # Impor Path untuk membentuk alamat file data relatif terhadap lokasi skrip.

from tokoku_oop import Keranjang, Minuman, Toko, rupiah  # Impor objek domain dan formatter dari package agar aplikasi utama memakai implementasi bersama.

FOLDER = Path(__file__).parent  # Simpan folder skrip sebagai dasar untuk menemukan menu dan file transaksi.
LEBAR = 40  # Tetapkan lebar tampilan struk agar semua garis dan judul rata.


def minta_angka(pesan):  # Buat fungsi pembantu yang terus meminta angka positif dengan pesan yang diberikan.
    while True:  # Ulangi permintaan sampai pengguna memasukkan bilangan bulat yang lebih besar dari nol.
        try:  # Lindungi konversi angka agar teks yang bukan angka tidak menghentikan aplikasi.
            nilai = int(input(pesan))  # Tampilkan prompt, baca masukan, lalu konversikan menjadi bilangan bulat.
            if nilai > 0:  # Pastikan jumlah yang dimasukkan bernilai positif.
                return nilai  # Kembalikan angka yang valid agar pemanggil dapat menggunakannya.
        except ValueError:  # Masuk ke sini bila int() tidak dapat mengubah teks menjadi bilangan bulat.
            pass  # Abaikan kesalahan konversi untuk sementara lalu tampilkan instruksi di bawah.
        print("  Masukkan angka lebih dari nol.")  # Minta pengguna mencoba kembali setelah masukan tidak valid.


def transaksi(toko):  # Jalankan satu transaksi kasir menggunakan objek Toko yang diberikan.
    keranjang = Keranjang()  # Buat keranjang kosong untuk mengumpulkan barang dalam transaksi saat ini.
    for p in toko.katalog.values():  # Iterasi produk yang tersedia agar kode dan harga dapat ditampilkan kepada kasir.
        print(f"  {p.kode}  {p.deskripsi():<16} {rupiah(p.harga_satuan())}")  # Tampilkan kode, deskripsi, dan harga satuan produk dengan format rapi.
    while True:  # Terus terima kode produk sampai kasir memasukkan kata untuk menyelesaikan transaksi.
        kode = input("Kode menu (selesai): ").strip().upper()  # Baca kode menu, buang spasi tepi, lalu samakan kapitalisasinya.
        if kode == "SELESAI":  # Periksa perintah berhenti yang tidak peka terhadap besar-kecil huruf.
            break  # Hentikan pemilihan produk dan lanjutkan ke proses pembayaran.
        try:  # Cari produk dengan penanganan jika kode tidak terdaftar.
            produk = toko.cari(kode)  # Minta objek Toko menemukan dan mengembalikan produk berdasarkan kode.
        except KeyError as e:  # Tangkap kegagalan pencarian kode yang menandakan produk tidak ditemukan.
            print(" ", e.args[0])  # Tampilkan pesan kesalahan yang disimpan pada exception tanpa menghentikan transaksi.
            continue  # Lewati sisa putaran ini agar kasir dapat memasukkan kode lain.
        if isinstance(produk, Minuman):  # Periksa tipe objek agar pilihan ukuran hanya diminta untuk produk minuman.
            ukuran = input("  Ukuran S/M/L [M]: ").strip().upper() or "M"  # Minta ukuran, rapikan hurufnya, dan gunakan M bila masukan kosong.
            produk = produk.dengan_ukuran(ukuran if ukuran in Minuman.TAMBAHAN else "M")  # Buat pilihan produk berukuran sesuai opsi valid atau gunakan ukuran M sebagai cadangan.
        keranjang.tambah(produk, minta_angka("  Jumlah: "))  # Tambahkan produk ke keranjang dengan jumlah positif yang diminta helper.
        print(f"  Keranjang: {len(keranjang)} item")  # Tampilkan jumlah item yang kini tersimpan di keranjang.
    if not keranjang:  # Periksa apakah kasir mengakhiri pemilihan tanpa menambahkan barang.
        print("Transaksi dibatalkan.")  # Beri tahu pengguna bahwa tidak ada produk yang akan dibayar.
        return  # Akhiri fungsi lebih awal karena transaksi kosong tidak perlu checkout.
    member = input("Member? (y/n): ").strip().lower() == "y"  # Ubah jawaban pengguna menjadi Boolean yang menyatakan status member.
    r = toko.checkout(keranjang, member)  # Minta Toko menghitung dan mencatat transaksi berdasarkan keranjang serta status member.
    print("=" * LEBAR)  # Cetak garis pembuka sepanjang lebar struk.
    print(toko.nama.upper().center(LEBAR))  # Cetak nama toko dalam huruf kapital dan posisikan di tengah struk.
    print("=" * LEBAR)  # Pisahkan judul toko dari rincian belanja dengan garis.
    print(keranjang)  # Tampilkan isi keranjang menggunakan representasi teks milik objek keranjang.
    print("-" * LEBAR)  # Cetak garis pemisah sebelum rincian pembayaran.
    for label, kunci in [("Subtotal", "subtotal"), ("Diskon", "diskon"), ("Pajak 11%", "pajak"), ("TOTAL", "total")]:  # Pasangkan label struk dengan nama nilai pada hasil checkout.
        nilai = rupiah(r[kunci])  # Ambil nilai berdasarkan kunci dan ubah menjadi teks rupiah.
        print(f"{label:<24}{'-' + nilai if kunci == 'diskon' else nilai:>16}")  # Rata kiri label, rata kanan nominal, dan awali diskon dengan tanda minus.
    print("=" * LEBAR)  # Cetak garis penutup agar struk memiliki batas akhir yang jelas.


def main():  # Atur alur utama aplikasi kasir agar dapat dijalankan langsung atau diimpor tanpa otomatis membuka menu.
    toko = Toko.dari_csv(FOLDER / "menu.csv", file_transaksi=FOLDER / "transaksi.csv")  # Bangun toko dari katalog CSV dan arahkan pencatatan transaksi ke file CSV lain.
    while True:  # Tampilkan menu utama berulang kali sampai pengguna memilih keluar.
        cmd = input(f"\n[{toko.nama}] baru | laporan | keluar: ").strip().lower()  # Tampilkan nama toko, baca perintah, lalu normalkan huruf masukan.
        if cmd == "baru":  # Periksa apakah pengguna ingin memulai transaksi baru.
            transaksi(toko)  # Jalankan alur kasir dengan menggunakan objek toko yang sama.
        elif cmd == "laporan":  # Periksa apakah pengguna ingin melihat ringkasan penjualan.
            lap = toko.laporan()  # Ambil ringkasan transaksi dan omzet dari objek toko.
            print(f"  Transaksi: {lap['jumlah']} | Omzet sebelum pajak: {rupiah(lap['omzet'])}")  # Tampilkan jumlah transaksi serta omzet yang diformat sebagai rupiah.
        elif cmd == "keluar":  # Periksa perintah untuk menutup aplikasi kasir.
            break  # Hentikan perulangan menu dan akhiri fungsi utama.


if __name__ == "__main__":  # Jalankan aplikasi hanya saat skrip dieksekusi langsung, bukan ketika modulnya diimpor.
    main()  # Mulai menu kasir setelah pemeriksaan titik masuk program.
