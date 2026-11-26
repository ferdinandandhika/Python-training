# Latihan 5.6 - Membersihkan Data Penjualan

File `../data/penjualan_cabang_kotor.csv` berisi nama cabang yang penulisannya
belum rapi, angka yang kosong atau berupa tanda `-`, dan beberapa baris duplikat.

1. Baca kolom transaksi, cabang, jumlah, harga, dan total dari file CSV.
2. Rapikan nama cabang dengan `str.strip()` dan `str.title()`.
3. Ubah kolom jumlah, harga, dan total menjadi angka menggunakan
   `pd.to_numeric(errors="coerce")`.
4. Hapus baris duplikat dan baris yang tidak memiliki angka transaksi.
5. Hitung total penjualan setiap cabang dan simpan data bersih ke
   `output/penjualan_bersih.csv`.

Terakhir, tulis satu kalimat di `INSIGHT.md` tentang cabang dengan penjualan tertinggi.
