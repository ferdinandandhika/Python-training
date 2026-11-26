# Solusi 1.5 - Struk TokoKu versi HTML
import webbrowser  # Impor modul untuk membuka halaman HTML yang dibuat menggunakan browser bawaan komputer.
from pathlib import Path  # Impor Path untuk menyusun dan mengelola alamat file secara lintas sistem operasi.

# ===================== TEMPLATE (JANGAN DIUBAH) =====================
TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="3">
<title>Struk TokoKu</title>
<style>
  body   { font-family: Arial; background: #1E2A44; display: flex; justify-content: center; padding-top: 60px; }
  .struk { background: white; width: 300px; padding: 24px; border-radius: 10px; }
  h1     { text-align: center; color: #1E2A44; margin: 0 0 16px; }
  .baris { display: flex; justify-content: space-between; padding: 4px 0; }
  .total { border-top: 2px dashed #999; margin-top: 10px; padding-top: 10px; font-weight: bold; color: #0F766E; }
  p      { text-align: center; }
</style>
</head>
<body>
<div class="struk">
  <h1>TOKOKU</h1>
  <div class="baris"><span>Pelanggan</span><span>__NAMA__</span></div>
  <div class="baris"><span>Menu</span><span>__MENU__</span></div>
  <div class="baris"><span>Harga</span><span>__HARGA__</span></div>
  <div class="baris"><span>Jumlah</span><span>__JUMLAH__</span></div>
  <div class="baris total"><span>TOTAL</span><span>__TOTAL__</span></div>
  <p>Terima kasih, __NAMA__!</p>
</div>
</body>
</html>"""  # Simpan templat HTML dan CSS lengkap sebagai teks; bagian __...__ akan diganti dengan data struk.
# ====================================================================

# TODO 1: input
nama = input("Nama pelanggan : ").strip().title()  # Minta nama pelanggan, rapikan spasi tepi, dan ubah awal kata menjadi kapital.
menu = input("Menu           : ").strip().title()  # Minta nama menu, rapikan spasi tepi, dan samakan kapitalisasinya.
harga = int(input("Harga          : "))  # Minta harga sebagai teks lalu ubah menjadi bilangan bulat untuk operasi hitung.
jumlah = int(input("Jumlah         : "))  # Minta jumlah barang lalu ubah menjadi bilangan bulat agar dapat dikalikan.

# TODO 2: hitung total
total = harga * jumlah  # Kalikan harga dan jumlah untuk memperoleh total belanja sebelum dimasukkan ke struk.


# TODO 3: format Rupiah
def rupiah(angka):  # Sediakan fungsi pemformat agar harga dan total memakai tampilan Rupiah yang sama.
    return "Rp " + f"{angka:,}".replace(",", ".")  # Beri pemisah ribuan pada angka, ubah koma menjadi titik, dan tambahkan awalan Rp.


# TODO 4: isi template
html = TEMPLATE  # Salin teks templat ke variabel kerja agar nilai templat asli tetap tersedia.
html = html.replace("__NAMA__", nama)  # Ganti penanda nama pelanggan di dalam HTML dengan nama yang dimasukkan.
html = html.replace("__MENU__", menu)  # Ganti penanda menu di dalam HTML dengan nama menu pesanan.
html = html.replace("__HARGA__", rupiah(harga))  # Ganti penanda harga dengan harga yang sudah diformat sebagai Rupiah.
html = html.replace("__JUMLAH__", str(jumlah))  # Ganti penanda jumlah dengan teks dari jumlah barang.
html = html.replace("__TOTAL__", rupiah(total))  # Ganti penanda total dengan total belanja yang sudah diformat sebagai Rupiah.

# ========== BAGIAN INI SUDAH JADI: simpan dan buka di browser ==========
file = Path(__file__).parent / "struk.html"  # Buat alamat file struk.html di folder yang sama dengan skrip ini.
file.write_text(html, encoding="utf-8")  # Tulis HTML yang sudah diisi ke file dengan encoding UTF-8 agar karakter tersimpan benar.
print("Struk tersimpan di", file)  # Beri tahu pengguna lokasi file HTML yang baru disimpan.
webbrowser.open(file.as_uri())  # Ubah alamat file menjadi URI lalu minta browser membukanya untuk menampilkan struk.