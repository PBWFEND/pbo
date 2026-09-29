"""Contoh exception handling, validation, debugging, dan refactoring."""


class DataTidakDitemukanError(Exception):
    """Exception untuk identifier yang tidak ditemukan."""


class DataDuplikatError(Exception):
    """Exception untuk identifier yang sudah digunakan."""


class Ruang:
    """Merepresentasikan ruang dengan data yang tervalidasi."""

    def __init__(self, kode, nama, kapasitas):
        if not kode or not nama:
            raise ValueError("Kode dan nama ruang wajib diisi")
        if not isinstance(kapasitas, int) or kapasitas <= 0:
            raise ValueError("Kapasitas harus bilangan bulat positif")
        self.kode = kode
        self.nama = nama
        self.kapasitas = kapasitas

    def __str__(self):
        return f"{self.kode} — {self.nama} ({self.kapasitas} orang)"


class LayananPeminjaman:
    """Mengelola ruang dengan validation dan custom exception."""

    def __init__(self):
        self.__ruang = {}

    def tambah_ruang(self, ruang):
        if ruang.kode in self.__ruang:
            raise DataDuplikatError(f"Kode ruang {ruang.kode} sudah digunakan")
        self.__ruang[ruang.kode] = ruang

    def cari_ruang_wajib(self, kode):
        ruang = self.__ruang.get(kode)
        if ruang is None:
            raise DataTidakDitemukanError(f"Ruang {kode} tidak ditemukan")
        return ruang

    def ubah_kapasitas(self, kode, kapasitas_baru):
        if not isinstance(kapasitas_baru, int) or kapasitas_baru <= 0:
            raise ValueError("Kapasitas harus bilangan bulat positif")
        ruang = self.cari_ruang_wajib(kode)
        ruang.kapasitas = kapasitas_baru

    def daftar_ruang(self):
        return list(self.__ruang.values())


def proses_input(layanan, kode, nama, kapasitas):
    """Menangani exception pada batas interaksi program."""
    try:
        layanan.tambah_ruang(Ruang(kode, nama, kapasitas))
    except (ValueError, DataDuplikatError) as error:
        print(f"Input ditolak: {error}")
    else:
        print(f"Ruang {kode} berhasil disimpan.")
    finally:
        print("Pemeriksaan input selesai.")


# === Program utama ===
if __name__ == "__main__":
    layanan = LayananPeminjaman()
    proses_input(layanan, "R001", "Lab 1", 30)
    proses_input(layanan, "R001", "Lab Duplikat", 20)
    proses_input(layanan, "R002", "", 20)

    try:
        layanan.ubah_kapasitas("R999", 40)
    except DataTidakDitemukanError as error:
        print(f"Update ditolak: {error}")

    print("Daftar ruang:", [str(ruang) for ruang in layanan.daftar_ruang()])
