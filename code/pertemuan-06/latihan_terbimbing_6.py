"""Scaffold latihan terbimbing — Abstraction pada alat elektronik."""

from abc import ABC, abstractmethod


class AlatElektronik(ABC):
    """Abstract class yang menetapkan kontrak perilaku alat elektronik."""

    def __init__(self, merek):
        self.merek = merek

    @abstractmethod
    def nyalakan(self):
        # Abstract method: wajib diimplementasikan oleh setiap subclass.
        pass


class Televisi(AlatElektronik):
    pass


class Kulkas(AlatElektronik):
    pass


# Tugas:
# 1. Implementasikan nyalakan() pada Televisi mengembalikan "Televisi {merek} menyala".
# 2. Implementasikan nyalakan() pada Kulkas mengembalikan "Kulkas {merek} menyala".
# 3. Buat satu object Televisi dan satu object Kulkas, lalu panggil nyalakan().