# Latihan 4.3 - Inheritance dan Polymorphism

| Class | Attribute tambahan | Aturan harga_akhir(qty) |
|---|---|---|
| `Produk` (induk) | kode, nama, harga | harga x qty |
| `Minuman` | ukuran S/M/L, es | + 0 / 3.000 / 6.000 per cup |
| `Makanan` | dihangatkan | + 2.000 per porsi bila dihangatkan |
| `Merchandise` | - | diskon 10% bila beli >= 3 |

## Langkah
1. Buat class anak dengan `super().__init__(...)`.
2. **Override** `harga_akhir()` dan `deskripsi()` di setiap anak.
3. Simpan object berbeda jenis dalam satu list, lalu loop:
   `produk.harga_akhir(qty)` -> inilah **polymorphism**.
4. Hitung item per jenis dengan `isinstance()`.

## Diskusi
Bila TokoKu menjual **Paket**, apa yang perlu diubah? Cukup tambah class baru, loop tidak berubah.
