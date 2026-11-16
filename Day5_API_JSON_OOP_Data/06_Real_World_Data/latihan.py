# Latihan 5.6 - Real World Data
from pathlib import Path
import pandas as pd

FOLDER = Path(__file__).parent
(FOLDER / "output").mkdir(exist_ok=True)
df = pd.read_csv(FOLDER.parent / "data" / "penjualan_cabang_kotor.csv", dtype=str)
# TODO 1 inspeksi  TODO 2 rapikan cabang  TODO 3 ubah ke numerik  TODO 4 tanggal
# TODO 5 isi nilai kosong  TODO 6 hapus duplikat  TODO 7 validasi
# TODO 8 analisis + grafik  TODO 9 simpan output/penjualan_bersih.csv
