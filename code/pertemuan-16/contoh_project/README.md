# Contoh Project — Sistem Peminjaman Ruang

Contoh project ini menunjukkan pemisahan class domain, service, program utama, dan unit test.

## Struktur

```text
contoh_project/
├── README.md
├── aplikasi.py
├── domain.py
├── layanan.py
└── tests/
    └── test_peminjaman.py
```

## Menjalankan aplikasi

Dari folder `contoh_project/`:

```bash
python3 aplikasi.py
```

## Menjalankan test

Dari folder `contoh_project/`:

```bash
python3 -m unittest discover -s tests -v
```
