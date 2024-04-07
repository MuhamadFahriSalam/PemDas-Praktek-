def gaji_karyawan():
    GAJI_DASAR = {'A': 1000000, 'B': 1500000, 'C': 2000000} # Define gaji dasar untuk setiap golongan
    TUNJANGAN_PERS = {'A': 0.05, 'B': 0.15, 'C': 0.25} # Define persentase tunjangan untuk setiap golongan
    GAJI_LEMBUR_PER_JAM = {'A': 20000, 'B': 25000, 'C': 30000} # Define gaji lembur per jam untuk setiap golongan
     # Dapatkan input dari pengguna
    nama = input("Nama: ") 
    masa_kerja = int(input("Masa Kerja: "))
    golongan = input("Golongan: ").upper()
    total_jam_kerja = int(input("Total Jam Kerja: "))
    gaji = GAJI_DASAR[golongan] # Hitung gaji dasar berdasarkan golongan
    tunjangan = TUNJANGAN_PERS[golongan] * gaji # Hitung tunjangan berdasarkan golongan
    if total_jam_kerja > 40 * 4:  # Hitung gaji lembur jika berlaku # 40 jam * 4 minggu
        jam_lembur = total_jam_kerja - 40 * 4
        gaji_lembur = GAJI_LEMBUR_PER_JAM[golongan] * jam_lembur
    else:
        gaji_lembur = 0
    # Hitung total gaji    
    total_gaji = gaji + tunjangan + gaji_lembur 
    # Cetak hasil
    print('=' *50) 
    print("{:^50}".format("DATA PEGAWAI"))
    print('=' *50)
    print("{:<15}: {:>2}".format("Nama", nama))
    print("{:<15}: {:>2}".format("Masa Kerja", masa_kerja))
    print("{:<15}: {:>2}".format("Golongan", golongan))
    print("{:<13}: {:>3}".format("Total Jam Kerja", total_jam_kerja))
    print('=' *50)
    print("{:^50}".format("PERHITUNGAN GAJI"))
    print('=' *50)
    print("{:<15}: {:>8,}".format("Gaji Pokok", gaji))
    print("{:<15}: {:>8,}".format("Tunjangan", tunjangan))
    print("{:<15}: {:>8,}".format("Gaji Lembur", gaji_lembur))
    print('-' *50)
    print("{:<15}: {:>8,}".format("Total Gaji", total_gaji))
    print('-' *50)
gaji_karyawan()
