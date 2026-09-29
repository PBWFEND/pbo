"""Contoh CRUD dan pengelolaan data peminjaman ruang."""


class Ruang:
    """Merepresentasikan ruang yang dapat digunakan."""

    def __init__(self, kode, nama, kapasitas):
        self.kode = kode
        self.nama = nama
        self.kapasitas = kapasitas

    def __str__(self):
        return f"{self.kode} — {self.nama} ({self.kapasitas} orang)"


class Peminjaman:
    """Merepresentasikan pengajuan peminjaman ruang."""

    def __init__(self, kode, kode_ruang, pemohon):
        self.kode = kode
        self.kode_ruang = kode_ruang
        self.pemohon = pemohon
        self.status = "diajukan"

    def ubah_status(self, status_baru):
        status_valid = {"diajukan", "disetujui", "ditolak"}
        if status_baru not in status_valid:
            return False
        self.status = status_baru
        return True

    def __str__(self):
        return f"{self.kode} — {self.kode_ruang} — {self.pemohon} [{self.status}]"


class LayananPeminjaman:
    """Mengelola collection ruang dan pengajuan dengan operasi CRUD."""

    def __init__(self):
        self.__ruang = {}
        self.__peminjaman = {}

    # Create
    def tambah_ruang(self, ruang):
        if ruang.kode in self.__ruang:
            return False
        self.__ruang[ruang.kode] = ruang
        return True

    def ajukan(self, peminjaman):
        if peminjaman.kode in self.__peminjaman:
            return False
        if peminjaman.kode_ruang not in self.__ruang:
            return False
        self.__peminjaman[peminjaman.kode] = peminjaman
        return True

    # Read
    def cari_ruang(self, kode):
        return self.__ruang.get(kode)

    def daftar_ruang(self):
        return list(self.__ruang.values())

    def cari_peminjaman(self, kode):
        return self.__peminjaman.get(kode)

    def daftar_pengajuan(self):
        return list(self.__peminjaman.values())

    # Update
    def ubah_kapasitas(self, kode, kapasitas_baru):
        ruang = self.cari_ruang(kode)
        if ruang is None or kapasitas_baru <= 0:
            return False
        ruang.kapasitas = kapasitas_baru
        return True

    def ubah_status(self, kode, status_baru):
        peminjaman = self.cari_peminjaman(kode)
        if peminjaman is None:
            return False
        return peminjaman.ubah_status(status_baru)

    # Delete
    def hapus_ruang(self, kode):
        if kode not in self.__ruang:
            return False
        if any(data.kode_ruang == kode for data in self.__peminjaman.values()):
            return False
        del self.__ruang[kode]
        return True


def tampilkan_data(layanan):
    """Menampilkan data ruang dan pengajuan."""
    print("Daftar ruang:")
    for ruang in layanan.daftar_ruang():
        print(f"- {ruang}")
    print("Daftar pengajuan:")
    for peminjaman in layanan.daftar_pengajuan():
        print(f"- {peminjaman}")


# === Program utama ===
if __name__ == "__main__":
    layanan = LayananPeminjaman()
    ruang = Ruang("R001", "Lab 1", 30)
    print("Create ruang:", layanan.tambah_ruang(ruang))
    print("Create duplikat:", layanan.tambah_ruang(ruang))
    print("Read ruang:", layanan.cari_ruang("R001"))
    print("Update kapasitas:", layanan.ubah_kapasitas("R001", 40))

    peminjaman = Peminjaman("P001", "R001", "Nadia")
    print("Create pengajuan:", layanan.ajukan(peminjaman))
    print("Update status:", layanan.ubah_status("P001", "disetujui"))
    print("Delete ruang aktif:", layanan.hapus_ruang("R001"))
    tampilkan_data(layanan)
