# Solusi 4.6 - To-Do List OOP
import json  # Impor fungsi serialisasi untuk membaca dan menulis daftar tugas sebagai JSON.
from pathlib import Path  # Impor Path untuk membentuk lokasi berkas secara aman dan mudah dibaca.

FILE = Path(__file__).parent / "todo.json"  # Tetapkan berkas penyimpanan todo di folder yang sama dengan skrip ini.


class Tugas:
    def __init__(self, judul, selesai=False):  # Buat tugas dengan judul dan status selesai yang secara default masih False.
        self.judul = judul  # Simpan teks judul sebagai data milik masing-masing objek tugas.
        self.selesai = selesai  # Simpan status Boolean untuk menandai apakah tugas sudah selesai.

    def tandai_selesai(self):  # Sediakan operasi objek untuk mengubah status tugas menjadi selesai.
        self.selesai = True  # Tandai tugas ini selesai dengan menyimpan nilai Boolean True.

    def ke_dict(self):  # Ubah objek tugas menjadi bentuk kamus yang dapat diserialisasi sebagai JSON.
        return {"judul": self.judul, "selesai": self.selesai}  # Kembalikan data sederhana agar kedua atribut tersimpan.

    @classmethod  # Tandai metode berikut sebagai metode kelas yang menerima kelas melalui parameter cls.
    def dari_dict(cls, data):  # Sediakan cara untuk membangun objek Tugas dari satu kamus hasil pembacaan JSON.
        return cls(data["judul"], data["selesai"])  # Buat instance kelas ini dengan judul dan status yang tersimpan di kamus.

    def __str__(self):  # Tentukan representasi teks yang dipakai saat objek tugas ditampilkan sebagai string.
        return f"[{'x' if self.selesai else ' '}] {self.judul}"  # Tampilkan x untuk tugas selesai, kotak kosong untuk tugas belum selesai, lalu judulnya.


class TodoList:
    def __init__(self, file):  # Siapkan daftar tugas dengan lokasi berkas penyimpanan yang diberikan pemanggil.
        self.file = Path(file)  # Simpan lokasi berkas sebagai objek Path agar operasi berkas lebih mudah dilakukan.
        self.tugas = []  # Mulai dengan daftar kosong yang nantinya berisi objek Tugas.
        self.muat()  # Muat isi berkas saat daftar dibuat agar data sebelumnya dapat digunakan kembali.

    def muat(self):  # Baca tugas dari berkas bila berkas penyimpanan sudah tersedia.
        if self.file.exists():  # Periksa keberadaan berkas supaya program tidak mencoba membukanya jika belum dibuat.
            with open(self.file, encoding="utf-8") as f:  # Buka berkas UTF-8 dalam konteks agar otomatis ditutup setelah selesai dibaca.
                self.tugas = [Tugas.dari_dict(d) for d in json.load(f)]  # Baca daftar JSON lalu ubah setiap kamus menjadi objek Tugas.

    def simpan(self):  # Simpan daftar tugas saat ini agar perubahan tetap ada setelah program ditutup.
        with open(self.file, "w", encoding="utf-8") as f:  # Buka berkas dalam mode tulis UTF-8; isi lama diganti dengan keadaan daftar terbaru.
            json.dump([t.ke_dict() for t in self.tugas], f, indent=2, ensure_ascii=False)  # Ubah tiap tugas menjadi kamus lalu tulis sebagai JSON yang rapi.

    def _ambil(self, nomor):  # Sediakan fungsi internal untuk mengambil tugas berdasarkan nomor yang dimulai dari satu.
        if not 1 <= nomor <= len(self.tugas):  # Pastikan nomor berada di rentang tugas yang tersedia sebelum mengakses daftar.
            raise IndexError(f"Nomor {nomor} tidak ada")  # Beri tahu pemanggil bahwa nomor di luar rentang tidak valid.
        return self.tugas[nomor - 1]  # Ubah nomor pengguna menjadi indeks daftar yang dimulai dari nol lalu kembalikan tugasnya.

    def tambah(self, judul):  # Tambahkan tugas baru jika judul yang diberikan berisi teks.
        judul = judul.strip()  # Buang spasi di awal dan akhir supaya judul kosong berisi spasi tidak dianggap valid.
        if judul:  # Periksa bahwa setelah dibersihkan, judul masih memiliki isi.
            self.tugas.append(Tugas(judul))  # Buat objek Tugas baru dan tambahkan ke akhir daftar.

    def tandai(self, nomor):  # Tandai tugas yang dipilih pengguna sebagai selesai.
        self._ambil(nomor).tandai_selesai()  # Ambil tugas tervalidasi lalu panggil perilaku untuk mengubah statusnya.

    def hapus(self, nomor):  # Hapus tugas yang dipilih berdasarkan nomor pengguna.
        self.tugas.remove(self._ambil(nomor))  # Ambil objek pada nomor tersebut lalu keluarkan objek itu dari daftar.

    def tampilkan(self):  # Tampilkan daftar tugas dalam format bernomor.
        if not self.tugas:  # Periksa apakah daftar masih kosong sebelum mencetak setiap tugas.
            print("  (belum ada tugas)")  # Beri umpan balik ketika pengguna belum memiliki tugas.
        for i, t in enumerate(self.tugas, start=1):  # Pasangkan setiap tugas dengan nomor tampilan yang dimulai dari satu.
            print(f"  {i}. {t}")  # Cetak nomor dan representasi teks tugas.

    def __len__(self):  # Definisikan cara menghitung panjang objek TodoList dengan fungsi len().
        return len(self.tugas)  # Teruskan jumlah elemen pada daftar tugas sebagai panjang TodoList.


