"""Uji alur HTTP lokal TokoKu tanpa mengubah transaksi.csv contoh."""
from http.server import HTTPServer
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from unittest.mock import patch

import web_app
from tokoku_oop import Keranjang


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.transaksi_asli = web_app.toko.file_transaksi
        self.nomor_asli = web_app.toko._nomor
        self.output_asli = web_app.OUTPUT
        self.keranjang_asli = web_app.keranjang
        self.nama_asli = web_app.nama_pelanggan
        self.struk_asli = web_app.struk_terakhir
        self.dashboard_asli = web_app.dashboard_path

        web_app.toko.file_transaksi = Path(self.temp.name) / "transaksi.csv"
        web_app.toko._nomor = 0
        web_app.OUTPUT = Path(self.temp.name) / "output"
        web_app.keranjang = Keranjang()
        web_app.nama_pelanggan = ""
        web_app.struk_terakhir = None
        web_app.dashboard_path = None

        self.server = HTTPServer(("127.0.0.1", 0), web_app.TokoKuHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base_url = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        web_app.toko.file_transaksi = self.transaksi_asli
        web_app.toko._nomor = self.nomor_asli
        web_app.OUTPUT = self.output_asli
        web_app.keranjang = self.keranjang_asli
        web_app.nama_pelanggan = self.nama_asli
        web_app.struk_terakhir = self.struk_asli
        web_app.dashboard_path = self.dashboard_asli
        self.temp.cleanup()

    def request(self, path, fields=None):
        data = urlencode(fields or {}).encode("utf-8") if fields is not None else None
        request = Request(self.base_url + path, data=data)
        try:
            with urlopen(request, timeout=5) as response:
                return response.status, response.read().decode("utf-8")
        except HTTPError as error:
            return error.code, error.read().decode("utf-8")

    def mulai_transaksi(self):
        self.request("/transaksi/baru", {})
        self.request(
            "/keranjang/tambah",
            {"pelanggan": "Ayu", "nomor": "1", "ukuran": "S", "qty": "1"},
        )

    def test_checkout_qris_menyimpan_dan_menampilkan_struk(self):
        status, halaman = self.request("/")
        self.assertEqual(status, 200)
        self.assertIn("Transaksi baru", halaman)
        self.assertIn("Konverter dan harga USD", halaman)

        self.mulai_transaksi()
        _, halaman_bayar = self.request("/pembayaran", {"member": "ya"})
        self.assertIn("hanya simulasi", halaman_bayar)
        _, struk = self.request("/checkout/qris", {"member": "ya"})

        self.assertIn("QRIS (simulasi)", struk)
        self.assertIn("Ayu", struk)
        transaksi = web_app.toko.data_transaksi()
        self.assertEqual(transaksi["metode"].tolist(), ["QRIS"])

        _, halaman_dashboard = self.request("/dashboard/buat", {})
        self.assertIn('src="/dashboard.png"', halaman_dashboard)
        with urlopen(self.base_url + "/dashboard.png", timeout=10) as gambar:
            self.assertEqual(gambar.headers.get_content_type(), "image/png")
            self.assertTrue(gambar.read().startswith(b"\x89PNG\r\n\x1a\n"))

    def test_pembayaran_tunai_kurang_tidak_menyimpan_transaksi(self):
        self.mulai_transaksi()
        status, halaman = self.request("/checkout/tunai", {"uang": "1"})

        self.assertEqual(status, 400)
        self.assertIn("Transaksi belum disimpan", halaman)
        self.assertFalse(web_app.toko.file_transaksi.exists())

    def test_konversi_usd_menggunakan_kurs_dan_menampilkan_harga(self):
        with patch("web_app.ambil_kurs_usd", return_value=(0.00006, "data cadangan")):
            _, halaman_usd = self.request("/usd")
            _, hasil_konversi = self.request("/usd/konversi", {"jumlah": "50000"})

        self.assertIn("data cadangan", halaman_usd)
        self.assertIn("1 IDR = 0.0000600 USD", halaman_usd)
        self.assertIn("$3.00", hasil_konversi)


if __name__ == "__main__":
    unittest.main()
