# Proyek TokoKu - Day 2: Validasi dan Diskon

Lanjutkan struk sederhana dari Day 1. Kali ini, TokoKu menerima **satu jenis barang** per transaksi dan menghitung diskon serta pajak.

## Yang dilatih
- Hasil `input()` bertipe teks, lalu harga dan jumlah diubah menjadi `int`.
- `try/except ValueError` untuk menangani harga atau jumlah yang bukan angka bulat.
- `if/elif/else` untuk memeriksa nilai dan menentukan diskon.
- Operasi hitung untuk subtotal, diskon, pajak, dan total.

## Aturan transaksi
1. Harga dan jumlah harus berupa angka bulat lebih dari nol. Jika konversi gagal atau nilainya tidak valid, tampilkan pesan dan batalkan transaksi.
2. Diskon dihitung dari subtotal:

   | Subtotal | Diskon |
   |---|---:|
   | Rp 200.000 atau lebih | 15% |
   | Rp 100.000 sampai kurang dari Rp 200.000 | 10% |
   | Kurang dari Rp 100.000 | 0% |

3. Pajak sebesar 11% dihitung dari subtotal setelah diskon.
4. Cetak struk yang menampilkan pelanggan, barang, jumlah, subtotal, diskon, pajak, dan total bayar.

## Langkah
1. Minta nama pelanggan, nama barang, harga satuan, dan jumlah.
2. Ubah harga dan jumlah dari teks ke `int` di dalam `try`.
3. Tangani `ValueError` dengan `except`. Tidak perlu meminta ulang; transaksi boleh dibatalkan.
4. Pastikan harga dan jumlah lebih dari nol.
5. Hitung subtotal, pilih diskon menggunakan `if/elif/else`, lalu hitung pajak dan total.
6. Cetak struk dengan format Rupiah.

**Catatan:** Masukkan harga tanpa pemisah ribuan, misalnya `120000`. Tidak perlu menggunakan `while`, `for`, atau membuat fungsi.

## Contoh
Masukan:
```
Nama pelanggan: Rina
Nama barang: Paket Keluarga
Harga satuan: 120000
Jumlah: 2
```

Bagian perhitungan pada struk:
```
Subtotal        : Rp 240.000
Diskon (15%)    : -Rp 36.000
Pajak (11%)     : Rp 22.440
TOTAL BAYAR     : Rp 226.440
```
