# Solusi kalkulator dengan beberapa function


def tambah(a, b):  # Definisikan fungsi untuk menerima dua nilai dan mengembalikan jumlahnya.
    return a + b  # Kembalikan hasil penjumlahan kedua angka kepada pemanggil fungsi.


def kurang(a, b):  # Definisikan fungsi untuk menerima dua nilai dan mengembalikan selisihnya.
    return a - b  # Kembalikan hasil pengurangan b dari a.


def kali(a, b):  # Definisikan fungsi untuk menerima dua nilai dan mengembalikan hasil kalinya.
    return a * b  # Kembalikan hasil perkalian kedua angka.


def bagi(a, b):  # Definisikan fungsi untuk membagi dua nilai dengan pemeriksaan pembagi nol.
    if b == 0:  # Periksa pembagi lebih dulu agar program tidak mencoba membagi dengan nol.
        return None  # Gunakan None sebagai tanda bahwa pembagian tidak dapat dilakukan.
    return a / b  # Jika pembagi bukan nol, kembalikan hasil pembagian.


def tampilkan_menu():  # Definisikan fungsi untuk mencetak seluruh pilihan operasi kalkulator.
    print("\n=== Kalkulator ===")  # Tampilkan judul menu dengan baris baru di depannya.
    print("1. Tambah")  # Tampilkan pilihan operasi penjumlahan.
    print("2. Kurang")  # Tampilkan pilihan operasi pengurangan.
    print("3. Kali")  # Tampilkan pilihan operasi perkalian.
    print("4. Bagi")  # Tampilkan pilihan operasi pembagian.
    print("5. Keluar")  # Tampilkan pilihan untuk mengakhiri program.
    print("===================")  # Tampilkan garis pemisah agar menu lebih mudah dibaca.


while True:  # Ulangi menu sampai pengguna memilih keluar.
    tampilkan_menu()  # Tampilkan pilihan operasi setiap kali satu putaran dimulai.
    pilihan = input("Pilih operasi: ")  # Baca pilihan pengguna sebagai teks.

    if pilihan == "5":  # Periksa apakah pengguna memilih pilihan keluar.
        print("Program selesai.")  # Beri tahu pengguna bahwa program akan dihentikan.
        break  # Hentikan perulangan utama dan akhiri program.

    if pilihan not in ("1", "2", "3", "4"):  # Tolak masukan yang bukan salah satu operasi yang tersedia.
        print("Pilihan tidak tersedia.")  # Beri tahu pengguna bahwa pilihan harus diperbaiki.
        continue  # Kembali menampilkan menu tanpa meminta angka untuk pilihan yang salah.

    angka_1 = float(input("Angka pertama: "))  # Baca angka pertama dan ubah teks masukan menjadi bilangan desimal.
    angka_2 = float(input("Angka kedua: "))  # Baca angka kedua dan ubah teks masukan menjadi bilangan desimal.

    if pilihan == "1":  # Pilih fungsi penjumlahan ketika masukan pengguna adalah 1.
        hasil = tambah(angka_1, angka_2)  # Jalankan penjumlahan dan simpan hasilnya.
    elif pilihan == "2":  # Pilih fungsi pengurangan ketika masukan pengguna adalah 2.
        hasil = kurang(angka_1, angka_2)  # Jalankan pengurangan dan simpan hasilnya.
    elif pilihan == "3":  # Pilih fungsi perkalian ketika masukan pengguna adalah 3.
        hasil = kali(angka_1, angka_2)  # Jalankan perkalian dan simpan hasilnya.
    else:  # Karena pilihan sudah divalidasi, satu-satunya pilihan tersisa adalah pembagian.
        hasil = bagi(angka_1, angka_2)  # Jalankan pembagian dan simpan hasil atau tanda pembagian tidak valid.

    if hasil is None:  # Periksa tanda None yang menandakan pembagi bernilai nol.
        print("Tidak bisa membagi dengan nol.")  # Tampilkan pesan khusus untuk pembagian dengan nol.
    else:  # Jalankan cabang ini jika operasi menghasilkan nilai.
        print("Hasil:", hasil)  # Tampilkan hasil operasi kepada pengguna.
