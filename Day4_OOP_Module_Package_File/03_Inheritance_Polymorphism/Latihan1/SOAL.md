# Latihan 4.3A - Inheritance dengan Input

**Kasus:** TokoKu ingin membuat class `Minuman` yang mewarisi data dan method dari class `Produk`.

## Konsep
- `Produk` adalah parent class yang menyimpan nama dan harga serta memiliki method untuk menampilkan informasi.
- `Minuman` adalah child class. Dengan menulis `class Minuman(Produk)`, `Minuman` mewarisi constructor dan method dari `Produk`.
- Untuk latihan ini, `Minuman` belum membutuhkan attribute atau method tambahan.

## Langkah
1. Lengkapi class `Produk` dengan `__init__(nama, harga)` dan simpan datanya sebagai attribute.
2. Lengkapi method `tampilkan_info()` untuk menampilkan nama dan harga.
3. Buat class `Minuman` yang mewarisi `Produk`. Gunakan `pass` karena belum ada perilaku tambahan.
4. Minta nama dan harga minuman menggunakan `input()`. Masukkan harga sebagai angka bulat tanpa pemisah ribuan.
5. Buat object `Minuman` dari input dan panggil `tampilkan_info()`.

Fokus latihan ini hanya pada parent class, child class, inheritance, dan input. Belum perlu `super()`, override, banyak jenis produk, atau loop.

## Contoh
Input:
```
Nama minuman: Kopi Susu Aren
Harga: 25000
```

Hasil:
```
Produk: Kopi Susu Aren
Harga : Rp 25.000
```
