# TokoKu Day 2 - Validasi dan Diskon

nama = input("Nama pelanggan : ").strip().title()
menu = input("Nama barang    : ").strip().title()
harga_teks = input("Harga satuan   : ")
jumlah_teks = input("Jumlah         : ")

# TODO 1: gunakan try untuk mengubah harga_teks dan jumlah_teks menjadi int
# TODO 2: tangani ValueError; tampilkan pesan dan batalkan transaksi
# TODO 3: jika konversi berhasil, pastikan harga dan jumlah lebih dari nol
# TODO 4: hitung subtotal, lalu tentukan diskon dengan if/elif/else:
#         subtotal >= 200000 -> 15%
#         subtotal >= 100000 -> 10%
#         selain itu -> 0%
# TODO 5: hitung pajak 11% dari subtotal setelah diskon dan total bayar
# TODO 6: cetak struk dengan format Rupiah
