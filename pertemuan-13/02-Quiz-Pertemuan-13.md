# Quiz Pertemuan 13 — CRUD dan Pengelolaan Data dengan Object

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 13 | **Tanggal:** 9 Desember 2026 | **CPMK:** CPMK115

## Petunjuk Pengerjaan

- Waktu: 20 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu, kecuali ada arahan dosen
- Soal 3–5 berbasis kode dan analisis skenario

## Soal 1 — Konsep CRUD

Jelaskan perbedaan Create, Read, Update, dan Delete pada aplikasi OOP. Berikan satu contoh operasi untuk setiap jenis.

## Soal 2 — Identifier

Mengapa collection object sebaiknya menggunakan identifier yang stabil? Jelaskan risiko menggunakan index list sebagai identifier saat data dihapus.

## Soal 3 — Validasi Create

Perhatikan kode berikut:

```python
def tambah_ruang(self, ruang):
    if ruang.kode in self.__ruang:
        return False
    self.__ruang[ruang.kode] = ruang
    return True
```

Jelaskan tujuan pemeriksaan kode duplikat dan hasil yang dikembalikan method tersebut.

## Soal 4 — Analisis Update

Sebuah method `ubah_kapasitas(kode, kapasitas_baru)` langsung mengubah attribute tanpa memeriksa apakah kode ditemukan dan apakah kapasitas bernilai positif. Identifikasi dua masalah pada method tersebut dan jelaskan perbaikannya.

## Soal 5 — Analisis Delete

Sistem menolak penghapusan ruang yang masih digunakan oleh pengajuan aktif. Jelaskan mengapa pemeriksaan dependensi diperlukan sebelum operasi Delete.
