"""Contoh implementasi class dan relasi dari rancangan UML akademik."""


class Mahasiswa:
    """Merepresentasikan mahasiswa yang dapat mendaftar pada kelas kuliah."""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.__kelas_diikuti = []  # Association disimpan sebagai kode kelas.

    @property
    def kelas_diikuti(self):
        return list(self.__kelas_diikuti)

    def tambah_kelas(self, kode_kelas):
        if kode_kelas in self.__kelas_diikuti:
            return False
        self.__kelas_diikuti.append(kode_kelas)
        return True

    def __str__(self):
        return f"{self.nim} — {self.nama}"


class MataKuliah:
    """Merepresentasikan definisi mata kuliah."""

    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.kode} — {self.nama} ({self.sks} SKS)"


class KelasKuliah:
    """Merepresentasikan kelas yang menggunakan satu mata kuliah."""

    def __init__(self, kode_kelas, mata_kuliah, kapasitas):
        self.kode_kelas = kode_kelas
        self.mata_kuliah = mata_kuliah  # Association dengan MataKuliah.
        self.kapasitas = kapasitas
        self.__peserta = []

    @property
    def peserta(self):
        return list(self.__peserta)

    def daftarkan(self, mahasiswa):
        if len(self.__peserta) >= self.kapasitas:
            return False
        if mahasiswa.nim in self.__peserta:
            return False
        self.__peserta.append(mahasiswa.nim)
        mahasiswa.tambah_kelas(self.kode_kelas)
        return True

    def __str__(self):
        return f"{self.kode_kelas} — {self.mata_kuliah}"


def tampilkan_rancangan(mahasiswa, mata_kuliah, kelas):
    """Menampilkan hasil implementasi class dan relasi akademik."""
    print("Mahasiswa:", mahasiswa)
    print("Mata kuliah:", mata_kuliah)
    print("Kelas:", kelas)
    print("Peserta:", kelas.peserta)


# === Program utama ===
if __name__ == "__main__":
    mahasiswa = Mahasiswa("2026001", "Nadia")
    mata_kuliah = MataKuliah("PBO", "Pemrograman Berorientasi Objek", 3)
    kelas = KelasKuliah("PBO-A", mata_kuliah, 2)

    print("Pendaftaran berhasil:", kelas.daftarkan(mahasiswa))
    tampilkan_rancangan(mahasiswa, mata_kuliah, kelas)
