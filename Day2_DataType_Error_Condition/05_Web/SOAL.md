# Latihan 2.5 - TokoKu Day 2 versi Web

Lanjutkan proyek struk HTML dari Day 1. Data transaksi tetap dimasukkan di terminal, lalu Python menghitung pembayaran dan menampilkan struk di browser.

## Pilihan menu
| Nomor | Menu | Harga |
|---:|---|---:|
| 1 | Kopi Susu Aren | Rp 25.000 |
| 2 | Matcha Latte | Rp 28.000 |
| 3 | Croissant | Rp 18.000 |

## Aturan transaksi
- Pilih menu dengan memasukkan nomor `1`, `2`, atau `3`.
- Jumlah harus berupa angka bulat lebih dari nol.
- Subtotal Rp 200.000 atau lebih mendapat diskon 15%.
- Subtotal Rp 100.000 sampai kurang dari Rp 200.000 mendapat diskon 10%.
- Subtotal di bawah Rp 100.000 tidak mendapat diskon.
- Pajak 11% dihitung dari subtotal setelah diskon.
- Jika pilihan menu atau jumlah tidak valid, tampilkan pesan di terminal dan jangan buat struk.

## Langkah
1. Minta nama pelanggan, nomor menu, dan jumlah dari terminal.
2. Gunakan `try/except ValueError` untuk mengubah nomor menu dan jumlah menjadi `int`.
3. Gunakan `if/elif/else` untuk menentukan nama dan harga menu, lalu menghitung diskon.
4. Hitung subtotal, pajak, dan total bayar.
5. Isi penanda pada template HTML menggunakan `.replace()`.
6. Simpan sebagai `struk.html` di folder latihan ini dan buka dengan browser.

**Catatan:** Menu dipilih di terminal, bukan melalui dropdown pada halaman web. Tidak perlu menggunakan `while`, `for`, `list`, `dictionary`, atau membuat fungsi.

## Contoh
Jika pelanggan memilih Kopi Susu Aren sebanyak 8:
```
Subtotal        : Rp 200.000
Diskon (15%)    : -Rp 30.000
Pajak (11%)     : Rp 18.700
TOTAL BAYAR     : Rp 188.700
```
