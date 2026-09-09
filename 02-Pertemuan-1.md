# Pertemuan 1 — Pengantar OOP & Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek
**Pertemuan:** 1 dari 16 | **Minggu:** 16 September 2026
**CPMK:** CPMK114
**Materi:** Pengantar OOP & Python — paradigma OOP, class, object, attribute, method, constructor

---

## Slide 1 — Judul

# Pengantar OOP & Python
### Pemrograman Berorientasi Objek — Pertemuan 1

- Program Studi Sistem Informasi — SI-IIIA
- Semester 2026/2027 Gasal
- Rabu, 16 September 2026 | 15:30–18:00 | Lab. 2

> *"Belajar melihat dunia sebagai kumpulan objek yang saling berinteraksi."*

---

## Slide 2 — Capaian Pembelajaran Pertemuan 1

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** alasan OOP penting dalam pengembangan Sistem Informasi
2. **Membedakan** paradigma *procedural* dan *object-oriented*
3. **Menjelaskan** konsep **class, object, attribute, method,** dan **constructor**
4. **Menjelaskan** peran `self` dan `__init__()` dalam Python
5. **Menulis** program Python sederhana berbasis class dan object
6. **Memodelkan** entitas Sistem Informasi Perpustakaan sebagai class Python

**Asesmen:** Quiz (Minggu 1) + Praktikum terbimbing + Latihan mandiri

---

## Slide 3 — Mengapa OOP Penting untuk Sistem Informasi?

Sistem Informasi (SI) memodelkan **dunia nyata**: mahasiswa, dosen, buku, transaksi, pegawai...

**Masalah pendekatan prosedural saat program membesar:**

- Data (variabel) dan perilaku (fungsi) **terpisah** → mudah tidak sinkron
- Perubahan kecil bisa merusak bagian lain (*ripple effect*)
- Sulit memetakan kode ke entitas bisnis yang dihadapi user

**Yang ditawarkan OOP:**

| Dunia Nyata / SI | OOP |
| ---------------- | --- |
| Mahasiswa, Buku, Transaksi | **Class** |
| Data yang dimiliki entitas | **Attribute** |
| Apa yang bisa dilakukan entitas | **Method** |
| Satu mahasiswa konkret | **Object** |

> 💡 Kode yang lebih mudah **dimengerti**, **diperbaiki**, dan **dikembangkan** — skill yang paling dicari saat membangun aplikasi SI skala industri.

---

## Slide 4 — Relevansi Python dan AI di Industri 2026

**Python = bahasa #1 dunia** (indeks TIOBE & IEEE Spectrum, 2021–sekarang)

- **AI & Machine Learning:** PyTorch, TensorFlow, scikit-learn
- **Data Engineering & Analytics:** pandas, Polars, Apache Airflow
- **Backend Web & API:** Django, FastAPI
- **Otomasi & DevOps:** scripting, CI/CD, testing
- **LLM Engineering:** LangChain, integrasi OpenAI/Anthropic API

**Mengapa Python untuk belajar OOP?**

- Sintaks bersih → fokus pada **konsep OOP**, bukan tata bahasa
- `python3`, `pip`, `venv` tersedia di semua OS
- Tool AI coding assistant (Copilot, Cursor, ChatGPT/Claude) paling matang untuk Python

> 📈 Karier SI 2026: *Data Analyst* → *Data Engineer* → *AI Engineer* — semuanya Python-first.

---

## Slide 5 — Paradigma Procedural vs OOP

**Procedural:** program = urutan instruksi + fungsi yang memproses data terpisah

```python
# PROSEDURAL
mahasiswa_nama = "Budi"
mahasiswa_nim = "SI-101"
mahasiswa_sks = 24

def tampilkan(nama, nim, sks):
    print(f"{nama} ({nim}) - {sks} SKS")

tampilkan(mahasiswa_nama, mahasiswa_nim, mahasiswa_sks)
```

**OOP:** data + perilaku dibungkus jadi satu (**object**)

```python
# OOP
class Mahasiswa:
    def __init__(self, nama, nim, sks):
        self.nama = nama
        self.nim = nim
        self.sks = sks

    def perkenalan(self):
        print(f"{self.nama} ({self.nim}) - {self.sks} SKS")

mhs = Mahasiswa("Budi", "SI-101", 24)
mhs.perkenalan()
```

