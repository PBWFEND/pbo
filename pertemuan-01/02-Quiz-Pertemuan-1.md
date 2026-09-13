# Quiz Pertemuan 1 — Pengantar OOP & Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek
**Pertemuan:** 1 | **Tanggal:** 16 September 2026 | **CPMK:** CPMK114

---

## Petunjuk Pengerjaan

- ⏱️ Waktu: **15 menit**
- ✍️ Jumlah: **5 soal** — masing-masing bernilai **20 poin** (total 100)
- 📵 Dikerjakan **individu, tanpa catatan** (kecuali dosen menentukan lain)
- 💻 Soal 3–5 berbasis kode — tulis jawaban dengan jelas

---

## Soal 1 — Konsep Class & Object (20 poin)

Jelaskan perbedaan **class** dan **object** dengan kalimatmu sendiri, lalu berikan **satu contoh** dari Sistem Informasi Perpustakaan (sebutkan mana yang menjadi class dan mana yang menjadi object-nya).

> _Petunjuk: ingat analogi cetakan kue pada bagian Class dan Object._

**Jawaban:**

&nbsp;

---

## Soal 2 — Memahami `self` (20 poin)

a. Apa fungsi `self` di dalam method Python? *(10 poin)*

b. Apa yang terjadi jika parameter `self` **dihilangkan** dari sebuah instance method, lalu method tersebut dipanggil lewat object? Tuliskan pesan error yang muncul. *(10 poin)*

**Jawaban:**

&nbsp;

---

## Soal 3 — Prediksi Output (20 poin)

Perhatikan kode berikut:

```python
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def sapa(self):
        print(f"Halo, saya {self.nama} ({self.nim})")


m1 = Mahasiswa("Budi", "SI-101")
m2 = Mahasiswa("Ani", "SI-102")

m1.sapa()
m2.sapa()
```

Tuliskan **output** yang muncul saat kode dijalankan, dan jelaskan **mengapa `m1` dan `m2` menghasilkan output yang berbeda** padahal keduanya dibuat dari class yang sama.

**Jawaban:**

&nbsp;

---

## Soal 4 — Cari & Perbaiki Error (20 poin)

Kode berikut **memiliki 2 kesalahan**. Temukan, sebutkan, dan perbaiki:

```python
class Buku:
    def __init__(self, judul):
        self.judul = judul

    def info():
        print(f"Judul: {judul}")


b = Buku("Pemrograman Python")
b.info()
```

**Kesalahan 1:** &nbsp;

**Kesalahan 2:** &nbsp;

**Kode yang sudah diperbaiki:**

&nbsp;

---

## Soal 5 — Constructor & Class Attribute (20 poin)

Perhatikan kode berikut:

```python
class Produk:
    total_produk = 0

    def __init__(self, nama):
        self.nama = nama
        Produk.total_produk += 1


a = Produk("Laptop")
b = Produk("Mouse")
c = Produk("Keyboard")

print(Produk.total_produk)
print(a.nama)
```

a. Kapan method `__init__()` dipanggil? Apa fungsinya? *(10 poin)*

b. Tuliskan **output** kedua perintah `print` di atas, dan jelaskan perbedaan `total_produk` (class attribute) dengan `nama` (instance attribute). *(10 poin)*

**Jawaban:**

&nbsp;

---

