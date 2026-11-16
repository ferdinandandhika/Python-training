# Latihan 4.6 - To-Do List OOP
import json
from pathlib import Path

FILE = Path(__file__).parent / "todo.json"


class Tugas:
    def __init__(self, judul, selesai=False):
        self.judul = judul
        self.selesai = selesai

    def tandai_selesai(self):
        pass  # TODO 1

    def ke_dict(self):
        pass  # TODO 2: return {"judul": ..., "selesai": ...}

    @classmethod
    def dari_dict(cls, data):
        pass  # TODO 3: return cls(data["judul"], data["selesai"])

    def __str__(self):
        return f"[{'x' if self.selesai else ' '}] {self.judul}"


class TodoList:
    def __init__(self, file):
        self.file = Path(file)
        self.tugas = []
        self.muat()

    def muat(self):
        pass  # TODO 4: bila file ada, json.load lalu ubah tiap dict menjadi Tugas

    def simpan(self):
        pass  # TODO 5: json.dump list hasil ke_dict()

    def tambah(self, judul):
        pass  # TODO 6

    def tandai(self, nomor):
        pass  # TODO 7: nomor mulai dari 1; raise IndexError bila salah

    def hapus(self, nomor):
        pass  # TODO 8

    def tampilkan(self):
        pass  # TODO 9

    def __len__(self):
        return len(self.tugas)


# TODO 10: menu utama dengan while loop
