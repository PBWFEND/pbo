"""Contoh aplikasi perpustakaan sederhana berbasis object."""


class Buku:
    """Merepresentasikan satu buku dan status ketersediaannya."""

    def __init__(self, kode, judul, penulis):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True  # Attribute privat dikendalikan oleh method.

    @property
    def tersedia(self):
        """Mengembalikan status ketersediaan tanpa akses tulis langsung."""
        return self.__tersedia

    def pinjam(self):
        """Mengubah status menjadi dipinjam jika buku masih tersedia."""
        if not self.__tersedia:
            return False
        self.__tersedia = False
        return True

    def kembalikan(self):
        """Mengubah status buku menjadi tersedia."""
        self.__tersedia = True

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.kode} — {self.judul} oleh {self.penulis} [{status}]"


class Anggota:
    """Merepresentasikan anggota dan buku yang sedang dipinjam."""

    def __init__(self, nomor, nama):
        self.nomor = nomor
        self.nama = nama
        self.__buku_dipinjam = []  # Koleksi internal dilindungi melalui method.

    @property
    def buku_dipinjam(self):
        """Mengembalikan salinan daftar kode buku yang dipinjam."""
        return list(self.__buku_dipinjam)

    def tambah_pinjaman(self, kode_buku):
        self.__buku_dipinjam.append(kode_buku)

    def hapus_pinjaman(self, kode_buku):
        if kode_buku not in self.__buku_dipinjam:
            return False
        self.__buku_dipinjam.remove(kode_buku)
        return True

    def __str__(self):
        jumlah = len(self.__buku_dipinjam)
        return f"{self.nomor} — {self.nama} ({jumlah} buku dipinjam)"


class Perpustakaan:
    """Mengelola koleksi buku, anggota, dan proses peminjaman."""

    def __init__(self):
        self.__buku = {}
        self.__anggota = {}

    def tambah_buku(self, buku):
        self.__buku[buku.kode] = buku

    def tambah_anggota(self, anggota):
        self.__anggota[anggota.nomor] = anggota

    def daftar_buku(self):
        return list(self.__buku.values())

    def daftar_anggota(self):
        return list(self.__anggota.values())

    def pinjamkan(self, nomor_anggota, kode_buku):
        """Memproses peminjaman melalui interaksi antar-object."""
        anggota = self.__anggota.get(nomor_anggota)
        buku = self.__buku.get(kode_buku)

        if anggota is None or buku is None:
            return False
        if not buku.pinjam():
            return False

        anggota.tambah_pinjaman(kode_buku)
        return True

    def kembalikan(self, nomor_anggota, kode_buku):
        """Memproses pengembalian jika buku dipinjam oleh anggota tersebut."""
        anggota = self.__anggota.get(nomor_anggota)
        buku = self.__buku.get(kode_buku)

        if anggota is None or buku is None:
            return False
        if not anggota.hapus_pinjaman(kode_buku):
            return False

        buku.kembalikan()
        return True


def tampilkan_status(perpustakaan):
    """Menampilkan seluruh object buku dan anggota."""
    print("Daftar buku:")
    for buku in perpustakaan.daftar_buku():
        print(f"- {buku}")

    print("Daftar anggota:")
    for anggota in perpustakaan.daftar_anggota():
        print(f"- {anggota}")


# === Program utama ===
if __name__ == "__main__":
    perpustakaan = Perpustakaan()
    perpustakaan.tambah_buku(Buku("B001", "Pemrograman Python", "Andi"))
    perpustakaan.tambah_buku(Buku("B002", "Dasar Sistem Informasi", "Sari"))
    perpustakaan.tambah_anggota(Anggota("A001", "Nadia"))

    tampilkan_status(perpustakaan)
    print("\nPeminjaman B001 oleh A001:", perpustakaan.pinjamkan("A001", "B001"))
    print("Peminjaman kedua B001 oleh A001:", perpustakaan.pinjamkan("A001", "B001"))
    tampilkan_status(perpustakaan)
    print("\nPengembalian B001 oleh A001:", perpustakaan.kembalikan("A001", "B001"))
    tampilkan_status(perpustakaan)
