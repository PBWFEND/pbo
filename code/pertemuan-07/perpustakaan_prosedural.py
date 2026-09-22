"""Contoh Pertemuan 7: pengelolaan perpustakaan dengan pendekatan prosedural."""


def buat_buku(judul, penulis):
    # Data disimpan dalam dictionary, terpisah dari fungsi.
    return {"judul": judul, "penulis": penulis, "tersedia": True}


def pinjam_buku(buku):
    if buku["tersedia"]:
        buku["tersedia"] = False
        return True
    return False


def kembalikan_buku(buku):
    buku["tersedia"] = True


def tampilkan_status(buku):
    status = "Tersedia" if buku["tersedia"] else "Dipinjam"
    print(f"{buku['judul']} oleh {buku['penulis']} [{status}]")


def main():
    # Fungsi menerima data sebagai parameter dan mengelolanya secara langsung.
    buku = buat_buku("Pemrograman Python", "Andi")
    tampilkan_status(buku)

    pinjam_buku(buku)
    tampilkan_status(buku)

    kembalikan_buku(buku)
    tampilkan_status(buku)


if __name__ == "__main__":
    main()