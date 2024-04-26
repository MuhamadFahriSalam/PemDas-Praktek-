def kecepatan_mobil():
    # Menghitung jarak dengan rumus jarak = kecepatan * waktu
    def hitung_jarak(kecepatan, waktu): 
        jarak = kecepatan * waktu
        return jarak
    # Menghitung waktu dengan rumus waktu = jarak / kecepatan
    def hitung_waktu(jarak, kecepatan): 
        waktu = jarak / kecepatan
        return waktu
    # Menghitung kecepatan dengan rumus kecepatan = jarak / waktu
    def hitung_kecepatan(jarak, waktu): 
        kecepatan = jarak / waktu
        return kecepatan
    # Meminta pengguna memasukkan kecepatan rata-rata dan waktu tempuh
    kecepatan_rata_rata = float(input("Kecepatan rata-rata mobil (km/jam): ")) 
    waktu_tempuh = float(input("Waktu tempuh (jam): "))
    # Menghitung jarak tempuh menggunakan fungsi hitung_jarak()
    jarak_tempuh = hitung_jarak(kecepatan_rata_rata, waktu_tempuh) 
    # Menghitung kecepatan menggunakan fungsi hitung_kecepatan()
    kecepatan = hitung_kecepatan(jarak_tempuh, waktu_tempuh) 
    # Mencetak hasil kecepatan
    print("Kecepatan mobil adalah", kecepatan, "kilometer per jam.") 
     # Menghitung waktu menggunakan fungsi hitung_waktu()
    waktu = hitung_waktu(jarak_tempuh, kecepatan_rata_rata)
    # Mencetak hasil waktu
    print("Waktu tempuh mobil adalah", waktu, "jam.")
    # Mencetak hasil jarak tempuh
    print("Jarak tempuh mobil adalah", jarak_tempuh, "kilometer.") 
kecepatan_mobil()
