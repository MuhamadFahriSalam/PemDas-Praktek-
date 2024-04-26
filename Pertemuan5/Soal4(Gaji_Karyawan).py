import locale

def hitung_gaji_total():
    # Setel pengaturan lokal untuk Indonesia (ID)
    locale.setlocale(locale.LC_ALL, 'id_ID')

    masa_kerja = int(input("Masukkan Masa Kerja: "))
    gaji_pokok = int(input("Masukkan Gaji Pokok: "))

    # Jika masa kerja kurang dari atau sama dengan 5 tahun, kenaikan gaji sebesar 10%
    if masa_kerja <= 5:
        kenaikan_gaji = 0.10
    # Jika masa kerja lebih dari 5 tahun, kenaikan gaji sebesar 20%
    else:
        kenaikan_gaji = 0.20

    gaji_total = gaji_pokok * (1 + kenaikan_gaji)

    # Format gaji total dengan pemisah ribuan
    gaji_total_formatted = locale.format_string("%.1f", gaji_total, grouping=True)

    print("Gaji total: Rp {}".format(gaji_total_formatted))

hitung_gaji_total()
