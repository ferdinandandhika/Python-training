# Python Cheat Sheet - Pegangan Peserta

## Output dan input
```python
print("Halo")
nama = input("Nama: ")            # input selalu berupa str
umur = int(input("Umur: "))       # ubah ke angka
print(f"Halo {nama}, umur {umur}")
```

## String
```python
s = "  Python Itu Seru  "
s.strip()   s.upper()   s.lower()   s.title()
s.replace("Seru", "Mudah")   s.split()   len(s)
"-".join(["a", "b"])   s[0]   s[-1]   s[0:6]
f"{1234567:,}"   f"{0.256:.1%}"   f"{3.14159:.2f}"
```

## Tipe data dan kondisi
```python
int("10")  float("3.5")  str(10)  type(x)  isinstance(x, int)
if nilai >= 85: ...
elif nilai >= 70: ...
else: ...
and  or  not  ==  !=  >=  <=  in
```

## Error
```python
try:
    angka = int(teks)
except ValueError:
    print("Bukan angka")
finally:
    print("selesai")
```

## Collection, loop, function
```python
daftar = [1, 2, 3];  daftar.append(4)
data = {"nama": "Andi"};  data.get("kota", "-")
for k, v in data.items(): ...
for i, item in enumerate(daftar, start=1): ...
while syarat: ...      break    continue
def hitung_total(harga, qty=1):
    return harga * qty
```

## OOP (Day 4 dan Day 5)
```python
class Produk:
    jumlah = 0                           # class attribute
    def __init__(self, nama, harga):     # constructor
        self.nama = nama                 # instance attribute
        self._harga = harga              # "private" (konvensi)
        Produk.jumlah += 1
    @property
    def harga(self):                     # getter
        return self._harga
    @harga.setter
    def harga(self, nilai):              # setter + validasi
        if nilai <= 0:
            raise ValueError("Harga harus positif")
        self._harga = nilai
    def __str__(self):                   # tampilan saat print()
        return f"{self.nama} Rp {self._harga:,}"

class Minuman(Produk):                   # inheritance
    def __init__(self, nama, harga, ukuran="M"):
        super().__init__(nama, harga)
        self.ukuran = ukuran

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Item:
    nama: str
    qty: int = 1

class Pembayaran(ABC):
    @abstractmethod
    def proses(self, total): ...
```

## File dan package
```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("baris\n")
import csv, json
```
```
python -m venv .venv
pip install pandas
pip freeze > requirements.txt
python -m unittest -v
```

## Pandas cepat
```python
import pandas as pd
df = pd.read_csv("file.csv")
df.head()  df.info()  df.describe()
df[df["Kota"] == "Jakarta"]
df.groupby("Kategori")["Total"].sum()
```
