# Latihan 4.2 - Encapsulation Sederhana

**Kasus:** Buat dompet sederhana yang menyimpan saldo. Saldo bisa dilihat, tetapi penambahannya dilakukan melalui method `setor()`.

## Konsep
- `self._saldo` menandai bahwa saldo adalah data internal object. Garis bawah adalah konvensi: dari luar class, gunakan property `saldo`.
- `@property` membuat `saldo` bisa dibaca seperti attribute biasa.
- Method `setor()` menjadi cara untuk mengubah saldo.

## Langkah
1. Buat class `Dompet` dengan `__init__(pemilik, saldo_awal)`.
2. Simpan nama pemilik pada `self.pemilik` dan saldo pada `self._saldo`.
3. Buat property `saldo` yang mengembalikan `self._saldo`.
4. Buat method `setor(jumlah)` yang menambahkan jumlah ke saldo.
5. Buat satu object, tampilkan saldonya, lakukan setor, lalu tampilkan saldo terbaru.

Fokus latihan ini pada data internal, `@property`, dan method untuk mengubah data. Belum perlu setter, validasi, poin, level, atau penanganan error.

## Target
```
Saldo awal Rina: Rp 100.000
Saldo setelah setor: Rp 150.000
```

## Diskusi
- Apa fungsi `self._saldo`?
- Kenapa saldo diakses lewat `dompet.saldo`, tetapi diubah lewat `dompet.setor()`?
