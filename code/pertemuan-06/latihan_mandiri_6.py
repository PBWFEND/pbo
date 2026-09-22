"""Scaffold latihan mandiri — Abstraction pada transaksi."""

from abc import ABC, abstractmethod


class Transaksi(ABC):
    """Abstract class yang menetapkan kontrak perilaku transaksi."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    @abstractmethod
    def proses(self):
        # Abstract method: wajib diimplementasikan oleh setiap subclass.
        pass


class TransaksiTunai(Transaksi):
    pass


class TransaksiTransfer(Transaksi):
    pass


# Tugas:
# 1. Tambahkan attribute khusus pada TransaksiTransfer (nomor_referensi).
# 2. Implementasikan proses() pada TransaksiTunai yang menampilkan jumlah yang dibayarkan.
# 3. Implementasikan proses() pada TransaksiTransfer yang menampilkan jumlah dan nomor referensi.
# 4. Buat fungsi proses_semua(daftar) yang memanggil proses() pada setiap object tanpa pemeriksaan tipe.
# 5. Uji fungsi dengan minimal satu object dari setiap subclass.