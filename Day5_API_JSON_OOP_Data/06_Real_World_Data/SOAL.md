# Latihan 5.6 - Examine Real World Data

File `../data/penjualan_cabang_kotor.csv` diisi manual oleh cabang dan penuh masalah:
nama cabang tidak konsisten, qty kosong, total berisi `-`, format tanggal campur,
rating kosong, dan baris duplikat.

1. **Inspeksi:** `info()`, `isna().sum()`, `duplicated().sum()`, `unique()`.
2. **Bersihkan:** `str.strip().str.title()`, `pd.to_numeric(errors="coerce")`,
   `pd.to_datetime(format="mixed", dayfirst=True)`, isi qty dan total yang kosong,
   rating diisi median, `drop_duplicates()`.
3. **Validasi:** tidak ada nilai kosong tersisa.
4. **Analisis:** omzet per cabang dan per bulan, lalu buat 1 grafik.
5. **Simpan:** `output/penjualan_bersih.csv`, tulis 3 insight di `INSIGHT.md`.
