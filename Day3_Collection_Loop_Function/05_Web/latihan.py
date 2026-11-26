# Latihan 3.5 - TokoKu Day 3 versi Web
import webbrowser
from pathlib import Path

PAJAK = 0.11
LEBAR = 38
MENU = {
    "K01": {"nama": "Kopi Susu Aren", "harga": 25000},
    "K02": {"nama": "Americano", "harga": 22000},
    "T01": {"nama": "Matcha Latte", "harga": 28000},
    "F01": {"nama": "Croissant", "harga": 18000},
    "F02": {"nama": "Cheesecake", "harga": 32000},
}

# ===================== TEMPLATE (JANGAN DIUBAH) =====================
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
    background: linear-gradient(135deg, #101827, #1E2A44 55%, #0F766E);
    font-family: Arial, sans-serif;
  }
  .struk {
    width: 100%;
    max-width: 460px;
    padding: 30px;
    border: 1px solid #ffffff30;
    border-radius: 22px;
    background: #fff;
    box-shadow: 0 24px 70px #0005;
  }
  .label {
    margin: 0;
    color: #0F766E;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    text-align: center;
  }
  h1 { margin: 8px 0 4px; color: #1E2A44; text-align: center; }
  .subjudul { margin: 0 0 22px; color: #64748B; text-align: center; }
  .item {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding: 13px 0;
    border-bottom: 1px solid #E2E8F0;
  }
  .item strong { color: #1E293B; }
  .item-total { white-space: nowrap; }
  .ringkasan { margin-top: 16px; }
  .baris { display: flex; justify-content: space-between; gap: 16px; padding: 7px 0; color: #64748B; }
  .baris strong { color: #1E293B; text-align: right; }
  .total {
    margin-top: 9px;
    padding-top: 16px;
    border-top: 2px dashed #CBD5E1;
    color: #0F766E;
    font-size: 18px;
    font-weight: bold;
  }
  .total strong { color: #0F766E; font-size: 20px; }
  .tombol-cetak {
    display: block;
    margin: 22px auto 0;
    padding: 11px 20px;
    border: 0;
    border-radius: 999px;
    background: #0F766E;
    color: #fff;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
  }
  @media print {
    body { display: block; min-height: 0; padding: 0; background: #fff; }
    .struk {
      width: 100%;
      max-width: none;
      padding: 0;
      border: 0;
      border-radius: 0;
      box-shadow: none;
    }
    .tombol-cetak { display: none; }
    .item, .ringkasan { break-inside: avoid; page-break-inside: avoid; }
  }
</style>
</head>
<body>
<main class="struk">
  <p class="label">TOKOKU COFFEE & BAKERY</p>
  <h1>Struk Belanja</h1>
  <p class="subjudul">Keranjang TokoKu</p>
  __DAFTAR_ITEM__
  <section class="ringkasan">
    <div class="baris"><span>Subtotal</span><strong>__SUBTOTAL__</strong></div>
    <div class="baris"><span>Diskon</span><strong>-__DISKON__</strong></div>
    <div class="baris"><span>Pajak (11%)</span><strong>__PAJAK__</strong></div>
    <div class="baris total"><span>Total bayar</span><strong>__TOTAL__</strong></div>
  </section>
  <button class="tombol-cetak" type="button" onclick="window.print()">Cetak struk</button>
</main>
</body>
</html>"""
# ====================================================================


def rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


def tampilkan_menu():
    # TODO 1: gunakan for untuk menampilkan kode, nama, dan harga dari MENU
    pass


def tambah_ke_keranjang(keranjang, kode, qty):
    # TODO 2: ambil info barang dari MENU dan tambahkan ke keranjang
    pass


def cetak_struk(keranjang):
    # TODO 3: salin perhitungan subtotal, diskon, pajak, dan total dari proyek 04
    # TODO 4: gunakan for untuk membuat baris HTML barang dari keranjang
    # TODO 5: ganti penanda pada TEMPLATE dengan .replace()
    # TODO 6: simpan sebagai struk.html dan buka menggunakan browser
    pass


keranjang = []
tampilkan_menu()

# TODO 7: salin loop input dan validasi dari proyek 04
# TODO 8: jika keranjang berisi barang, panggil cetak_struk()
#         jika kosong, tampilkan pesan transaksi dibatalkan
