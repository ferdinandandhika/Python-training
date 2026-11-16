# TokoKu Day 4 OOP - aplikasi kasir yang memakai package tokoku_oop
from pathlib import Path

from tokoku_oop import Keranjang, Minuman, Toko, rupiah

FOLDER = Path(__file__).parent
LEBAR = 40


def minta_angka(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai > 0:
                return nilai
        except ValueError:
            pass
        print("  Masukkan angka lebih dari nol.")


def transaksi(toko):
    keranjang = Keranjang()
    for p in toko.katalog.values():
        print(f"  {p.kode}  {p.deskripsi():<16} {rupiah(p.harga_satuan())}")
    while True:
        kode = input("Kode menu (selesai): ").strip().upper()
        if kode == "SELESAI":
            break
        try:
            produk = toko.cari(kode)
        except KeyError as e:
            print(" ", e.args[0])
            continue
        if isinstance(produk, Minuman):
            ukuran = input("  Ukuran S/M/L [M]: ").strip().upper() or "M"
            produk = produk.dengan_ukuran(ukuran if ukuran in Minuman.TAMBAHAN else "M")
        keranjang.tambah(produk, minta_angka("  Jumlah: "))
        print(f"  Keranjang: {len(keranjang)} item")
    if not keranjang:
        print("Transaksi dibatalkan.")
        return
    member = input("Member? (y/n): ").strip().lower() == "y"
    r = toko.checkout(keranjang, member)
    print("=" * LEBAR)
    print(toko.nama.upper().center(LEBAR))
    print("=" * LEBAR)
    print(keranjang)
    print("-" * LEBAR)
    for label, kunci in [("Subtotal", "subtotal"), ("Diskon", "diskon"), ("Pajak 11%", "pajak"), ("TOTAL", "total")]:
        nilai = rupiah(r[kunci])
        print(f"{label:<24}{'-' + nilai if kunci == 'diskon' else nilai:>16}")
    print("=" * LEBAR)


def main():
    toko = Toko.dari_csv(FOLDER / "menu.csv", file_transaksi=FOLDER / "transaksi.csv")
    while True:
        cmd = input(f"\n[{toko.nama}] baru | laporan | keluar: ").strip().lower()
        if cmd == "baru":
            transaksi(toko)
        elif cmd == "laporan":
            lap = toko.laporan()
            print(f"  Transaksi: {lap['jumlah']} | Omzet sebelum pajak: {rupiah(lap['omzet'])}")
        elif cmd == "keluar":
            break


if __name__ == "__main__":
    main()
