# Solusi 3.1B - Mengenal List

menu = []  # Buat list kosong untuk menampung nama-nama menu yang dimasukkan pengguna.
menu.append(input("Nama menu 1: ").strip())  # Minta menu pertama, hapus spasi di awal/akhir, lalu simpan ke list.
menu.append(input("Nama menu 2: ").strip())  # Minta menu kedua dan tambahkan hasilnya ke list yang sama.
menu.append(input("Nama menu 3: ").strip())  # Minta menu ketiga agar list berisi tiga nama menu.

print("Isi list:", menu)  # Tampilkan seluruh isi list untuk memperlihatkan data yang sudah terkumpul.

nomor = 1  # Siapkan nomor urut pertama untuk menandai setiap nama saat ditampilkan.
for nama_menu in menu:  # Ambil setiap nama dari list secara bergantian.
    print(nomor, nama_menu)  # Tampilkan nomor urut bersama nama menu yang sedang diproses.
    nomor += 1  # Naikkan nomor supaya menu berikutnya memakai urutan selanjutnya.