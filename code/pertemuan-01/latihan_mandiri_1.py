# Latihan Mandiri Pertemuan 1
#
# Buat class Produk sesuai spesifikasi bagian Latihan Mandiri:
#   1. Attribute: nama, harga, stok
#   2. Constructor: mengisi ketiga attribute dari parameter
#   3. Method info(): cetak "{nama} - Rp{harga} (stok: {stok})"
#   4. Method jual(jumlah): kurangi stok; tolak jika stok < jumlah
#   5. Method restock(jumlah): tambah stok
#   6. Bonus: class attribute total_produk
#
# Kerjakan di file ini, lalu jalankan: python latihan_mandiri_1.py


class Produk:
    pass  # TODO: ganti dengan implementasi lengkap


# === Program utama (jangan diubah) ===
if __name__ == "__main__":
    p = Produk("Laptop", 8000000, 5)
    p.info()
    p.jual(2)
    p.info()
    p.jual(10)
    p.restock(10)
    p.info()

# Expected output:
# Laptop - Rp8000000 (stok: 5)
# Laptop - Rp8000000 (stok: 3)
# Stok tidak cukup!
# Laptop - Rp8000000 (stok: 13)
