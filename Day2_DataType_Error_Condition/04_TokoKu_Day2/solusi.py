# TokoKu Day 2 - Validasi dan Diskon
from datetime import datetime

PAJAK = 0.11
LEBAR = 34


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


def minta_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            if angka <= 0:
                print("  Harus lebih dari nol.")
                continue
            return angka
        except ValueError:
            print("  Harus angka, coba lagi.")


nama = input("Nama pelanggan : ").strip().title()
menu = input("Menu           : ").strip().title()
harga = minta_angka("Harga          : ")
jumlah = minta_angka("Jumlah         : ")
member = input("Member? (y/n)  : ").strip().lower() == "y"

subtotal = harga * jumlah
if subtotal >= 200_000:
    persen = 0.15
elif subtotal >= 100_000:
    persen = 0.10
else:
    persen = 0.0
if member:
    persen += 0.05
diskon = subtotal * persen
pajak = (subtotal - diskon) * PAJAK
total = subtotal - diskon + pajak

print()
print("=" * LEBAR)
print("STRUK TOKOKU".center(LEBAR))
print(datetime.now().strftime("%d-%m-%Y %H:%M").center(LEBAR))
print("=" * LEBAR)
print(f"{menu} x{jumlah}")
print(f"Subtotal        : {rupiah(subtotal)}")
print(f"Diskon ({persen:.0%})    : -{rupiah(diskon)}")
print(f"Pajak (11%)     : {rupiah(pajak)}")
print("-" * LEBAR)
print(f"TOTAL BAYAR     : {rupiah(total)}")
print("=" * LEBAR)
print(f"Terima kasih, {nama}!".center(LEBAR))
