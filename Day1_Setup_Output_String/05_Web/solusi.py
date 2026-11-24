# Solusi 1.5 - Struk TokoKu versi HTML
import webbrowser
from pathlib import Path

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
</html>"""
# ====================================================================

# TODO 1: input
nama = input("Nama pelanggan : ").strip().title()
menu = input("Menu           : ").strip().title()
harga = int(input("Harga          : "))
jumlah = int(input("Jumlah         : "))

# TODO 2: hitung total
total = harga * jumlah


# TODO 3: format Rupiah
def rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")


# TODO 4: isi template
html = TEMPLATE
html = html.replace("__NAMA__", nama)
html = html.replace("__MENU__", menu)
html = html.replace("__HARGA__", rupiah(harga))
html = html.replace("__JUMLAH__", str(jumlah))
html = html.replace("__TOTAL__", rupiah(total))

# ========== BAGIAN INI SUDAH JADI: simpan dan buka di browser ==========
file = Path(__file__).parent / "struk.html"
file.write_text(html, encoding="utf-8")
print("Struk tersimpan di", file)
webbrowser.open(file.as_uri())