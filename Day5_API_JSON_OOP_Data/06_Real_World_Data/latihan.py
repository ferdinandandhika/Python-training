# Latihan 5.6 - Membersihkan Data Penjualan
from pathlib import Path
import pandas as pd

FOLDER = Path(__file__).parent
DATA = FOLDER.parent / "data" / "penjualan_cabang_kotor.csv"
OUTPUT = FOLDER / "output"
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(
    DATA,
    usecols=["id_transaksi", "cabang", "qty", "harga", "total"],
    dtype=str,
)
jumlah_awal = len(df)

# TODO 1: rapikan nama cabang.
# TODO 2: ubah qty, harga, dan total menjadi angka.
# TODO 3: hapus baris duplikat dan baris dengan angka yang kosong.
# TODO 4: hitung total penjualan per cabang.
# TODO 5: simpan data bersih ke output/penjualan_bersih.csv.