**Perbedaan inti:**

| Aspek | Procedural | OOP |
| ----- | ---------- | --- |
| Unit utama | Fungsi | Object (class) |
| Data & perilaku | Terpisah | Menyatu (*encapsulation*) |
| Cocok untuk | Script kecil | Aplikasi SI besar |

---

## Slide 6 — Konsep Dasar: Class dan Object

**Class** = *blueprint/cetakan* → mendefinisikan data & perilaku
**Object** = *instansiasi* class → wujud nyata di memori

```python
class Buku:
    pass  # blueprint kosong dulu

# Membuat object (instansiasi)
buku1 = Buku()
buku2 = Buku()
```

**Analogi:** Class = cetakan kue 🍪, Object = kue jadi.
Satu cetakan → banyak kue, tiap kue bisa berbeda isi (coklat, keju...).

```
     Class Buku            Object buku1        Object buku2
  ┌─────────────────┐    ┌──────────────┐    ┌──────────────┐
  │ judul           │    │ judul="AI 101"│   │ judul="PBO"  │
  │ penulis         │ →  │ penulis="Ani" │   │ penulis="Ben"│
  │ tersedia        │    │ tersedia=True │   │ tersedia=False│
  └─────────────────┘    └──────────────┘    └──────────────┘
```

> Ingat: **class sekali dibuat, object bisa banyak** — masing-masing punya data sendiri.

---

## Slide 7 — Attribute: Data yang Dimiliki Object

**Attribute** = variabel yang menempel pada object.

**Dua jenis:**

```python
class Mahasiswa:
    jumlah_mahasiswa = 0          # class attribute (dibagi semua object)

    def __init__(self, nama, nim):
        self.nama = nama          # instance attribute (milik tiap object)
        self.nim = nim
        Mahasiswa.jumlah_mahasiswa += 1

m1 = Mahasiswa("Budi", "SI-101")
m2 = Mahasiswa("Ani", "SI-102")

print(m1.nama)                    # Budi
print(m2.nama)                    # Ani
print(Mahasiswa.jumlah_mahasiswa) # 2
```

- **Instance attribute:** `m1.nama` ≠ `m2.nama` — tiap object beda
- **Class attribute:** satu nilai untuk semua object (misal counter, konstanta)

---

## Slide 8 — Method: Perilaku Object

**Method** = fungsi yang didefinisikan di dalam class → perilaku object.

```python
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True

    def info(self):                      # method menampilkan info
        status = "Tersedia" if self.tersedia else "Dipinjam"
        print(f"'{self.judul}' — {self.penulis} [{status}]")

    def pinjam(self):                    # method mengubah state
        if self.tersedia:
            self.tersedia = False
            print(f"Buku '{self.judul}' dipinjam.")
        else:
            print(f"Maaf, '{self.judul}' sedang dipinjam.")

buku = Buku("OOP dengan Python", "Andi")
buku.info()      # 'OOP dengan Python' — Andi [Tersedia]
buku.pinjam()    # Buku 'OOP dengan Python' dipinjam.
buku.info()      # 'OOP dengan Python' — Andi [Dipinjam]
```

> Method bisa **membaca** dan **mengubah** attribute object itu sendiri.

---

## Slide 9 — Constructor: `__init__()`

**Constructor** = method khusus yang otomatis dipanggil saat object dibuat.

```python
class Mahasiswa:
    def __init__(self, nama, nim):   # dipanggil oleh Mahasiswa(...)
        self.nama = nama
        self.nim = nim
        print(f"Object Mahasiswa {nama} berhasil dibuat!")

mhs = Mahasiswa("Budi", "SI-101")
# Output: Object Mahasiswa Budi berhasil dibuat!
```

**Kegunaan constructor:**

- Memberi **nilai awal** attribute saat object lahir
- Memastikan object **selalu valid** sejak awal (misal `tersedia = True`)
- Menerima **parameter** dari pemanggil: `Mahasiswa("Budi", "SI-101")`

> Tanpa `__init__`, object dibuat "kosong" — kita harus mengisi attribute satu per satu.

---

