# Solusi 2.2 - Error Handling


def minta_angka(pesan, boleh_nol=False):
    while True:
        try:
            angka = int(input(pesan).replace(".", "").strip())
        except ValueError:
            print("  Harus angka, coba lagi.")
            continue
        if angka < 0 or (angka == 0 and not boleh_nol):
            print("  Angka harus lebih dari nol.")
            continue
        return angka


total = minta_angka("Total tagihan : ")
orang = minta_angka("Jumlah orang  : ", boleh_nol=True)
try:
    per_orang = total / orang
except ZeroDivisionError:
    print("  Jumlah orang tidak boleh nol, dianggap 1 orang.")
    per_orang = total
else:
    print("  Perhitungan berhasil.")
finally:
    print("  Proses selesai.")
print(f"Per orang     : Rp {per_orang:,.0f}".replace(",", "."))
