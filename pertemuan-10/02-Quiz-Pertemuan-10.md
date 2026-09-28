# Quiz Pertemuan 10 — Analisis Object dan Class

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 10 | **Tanggal:** 18 November 2026 | **CPMK:** CPMK115

## Petunjuk Pengerjaan

- Waktu: 20 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu, kecuali ada arahan dosen
- Soal 3–5 berbasis kode dan analisis kasus

## Soal 1 — Kandidat Class

Sistem Informasi klinik mengelola pasien, dokter, jadwal pemeriksaan, dan rekam medis. Identifikasi minimal empat kandidat class dan jelaskan alasan setiap kandidat dipilih.

## Soal 2 — Attribute dan Method

Untuk class `Pasien`, tuliskan tiga attribute dan tiga method yang sesuai dengan kebutuhan klinik. Jelaskan perbedaan antara attribute dan method yang Anda pilih.

## Soal 3 — Tanggung Jawab Class

Sebuah class `SistemKlinik` menyimpan data pasien, memvalidasi jadwal, menghitung biaya, mencetak laporan, dan menyimpan file. Analisis masalah rancangan tersebut dan usulkan pembagian tanggung jawab yang lebih tepat.

## Soal 4 — Analisis Kode

```python
class MataKuliah:
    def __init__(self, kode, nama, kapasitas):
        self.kode = kode
        self.nama = nama
        self.kapasitas = kapasitas
        self.jumlah_peserta = 0

    def masih_tersedia(self):
        return self.jumlah_peserta < self.kapasitas
```

Identifikasi attribute dan method pada kode tersebut. Jelaskan aturan bisnis yang dikelola oleh method `masih_tersedia()`.

## Soal 5 — Relasi Antar-Class

Pada sistem akademik terdapat class `Mahasiswa`, `KRS`, dan `MataKuliah`. Jelaskan minimal dua relasi antar-class tersebut dan berikan alasan mengapa relasi itu diperlukan dalam skenario pengisian KRS.
