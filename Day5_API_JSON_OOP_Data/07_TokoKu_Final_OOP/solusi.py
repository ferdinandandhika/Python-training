# TokoKu FINAL OOP - aplikasi kasir lengkap
from pathlib import Path

from tokoku_oop import KartuDebit, Keranjang, Minuman, QRIS, Toko, Tunai, ambil_kurs_usd, rupiah

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


def pilih_metode():
    pilihan = input("Bayar dengan 1 Tunai / 2 QRIS / 3 Kartu Debit: ").strip()
    if pilihan == "2":
        return QRIS()
    if pilihan == "3":
        return KartuDebit(input("PIN: ").strip())
    return Tunai(minta_angka("Uang diterima: "))


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
    if not keranjang:
        print("Transaksi dibatalkan.")
        return
    member = input("Member? (y/n): ").strip().lower() == "y"
    print(f"Total bayar: {rupiah(toko.hitung(keranjang, member)['total'])}")
    rincian, hasil = toko.checkout(keranjang, pilih_metode(), member)
    if not hasil.berhasil:
        print(f"Pembayaran gagal: {hasil.pesan}. Transaksi tidak disimpan.")
        return
    print("=" * LEBAR)
    print(toko.nama.upper().center(LEBAR))
    print("=" * LEBAR)
    print(keranjang)
    print("-" * LEBAR)
    for label, nilai in [("Subtotal", rupiah(rincian["subtotal"])), ("Diskon", "-" + rupiah(rincian["diskon"])),
                         ("Pajak 11%", rupiah(rincian["pajak"])), ("TOTAL", rupiah(rincian["total"])),
                         (hasil.metode, rupiah(hasil.dibayar))]:
        print(f"{label:<24}{nilai:>16}")
    if hasil.kembalian:
        print(f"{'Kembalian':<24}{rupiah(hasil.kembalian):>16}")
    print("=" * LEBAR)


def laporan(toko):
    lap = toko.laporan()
    if not lap["jumlah"]:
        print("  Belum ada transaksi. Jalankan buat_data_contoh.py atau buat transaksi baru.")
        return
    print(f"  Jumlah transaksi : {lap['jumlah']}")
    print(f"  Omzet            : {rupiah(lap['omzet'])}  (sebelum diskon dan pajak)")
    print(f"  Menu terlaris    : {lap['menu_terlaris']}")
    print(f"  Jam tersibuk     : {lap['jam_tersibuk']:02d}.00")
    for jenis, nilai in lap["per_jenis"].items():
        print(f"  Omzet {jenis:<10} : {rupiah(nilai)}")
    for metode, n in lap["per_metode"].items():
        print(f"  {metode:<16} : {n} transaksi")


def harga_usd(toko):
    kurs, sumber = ambil_kurs_usd()
    print(f"  Kurs dari {sumber}: 1 IDR = {kurs:.7f} USD")
    for p in toko.katalog.values():
        print(f"  {p.deskripsi():<20} {rupiah(p.harga_satuan()):>10}  USD {p.harga_satuan() * kurs:.2f}")


def main():
    toko = Toko.dari_csv(FOLDER / "menu.csv", file_transaksi=FOLDER / "transaksi.csv")
    aksi = {"1": transaksi, "2": laporan,
            "3": lambda t: print(f"  Dashboard: {t.dashboard(FOLDER / 'output')}"), "4": harga_usd}
    while True:
        print("\n=== TOKOKU ===")
        print("1. Transaksi baru\n2. Laporan penjualan\n3. Buat grafik dashboard")
        print("4. Lihat harga dalam USD\n5. Keluar")
        pilihan = input("Pilih: ").strip()
        if pilihan == "5":
            print("Sampai jumpa!")
            break
        if pilihan in aksi:
            try:
                aksi[pilihan](toko)
            except Exception as e:
                print(f"  Terjadi error: {type(e).__name__}: {e}")
        else:
            print("  Pilihan tidak dikenal.")


if __name__ == "__main__":
    main()
