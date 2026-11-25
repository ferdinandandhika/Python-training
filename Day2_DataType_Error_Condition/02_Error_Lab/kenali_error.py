# Kenali tipe data dan ValueError

nama = "Andi"
jumlah = 3
harga = 12500.0

print(f"nama   : {nama} ({type(nama).__name__})")
print(f"jumlah : {jumlah} ({type(jumlah).__name__})")
print(f"harga  : {harga} ({type(harga).__name__})")

jumlah_teks = input("\nCoba masukkan jumlah barang (misalnya tiga): ")
try:
    jumlah = int(jumlah_teks)
except ValueError:
    print(f"\n'{jumlah_teks}' tidak bisa diubah menjadi int.")
else:
    print(f"{jumlah_teks} berhasil diubah menjadi int: {jumlah}")
