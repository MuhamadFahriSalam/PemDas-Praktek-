import os
import time

# Data Menu
menu_makanan = [
    {'nama': 'Steak Ayam', 'harga': 25000},
    {'nama': 'Steak Sirlon Sapi', 'harga': 45000},
    {'nama': 'Steak Kambing', 'harga': 45000},
    {'nama': 'Nasi Gurih', 'harga': 15000},
    {'nama': 'Nasi Goreng', 'harga': 25000},
    {'nama': 'Mie Ayam', 'harga': 15000},
    {'nama': 'Dimsum Ayam', 'harga': 15000},
    {'nama': 'Dimsum Sapi', 'harga': 20000},
    {'nama': 'Dimsum Jamur', 'harga': 15000},
    {'nama': 'Keripik Ubi', 'harga': 5000}
]

menu_minuman = [
    {'nama': 'Jus Apel', 'harga': 15000},
    {'nama': 'Jus Jeruk', 'harga': 15000},
    {'nama': 'Jus Alpukat', 'harga': 15000},
    {'nama': 'Jus Mangga', 'harga': 15000},
    {'nama': 'Cappucino', 'harga': 15000},
    {'nama': 'Air Mineral', 'harga': 10000},
    {'nama': 'Kopi Tubruk', 'harga': 10000}
]

menu_tambahan = [
    {'nama': 'Nasi Uduk','harga': 5000},
    {'nama': 'Nasi Putih','harga': 5000},
    {'nama': 'Kuah Soto', 'harga': 5000}
]


# Fungsi - Fungsi
def gett_menu(tipe):
    if (tipe == 0):
        return menu_makanan
    elif (tipe == 1):
        return menu_minuman
    elif (tipe == 2):
        return menu_tambahan
    else:
        return None

# Menampilkan Semua
def display_menu(tipe):
    menu = gett_menu(tipe)
    if (menu == None):
        return False

    # Tampilkan Semua Array dengan looping
    for id in range(len(menu)):
        menunya = menu[id]
        no = id + 1
        if (tipe == 2):
            no = chr(no + 64) # Angka ke huruf
        print(f"{no}. {menunya['nama']}, Rp: {menunya['harga']}")

    return True

def display_pesanan():
    # Tampilkan Semua Array dengan looping
    for id in range(len(data_pesanan)):
        pesanannya = data_pesanan[id]
        no = id + 1
        print(f"{no}. {pesanannya['pelanggan']}, {pesanannya['pesanan']['nama']}, Rp: {pesanannya['pesanan']['harga']}")

# Mengecek Menu
def cekk_menu(tipe, pilih):
    if (pilih < 0):
        return None
    
    menu = gett_menu(tipe)
    try:
        menunya = menu[pilih]
        return menunya
    except:
        return None

# Bersihkan Layar    
def clear():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')


# Data Pesanan
data_pesanan = []

# Konsol Input
keluar = False
while(keluar == False):
    clear()
    print("----Selamat Datang di warung ABCD----")
    print("1. Beli Sesuatu")
    print("2. Lihat Daftar Pembayaran")
    pilih = int(input("mau ngapain? "))
    pilih -= 1

    # Pembelian
    if (pilih == 0):
        # Data
        pesanan = {
            'pelanggan': '',
            'makanan': {},
            'minuman': {},
            'tambahan': {}
        }

        nama = input("nama kamu? ")
        clear()

        # Pembelian Makanan
        print("----Menu Makanan----")
        display_menu(0)
        pilih = int(input("mau beli makanan apa? "))
        pilih -= 1
        clear()

        menunya = cekk_menu(0, pilih)
        if (menunya != None):
            pesanan['makanan'] = menunya
            print("Berhasil Membeli")
        else:
            print("Makanan Tidak ada, skipp")
        time.sleep(1)
        clear()


        # Pembelian Minuman
        print("----Menu Minuman----")
        display_menu(1)
        pilih = int(input("mau beli minuman apa? "))
        pilih -= 1
        clear()

        menunya = cekk_menu(1, pilih)
        if (menunya != None):
            pesanan['minuman'] = menunya
            print("Berhasil Membeli")
        else:
            print("Minuman Tidak ada, skipp")
        time.sleep(1)
        clear()


        # Pembelian Tambahan
        print("----Menu Tambahan----")
        display_menu(2)
        pilih = input("mau menambahkan sesuatu? ")
        pilih = ord(pilih.upper()) - 65
        clear()

        menunya = cekk_menu(2, pilih)
        if (menunya != None):
            pesanan['tambahan'] = menunya
            print("Berhasil Membeli")
        else:
            print("Tambahan Tidak ada, skipp")
        time.sleep(1)
        clear()

        # Penambahan Pesanan
        data_pesanan.append(pesanan)


    # Daftar Pembayaran
    elif (pilih == 1):
        # Percobaan display semua pesanan
        print("----Data Pembayaran----")
        for n in range(len(data_pesanan)):
            tpesanan = data_pesanan[n]
            print(f"{n + 1}. {tpesanan}")
        
        input("...")

    else:
        pass



# Nyimpen
#with open("pesanan.txt", "a") as file:
#    file.write(f"{nama}, {kode}")