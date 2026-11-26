# Proyek TokoKu - Day 4: TokoKu Berbasis Class + Simpan ke CSV

Hari ini TokoKu Day 3 (dictionary + function) ditulis ulang memakai class
dan disusun sebagai **package** `tokoku_oop`.

## Konsep baru: Composition (has-a)
- Minuman **adalah** Produk -> inheritance
- Keranjang **memiliki** ItemKeranjang, ItemKeranjang **memiliki** Produk -> composition

## Dunder method di Keranjang
| Method | Dipanggil saat |
|---|---|
| `__len__` | `len(keranjang)` |
| `__iter__` | `for item in keranjang` |
| `__contains__` | `"K01" in keranjang` |
| `__bool__` | `if keranjang:` |
| `__str__` | `print(keranjang)` |

## Struktur
```
07_TokoKu_Day4_OOP/
  menu.csv
  tokoku_oop/
    __init__.py
    produk.py      Produk, Minuman (S/M/L), Makanan
    keranjang.py   ItemKeranjang, Keranjang
    toko.py        Toko: dari_csv(), cari(), hitung(), checkout(), laporan()
  latihan.py       kerangka satu file
  solusi.py        aplikasi kasir yang memakai package
```

## Langkah
1. Kerjakan `latihan.py` mengikuti TODO (salin class dari latihan 4.1 dan 4.3).
2. Buka package `tokoku_oop/` dan bandingkan dengan hasilmu.
3. Jalankan `python solusi.py`: beli 2 Kopi Susu Aren ukuran L dan 3 Cheesecake.
4. Buka `transaksi.csv` di Excel.

## Antarmuka Web Lokal
Proyek ini juga menyediakan antarmuka browser di `web_app.py`. Jalankan:
```
python web_app.py
```
Browser membuka `http://127.0.0.1:8000`. Pilih **1. Transaksi baru** atau **2. Laporan penjualan** lewat tombol, lalu isi form dan pilih barang dari daftar bernomor. Tidak perlu mengetik perintah seperti `baru` atau `laporan`.

Transaksi Web menggunakan package dan file `transaksi.csv` yang sama. Ini aplikasi lokal untuk latihan, bukan situs yang dipublikasikan di internet; server berhenti dengan `Ctrl+C` di terminal.

Besok (Day 5) TokoKu ditambah metode pembayaran, laporan Pandas, grafik, kurs API, dan unit test.
