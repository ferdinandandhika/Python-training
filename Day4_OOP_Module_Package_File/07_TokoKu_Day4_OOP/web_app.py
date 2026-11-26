"""Antarmuka web lokal untuk proyek TokoKu Day 4."""
import csv
from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import webbrowser

from tokoku_oop import Keranjang, Minuman, Toko, rupiah

FOLDER = Path(__file__).parent
ALAMAT = "127.0.0.1"
PORT = 8000

toko = Toko.dari_csv(
    FOLDER / "menu.csv",
    file_transaksi=FOLDER / "transaksi.csv",
)
keranjang = Keranjang()
nama_pelanggan = ""
struk_terakhir = None

HALAMAN = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__JUDUL__ - TokoKu</title>
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    min-height: 100vh;
    background: #F1F5F9;
    color: #1E293B;
    font-family: Arial, sans-serif;
  }
  header {
    padding: 22px;
    background: #1E2A44;
    color: white;
  }
  .header-inner, main { width: min(940px, calc(100% - 32px)); margin: auto; }
  header strong { font-size: 21px; letter-spacing: 1px; }
  header span { margin-left: 10px; color: #CBD5E1; }
  main { padding: 30px 0 56px; }
  h1 { margin: 0 0 8px; color: #1E2A44; }
  h2 { margin: 0 0 16px; font-size: 19px; }
  p { line-height: 1.55; }
  .muted { color: #64748B; }
  .card {
    margin: 18px 0;
    padding: 22px;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    background: white;
    box-shadow: 0 8px 24px #0F172A0A;
  }
  .actions { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; }
  .actions form { margin: 0; }
  .actions form button { width: 100%; min-height: 88px; margin: 0; text-align: left; }
  .action {
    display: block;
    min-height: 88px;
    padding: 20px;
    border-radius: 14px;
    background: #0F766E;
    color: white;
    text-decoration: none;
    font-size: 17px;
    font-weight: bold;
  }
  .action.secondary { background: #334155; }
  .number {
    display: inline-grid;
    width: 32px;
    height: 32px;
    margin-right: 10px;
    place-items: center;
    border-radius: 50%;
    background: #FFFFFF2B;
  }
  label { display: block; margin: 14px 0 6px; font-weight: bold; }
  input, select {
    width: 100%;
    min-height: 44px;
    padding: 10px 12px;
    border: 1px solid #CBD5E1;
    border-radius: 9px;
    background: white;
    color: #1E293B;
    font: inherit;
  }
  input[type="checkbox"] { width: 18px; min-height: auto; margin-right: 8px; }
  .check { display: flex; align-items: center; font-weight: normal; }
  button, .button {
    display: inline-block;
    margin-top: 16px;
    padding: 12px 18px;
    border: 0;
    border-radius: 9px;
    background: #0F766E;
    color: white;
    cursor: pointer;
    font: inherit;
    font-weight: bold;
    text-decoration: none;
  }
  button.secondary, .button.secondary { background: #475569; }
  button.danger { background: #B91C1C; }
  .button-row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
  .notice { padding: 13px 15px; border-radius: 10px; background: #FEF3C7; color: #92400E; }
  .success { padding: 13px 15px; border-radius: 10px; background: #CCFBF1; color: #115E59; }
  .cart-row, .summary-row {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding: 12px 0;
    border-bottom: 1px solid #E2E8F0;
  }
  .cart-row small { display: block; margin-top: 4px; color: #64748B; }
  .summary-row.total { border-top: 2px dashed #94A3B8; border-bottom: 0; color: #0F766E; font-size: 19px; font-weight: bold; }
  .table-wrap { overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; }
  th, td { padding: 11px 9px; border-bottom: 1px solid #E2E8F0; text-align: left; white-space: nowrap; }
  th { color: #475569; font-size: 13px; }
  .empty { padding: 18px; border-radius: 10px; background: #F8FAFC; color: #64748B; }
  @media print {
    body { background: white; }
    header, .no-print { display: none !important; }
    main { width: 100%; padding: 0; }
    .card { border: 0; box-shadow: none; }
  }
</style>
</head>
<body>
<header><div class="header-inner"><strong>TOKOKU</strong><span>Kasir Web Lokal</span></div></header>
<main>__ISI__</main>
</body>
</html>"""


def buat_halaman(judul, isi):
    """Masukkan judul dan isi halaman ke dalam template HTML."""
    return HALAMAN.replace("__JUDUL__", escape(judul)).replace("__ISI__", isi)


def halaman_utama(pesan=""):
    """Tampilkan pilihan utama dengan nomor, bukan perintah yang harus diketik."""
    laporan = toko.laporan()
    notifikasi = f'<p class="success">{escape(pesan)}</p>' if pesan else ""
    isi = f"""
    <h1>Selamat datang di {escape(toko.nama)}</h1>
    <p class="muted">Pilih kegiatan dengan menekan tombol. Transaksi disimpan ke file CSV lokal.</p>
    {notifikasi}
    <section class="card">
      <div class="actions">
        <form method="post" action="/transaksi/baru">
          <button class="action" type="submit"><span class="number">1</span>Transaksi baru</button>
        </form>
        <a class="action secondary" href="/laporan"><span class="number">2</span>Laporan penjualan</a>
      </div>
    </section>
    <section class="card">
      <h2>Ringkasan tersimpan</h2>
      <p>Jumlah transaksi: <strong>{laporan["jumlah"]}</strong></p>
      <p>Subtotal barang sebelum diskon dan pajak: <strong>{rupiah(laporan["omzet"])}</strong></p>
      <p class="muted">Data dicatat di <code>transaksi.csv</code>. File ini penyimpanan CSV, bukan database server.</p>
    </section>
    """
    return buat_halaman("Menu utama", isi)


def halaman_transaksi(pesan=""):
    """Tampilkan form pemilihan produk, input jumlah, dan isi keranjang."""
    global nama_pelanggan

    pilihan_menu = []
    for nomor, (kode, produk) in enumerate(toko.katalog.items(), start=1):
        label = f"{nomor}. {kode} - {produk.nama} - mulai {rupiah(produk.harga)}"
        pilihan_menu.append(
            f'<option value="{escape(kode)}">{escape(label)}</option>'
        )

    daftar_barang = []
    for item in keranjang:
        daftar_barang.append(
            '<div class="cart-row">'
            f'<span><strong>{escape(item.produk.deskripsi())}</strong>'
            f'<small>{item.qty} x {rupiah(item.produk.harga_satuan())}</small></span>'
            f'<strong>{rupiah(item.subtotal())}</strong>'
            "</div>"
        )
    tampilan_keranjang = (
        "".join(daftar_barang)
        if daftar_barang
        else '<p class="empty">Keranjang masih kosong. Pilih barang untuk memulai.</p>'
    )
    notifikasi = f'<p class="notice">{escape(pesan)}</p>' if pesan else ""
    pilihan_ukuran = "".join(
        f'<option value="{ukuran}"{" selected" if ukuran == "M" else ""}>{ukuran}</option>'
        for ukuran in Minuman.TAMBAHAN
    )
    tombol_checkout = ""
    if keranjang:
        tombol_checkout = f"""
        <form method="post" action="/transaksi/checkout">
          <input type="hidden" name="pelanggan" value="{escape(nama_pelanggan)}">
          <label class="check"><input type="checkbox" name="member" value="ya"> Pelanggan member (diskon tambahan 5%)</label>
          <div class="button-row">
            <button type="submit">Selesaikan transaksi</button>
          </div>
        </form>
        """

    isi = f"""
    <p><a class="button secondary no-print" href="/">← Menu utama</a></p>
    <h1>Transaksi baru</h1>
    {notifikasi}
    <section class="card no-print">
      <h2>Tambah barang</h2>
      <form method="post" action="/keranjang/tambah">
        <label for="pelanggan">Nama pelanggan</label>
        <input id="pelanggan" name="pelanggan" value="{escape(nama_pelanggan)}" required>
        <label for="kode">Pilih barang</label>
        <select id="kode" name="kode" required>{"".join(pilihan_menu)}</select>
        <label for="ukuran">Ukuran minuman (diabaikan untuk makanan)</label>
        <select id="ukuran" name="ukuran">{pilihan_ukuran}</select>
        <label for="qty">Jumlah</label>
        <input id="qty" name="qty" type="number" min="1" step="1" value="1" required>
        <button type="submit">Tambah ke keranjang</button>
      </form>
    </section>
    <section class="card">
      <h2>Keranjang ({len(keranjang)} item)</h2>
      {tampilan_keranjang}
      <div class="summary-row"><span>Subtotal sementara</span><strong>{rupiah(keranjang.subtotal())}</strong></div>
      {tombol_checkout}
    </section>
    """
    return buat_halaman("Transaksi baru", isi)


def halaman_laporan():
    """Baca dan tampilkan riwayat item transaksi yang tersimpan di CSV."""
    hasil = toko.laporan()
    baris_tabel = []
    if toko.file_transaksi and toko.file_transaksi.exists():
        with open(toko.file_transaksi, encoding="utf-8", newline="") as file_csv:
            for baris in csv.DictReader(file_csv):
                baris_tabel.append(
                    "<tr>"
                    f"<td>{escape(baris['waktu'])}</td>"
                    f"<td>{escape(baris['id_transaksi'])}</td>"
                    f"<td>{escape(baris['nama'])}</td>"
                    f"<td>{escape(baris['qty'])}</td>"
                    f"<td>{rupiah(int(baris['subtotal']))}</td>"
                    "</tr>"
                )
    isi_riwayat = "".join(baris_tabel[-20:])
    if not isi_riwayat:
        isi_riwayat = '<tr><td colspan="5">Belum ada transaksi tersimpan.</td></tr>'

    isi = f"""
    <p><a class="button secondary" href="/">← Menu utama</a></p>
    <h1>Laporan penjualan</h1>
    <section class="card">
      <p>Jumlah transaksi: <strong>{hasil["jumlah"]}</strong></p>
      <p>Subtotal barang sebelum diskon dan pajak: <strong>{rupiah(hasil["omzet"])}</strong></p>
    </section>
    <section class="card">
      <h2>Riwayat barang (maksimal 20 baris terbaru)</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Waktu</th><th>ID transaksi</th><th>Nama barang</th><th>Jumlah</th><th>Subtotal</th></tr></thead>
          <tbody>{isi_riwayat}</tbody>
        </table>
      </div>
    </section>
    """
    return buat_halaman("Laporan penjualan", isi)


def halaman_struk():
    """Tampilkan hasil checkout terakhir dengan tombol cetak."""
    if not struk_terakhir:
        return buat_halaman(
            "Struk",
            '<section class="card"><h1>Belum ada struk</h1><p>Mulai transaksi untuk membuat struk.</p><a class="button" href="/">Menu utama</a></section>',
        )

    rincian = []
    for item in struk_terakhir["items"]:
        rincian.append(
            '<div class="cart-row">'
            f'<span><strong>{escape(item["nama"])}</strong>'
            f'<small>{item["qty"]} x {rupiah(item["harga"])}</small></span>'
            f'<strong>{rupiah(item["subtotal"])}</strong>'
            "</div>"
        )
    ringkasan = struk_terakhir["ringkasan"]
    isi = f"""
    <section class="card">
      <p class="muted">TOKOKU • STRUK TRANSAKSI</p>
      <h1>Terima kasih, {escape(struk_terakhir["pelanggan"])}!</h1>
      {"".join(rincian)}
      <div class="summary-row"><span>Subtotal</span><strong>{rupiah(ringkasan["subtotal"])}</strong></div>
      <div class="summary-row"><span>Diskon</span><strong>-{rupiah(ringkasan["diskon"])}</strong></div>
      <div class="summary-row"><span>Pajak 11%</span><strong>{rupiah(ringkasan["pajak"])}</strong></div>
      <div class="summary-row total"><span>Total bayar</span><strong>{rupiah(ringkasan["total"])}</strong></div>
      <div class="button-row no-print">
        <button type="button" onclick="window.print()">Cetak struk</button>
        <a class="button secondary" href="/">Menu utama</a>
      </div>
    </section>
    """
    return buat_halaman("Struk transaksi", isi)


class TokoKuHandler(BaseHTTPRequestHandler):
    """Tangani permintaan form web lokal TokoKu."""

    def kirim_html(self, isi, status=200):
        data = isi.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def alihkan(self, alamat):
        self.send_response(303)
        self.send_header("Location", alamat)
        self.end_headers()

    def baca_form(self):
        panjang = int(self.headers.get("Content-Length", "0"))
        isi = self.rfile.read(panjang).decode("utf-8")
        return {
            kunci: nilai[0]
            for kunci, nilai in parse_qs(isi, keep_blank_values=True).items()
        }

    def do_GET(self):
        alamat = urlparse(self.path).path
        if alamat == "/":
            self.kirim_html(halaman_utama())
        elif alamat == "/transaksi":
            self.kirim_html(halaman_transaksi())
        elif alamat == "/laporan":
            try:
                self.kirim_html(halaman_laporan())
            except OSError as error:
                self.kirim_html(
                    buat_halaman(
                        "Kesalahan laporan",
                        f'<section class="card"><h1>Gagal membaca laporan</h1><p>{escape(str(error))}</p><a class="button" href="/">Menu utama</a></section>',
                    ),
                    status=500,
                )
        elif alamat == "/struk":
            self.kirim_html(halaman_struk())
        else:
            self.kirim_html(
                buat_halaman("Halaman tidak ditemukan", "<h1>Halaman tidak ditemukan</h1>"),
                status=404,
            )

    def do_POST(self):
        global keranjang, nama_pelanggan, struk_terakhir

        alamat = urlparse(self.path).path
        form = self.baca_form()

        if alamat == "/transaksi/baru":
            keranjang = Keranjang()
            nama_pelanggan = ""
            self.alihkan("/transaksi")
        elif alamat == "/keranjang/tambah":
            nama = form.get("pelanggan", "").strip()
            kode = form.get("kode", "").strip().upper()
            ukuran = form.get("ukuran", "M").strip().upper()
            try:
                qty = int(form.get("qty", ""))
            except ValueError:
                self.kirim_html(halaman_transaksi("Jumlah harus berupa angka bulat."), status=400)
                return

            if not nama:
                self.kirim_html(halaman_transaksi("Nama pelanggan wajib diisi."), status=400)
                return
            nama_pelanggan = nama
            if kode not in toko.katalog:
                self.kirim_html(halaman_transaksi("Pilihan barang tidak tersedia."), status=400)
                return
            if qty <= 0:
                self.kirim_html(halaman_transaksi("Jumlah harus lebih dari nol."), status=400)
                return

            produk = toko.cari(kode)
            if isinstance(produk, Minuman):
                if ukuran not in Minuman.TAMBAHAN:
                    self.kirim_html(halaman_transaksi("Pilih ukuran S, M, atau L."), status=400)
                    return
                produk = produk.dengan_ukuran(ukuran)

            keranjang.tambah(produk, qty)
            self.alihkan("/transaksi")
        elif alamat == "/transaksi/checkout":
            if not keranjang:
                self.kirim_html(halaman_transaksi("Keranjang masih kosong."), status=400)
                return

            member = form.get("member") == "ya"
            items = [
                {
                    "nama": item.produk.deskripsi(),
                    "qty": item.qty,
                    "harga": item.produk.harga_satuan(),
                    "subtotal": item.subtotal(),
                }
                for item in keranjang
            ]
            try:
                ringkasan = toko.checkout(keranjang, member)
            except OSError as error:
                self.kirim_html(
                    halaman_transaksi(f"Tidak dapat menyimpan transaksi: {error}"),
                    status=500,
                )
                return

            struk_terakhir = {
                "pelanggan": nama_pelanggan,
                "items": items,
                "ringkasan": ringkasan,
            }
            keranjang = Keranjang()
            nama_pelanggan = ""
            self.alihkan("/struk")
        else:
            self.kirim_html(
                buat_halaman("Halaman tidak ditemukan", "<h1>Halaman tidak ditemukan</h1>"),
                status=404,
            )


def main():
    server = HTTPServer((ALAMAT, PORT), TokoKuHandler)
    alamat_web = f"http://{ALAMAT}:{PORT}"
    print(f"TokoKu berjalan di {alamat_web}")
    print("Tekan Ctrl+C di terminal untuk menghentikan server.")
    webbrowser.open(alamat_web)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer TokoKu dihentikan.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
