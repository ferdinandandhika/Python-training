# Latihan 5.4 - NumPy dan Pandas Dasar
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).parent.parent / "data" / "penjualan_tokoku.csv"
qty = np.array([2, 1, 3])
harga = np.array([25000, 18000, 32000])

# TODO 1: kalikan qty dan harga, lalu tampilkan total setiap barang dan jumlahnya.

# TODO 2: baca file CSV ke DataFrame.
df = pd.read_csv(DATA)
# TODO 3: tampilkan lima baris pertama dan ukuran data.
# TODO 4: hitung total penjualan dan total per cabang.
