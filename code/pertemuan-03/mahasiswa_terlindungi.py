"""Contoh Pertemuan 3: encapsulation pada class Mahasiswa."""


class Mahasiswa:
    """Menyimpan data mahasiswa dengan attribute yang divalidasi."""

    def __init__(self, nama, nim, sks=0):
        self.nama = nama
        self.nim = nim
        self.__sks = 0  # attribute privat menggunakan name mangling
        self.sks = sks  # memakai setter untuk validasi

    @property
    def sks(self):
        # Getter: membaca attribute privat seperti attribute biasa.
        return self.__sks

    @sks.setter
    def sks(self, nilai):
        # Setter: memvalidasi nilai sebelum disimpan ke attribute privat.
        if not isinstance(nilai, int) or nilai < 0:
            raise ValueError("SKS harus bilangan bulat tidak negatif")
        self.__sks = nilai

    def tambah_sks(self, jumlah):
        if not isinstance(jumlah, int) or jumlah <= 0:
            raise ValueError("Jumlah SKS harus bilangan bulat positif")
        self.sks += jumlah  # memakai setter sehingga validasi tetap berjalan

    def __str__(self):
        return f"{self.nama} ({self.nim}) - {self.sks} SKS"


if __name__ == "__main__":
    mahasiswa = Mahasiswa("Jhon Doe", "SI-101", 3)
    mahasiswa.tambah_sks(2)
    print(mahasiswa)

    try:
        mahasiswa.sks = -1  # nilai negatif ditolak oleh setter
    except ValueError as error:
        print(f"Validasi: {error}")
