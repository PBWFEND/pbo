# Soal UAS Pertemuan 16 — Project Defense Aplikasi OOP

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Kode:** USA-WP2360214  
**Pertemuan:** 16  
**CPMK:** CPMK116  
**Bentuk:** Project Defense, demo aplikasi, presentasi, dan tanya jawab  
**Bobot:** 15%  
**Waktu demo:** Maksimal 10 menit per kelompok, dilanjutkan tanya jawab

> **Penting:** Dokumen ini adalah instruksi UAS. Setiap kelompok wajib membaca seluruh bagian sebelum menyiapkan aplikasi, dokumen, dan presentasi.

---

## A. Tema UAS

Buat dan pertahankan sebuah aplikasi sederhana berbasis **Object-Oriented Programming dengan Python 3** untuk menyelesaikan masalah pada bidang Sistem Informasi.

Contoh tema:

- Sistem Peminjaman Ruang
- Sistem Perpustakaan
- Sistem Pengelolaan Inventaris
- Sistem Pengajuan Surat
- Sistem Pengelolaan Jadwal Kuliah
- Sistem Pengelolaan Layanan Mahasiswa

Kelompok dapat memilih tema lain dengan persetujuan dosen. Tema harus memiliki data atau object yang dapat dikelola, minimal melalui operasi Create, Read, Update, dan Delete.

---

## B. Ketentuan Kelompok

1. Project dikerjakan secara berkelompok sesuai arahan dosen.
2. Setiap anggota wajib memiliki kontribusi yang dapat dijelaskan.
3. Nama anggota dan pembagian tugas harus dicantumkan dalam README.
4. Setiap anggota dapat dipanggil untuk menjelaskan bagian project yang dikerjakan anggota lain.
5. Source code yang digunakan saat demo harus sama dengan source code yang dikumpulkan.
6. Penggunaan AI diperbolehkan sebagai coding assistant, tetapi anggota wajib memahami dan dapat menjelaskan seluruh kode yang dipresentasikan.

---

## C. Fitur Wajib

Aplikasi minimal harus memiliki komponen berikut:

### 1. Class dan Object

- minimal tiga class domain atau layanan;
- attribute dan method yang memiliki tanggung jawab jelas;
- object yang saling berinteraksi melalui method;
- nama class, function, dan variable mengikuti konvensi Python.

### 2. Pengelolaan Data

- operasi Create untuk menambah data;
- operasi Read untuk menampilkan atau mencari data;
- operasi Update untuk mengubah data;
- operasi Delete untuk menghapus data dengan aturan yang sesuai.

### 3. Validation dan Exception Handling

- minimal tiga aturan validation;
- minimal satu kondisi input tidak valid;
- minimal satu kondisi aturan bisnis yang ditolak;
- exception ditangani secara spesifik;
- pesan kesalahan membantu pengguna memahami penyebab penolakan.

### 4. Testing

- minimal enam test case;
- minimal empat test otomatis menggunakan `unittest`;
- test mencakup jalur berhasil dan jalur gagal;
- hasil test dapat ditunjukkan saat defense.

### 5. Dokumentasi

README wajib memuat:

- nama dan tujuan aplikasi;
- masalah dan pengguna sasaran;
- anggota kelompok dan pembagian tugas;
- kebutuhan Python;
- cara menjalankan aplikasi;
- cara menjalankan test;
- daftar fitur;
- struktur class atau module;
- contoh alur penggunaan;
- batasan aplikasi;
- referensi dan penggunaan AI jika ada.

---

## D. Deliverables yang Dikumpulkan

Kumpulkan satu folder atau repository project yang berisi:

```text
project-kelompok/
├── README.md
├── aplikasi.py atau package aplikasi/
├── tests/
│   └── test_*.py
├── docs/
│   ├── diagram-class.png atau diagram-class.md
│   └── test-case.md
└── requirements.txt jika memang menggunakan dependency tambahan
```

Jika project tidak menggunakan folder tertentu, struktur dapat disesuaikan. Nama dan lokasi file harus dijelaskan dalam README.

File yang wajib tersedia:

1. source code aplikasi;
2. test otomatis;
3. README;
4. diagram class atau penjelasan struktur class;
5. tabel test case;
6. catatan pembagian kontribusi.

---

## E. Tugas 1 — Analisis Kebutuhan

Tuliskan dalam README atau dokumen project:

1. masalah yang ingin diselesaikan;
2. pengguna sasaran;
3. minimal tiga kebutuhan fungsional;
4. minimal dua aturan atau batasan bisnis;
5. batasan aplikasi yang belum ditangani.

Contoh kebutuhan fungsional:

- pengguna dapat menambahkan data ruang;
- pengguna dapat mencari pengajuan berdasarkan identifier;
- pengguna dapat memperbarui status pengajuan;
- sistem menolak penghapusan ruang yang masih digunakan.

---

## F. Tugas 2 — Perancangan OOP

Buat diagram class atau dokumen desain yang menjelaskan:

1. nama dan tanggung jawab setiap class;
2. attribute utama setiap class;
3. method utama setiap class;
4. relasi antar-class;
5. arah interaksi object;
6. alasan teknis pembagian tanggung jawab.

Diagram tidak dinilai berdasarkan hiasan visual, tetapi berdasarkan kesesuaian dengan source code yang dipresentasikan.

---