## Slide 10 — Memahami `self`

**`self`** = referensi ke **object sendiri** yang sedang memanggil method.

```python
class Mahasiswa:
    def perkenalan(self):
        print(f"Saya {self.nama}")   # self = object yang memanggil

m1 = Mahasiswa(); m1.nama = "Budi"
m2 = Mahasiswa(); m2.nama = "Ani"

m1.perkenalan()   # self → m1  → "Saya Budi"
m2.perkenalan()   # self → m2  → "Saya Ani"
```

**Cara Python menerjemahkan:**

```python
m1.perkenalan()           # bentuk panggilan
Mahasiswa.perkenalan(m1)  # makna sebenarnya: m1 dikirim sebagai self
```

**Aturan penting:**

- `self` **wajib** menjadi **parameter pertama** setiap instance method
- Nama `self` hanyalah **kesepakatan** — tapi **jangan ganti** (konvensi seluruh komunitas Python)
- Di dalam method, akses attribute selalu lewat `self.attribute`

---

## Slide 11 — Anatomi Class Python

Semua konsep dalam satu gambar:

```python
class Mahasiswa:                    # 1. definisi class (CamelCase)
    universitas = "UNSAP"           # 2. class attribute

    def __init__(self, nama, nim):  # 3. constructor
        self.nama = nama            # 4. instance attribute
        self.nim = nim

    def perkenalan(self):           # 5. instance method
        print(f"Saya {self.nama} dari {self.universitas}")

    def __str__(self):              # 6. method khusus (magic method)
        return f"Mahasiswa({self.nama}, {self.nim})"


mhs = Mahasiswa("Budi", "SI-101")   # 7. instansiasi → __init__ jalan otomatis
print(mhs)                          # Mahasiswa(Budi, SI-101)
mhs.perkenalan()                    # Saya Budi dari UNSAP
```

**Ingat penomoran:** 1 definisi → 2 class attribute → 3 constructor → 4 instance attribute → 5 method → 6 magic method → 7 instansiasi.

---

## Slide 12 — Contoh Kode 1: Class Mahasiswa (File Lengkap)

📄 **File:** `code/pertemuan-01/mahasiswa.py`

```python
class Mahasiswa:
    """Class Mahasiswa untuk data akademik sederhana."""

    jumlah_mahasiswa = 0  # class attribute

    def __init__(self, nama, nim, prodi="Sistem Informasi"):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.sks = 0
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_sks(self, jumlah):
        self.sks += jumlah
        print(f"{self.nama}: total {self.sks} SKS")

    def perkenalan(self):
        print(f"Halo, saya {self.nama} ({self.nim}) - {self.prodi}")

    def __str__(self):
        return f"Mahasiswa({self.nama}, {self.nim})"


# === Program utama ===
if __name__ == "__main__":
    m1 = Mahasiswa("Budi Santoso", "SI-101")
    m2 = Mahasiswa("Ani Lestari", "SI-102")

    m1.perkenalan()
    m2.perkenalan()

    m1.tambah_sks(3)
    m1.tambah_sks(2)
    m2.tambah_sks(4)

    print(m1)
    print(f"Total mahasiswa: {Mahasiswa.jumlah_mahasiswa}")
```

**Output yang diharapkan:**
```
Halo, saya Budi Santoso (SI-101) - Sistem Informasi
Halo, saya Ani Lestari (SI-102) - Sistem Informasi
Budi Santoso: total 3 SKS
Budi Santoso: total 5 SKS
Ani Lestari: total 4 SKS
Mahasiswa(Budi Santoso, SI-101)
Total mahasiswa: 2
```

---

## Slide 13 — Studi Kasus: Sistem Informasi Perpustakaan

**Skenario:** Perpustakaan kampus meminjamkan buku ke mahasiswa.

**Langkah analisis object (minggu 10 akan kita dalami):**

1. Cari **kata benda** penting → calon class: `Buku`, `Anggota`
2. Cari **data** yang dimiliki tiap benda → attribute
3. Cari **aksi/peristiwa** → method

