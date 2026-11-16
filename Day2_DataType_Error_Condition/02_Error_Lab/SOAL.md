# Latihan 2.2 - Error Handling Lab

**Kasus:** Aplikasi kasir sering berhenti karena kasir salah ketik.

## Bagian A - Kenali error (5 menit)
Jalankan `kenali_error.py`. Tebak nama error sebelum melihat output:
`ValueError`, `ZeroDivisionError`, `TypeError`, `KeyError`, `IndexError`,
`FileNotFoundError`, `NameError`.

## Bagian B - Tangani error
Buat fungsi `minta_angka()` yang:
1. Terus meminta input sampai yang diketik adalah angka bulat positif.
2. Menampilkan pesan ramah bila salah ketik.
3. Menangani pembagian nol saat menghitung tagihan per orang.
