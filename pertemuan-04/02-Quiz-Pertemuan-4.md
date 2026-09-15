# Quiz Pertemuan 4 — Inheritance pada Python

## Petunjuk

Jawablah setiap pertanyaan secara ringkas dan berikan alasan teknis jika diminta.

## Soal

1. Jelaskan perbedaan superclass dan subclass.
2. Apa fungsi `super().__init__()` pada constructor subclass?
3. Jelaskan overriding dan berikan contoh penerapannya.
4. Mengapa inheritance sebaiknya digunakan ketika terdapat hubungan **is-a**?
5. Perhatikan kode berikut:

   ```python
   class Pengguna:
       def tampilkan_peran(self):
           return "Pengguna"

   class Mahasiswa(Pengguna):
       def tampilkan_peran(self):
           return "Mahasiswa"
   ```

   Apa output dari `Mahasiswa().tampilkan_peran()` dan konsep OOP apa yang ditunjukkan?
