# Soal UTS — Konsep OOP, Analisis Desain, dan Coding

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 8 | **Tanggal:** 4 November 2026 | **CPMK:** CPMK114  
**Bobot:** 20% dari nilai akhir

## Petunjuk Umum

- Waktu: sesuai jadwal kelas — Rabu, 4 November 2026, 15:30–18:00
- UTS terdiri dari dua bagian: **Bagian A (Teori)** dan **Bagian B (Coding)**
- Dikerjakan secara individu tanpa catatan dan tanpa bantuan AI, kecuali ada arahan dosen
- Untuk soal coding, tulis kode pada file Python terpisah: `soal_a1.py`, `soal_a2.py`, `soal_b1.py`, `soal_b2.py`, `soal_b3.py`
- Jalankan setiap file dengan `python3 <nama_file>.py` dan pastikan program berjalan tanpa error
- Gunakan Python 3 dan standard library
- Penamaan class `PascalCase`, function dan variable `snake_case`, indentasi empat spasi

---

## Bagian A — Teori (40 poin)

### Soal A1 — Konsep Dasar OOP (10 poin)

Jelaskan pengertian dari kelima konsep berikut dan berikan satu contoh penerapannya pada kode Python:

1. `class`
2. `object`
3. `attribute`
4. `method`
5. `constructor`

### Soal A2 — Pilar OOP (15 poin)

Jelaskan keempat pilar OOP berikut beserta penggunaannya pada program Python:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

Untuk setiap pilar, sertakan satu contoh kode singkat yang menunjukkan penerapannya.

### Soal A3 — Analisis Desain (15 poin)

Perhatikan rancangan class berikut:

```python
class Pengguna:
    def __init__(self, nama, email):
        self.__nama = nama
        self.__email = email

    @property
    def nama(self):
        return self.__nama

class Mahasiswa(Pengguna):
    def __init__(self, nama, email, nim):
        super().__init__(nama, email)
        self.nim = nim

    def tampilkan_peran(self):
        return f"{self.nama} adalah mahasiswa dengan NIM {self.nim}"
```

Jawab pertanyaan berikut:

1. Konsep OOP mana yang diterapkan pada `self.__nama` dan `@property`? Jelaskan alasan teknisnya.
2. Konsep OOP mana yang diterapkan pada `class Mahasiswa(Pengguna)`? Jelaskan apa yang dilakukan `super()`.
3. Mengapa `self.nama` dapat dipanggil pada method `tampilkan_peran()` di subclass meskipun attribute tersebut privat di superclass?

---

## Bagian B — Coding dan Problem Solving (60 poin)

### Soal B1 — Class dan Encapsulation (20 poin)

Buat class `Buku` dengan ketentuan berikut:

1. Constructor menerima `judul` (str) dan `penulis` (str).
2. Attribute `tersedia` diinisialisasi dengan `True` dan bersifat privat.
3. Method `pinjam()` mengubah `tersedia` menjadi `False` dan mengembalikan `True` jika buku tersedia. Jika tidak tersedia, kembalikan `False`.
4. Method `kembalikan()` mengubah `tersedia` menjadi `True`.
5. Property `tersedia` mengembalikan status ketersediaan tanpa bisa diubah langsung dari luar class.
6. Method `__str__()` mengembalikan string berformat: `"judul — penulis [Tersedia]"` atau `"judul — penulis [Dipinjam]"`.

Tulis program utama yang membuat dua object `Buku`, meminjam satu buku, dan menampilkan status kedua buku.

### Soal B2 — Inheritance dan Polymorphism (20 poin)

Diberikan class `Buku` dari Soal B1. Buat subclass `BukuDigital` dengan ketentuan berikut:

1. Subclass mewarisi `Buku` dan menambahkan attribute `format_file` (str, misalnya `"PDF"` atau `"EPUB"`).
2. Constructor menggunakan `super()` untuk memanggil constructor parent.
3. Override method `__str__()` sehingga formatnya menjadi: `"judul — penulis [Dipinjam] (format_file)"`.
4. Method `unduh()` mengembalikan string `"Mengunduh judul dalam format format_file."` jika buku tersedia, dan `"Buku tidak tersedia."` jika sedang dipinjam.

Selanjutnya, tulis fungsi `tampilkan_info(daftar_buku)` yang menerima list berisi object `Buku` dan `BukuDigital`, lalu mencetak `__str__()` dari setiap object. Fungsi ini harus bekerja untuk kedua tipe object tanpa pengecekan tipe eksplisit.

### Soal B3 — Analisis dan Perbaikan Kode (20 poin)

Perhatikan kode berikut yang memiliki beberapa kesalahan:

```python
class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo = self.saldo + jumlah

    def tarik(self, jumlah):
        self.saldo = self.saldo - jumlah

    def tampilkan_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.saldo}")
```

Tugas:

1. Identifikasi tiga kesalahan atau kelemahan pada kode tersebut dari perspektif OOP.
2. Perbaiki kode dengan menerapkan encapsulation (attribute privat), validasi pada method `setor()` dan `tarik()` (jumlah harus positif dan penarikan tidak boleh melebihi saldo), serta property untuk mengakses saldo.
3. Tulis program utama yang mendemonstrasikan: setor uang, tarik uang yang valid, tarik uang yang melebihi saldo (harus menolak), dan tarik jumlah negatif (harus menolak).
