# Latihan 5.3 - ABC dan Dataclass

Buat simulasi pembayaran sederhana untuk TokoKu menggunakan input.

1. Gunakan `@dataclass` untuk menyimpan nama metode, total, dan status pembayaran.
2. Buat `MetodePembayaran` sebagai abstract class dengan method `proses(total)`.
3. Minta pengguna memasukkan total belanja.
4. Tampilkan pilihan bernomor: `1. Tunai` dan `2. QRIS`.
5. Untuk tunai, minta jumlah uang yang diterima. Untuk QRIS, tampilkan pesan simulasi.

Fokus latihan adalah memahami kontrak abstract class dan cara dataclass menyimpan
hasil. QRIS di latihan ini hanya simulasi, bukan pembayaran sungguhan.
PIN, limit transaksi, dan biaya tambahan belum diperlukan.
