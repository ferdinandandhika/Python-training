# Solusi 2.3 - Batu Kertas Gunting (satu ronde)
import random  # Mengimpor modul random agar komputer dapat memilih langkah secara acak.

pilihan = ["batu", "kertas", "gunting"]  # Menyimpan semua langkah yang diizinkan dalam satu daftar.
komputer = random.choice(pilihan)  # Memilih satu langkah komputer secara acak dari daftar pilihan.
pemain = input("Pilih batu/kertas/gunting: ").strip().lower()  # Meminta langkah pemain lalu membuang spasi tepi dan menyamakan huruf kecil.

if pemain not in pilihan:  # Memastikan teks pemain cocok dengan salah satu langkah yang diizinkan.
    print("Pilihan tidak valid.")  # Memberi pesan kesalahan jika pemain memasukkan kata di luar daftar.
else:  # Melanjutkan permainan karena pilihan pemain termasuk pilihan yang diizinkan.
    print(f"Kamu: {pemain} | Komputer: {komputer}")  # Menampilkan kedua langkah agar hasil ronde dapat dipahami.
    if pemain == komputer:  # Memeriksa apakah pemain dan komputer memilih langkah yang sama.
        print("SERI")  # Mengumumkan hasil seri saat kedua pilihan sama.
    # Kondisi ini menguji tiga kombinasi yang membuat pilihan pemain mengalahkan pilihan komputer.
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        print("MENANG")  # Mengumumkan kemenangan jika salah satu kombinasi menang pemain terpenuhi.
    else:  # Menangani kombinasi valid yang tidak seri dan tidak memenuhi kondisi menang pemain.
        print("KALAH")  # Mengumumkan kekalahan jika pilihan valid tetapi bukan seri atau kemenangan pemain.
