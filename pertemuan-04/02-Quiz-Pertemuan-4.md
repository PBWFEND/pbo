# Quiz Pertemuan 4 — Inheritance pada Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 4 | **Tanggal:** 7 Oktober 2026 | **CPMK:** CPMK114

## Petunjuk Pengerjaan

- Waktu: 15 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu tanpa catatan, kecuali ada arahan dosen
- Soal 3–5 berbasis kode Python

## Soal 1 — Superclass dan Subclass

Jelaskan perbedaan superclass dan subclass. Berikan satu contoh hierarki class dari Sistem Informasi Perpustakaan.

## Soal 2 — Fungsi `super().__init__()`

Jelaskan fungsi `super().__init__()` pada constructor subclass. Mengapa pemanggilan tersebut diperlukan?

## Soal 3 — Overriding

Jelaskan overriding dan berikan contoh penerapannya pada method yang diwarisi dari superclass.

## Soal 4 — Hubungan is-a

Mengapa inheritance sebaiknya digunakan ketika terdapat hubungan **is-a**? Jelaskan alasan teknisnya.

## Soal 5 — Prediksi Output

```python
class Pengguna:
    def tampilkan_peran(self):
        return "Pengguna"

class Mahasiswa(Pengguna):
    def tampilkan_peran(self):
        return "Mahasiswa"
```

Tuliskan output dari `Mahasiswa().tampilkan_peran()` dan jelaskan konsep OOP yang ditunjukkan.
