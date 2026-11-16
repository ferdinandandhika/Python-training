# Latihan 4.6 - Build a To-Do List (versi OOP)

**Kasus:** Tim TokoKu butuh to-do list yang tidak hilang saat program ditutup.
Kali ini kita gabungkan **class** dan **file JSON**.

## Desain class
```
Tugas            judul, selesai, tandai_selesai(), ke_dict(), dari_dict() [classmethod]
TodoList         file, tugas (list of Tugas)
                 muat(), simpan(), tambah(), tandai(nomor), hapus(nomor), tampilkan()
                 __len__()  -> jumlah tugas
```

## Menu
`1` Lihat | `2` Tambah | `3` Tandai selesai | `4` Hapus | `5` Simpan dan keluar

## Aturan
- Data disimpan di `todo.json`, otomatis dimuat saat program dibuka.
- Nomor yang salah tidak membuat program berhenti.
- Uji: tambah 3 tugas, tutup program, jalankan lagi. Tugas masih ada.
