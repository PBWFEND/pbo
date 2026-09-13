# Quiz Pertemuan 3 — Encapsulation pada Python

**Mata Kuliah:** USA-WP2360214 — Pemrograman Berorientasi Objek  
**Pertemuan:** 3 | **Tanggal:** 30 September 2026 | **CPMK:** CPMK114

## Petunjuk Pengerjaan

- Waktu: 15 menit
- Jumlah: 5 soal, masing-masing 20 poin
- Dikerjakan secara individu tanpa catatan, kecuali ada arahan dosen
- Soal 3–5 berbasis kode Python

## Soal 1 — Tujuan Encapsulation

Jelaskan tujuan encapsulation dalam OOP. Mengapa data tertentu perlu dikendalikan melalui method atau property?

## Soal 2 — Private Attribute dan Property

Jelaskan fungsi nama attribute dengan awalan `__` dan peran decorator `@property` serta `@<nama>.setter`.

## Soal 3 — Prediksi Output

```python
class Mahasiswa:
    def __init__(self, nama, sks):
        self.nama = nama
        self.__sks = sks

    @property
    def sks(self):
        return self.__sks

mhs = Mahasiswa("Jhon Doe", 3)
print(mhs.sks)
```

Tuliskan output dan jelaskan bagaimana property membaca private attribute.

## Soal 4 — Validasi Setter

Lengkapi setter berikut agar nilai saldo negatif menghasilkan `ValueError`.

```python
class Rekening:
    def __init__(self, saldo):
        self.__saldo = 0
        self.saldo = saldo

    @property
    def saldo(self):
        pass

    @saldo.setter
    def saldo(self, nilai):
        pass
```

## Soal 5 — Analisis Access Control

Apa risiko jika attribute `saldo` dapat diubah langsung tanpa validasi? Berikan satu contoh aturan validasi yang sesuai untuk rekening mahasiswa.
