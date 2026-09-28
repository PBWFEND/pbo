"""Scaffold latihan persiapan UTS — Gabungan konsep dasar OOP.

File ini berisi latihan bertahap yang menggabungkan:
1. Class, object, attribute, method, dan constructor.
2. Encapsulation dengan attribute privat dan property.
3. Inheritance menggunakan super() dan overriding.
4. Polymorphism melalui pemrosesan object beragam tipe.
"""


class Buku:
    """Class dasar untuk merepresentasikan buku dalam perpustakaan."""

    def __init__(self, judul, penulis):
        # LATIHAN 1: Simpan judul dan penulis sebagai attribute.
        # Buat attribute privat __tersedia dengan nilai awal True.
        pass

    def pinjam(self):
        # LATIHAN 2: Jika buku tersedia, ubah __tersedia menjadi False dan kembalikan True.
        # Jika tidak tersedia, kembalikan False.
        pass

    def kembalikan(self):
        # LATIHAN 3: Ubah __tersedia menjadi True.
        pass

    @property
    def tersedia(self):
        # LATIHAN 4: Kembalikan nilai attribute __tersedia.
        pass

    def __str__(self):
        # LATIHAN 5: Kembalikan string berformat: "judul — penulis [Tersedia/Dipinjam]".
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}]"


class BukuDigital(Buku):
    """Subclass yang merepresentasikan buku elektronik."""

    def __init__(self, judul, penulis, format_file):
        # LATIHAN 6: Panggil constructor superclass menggunakan super().
        # Simpan format_file sebagai attribute.
        pass

    def __str__(self):
        # LATIHAN 7: Override method __str__ untuk menambahkan format_file di akhir.
        # Format: "judul — penulis [Tersedia/Dipinjam] (format_file)".
        return f"{super().__str__()} ({self.format_file})"

    def unduh(self):
        # LATIHAN 8: Jika buku tersedia, kembalikan "Mengunduh <judul> dalam format <format_file>."
        # Jika tidak tersedia, kembalikan "Buku tidak tersedia."
        pass


def tampilkan_daftar_buku(daftar_buku):
    """Fungsi polimorfik untuk menampilkan status buku dari berbagai tipe."""
    # LATIHAN 9: Lakukan perulangan pada daftar_buku dan cetak setiap object.
    pass


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
