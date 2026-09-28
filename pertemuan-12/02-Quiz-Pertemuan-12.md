# Quiz Pertemuan 12 — Implementasi Mini Project Berbasis OOP

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 12 | **Tanggal:** 2 Desember 2026 | **CPMK:** CPMK115

## Petunjuk Pengerjaan

- Waktu: 20 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu, kecuali ada arahan dosen
- Soal 3–5 berbasis kode dan rancangan UML

## Soal 1 — UML ke Python

Jelaskan langkah utama untuk menerjemahkan satu class pada UML class diagram menjadi class Python.

## Soal 2 — Struktur Module

Jelaskan pembagian tanggung jawab yang tepat untuk `model.py`, `layanan.py`, dan `main.py` pada mini project OOP.

## Soal 3 — Relasi Antar-Object

Perhatikan kode berikut:

```python
class Peminjaman:
    def __init__(self, pengguna, ruang):
        self.pengguna = pengguna
        self.ruang = ruang
```

Relasi apa yang direpresentasikan oleh attribute `pengguna` dan `ruang`? Jelaskan alasan Anda.

## Soal 4 — Class Layanan

Mengapa pemeriksaan ruang yang sudah terdaftar dan penyimpanan daftar pengajuan dapat dikelola oleh class `LayananPeminjaman`, bukan oleh `Pengguna` atau `Ruang`? Jelaskan berdasarkan pembagian tanggung jawab.

## Soal 5 — Analisis Skenario

Sebuah implementasi memiliki UML dengan multiplicity `LayananPeminjaman "1" o-- "0..*" Ruang`, tetapi program tidak memiliki collection untuk menyimpan object `Ruang`. Identifikasi ketidaksesuaian tersebut dan tuliskan perbaikannya.
