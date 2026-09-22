"""Contoh polymorphism dan duck typing pada pengguna Sistem Informasi."""


class Pengguna:
    """Superclass yang menyimpan data umum pengguna."""

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        return "Pengguna sistem"

    def ringkasan(self):
        # Memanggil self.tampilkan_peran() agar subclass dapat mengubah perilakunya.
        return f"{self.nama} — {self.email} — {self.tampilkan_peran()}"


class Mahasiswa(Pengguna):
    """Subclass yang menambahkan data khusus mahasiswa."""

    def __init__(self, nama, email, nim, program_studi):
        super().__init__(nama, email)  # memanggil constructor superclass
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        return "Mahasiswa"  # overriding method superclass

    def ringkasan(self):
        ringkasan_dasar = super().ringkasan()  # memakai ringkasan superclass
        return f"{ringkasan_dasar} — {self.nim} — {self.program_studi}"


class Dosen(Pengguna):
    """Subclass yang menambahkan data khusus dosen."""

    def __init__(self, nama, email, nuptk, bidang_keahlian):
        super().__init__(nama, email)  # memanggil constructor superclass
        self.nuptk = nuptk
        self.bidang_keahlian = bidang_keahlian

    def tampilkan_peran(self):
        return "Dosen"  # overriding method superclass

    def ringkasan(self):
        ringkasan_dasar = super().ringkasan()  # memakai ringkasan superclass
        return f"{ringkasan_dasar} — {self.nuptk} — {self.bidang_keahlian}"


class Admin(Pengguna):
    """Subclass yang menambahkan data khusus administrator."""

    def __init__(self, nama, email, unit_kerja):
        super().__init__(nama, email)  # memanggil constructor superclass
        self.unit_kerja = unit_kerja

    def tampilkan_peran(self):
        return "Administrator"  # overriding method superclass

    def ringkasan(self):
        ringkasan_dasar = super().ringkasan()  # memakai ringkasan superclass
        return f"{ringkasan_dasar} — {self.unit_kerja}"


def tampilkan_semua(daftar):
    # Duck typing: fungsi hanya membutuhkan method ringkasan() pada setiap object.
    for data in daftar:
        print(data.ringkasan())


def main():
    pengguna = [
        Mahasiswa("Budi", "budi@example.com", "SI-101", "Sistem Informasi"),
        Dosen("Sari", "sari@example.com", "NUPTK-001", "Pemrograman"),
        Admin("Rina", "rina@example.com", "Akademik"),
    ]

    tampilkan_semua(pengguna)


if __name__ == "__main__":
    main()
