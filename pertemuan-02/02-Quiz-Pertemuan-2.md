# Quiz Pertemuan 2 — Class dan Object dengan Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 2 | **Tanggal:** 23 September 2026 | **CPMK:** CPMK114

## Petunjuk Pengerjaan

- Waktu: 15 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu tanpa catatan, kecuali ada arahan dosen
- Soal 3–5 berbasis kode Python

## Soal 1 — Class dan Object

Jelaskan perbedaan class dan object. Berikan contoh class `MataKuliah` dan dua object yang dibuat dari class tersebut.

## Soal 2 — Attribute dan Method

Jelaskan perbedaan attribute dan method. Berikan satu contoh masing-masing pada class `Mahasiswa`.

## Soal 3 — Prediksi Output

```python
class Buku:
    def __init__(self, judul):
        self.judul = judul

    def info(self):
        print(self.judul)


buku1 = Buku("Python Dasar")
buku2 = Buku("OOP dengan Python")
buku1.info()
buku2.info()
```

Tuliskan output dan jelaskan mengapa kedua object menghasilkan judul berbeda.

## Soal 4 — Melengkapi Method

Lengkapi class berikut agar `tambah_sks(3)` menambah nilai `sks` dan `info()` mencetak nama serta total SKS.

```python
class Mahasiswa:
    def __init__(self, nama):
        # Lengkapi
        pass

    def tambah_sks(self, jumlah):
        # Lengkapi
        pass

    def info(self):
        # Lengkapi
        pass
```

## Soal 5 — Interaksi Object

Jelaskan alur yang terjadi ketika `anggota.pinjam_buku(buku)` dipanggil pada sistem perpustakaan. Sebutkan method pada object `Anggota` dan object `Buku` yang terlibat.

---

