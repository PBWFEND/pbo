"""Scaffold latihan exception handling, validation, debugging, dan refactoring."""


class DataTidakDitemukanError(Exception):
    """Exception latihan untuk identifier yang tidak ditemukan."""


class DataDuplikatError(Exception):
    """Exception latihan untuk identifier yang sudah digunakan."""


class Ruang:
    """Class latihan untuk menyimpan data ruang yang valid."""

    def __init__(self, kode, nama, kapasitas):
        # LATIHAN 1: Tolak kode atau nama kosong dengan ValueError.
        # Tolak kapasitas yang bukan integer positif dengan ValueError.
        pass

    def __str__(self):
        # LATIHAN 2: Kembalikan ringkasan ruang.
        return f"{self.kode} — {self.nama} ({self.kapasitas} orang)"


class LayananPeminjaman:
    """Class latihan untuk menerapkan exception pada operasi data."""

    def __init__(self):
        # LATIHAN 3: Siapkan dictionary privat __ruang.
        pass

    def tambah_ruang(self, ruang):
        # LATIHAN 4: Naikkan DataDuplikatError jika kode sudah digunakan.
        pass

    def cari_ruang_wajib(self, kode):
        # LATIHAN 5: Kembalikan ruang atau naikkan DataTidakDitemukanError.
        pass

    def ubah_kapasitas(self, kode, kapasitas_baru):
        # LATIHAN 6: Validasi kapasitas, cari ruang, lalu ubah kapasitas.
        pass

    def daftar_ruang(self):
        # LATIHAN 7: Kembalikan list baru dari seluruh ruang.
        pass


def proses_input(layanan, kode, nama, kapasitas):
    """Fungsi latihan untuk menangani exception pada batas program."""
    # LATIHAN 8: Gunakan try, except, else, dan finally secara tepat.
    pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
