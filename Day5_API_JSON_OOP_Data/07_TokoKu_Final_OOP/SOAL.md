# Proyek TokoKu FINAL (OOP)

Gabungkan seluruh materi 5 hari dalam package berbasis class.

## Menu aplikasi
```
=== TOKOKU ===
1. Transaksi baru         Keranjang + pilihan pembayaran Tunai/QRIS/Kartu Debit
2. Laporan penjualan      Pandas + decorator @catat_waktu
3. Buat grafik dashboard  Matplotlib, disimpan sebagai PNG
4. Lihat harga dalam USD  API + JSON + data cadangan
5. Keluar
```

## Struktur package
```
tokoku_oop/
  produk.py       Produk, Minuman, Makanan            (Day 4)
  keranjang.py    ItemKeranjang, Keranjang            (Day 4)
  pembayaran.py   MetodePembayaran ABC, Tunai, QRIS, KartuDebit, HasilBayar  (Day 5)
  kurs.py         ambil_kurs_usd()                    (Day 5)
  toko.py         Toko: checkout(), laporan(), dashboard()   (Day 4 + Day 5)
test_tokoku.py    unit test
buat_data_contoh.py   isi transaksi.csv dengan 300 transaksi
```

## Checklist fitur
- [ ] Menu dibaca dari `menu.csv` lewat `Toko.dari_csv()`
- [ ] Minuman bisa dipilih ukuran S/M/L
- [ ] Diskon, member, dan pajak 11%
- [ ] Pembayaran memakai class turunan `MetodePembayaran`
- [ ] Transaksi berhasil tersimpan di `transaksi.csv`, transaksi gagal tidak tersimpan
- [ ] Laporan Pandas dan dashboard PNG
- [ ] Kurs USD dari API dengan cadangan offline
- [ ] `python -m unittest -v` lolos

## Tantangan
Tambahkan class `Paket` (gabungan 1 minuman + 1 makanan, potongan Rp 5.000) dan 1 test baru.

## Show and tell (5 menit per kelompok)
Demo aplikasi, satu class yang paling dibanggakan, dan satu error yang berhasil diatasi.
