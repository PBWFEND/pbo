"""Contoh Pertemuan 2: class, object, method, dan constructor."""


class Mahasiswa:
    """Merepresentasikan mahasiswa dengan daftar mata kuliah."""

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.mata_kuliah = []

    def ambil_mata_kuliah(self, mata_kuliah):
        if mata_kuliah not in self.mata_kuliah:
            self.mata_kuliah.append(mata_kuliah)
            return True
        return False

    def tampilkan_krs(self):
        daftar = ", ".join(self.mata_kuliah) or "Belum ada mata kuliah"
        print(f"{self.nama} ({self.nim}): {daftar}")


if __name__ == "__main__":
    mahasiswa = Mahasiswa("Jhon Doe", "SI-101")
    mahasiswa.ambil_mata_kuliah("Pemrograman Berorientasi Objek")
    mahasiswa.ambil_mata_kuliah("Basis Data")
    mahasiswa.tampilkan_krs()
