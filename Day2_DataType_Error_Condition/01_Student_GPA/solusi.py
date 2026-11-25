# Solusi 2.1 - Menentukan Nilai Mata Kuliah

nama = input("Nama mahasiswa: ")
mata_kuliah = input("Mata kuliah: ")
nilai_teks = input("Nilai angka: ")
nilai = float(nilai_teks)

if nilai >= 85:
    nilai_huruf = "A"
elif nilai >= 75:
    nilai_huruf = "B"
elif nilai >= 65:
    nilai_huruf = "C"
elif nilai >= 50:
    nilai_huruf = "D"
else:
    nilai_huruf = "E"

print(f"Mahasiswa : {nama}")
print(f"Mata kuliah: {mata_kuliah}")
print(f"Nilai     : {nilai}")
print(f"Nilai huruf: {nilai_huruf}")
