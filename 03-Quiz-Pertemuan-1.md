# Quiz Pertemuan 1 — Pengantar OOP & Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek
**Pertemuan:** 1 | **Minggu:** 16 September 2026 | **CPMK:** CPMK114

---

## Petunjuk Pengerjaan

- ⏱️ Waktu: **15 menit**
- ✍️ Jumlah: **5 soal** — masing-masing bernilai **20 poin** (total 100)
- 📵 Dikerjakan **individu, tanpa catatan** (kecuali dosen menentukan lain)
- 💻 Soal 3–5 berbasis kode — tulis jawaban dengan jelas

---

## Soal 1 — Konsep Class & Object (20 poin)

Jelaskan perbedaan **class** dan **object** dengan kalimatmu sendiri, lalu berikan **satu contoh** dari Sistem Informasi Perpustakaan (sebutkan mana yang menjadi class dan mana yang menjadi object-nya).

> _Petunjuk: ingat analogi cetakan kue di slide 6._

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
---

# 🔑 KUNCI JAWABAN

> ⚠️ **Untuk dosen** — hapus/sembunyikan bagian ini saat membagikan soal ke mahasiswa.

## Soal 1

- **Class** = blueprint/cetakan yang mendefinisikan data (attribute) dan perilaku (method); belum "nyata" di memori.
- **Object** = hasil instansiasi class; wujud nyata yang punya data sendiri.
- Contoh: `Buku` adalah **class**; `buku1 = Buku("Basis Data", "Budi")` adalah **object** (atau: satu buku konkret di rak perpustakaan).
- *Rubrik:* beda class vs object benar (10), contoh tepat dengan penunjukan class & object-nya (10).

## Soal 2

a. `self` adalah **referensi ke object sendiri** yang sedang memanggil method — lewat `self` method mengakses attribute/method milik object tersebut.

b. Muncul `TypeError`. Contoh:
```
TypeError: info() takes 0 positional arguments but 1 was given
```
Karena Python otomatis mengirim object pemanggil sebagai argumen pertama (`Buku.info(b)`), sementara method tidak menyediakan slot parameternya.
- *Rubrik:* (a) makna self benar (10); (b) menyebut TypeError dan benar mengapa (10) — pesan error persis tidak wajib, asalkan `TypeError` + alasan "object dikirim otomatis" muncul.

## Soal 3

Output:
```
Halo, saya Budi (SI-101)
Halo, saya Ani (SI-102)
```
Karena `m1` dan `m2` adalah **dua object berbeda** — masing-masing punya salinan sendiri untuk attribute `nama` dan `nim` (instance attribute) yang diisi `__init__` saat instansiasi. Class-nya sama (blueprint sama), datanya berbeda.
- *Rubrik:* output keduanya benar (10); penjelasan "instance attribute milik masing-masing object" (10).

## Soal 4

- **Kesalahan 1:** method `info()` tidak punya parameter `self`.
- **Kesalahan 2:** baris cetak memakai `judul` tanpa `self.` → `NameError: name 'judul' is not defined`.

Kode benar:
```python
class Buku:
    def __init__(self, judul):
        self.judul = judul

    def info(self):
        print(f"Judul: {self.judul}")


b = Buku("Pemrograman Python")
b.info()
```
- *Rubrik:* tiap kesalahan benar disebut **dan** diperbaiki (10 + 10). Menyebut error tapi perbaikan salah: setengah poin per butir.

## Soal 5

a. `__init__()` dipanggil **otomatis oleh Python saat object dibuat** (saat `Produk(...)` dijalankan) — fungsinya mengisi **nilai awal** attribute object / menyiapkan object agar valid sejak lahir.

b. Output:
```
3
Laptop
```
`total_produk` adalah **class attribute** — satu nilai milik class, dibagi semua object (bertambah tiap instansiasi: 3). `nama` adalah **instance attribute** — milik masing-masing object (`a.nama` hanya milik `a`).
- *Rubrik:* (a) "dipanggil otomatis saat object dibuat" + fungsi nilai awal (10); (b) output benar (5) + perbedaan class vs instance attribute (5).

---

## Skor & Tindak Lanjut

| Skor | Tindak Lanjut |
| ---- | ------------- |
| 80–100 | Siap lanjut Pertemuan 2; beri tantangan tambahan (mini challenge level 2) |
| 60–79 | Lanjut, ulangi bagian yang salah lewat materi slide terkait |
| < 60 | Pendampingan khusus: ulangi slide 6–11 + praktikum `code/pertemuan-01/` bersama asisten |

*Hasil quiz mencatat skor komponen "Quiz minggu 1" sesuai Timeline.md (Output: Quiz & diskusi).*
