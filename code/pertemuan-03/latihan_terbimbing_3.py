"""Scaffold latihan terbimbing Pertemuan 3.

Lengkapi class RekeningMahasiswa, lalu jalankan:
    python3 latihan_terbimbing_3.py
"""


class RekeningMahasiswa:
    """Latihan private attribute dan property saldo."""

    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = 0
        # LATIHAN 1: gunakan setter saldo untuk memvalidasi saldo_awal.
        self.saldo = saldo_awal

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        if not isinstance(nilai, (int, float)) or isinstance(nilai, bool) or nilai < 0:
            raise ValueError("Saldo harus berupa angka tidak negatif")
        self.__saldo = nilai

    def setor(self, jumlah):
        if not isinstance(jumlah, (int, float)) or isinstance(jumlah, bool) or jumlah <= 0:
            raise ValueError("Jumlah setoran harus berupa angka positif")
        self.saldo += jumlah


if __name__ == "__main__":
    rekening = RekeningMahasiswa("Jhon Doe", 50000)
    rekening.setor(25000)
    print(rekening.saldo)
