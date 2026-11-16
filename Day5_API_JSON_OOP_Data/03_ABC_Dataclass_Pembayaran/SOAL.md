# Latihan 5.3 - Abstract Class dan Dataclass (OOP lanjutan)

**Kasus:** TokoKu menerima 3 metode pembayaran. Semua wajib punya `proses(total)`,
tetapi aturannya berbeda.

| Class | Aturan |
|---|---|
| `Tunai` | uang diterima >= total, hitung kembalian |
| `QRIS` | biaya layanan 0,7% ditanggung toko, pembeli bayar pas |
| `KartuDebit` | PIN 6 digit, maksimal Rp 5.000.000 per transaksi |

## Konsep
- `MetodePembayaran(ABC)` dengan `@abstractmethod proses(total)`: **kontrak**.
  Class abstrak tidak bisa dibuat object-nya.
- `@dataclass HasilBayar`: Python otomatis membuat `__init__`, `__repr__`, `__eq__`.

## Langkah
1. Coba `MetodePembayaran()` dan baca `TypeError`-nya.
2. Lengkapi `HasilBayar` dan 3 class turunan.
3. Jalankan 6 skenario: tunai cukup, tunai kurang, QRIS, PIN salah, melebihi limit, debit sukses.
