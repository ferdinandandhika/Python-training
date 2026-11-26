# Python Programming Fundamentals - 5 Hari (Paket Praktik, termasuk OOP)

Paket ini dipakai bersama **00_Trainer_Guide_Python_5_Hari.docx**.
Prinsipnya: **demo singkat, lalu langsung praktik**. Setiap folder latihan berisi:

| File | Fungsi |
|---|---|
| `SOAL.md` | Cerita kasus, target, dan langkah praktik |
| `latihan.py` | File yang dikerjakan peserta (ada tanda `# TODO`) |
| `solusi.py` | Kunci jawaban untuk trainer, jangan dibagikan di awal |

## Cara mulai
1. Install Python 3.11+ dan Visual Studio Code (lihat `00_Setup/PANDUAN_SETUP.md`).
2. Buka folder ini di VS Code: **File > Open Folder**.
3. Buat virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate        (Windows)
   source .venv/bin/activate       (Mac/Linux)
   pip install -r requirements.txt
   ```
4. Cek instalasi: `python 00_Setup/cek_setup.py`

## Alur 5 hari
| Hari | Tema | Latihan | Proyek TokoKu |
|---|---|---|---|
| 1 | Setup, Output, String | Hello App, Greeting, String Lab | Struk sederhana |
| 2 | Tipe Data, Error, Kondisi | GPA, Error Lab, Rock Paper Scissors, Struk Web | Validasi input + diskon + struk Web |
| 3 | Collection, Loop, Function | For Loop, List Basics, Guess Number, Calculator, TokoKu Web | Keranjang belanja + struk Web |
| 4 | **OOP**, Module, Package, File | Class, Encapsulation, Inheritance, Package, File Lab, To-Do OOP | Class Produk + Keranjang, simpan ke CSV |
| 5 | API, JSON, **ABC + Dataclass**, Data | Kurs API, Decorator, Pembayaran OOP, Pandas, Matplotlib, Real Data | TokoKu Final Web + OOP + unit test |

## Di mana OOP diajarkan?
- **Day 4 pagi:** class, object, encapsulation (`@property`), inheritance, polymorphism.
- **Day 4 sore:** composition dan dunder method di proyek TokoKu, To-Do List berbasis class.
- **Day 5:** abstract class (ABC) dan `@dataclass` untuk metode pembayaran,
  lalu TokoKu Final dikembangkan menjadi aplikasi web lokal berbasis package dengan unit test.

Semua data di paket ini adalah data dummy untuk pelatihan.
