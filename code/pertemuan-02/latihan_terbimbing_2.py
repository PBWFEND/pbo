"""Scaffold latihan terbimbing Pertemuan 2.

Lengkapi class MataKuliah bersama dosen, lalu jalankan:
    python3 latihan_terbimbing_2.py
"""


class MataKuliah:
    """Latihan membuat class dengan attribute dan method."""

    def __init__(self, kode, nama, sks):
        # LATIHAN 1: simpan kode, nama, dan sks sebagai attribute.
        pass

    def tampilkan_info(self):
        # LATIHAN 2: cetak kode, nama, dan sks.
        pass

    def ubah_sks(self, sks_baru):
        # LATIHAN 3: ubah nilai sks dengan parameter sks_baru.
        pass


if __name__ == "__main__":
    mata_kuliah = MataKuliah("SI204", "Pemrograman Berorientasi Objek", 2)
    mata_kuliah.tampilkan_info()
    mata_kuliah.ubah_sks(3)
    mata_kuliah.tampilkan_info()
