"""Scaffold latihan implementasi aplikasi perpustakaan berbasis object."""


class Buku:
    """Class latihan untuk menyimpan data dan status satu buku."""

    def __init__(self, kode, judul, penulis):
        # LATIHAN 1: Simpan kode, judul, dan penulis sebagai attribute.
        # Buat attribute privat __tersedia dengan nilai awal True.
        pass

    @property
    def tersedia(self):
        # LATIHAN 2: Kembalikan status attribute privat __tersedia.
        pass

    def pinjam(self):
        # LATIHAN 3: Tolak peminjaman jika buku tidak tersedia.
        # Jika tersedia, ubah status dan kembalikan True.
        pass

    def kembalikan(self):
        # LATIHAN 4: Ubah status buku menjadi tersedia.
        pass

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.kode} — {self.judul} oleh {self.penulis} [{status}]"


class Anggota:
    """Class latihan untuk menyimpan data dan daftar pinjaman anggota."""

    def __init__(self, nomor, nama):
        # LATIHAN 5: Simpan nomor, nama, dan list privat __buku_dipinjam.
        pass

    @property
    def buku_dipinjam(self):
        # LATIHAN 6: Kembalikan salinan daftar buku yang dipinjam.
        pass

    def tambah_pinjaman(self, kode_buku):
        # LATIHAN 7: Tambahkan kode buku ke daftar pinjaman.
        pass

    def hapus_pinjaman(self, kode_buku):
        # LATIHAN 8: Hapus kode buku jika ada dan kembalikan True atau False.
        pass


class Perpustakaan:
    """Class latihan untuk mengelola buku, anggota, dan transaksi."""

    def __init__(self):
        # LATIHAN 9: Siapkan dictionary privat untuk buku dan anggota.
        pass

    def tambah_buku(self, buku):
        # LATIHAN 10: Simpan object buku berdasarkan kode.
        pass

    def tambah_anggota(self, anggota):
        # LATIHAN 11: Simpan object anggota berdasarkan nomor.
        pass

    def pinjamkan(self, nomor_anggota, kode_buku):
        # LATIHAN 12: Cari object, validasi, panggil buku.pinjam(),
        # lalu tambahkan pinjaman ke anggota jika berhasil.
        pass

    def kembalikan(self, nomor_anggota, kode_buku):
        # LATIHAN 13: Validasi anggota dan buku, hapus pinjaman,
        # lalu panggil buku.kembalikan() jika sesuai.
        pass

    def tampilkan_buku(self):
        # LATIHAN 14: Cetak setiap object buku yang tersimpan.
        pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
