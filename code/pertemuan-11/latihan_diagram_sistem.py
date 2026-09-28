"""Scaffold latihan UML class diagram dan relasi antar-class."""


class Produk:
    """Class latihan untuk menyimpan data produk."""

    def __init__(self, kode, nama, harga):
        # LATIHAN 1: Simpan kode, nama, dan harga sebagai attribute.
        pass

    def __str__(self):
        # LATIHAN 2: Kembalikan ringkasan produk.
        return f"{self.kode} — {self.nama} (Rp{self.harga})"


class Pelanggan:
    """Class latihan untuk menyimpan data pelanggan."""

    def __init__(self, kode, nama):
        # LATIHAN 3: Simpan kode dan nama pelanggan.
        pass


class DetailPesanan:
    """Bagian dari Pesanan dalam relasi composition."""

    def __init__(self, produk, jumlah):
        # LATIHAN 4: Simpan object produk dan jumlah pembelian.
        pass

    def subtotal(self):
        # LATIHAN 5: Kembalikan harga produk dikali jumlah.
        pass


class Pesanan:
    """Class latihan yang memiliki beberapa DetailPesanan."""

    def __init__(self, nomor, pelanggan):
        # LATIHAN 6: Simpan nomor dan object pelanggan.
        # Siapkan list privat __detail.
        pass

    @property
    def detail(self):
        # LATIHAN 7: Kembalikan salinan list detail pesanan.
        pass

    def tambah_detail(self, produk, jumlah):
        # LATIHAN 8: Buat DetailPesanan baru dan tambahkan ke list.
        pass

    def total(self):
        # LATIHAN 9: Jumlahkan seluruh subtotal detail pesanan.
        pass


def tampilkan_rancangan(pelanggan, pesanan):
    """Fungsi untuk menampilkan hasil implementasi rancangan class."""
    # LATIHAN 10: Tampilkan pelanggan, nomor pesanan, detail, dan total.
    pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
