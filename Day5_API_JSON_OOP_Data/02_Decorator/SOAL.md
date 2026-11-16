# Latihan 5.2 - Using Decorators

**Kasus:** Manajer ingin tahu berapa lama fungsi berjalan dan siapa yang memanggilnya,
tanpa mengubah isi fungsi.

1. Pelajari decorator `@catat_waktu` yang sudah jadi.
2. Lengkapi `@log_aktivitas` (tulis nama fungsi dan argumen ke `aktivitas.log`).
3. Lengkapi `@hanya_admin` (tolak bila `peran != "admin"`).
4. Pasang ketiganya pada `hapus_transaksi()`.

**Hubungan dengan OOP:** `@property` (Day 4), `@classmethod`, `@staticmethod`, `@dataclass`,
dan `@abstractmethod` (latihan berikutnya) juga decorator.
