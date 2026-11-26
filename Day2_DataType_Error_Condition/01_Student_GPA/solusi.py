# Solusi 2.1 - Menentukan Nilai Mata Kuliah

nama = input("Nama mahasiswa: ")  # Meminta nama mahasiswa agar hasil penilaian dapat ditampilkan bersama identitasnya.
mata_kuliah = input("Mata kuliah: ")  # Meminta nama mata kuliah agar nilai yang dihitung jelas merujuk ke pelajaran tertentu.
nilai_teks = input("Nilai angka: ")  # Menerima nilai sebagai teks karena fungsi input selalu menghasilkan data bertipe string.
nilai = float(nilai_teks)  # Mengubah teks nilai menjadi angka desimal supaya bisa dibandingkan dengan batas nilai.

if nilai >= 85:  # Memeriksa batas tertinggi lebih dahulu agar nilai 85 ke atas mendapat kategori A.
    nilai_huruf = "A"  # Menyimpan huruf A ketika syarat pada if terpenuhi.
elif nilai >= 75:  # Memeriksa batas B hanya jika syarat A tidak terpenuhi.
    nilai_huruf = "B"  # Menyimpan huruf B untuk nilai yang memenuhi batas ini.
elif nilai >= 65:  # Memeriksa batas C setelah kategori A dan B gagal.
    nilai_huruf = "C"  # Menyimpan huruf C untuk nilai yang memenuhi batas ini.
elif nilai >= 50:  # Memeriksa batas D setelah kategori yang lebih tinggi gagal.
    nilai_huruf = "D"  # Menyimpan huruf D untuk nilai yang memenuhi batas ini.
else:  # Menangani semua nilai yang tidak mencapai batas nilai D.
    nilai_huruf = "E"  # Memberi kategori E jika nilai tidak memenuhi batas kategori sebelumnya.

print(f"Mahasiswa : {nama}")  # Menampilkan nama mahasiswa dengan format label yang mudah dibaca.
print(f"Mata kuliah: {mata_kuliah}")  # Menampilkan nama mata kuliah yang dimasukkan.
print(f"Nilai     : {nilai}")  # Menampilkan nilai angka setelah dikonversi menjadi float.
print(f"Nilai huruf: {nilai_huruf}")  # Menampilkan kategori huruf hasil pemeriksaan kondisi.
