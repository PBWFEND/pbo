class Dosen:
    """Latihan terbimbing Pertemuan 1 — lengkapi bagian TODO."""

    def __init__(self, nama, nidn, mata_kuliah):
        # TODO 1: simpan ketiga parameter sebagai attribute
        pass

    def mengajar(self):
        # TODO 2: cetak "Dosen {nama} mengajar {mata_kuliah}"
        pass

    def perkenalan(self):
        # TODO 3: cetak "Saya {nama}, NIDN {nidn}"
        pass


# === Program utama ===
if __name__ == "__main__":
    dosen = Dosen("Pak Yofi", "001234", "PBO")
    dosen.mengajar()
    dosen.perkenalan()

# Expected output setelah TODO selesai:
# Dosen Pak Yofi mengajar PBO
# Saya Pak Yofi, NIDN 001234
