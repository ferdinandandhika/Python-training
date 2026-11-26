# Solusi 2.2 - Memeriksa Jumlah Barang

jumlah_teks = input("Jumlah barang: ")  # Meminta jumlah barang sebagai teks karena input selalu menghasilkan string.

try:  # Mencoba mengubah masukan; blok ini mencegah program langsung berhenti jika formatnya salah.
    jumlah = int(jumlah_teks)  # Mengubah masukan menjadi bilangan bulat agar dapat divalidasi dan dihitung.
except ValueError:  # Menjalankan penanganan khusus ketika konversi ke integer gagal.
    print("Jumlah harus berupa angka bulat.")  # Menjelaskan kesalahan jika teks masukan tidak dapat diubah menjadi integer.
else:  # Menjalankan validasi jumlah hanya jika konversi integer berhasil.
    if jumlah < 0:  # Memeriksa nilai negatif karena jumlah stok tidak boleh kurang dari nol.
        print("Jumlah tidak boleh negatif.")  # Memberi tahu pengguna bahwa jumlah yang dimasukkan tidak valid.
    elif jumlah == 0:  # Memeriksa kondisi khusus saat jumlah barang tepat nol.
        print(f"Jumlah barang: {jumlah}")  # Menampilkan jumlah yang sudah berhasil dikonversi.
        print("Stok habis.")  # Menjelaskan bahwa tidak ada barang yang tersedia.
    else:  # Menangani jumlah positif, yaitu nilai yang bukan negatif maupun nol.
        print(f"Jumlah barang: {jumlah}")  # Menampilkan jumlah barang jika nilainya positif dan valid.
