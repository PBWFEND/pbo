class Buku:
    """Merepresentasikan satu buku di perpustakaan."""

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def kembalikan(self):
        self.tersedia = True

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"'{self.judul}' oleh {self.penulis} [{status}]"


class Anggota:
    """Merepresentasikan anggota perpustakaan."""

    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.daftar_pinjam = []  # list berisi object Buku

    def pinjam_buku(self, buku):
        if buku.pinjam():  # object Buku bekerja
            self.daftar_pinjam.append(buku)
            print(f"{self.nama} meminjam '{buku.judul}'")
        else:
            print(f"'{buku.judul}' sedang tidak tersedia")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_pinjam:
            buku.kembalikan()
            self.daftar_pinjam.remove(buku)
            print(f"{self.nama} mengembalikan '{buku.judul}'")
        else:
            print(f"{self.nama} tidak meminjam '{buku.judul}'")

    def lihat_pinjaman(self):
        print(f"Pinjaman {self.nama}:")
        if not self.daftar_pinjam:
            print("  (tidak ada)")
        for buku in self.daftar_pinjam:
            print(f"  - {buku.judul}")


# === Program utama ===
if __name__ == "__main__":
    buku1 = Buku("Pemrograman Python", "Andi")
    buku2 = Buku("Basis Data", "Budi")
    anggota = Anggota("Citra", "A-001")

    anggota.pinjam_buku(buku1)
    anggota.pinjam_buku(buku2)
    anggota.lihat_pinjaman()

    anggota.kembalikan_buku(buku1)
    anggota.lihat_pinjaman()
    print(buku1)
