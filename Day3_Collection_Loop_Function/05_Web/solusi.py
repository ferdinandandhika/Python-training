# Solusi 3.5 - TokoKu Day 3 versi Web
import webbrowser  # Impor alat untuk membuka berkas hasil struk melalui peramban web.
from pathlib import Path  # Impor Path untuk menyusun lokasi berkas secara lintas platform.

PAJAK = 0.11  # Simpan tarif pajak 11% agar dipakai secara konsisten saat menghitung transaksi.
LEBAR = 38  # Simpan lebar tampilan struk yang digunakan bersama perhitungan.
MENU = {  # Simpan data produk dengan kode sebagai kunci untuk mencari nama dan harga.
    "K01": {"nama": "Kopi Susu Aren", "harga": 25000},  # Catat kopi susu aren dengan kode K01 dan harganya.
    "K02": {"nama": "Americano", "harga": 22000},  # Catat americano dengan kode K02 dan harganya.
    "T01": {"nama": "Matcha Latte", "harga": 28000},  # Catat matcha latte dengan kode T01 dan harganya.
    "F01": {"nama": "Croissant", "harga": 18000},  # Catat croissant dengan kode F01 dan harganya.
    "F02": {"nama": "Cheesecake", "harga": 32000},  # Catat cheesecake dengan kode F02 dan harganya.
}  # Akhiri kamus daftar produk yang digunakan selama transaksi.

# TEMPLATE berisi kerangka HTML/CSS struk; penanda di dalamnya akan diisi dengan data transaksi.
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


def rupiah(angka):  # Buat fungsi untuk menyajikan nilai angka sebagai teks rupiah.
    return "Rp " + f"{angka:,.0f}".replace(",", ".")  # Tambahkan awalan mata uang dan ubah koma ribuan menjadi titik.


def tampilkan_menu():  # Buat fungsi untuk menampilkan kode, nama, dan harga semua produk.
    print("MENU TOKOKU")  # Tampilkan judul daftar menu.
    for kode, info in MENU.items():  # Ambil kode dan data masing-masing produk dari kamus MENU.
        print(f"  {kode}  {info['nama']:<16} {rupiah(info['harga'])}")  # Tampilkan rincian produk dengan format kolom dan harga rupiah.


def tambah_ke_keranjang(keranjang, kode, qty):  # Buat fungsi untuk memasukkan produk dan jumlahnya ke keranjang.
    info = MENU[kode]  # Ambil rincian produk dari menu berdasarkan kode yang dipilih.
    barang = {"nama": info["nama"], "harga": info["harga"], "qty": qty}  # Bentuk data transaksi berisi nama, harga, dan jumlah.
    keranjang.append(barang)  # Tambahkan data transaksi tersebut ke list keranjang.


