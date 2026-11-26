# Solusi 4.5 - File Lab
import csv  # Impor alat Python untuk menulis data berbentuk tabel CSV.
import json  # Impor alat untuk menyimpan ringkasan dalam format JSON.
from pathlib import Path  # Impor Path agar lokasi dan nama berkas dapat dibentuk lintas sistem operasi.

FOLDER = Path(__file__).parent  # Tentukan folder tempat skrip ini berada agar lokasi berkas relatif terhadap skrip.
SUMBER = FOLDER / "data" / "penjualan_harian.txt"  # Bentuk alamat berkas sumber penjualan di subfolder data.
OUTPUT = FOLDER / "output"  # Tentukan folder tujuan untuk berkas hasil olahan.
OUTPUT.mkdir(exist_ok=True)  # Buat folder keluaran bila belum ada; folder yang sudah ada tidak dianggap sebagai kesalahan.

rekap = {}  # Siapkan kamus kosong untuk mengumpulkan jumlah dan omzet setiap menu.
try:  # Jalankan pembacaan dengan penanganan khusus jika berkas sumber tidak ditemukan.
    with open(SUMBER, encoding="utf-8") as f:  # Buka berkas sebagai teks UTF-8 dan tutup otomatis setelah blok selesai diproses.
        for baris in f:  # Baca setiap baris penjualan satu per satu agar seluruh transaksi dapat direkap.
            baris = baris.strip()  # Hilangkan spasi serta karakter baris baru di kedua ujung baris.
            if not baris or baris.startswith("#"):  # Abaikan baris kosong dan baris komentar yang diawali tanda pagar.
                continue  # Lewati baris tersebut dan lanjutkan membaca baris berikutnya.
            tanggal, menu, qty, harga = baris.split(";")  # Pisahkan empat kolom data menggunakan titik koma sebagai pembatas.
            data = rekap.setdefault(menu, {"qty": 0, "total": 0})  # Ambil rekap menu atau buat nilai awal untuk menu yang baru ditemui.
            data["qty"] += int(qty)  # Tambahkan jumlah terjual setelah mengubah teks jumlah menjadi bilangan bulat.
            data["total"] += int(qty) * int(harga)  # Tambahkan omzet baris ini dengan mengalikan jumlah dan harga satuan.
except FileNotFoundError:  # Tangani kasus ketika berkas sumber penjualan tidak tersedia di lokasi yang diharapkan.
    print(f"File {SUMBER} tidak ditemukan.")  # Jelaskan kepada pengguna berkas mana yang tidak ditemukan.
    raise SystemExit(1)  # Hentikan program dengan kode gagal karena rekap tidak dapat dibuat tanpa berkas sumber.

with open(OUTPUT / "rekap_menu.csv", "w", newline="", encoding="utf-8") as f:  # Buka atau buat berkas CSV; newline kosong mencegah baris kosong tambahan pada beberapa sistem.
    writer = csv.writer(f)  # Buat penulis CSV yang mengubah daftar nilai menjadi baris tabel.
    writer.writerow(["Menu", "Qty", "Total"])  # Tulis nama kolom sebagai baris pertama agar isi laporan mudah dipahami.
    for menu, data in sorted(rekap.items(), key=lambda x: x[1]["total"], reverse=True):  # Urutkan menu dari omzet terbesar ke terkecil sebelum ditulis.
        writer.writerow([menu, data["qty"], data["total"]])  # Tulis nama menu, kuantitas terjual, dan omzet ke satu baris CSV.

ringkasan = {
    "total_omzet": sum(d["total"] for d in rekap.values()),  # Jumlahkan omzet seluruh menu untuk memperoleh omzet keseluruhan.
    "total_cup": sum(d["qty"] for d in rekap.values()),  # Jumlahkan kuantitas seluruh menu untuk menghitung total cup terjual.
    "menu_terlaris": max(rekap, key=lambda m: rekap[m]["qty"]),  # Pilih nama menu dengan kuantitas terjual paling tinggi.
}  # Simpan seluruh nilai ringkasan dalam satu kamus agar mudah ditulis sebagai JSON.
with open(OUTPUT / "ringkasan.json", "w", encoding="utf-8") as f:  # Buka atau buat berkas JSON dengan UTF-8 supaya karakter non-ASCII tersimpan dengan benar.
    json.dump(ringkasan, f, indent=2, ensure_ascii=False)  # Tulis kamus ringkasan dengan indentasi dan pertahankan karakter Unicode.
for menu, data in rekap.items():  # Ulangi seluruh pasangan menu dan data untuk menampilkan rekap ringkas di terminal.
    print(f"{menu:<16} {data['qty']:>3}  Rp {data['total']:>9,}")  # Tampilkan menu, jumlah, dan omzet dengan lebar kolom yang rapi.
print(json.dumps(ringkasan, indent=2))  # Tampilkan ringkasan sebagai JSON berindentasi agar hasil akhir mudah dibaca.
