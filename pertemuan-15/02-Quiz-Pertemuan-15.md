# Quiz Pertemuan 15 — Testing, Dokumentasi, dan Presentasi Mini Project

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 15 | **Tanggal:** 23 Desember 2026 | **CPMK:** CPMK116

## Petunjuk Pengerjaan

- Waktu: 20 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu, kecuali ada arahan dosen
- Soal 2–5 berbasis kode dan skenario

## Soal 1 — Test Case

Jelaskan komponen minimal sebuah test case. Mengapa `expected result` harus ditentukan sebelum program dijalankan?

## Soal 2 — Assertion

Jelaskan perbedaan penggunaan `assertEqual()` dan `assertRaises()` pada `unittest`. Berikan contoh kondisi yang sesuai untuk masing-masing.

## Soal 3 — Test Method

Perhatikan class berikut:

```python
class Ruang:
    def __init__(self, kode, kapasitas):
        if kapasitas <= 0:
            raise ValueError("Kapasitas harus positif")
        self.kode = kode
        self.kapasitas = kapasitas
```

Tuliskan dua test method: satu untuk kapasitas valid dan satu untuk kapasitas `0`.

## Soal 4 — Evaluasi Testing

Sebuah test hanya memeriksa bahwa program tidak mengalami crash, tetapi tidak memeriksa nilai hasil operasi. Jelaskan keterbatasan test tersebut dan assertion yang dapat ditambahkan.

## Soal 5 — Dokumentasi dan Presentasi

Sebutkan minimal empat bagian yang harus ada pada README mini project dan jelaskan dua bukti yang perlu ditampilkan saat demo project.
