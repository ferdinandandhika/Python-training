# Latihan 2.3 - Batu, Kertas, Gunting

Buat permainan satu ronde antara pemain dan komputer.

## Aturan
- Batu mengalahkan gunting.
- Gunting mengalahkan kertas.
- Kertas mengalahkan batu.
- Jika pilihan sama, hasilnya seri.

## Langkah
1. Komputer memilih secara acak menggunakan `random.choice`.
2. Minta pemain memasukkan `batu`, `kertas`, atau `gunting`.
3. Rapikan input dengan `.strip().lower()`.
4. Jika pilihan tidak valid, tampilkan pesan kesalahan.
5. Jika valid, tentukan hasil dengan `if`, `elif`, `else`, dan operator `and`/`or`.
6. Tampilkan pilihan pemain, pilihan komputer, dan hasilnya.

**Catatan:** Permainan hanya satu ronde. Tidak perlu menggunakan `while` atau `for`.

## Contoh
Jika pemain memilih `batu` dan komputer memilih `gunting`:
```
Kamu: batu | Komputer: gunting
MENANG
```
