class Dosen:
    """Latihan terbimbing Pertemuan 1 — lengkapi bagian TODO."""

    def __init__(self, nama, nuptk, mata_kuliah):
        # TODO 1: simpan ketiga parameter sebagai attribute
        pass

    def mengajar(self):
        # TODO 2: cetak "Dosen {nama} mengajar {mata_kuliah}"
        pass

    def perkenalan(self):
        # TODO 3: cetak "Saya {nama}, NUPTK {nuptk}"
        pass


# === Program utama ===
if __name__ == "__main__":
    dosen = Dosen("Pak Yys", "1234567890123456", "PBO")
    dosen.mengajar()
    dosen.perkenalan()

# Expected output setelah TODO selesai:
# Dosen Pak Yys mengajar PBO
# Saya Pak Yys, NUPTK 1234567890123456
