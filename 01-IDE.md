# Panduan Penggunaan

Terdapat beberapa cara untuk _menjalankan_ program Python di project ini. Kalian dapat menggunakan _IDE (Integrated Development Environment)_ seperti:  

- `PyCharm`, 
- `IDLE`, dsb. Selain itu, kalian juga dapat menggunakan code editor seperti
- [VS Code](https://code.visualstudio.com/) 

  - Atau kalian dapat menggunakan website :
    - [jdoodle.com](https://www.jdoodle.com/python-programming-online) 
    - [onecompiler.com/python](https://onecompiler.com/python)
  
untuk menjalankan program Python secara online.

Seluruh kode yang tersedia di repositori ini dapat kalian jalankan secara langsung tanpa perlu melakukan kompilasi terlebih dahulu. Dikarenakan Python bersifat _interpreted_, yang berarti kode dieksekusi langsung oleh _interpreter_, baris per baris.

Sebelum kalian menjalankan program Python, kalian membutuhkan **Python Interpreter** dan IDE/code editor.

**Python** adalah bahasa pemrograman tingkat tinggi yang dikembangkan oleh Guido van Rossum. _Interpreter_ Python berfungsi untuk membaca dan menjalankan kode Python secara langsung, dan sudah _mem-bundle_ _REPL (Read-Eval-Print Loop)_ untuk mencoba kode secara interaktif serta `pip` untuk meng-install _package/library_ Python.

Kalian bisa mengunduh Python di
[www.python.org/downloads/](https://www.python.org/downloads/)

Python yang dipakai saat ini adalah Python 3, yang berarti versi Python yang terus dikembangkan dan paling banyak dipakai saat ini. Jika kalian belum mengetahui apa saja jenis-jenis implementasi Python, berikut penjabaran secara singkat

- `Python 3` = Versi Python yang resmi dikembangkan dan digunakan saat ini. Gunakan versi ini untuk seluruh materi di repositori ini.
- `Python 2` = Versi lama yang sudah tidak didukung lagi (_end-of-life_ sejak tahun 2020). Jangan gunakan versi ini.
- `CPython` = Implementasi _interpreter_ Python standar yang dapat kalian unduh di python.org, ditulis dengan bahasa C.
- `Anaconda` = Distribusi Python yang berisi banyak _package_ untuk data science, sudah termasuk manajer _package_ `conda`.

Untuk menjalankan program, buka terminal pada direktori kode yang ingin kalian jalankan, lalu jalankan perintah berikut di CMD/terminal/bash.

```bash
python NamaFile.py
```

> Pada Windows, kalian juga dapat menggunakan perintah `py NamaFile.py` jika perintah `python` tidak dikenali.

> Pastikan untuk selalu memperhatikan source code dengan benar ketika terjadi error. Dikarenakan kode Python bersifat case-sensitive.

Jika masih bingung bagaimana cara menjalankan program Python, silakan lihat caranya [di sini](https://www.duniailkom.com/tutorial-belajar-python-cara-menjalankan-file-python-dari-cmd/)

# Menggunakan Code Editor Visual Studio Code

Kalian dapat mengunduh VS Code di [code.visualstudio.com](https://code.visualstudio.com/). Setelah itu, pastikan Python telah ter-install di sistem operasi kalian, lalu tambahkan [extension Python di VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python). Extension ini sudah _mem-bundle_ dukungan debugger, IntelliSense, dan linting untuk Python. Silakan ikuti [tutorial instalasi](https://code.visualstudio.com/docs/python/python-tutorial) ini untuk informasi lebih detail.

> Tutorial instalasi di atas berlaku untuk sistem operasi Windows, macOS, dan Linux.

Jika kalian sudah pernah menggunakan atau meng-install VS Code, silakan tambahkan [extension Python di VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python). Pastikan Python telah ter-install di sistem operasi kalian. Silakan ikuti tutorial berikut untuk menambahkan Python di VS Code.

- [Tutorial instalasi Python extension di VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_install-python-and-the-python-extension)
- [Tutorial unduh Python](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)
- [Tutorial lebih detail tentang VS Code untuk Python](https://code.visualstudio.com/docs/python/python-tutorial)

Kalian dapat menjalankan program Python dengan cara klik kanan _file_ dengan ekstensi `.py` setelah itu klik `Run Python File in Terminal`.
