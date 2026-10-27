"""Unit test contoh untuk domain dan service peminjaman ruang."""

import unittest

from domain import Peminjaman, Ruang
from layanan import DataDuplikatError, buat_data_awal


class TestPeminjaman(unittest.TestCase):
    """Menguji pembuatan object dan perubahan status."""

    def test_ruang_valid(self):
        ruang = Ruang("R001", "Lab 1", 30)
        self.assertEqual(ruang.kapasitas, 30)

    def test_kapasitas_tidak_valid(self):
        with self.assertRaises(ValueError):
            Ruang("R001", "Lab 1", 0)

    def test_pengajuan_dan_update_status(self):
        layanan = buat_data_awal()
        layanan.ajukan(Peminjaman("P001", "R001", "Nadia"))
        berhasil = layanan.ubah_status("P001", "disetujui")
        self.assertTrue(berhasil)
        self.assertEqual(layanan.cari_peminjaman("P001").status, "disetujui")

    def test_kode_pengajuan_duplikat(self):
        layanan = buat_data_awal()
        layanan.ajukan(Peminjaman("P001", "R001", "Nadia"))
        pengajuan_duplikat = Peminjaman("P001", "R001", "Bima")
        with self.assertRaises(DataDuplikatError):
            layanan.ajukan(pengajuan_duplikat)


# === Program utama ===
if __name__ == "__main__":
    unittest.main(verbosity=2)
