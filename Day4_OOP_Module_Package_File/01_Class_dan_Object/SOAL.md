# Latihan 4.1 - Class dan Object

**Kasus:** Sampai Day 3, menu TokoKu disimpan sebagai dictionary.
Sekarang setiap menu menjadi **object** dari class `Produk`.

## Analogi
- **Class** = cetakan kue. **Object** = kue hasil cetakan.

## Langkah
1. Lengkapi class `Produk` dengan `__init__(self, kode, nama, harga, stok=0)`.
2. Tambahkan class attribute `jumlah_produk` yang bertambah setiap object dibuat.
3. Buat method `info()`, `jual(qty)` (False bila stok kurang), dan `restock(qty)`.
4. Buat method `__str__` agar `print(produk)` tampil rapi.
5. Buat 4 object, jual dan restock, lalu tampilkan semua.

## Target output
```
Jumlah produk dibuat: 4
K01 | Kopi Susu Aren   | Rp 25.000 | stok 20
Jual  5 Kopi Susu Aren  : berhasil, sisa 15
Jual 50 Croissant       : GAGAL, stok hanya 10
```

## Diskusi
- Apa beda `self.nama` dengan `Produk.jumlah_produk`?
- Kenapa method selalu punya parameter `self`?
