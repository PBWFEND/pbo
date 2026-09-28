"""Contoh implementasi mini project Sistem Peminjaman Ruang."""


class Pengguna:
    """Merepresentasikan pengguna yang mengajukan peminjaman."""

    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

    def __str__(self):
        return f"{self.kode} — {self.nama}"


class Ruang:
    """Merepresentasikan ruang yang dapat dipinjam."""

    def __init__(self, kode, nama, kapasitas):
        self.kode = kode
        self.nama = nama
        self.kapasitas = kapasitas

    def sesuai_kapasitas(self, jumlah_peserta):
        return jumlah_peserta <= self.kapasitas

    def __str__(self):
        return f"{self.kode} — {self.nama} ({self.kapasitas} orang)"


class Peminjaman:
    """Menghubungkan pengguna dengan ruang dan jadwal peminjaman."""

    def __init__(self, kode, pengguna, ruang, tanggal, waktu, jumlah_peserta):
        self.kode = kode
        self.pengguna = pengguna
        self.ruang = ruang
        self.tanggal = tanggal
        self.waktu = waktu
        self.jumlah_peserta = jumlah_peserta
        self.status = "diajukan"

    def setujui(self):
        self.status = "disetujui"

    def __str__(self):
        return (
            f"{self.kode} — {self.pengguna.nama} — {self.ruang.nama} "
            f"({self.tanggal} {self.waktu}) [{self.status}]"
        )


class LayananPeminjaman:
    """Mengelola ruang dan pengajuan peminjaman."""

    def __init__(self):
        self.__ruang = {}
        self.__peminjaman = []

    def tambah_ruang(self, ruang):
        self.__ruang[ruang.kode] = ruang

    def ajukan(self, peminjaman):
        ruang = self.__ruang.get(peminjaman.ruang.kode)
        if ruang is None:
            return False
        if not ruang.sesuai_kapasitas(peminjaman.jumlah_peserta):
            return False
        self.__peminjaman.append(peminjaman)
        return True

    def daftar_pengajuan(self):
        return list(self.__peminjaman)


def tampilkan_pengajuan(layanan):
    """Menampilkan seluruh pengajuan yang tersimpan."""
    for peminjaman in layanan.daftar_pengajuan():
        print(peminjaman)


# === Program utama ===
if __name__ == "__main__":
    pengguna = Pengguna("U001", "Nadia")
    ruang = Ruang("R001", "Lab 1", 30)
    layanan = LayananPeminjaman()

    layanan.tambah_ruang(ruang)
    pengajuan = Peminjaman(
        "P001", pengguna, ruang, "2026-12-03", "09:00", 25
    )
    print("Pengajuan berhasil:", layanan.ajukan(pengajuan))
    pengajuan.setujui()
    tampilkan_pengajuan(layanan)

    ruang_tidak_terdaftar = Ruang("R999", "Ruang Tidak Terdaftar", 20)
    pengajuan_gagal = Peminjaman(
        "P002", pengguna, ruang_tidak_terdaftar, "2026-12-04", "10:00", 10
    )
    print("Pengajuan ruang tidak terdaftar:", layanan.ajukan(pengajuan_gagal))
