# Solusi 1.1 - Kartu Identitas Toko
nama_toko = "KOPI TOKOKU"  # Simpan nama toko dalam variabel agar mudah dipakai saat mencetak kartu identitas.
alamat = "Jl. Merdeka No. 10, Bandung"  # Simpan alamat toko sebagai teks untuk ditampilkan kepada pelanggan.
jam_buka = "08.00 - 22.00"  # Simpan rentang jam operasional toko supaya informasinya ikut tercetak.
telepon = "022-1234567"  # Simpan nomor telepon toko sebagai teks karena nomor telepon bukan untuk dihitung.

garis = "=" * 40  # Ulangi tanda sama dengan 40 kali untuk membuat garis pemisah sepanjang 40 karakter.
print(garis)  # Cetak garis pembuka agar bagian atas kartu terlihat rapi.
print(nama_toko.center(40))  # Pusatkan nama toko di dalam lebar 40 karakter agar tampil di tengah.
print(garis)  # Cetak garis setelah nama untuk memisahkannya dari informasi toko.
print("Alamat   :", alamat)  # Cetak label alamat dan nilai alamat supaya pembaca tahu informasi yang ditampilkan.
print("Jam buka :", jam_buka)  # Cetak label jam buka beserta jadwal operasional toko.
print("Telepon  :", telepon)  # Cetak label telepon beserta nomor yang dapat dihubungi.
print(garis)  # Cetak garis penutup untuk menandai akhir kartu identitas.
