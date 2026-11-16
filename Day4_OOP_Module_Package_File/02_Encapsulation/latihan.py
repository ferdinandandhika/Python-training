# Latihan 4.2 - Encapsulation


class KartuMember:
    MIN_TOPUP = 10_000

    def __init__(self, nomor, nama):
        self.nomor = nomor
        self._nama = nama
        self._saldo = 0
        self._poin = 0

    # TODO 1: @property saldo -> return self._saldo (tanpa setter)
    # TODO 2: @property poin
    # TODO 3: @property nama dan @nama.setter (tolak nama kosong dengan ValueError)
    # TODO 4: @property level: poin >= 50 Gold, >= 20 Silver, selainnya Bronze

    def top_up(self, jumlah):
        pass  # TODO 5: tolak bila < MIN_TOPUP, lalu tambah saldo

    def bayar(self, jumlah):
        pass  # TODO 6: tolak bila saldo kurang, kurangi saldo, tambah poin jumlah // 10_000


kartu = KartuMember("M001", "Rina")
# TODO 7: top up 300.000, bayar 75.000, 120.000, 50.000, lalu uji 4 penolakan
