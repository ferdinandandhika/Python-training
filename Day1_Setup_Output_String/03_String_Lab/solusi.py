# Solusi 1.3 - String Lab
nama = "   bUDi   santoso "  # Siapkan contoh nama dengan spasi dan kapitalisasi tidak beraturan untuk latihan merapikan teks.
email = "  BUDI.Santoso@Mail.COM "  # Siapkan contoh email dengan spasi dan huruf campuran untuk latihan normalisasi.
hp = "081234567890"  # Simpan nomor HP sebagai teks agar angka nol di depannya tidak hilang.
kode = "ORD-2026-BDG-0042"  # Siapkan kode pesanan yang bagian-bagiannya dipisahkan tanda hubung.
total = 1250000  # Simpan total belanja sebagai bilangan bulat karena nilainya akan dipakai untuk format rupiah.
diskon = 0.15  # Simpan nilai diskon sebagai desimal, yaitu 0,15 atau 15 persen.
kartu = "4111222233334444"  # Simpan nomor kartu sebagai teks supaya mudah mengambil dan menyamarkan digitnya.

nama_rapi = " ".join(nama.split()).title()  # Pecah nama untuk merapikan spasi berlebih, gabungkan dengan satu spasi, lalu rapikan kapitalisasi.
email_rapi = email.strip().lower()  # Buang spasi tepi dan ubah email menjadi huruf kecil agar formatnya seragam.
username = email_rapi.split("@")[0]  # Pisahkan email pada tanda @ lalu ambil bagian pertama sebagai nama pengguna.
hp_rapi = f"{hp[0:4]}-{hp[4:8]}-{hp[8:]}"  # Ambil potongan nomor HP per kelompok dan sisipkan tanda hubung agar mudah dibaca.
_, tahun, kota, nomor = kode.split("-")  # Pisahkan kode pada tanda hubung; abaikan awalan dan simpan tahun, kota, serta nomor.
total_rp = "Rp " + f"{total:,}".replace(",", ".")  # Tambahkan pemisah ribuan lalu ubah koma menjadi titik sesuai format Rupiah yang digunakan.
diskon_persen = f"{diskon:.0%}"  # Ubah nilai desimal diskon menjadi persen tanpa angka di belakang koma.
kartu_sensor = "*" * (len(kartu) - 4) + kartu[-4:]  # Ganti semua digit kecuali empat digit terakhir dengan tanda bintang.

print("1. Nama      :", nama_rapi)  # Tampilkan nama yang sudah dirapikan beserta nomor urut informasinya.
print("2. Email     :", email_rapi)  # Tampilkan email yang sudah dibuat konsisten dalam huruf kecil.
print("3. Username  :", username)  # Tampilkan nama pengguna yang diambil dari bagian sebelum tanda @.
print("4. HP        :", hp_rapi)  # Tampilkan nomor HP dengan pemisah agar kelompok angkanya mudah dibaca.
print(f"5. Kode      : tahun={tahun}, kota={kota}, nomor={int(nomor)}")  # Tampilkan isi kode dan ubah nomor teks menjadi bilangan bulat saat dicetak.
print("6. Total     :", total_rp)  # Tampilkan nilai belanja dengan format Rupiah.
print("7. Diskon    :", diskon_persen)  # Tampilkan diskon dalam bentuk persentase.
print("8. Kartu     :", kartu_sensor)  # Tampilkan nomor kartu yang sudah disamarkan demi menjaga privasi.
