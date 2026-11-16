# Solusi 3.2 - Tebak Angka
import random

rahasia = random.randint(1, 100)
kesempatan = 7
percobaan = 0
menang = False
print("Aku sudah memilih angka 1 sampai 100. Kamu punya 7 kesempatan.")
while kesempatan > 0:
    teks = input(f"[{kesempatan} sisa] Tebakanmu: ").strip().lower()
    if teks == "menyerah":
        break
    if not teks.isdigit():
        print("  Ketik angka, kesempatan tidak berkurang.")
        continue
    tebakan = int(teks)
    percobaan += 1
    kesempatan -= 1
    if tebakan < rahasia:
        print("  Terlalu kecil.")
    elif tebakan > rahasia:
        print("  Terlalu besar.")
    else:
        menang = True
        print(f"  BENAR! Kamu menebak dalam {percobaan} kali.")
        break
if not menang:
    print(f"Angka rahasianya adalah {rahasia}.")
