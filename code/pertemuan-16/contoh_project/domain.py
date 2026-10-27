"""Class domain untuk contoh Sistem Peminjaman Ruang."""


class Ruang:
    """Merepresentasikan ruang yang dapat dipinjam."""

    def __init__(self, kode, nama, kapasitas):
        if not kode or not nama:
            raise ValueError("Kode dan nama ruang wajib diisi")
        if not isinstance(kapasitas, int) or kapasitas <= 0:
            raise ValueError("Kapasitas harus bilangan bulat positif")
        self.kode = kode
        self.nama = nama
        self.kapasitas = kapasitas


class Peminjaman:
    """Merepresentasikan pengajuan peminjaman ruang."""

    STATUS_VALID = {"diajukan", "disetujui", "ditolak"}

    def __init__(self, kode, kode_ruang, pemohon):
        if not kode or not kode_ruang or not pemohon:
            raise ValueError("Kode dan pemohon wajib diisi")
        self.kode = kode
        self.kode_ruang = kode_ruang
        self.pemohon = pemohon
        self.status = "diajukan"

    def ubah_status(self, status_baru):
        if status_baru not in self.STATUS_VALID:
            raise ValueError("Status peminjaman tidak valid")
        self.status = status_baru
