# Solusi 2.1 - Kalkulator IPK
from datetime import date

nama = "Siti Rahma"
tanggal_lahir = date(2005, 3, 14)
matkul = [
    ("Algoritma", "85", 3),
    ("Basis Data", "78", 3),
    ("Statistika", "68.5", 2),
    ("Bahasa Inggris", "91", 2),
]

hari_ini = date.today()
umur = hari_ini.year - tanggal_lahir.year - (
    (hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day))
print(f"Mahasiswa : {nama} (umur {umur} tahun)")
print("-" * 45)

total_bobot = 0.0
total_sks = 0
for nama_mk, nilai_teks, sks in matkul:
    nilai = float(nilai_teks)
    if nilai >= 85:
        huruf, bobot = "A", 4.0
    elif nilai >= 75:
        huruf, bobot = "B", 3.0
    elif nilai >= 65:
        huruf, bobot = "C", 2.0
    elif nilai >= 50:
        huruf, bobot = "D", 1.0
    else:
        huruf, bobot = "E", 0.0
    total_bobot += bobot * sks
    total_sks += sks
    print(f"{nama_mk:<16} {nilai:>5}  {huruf}  {bobot} x {sks} SKS")

ipk = round(total_bobot / total_sks, 2)
if ipk >= 3.5:
    predikat = "Cum Laude"
elif ipk >= 3.0:
    predikat = "Sangat Memuaskan"
elif ipk >= 2.5:
    predikat = "Memuaskan"
else:
    predikat = "Cukup"
print("-" * 45)
print(f"Total SKS : {total_sks}")
print(f"IPK       : {ipk:.2f}")
print(f"Predikat  : {predikat}")
