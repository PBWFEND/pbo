# Quiz Pertemuan 9 — Implementasi OOP dengan Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 9 | **Tanggal:** 11 November 2026 | **CPMK:** CPMK115

## Petunjuk Pengerjaan

- Waktu: 20 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu, kecuali ada arahan dosen
- Soal 3–5 berbasis kode Python

## Soal 1 — Identifikasi Object

Sistem Informasi perpustakaan memiliki data buku, anggota, dan proses peminjaman. Identifikasi tiga object yang dapat dimodelkan sebagai class. Untuk setiap object, tuliskan dua attribute dan dua method yang sesuai.

## Soal 2 — Pembagian Tanggung Jawab

Jelaskan alasan class `Buku`, `Anggota`, dan `Perpustakaan` sebaiknya memiliki tanggung jawab yang berbeda. Apa risiko jika seluruh operasi diletakkan dalam satu class?

## Soal 3 — Encapsulation

Perhatikan kode berikut:

```python
class Buku:
    def __init__(self, judul):
        self.judul = judul
        self.__tersedia = True

    @property
    def tersedia(self):
        return self.__tersedia
```

Jelaskan tujuan attribute `__tersedia` dan property `tersedia`. Mengapa program tidak memberikan setter publik untuk attribute tersebut?

## Soal 4 — Interaksi Antar-Object

Tuliskan method `pinjamkan(self, nomor_anggota, kode_buku)` pada class `Perpustakaan` yang melakukan hal berikut:

1. Mencari anggota dan buku berdasarkan identifier.
2. Menolak operasi jika salah satu object tidak ditemukan.
3. Memanggil method `pinjam()` pada object buku.
4. Menambahkan kode buku ke daftar pinjaman anggota jika peminjaman berhasil.
5. Mengembalikan `True` atau `False`.

## Soal 5 — Analisis Skenario

Sebuah buku yang sedang dipinjam masih dapat dipinjam oleh anggota lain. Analisis kemungkinan kesalahan pada desain atau implementasinya, lalu tuliskan perbaikan yang diperlukan.
