# Solusi 4.2 - Encapsulation Sederhana


class Dompet:
    def __init__(self, pemilik, saldo_awal):  # Inisialisasi pemilik dan saldo saat objek Dompet dibuat.
        self.pemilik = pemilik  # Simpan nama pemilik sebagai atribut instance yang dapat dibaca.
        self._saldo = saldo_awal  # Awalan garis bawah menandai saldo sebagai atribut internal yang sebaiknya diakses melalui antarmuka kelas.

    @property  # Dekorator mengubah metode saldo menjadi properti baca yang dipakai dengan sintaks atribut.
    def saldo(self):  # Jadikan metode ini properti agar saldo dapat dibaca seperti atribut tanpa memanggil tanda kurung.
        return self._saldo  # Berikan nilai saldo internal sebagai nilai baca properti saldo.

    def setor(self, jumlah):  # Sediakan metode untuk menambah saldo melalui perilaku dompet.
        self._saldo += jumlah  # Tambahkan jumlah setoran langsung ke saldo internal dompet ini.


dompet = Dompet("Rina", 100_000)  # Buat dompet contoh milik Rina dengan saldo awal seratus ribu.
print(f"Saldo awal {dompet.pemilik}: Rp {dompet.saldo:,}".replace(",", "."))  # Tampilkan pemilik dan saldo awal dengan pemisah ribuan bergaya Indonesia.

dompet.setor(50_000)  # Gunakan metode setor agar saldo bertambah lima puluh ribu.
print(f"Saldo setelah setor: Rp {dompet.saldo:,}".replace(",", "."))  # Tampilkan saldo setelah setoran untuk memperlihatkan perubahan.
