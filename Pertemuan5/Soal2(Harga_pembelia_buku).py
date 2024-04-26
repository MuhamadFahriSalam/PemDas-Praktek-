def daftar_buku():
    # Daftar Buku
    daftar_buku = {
        1: {"judul": "Belajar Python Untuk Pemula", "harga": 10000},
        2: {"judul": "Langkah Menuju Data Analys", "harga": 15000},
        3: {"judul": "Menjadi Data Scientis", "harga": 20000}
    }

    print("Daftar Buku:") # Menampilkan Daftar Buku
    for nomor, buku in daftar_buku.items():
        print("{}. {} - Harga: Rp {:,}".format(nomor, buku['judul'], buku['harga']))
    nomor_buku = int(input("Masukkan nomor buku yang ingin dibeli (0 untuk keluar): ")) # Input nomor buku yang ingin dibeli
    if nomor_buku not in daftar_buku and nomor_buku != 0: # Periksa apakah nomor buku ada dalam daftar
        print("Nomor buku tidak valid!")
    elif nomor_buku == 0:
        print("Terima kasih!")
    else:
        jumlah_buku = int(input("Berapa banyak buku yang ingin Anda beli?: ")) # Input jumlah buku yang ingin dibeli
        judul_buku = daftar_buku[nomor_buku]["judul"] # Hitung total harga
        harga_satuan = daftar_buku[nomor_buku]["harga"]
        total_harga = harga_satuan * jumlah_buku
        print("\nStruk Penjualan Buku:") # Output Struk Penjualan Buku
        print("Judul buku: {}".format(judul_buku))
        print("Jumlah: {}".format(jumlah_buku))
        print("Total harga: Rp {:,}".format(total_harga))
daftar_buku()
