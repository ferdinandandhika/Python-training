# Latihan 2.1 - Kalkulator IPK
from datetime import date

nama = "Siti Rahma"
tanggal_lahir = date(2005, 3, 14)
# (nama mata kuliah, nilai angka dalam bentuk teks, sks)
matkul = [
    ("Algoritma", "85", 3),
    ("Basis Data", "78", 3),
    ("Statistika", "68.5", 2),
    ("Bahasa Inggris", "91", 2),
]

# TODO 1: hitung umur dari tanggal_lahir sampai hari ini
# TODO 2: buat variabel total_bobot dan total_sks bernilai 0
# TODO 3: untuk setiap mata kuliah: ubah nilai teks ke float, tentukan huruf dan
#         bobot dengan if/elif/else, jumlahkan bobot * sks dan sks, tampilkan rincian
# TODO 4: hitung IPK = total_bobot / total_sks, bulatkan 2 desimal
# TODO 5: tentukan predikat
