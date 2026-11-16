# Solusi 2.3 - Batu Kertas Gunting (terbaik dari 3)
import random

pilihan = ["batu", "kertas", "gunting"]
singkatan = {"b": "batu", "k": "kertas", "g": "gunting"}
skor_pemain = skor_komputer = 0
ronde = 1
while ronde <= 3 and skor_pemain < 2 and skor_komputer < 2:
    print(f"\n--- Ronde {ronde} ---")
    pemain = input("Pilih batu/kertas/gunting (b/k/g): ").strip().lower()
    pemain = singkatan.get(pemain, pemain)
    if pemain not in pilihan:
        print("Pilihan tidak valid, ulangi ronde ini.")
        continue
    komputer = random.choice(pilihan)
    print(f"Kamu: {pemain} | Komputer: {komputer}")
    if pemain == komputer:
        print("SERI")
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        print("MENANG")
        skor_pemain += 1
    else:
        print("KALAH")
        skor_komputer += 1
    ronde += 1
print(f"\nSkor akhir  Kamu {skor_pemain} - {skor_komputer} Komputer")
