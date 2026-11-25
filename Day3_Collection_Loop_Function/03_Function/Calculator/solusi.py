# Solusi kalkulator dengan beberapa function


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


def tampilkan_menu():
    print("\n=== Kalkulator ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")
    print("===================")


while True:
    tampilkan_menu()
    pilihan = input("Pilih operasi: ")

    if pilihan == "5":
        print("Program selesai.")
        break

    if pilihan not in ("1", "2", "3", "4"):
        print("Pilihan tidak tersedia.")
        continue

    angka_1 = float(input("Angka pertama: "))
    angka_2 = float(input("Angka kedua: "))

    if pilihan == "1":
        hasil = tambah(angka_1, angka_2)
    elif pilihan == "2":
        hasil = kurang(angka_1, angka_2)
    elif pilihan == "3":
        hasil = kali(angka_1, angka_2)
    else:
        hasil = bagi(angka_1, angka_2)

    if hasil is None:
        print("Tidak bisa membagi dengan nol.")
    else:
        print("Hasil:", hasil)
