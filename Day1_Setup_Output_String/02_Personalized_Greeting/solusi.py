# Solusi 1.2 - Sapaan Personal

# 1. Ambil input pelanggan
nama = input("Siapa nama kamu? ").strip().title()  # Minta nama, hapus spasi di tepi, lalu ubah awal setiap kata menjadi huruf kapital.
kota = input("Dari kota mana? ").strip().title()  # Minta kota, rapikan spasi di tepi, dan samakan penulisan nama kota.
minuman = input("Minuman favorit? ").strip().lower()  # Minta minuman, rapikan spasi, dan ubah semua huruf menjadi kecil untuk tampilan konsisten.

# 2. Tampilkan sapaan
print()  # Cetak baris kosong agar sapaan terpisah dari pertanyaan input.
print(f"Halo, {nama} dari {kota}!")  # Gabungkan nama dan kota ke dalam f-string agar sapaan terasa personal.
print(f"Hari ini {minuman} spesial untukmu.")  # Masukkan minuman favorit ke dalam pesan menggunakan f-string.

# 3. Info tambahan
jumlah_huruf = len(nama.replace(" ", ""))  # Hapus spasi dari nama lalu hitung karakternya agar yang dihitung hanya huruf nama.
print(f"Nama kamu terdiri dari {jumlah_huruf} huruf.")  # Tampilkan jumlah karakter nama yang sudah dihitung.
