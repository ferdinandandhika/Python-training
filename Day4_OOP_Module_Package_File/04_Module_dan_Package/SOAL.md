# Latihan 4.4 - Modules, Packages, and Virtual Environment

## Bagian A - Module bawaan (10 menit)
Jalankan `modul_bawaan.py`, lalu tampilkan 3 angka acak, tanggal 30 hari lagi, dan akar 144.

## Bagian B - Package sendiri
1. Folder `tokoku_utils/` adalah **package** (ada `__init__.py`).
2. Buka `format.py` dan `hitung.py`, pahami isinya.
3. Kerjakan `latihan.py` yang meng-import package tersebut.
4. Tantangan: tambahkan function `hitung_pajak()` ke `hitung.py`.

## Bagian C - Virtual environment dan package (praktik di terminal)
```
python -m venv .venv
.venv\Scripts\activate          (Windows)
pip install requests
pip list
pip freeze > requirements_saya.txt
deactivate
```
Diskusi: kenapa setiap project sebaiknya punya virtual environment sendiri?
