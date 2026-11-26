# Solusi 2.5 - TokoKu Day 2 versi Web
from html import escape  # Mengimpor fungsi escape untuk mengamankan teks pelanggan saat dimasukkan ke HTML.
import webbrowser  # Mengimpor modul untuk membuka struk HTML di peramban bawaan.
from pathlib import Path  # Mengimpor Path agar lokasi dan berkas struk ditangani dengan cara lintas platform.

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
</html>"""  # Menyimpan kerangka HTML/CSS struk beserta penanda yang nanti diganti dengan data transaksi.

nama = input("Nama pelanggan: ").strip().title()  # Meminta nama pelanggan, membersihkan spasi tepi, dan merapikan kapitalisasi.
print("\nMenu TokoKu")  # Menampilkan judul daftar menu dengan baris kosong sebelumnya.
print("1. Kopi Susu Aren - Rp 25.000")  # Menampilkan pilihan menu pertama dan harganya.
print("2. Matcha Latte    - Rp 28.000")  # Menampilkan pilihan menu kedua dan harganya.
print("3. Croissant       - Rp 18.000")  # Menampilkan pilihan menu ketiga dan harganya.
pilihan_teks = input("Pilih nomor menu: ")  # Meminta nomor pilihan menu sebagai teks untuk dikonversi kemudian.
jumlah_teks = input("Jumlah: ")  # Meminta jumlah barang sebagai teks untuk dikonversi kemudian.

try:  # Mencoba mengubah nomor pilihan dan jumlah menjadi angka bulat.
    pilihan_menu = int(pilihan_teks)  # Mengubah nomor menu menjadi bilangan bulat agar dapat dicocokkan.
    jumlah = int(jumlah_teks)  # Mengubah jumlah pesanan menjadi bilangan bulat.
except ValueError:  # Menangani masukan yang tidak dapat diubah menjadi bilangan bulat.
    print("Pilihan menu dan jumlah harus berupa angka bulat.")  # Menjelaskan bahwa setidaknya satu masukan bukan bilangan bulat.
else:  # Memeriksa dan memproses transaksi hanya setelah kedua konversi berhasil.
    menu_valid = True  # Menganggap pilihan valid dahulu, lalu akan mengubahnya jika nomor tidak dikenal.
    if pilihan_menu == 1:  # Memeriksa apakah pelanggan memilih menu pertama.
        menu = "Kopi Susu Aren"  # Menyimpan nama menu pertama untuk perhitungan dan struk.
        harga = 25_000  # Menyimpan harga menu pertama dalam satuan rupiah.
    elif pilihan_menu == 2:  # Memeriksa pilihan menu kedua jika pilihan pertama tidak cocok.
        menu = "Matcha Latte"  # Menyimpan nama menu kedua untuk perhitungan dan struk.
        harga = 28_000  # Menyimpan harga menu kedua dalam satuan rupiah.
    elif pilihan_menu == 3:  # Memeriksa pilihan menu ketiga jika dua pilihan sebelumnya tidak cocok.
        menu = "Croissant"  # Menyimpan nama menu ketiga untuk perhitungan dan struk.
        harga = 18_000  # Menyimpan harga menu ketiga dalam satuan rupiah.
    else:  # Menangani nomor pilihan yang tidak sama dengan menu mana pun.
        menu_valid = False  # Menandai bahwa nomor menu tidak cocok dengan pilihan yang tersedia.
        print("Pilihan menu tidak tersedia.")  # Memberi tahu pelanggan bahwa nomor tersebut tidak ada pada daftar.

    if menu_valid:  # Melanjutkan transaksi hanya jika nomor menu berhasil dikenali.
        if jumlah <= 0:  # Menolak jumlah nol atau negatif karena pesanan harus berisi barang.
            print("Jumlah harus lebih dari nol.")  # Menjelaskan syarat jumlah minimum kepada pelanggan.
        else:  # Menghitung dan membuat struk hanya untuk jumlah pesanan yang positif.
            subtotal = harga * jumlah  # Mengalikan harga per barang dengan jumlah untuk mendapatkan subtotal.
            if subtotal >= 200_000:  # Memeriksa ambang diskon tertinggi terlebih dahulu.
                persen_diskon = 0.15  # Menetapkan diskon 15 persen untuk subtotal minimal 200.000.
            elif subtotal >= 100_000:  # Memeriksa ambang diskon berikutnya jika ambang tertinggi tidak tercapai.
                persen_diskon = 0.10  # Menetapkan diskon 10 persen untuk subtotal minimal 100.000.
            else:  # Menetapkan nol persen jika subtotal belum memenuhi ambang diskon.
                persen_diskon = 0  # Tidak memberi diskon jika subtotal di bawah kedua ambang.

            diskon = round(subtotal * persen_diskon)  # Menghitung nominal diskon lalu membulatkannya menjadi rupiah bulat.
            setelah_diskon = subtotal - diskon  # Menghitung sisa pembayaran setelah diskon dikurangi.
            pajak = round(setelah_diskon * 0.11)  # Menghitung pajak 11 persen dari nilai setelah diskon dan membulatkannya.
            total = setelah_diskon + pajak  # Menjumlahkan sisa pembayaran dan pajak untuk memperoleh total transaksi.

            html = TEMPLATE  # Menyalin kerangka HTML agar penanda dapat diisi tanpa mengubah template aslinya.
            html = html.replace("__MENU__", menu)  # Mengganti penanda nama menu dengan nama menu yang dipilih.
            html = html.replace("__HARGA__", f"Rp {harga:,.0f}".replace(",", "."))  # Mengisi harga yang sudah diformat sebagai rupiah dengan titik ribuan.
            html = html.replace("__JUMLAH__", str(jumlah))  # Mengganti penanda jumlah dengan teks dari angka pesanan.
            html = html.replace("__SUBTOTAL__", f"Rp {subtotal:,.0f}".replace(",", "."))  # Mengisi subtotal dengan format rupiah tanpa desimal.
            html = html.replace(
                "__PERSEN_DISKON__", f"{persen_diskon:.0%}"
            )  # Mengganti penanda persentase diskon dengan persentase tanpa angka desimal.
            html = html.replace("__DISKON__", f"Rp {diskon:,.0f}".replace(",", "."))  # Mengisi nominal diskon dengan format rupiah.
            html = html.replace("__PAJAK__", f"Rp {pajak:,.0f}".replace(",", "."))  # Mengisi nominal pajak dengan format rupiah.
            html = html.replace("__TOTAL__", f"Rp {total:,.0f}".replace(",", "."))  # Mengisi total akhir pembayaran dengan format rupiah.
            html = html.replace("__NAMA__", escape(nama))  # Mengamankan teks nama lalu mengganti semua penanda nama pada HTML.

            file = (Path(__file__).parent / "struk.html").resolve()  # Menentukan lokasi struk di folder skrip lalu memperoleh path absolut.
            file.write_text(html, encoding="utf-8")  # Menulis HTML yang telah diisi ke berkas dengan pengodean UTF-8.
            print("Struk tersimpan di", file)  # Menampilkan lokasi penyimpanan agar pengguna dapat menemukannya.
            webbrowser.open(file.as_uri())  # Membuka berkas struk menggunakan URL lokal di peramban bawaan.
