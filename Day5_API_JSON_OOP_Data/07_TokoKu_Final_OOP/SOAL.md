# Proyek TokoKu FINAL (Web + OOP)

Kembangkan aplikasi kasir TokoKu dari Day 4 menjadi web lokal. Proyek ini
menggabungkan package OOP Day 4 dengan pembayaran, kurs API/JSON, Pandas,
decorator, dan Matplotlib dari Day 5.

## Menjalankan aplikasi

Di terminal, dari folder proyek ini jalankan:

```text
python solusi.py
```

Browser akan membuka `http://127.0.0.1:8001`. Jika tidak terbuka otomatis,
masukkan alamat tersebut secara manual. Server hanya menerima koneksi dari
komputer sendiri. Tekan `Ctrl+C` di terminal untuk menghentikannya.

## Menu web

1. Transaksi baru: pilih produk dengan nomor, ukuran minuman, jumlah, dan status member.
2. Laporan penjualan: ringkasan omzet, menu terlaris, metode pembayaran, dan transaksi terbaru.
3. Dashboard: buat dan lihat grafik PNG dari transaksi.
4. Konverter dan harga USD: gunakan kurs API dengan data cadangan.

QRIS dan kartu debit adalah simulasi latihan, bukan pembayaran sungguhan.
Transaksi berhasil disimpan di `transaksi.csv`; transaksi yang gagal tidak disimpan.

## Struktur package
```
tokoku_oop/
  produk.py       Produk, Minuman, Makanan            (Day 4)
  keranjang.py    ItemKeranjang, Keranjang            (Day 4)
  pembayaran.py   MetodePembayaran ABC, Tunai, QRIS, KartuDebit, HasilBayar  (Day 5)
  kurs.py         ambil_kurs_usd()                    (Day 5)
  toko.py         Toko: checkout(), laporan(), dashboard()   (Day 4 + Day 5)
test_tokoku.py    unit test
test_web_app.py   uji alur web lokal
buat_data_contoh.py   isi transaksi.csv dengan 300 transaksi
web_app.py        server HTTP dan halaman web
solusi.py         launcher aplikasi web
solusi_terminal.py versi terminal opsional
```

## Checklist fitur
- [ ] Menu dibaca dari `menu.csv` lewat `Toko.dari_csv()`
- [ ] Minuman bisa dipilih ukuran S/M/L
- [ ] Diskon, member, dan pajak 11%
- [ ] Pembayaran memakai class turunan `MetodePembayaran`
- [ ] Transaksi berhasil tersimpan di `transaksi.csv`, transaksi gagal tidak tersimpan
- [ ] Laporan Pandas dan dashboard PNG
- [ ] Kurs USD dari API dengan cadangan offline
- [ ] Antarmuka web lokal memakai `HTTPServer`
- [ ] Struk dapat dicetak dari browser
- [ ] `python -m unittest -v` lolos

## Tantangan
Tambahkan class `Paket` (gabungan 1 minuman + 1 makanan, potongan Rp 5.000) dan 1 test baru.

## Show and tell (5 menit per kelompok)
Demo aplikasi, satu class yang paling dibanggakan, dan satu error yang berhasil diatasi.
