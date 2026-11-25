# TokoKu Day 3 - Keranjang Belanja
PAJAK = 0.11
LEBAR = 38
MENU = {
    "K01": {"nama": "Kopi Susu Aren", "harga": 25000},
    "K02": {"nama": "Americano", "harga": 22000},
    "T01": {"nama": "Matcha Latte", "harga": 28000},
    "F01": {"nama": "Croissant", "harga": 18000},
    "F02": {"nama": "Cheesecake", "harga": 32000},
}


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


def tampilkan_menu():
    print("MENU TOKOKU")
    for kode, info in MENU.items():
        print(f"  {kode}  {info['nama']:<16} {rupiah(info['harga'])}")


def tambah_ke_keranjang(keranjang, kode, qty):
    info = MENU[kode]
    barang = {"nama": info["nama"], "harga": info["harga"], "qty": qty}
    keranjang.append(barang)


def cetak_struk(keranjang):
    subtotal = 0

    print("\n" + "=" * LEBAR)
    print("STRUK TOKOKU".center(LEBAR))
    print("=" * LEBAR)

    for barang in keranjang:
        total_barang = barang["harga"] * barang["qty"]
        subtotal += total_barang
        print(f"{barang['nama']:<20} x{barang['qty']:<3} {rupiah(total_barang):>12}")

    if subtotal >= 200_000:
        persen_diskon = 0.15
    elif subtotal >= 100_000:
        persen_diskon = 0.10
    else:
        persen_diskon = 0

    diskon = subtotal * persen_diskon
    setelah_diskon = subtotal - diskon
    pajak = setelah_diskon * PAJAK
    total = setelah_diskon + pajak

    print("-" * LEBAR)
    print(f"Subtotal     : {rupiah(subtotal)}")
    print(f"Diskon       : -{rupiah(diskon)}")
    print(f"Pajak (11%)  : {rupiah(pajak)}")
    print(f"TOTAL BAYAR  : {rupiah(total)}")
    print("=" * LEBAR)


keranjang = []
tampilkan_menu()

while True:
    kode = input("\nKode barang (atau selesai): ").strip().upper()
    if kode == "SELESAI":
        break

    if kode not in MENU:
        print("Kode barang tidak ditemukan.")
        continue

    try:
        qty = int(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka bulat.")
        continue

    if qty <= 0:
        print("Jumlah harus lebih dari nol.")
        continue

    tambah_ke_keranjang(keranjang, kode, qty)

if keranjang:
    cetak_struk(keranjang)
else:
    print("Keranjang kosong. Transaksi dibatalkan.")
