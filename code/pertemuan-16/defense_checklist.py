"""Contoh checklist kesiapan UAS / Project Defense."""


class ChecklistDefense:
    """Menyimpan dan menampilkan status kesiapan project."""

    def __init__(self, nama_project):
        if not nama_project:
            raise ValueError("Nama project wajib diisi")
        self.nama_project = nama_project
        self.__items = []

    def tambah_item(self, deskripsi, selesai=False):
        if not deskripsi:
            raise ValueError("Deskripsi checklist wajib diisi")
        self.__items.append({"deskripsi": deskripsi, "selesai": selesai})

    def tandai_selesai(self, nomor):
        if nomor < 1 or nomor > len(self.__items):
            return False
        self.__items[nomor - 1]["selesai"] = True
        return True

    def semua_selesai(self):
        return bool(self.__items) and all(item["selesai"] for item in self.__items)

    def tampilkan(self):
        for nomor, item in enumerate(self.__items, start=1):
            status = "selesai" if item["selesai"] else "belum selesai"
            print(f"{nomor}. [{status}] {item['deskripsi']}")


# === Program utama ===
if __name__ == "__main__":
    checklist = ChecklistDefense("Sistem Peminjaman Ruang")
    checklist.tambah_item("Source code dapat dijalankan")
    checklist.tambah_item("Test utama sudah dijalankan")
    checklist.tambah_item("Demo dan README sudah disiapkan")

    checklist.tandai_selesai(1)
    checklist.tandai_selesai(2)
    checklist.tampilkan()
    print("Semua selesai:", checklist.semua_selesai())
