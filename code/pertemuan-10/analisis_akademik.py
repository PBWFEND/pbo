"""Contoh analisis object dan class dari kasus Sistem Informasi akademik."""


class Mahasiswa:
    """Merepresentasikan mahasiswa dalam analisis domain akademik."""

    def __init__(self, nim, nama, program_studi):
        self.nim = nim
        self.nama = nama
        self.program_studi = program_studi
        self.__daftar_kelas = []  # Attribute privat mengikuti aturan class.

    @property
    def daftar_kelas(self):
        """Mengembalikan salinan kelas yang diikuti mahasiswa."""
        return list(self.__daftar_kelas)

    def daftar_pada_kelas(self, kode_kelas):
        """Menambahkan kelas ke daftar mahasiswa jika belum terdaftar."""
        if kode_kelas in self.__daftar_kelas:
            return False
        self.__daftar_kelas.append(kode_kelas)
        return True

    def __str__(self):
        return f"{self.nim} — {self.nama} ({self.program_studi})"


class MataKuliah:
    """Merepresentasikan definisi mata kuliah."""

    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.kode} — {self.nama} ({self.sks} SKS)"


class KelasKuliah:
    """Merepresentasikan kelas dan aturan kapasitas peserta."""

    def __init__(self, kode_kelas, mata_kuliah, kapasitas):
        self.kode_kelas = kode_kelas
        self.mata_kuliah = mata_kuliah
        self.kapasitas = kapasitas
        self.__peserta = []  # Koleksi peserta menjadi data internal class.

    @property
    def peserta(self):
        return list(self.__peserta)

    def masih_tersedia(self):
        return len(self.__peserta) < self.kapasitas

    def daftarkan(self, mahasiswa):
        if not self.masih_tersedia():
            return False
        if mahasiswa.nim in self.__peserta:
            return False
        self.__peserta.append(mahasiswa.nim)
        return mahasiswa.daftar_pada_kelas(self.kode_kelas)


def tampilkan_analisis(mahasiswa, mata_kuliah, kelas):
    """Menampilkan ringkasan object, attribute, dan perilaku hasil analisis."""
    print("Mahasiswa:", mahasiswa)
    print("Mata kuliah:", mata_kuliah)
    print("Kelas:", kelas.kode_kelas)
    print("Kapasitas tersedia:", kelas.masih_tersedia())
    print("Peserta:", kelas.peserta)


# === Program utama ===
if __name__ == "__main__":
    mahasiswa = Mahasiswa("2026001", "Nadia", "Sistem Informasi")
    mata_kuliah = MataKuliah("PBO", "Pemrograman Berorientasi Objek", 3)
    kelas = KelasKuliah("PBO-A", mata_kuliah, 2)

    print("Pendaftaran berhasil:", kelas.daftarkan(mahasiswa))
    tampilkan_analisis(mahasiswa, mata_kuliah, kelas)
