"""Scaffold latihan mandiri — Analisis pengelolaan data buku."""


def tambah_buku(daftar_buku, judul, penulis):
    # LATIHAN 1: tambahkan dictionary buku ke daftar_buku.
    pass


def tampilkan_buku(daftar_buku):
    # LATIHAN 2: tampilkan seluruh buku dalam daftar_buku.
    pass


def hapus_buku(daftar_buku, judul):
    # LATIHAN 3: hapus buku dengan judul tertentu dari daftar_buku.
    pass


class Buku:
    """Class yang menggabungkan data dan perilaku buku."""

    def __init__(self, judul, penulis):
        # LATIHAN 4: simpan judul dan penulis sebagai attribute.
        pass

    def tampilkan(self):
        # LATIHAN 5: tampilkan judul dan penulis buku.
        pass


class KoleksiBuku:
    """Class yang mengelola daftar object Buku."""

    def __init__(self):
        # LATIHAN 6: siapkan list kosong untuk menyimpan object Buku.
        pass

    def tambah(self, buku):
        # LATIHAN 7: tambahkan object Buku ke dalam koleksi.
        pass

    def tampilkan_semua(self):
        # LATIHAN 8: tampilkan seluruh buku dalam koleksi.
        pass


# Tugas:
# 1. Lengkapi fungsi prosedural tambah_buku(), tampilkan_buku(), dan hapus_buku().
# 2. Lengkapi class Buku dan KoleksiBuku untuk kebutuhan yang sama.
# 3. Uji kedua pendekatan dengan data yang sama.
# 4. Tuliskan analisis singkat: pendekatan mana yang lebih tepat untuk sistem
#    perpustakaan yang berkembang, beserta alasan teknis.