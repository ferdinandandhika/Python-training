# Solusi 2.2 - Memeriksa Jumlah Barang

jumlah_teks = input("Jumlah barang: ")

try:
    jumlah = int(jumlah_teks)
except ValueError:
    print("Jumlah harus berupa angka bulat.")
else:
    if jumlah < 0:
        print("Jumlah tidak boleh negatif.")
    elif jumlah == 0:
        print(f"Jumlah barang: {jumlah}")
        print("Stok habis.")
    else:
        print(f"Jumlah barang: {jumlah}")
