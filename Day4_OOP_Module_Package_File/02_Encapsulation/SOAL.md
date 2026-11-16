# Latihan 4.2 - Encapsulation dan @property

**Kasus:** Kartu member TokoKu punya saldo dan poin.
Kasir **tidak boleh** mengubah saldo langsung (`kartu.saldo = 999999999`).
Saldo hanya boleh berubah lewat `top_up()` dan `bayar()`.

## Aturan bisnis
- Top up minimal Rp 10.000.
- Bayar gagal bila saldo kurang (`ValueError`).
- Setiap Rp 10.000 pembayaran mendapat 1 poin.
- Level: poin >= 50 **Gold**, >= 20 **Silver**, selainnya **Bronze**.
- Nama boleh diubah tetapi tidak boleh kosong.

## Langkah
1. Simpan saldo di `self._saldo` (garis bawah = jangan diakses dari luar).
2. Buat `@property saldo` tanpa setter (read-only).
3. Buat `@property nama` dan `@nama.setter` dengan validasi.
4. Buat `@property level` yang dihitung dari poin.
5. Uji: `kartu.saldo = 5000000` harus ditolak.
