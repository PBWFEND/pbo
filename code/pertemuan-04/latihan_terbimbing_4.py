"""Scaffold latihan terbimbing Pertemuan 4 — Inheritance pada kendaraan."""


class Kendaraan:
    """Superclass yang merepresentasikan kendaraan umum."""

    def __init__(self, merek):
        self.merek = merek  # attribute umum yang dimiliki semua kendaraan

    def informasi(self):
        return f"Kendaraan {self.merek}"


class Mobil(Kendaraan):
    pass


class Motor(Kendaraan):
    pass


# Tugas:
# 1. Tambahkan attribute khusus pada Mobil dan Motor.
# 2. Gunakan super() pada constructor subclass.
# 3. Override method informasi() pada kedua subclass.
# 4. Buat dan tampilkan satu object Mobil serta satu object Motor.
