# Solusi 4.6 - To-Do List OOP
import json
from pathlib import Path

FILE = Path(__file__).parent / "todo.json"


class Tugas:
    def __init__(self, judul, selesai=False):
        self.judul = judul
        self.selesai = selesai

    def tandai_selesai(self):
        self.selesai = True

    def ke_dict(self):
        return {"judul": self.judul, "selesai": self.selesai}

    @classmethod
    def dari_dict(cls, data):
        return cls(data["judul"], data["selesai"])

    def __str__(self):
        return f"[{'x' if self.selesai else ' '}] {self.judul}"


class TodoList:
    def __init__(self, file):
        self.file = Path(file)
        self.tugas = []
        self.muat()

    def muat(self):
        if self.file.exists():
            with open(self.file, encoding="utf-8") as f:
                self.tugas = [Tugas.dari_dict(d) for d in json.load(f)]

    def simpan(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump([t.ke_dict() for t in self.tugas], f, indent=2, ensure_ascii=False)

    def _ambil(self, nomor):
        if not 1 <= nomor <= len(self.tugas):
            raise IndexError(f"Nomor {nomor} tidak ada")
        return self.tugas[nomor - 1]

    def tambah(self, judul):
        judul = judul.strip()
        if judul:
            self.tugas.append(Tugas(judul))

    def tandai(self, nomor):
        self._ambil(nomor).tandai_selesai()

    def hapus(self, nomor):
        self.tugas.remove(self._ambil(nomor))

    def tampilkan(self):
        if not self.tugas:
            print("  (belum ada tugas)")
        for i, t in enumerate(self.tugas, start=1):
            print(f"  {i}. {t}")

    def __len__(self):
        return len(self.tugas)


def main():
    todo = TodoList(FILE)
    print(f"Memuat {len(todo)} tugas dari {FILE.name}")
    while True:
        print("\n1 Lihat | 2 Tambah | 3 Selesai | 4 Hapus | 5 Simpan & keluar")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                todo.tampilkan()
            elif pilihan == "2":
                todo.tambah(input("  Judul tugas: "))
            elif pilihan in ("3", "4"):
                nomor = int(input("  Nomor: "))
                todo.tandai(nomor) if pilihan == "3" else todo.hapus(nomor)
            elif pilihan == "5":
                todo.simpan()
                print(f"Tersimpan {len(todo)} tugas.")
                break
            else:
                print("  Pilihan tidak dikenal.")
        except (ValueError, IndexError) as e:
            print("  Input tidak valid:", e)
        todo.simpan()


if __name__ == "__main__":
    main()
