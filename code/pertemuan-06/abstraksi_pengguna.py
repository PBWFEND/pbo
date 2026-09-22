"""Contoh abstraction dan interface pada pengguna Sistem Informasi."""

from abc import ABC, abstractmethod


class Pengguna(ABC):
    """Abstract class yang menetapkan kontrak perilaku pengguna."""

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    @abstractmethod
    def tampilkan_peran(self):
        # Abstract method: wajib diimplementasikan oleh setiap subclass.
        pass

    def ringkasan(self):
        # Method biasa: memanggil abstract method agar subclass dapat mengubah perilakunya.
        return f"{self.nama} — {self.email} — {self.tampilkan_peran()}"


class Mahasiswa(Pengguna):
    """Subclass yang mengimplementasikan kontrak untuk mahasiswa."""

    def __init__(self, nama, email, nim, program_studi):
        super().__init__(nama, email)  # memanggil constructor superclass
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        return "Mahasiswa"  # implementasi abstract method


class Dosen(Pengguna):
    """Subclass yang mengimplementasikan kontrak untuk dosen."""

    def __init__(self, nama, email, nuptk, bidang_keahlian):
        super().__init__(nama, email)  # memanggil constructor superclass
        self.nuptk = nuptk
        self.bidang_keahlian = bidang_keahlian

    def tampilkan_peran(self):
        return "Dosen"  # implementasi abstract method


class Admin(Pengguna):
    """Subclass yang mengimplementasikan kontrak untuk administrator."""

    def __init__(self, nama, email, unit_kerja):
        super().__init__(nama, email)  # memanggil constructor superclass
        self.unit_kerja = unit_kerja

    def tampilkan_peran(self):
        return "Administrator"  # implementasi abstract method


def tampilkan_semua(daftar):
    # Kontrak abstraction menjamin setiap object memiliki method ringkasan().
    for data in daftar:
        print(data.ringkasan())


def main():
    pengguna = [
        Mahasiswa("Budi", "budi@example.com", "SI-101", "Sistem Informasi"),
        Dosen("Sari", "sari@example.com", "NUPTK-001", "Pemrograman"),
        Admin("Rina", "rina@example.com", "Akademik"),
    ]

    tampilkan_semua(pengguna)

    # Abstract class tidak dapat diinstansiasi langsung.
    try:
        Pengguna("Tanpa Peran", "tanpa@example.com")
    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()