# Solusi 2.5 - TokoKu Day 2 versi Web
from html import escape
import webbrowser
from pathlib import Path

TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Struk TokoKu</title>
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 24px;
    background: #1E2A44;
    font-family: Arial, sans-serif;
  }
  .struk {
    width: 100%;
    max-width: 380px;
    padding: 28px;
    border-radius: 16px;
    background: #fff;
    box-shadow: 0 16px 40px #10182766;
  }
  .label {
    margin: 0;
    color: #0F766E;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 2px;
    text-align: center;
  }
  h1 {
    margin: 8px 0 4px;
    color: #1E2A44;
    text-align: center;
  }
  .subjudul {
    margin: 0 0 24px;
    color: #64748B;
    text-align: center;
  }
  .baris {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding: 10px 0;
    border-bottom: 1px solid #E2E8F0;
  }
  .baris span { color: #64748B; }
  .baris strong { color: #1E293B; text-align: right; }
  .diskon strong { color: #0F766E; }
  .total {
    margin-top: 8px;
    padding-top: 16px;
    border-top: 2px dashed #94A3B8;
    border-bottom: 0;
  }
  .total span, .total strong {
    color: #0F766E;
    font-size: 18px;
    font-weight: bold;
  }
  .terima-kasih {
    margin: 20px 0 0;
    color: #64748B;
    text-align: center;
  }
</style>
</head>
<body>
<main class="struk">
  <p class="label">PEMBAYARAN BERHASIL</p>
  <h1>TOKOKU</h1>
  <p class="subjudul">Ringkasan transaksi</p>
  <div class="baris"><span>Pelanggan</span><strong>__NAMA__</strong></div>
  <div class="baris"><span>Menu</span><strong>__MENU__</strong></div>
  <div class="baris"><span>Harga satuan</span><strong>__HARGA__</strong></div>
  <div class="baris"><span>Jumlah</span><strong>__JUMLAH__</strong></div>
  <div class="baris"><span>Subtotal</span><strong>__SUBTOTAL__</strong></div>
  <div class="baris diskon"><span>Diskon (__PERSEN_DISKON__)</span><strong>-__DISKON__</strong></div>
  <div class="baris"><span>Pajak (11%)</span><strong>__PAJAK__</strong></div>
  <div class="baris total"><span>Total bayar</span><strong>__TOTAL__</strong></div>
  <p class="terima-kasih">Terima kasih, __NAMA__!</p>
</main>
</body>
</html>"""

nama = input("Nama pelanggan: ").strip().title()
print("\nMenu TokoKu")
print("1. Kopi Susu Aren - Rp 25.000")
print("2. Matcha Latte    - Rp 28.000")
print("3. Croissant       - Rp 18.000")
pilihan_teks = input("Pilih nomor menu: ")
jumlah_teks = input("Jumlah: ")

try:
    pilihan_menu = int(pilihan_teks)
    jumlah = int(jumlah_teks)
except ValueError:
    print("Pilihan menu dan jumlah harus berupa angka bulat.")
else:
    menu_valid = True
    if pilihan_menu == 1:
        menu = "Kopi Susu Aren"
        harga = 25_000
    elif pilihan_menu == 2:
        menu = "Matcha Latte"
        harga = 28_000
    elif pilihan_menu == 3:
        menu = "Croissant"
        harga = 18_000
    else:
        menu_valid = False
        print("Pilihan menu tidak tersedia.")

    if menu_valid:
        if jumlah <= 0:
            print("Jumlah harus lebih dari nol.")
        else:
            subtotal = harga * jumlah
            if subtotal >= 200_000:
                persen_diskon = 0.15
            elif subtotal >= 100_000:
                persen_diskon = 0.10
            else:
                persen_diskon = 0

            diskon = round(subtotal * persen_diskon)
            setelah_diskon = subtotal - diskon
            pajak = round(setelah_diskon * 0.11)
            total = setelah_diskon + pajak

            html = TEMPLATE
            html = html.replace("__MENU__", menu)
            html = html.replace("__HARGA__", f"Rp {harga:,.0f}".replace(",", "."))
            html = html.replace("__JUMLAH__", str(jumlah))
            html = html.replace("__SUBTOTAL__", f"Rp {subtotal:,.0f}".replace(",", "."))
            html = html.replace(
                "__PERSEN_DISKON__", f"{persen_diskon:.0%}"
            )
            html = html.replace("__DISKON__", f"Rp {diskon:,.0f}".replace(",", "."))
            html = html.replace("__PAJAK__", f"Rp {pajak:,.0f}".replace(",", "."))
            html = html.replace("__TOTAL__", f"Rp {total:,.0f}".replace(",", "."))
            html = html.replace("__NAMA__", escape(nama))

            file = (Path(__file__).parent / "struk.html").resolve()
            file.write_text(html, encoding="utf-8")
            print("Struk tersimpan di", file)
            webbrowser.open(file.as_uri())
