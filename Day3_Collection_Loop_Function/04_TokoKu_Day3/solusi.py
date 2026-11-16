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
    for item in keranjang:
        if item["kode"] == kode:
            item["qty"] += qty
            return
    info = MENU[kode]
    keranjang.append({"kode": kode, "nama": info["nama"], "harga": info["harga"], "qty": qty})


def hitung_total(keranjang, member=False):
    subtotal = sum(i["harga"] * i["qty"] for i in keranjang)
    persen = 0.15 if subtotal >= 200_000 else 0.10 if subtotal >= 100_000 else 0.0
    if member:
        persen += 0.05
    diskon = subtotal * persen
    pajak = (subtotal - diskon) * PAJAK
    return {"subtotal": subtotal, "persen": persen, "diskon": diskon, "pajak": pajak,
            "total": subtotal - diskon + pajak}


def cetak_struk(keranjang, r):
    print("=" * LEBAR)
    print("STRUK TOKOKU".center(LEBAR))
    print("=" * LEBAR)
    for i in keranjang:
        print(f"{i['nama']:<16} x{i['qty']:<3} {rupiah(i['harga'] * i['qty']):>15}")
    print("-" * LEBAR)
    print(f"{'Subtotal':<20}{rupiah(r['subtotal']):>18}")
    print(f"{'Diskon ' + format(r['persen'], '.0%'):<20}{'-' + rupiah(r['diskon']):>18}")
    print(f"{'Pajak 11%':<20}{rupiah(r['pajak']):>18}")
    print(f"{'TOTAL':<20}{rupiah(r['total']):>18}")
    print("=" * LEBAR)


def main():
    keranjang = []
    tampilkan_menu()
    while True:
        kode = input("Kode menu (atau selesai): ").strip().upper()
        if kode == "SELESAI":
            break
        if kode not in MENU:
            print("  Kode tidak ada di menu.")
            continue
        try:
            qty = int(input("Jumlah: "))
        except ValueError:
            print("  Jumlah harus angka.")
            continue
        if qty <= 0:
            print("  Jumlah harus lebih dari nol.")
            continue
        tambah_ke_keranjang(keranjang, kode, qty)
    if not keranjang:
        print("Keranjang kosong, transaksi dibatalkan.")
        return
    member = input("Member? (y/n): ").strip().lower() == "y"
    cetak_struk(keranjang, hitung_total(keranjang, member))


if __name__ == "__main__":
    main()
