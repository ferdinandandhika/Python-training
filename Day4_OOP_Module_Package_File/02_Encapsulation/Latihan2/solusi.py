# Solusi 4.2 - Encapsulation: Setor dan Tarik


class Dompet:
    def __init__(self, pemilik, saldo_awal):  # Inisialisasi objek dompet dengan nama pemilik dan saldo awal.
        self.pemilik = pemilik  # Simpan pemilik sebagai informasi yang melekat pada instance dompet.
        self._saldo = saldo_awal  # Simpan saldo sebagai atribut internal yang dikelola melalui metode kelas.

    @property  # Dekorator menyediakan akses saldo dengan sintaks atribut sambil tetap mengendalikan cara membacanya.
    def saldo(self):  # Sediakan akses baca saldo menggunakan sintaks properti.
        return self._saldo  # Kembalikan saldo internal tanpa membuka perubahan langsung melalui setter.

    def setor(self, jumlah):  # Definisikan operasi untuk memasukkan uang ke dalam dompet.
        self._saldo += jumlah  # Tambahkan uang yang disetor ke saldo saat ini.

    def tarik(self, jumlah):  # Definisikan operasi penarikan dan laporkan apakah penarikan berhasil.
        if jumlah > self._saldo:  # Periksa saldo terlebih dahulu supaya penarikan melebihi saldo dapat ditolak.
            return False  # Kembalikan penanda gagal tanpa mengubah saldo.
        self._saldo -= jumlah  # Kurangi saldo karena jumlah penarikan tidak melebihi saldo.
        return True  # Kembalikan penanda berhasil agar pemanggil dapat memilih pesan yang sesuai.


nama = input("Nama pemilik: ").strip()  # Minta nama dari pengguna lalu hapus spasi di awal dan akhir masukan.
dompet = Dompet(nama, 100_000)  # Buat dompet pengguna dengan saldo awal seratus ribu.
print(f"Saldo awal {dompet.pemilik}: Rp {dompet.saldo:,}".replace(",", "."))  # Tampilkan identitas pemilik dan saldo awal dalam format rupiah.

jumlah_setor = int(input("Jumlah setor: "))  # Baca masukan setoran lalu ubah teks menjadi bilangan bulat untuk perhitungan.
dompet.setor(jumlah_setor)  # Tambahkan setoran melalui metode dompet agar perubahan saldo terkelola oleh kelas.
print(
    f"Setor Rp {jumlah_setor:,} berhasil. Saldo: Rp {dompet.saldo:,}".replace(",", ".")
)  # Beri tahu jumlah setoran dan saldo terbaru setelah transaksi setor.

jumlah_tarik = int(input("Jumlah penarikan: "))  # Baca jumlah penarikan dan ubah nilainya menjadi bilangan bulat.
if dompet.tarik(jumlah_tarik):  # Gunakan nilai True/False dari metode tarik untuk menentukan hasil transaksi.
    print(
        f"Tarik Rp {jumlah_tarik:,} berhasil. Saldo: Rp {dompet.saldo:,}".replace(",", ".")
    )  # Tampilkan pesan berhasil dan saldo baru bila penarikan memenuhi saldo yang tersedia.
else:  # Jalankan cabang ini ketika metode tarik menolak transaksi karena saldo tidak mencukupi.
    print(
        f"Tarik Rp {jumlah_tarik:,} gagal. Saldo: Rp {dompet.saldo:,}".replace(",", ".")
    )  # Tampilkan pesan gagal dan saldo yang tetap tidak berubah.

