# Solusi 3.2 - Tebak Angka
import random  # Impor modul untuk memilih angka rahasia secara acak.

rahasia = random.randint(1, 100)  # Pilih angka rahasia secara acak, termasuk angka 1 dan 100.
kesempatan = 7  # Tetapkan jumlah tebakan valid yang boleh dilakukan pemain.
percobaan = 0  # Mulai penghitung tebakan valid dari nol.
menang = False  # Tandai bahwa pemain belum berhasil menebak angka rahasia.
print("Aku sudah memilih angka 1 sampai 100. Kamu punya 7 kesempatan.")  # Beri tahu aturan permainan sebelum mulai.
while kesempatan > 0:  # Jalankan permainan selama pemain masih memiliki kesempatan.
    teks = input(f"[{kesempatan} sisa] Tebakanmu: ").strip().lower()  # Baca tebakan, lalu rapikan spasi dan huruf.
    if teks == "menyerah":  # Periksa apakah pemain memilih berhenti dengan kata yang ditentukan.
        break  # Keluar dari perulangan tanpa melanjutkan tebakan.
    if not teks.isdigit():  # Pastikan masukan hanya berisi digit agar bisa diubah menjadi bilangan bulat.
        print("  Ketik angka, kesempatan tidak berkurang.")  # Jelaskan kesalahan tanpa mengurangi jatah tebakan.
        continue  # Kembali meminta masukan berikutnya dari awal perulangan.
    tebakan = int(teks)  # Ubah teks angka menjadi bilangan bulat untuk dibandingkan.
    percobaan += 1  # Hitung satu tebakan valid yang baru dilakukan.
    kesempatan -= 1  # Kurangi sisa kesempatan karena tebakan valid sudah dipakai.
    if tebakan < rahasia:  # Periksa apakah tebakan berada di bawah angka rahasia.
        print("  Terlalu kecil.")  # Beri petunjuk agar pemain mencoba angka yang lebih besar.
    elif tebakan > rahasia:  # Periksa apakah tebakan berada di atas angka rahasia.
        print("  Terlalu besar.")  # Beri petunjuk agar pemain mencoba angka yang lebih kecil.
    else:  # Jalankan cabang ini jika tebakan sama dengan angka rahasia.
        menang = True  # Catat bahwa pemain berhasil menang.
        print(f"  BENAR! Kamu menebak dalam {percobaan} kali.")  # Tampilkan keberhasilan dan jumlah tebakan yang dipakai.
        break  # Akhiri permainan karena angka sudah berhasil ditebak.
if not menang:  # Periksa apakah permainan berakhir tanpa pemain menebak dengan benar.
    print(f"Angka rahasianya adalah {rahasia}.")  # Ungkap angka rahasia ketika pemain belum menang.
