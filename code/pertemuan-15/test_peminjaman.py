"""Contoh unit testing untuk domain peminjaman ruang dengan unittest."""

import unittest


class DataDuplikatError(Exception):
    """Exception untuk identifier yang sudah digunakan."""


class Ruang:
    """Merepresentasikan ruang dengan kapasitas yang valid."""

    def __init__(self, kode, kapasitas):
        if not kode:
            raise ValueError("Kode ruang wajib diisi")
        if not isinstance(kapasitas, int) or kapasitas <= 0:
            raise ValueError("Kapasitas harus bilangan bulat positif")
        self.kode = kode
        self.kapasitas = kapasitas


class LayananRuang:
    """Menyimpan ruang dan menyediakan operasi yang dapat diuji."""

    def __init__(self):
        self.__ruang = {}

    def tambah_ruang(self, ruang):
        if ruang.kode in self.__ruang:
            raise DataDuplikatError(f"Kode {ruang.kode} sudah digunakan")
        self.__ruang[ruang.kode] = ruang

    def cari_ruang(self, kode):
        return self.__ruang.get(kode)

    def ubah_kapasitas(self, kode, kapasitas_baru):
        if not isinstance(kapasitas_baru, int) or kapasitas_baru <= 0:
            raise ValueError("Kapasitas harus bilangan bulat positif")
        ruang = self.cari_ruang(kode)
        if ruang is None:
            return False
        ruang.kapasitas = kapasitas_baru
        return True


class TestRuang(unittest.TestCase):
    """Menguji validation pada class Ruang."""

    def test_kapasitas_valid_disimpan(self):
        ruang = Ruang("R001", 30)
        self.assertEqual(ruang.kapasitas, 30)

    def test_kapasitas_nol_ditolak(self):
        with self.assertRaises(ValueError):
            Ruang("R001", 0)


class TestLayananRuang(unittest.TestCase):
    """Menguji operasi penyimpanan dan perubahan ruang."""

    def setUp(self):
        self.layanan = LayananRuang()
        self.layanan.tambah_ruang(Ruang("R001", 30))

    def test_kode_duplikat_ditolak(self):
        ruang_duplikat = Ruang("R001", 20)
        with self.assertRaises(DataDuplikatError):
            self.layanan.tambah_ruang(ruang_duplikat)

    def test_update_mengubah_state_object(self):
        berhasil = self.layanan.ubah_kapasitas("R001", 40)
        self.assertTrue(berhasil)
        self.assertEqual(self.layanan.cari_ruang("R001").kapasitas, 40)

    def test_update_kode_tidak_ditemukan(self):
        berhasil = self.layanan.ubah_kapasitas("R999", 40)
        self.assertFalse(berhasil)


# === Program utama ===
if __name__ == "__main__":
    unittest.main(verbosity=2)
