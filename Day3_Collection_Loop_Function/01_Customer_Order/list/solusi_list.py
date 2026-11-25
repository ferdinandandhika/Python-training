# Solusi 3.1B - Mengenal List

menu = []
menu.append(input("Nama menu 1: ").strip())
menu.append(input("Nama menu 2: ").strip())
menu.append(input("Nama menu 3: ").strip())

print("Isi list:", menu)

nomor = 1
for nama_menu in menu:
    print(nomor, nama_menu)
    nomor += 1