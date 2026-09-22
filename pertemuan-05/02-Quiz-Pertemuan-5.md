# Quiz Pertemuan 5 — Polymorphism dan Duck Typing pada Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 5 | **Tanggal:** 14 Oktober 2026 | **CPMK:** CPMK114

## Petunjuk Pengerjaan

- Waktu: 15 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu tanpa catatan, kecuali ada arahan dosen
- Soal 3–5 berbasis kode Python

## Soal 1 — Konsep Polymorphism

Jelaskan pengertian polymorphism dalam OOP dan berikan satu contoh method yang menghasilkan perilaku berbeda pada class yang berbeda.

## Soal 2 — Overriding dan Polymorphism

Jelaskan hubungan antara overriding dan polymorphism. Mengapa overriding menjadi dasar perilaku polimorfik pada Python?

## Soal 3 — Prediksi Output

```python
class Pengguna:
    def tampilkan_peran(self):
        return "Pengguna sistem"

class Mahasiswa(Pengguna):
    def tampilkan_peran(self):
        return "Mahasiswa"

class Dosen(Pengguna):
    def tampilkan_peran(self):
        return "Dosen"

for data in [Mahasiswa(), Dosen()]:
    print(data.tampilkan_peran())
```

Tuliskan output dari program tersebut dan jelaskan konsep OOP yang ditunjukkan.

## Soal 4 — Duck Typing

```python
class Mahasiswa:
    def ringkasan(self):
        return "Mahasiswa — Budi"

class Dosen:
    def ringkasan(self):
        return "Dosen — Sari"

def tampilkan(data):
    print(data.ringkasan())

tampilkan(Mahasiswa())
tampilkan(Dosen())
```

Jelaskan mengapa fungsi `tampilkan()` dapat menerima kedua object meskipun `Mahasiswa` dan `Dosen` tidak memiliki hubungan inheritance.

## Soal 5 — Merancang Fungsi Polimorfik

Tuliskan fungsi `tampilkan_semua(daftar)` yang menerima daftar object beragam dan memanggil method `ringkasan()` pada setiap object tanpa memeriksa tipe. Jelaskan apa yang terjadi jika sebuah object tidak memiliki method `ringkasan()`.