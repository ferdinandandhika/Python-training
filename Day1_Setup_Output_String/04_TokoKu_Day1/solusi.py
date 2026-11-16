# TokoKu Day 1 - Struk Sederhana
LEBAR = 30

nama = input("Nama pelanggan : ").strip().title()
menu = input("Menu           : ").strip().title()
harga = int(input("Harga          : "))
jumlah = int(input("Jumlah         : "))
total = harga * jumlah


def rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")


print()
print("=" * LEBAR)
print("STRUK TOKOKU".center(LEBAR))
print("=" * LEBAR)
print(f"Pelanggan : {nama}")
print(f"Menu      : {menu}")
print(f"Harga     : {rupiah(harga)}")
print(f"Jumlah    : {jumlah}")
print("-" * LEBAR)
print(f"TOTAL     : {rupiah(total)}")
print("=" * LEBAR)
print(f"Terima kasih, {nama}!".center(LEBAR))