## G. Tugas 3 — Implementasi Aplikasi

Implementasikan aplikasi dengan ketentuan:

1. gunakan Python 3;
2. gunakan class dan object sebagai struktur utama;
3. terapkan encapsulation atau validation pada data yang sesuai;
4. gunakan service atau class pengelola untuk operasi yang melibatkan beberapa object;
5. pisahkan kode aplikasi dan kode test;
6. sediakan program utama atau instruksi eksekusi yang jelas;
7. gunakan standard library Python kecuali dependency tambahan disetujui atau dijelaskan.

---

## H. Tugas 4 — Test Case dan Testing

Buat tabel minimal enam test case dengan format berikut:

| ID | Skenario | Kondisi awal | Input | Expected result | Actual result | Status |
| -- | -------- | ------------ | ----- | --------------- | ------------- | ------ |
| TC-01 | Data valid dibuat | Collection kosong | Data valid | Data tersimpan | Diisi setelah test | Lulus/Gagal |

Minimal test case harus mencakup:

- satu Create berhasil;
- satu Read atau pencarian;
- satu Update berhasil;
- satu Delete atau penolakan Delete;
- satu validation gagal;
- satu exception atau aturan bisnis gagal.

Jalankan test dengan perintah yang ditulis dalam README, misalnya:

```bash
python3 -m unittest discover -s tests -v
```

---

## I. Tugas 5 — Dokumentasi dan Presentasi

Buat presentasi singkat dengan urutan berikut:

1. judul project dan anggota;
2. masalah dan pengguna sasaran;
3. fitur utama;
4. diagram class dan pembagian tanggung jawab;
5. demo satu alur utama;
6. demo satu kondisi gagal;
7. hasil testing;
8. batasan dan rencana pengembangan;
9. pembagian kontribusi.

Setiap anggota harus berbicara atau menjawab bagian yang ditentukan oleh dosen.

---

## J. Alur Pelaksanaan Defense

Pada saat UAS, urutan kegiatan adalah:

1. kelompok menyiapkan project dan data demo;
2. kelompok menyampaikan tujuan dan fitur utama;
3. kelompok menjalankan demo aplikasi;
4. kelompok menunjukkan satu kondisi gagal yang ditangani;
5. kelompok menunjukkan hasil test;
6. dosen mengajukan pertanyaan teknis;
7. setiap anggota menjelaskan kontribusi dan keputusan desain;
8. kelompok menyampaikan batasan aplikasi.

Demo harus dapat diulang. Siapkan data awal dan langkah pemulihan jika terjadi kesalahan input.

---

## K. Persiapan Tanya Jawab

Siapkan penjelasan berdasarkan project Anda untuk aspek berikut:

- alasan pemisahan class dan tanggung jawab setiap class;
- alasan pemilihan `list` atau `dict` untuk collection;
- lokasi validation, exception handling, dan aturan bisnis;
- test yang membuktikan perubahan state object;
- keterbatasan aplikasi dan rencana pengembangan;
- kontribusi pribadi serta cara menguji bagian yang dikerjakan.

Gunakan [Template Penyelesaian UAS Pertemuan 16](./03-Template-Penyelesaian-UAS-Pertemuan-16.md) untuk menuliskan jawaban, bukti testing, struktur project, skenario demo, dan pembagian kontribusi.

---

## L. Rubrik Penilaian

| Komponen | Bobot | Kriteria |
| -------- | :---: | -------- |
| Fungsionalitas aplikasi | 30% | Fitur utama dapat dijalankan dan sesuai kebutuhan |
| Penerapan OOP | 20% | Class, object, attribute, method, dan relasi memiliki tanggung jawab jelas |
| Testing dan evaluasi | 15% | Test case lengkap, test otomatis tersedia, dan hasil dapat ditunjukkan |
| Dokumentasi | 10% | README, struktur project, instruksi, dan batasan jelas |
| Presentasi dan demo | 15% | Demo teratur, dapat diulang, dan menunjukkan fitur serta kondisi gagal |
| Tanya jawab | 10% | Jawaban sesuai source code dan alasan teknis dapat dipertanggungjawabkan |
| **Total** | **100%** | |

Penilaian individu dapat disesuaikan berdasarkan pemahaman kontribusi dan kemampuan menjawab pertanyaan.

---

## M. Checklist Sebelum Pengumpulan

- [ ] Nama anggota dan pembagian tugas sudah ditulis.
- [ ] Source code dapat dijalankan dari instruksi README.
- [ ] Minimal tiga class tersedia.
- [ ] CRUD atau pengelolaan data tersedia.
- [ ] Minimal tiga validation rule tersedia.
- [ ] Exception handling digunakan secara spesifik.
- [ ] Minimal enam test case ditulis.
- [ ] Minimal empat test otomatis lulus.
- [ ] Diagram class sesuai dengan source code.
- [ ] README memuat cara menjalankan aplikasi dan test.
- [ ] Demo fitur berhasil dan kondisi gagal sudah dilatih.
- [ ] Setiap anggota memahami project dan kontribusinya.

## N. Batasan Akademik

Project harus merupakan hasil kerja kelompok yang dapat dijelaskan oleh seluruh anggota. Bantuan AI boleh dicatat sebagai bagian dari proses, tetapi tidak menggantikan pemahaman, pengujian, dan tanggung jawab mahasiswa terhadap source code.
