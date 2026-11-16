# Latihan 4.5 - Read and Write Files

**Kasus:** Kasir mencatat penjualan harian di file teks.

1. Baca `data/penjualan_harian.txt` baris per baris dengan `with open()`.
2. Lewati baris kosong dan baris komentar (diawali `#`).
3. Pecah setiap baris `tanggal;menu;qty;harga`.
4. Hitung total per menu dengan dictionary.
5. Tulis hasil ke `output/rekap_menu.csv` (module `csv`).
6. Tulis ringkasan ke `output/ringkasan.json` (module `json`).
7. Tangani `FileNotFoundError`.
