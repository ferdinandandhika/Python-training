# Latihan 4.2 - Encapsulation: Setor dan Tarik

Lanjutkan konsep dompet dari Latihan 1. Kali ini, dompet bisa menerima setoran dan menolak penarikan yang melebihi saldo.

## Langkah
1. Buat class `Dompet` dengan `pemilik` dan saldo internal `self._saldo`.
2. Buat property `saldo` untuk membaca saldo.
3. Buat method `setor(jumlah)` untuk menambahkan saldo.
4. Buat method `tarik(jumlah)`:
   - Jika jumlah penarikan lebih besar dari saldo, kembalikan `False` dan jangan ubah saldo.
   - Jika saldo cukup, kurangi saldo dan kembalikan `True`.
5. Minta nama pemilik dengan `input()` dan buat dompet dengan saldo awal Rp 100.000.
6. Minta jumlah setoran, ubah input menjadi `int`, lalu setor ke dompet.
7. Minta jumlah penarikan, ubah input menjadi `int`, lalu gunakan hasil `tarik()` untuk menampilkan apakah penarikan berhasil.

Masukkan jumlah setoran dan penarikan sebagai angka bulat. **Fokus:** `input()`, konversi ke `int`, `@property`, method, dan percabangan `if`. Belum perlu menggunakan loop atau `try/except`.

## Contoh
Input:
```
Nama pemilik: Rina
Jumlah setor: 50000
Jumlah penarikan: 30000
```

Hasil:
```
Saldo awal Rina: Rp 100.000
Setor Rp 50.000 berhasil. Saldo: Rp 150.000
Tarik Rp 30.000 berhasil. Saldo: Rp 120.000
```
