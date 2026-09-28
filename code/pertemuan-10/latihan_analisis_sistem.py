"""Scaffold latihan analisis object dan class dari kasus akademik."""


class Mahasiswa:
    """Class latihan untuk merepresentasikan mahasiswa."""

    def __init__(self, nim, nama, program_studi):
        # LATIHAN 1: Simpan nim, nama, dan program_studi.
        # Siapkan list privat __daftar_kelas.
        pass

    @property
    def daftar_kelas(self):
        # LATIHAN 2: Kembalikan salinan daftar kelas mahasiswa.
        pass

    def daftar_pada_kelas(self, kode_kelas):
        # LATIHAN 3: Tambahkan kode kelas jika belum ada.
        # Kembalikan True jika berhasil dan False jika duplikat.
        pass


class MataKuliah:
    """Class latihan untuk menyimpan definisi mata kuliah."""

    def __init__(self, kode, nama, sks):
        # LATIHAN 4: Simpan kode, nama, dan sks sebagai attribute.
        pass


class KelasKuliah:
    """Class latihan untuk mengelola kelas dan kapasitas peserta."""

    def __init__(self, kode_kelas, mata_kuliah, kapasitas):
        # LATIHAN 5: Simpan kode_kelas, mata_kuliah, kapasitas,
        # dan siapkan list privat __peserta.
        pass

    @property
    def peserta(self):
        # LATIHAN 6: Kembalikan salinan daftar peserta.
        pass

    def masih_tersedia(self):
        # LATIHAN 7: Kembalikan True jika jumlah peserta belum mencapai kapasitas.
        pass

    def daftarkan(self, mahasiswa):
        # LATIHAN 8: Tolak jika kapasitas penuh atau mahasiswa sudah terdaftar.
        # Tambahkan nim mahasiswa dan panggil daftar_pada_kelas() jika valid.
        pass


def tampilkan_analisis(mahasiswa, mata_kuliah, kelas):
    """Fungsi untuk menampilkan ringkasan hasil analisis object."""
    # LATIHAN 9: Tampilkan data utama dan status kapasitas kelas.
    pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
