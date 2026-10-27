"""Program utama contoh Sistem Peminjaman Ruang."""

from domain import Peminjaman
from layanan import buat_data_awal


def jalankan_demo():
    """Menjalankan satu skenario pengajuan dan perubahan status."""
    layanan = buat_data_awal()
    pengajuan = Peminjaman("P001", "R001", "Nadia")
    layanan.ajukan(pengajuan)
    layanan.ubah_status("P001", "disetujui")
    hasil = layanan.cari_peminjaman("P001")
    print(f"{hasil.kode}: {hasil.status}")


# === Program utama ===
if __name__ == "__main__":
    jalankan_demo()
