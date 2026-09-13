"""Contoh Pertemuan 2: interaksi beberapa object dalam perpustakaan."""


class Buku:
    """Merepresentasikan buku yang dapat dipinjam."""

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True

    def pinjam(self):
        if not self.tersedia:
            return False
        self.tersedia = False
        return True

    def kembalikan(self):
        self.tersedia = True


class Anggota:
    """Merepresentasikan anggota yang dapat meminjam buku."""

    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.daftar_buku.append(buku)
            print(f"{self.nama} meminjam {buku.judul}")
            return True
        print(f"{buku.judul} sedang tidak tersedia")
        return False

    def kembalikan_buku(self, buku):
        if buku not in self.daftar_buku:
            return False
        buku.kembalikan()
        self.daftar_buku.remove(buku)
        print(f"{self.nama} mengembalikan {buku.judul}")
        return True


if __name__ == "__main__":
    buku = Buku("Pemrograman Python", "Andi")
    anggota = Anggota("Citra")
    anggota.pinjam_buku(buku)
    anggota.kembalikan_buku(buku)
