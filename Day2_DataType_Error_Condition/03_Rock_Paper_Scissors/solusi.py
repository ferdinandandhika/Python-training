# Solusi 2.3 - Batu Kertas Gunting (satu ronde)
import random

pilihan = ["batu", "kertas", "gunting"]
komputer = random.choice(pilihan)
pemain = input("Pilih batu/kertas/gunting: ").strip().lower()

if pemain not in pilihan:
    print("Pilihan tidak valid.")
else:
    print(f"Kamu: {pemain} | Komputer: {komputer}")
    if pemain == komputer:
        print("SERI")
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        print("MENANG")
    else:
        print("KALAH")
