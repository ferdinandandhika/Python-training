# Solusi 4.2 - Encapsulation


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


class KartuMember:
    MIN_TOPUP = 10_000

    def __init__(self, nomor, nama):
        self.nomor = nomor
        self.nama = nama          # lewat setter, langsung tervalidasi
        self._saldo = 0
        self._poin = 0

    @property
    def saldo(self):
        return self._saldo

    @property
    def poin(self):
        return self._poin

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        nilai = str(nilai).strip().title()
        if not nilai:
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nilai

    @property
    def level(self):
        if self._poin >= 50:
            return "Gold"
        if self._poin >= 20:
            return "Silver"
        return "Bronze"

    def top_up(self, jumlah):
        if jumlah < self.MIN_TOPUP:
            raise ValueError(f"Top up minimal {rupiah(self.MIN_TOPUP)}")
        self._saldo += jumlah

    def bayar(self, jumlah):
        if jumlah > self._saldo:
            raise ValueError(f"Saldo kurang. Saldo {rupiah(self._saldo)}, tagihan {rupiah(jumlah)}")
        self._saldo -= jumlah
        self._poin += jumlah // 10_000

    def __str__(self):
        return f"[{self.nomor}] {self.nama} | saldo {rupiah(self.saldo)} | {self.poin} poin | {self.level}"


kartu = KartuMember("M001", "  rina  ")
kartu.top_up(300_000)
for tagihan in [75_000, 120_000, 50_000]:
    kartu.bayar(tagihan)
    print(f"Bayar {rupiah(tagihan):>11} -> {kartu}")

for aksi in [lambda: kartu.bayar(500_000), lambda: kartu.top_up(5_000),
             lambda: setattr(kartu, "nama", "  ")]:
    try:
        aksi()
    except ValueError as e:
        print("  Ditolak:", e)
try:
    kartu.saldo = 5_000_000
except AttributeError:
    print("  Ditolak: saldo tidak bisa diubah langsung (property tanpa setter)")
