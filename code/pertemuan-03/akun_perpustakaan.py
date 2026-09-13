"""Contoh Pertemuan 3: encapsulation pada akun anggota perpustakaan."""


class Anggota:
    """Menyimpan data anggota dan nomor kontak melalui property."""

    def __init__(self, nama, nomor_kontak):
        self.nama = nama
        self.__nomor_kontak = ""
        self.nomor_kontak = nomor_kontak

    @property
    def nomor_kontak(self):
        return self.__nomor_kontak

    @nomor_kontak.setter
    def nomor_kontak(self, nilai):
        nilai_bersih = str(nilai).strip()
        if not nilai_bersih.isdigit() or len(nilai_bersih) < 10:
            raise ValueError("Nomor kontak harus berupa angka minimal 10 digit")
        self.__nomor_kontak = nilai_bersih

    def ringkasan(self):
        return f"{self.nama} - kontak {self.nomor_kontak}"


if __name__ == "__main__":
    anggota = Anggota("Jhon Doe", "081234567890")
    print(anggota.ringkasan())
