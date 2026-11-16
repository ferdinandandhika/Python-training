# Solusi 1.3 - String Lab
nama = "   bUDi   santoso "
email = "  BUDI.Santoso@Mail.COM "
hp = "081234567890"
kode = "ORD-2026-BDG-0042"
total = 1250000
diskon = 0.15
kartu = "4111222233334444"

nama_rapi = " ".join(nama.split()).title()
email_rapi = email.strip().lower()
username = email_rapi.split("@")[0]
hp_rapi = f"{hp[0:4]}-{hp[4:8]}-{hp[8:]}"
_, tahun, kota, nomor = kode.split("-")
total_rp = "Rp " + f"{total:,}".replace(",", ".")
diskon_persen = f"{diskon:.0%}"
kartu_sensor = "*" * (len(kartu) - 4) + kartu[-4:]

print("1. Nama      :", nama_rapi)
print("2. Email     :", email_rapi)
print("3. Username  :", username)
print("4. HP        :", hp_rapi)
print(f"5. Kode      : tahun={tahun}, kota={kota}, nomor={int(nomor)}")
print("6. Total     :", total_rp)
print("7. Diskon    :", diskon_persen)
print("8. Kartu     :", kartu_sensor)
