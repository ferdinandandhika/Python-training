"""Unit test TokoKu Final OOP. Jalankan: python -m unittest -v"""
import tempfile
import unittest
from pathlib import Path

from tokoku_oop import (KartuDebit, Keranjang, Makanan, MetodePembayaran, Minuman, QRIS, Toko, Tunai,
                        ambil_kurs_usd)

FOLDER = Path(__file__).parent


class TestProduk(unittest.TestCase):
    def test_minuman_ukuran_menambah_harga(self):
        self.assertEqual(Minuman("K01", "Kopi", 25000, "L").harga_satuan(), 31000)

    def test_ukuran_tidak_valid(self):
        with self.assertRaises(ValueError):
            Minuman("K01", "Kopi", 25000, "XL")

    def test_harga_harus_positif(self):
        with self.assertRaises(ValueError):
            Makanan("F01", "Roti", 0)


class TestKeranjang(unittest.TestCase):
    def setUp(self):
        self.k = Keranjang()
        self.kopi = Minuman("K01", "Kopi", 25000, "S")
        self.roti = Makanan("F01", "Roti", 18000)

    def test_produk_sama_digabung(self):
        self.k.tambah(self.kopi, 2)
        self.k.tambah(self.kopi, 1)
        self.assertEqual(len(self.k), 3)
        self.assertEqual(self.k.subtotal(), 75000)

    def test_kurangi_sampai_habis(self):
        self.k.tambah(self.roti, 1)
        self.k.kurangi("F01", 1)
        self.assertNotIn("F01", self.k)
        self.assertFalse(self.k)


class TestPembayaran(unittest.TestCase):
    def test_abstract_tidak_bisa_dibuat(self):
        with self.assertRaises(TypeError):
            MetodePembayaran()

    def test_tunai_kembalian(self):
        self.assertEqual(Tunai(100_000).proses(87_000).kembalian, 13_000)

    def test_tunai_kurang(self):
        self.assertFalse(Tunai(50_000).proses(87_000).berhasil)

    def test_debit_pin_salah(self):
        self.assertFalse(KartuDebit("12ab").proses(10_000).berhasil)


class TestToko(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.toko = Toko.dari_csv(FOLDER / "menu.csv", file_transaksi=Path(self.tmp.name) / "trx.csv")

    def tearDown(self):
        self.tmp.cleanup()

    def test_muat_menu_sesuai_jenis(self):
        self.assertIsInstance(self.toko.cari("K01"), Minuman)
        self.assertIsInstance(self.toko.cari("F01"), Makanan)

    def test_kode_tidak_ada(self):
        with self.assertRaises(KeyError):
            self.toko.cari("X99")

    def test_diskon_member(self):
        self.assertAlmostEqual(Toko.persen_diskon(250_000, member=True), 0.20)
        self.assertAlmostEqual(Toko.persen_diskon(50_000), 0.0)

    def test_checkout_menyimpan_transaksi(self):
        k = Keranjang()
        k.tambah(self.toko.cari("F02"), 4)            # 128.000 -> diskon 10%
        rincian, hasil = self.toko.checkout(k, QRIS())
        self.assertTrue(hasil.berhasil)
        self.assertEqual(rincian["diskon"], 12_800)
        self.assertEqual(rincian["total"], 127_872)
        lap = self.toko.laporan()
        self.assertEqual((lap["jumlah"], lap["omzet"]), (1, 128_000))

    def test_checkout_gagal_tidak_disimpan(self):
        k = Keranjang()
        k.tambah(self.toko.cari("K01"), 1)
        _, hasil = self.toko.checkout(k, Tunai(1_000))
        self.assertFalse(hasil.berhasil)
        self.assertEqual(self.toko.laporan()["jumlah"], 0)


class TestKurs(unittest.TestCase):
    def test_cadangan_dipakai_saat_api_gagal(self):
        kurs, sumber = ambil_kurs_usd(url="http://alamat-tidak-ada.invalid", timeout=2)
        self.assertEqual(sumber, "data cadangan")
        self.assertGreater(kurs, 0)


if __name__ == "__main__":
    unittest.main()