def main():  # Jadikan fungsi ini titik kumpul alur aplikasi agar definisi kelas terpisah dari interaksi pengguna.
    todo = TodoList(FILE)  # Buat daftar tugas yang memuat data dari berkas penyimpanan yang sudah ditetapkan.
    print(f"Memuat {len(todo)} tugas dari {FILE.name}")  # Beri tahu pengguna jumlah tugas yang berhasil dimuat dan nama berkasnya.
    while True:  # Tampilkan menu berulang kali sampai pengguna memilih untuk menyimpan dan keluar.
        print("\n1 Lihat | 2 Tambah | 3 Selesai | 4 Hapus | 5 Simpan & keluar")  # Tampilkan pilihan operasi yang tersedia.
        pilihan = input("Pilih: ").strip()  # Baca pilihan menu sebagai teks dan hapus spasi di ujungnya.
        try:  # Tangani kesalahan masukan atau nomor tugas agar aplikasi tetap dapat kembali ke menu.
            if pilihan == "1":  # Periksa apakah pengguna ingin melihat seluruh tugas.
                todo.tampilkan()  # Jalankan metode yang mencetak daftar tugas.
            elif pilihan == "2":  # Periksa apakah pengguna ingin menambahkan tugas baru.
                todo.tambah(input("  Judul tugas: "))  # Minta judul lalu serahkan ke metode tambah untuk dibersihkan dan disimpan.
            elif pilihan in ("3", "4"):  # Tangani pilihan menandai selesai dan menghapus tugas dengan alur meminta nomor yang sama.
                nomor = int(input("  Nomor: "))  # Baca nomor tugas dan ubah menjadi bilangan bulat agar dapat divalidasi.
                todo.tandai(nomor) if pilihan == "3" else todo.hapus(nomor)  # Pilih aksi tandai atau hapus berdasarkan pilihan menu.
            elif pilihan == "5":  # Periksa apakah pengguna meminta penyimpanan terakhir dan keluar dari aplikasi.
                todo.simpan()  # Simpan semua perubahan sebelum program dihentikan.
                print(f"Tersimpan {len(todo)} tugas.")  # Konfirmasikan jumlah tugas yang kini tersimpan.
                break  # Hentikan perulangan menu karena pengguna sudah memilih keluar.
            else:  # Jalankan cabang ini jika masukan bukan salah satu pilihan menu yang dikenali.
                print("  Pilihan tidak dikenal.")  # Beri tahu pengguna bahwa pilihan harus mengikuti menu.
        except (ValueError, IndexError) as e:  # Tangkap masukan angka yang gagal dikonversi atau nomor tugas di luar rentang.
            print("  Input tidak valid:", e)  # Tampilkan penjelasan kesalahan supaya pengguna tahu apa yang perlu diperbaiki.
        todo.simpan()  # Simpan perubahan setelah setiap putaran menu agar perubahan tidak hilang jika program berhenti.


if __name__ == "__main__":  # Pastikan menu hanya dijalankan saat berkas ini dijalankan langsung, bukan saat diimpor.
    main()  # Mulai aplikasi interaktif ketika syarat eksekusi langsung terpenuhi.
