"""Cek kesiapan laptop peserta. Jalankan: python 00_Setup/cek_setup.py"""
import sys
import importlib.util

print("=" * 45)
print(" CEK SETUP PYTHON TRAINING")
print("=" * 45)
versi = sys.version_info
status = "OK" if versi >= (3, 10) else "PERLU UPDATE"
print(f"[{status}] Python {versi.major}.{versi.minor}.{versi.micro}")
print(f"[INFO] Lokasi Python: {sys.executable}")
dalam_venv = sys.prefix != sys.base_prefix
print(f"[{'OK' if dalam_venv else 'INFO'}] Virtual environment aktif: {dalam_venv}")
for lib in ["numpy", "pandas", "matplotlib", "requests", "dotenv"]:
    ada = importlib.util.find_spec(lib) is not None
    print(f"[{'OK' if ada else 'BELUM'}] library {lib}")
print("-" * 45)
print("Library BELUM terpasang? jalankan: python -m pip install -r requirements.txt")
