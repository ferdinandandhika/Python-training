# Solusi TokoKu Day 2 - Validasi dan Diskon

nama = input("Nama pelanggan : ").strip().title()
menu = input("Nama barang    : ").strip().title()
harga_teks = input("Harga satuan   : ")
jumlah_teks = input("Jumlah         : ")

try:
    harga = int(harga_teks)
    jumlah = int(jumlah_teks)
except ValueError:
    print("Harga dan jumlah harus berupa angka bulat. Transaksi dibatalkan.")
else:
    if harga <= 0 or jumlah <= 0:
        print("Harga dan jumlah harus lebih dari nol. Transaksi dibatalkan.")
    else:
        subtotal = harga * jumlah

        if subtotal >= 200_000:
            persen_diskon = 0.15
        elif subtotal >= 100_000:
            persen_diskon = 0.10
        else:
            persen_diskon = 0

        diskon = subtotal * persen_diskon
        subtotal_setelah_diskon = subtotal - diskon
        pajak = subtotal_setelah_diskon * 0.11
        total = subtotal_setelah_diskon + pajak

        print()
        print("=" * 36)
        print("STRUK TOKOKU".center(36))
        print("=" * 36)
        print(f"Pelanggan       : {nama}")
        print(f"{menu} x{jumlah}")
        print(f"Harga satuan    : Rp {harga:,.0f}".replace(",", "."))
        print(f"Subtotal        : Rp {subtotal:,.0f}".replace(",", "."))
        print(
            f"Diskon ({persen_diskon:.0%})    : -Rp {diskon:,.0f}".replace(",", ".")
        )
        print(f"Pajak (11%)     : Rp {pajak:,.0f}".replace(",", "."))
        print("-" * 36)
        print(f"TOTAL BAYAR     : Rp {total:,.0f}".replace(",", "."))
        print("=" * 36)
        print(f"Terima kasih, {nama}!")
