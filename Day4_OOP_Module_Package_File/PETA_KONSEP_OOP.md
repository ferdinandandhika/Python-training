# Peta Konsep OOP di TokoKu

```
                  +-------------------+
                  |      Produk       |   class induk
                  | kode, nama, harga |
                  | harga_satuan()    |
                  +---------+---------+
                            | inheritance (is-a)
              +-------------+-------------+
              |                           |
      +-------+-------+           +-------+-------+
      |    Minuman    |           |    Makanan    |
      | ukuran S/M/L  |           |               |
      +---------------+           +---------------+

  Keranjang --memiliki--> ItemKeranjang --memiliki--> Produk     (composition, has-a)
  MetodePembayaran (ABC) <-- Tunai, QRIS, KartuDebit             (Day 5: abstraction)
  Toko --memakai--> Keranjang + MetodePembayaran + file CSV
```

| Konsep | Kalimat sederhana | Di TokoKu | Hari |
|---|---|---|---|
| Class | Cetakan | `class Produk` | Day 4 |
| Object | Hasil cetakan | `kopi = Produk(...)` | Day 4 |
| Encapsulation | Data dijaga, akses lewat pintu resmi | `kartu.saldo` read-only | Day 4 |
| Inheritance | Anak mewarisi induk | `Minuman(Produk)` | Day 4 |
| Polymorphism | Perintah sama, perilaku beda | `p.harga_akhir(qty)` | Day 4 |
| Composition | Object berisi object lain | `Keranjang` berisi `ItemKeranjang` | Day 4 |
| Abstraction | Kontrak yang wajib dipenuhi | `MetodePembayaran(ABC)` | Day 5 |
| Dataclass | Class khusus menyimpan data | `@dataclass HasilBayar` | Day 5 |
