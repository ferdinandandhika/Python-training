"""Antarmuka web lokal untuk proyek TokoKu Final."""
from datetime import datetime
from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import webbrowser

from tokoku_oop import (
    KartuDebit,
    Keranjang,
    Minuman,
    QRIS,
    Toko,
    Tunai,
    ambil_kurs_usd,
    rupiah,
)

FOLDER = Path(__file__).parent
OUTPUT = FOLDER / "output"
ALAMAT = "127.0.0.1"
PORT = 8001

toko = Toko.dari_csv(FOLDER / "menu.csv", file_transaksi=FOLDER / "transaksi.csv")
keranjang = Keranjang()
nama_pelanggan = ""
struk_terakhir = None
dashboard_path = None

TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__JUDUL__ - TokoKu Final</title>
<style>
  * { box-sizing: border-box; }
  body { margin: 0; background: #F1F5F9; color: #1E293B; font-family: Arial, sans-serif; }
  header { padding: 20px; background: #1E2A44; color: white; }
  header div, main { width: min(980px, calc(100% - 32px)); margin: auto; }
  header strong { font-size: 21px; letter-spacing: 1px; }
  header span { margin-left: 10px; color: #CBD5E1; }
  main { padding: 28px 0 52px; }
  h1 { margin: 0 0 8px; color: #1E2A44; }
  h2 { margin: 0 0 16px; font-size: 19px; }
  p { line-height: 1.5; }
  .muted { color: #64748B; }
  .card { margin: 18px 0; padding: 22px; border: 1px solid #E2E8F0; border-radius: 16px; background: white; box-shadow: 0 8px 24px #0F172A0A; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 12px; }
  .grid form { margin: 0; }
  .action { width: 100%; min-height: 76px; padding: 16px; border: 0; border-radius: 12px; background: #0F766E; color: white; cursor: pointer; font: inherit; font-weight: bold; text-align: left; }
  a.action { display: block; text-decoration: none; }
  .action.alt { background: #334155; }
  .number { display: inline-grid; width: 30px; height: 30px; margin-right: 8px; place-items: center; border-radius: 50%; background: #FFFFFF30; }
  label { display: block; margin: 13px 0 6px; font-weight: bold; }
  input, select { width: 100%; min-height: 42px; padding: 9px 11px; border: 1px solid #CBD5E1; border-radius: 8px; background: white; color: #1E293B; font: inherit; }
  input[type="checkbox"] { width: 18px; min-height: 0; margin-right: 8px; }
  .check { display: flex; align-items: center; font-weight: normal; }
  button, .button { display: inline-block; margin-top: 14px; padding: 11px 16px; border: 0; border-radius: 8px; background: #0F766E; color: white; cursor: pointer; font: inherit; font-weight: bold; text-decoration: none; }
  button.secondary, .button.secondary { background: #475569; }
  button.danger { background: #B91C1C; }
  .row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
  .notice { padding: 12px 14px; border-radius: 9px; background: #FEF3C7; color: #92400E; }
  .success { padding: 12px 14px; border-radius: 9px; background: #CCFBF1; color: #115E59; }
  .item, .summary { display: flex; justify-content: space-between; gap: 16px; padding: 11px 0; border-bottom: 1px solid #E2E8F0; }
  .item small { display: block; margin-top: 4px; color: #64748B; }
  .total { border-top: 2px dashed #94A3B8; border-bottom: 0; color: #0F766E; font-size: 19px; font-weight: bold; }
  .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; }
  .stat { padding: 15px; border-radius: 10px; background: #F8FAFC; }
  .stat strong { display: block; margin-top: 6px; color: #0F766E; font-size: 20px; }
  .table-wrap { overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; }
  th, td { padding: 10px 8px; border-bottom: 1px solid #E2E8F0; text-align: left; white-space: nowrap; }
  th { color: #475569; font-size: 13px; }
  .empty { padding: 16px; border-radius: 9px; background: #F8FAFC; color: #64748B; }
  img.dashboard { display: block; width: 100%; height: auto; border: 1px solid #E2E8F0; border-radius: 10px; }
  @media print {
    body { background: white; }
    header, .no-print { display: none !important; }
    main { width: 100%; padding: 0; }
    .card { border: 0; box-shadow: none; }
  }
</style>
</head>
<body>
<header><div><strong>TOKOKU</strong><span>Final Project - Web Lokal</span></div></header>
<main>__ISI__</main>
</body>
</html>"""


def buat_halaman(judul, isi):
    return TEMPLATE.replace("__JUDUL__", escape(judul)).replace("__ISI__", isi)


def halaman_utama(pesan=""):
    ringkasan = toko.laporan()
    notifikasi = f'<p class="success">{escape(pesan)}</p>' if pesan else ""
    if ringkasan["jumlah"]:
        statistik = f"""
        <div class="stats">
          <div class="stat">Jumlah transaksi<strong>{ringkasan["jumlah"]}</strong></div>
          <div class="stat">Subtotal barang<strong>{rupiah(ringkasan["omzet"])}</strong></div>
        </div>
        <p class="muted">Subtotal sebelum diskon dan pajak.</p>
        """
    else:
        statistik = '<p class="empty">Belum ada transaksi tersimpan.</p>'

    isi = f"""
    <h1>Kasir TokoKu</h1>
    <p class="muted">Pilih menu dengan menekan tombol. Transaksi tersimpan di CSV lokal.</p>
    {notifikasi}
    <section class="card">
      <div class="grid">
        <form method="post" action="/transaksi/baru">
          <button class="action" type="submit"><span class="number">1</span>Transaksi baru</button>
        </form>
        <a class="action alt" href="/laporan"><span class="number">2</span>Laporan penjualan</a>
        <form method="post" action="/dashboard/buat">
          <button class="action" type="submit"><span class="number">3</span>Buat dashboard</button>
        </form>
        <a class="action alt" href="/usd"><span class="number">4</span>Konverter dan harga USD</a>
      </div>
    </section>
    <section class="card">
      <h2>Ringkasan penjualan</h2>
      {statistik}
      <p class="muted">QRIS dan kartu debit hanya simulasi latihan. Server hanya tersedia di komputer ini.</p>
      <p class="muted">Hentikan server dengan menekan Ctrl+C di terminal.</p>
    </section>
    """
    return buat_halaman("Menu utama", isi)


def halaman_transaksi(pesan=""):
    pilihan_menu = []
    for nomor, produk in enumerate(toko.katalog.values(), start=1):
        label = f"{nomor}. {produk.nama} - mulai {rupiah(produk.harga)}"
        pilihan_menu.append(f'<option value="{nomor}">{escape(label)}</option>')

    daftar_barang = []
    for item in keranjang:
        daftar_barang.append(
            '<div class="item">'
            f'<span><strong>{escape(item.produk.deskripsi())}</strong>'
            f'<small>{item.qty} x {rupiah(item.produk.harga_satuan())}</small></span>'
            f'<strong>{rupiah(item.subtotal())}</strong>'
            "</div>"
        )
    tampilan_keranjang = (
        "".join(daftar_barang)
        if daftar_barang
        else '<p class="empty">Keranjang masih kosong.</p>'
    )
    notifikasi = f'<p class="notice">{escape(pesan)}</p>' if pesan else ""
    ukuran = "".join(
        f'<option value="{pilihan}"{" selected" if pilihan == "M" else ""}>{pilihan}</option>'
        for pilihan in Minuman.TAMBAHAN
    )

    tombol_lanjut = ""
    if keranjang:
        tombol_lanjut = """
        <form method="post" action="/pembayaran">
          <label class="check"><input type="checkbox" name="member" value="ya"> Member (diskon tambahan 5%)</label>
          <div class="row">
            <button type="submit">Lanjut ke pembayaran</button>
            <button class="danger" formaction="/transaksi/batal">Batalkan transaksi</button>
          </div>
        </form>
        """

    isi = f"""
    <p><a class="button secondary no-print" href="/">Menu utama</a></p>
    <h1>Transaksi baru</h1>
    {notifikasi}
    <section class="card no-print">
      <h2>Tambah barang</h2>
      <form method="post" action="/keranjang/tambah">
        <label for="pelanggan">Nama pelanggan</label>
        <input id="pelanggan" name="pelanggan" value="{escape(nama_pelanggan)}" required>
        <label for="nomor">Pilih barang</label>
        <select id="nomor" name="nomor" required>{"".join(pilihan_menu)}</select>
        <label for="ukuran">Ukuran minuman (makanan mengabaikan pilihan ini)</label>
        <select id="ukuran" name="ukuran">{ukuran}</select>
        <label for="qty">Jumlah</label>
        <input id="qty" name="qty" type="number" min="1" step="1" value="1" required>
        <button type="submit">Tambah ke keranjang</button>
      </form>
    </section>
    <section class="card">
      <h2>Keranjang ({len(keranjang)} barang)</h2>
      {tampilan_keranjang}
      <div class="summary"><span>Subtotal sementara</span><strong>{rupiah(keranjang.subtotal())}</strong></div>
      {tombol_lanjut}
    </section>
    """
    return buat_halaman("Transaksi baru", isi)


def halaman_pembayaran(member=False, pesan=""):
    rincian = toko.hitung(keranjang, member)
    notifikasi = f'<p class="notice">{escape(pesan)}</p>' if pesan else ""
    nilai_member = "ya" if member else "tidak"
    hidden_member = f'<input type="hidden" name="member" value="{nilai_member}">'
    isi = f"""
    <p><a class="button secondary no-print" href="/transaksi">Kembali ke keranjang</a></p>
    <h1>Pilih pembayaran</h1>
    {notifikasi}
    <section class="card">
      <h2>Total yang harus dibayar</h2>
      <div class="summary"><span>Subtotal</span><strong>{rupiah(rincian["subtotal"])}</strong></div>
      <div class="summary"><span>Diskon</span><strong>-{rupiah(rincian["diskon"])}</strong></div>
      <div class="summary"><span>Pajak 11%</span><strong>{rupiah(rincian["pajak"])}</strong></div>
      <div class="summary total"><span>Total</span><strong>{rupiah(rincian["total"])}</strong></div>
    </section>
    <section class="card">
      <p class="notice">QRIS dan kartu debit hanya simulasi. Tidak ada pembayaran sungguhan.</p>
      <div class="grid">
        <form method="post" action="/checkout/tunai">
          {hidden_member}
          <h2>1. Tunai</h2>
          <label for="uang">Uang diterima</label>
          <input id="uang" name="uang" type="number" min="1" required>
          <button type="submit">Bayar tunai</button>
        </form>
        <form method="post" action="/checkout/qris">
          {hidden_member}
          <h2>2. QRIS</h2>
          <p>Simulasi pembayaran QRIS untuk latihan polymorphism.</p>
          <button type="submit">Bayar dengan QRIS</button>
        </form>
        <form method="post" action="/checkout/debit">
          {hidden_member}
          <h2>3. Kartu debit</h2>
          <label for="pin">PIN demo (6 digit)</label>
          <input id="pin" name="pin" type="password" inputmode="numeric" minlength="6" maxlength="6" required>
          <button type="submit">Bayar dengan debit</button>
        </form>
      </div>
    </section>
    """
    return buat_halaman("Pilih pembayaran", isi)


def halaman_struk():
    if not struk_terakhir:
        return buat_halaman(
            "Struk",
            '<section class="card"><h1>Belum ada struk</h1><p>Selesaikan transaksi untuk melihat struk.</p><a class="button" href="/">Menu utama</a></section>',
        )

    baris_barang = []
    for item in struk_terakhir["items"]:
        baris_barang.append(
            '<div class="item">'
            f'<span><strong>{escape(item["nama"])}</strong>'
            f'<small>{item["qty"]} x {rupiah(item["harga"])}</small></span>'
            f'<strong>{rupiah(item["subtotal"])}</strong>'
            "</div>"
        )
    rincian = struk_terakhir["rincian"]
    pembayaran = struk_terakhir["pembayaran"]
    metode = pembayaran["metode"]
    label_metode = metode + (" (simulasi)" if metode in ("QRIS", "Kartu Debit") else "")
    kembalian = ""
    if pembayaran["kembalian"]:
        kembalian = (
            f'<div class="summary"><span>Kembalian</span>'
            f'<strong>{rupiah(pembayaran["kembalian"])}</strong></div>'
        )
    isi = f"""
    <section class="card">
      <p class="muted">TOKOKU - STRUK TRANSAKSI</p>
      <h1>Terima kasih, {escape(struk_terakhir["pelanggan"])}!</h1>
      <p class="muted">{escape(struk_terakhir["waktu"])}</p>
      {"".join(baris_barang)}
      <div class="summary"><span>Subtotal</span><strong>{rupiah(rincian["subtotal"])}</strong></div>
      <div class="summary"><span>Diskon</span><strong>-{rupiah(rincian["diskon"])}</strong></div>
      <div class="summary"><span>Pajak 11%</span><strong>{rupiah(rincian["pajak"])}</strong></div>
      <div class="summary total"><span>Total</span><strong>{rupiah(rincian["total"])}</strong></div>
      <div class="summary"><span>Metode pembayaran</span><strong>{escape(label_metode)}</strong></div>
      {kembalian}
      <div class="row no-print">
        <button type="button" onclick="window.print()">Cetak struk</button>
        <a class="button secondary" href="/">Menu utama</a>
      </div>
    </section>
    """
    return buat_halaman("Struk transaksi", isi)


def halaman_laporan():
    hasil = toko.laporan()
    if not hasil["jumlah"]:
        isi = """
        <p><a class="button secondary" href="/">Menu utama</a></p>
        <section class="card"><h1>Laporan penjualan</h1><p class="empty">Belum ada transaksi.</p></section>
        """
        return buat_halaman("Laporan penjualan", isi)

    ringkasan_jenis = "".join(
        f'<div class="summary"><span>Omzet {escape(str(jenis))}</span>'
        f'<strong>{rupiah(nilai)}</strong></div>'
        for jenis, nilai in hasil["per_jenis"].items()
    )
    ringkasan_metode = "".join(
        f'<div class="summary"><span>{escape(str(metode))}</span>'
        f'<strong>{jumlah} transaksi</strong></div>'
        for metode, jumlah in hasil["per_metode"].items()
    )
    df = toko.data_transaksi()
    baris = []
    for _, row in df.tail(10).iterrows():
        waktu = row["waktu"].strftime("%d-%m-%Y %H:%M")
        baris.append(
            "<tr>"
            f'<td>{escape(str(waktu))}</td>'
            f'<td>{escape(str(row["id_transaksi"]))}</td>'
            f'<td>{escape(str(row["nama"]))}</td>'
            f'<td>{escape(str(row["qty"]))}</td>'
            f'<td>{escape(str(row["metode"]))}</td>'
            f'<td>{rupiah(int(row["subtotal"]))}</td>'
            "</tr>"
        )
    isi = f"""
    <p><a class="button secondary" href="/">Menu utama</a></p>
    <h1>Laporan penjualan</h1>
    <section class="card">
      <div class="stats">
        <div class="stat">Jumlah transaksi<strong>{hasil["jumlah"]}</strong></div>
        <div class="stat">Subtotal barang<strong>{rupiah(hasil["omzet"])}</strong></div>
        <div class="stat">Menu terlaris<strong>{escape(str(hasil["menu_terlaris"]))}</strong></div>
        <div class="stat">Jam tersibuk<strong>{hasil["jam_tersibuk"]:02d}.00</strong></div>
      </div>
      <p class="muted">Subtotal barang dihitung sebelum diskon dan pajak.</p>
      <h2>Omzet per jenis</h2>
      {ringkasan_jenis}
      <h2>Transaksi per metode pembayaran</h2>
      {ringkasan_metode}
    </section>
    <section class="card">
      <h2>10 baris transaksi terbaru</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Waktu</th><th>ID</th><th>Menu</th><th>Qty</th><th>Metode</th><th>Subtotal</th></tr></thead>
          <tbody>{"".join(baris)}</tbody>
        </table>
      </div>
    </section>
    """
    return buat_halaman("Laporan penjualan", isi)


def halaman_dashboard(pesan=""):
    notifikasi = f'<p class="notice">{escape(pesan)}</p>' if pesan else ""
    if dashboard_path and dashboard_path.exists():
        konten = f"""
        <p><img class="dashboard" src="/dashboard.png" alt="Dashboard penjualan TokoKu"></p>
        <form class="no-print" method="post" action="/dashboard/buat">
          <button type="submit">Perbarui dashboard</button>
        </form>
        """
    else:
        konten = f"""
        <p class="empty">Dashboard belum dibuat. Aplikasi akan membuat grafik dari data transaksi.</p>
        <form class="no-print" method="post" action="/dashboard/buat">
          <button type="submit">Buat dashboard</button>
        </form>
        """
    isi = f"""
    <p><a class="button secondary" href="/">Menu utama</a></p>
    <h1>Dashboard penjualan</h1>
    {notifikasi}
    <section class="card">{konten}</section>
    """
    return buat_halaman("Dashboard", isi)


def halaman_usd(kurs=None, sumber="", nominal_idr=None, nominal_usd=None, pesan=""):
    notifikasi = f'<p class="notice">{escape(pesan)}</p>' if pesan else ""
    ringkasan_kurs = ""
    daftar_harga = ""
    hasil_konversi = ""
    if kurs is not None:
        ringkasan_kurs = (
            f'<p class="success">Kurs dari {escape(sumber)}: '
            f'1 IDR = {kurs:.7f} USD</p>'
        )
        baris = []
        for produk in toko.katalog.values():
            harga_usd = produk.harga_satuan() * kurs
            baris.append(
                "<tr>"
                f"<td>{escape(produk.deskripsi())}</td>"
                f"<td>{rupiah(produk.harga_satuan())}</td>"
                f"<td>${harga_usd:.2f}</td>"
                "</tr>"
            )
        daftar_harga = f"""
        <section class="card">
          <h2>Harga menu</h2>
          <div class="table-wrap">
            <table><thead><tr><th>Menu</th><th>Harga IDR</th><th>Harga USD</th></tr></thead>
            <tbody>{"".join(baris)}</tbody></table>
          </div>
        </section>
        """
    if nominal_idr is not None and nominal_usd is not None:
        hasil_konversi = (
            f'<p class="success">{rupiah(nominal_idr)} = '
            f'${nominal_usd:.2f}</p>'
        )

    isi = f"""
    <p><a class="button secondary" href="/">Menu utama</a></p>
    <h1>Konverter Rupiah ke USD</h1>
    {notifikasi}
    {ringkasan_kurs}
    <section class="card">
      <h2>Konversi nominal</h2>
      <form method="post" action="/usd/konversi">
        <label for="jumlah">Jumlah dalam rupiah</label>
        <input id="jumlah" name="jumlah" type="number" min="1" value="{nominal_idr or ''}" required>
        <button type="submit">Konversi ke USD</button>
      </form>
      {hasil_konversi}
    </section>
    {daftar_harga}
    """
    return buat_halaman("Konverter USD", isi)


class TokoKuHandler(BaseHTTPRequestHandler):
    """Melayani halaman dan form web TokoKu di komputer lokal."""

    def kirim_html(self, isi, status=200):
        data = isi.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def kirim_gambar(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "image/png")
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

    def halaman_error(self, judul, pesan, status=400):
        isi = (
            '<section class="card"><h1>'
            f'{escape(judul)}</h1><p class="notice">{escape(pesan)}</p>'
            '<a class="button secondary" href="/">Menu utama</a></section>'
        )
        self.kirim_html(buat_halaman(judul, isi), status)

    def do_GET(self):
        alamat = urlparse(self.path).path
        if alamat == "/":
            self.kirim_html(halaman_utama())
        elif alamat == "/transaksi":
            self.kirim_html(halaman_transaksi())
        elif alamat == "/struk":
            self.kirim_html(halaman_struk())
        elif alamat == "/laporan":
            try:
                self.kirim_html(halaman_laporan())
            except (OSError, ValueError, KeyError) as error:
                self.halaman_error("Gagal membaca laporan", str(error), status=500)
        elif alamat == "/dashboard":
            self.kirim_html(halaman_dashboard())
        elif alamat == "/dashboard.png":
            if not dashboard_path or not dashboard_path.exists():
                self.halaman_error("Dashboard belum tersedia", "Buat dashboard terlebih dahulu.", status=404)
                return
            try:
                self.kirim_gambar(dashboard_path.read_bytes())
            except OSError as error:
                self.halaman_error("Gagal membaca dashboard", str(error), status=500)
        elif alamat == "/usd":
            try:
                kurs, sumber = ambil_kurs_usd()
                self.kirim_html(halaman_usd(kurs=kurs, sumber=sumber))
            except (OSError, ValueError, KeyError) as error:
                self.kirim_html(
                    halaman_usd(pesan=f"Tidak dapat membaca kurs: {error}"),
                    status=500,
                )
        else:
            self.halaman_error("Halaman tidak ditemukan", "Alamat halaman tidak dikenal.", status=404)

    def tambah_barang(self, form):
        global nama_pelanggan

        nama = form.get("pelanggan", "").strip()
        if not nama:
            self.kirim_html(halaman_transaksi("Nama pelanggan wajib diisi."), status=400)
            return
        nama_pelanggan = nama

        try:
            nomor = int(form.get("nomor", ""))
            jumlah = int(form.get("qty", ""))
        except ValueError:
            self.kirim_html(halaman_transaksi("Pilih barang dan masukkan jumlah berupa angka."), status=400)
            return

        daftar_produk = list(toko.katalog.values())
        if not 1 <= nomor <= len(daftar_produk):
            self.kirim_html(halaman_transaksi("Nomor barang tidak tersedia."), status=400)
            return
        if jumlah <= 0:
            self.kirim_html(halaman_transaksi("Jumlah harus lebih dari nol."), status=400)
            return

        produk = daftar_produk[nomor - 1]
        if isinstance(produk, Minuman):
            ukuran = form.get("ukuran", "M").strip().upper()
            if ukuran not in Minuman.TAMBAHAN:
                self.kirim_html(halaman_transaksi("Pilih ukuran S, M, atau L."), status=400)
                return
            produk = produk.dengan_ukuran(ukuran)

        keranjang.tambah(produk, jumlah)
        self.alihkan("/transaksi")

    def selesaikan_pembayaran(self, metode, member):
        global keranjang, nama_pelanggan, struk_terakhir

        if not keranjang:
            self.kirim_html(halaman_transaksi("Keranjang masih kosong."), status=400)
            return

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
            rincian, hasil = toko.checkout(keranjang, metode, member)
        except OSError as error:
            self.kirim_html(
                halaman_pembayaran(member, f"Tidak dapat menyimpan transaksi: {error}"),
                status=500,
            )
            return

        if not hasil.berhasil:
            self.kirim_html(
                halaman_pembayaran(member, f"Pembayaran gagal: {hasil.pesan}. Transaksi belum disimpan."),
                status=400,
            )
            return

        struk_terakhir = {
            "pelanggan": nama_pelanggan,
            "waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "items": items,
            "rincian": rincian,
            "pembayaran": {
                "metode": hasil.metode,
                "dibayar": hasil.dibayar,
                "kembalian": hasil.kembalian,
            },
        }
        keranjang = Keranjang()
        nama_pelanggan = ""
        self.alihkan("/struk")

    def do_POST(self):
        global keranjang, nama_pelanggan, struk_terakhir, dashboard_path

        alamat = urlparse(self.path).path
        form = self.baca_form()

        if alamat == "/transaksi/baru":
            keranjang = Keranjang()
            nama_pelanggan = ""
            struk_terakhir = None
            self.alihkan("/transaksi")
        elif alamat == "/keranjang/tambah":
            self.tambah_barang(form)
        elif alamat == "/transaksi/batal":
            keranjang = Keranjang()
            nama_pelanggan = ""
            self.alihkan("/")
        elif alamat == "/pembayaran":
            if not keranjang:
                self.kirim_html(halaman_transaksi("Keranjang masih kosong."), status=400)
                return
            member = form.get("member") == "ya"
            self.kirim_html(halaman_pembayaran(member))
        elif alamat == "/checkout/tunai":
            member = form.get("member") == "ya"
            try:
                uang = int(form.get("uang", ""))
            except ValueError:
                self.kirim_html(halaman_pembayaran(member, "Masukkan jumlah uang berupa angka."), status=400)
                return
            if uang <= 0:
                self.kirim_html(halaman_pembayaran(member, "Jumlah uang harus lebih dari nol."), status=400)
                return
            self.selesaikan_pembayaran(Tunai(uang), member)
        elif alamat == "/checkout/qris":
            self.selesaikan_pembayaran(QRIS(), form.get("member") == "ya")
        elif alamat == "/checkout/debit":
            self.selesaikan_pembayaran(
                KartuDebit(form.get("pin", "")),
                form.get("member") == "ya",
            )
        elif alamat == "/dashboard/buat":
            try:
                dashboard_path = toko.dashboard(OUTPUT)
            except (ImportError, OSError, ValueError) as error:
                self.kirim_html(halaman_dashboard(f"Gagal membuat dashboard: {error}"), status=500)
                return
            if dashboard_path is None:
                self.kirim_html(halaman_dashboard("Belum ada transaksi untuk dibuatkan dashboard."))
                return
            self.alihkan("/dashboard")
        elif alamat == "/usd/konversi":
            try:
                jumlah_idr = int(form.get("jumlah", ""))
            except ValueError:
                self.kirim_html(halaman_usd(pesan="Masukkan nominal rupiah berupa angka."), status=400)
                return
            if jumlah_idr <= 0:
                self.kirim_html(halaman_usd(pesan="Nominal harus lebih dari nol."), status=400)
                return
            try:
                kurs, sumber = ambil_kurs_usd()
            except (OSError, ValueError, KeyError) as error:
                self.kirim_html(halaman_usd(pesan=f"Tidak dapat membaca kurs: {error}"), status=500)
                return
            self.kirim_html(
                halaman_usd(
                    kurs=kurs,
                    sumber=sumber,
                    nominal_idr=jumlah_idr,
                    nominal_usd=jumlah_idr * kurs,
                )
            )
        else:
            self.halaman_error("Halaman tidak ditemukan", "Alamat halaman tidak dikenal.", status=404)


def main():
    server = HTTPServer((ALAMAT, PORT), TokoKuHandler)
    alamat_web = f"http://{ALAMAT}:{PORT}"
    print(f"TokoKu Final berjalan di {alamat_web}")
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
