# Quiz Pertemuan 6 — Abstraction dan Interface pada Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 6 | **Tanggal:** 21 Oktober 2026 | **CPMK:** CPMK114

## Petunjuk Pengerjaan

- Waktu: 15 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu tanpa catatan, kecuali ada arahan dosen
- Soal 3–5 berbasis kode Python

## Soal 1 — Konsep Abstraction

Jelaskan pengertian abstraction dalam OOP dan berikan satu contoh antarmuka yang menyembunyikan detail implementasi.

## Soal 2 — Abstract Class dan Abstract Method

Jelaskan perbedaan abstract class dan abstract method. Mengapa abstract class tidak dapat diinstansiasi langsung?

## Soal 3 — Prediksi Output

```python
from abc import ABC, abstractmethod

class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def tampilkan_peran(self):
        pass

class Mahasiswa(Pengguna):
    def tampilkan_peran(self):
        return "Mahasiswa"

print(Mahasiswa("Budi").tampilkan_peran())
```

Tuliskan output dari program tersebut dan jelaskan peran `@abstractmethod`.

## Soal 4 — Error pada Abstract Class

```python
from abc import ABC, abstractmethod

class Pengguna(ABC):
    @abstractmethod
    def tampilkan_peran(self):
        pass

class Mahasiswa(Pengguna):
    pass

mahasiswa = Mahasiswa()
```

Apa yang terjadi ketika `Mahasiswa()` dijalankan? Jelaskan alasan teknisnya.

## Soal 5 — Merancang Abstract Class

Tuliskan abstract class `Transaksi` dengan abstract method `proses()`, lalu buat subclass `TransaksiTunai` yang mengimplementasikan method tersebut. Jelaskan manfaat kontrak perilaku pada rancangan tersebut.