def cetak_struk(keranjang):  # Buat fungsi yang menghitung transaksi lalu menghasilkan struk web.
    subtotal = 0  # Mulai penjumlahan harga barang sebelum diskon dan pajak dari nol.
    baris_item = ""  # Siapkan teks kosong untuk menampung HTML setiap barang.

    for barang in keranjang:  # Proses satu per satu barang yang dipilih.
        total_barang = barang["harga"] * barang["qty"]  # Hitung harga total untuk satu jenis barang.
        subtotal += total_barang  # Tambahkan biaya barang ke subtotal seluruh keranjang.
        baris_item += (  # Gabungkan beberapa potongan teks menjadi satu baris HTML untuk barang ini.
            '<div class="item">'  # Buka elemen HTML yang menampung tampilan satu barang.
            f'<strong>{barang["nama"]} x{barang["qty"]}</strong>'  # Masukkan nama dan jumlah barang ke bagian tebal HTML.
            f'<strong class="item-total">{rupiah(total_barang)}</strong>'  # Masukkan total harga barang dengan format rupiah.
            "</div>"  # Tutup elemen HTML untuk barang ini.
        )  # Selesaikan penggabungan teks HTML dan tambahkan ke baris_item.

    if subtotal >= 200_000:  # Periksa apakah subtotal mencapai syarat diskon tertinggi.
        persen_diskon = 0.15  # Gunakan diskon 15% jika subtotal minimal 200.000.
    elif subtotal >= 100_000:  # Jika tidak, periksa apakah subtotal mencapai syarat diskon berikutnya.
        persen_diskon = 0.10  # Gunakan diskon 10% jika subtotal minimal 100.000.
    else:  # Jalankan cabang ini jika subtotal belum memenuhi syarat diskon.
        persen_diskon = 0  # Tetapkan persentase diskon menjadi nol.

    diskon = subtotal * persen_diskon  # Hitung nilai diskon dari subtotal dan persentase yang dipilih.
    setelah_diskon = subtotal - diskon  # Kurangi diskon untuk mendapatkan nilai sebelum pajak.
    pajak = setelah_diskon * PAJAK  # Hitung pajak berdasarkan nilai setelah diskon.
    total = setelah_diskon + pajak  # Tambahkan pajak untuk mendapatkan jumlah pembayaran akhir.

    html = TEMPLATE.replace("__DAFTAR_ITEM__", baris_item)  # Isi penanda daftar barang pada templat dengan baris HTML hasil perulangan.
    html = html.replace("__SUBTOTAL__", rupiah(subtotal))  # Ganti penanda subtotal dengan angka yang sudah diformat sebagai rupiah.
    html = html.replace("__DISKON__", rupiah(diskon))  # Ganti penanda diskon dengan nilai diskon berformat rupiah.
    html = html.replace("__PAJAK__", rupiah(pajak))  # Ganti penanda pajak dengan nilai pajak berformat rupiah.
    html = html.replace("__TOTAL__", rupiah(total))  # Ganti penanda total pembayaran dengan jumlah akhir berformat rupiah.

    file = Path(__file__).parent / "struk.html"  # Tentukan berkas struk.html di folder yang sama dengan skrip ini.
    file.write_text(html, encoding="utf-8")  # Tulis HTML struk ke berkas menggunakan pengodean teks UTF-8.
    print("Struk tersimpan di", file)  # Beri tahu pengguna lokasi berkas struk yang baru dibuat.
    webbrowser.open(file.resolve().as_uri())  # Ubah lokasi menjadi alamat berkas lalu buka melalui peramban web.


keranjang = []  # Buat list kosong untuk mengumpulkan barang yang akan dibeli.
tampilkan_menu()  # Tampilkan semua produk sebelum meminta masukan transaksi.

while True:  # Ulangi pemilihan produk sampai pengguna memasukkan perintah selesai.
    kode = input("\nKode barang (atau selesai): ").strip().upper()  # Baca kode, hapus spasi pinggir, dan ubah menjadi huruf kapital.
    if kode == "SELESAI":  # Periksa apakah pengguna ingin berhenti memilih barang.
        break  # Akhiri perulangan input barang.

    if kode not in MENU:  # Pastikan kode yang dimasukkan terdapat di daftar produk.
        print("Kode barang tidak ditemukan.")  # Beri tahu pengguna jika kode tidak cocok dengan menu.
        continue  # Kembali meminta kode tanpa melanjutkan ke input jumlah.

    try:  # Coba membaca jumlah dan mengubahnya menjadi bilangan bulat.
        qty = int(input("Jumlah: "))  # Minta jumlah barang, lalu ubah teks masukan menjadi integer.
    except ValueError:  # Tangani kesalahan jika masukan jumlah bukan bilangan bulat.
        print("Jumlah harus berupa angka bulat.")  # Jelaskan jenis nilai jumlah yang dapat diterima.
        continue  # Kembali ke awal agar pengguna bisa memasukkan ulang kode dan jumlah.

    if qty <= 0:  # Tolak jumlah nol atau negatif agar keranjang berisi jumlah yang valid.
        print("Jumlah harus lebih dari nol.")  # Beri tahu bahwa jumlah wajib lebih besar daripada nol.
        continue  # Ulangi pemilihan karena jumlah barang tidak valid.

    tambah_ke_keranjang(keranjang, kode, qty)  # Simpan data produk dan jumlah yang sudah lolos pemeriksaan.

if keranjang:  # Periksa apakah setidaknya satu barang telah dimasukkan ke keranjang.
    cetak_struk(keranjang)  # Hitung transaksi, simpan struk HTML, dan buka hasilnya di peramban.
else:  # Gunakan cabang ini jika keranjang tetap kosong setelah pemilihan selesai.
    print("Keranjang kosong. Transaksi dibatalkan.")  # Tampilkan pesan bahwa struk tidak dibuat untuk transaksi kosong.
