class Akun:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError

    def ringkasan(self):
        raise NotImplementedError


class AkunMahasiswa(Akun):
    pass


class AkunDosen(Akun):
    pass


# Tugas:
# 1. Tambahkan attribute khusus pada setiap subclass.
# 2. Panggil constructor superclass menggunakan super().
# 3. Implementasikan tampilkan_peran() pada setiap subclass.
# 4. Implementasikan ringkasan() yang memuat data umum dan data khusus.
# 5. Uji minimal satu object dari setiap subclass.
