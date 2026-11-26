# Latihan 5.2 - Decorator Sederhana
def catat_pesan(fungsi):
    def pembungkus():
        # TODO 1: tampilkan pesan bahwa fungsi mulai dijalankan.
        # TODO 2: panggil fungsi asli.
        # TODO 3: tampilkan pesan bahwa fungsi selesai dijalankan.
        pass

    return pembungkus


@catat_pesan
def tampilkan_laporan():
    print("Laporan penjualan TokoKu")


tampilkan_laporan()
