# Latihan 4.1 - Class dan Object

**Kasus:** TokoKu ingin menyimpan informasi satu produk. Buat class sederhana sebagai cetakan produk, lalu buat satu object dari class tersebut.

## Analogi
- **Class** adalah cetakan.
- **Object** adalah hasil yang dibuat dari cetakan.
- **Attribute** adalah data yang disimpan pada object, seperti nama dan harga produk.
- **Method** adalah tindakan yang bisa dilakukan oleh object.

## Langkah
1. Buat class `Produk`.
2. Buat `__init__()` yang menerima `nama` dan `harga`, lalu simpan sebagai `self.nama` dan `self.harga`.
3. Buat method `tampilkan_info()` untuk menampilkan nama dan harga produk.
4. Buat satu object produk Kopi Susu Aren, lalu panggil method `tampilkan_info()`.

Fokus latihan ini hanya pada class, object, attribute, method, dan `self`. Belum perlu menggunakan stok, banyak object, atau loop.

## Target
```
Nama produk : Kopi Susu Aren
Harga       : Rp 25.000
```

## Diskusi
- Apa bedanya class `Produk` dengan object `kopi`?
- Data apa yang disimpan oleh `self.nama` dan `self.harga`?
