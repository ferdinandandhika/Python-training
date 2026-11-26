# Solusi 5.2 - Decorator Sederhana
def catat_pesan(fungsi):
    def pembungkus():
        print("Mulai menjalankan fungsi")
        fungsi()
        print("Selesai menjalankan fungsi")

    return pembungkus


@catat_pesan
def tampilkan_laporan():
    print("Laporan penjualan TokoKu")


tampilkan_laporan()
