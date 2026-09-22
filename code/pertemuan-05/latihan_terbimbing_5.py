"""Scaffold latihan terbimbing — Polymorphism pada hewan."""


class Hewan:
    """Superclass yang merepresentasikan hewan secara umum."""

    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "..."  # method dasar yang akan dioverride oleh subclass


class Kucing(Hewan):
    pass


class Anjing(Hewan):
    pass


# Tugas:
# 1. Override method suara() pada Kucing mengembalikan "Meong".
# 2. Override method suara() pada Anjing mengembalikan "Guk".
# 3. Buat fungsi tampilkan_suara(daftar) yang memanggil suara() pada setiap object.
# 4. Uji fungsi dengan minimal satu object Kucing dan satu object Anjing.