| Entitas | Attribute | Method |
| ------- | --------- | ------ |
| `Buku` | judul, penulis, tersedia | `info()`, `pinjam()`, `kembalikan()` |
| `Anggota` | nama, id_anggota, daftar_pinjam | `pinjam_buku()`, `kembalikan_buku()`, `lihat_pinjaman()` |

**Interaksi antar-object:**

```
Anggota --pinjam_buku(buku)--> Buku
   │                             │
   │ tambah ke daftar_pinjam     │ tersedia = False
   ▼                             ▼
```

> 🎯 Ini yang dimaksud "OOP memodelkan dunia nyata": object **saling bekerja sama** lewat pemanggilan method.

---

## Slide 14 — Contoh Kode 2: Sistem Perpustakaan (File Lengkap)

📄 **File:** `code/pertemuan-01/perpustakaan.py`

```python
class Buku:
    """Merepresentasikan satu buku di perpustakaan."""

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def kembalikan(self):
        self.tersedia = True

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"'{self.judul}' oleh {self.penulis} [{status}]"


class Anggota:
    """Merepresentasikan anggota perpustakaan."""

    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.daftar_pinjam = []   # list berisi object Buku

    def pinjam_buku(self, buku):
        if buku.pinjam():                       # object Buku bekerja
            self.daftar_pinjam.append(buku)
            print(f"{self.nama} meminjam '{buku.judul}'")
        else:
            print(f"'{buku.judul}' sedang tidak tersedia")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_pinjam:
            buku.kembalikan()
            self.daftar_pinjam.remove(buku)
            print(f"{self.nama} mengembalikan '{buku.judul}'")
        else:
            print(f"{self.nama} tidak meminjam '{buku.judul}'")

    def lihat_pinjaman(self):
        print(f"Pinjaman {self.nama}:")
        if not self.daftar_pinjam:
            print("  (tidak ada)")
        for buku in self.daftar_pinjam:
            print(f"  - {buku.judul}")


# === Program utama ===
if __name__ == "__main__":
    buku1 = Buku("Pemrograman Python", "Andi")
    buku2 = Buku("Basis Data", "Budi")
    anggota = Anggota("Citra", "A-001")

    anggota.pinjam_buku(buku1)
    anggota.pinjam_buku(buku2)
    anggota.lihat_pinjaman()

    anggota.kembalikan_buku(buku1)
    anggota.lihat_pinjaman()
    print(buku1)
```

**Output yang diharapkan:**
```
Citra meminjam 'Pemrograman Python'
Citra meminjam 'Basis Data'
Pinjaman Citra:
  - Pemrograman Python
  - Basis Data
Citra mengembalikan 'Pemrograman Python'
Pinjaman Citra:
  - Basis Data
'Pemrograman Python' oleh Andi [Tersedia]
```

---

## Slide 15 — Menjalankan Kode Praktikum

Cara menjalankan file contoh (lihat juga `01-IDE.md`):

```bash
# 1. Pastikan Python 3 ter-install
python --version

# 2. Masuk folder kode
cd code/pertemuan-01

# 3. Jalankan
python mahasiswa.py
python perpustakaan.py
```

**Eksperimen yang disarankan saat praktikum:**

1. Tambah attribute `tahun` pada class `Buku` → update `__str__`
2. Buat object ke-3 `Mahasiswa`, cek `jumlah_mahasiswa` menjadi 3
3. Coba pinjam buku yang sama dua kali — amati pesan error-nya
4. Panggil `buku1.pinjam()` langsung tanpa lewat `Anggota` — apa yang terjadi?

> 💡 Jangan hanya membaca kode — **ubah, jalankan, rusak, perbaiki**. Itu cara belajar OOP tercepat.

---

## Slide 16 — Latihan Terbimbing (Bersama Dosen)

**Bersama-sama di kelas (± 30 menit):**

Buat class `Dosen` dengan spesifikasi:

| Bagian | Isi |
| ------ | --- |
| Attribute | `nama`, `nidn`, `mata_kuliah` |
| Constructor | menerima 3 parameter di atas |
| Method `mengajar()` | cetak `"Dosen {nama} mengajar {mata_kuliah}"` |
| Method `perkenalan()` | cetak `"Saya {nama}, NIDN {nidn}"` |

**Kerangka awal (lengkapi):**

