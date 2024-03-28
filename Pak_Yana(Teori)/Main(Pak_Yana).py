def choose():
    print("Rencana setelah lulus sekolah? \n1. Kuliah \n2. Kerja")
    pilihan_utama = input("Masukkan pilihan: ")
    
    if pilihan_utama == '1':
        print("Kuliah jurusan apa? \n1. Teknik Industri \n2. Kedokteran")
        pilihan_kuliah = input("Masukkan pilihan: ")
        if pilihan_kuliah == '1':
            print("Kuliah di Jurusan Teknik Industri")
        elif pilihan_kuliah == '2':
            print("Kuliah di Jurusan Kedokteran")
        else:
            print("Pilihan tidak valid.")
        
    elif pilihan_utama == '2':
        print("Kerja di Industri apa? \n1. Pertambangan \n2. Teknologi")
        pilihan_kerja = input("Masukkan Pilihan: ")
        if pilihan_kerja == '1':
            print("Kerja di Industri Pertambangan")
        elif pilihan_kerja == '2':
            print("Kerja di Industri Teknologi")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Pilihan tidak valid.")

choose()



