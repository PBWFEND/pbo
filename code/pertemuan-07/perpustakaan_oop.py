"""Contoh Pertemuan 7: pengelolaan perpustakaan dengan pendekatan OOP."""


class Buku:
    """Class yang menggabungkan data dan perilaku buku."""

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True  # status ketersediaan buku

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def kembalikan(self):
        self.tersedia = True

    def tampilkan_status(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        print(f"{self.judul} oleh {self.penulis} [{status}]")


def main():
    # Object mengelola datanya sendiri melalui method.
    buku = Buku("Pemrograman Python", "Andi")
    buku.tampilkan_status()

    buku.pinjam()
    buku.tampilkan_status()

    buku.kembalikan()
    buku.tampilkan_status()


if __name__ == "__main__":
    main()