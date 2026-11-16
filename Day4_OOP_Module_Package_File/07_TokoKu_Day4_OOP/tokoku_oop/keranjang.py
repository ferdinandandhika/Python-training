"""Keranjang belanja: composition + dunder method."""
from .produk import rupiah


class ItemKeranjang:
    def __init__(self, produk, qty):
        self.produk = produk
        self.qty = qty

    def subtotal(self):
        return self.produk.harga_satuan() * self.qty


class Keranjang:
    def __init__(self):
        self._items = {}                       # {kode: ItemKeranjang}

    def tambah(self, produk, qty=1):
        if qty <= 0:
            raise ValueError("Qty harus lebih dari nol")
        if produk.kode in self._items:
            self._items[produk.kode].qty += qty
        else:
            self._items[produk.kode] = ItemKeranjang(produk, qty)

    def kurangi(self, kode, qty=1):
        if kode not in self._items:
            raise KeyError(kode)
        self._items[kode].qty -= qty
        if self._items[kode].qty <= 0:
            del self._items[kode]

    def subtotal(self):
        return sum(i.subtotal() for i in self)

    def __iter__(self):                        # for item in keranjang
        return iter(self._items.values())

    def __len__(self):                         # len(keranjang)
        return sum(i.qty for i in self._items.values())

    def __contains__(self, kode):              # "K01" in keranjang
        return kode in self._items

    def __bool__(self):                        # if keranjang:
        return bool(self._items)

    def __str__(self):                         # print(keranjang)
        if not self:
            return "(keranjang kosong)"
        return "\n".join(f"{i.produk.deskripsi():<20} x{i.qty:<3}{rupiah(i.subtotal()):>12}" for i in self)
