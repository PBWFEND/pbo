"""Scaffold latihan unit testing untuk domain peminjaman ruang."""

import unittest


class Ruang:
    """Class latihan untuk menyimpan ruang yang tervalidasi."""

    def __init__(self, kode, kapasitas):
        # LATIHAN 1: Tolak kode kosong dan kapasitas bukan integer positif.
        pass


class LayananRuang:
    """Class latihan untuk mengelola collection ruang."""

    def __init__(self):
        # LATIHAN 2: Siapkan dictionary privat __ruang.
        pass

    def tambah_ruang(self, ruang):
        # LATIHAN 3: Simpan ruang dan tolak kode duplikat.
        pass

    def cari_ruang(self, kode):
        # LATIHAN 4: Kembalikan ruang atau None.
        pass

    def ubah_kapasitas(self, kode, kapasitas_baru):
        # LATIHAN 5: Validasi kapasitas dan ubah object jika ditemukan.
        pass


class TestRuang(unittest.TestCase):
    """Test latihan untuk validation class Ruang."""

    def test_kapasitas_valid(self):
        # LATIHAN 6: Buat ruang dan periksa kapasitas dengan assertEqual.
        pass

    def test_kapasitas_tidak_valid(self):
        # LATIHAN 7: Pastikan kapasitas nol menaikkan ValueError.
        pass


class TestLayananRuang(unittest.TestCase):
    """Test latihan untuk operasi service."""

    def setUp(self):
        # LATIHAN 8: Siapkan service dan satu ruang untuk setiap test.
        pass

    def test_cari_ruang(self):
        # LATIHAN 9: Periksa ruang ditemukan dengan assertEqual atau assertIsNotNone.
        pass

    def test_update_kapasitas(self):
        # LATIHAN 10: Ubah kapasitas lalu periksa state object.
        pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan dengan python3.")
