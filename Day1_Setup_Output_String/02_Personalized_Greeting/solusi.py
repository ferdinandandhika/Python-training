# Solusi 1.2 - Sapaan Personal

# 1. Ambil input pelanggan
nama = input("Siapa nama kamu? ").strip().title()
kota = input("Dari kota mana? ").strip().title()
minuman = input("Minuman favorit? ").strip().lower()

# 2. Tampilkan sapaan
print()
print(f"Halo, {nama} dari {kota}!")
print(f"Hari ini {minuman} spesial untukmu.")

# 3. Info tambahan
jumlah_huruf = len(nama.replace(" ", ""))
print(f"Nama kamu terdiri dari {jumlah_huruf} huruf.")