```python
class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        # TODO 1: simpan ketiga parameter sebagai attribute
        pass

    def mengajar(self):
        # TODO 2: cetak "Dosen {nama} mengajar {mata_kuliah}"
        pass

    def perkenalan(self):
        # TODO 3: cetak "Saya {nama}, NIDN {nidn}"
        pass


dosen = Dosen("Pak Yofi", "001234", "PBO")
dosen.mengajar()      # Dosen Pak Yofi mengajar PBO
dosen.perkenalan()    # Saya Pak Yofi, NIDN 001234
```

**Target:** mahasiswa menyelesaikan 3 TODO bersama, lalu jalankan dan cocokkan output.

---

## Slide 17 — Latihan Mandiri

**Kerjakan di rumah, kumpulkan sebelum pertemuan berikutnya:**

Buat file `latihan_mandiri_1.py` berisi class `Produk`:

1. **Attribute:** `nama`, `harga`, `stok`
2. **Constructor:** mengisi ketiga attribute dari parameter
3. **Method `info()`:** mencetak `"{nama} - Rp{harga} (stok: {stok})"`
4. **Method `jual(jumlah)`:** mengurangi stok; tolak jika stok kurang dari `jumlah` (cetak pesan)
5. **Method `restock(jumlah)`:** menambah stok
6. **Bonus:** tambahkan class attribute `total_produk` yang menghitung jumlah object `Produk` yang dibuat

**Contoh pemakaian:**

```python
p = Produk("Laptop", 8000000, 5)
p.info()          # Laptop - Rp8000000 (stok: 5)
p.jual(2)
p.info()          # Laptop - Rp8000000 (stok: 3)
p.jual(10)        # Stok tidak cukup!
p.restock(10)
p.info()          # Laptop - Rp8000000 (stok: 13)
```

**Kriteria penilaian:** constructor benar (30%), method jalan sesuai output (50%), gaya penulisan rapi & PEP 8 (20%).

---

## Slide 18 — Mini Challenge 🏆

**"Perpustakaan Plus" — tingkatkan sistem perpustakaan:**

Tambahkan ke class `Buku` (dari `perpustakaan.py`):

1. Attribute `kode` (misal `BK-001`) — unik untuk tiap buku
2. Attribute `dipinjam_oleh` — menyimpan nama anggota yang meminjam (atau `None`)
3. Update `__str__` agar menampilkan kode dan peminjam
4. Di class `Anggota`, saat pinjam → set `buku.dipinjam_oleh = self.nama`

**Level 2 (untuk yang cepat selesai):**

- Tambah class `Perpustakaan` dengan attribute `daftar_buku` (list)
- Method `tambah_buku(buku)` dan `cari_buku(judul)` yang mengembalikan object `Buku` atau `None`

**Ketentuan:**

- ⏱️ 20 menit di kelas, boleh berpasangan (*pair programming*)
- ✅ Wajib jalan tanpa error
- 🚀 Demo 1 menit di depan: tunjukkan object berinteraksi

> Pertanyaan pemantik: bagaimana memastikan dua buku tidak punya kode sama?

---

## Slide 19 — Kesalahan Umum Pemula

| # | Kesalahan | Contoh Salah | Perbaikan |
| - | --------- | ------------ | --------- |
| 1 | Lupa `self` di method | `def pinjam(self):` ditulis `def pinjam():` | Selalu tulis `self` pertama |
| 2 | Lupa `self.` saat akses attribute | `judul = judul` | `self.judul = judul` |
| 3 | Memanggil `__init__` manual | `mhs.__init__("Budi")` | `mhs = Mahasiswa("Budi")` |
| 4 | Nama class tidak CamelCase | `class mahasiswa:` | `class Mahasiswa:` |
| 5 | Indentasi salah (bukan 4 spasi) | campur tab & spasi | konsisten 4 spasi |
| 6 | Kirim `self` saat memanggil method | `m1.perkenalan(m1)` | `m1.perkenalan()` |
| 7 | Pakai `=` bukan `==` di kondisi | `if tersedia = True:` | `if self.tersedia:` |

**Error yang paling sering muncul malam ini:**

```python
TypeError: pinjam() takes 0 positional arguments but 1 was given
```
→ artinya kamu lupa menulis `self` di parameter method. 🙂

