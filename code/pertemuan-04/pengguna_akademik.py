class Pengguna:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        return "Pengguna sistem"

    def ringkasan(self):
        return f"{self.nama} — {self.email} — {self.tampilkan_peran()}"


class Mahasiswa(Pengguna):
    def __init__(self, nama, email, nim, program_studi):
        super().__init__(nama, email)
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        ringkasan_dasar = super().ringkasan()
        return f"{ringkasan_dasar} — {self.nim} — {self.program_studi}"


class Dosen(Pengguna):
    def __init__(self, nama, email, nuptk, bidang_keahlian):
        super().__init__(nama, email)
        self.nuptk = nuptk
        self.bidang_keahlian = bidang_keahlian

    def tampilkan_peran(self):
        return "Dosen"


class Admin(Pengguna):
    def __init__(self, nama, email, unit_kerja):
        super().__init__(nama, email)
        self.unit_kerja = unit_kerja

    def tampilkan_peran(self):
        return "Administrator"


def main():
    pengguna = [
        Mahasiswa("Budi", "budi@example.com", "SI-101", "Sistem Informasi"),
        Dosen("Sari", "sari@example.com", "NUPTK-001", "Pemrograman"),
        Admin("Rina", "rina@example.com", "Akademik"),
    ]

    for data in pengguna:
        print(data.ringkasan())


if __name__ == "__main__":
    main()
