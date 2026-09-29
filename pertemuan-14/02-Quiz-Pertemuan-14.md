# Quiz Pertemuan 14 — Exception Handling, Validation, Debugging, dan Refactoring

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 14 | **Tanggal:** 16 Desember 2026 | **CPMK:** CPMK115

## Petunjuk Pengerjaan

- Waktu: 20 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu, kecuali ada arahan dosen
- Soal 2–5 berbasis kode dan skenario

## Soal 1 — Jenis Kesalahan

Jelaskan perbedaan syntax error, runtime error, validation error, dan logic error. Berikan satu contoh singkat untuk masing-masing.

## Soal 2 — Exception Handling

Mengapa `except Exception` sebaiknya tidak digunakan sebagai satu-satunya penanganan semua kesalahan? Jelaskan cara memilih exception yang lebih spesifik.

## Soal 3 — Custom Exception

Tuliskan class `DataTidakDitemukanError` dan method `cari_ruang_wajib(self, kode)` yang menaikkan exception tersebut ketika ruang tidak ditemukan.

## Soal 4 — Validation

Sebuah class `Ruang` menerima kapasitas `0` dan string kosong sebagai nama. Jelaskan validation yang harus ditambahkan dan kapan validation tersebut dijalankan.

## Soal 5 — Refactoring

Sebuah service memiliki kode pencarian object yang sama pada lima method. Usulkan strategi refactoring dan jelaskan cara memastikan perilaku CRUD tidak berubah setelah refactoring.
