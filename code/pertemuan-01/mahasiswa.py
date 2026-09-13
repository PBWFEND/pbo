class Mahasiswa:
    """Class Mahasiswa untuk data akademik sederhana."""

    jumlah_mahasiswa = 0  # class attribute

    def __init__(self, nama, nim, prodi="Sistem Informasi"):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.sks = 0
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_sks(self, jumlah):
        self.sks += jumlah
        print(f"{self.nama}: total {self.sks} SKS")

    def perkenalan(self):
        print(f"Halo, saya {self.nama} ({self.nim}) - {self.prodi}")

    def __str__(self):
        return f"Mahasiswa({self.nama}, {self.nim})"


# === Program utama ===
if __name__ == "__main__":
    m1 = Mahasiswa("Jhon Doe", "SI-101")
    m2 = Mahasiswa("Ani Lestari", "SI-102")

    m1.perkenalan()
    m2.perkenalan()

    m1.tambah_sks(3)
    m1.tambah_sks(2)
    m2.tambah_sks(4)

    print(m1)
    print(f"Total mahasiswa: {Mahasiswa.jumlah_mahasiswa}")
