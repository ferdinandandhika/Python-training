# Latihan 4.2 - Encapsulation Sederhana


class Dompet:
    def __init__(self, pemilik, saldo_awal):
        # TODO 1: simpan pemilik dan saldo sebagai attribute
        #         gunakan nama _saldo untuk saldo internal
        pass

    @property
    def saldo(self):
        # TODO 2: kembalikan saldo internal
        pass

    def setor(self, jumlah):
        # TODO 3: tambahkan jumlah ke saldo internal
        pass


# TODO 4: buat dompet Rina dengan saldo awal 100000
# TODO 5: tampilkan saldo awal, setor 50000, lalu tampilkan saldo terbaru
