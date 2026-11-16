# Solusi 3.3 - Kalkulator dengan Function
riwayat = []


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return None
    return a / b


OPERASI = {"+": tambah, "-": kurang, "*": kali, "/": bagi}


def hitung(a, operator, b):
    fungsi = OPERASI.get(operator)
    return None if fungsi is None else fungsi(a, b)


print("Kalkulator TokoKu. Contoh: 12 * 3 | riwayat | keluar")
while True:
    perintah = input("> ").strip().lower()
    if perintah == "keluar":
        break
    if perintah == "riwayat":
        for i, baris in enumerate(riwayat, start=1):
            print(f"  {i}. {baris}")
        continue
    bagian = perintah.split()
    if len(bagian) != 3:
        print("  Format: angka operator angka")
        continue
    try:
        a, op, b = float(bagian[0]), bagian[1], float(bagian[2])
    except ValueError:
        print("  Angka tidak valid.")
        continue
    hasil = hitung(a, op, b)
    if hasil is None:
        print("  Operator salah atau pembagian dengan nol.")
        continue
    teks = f"{a:g} {op} {b:g} = {hasil:g}"
    riwayat.append(teks)
    print(" ", teks)
print(f"Selesai. Total perhitungan: {len(riwayat)}")
