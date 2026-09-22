"""Scaffold latihan mandiri — Polymorphism pada pembayaran."""


class Pembayaran:
    """Superclass yang menyimpan jumlah pembayaran."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError  # diimplementasikan oleh setiap subclass


class PembayaranTunai(Pembayaran):
    pass


class PembayaranTransfer(Pembayaran):
    pass


# Tugas:
# 1. Tambahkan attribute khusus pada PembayaranTransfer (nomor_referensi).
# 2. Implementasikan proses() pada PembayaranTunai yang menampilkan jumlah yang dibayarkan.
# 3. Implementasikan proses() pada PembayaranTransfer yang menampilkan jumlah dan nomor referensi.
# 4. Buat fungsi proses_semua(daftar) yang memanggil proses() pada setiap object tanpa pemeriksaan tipe.
# 5. Uji fungsi dengan minimal satu object dari setiap subclass.
