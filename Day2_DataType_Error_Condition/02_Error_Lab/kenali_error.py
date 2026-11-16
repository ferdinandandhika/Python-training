# Bagian A - Tebak nama error sebelum melihat hasilnya.
contoh = ["int('abc')", "10 / 0", "'umur: ' + 25", "{'nama': 'Andi'}['kota']",
          "[1, 2, 3][10]", "open('tidak_ada.txt')", "print(variabel_belum_dibuat)"]
for kode in contoh:
    try:
        eval(kode)
    except Exception as e:
        print(f"{kode:<35} -> {type(e).__name__}: {e}")
