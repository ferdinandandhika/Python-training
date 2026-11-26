# Proyek TokoKu Day 3 - Struk versi Web

Latihan ini adalah lanjutan langsung dari [TokoKu Day 3](../04_TokoKu_Day3/SOAL.md). Salin alur dan aturan transaksi dari proyek 04. Perubahannya hanya pada struk: tampilkan hasilnya di browser sebagai halaman HTML.

## Yang sama dengan proyek 04
- Menu disimpan dalam `dictionary` dan keranjang dalam `list`.
- Menu dan struk menggunakan loop `for`.
- Input barang diulang dengan `while` sampai kasir mengetik `selesai`.
- Kode barang dan jumlah divalidasi seperti di proyek 04.
- Aturan diskon dan pajak tetap sama.

## Yang berbeda
- Alih-alih mencetak struk ke terminal, isi template HTML menggunakan `.replace()`.
- Simpan halaman sebagai `struk.html`, lalu buka di browser.
- Gunakan tombol **Cetak struk** untuk mencetak atau menyimpan sebagai PDF.

## Langkah
1. Salin kode proyek 04 ke bagian Python di `latihan.py`.
2. Pertahankan cara kerja menu, keranjang, input, diskon, dan pajaknya.
3. Ubah isi fungsi `cetak_struk()` agar baris barang dan ringkasan pembayaran dimasukkan ke template HTML.
4. Simpan template yang sudah diisi ke `struk.html` dan buka dengan browser.

**Tidak ada aturan transaksi atau fitur baru yang perlu dibuat.** Fokusnya hanya mengubah tampilan struk terminal dari proyek 04 menjadi struk Web.
