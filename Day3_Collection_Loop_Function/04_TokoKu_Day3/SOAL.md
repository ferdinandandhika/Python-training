# Proyek TokoKu - Day 3: Keranjang Belanja

Lanjutkan proyek TokoKu dengan menyimpan beberapa barang dalam keranjang.

## Yang dilatih
- Menu disimpan dalam `dictionary`.
- Barang yang dibeli disimpan dalam `list`.
- Loop `for` untuk menampilkan menu dan isi keranjang.
- Loop `while` untuk menerima barang sampai kasir mengetik `selesai`.
- Fungsi sederhana untuk menampilkan menu, menambahkan barang, dan mencetak struk.
- Diskon dan pajak yang sudah dipelajari pada Day 2.

## Aturan transaksi
- Pilih barang dengan kode yang tersedia di menu.
- Masukkan jumlah sebagai angka lebih dari nol.
- Jika kode atau jumlah tidak valid, tampilkan pesan dan minta input lagi.
- Jika barang yang sama dimasukkan beberapa kali, tampilkan sebagai baris terpisah di struk.
- Diskon: subtotal Rp 200.000 atau lebih mendapat 15%; subtotal Rp 100.000 sampai kurang dari Rp 200.000 mendapat 10%; selain itu tidak ada diskon.
- Pajak 11% dihitung setelah diskon.

## Langkah
1. Lengkapi fungsi `tampilkan_menu()` untuk menampilkan menu.
2. Lengkapi fungsi `tambah_ke_keranjang()` untuk menambahkan satu barang ke list.
3. Buat loop input yang berhenti saat kasir mengetik `selesai`.
4. Lengkapi fungsi `cetak_struk()` untuk menampilkan barang, menghitung subtotal, diskon, pajak, dan total.
5. Jika keranjang kosong, tampilkan pesan bahwa transaksi dibatalkan.

**Catatan:** Kerjakan satu langkah setiap kali. Belum perlu menggabungkan barang yang sama atau menambahkan diskon member.

Besok, keranjang ini akan ditulis ulang menggunakan **class**.