**Class attribute vs instance attribute:**

```python
class Kucing:
    suara = "Meong"     # class attribute — akses: Kucing.suara / self.suara

k = Kucing()
k.nama = "Kitty"        # instance attribute — hanya milik k
```

---

## Slide 20 — Pemanfaatan AI sebagai Coding Assistant

**AI assistant (Copilot, ChatGPT, Claude, Gemini) boleh dipakai — dengan cara yang benar:**

**✅ Gunakan AI untuk:**

- Menjelaskan ulang konsep yang belum paham ("apa itu `self`?")
- Mencari penyebab error (*debugging partner*)
- Mereview gaya kode & saran perbaikan
- Membuat *test case* / contoh pemakaian
- Menjelaskan kode contoh baris per baris

**❌ Jangan gunakan AI untuk:**

- Menuliskan **seluruh** tugas yang seharusnya kamu kerjakan
- Menyalin solusi latihan tanpa memahaminya

**Etika di kelas ini:**

1. Kamu **wajib bisa menjelaskan** setiap baris kode yang kamu kumpulkan
2. Jika memakai AI, **cantumkan** di komentar: `# Bantuan: ChatGPT — penjelasan self`
3. AI = **asisten**, bukan **pengganti**. OOP harus ada di kepala *kamu*, bukan hanya di layar.

> 🧠 Analogi: kalkulator boleh dipakai saat matematika — tapi kamu tetap harus paham operasinya.

---

## Slide 21 — Rangkuman

**Konsep hari ini:**

| Konsep | Satu Kalimat |
| ------ | ------------ |
| **OOP** | Paradigma yang membungkus data + perilaku dalam object |
| **Class** | Blueprint/cetakan object |
| **Object** | Wujud nyata dari class, punya data sendiri |
| **Attribute** | Data yang dimiliki object (instance & class attribute) |
| **Method** | Perilaku/fungsi milik object |
| **Constructor `__init__`** | Method otomatis yang mengisi nilai awal object |
| **`self`** | Referensi object yang sedang memanggil method |

**Alur berpikir OOP:** identifikasi entitas → definisikan class → tentukan attribute & method → instansiasi object → object berinteraksi.

**Pertemuan depan (Minggu 2):** *Class & Object dengan Python* — praktikum penuh membuat class, object, attribute, method, dan constructor dari studi kasus Sistem Informasi.

---

## Slide 22 — Asesmen & Penugasan

**Penilaian pertemuan ini:**

| Komponen | Bentuk | Bobot |
| -------- | ------ | ----- |
| Quiz | 5 soal singkat (konsep class/object/self) | skor quiz minggu ini |
| Latihan terbimbing | Class `Dosen` selesai di kelas | partisipasi |
| Latihan mandiri | `latihan_mandiri_1.py` (class `Produk`) | dikumpulkan |
| Mini challenge | "Perpustakaan Plus" | bonus |

**Deadline:** Latihan mandiri dikumpulkan **sebelum pertemuan ke-2** (Rabu, 23 September 2026, 15:30).

**Cara kumpul:** commit & push ke repo pribadi masing-masing dengan pesan:
`feat: latihan mandiri pertemuan 1 - class Produk`

**Checklist sebelum kumpul:**

- [ ] Kode jalan tanpa error (`python latihan_mandiri_1.py`)
- [ ] Semua method sesuai spesifikasi slide 17
- [ ] Output cocok dengan contoh
- [ ] Sudah coba jelaskan kode ke teman tanpa melihat

---

## Slide 23 — Terima Kasih & Referensi

# Terima Kasih 🙌
### Sampai jumpa di Pertemuan 2 — Class & Object dengan Python

**Referensi belajar:**

- [Python Docs — Classes (Bab 9 Tutorial)](https://docs.python.org/3/tutorial/classes.html)
- [Real Python — Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools — Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)
- [Refactoring Guru — Prinsip OOP](https://refactoring.guru/design-patterns)

**Kontak:** kanal kelas SI-IIIA (discord/LMS kampus) — tanyakan kapan saja!

---

*Dokumen ini bagian dari materi PBO USA-WP2360214. Kode contoh tersedia di `code/pertemuan-01/`.*
