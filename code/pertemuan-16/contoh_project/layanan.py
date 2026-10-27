"""Service untuk mengelola object contoh peminjaman ruang."""

from domain import Peminjaman, Ruang


class DataDuplikatError(Exception):
    """Exception untuk identifier yang sudah digunakan."""


class LayananPeminjaman:
    """Mengelola collection ruang dan pengajuan."""

    def __init__(self):
        self.__ruang = {}
        self.__peminjaman = {}

    def tambah_ruang(self, ruang):
        if ruang.kode in self.__ruang:
            raise DataDuplikatError(f"Kode ruang {ruang.kode} sudah digunakan")
        self.__ruang[ruang.kode] = ruang

    def cari_ruang(self, kode):
        return self.__ruang.get(kode)

    def ajukan(self, peminjaman):
        if peminjaman.kode in self.__peminjaman:
            raise DataDuplikatError(
                f"Kode peminjaman {peminjaman.kode} sudah digunakan"
            )
        if peminjaman.kode_ruang not in self.__ruang:
            raise ValueError("Ruang belum terdaftar")
        self.__peminjaman[peminjaman.kode] = peminjaman

    def cari_peminjaman(self, kode):
        return self.__peminjaman.get(kode)

    def ubah_status(self, kode, status_baru):
        peminjaman = self.cari_peminjaman(kode)
        if peminjaman is None:
            return False
        peminjaman.ubah_status(status_baru)
        return True


def buat_data_awal():
    """Membuat service dengan satu ruang contoh."""
    layanan = LayananPeminjaman()
    layanan.tambah_ruang(Ruang("R001", "Lab 1", 30))
    return layanan
