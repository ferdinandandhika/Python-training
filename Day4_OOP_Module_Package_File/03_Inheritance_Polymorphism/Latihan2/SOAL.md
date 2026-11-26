# Latihan 4.3B - Mengubah Tampilan Info Produk

Lanjutkan latihan inheritance dari folder `Input`. Kali ini, class `Minuman` memiliki tampilan informasi sendiri.

## Konsep
- `Minuman` mewarisi `__init__()` dari class `Produk`, jadi object minuman tetap menerima nama dan harga.
- `Minuman` memiliki method `tampilkan_info()` sendiri. Method ini menggantikan method dengan nama sama dari `Produk` (**override**).

## Langkah
1. Buat class induk `Produk` dengan `__init__(nama, harga)`.
2. Buat method `tampilkan_info()` di `Produk`.
3. Buat class `Minuman(Produk)`.
4. Di dalam `Minuman`, buat method `tampilkan_info()` yang menampilkan nama, harga, dan keterangan bahwa produk adalah minuman.
5. Minta nama dan harga minuman menggunakan `input()`, lalu buat object `Minuman` dan panggil method-nya.

Masukkan harga sebagai angka bulat tanpa pemisah ribuan. Fokus latihan ini pada inheritance dan override satu method. Belum perlu `super()`, banyak class anak, loop, atau aturan harga khusus.

## Contoh
Input:
```
Nama minuman: Matcha Latte
Harga: 28000
```

Hasil:
```
Jenis  : Minuman
Nama   : Matcha Latte
Harga  : Rp 28.000
```
