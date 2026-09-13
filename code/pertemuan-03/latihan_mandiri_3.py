"""Scaffold latihan mandiri Pertemuan 3.

Buat class ProfilMahasiswa dengan private attribute dan property.
Jalankan:
    python3 latihan_mandiri_3.py
"""


class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        # LATIHAN: simpan nama dan gunakan property untuk email serta semester.
        pass

    @property
    def email(self):
        # LATIHAN: kembalikan email private.
        pass

    @email.setter
    def email(self, nilai):
        # LATIHAN: validasi bahwa email memuat karakter @.
        pass

    @property
    def semester(self):
        # LATIHAN: kembalikan semester private.
        pass

    @semester.setter
    def semester(self, nilai):
        # LATIHAN: validasi semester berupa integer positif.
        pass

    def tampilkan_info(self):
        # LATIHAN: tampilkan nama, email, dan semester.
        pass


if __name__ == "__main__":
    profil = ProfilMahasiswa("Jhon Doe", "jhon.doe@example.com", 3)
    profil.tampilkan_info()
