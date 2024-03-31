def gaji_karyawan():
    # Define gaji dasar untuk setiap golongan
    GAJI_DASAR = {'A': 1000000, 'B': 1500000, 'C': 2000000}
    # Define persentase tunjangan untuk setiap golongan
    TUNJANGAN_PERS = {'A': 0.05, 'B': 0.15, 'C': 0.25}
    # Define gaji lembur per jam untuk setiap golongan
    GAJI_LEMBUR_PER_JAM = {'A': 20000, 'B': 25000, 'C': 30000}
    # Dapatkan input dari pengguna
    nama = input("Nama: ")
    masa_kerja = int(input("Masa Kerja: "))
    golongan = input("Golongan: ").upper()
    total_jam_kerja = int(input("Total Jam Kerja: "))
    # Hitung gaji dasar berdasarkan golongan
    gaji = GAJI_DASAR[golongan]
    # Hitung tunjangan berdasarkan golongan
    tunjangan = TUNJANGAN_PERS[golongan] * gaji
    # Hitung gaji lembur jika berlaku
    if total_jam_kerja > 40 * 4:  # 40 jam * 4 minggu
        jam_lembur = total_jam_kerja - 40 * 4
        gaji_lembur = GAJI_LEMBUR_PER_JAM[golongan] * jam_lembur
    else:
        gaji_lembur = 0
    # Hitung total gaji
    total_gaji = gaji + tunjangan + gaji_lembur
    # Cetak hasil
    print("\nDATA PEGAWAI")
    print("Nama: ", nama)
    print("Masa Kerja: ", masa_kerja, "tahun")
    print("Golongan: ", golongan)
    print("Total Jam Kerja: ", total_jam_kerja, "jam")
    print("\nPERHITUNGAN GAJI")
    print("Gaji Pokok: ", gaji)
    print("Tunjangan: ", tunjangan)
    print("Gaji Lembur: ", gaji_lembur)
    print("Total Gaji: ", total_gaji)
gaji_karyawan()