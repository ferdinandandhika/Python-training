# Latihan 4.2 - Encapsulation: Setor dan Tarik


class Dompet:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        # TODO 1: simpan saldo sebagai data internal

    @property
    def saldo(self):
        # TODO 2: kembalikan saldo internal
        pass

    def setor(self, jumlah):
        # TODO 3: tambahkan jumlah ke saldo
        pass

    def tarik(self, jumlah):
        # TODO 4: jika saldo kurang, kembalikan False tanpa mengubah saldo
        # TODO 5: jika saldo cukup, kurangi saldo dan kembalikan True
        pass


nama = input("Nama pemilik: ").strip()
dompet = Dompet(nama, 100_000)
print(f"Saldo awal {dompet.pemilik}: Rp {dompet.saldo:,}".replace(",", "."))

# TODO 6: minta jumlah setoran, ubah menjadi int, panggil setor(),
#         lalu tampilkan jumlah setoran dan saldo terbaru

# TODO 7: minta jumlah penarikan dan ubah menjadi int
# TODO 8: gunakan if/else berdasarkan hasil dompet.tarik()
#         tampilkan berhasil/gagal dan saldo terbaru
