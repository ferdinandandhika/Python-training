# Contoh module bawaan Python
import math
import os
import random
from datetime import date, timedelta

print("Akar 81        :", math.sqrt(81))
print("Angka acak     :", random.randint(1, 10))
print("Hari ini       :", date.today())
print("7 hari lagi    :", date.today() + timedelta(days=7))
print("Folder kerja   :", os.getcwd())
# TODO: tampilkan 3 angka acak 1-100, tanggal 30 hari lagi, dan akar 144
