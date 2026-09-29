"""Scaffold latihan CRUD dan pengelolaan data peminjaman ruang."""


class Ruang:
    """Class latihan untuk menyimpan data ruang."""

    def __init__(self, kode, nama, kapasitas):
        # LATIHAN 1: Simpan kode, nama, dan kapasitas.
        pass

    def __str__(self):
        # LATIHAN 2: Kembalikan ringkasan ruang.
        return f"{self.kode} — {self.nama} ({self.kapasitas} orang)"


class Peminjaman:
    """Class latihan untuk menyimpan pengajuan peminjaman."""

    def __init__(self, kode, kode_ruang, pemohon):
        # LATIHAN 3: Simpan data pengajuan dan status awal "diajukan".
        pass

    def ubah_status(self, status_baru):
        # LATIHAN 4: Terima status diajukan, disetujui, atau ditolak.
        # Kembalikan False jika status tidak valid.
        pass

    def __str__(self):
        # LATIHAN 5: Kembalikan ringkasan pengajuan.
        return f"{self.kode} — {self.kode_ruang} [{self.status}]"


class LayananPeminjaman:
    """Class latihan untuk mengelola collection ruang dan pengajuan."""

    def __init__(self):
        # LATIHAN 6: Siapkan dictionary privat __ruang dan __peminjaman.
        pass

    def tambah_ruang(self, ruang):
        # LATIHAN 7: Create ruang dan tolak kode duplikat.
        pass

    def cari_ruang(self, kode):
        # LATIHAN 8: Read satu ruang atau kembalikan None.
        pass

    def daftar_ruang(self):
        # LATIHAN 9: Read seluruh ruang sebagai list baru.
        pass

    def ubah_kapasitas(self, kode, kapasitas_baru):
        # LATIHAN 10: Update kapasitas jika ruang ditemukan dan nilai valid.
        pass

    def hapus_ruang(self, kode):
        # LATIHAN 11: Delete ruang jika ditemukan dan belum digunakan pengajuan.
        pass

    def ajukan(self, peminjaman):
        # LATIHAN 12: Simpan pengajuan jika kode unik dan ruang tersedia.
        pass

    def ubah_status(self, kode, status_baru):
        # LATIHAN 13: Update status pengajuan berdasarkan kode.
        pass

    def daftar_pengajuan(self):
        # LATIHAN 14: Kembalikan seluruh pengajuan sebagai list baru.
        pass


def tampilkan_data(layanan):
    """Fungsi untuk menampilkan hasil operasi CRUD."""
    # LATIHAN 15: Tampilkan daftar ruang dan daftar pengajuan.
    pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
