# Solusi 3.1 - Customer Order
menu = {
    "K01": {"nama": "Kopi Susu Aren", "harga": 25000},
    "K02": {"nama": "Americano", "harga": 22000},
    "T01": {"nama": "Matcha Latte", "harga": 28000},
    "F01": {"nama": "Croissant", "harga": 18000},
}
pesanan = [{"kode": "K01", "qty": 2}, {"kode": "F01", "qty": 3}, {"kode": "T01", "qty": 1}]
menu["F02"] = {"nama": "Cheesecake", "harga": 32000}

print("DAFTAR MENU")
for kode, info in menu.items():
    print(f"  {kode}  {info['nama']:<16} Rp {info['harga']:>7,}")

print("\nPESANAN")
total = 0
rincian = []
for item in pesanan:
    info = menu[item["kode"]]
    subtotal = info["harga"] * item["qty"]
    total += subtotal
    rincian.append({"nama": info["nama"], "subtotal": subtotal})
    print(f"  {info['nama']:<16} x{item['qty']}  Rp {subtotal:>8,}")

termahal = max(rincian, key=lambda r: r["subtotal"])
print(f"\nJumlah item : {sum(i['qty'] for i in pesanan)}")
print(f"Total       : Rp {total:,}")
print(f"Termahal    : {termahal['nama']} (Rp {termahal['subtotal']:,})")
