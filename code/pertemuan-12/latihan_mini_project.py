"""Scaffold latihan implementasi mini project Sistem Peminjaman Ruang."""


class Pengguna:
    """Class latihan untuk menyimpan data pengguna."""

    def __init__(self, kode, nama):
        # LATIHAN 1: Simpan kode dan nama pengguna.
        pass


class Ruang:
    """Class latihan untuk menyimpan data dan kapasitas ruang."""

    def __init__(self, kode, nama, kapasitas):
        # LATIHAN 2: Simpan kode, nama, dan kapasitas ruang.
        pass

    def sesuai_kapasitas(self, jumlah_peserta):
        # LATIHAN 3: Kembalikan True jika jumlah peserta tidak melebihi kapasitas.
        return jumlah_peserta <= self.kapasitas


class Peminjaman:
    """Class latihan yang menghubungkan pengguna, ruang, dan jadwal."""

    def __init__(self, kode, pengguna, ruang, tanggal, waktu, jumlah_peserta):
        # LATIHAN 4: Simpan seluruh data pengajuan dan status awal "diajukan".
        pass

    def setujui(self):
        # LATIHAN 5: Ubah status menjadi "disetujui".
        pass

    def __str__(self):
        # LATIHAN 6: Kembalikan ringkasan pengajuan.
        return f"{self.kode} [{self.status}]"


class LayananPeminjaman:
    """Class latihan untuk mengelola ruang dan pengajuan."""

    def __init__(self):
        # LATIHAN 7: Siapkan dictionary privat __ruang dan list privat __peminjaman.
        pass

    def tambah_ruang(self, ruang):
        # LATIHAN 8: Simpan object ruang berdasarkan kode.
        pass

    def ajukan(self, peminjaman):
        # LATIHAN 9: Tolak ruang yang belum terdaftar atau kapasitas tidak cukup.
        # Jika valid, simpan peminjaman dan kembalikan True.
        pass

    def daftar_pengajuan(self):
        # LATIHAN 10: Kembalikan salinan daftar pengajuan.
        pass


def tampilkan_pengajuan(layanan):
    """Fungsi untuk menampilkan pengajuan yang tersimpan."""
    # LATIHAN 11: Lakukan perulangan dan cetak setiap object peminjaman.
    pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
