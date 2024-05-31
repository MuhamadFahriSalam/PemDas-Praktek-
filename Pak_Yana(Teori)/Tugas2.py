# Rancang Bangun Sistem Informasi Pengelolaan Data Akademik Berbasis Web
from tabulate import tabulate

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def tampilkan_info(self):
        return [self.nim, self.nama, self.jurusan]

# Daftar mahasiswa
daftar_mahasiswa = []

# Fungsi untuk menambah mahasiswa
def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    mahasiswa = Mahasiswa(nim, nama, jurusan)
    daftar_mahasiswa.append(mahasiswa)
    print("Data mahasiswa berhasil ditambahkan!")

# Fungsi untuk menampilkan semua mahasiswa
def tampilkan_semua_mahasiswa():
    if not daftar_mahasiswa:
        print("Tidak ada data mahasiswa.")
        return

    # Menggunakan tabulate untuk menampilkan data dalam bentuk tabel dengan perataan tengah
    tabel = [mahasiswa.tampilkan_info() for mahasiswa in daftar_mahasiswa]
    print(tabulate(tabel, headers=["NIM", "Nama", "Jurusan"], tablefmt="grid", stralign="center", colalign=("center", "center", "center")))

# Fungsi untuk mencari mahasiswa berdasarkan 4 angka terakhir NIM
def cari_mahasiswa(nim_akhir):
    hasil_pencarian = [mahasiswa for mahasiswa in daftar_mahasiswa if mahasiswa.nim.endswith(nim_akhir)]
    return hasil_pencarian

# Fungsi utama
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua_mahasiswa()
        elif pilihan == "3":
            nim_akhir = input("Masukkan 4 angka terakhir NIM: ")
            hasil = cari_mahasiswa(nim_akhir)
            if hasil:
                tabel_hasil = [mahasiswa.tampilkan_info() for mahasiswa in hasil]
                print(tabulate(tabel_hasil, headers=["NIM", "Nama", "Jurusan"], tablefmt="grid", stralign="center", colalign=("center", "center", "center")))
            else:
                print("Mahasiswa tidak ditemukan.")
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
