# Latihan 2.2 - Memeriksa Jumlah Barang

**Kasus:** Kasir menerima jumlah barang sebagai teks dan perlu memastikan nilainya bisa dipakai untuk transaksi.

## Langkah
1. Minta jumlah barang menggunakan `input()`. Hasilnya bertipe `str`.
2. Ubah teks tersebut menjadi `int` di dalam `try`.
3. Jika konversi gagal, tangani `ValueError` dan tampilkan pesan bahwa jumlah harus berupa angka bulat.
4. Jika konversi berhasil, gunakan `if`, `elif`, dan `else` untuk membedakan jumlah negatif, nol, dan positif.
5. Jalankan program lagi dengan memasukkan `abc` untuk mencoba penanganan error.

**Catatan:** Gunakan satu nilai setiap kali menjalankan program. Tidak perlu menggunakan `while` atau `for`.

## Target
Jika memasukkan `0`:
```
Jumlah barang: 0
Stok habis.
```

Jika memasukkan `abc`:
```
Jumlah harus berupa angka bulat.
```
