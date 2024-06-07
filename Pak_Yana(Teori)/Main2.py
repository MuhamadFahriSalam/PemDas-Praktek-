# Rancang Bangun Sistem Informasi Manajemen Laundry
import streamlit as st
from tabulate import tabulate
import json
import os

class LaundryItem:
    def __init__(self, nama, berat, harga):
        self.nama = nama
        self.berat = berat
        self.harga = harga

    def to_dict(self):
        return {"nama": self.nama, "berat": self.berat, "harga": self.harga}

class LaundryOrder:
    def __init__(self):
        self.items = []

    def tambah_item(self, item):
        self.items.append(item)
    
    def hapus_item(self, item):
        self.items.remove(item)

    def hitung_total_berat(self):
        total_berat = sum(item.berat for item in self.items)
        return total_berat
    
    def hitung_total_harga(self):
        total_harga = sum(item.harga for item in self.items)
        return total_harga
    
    def cari_item(self, nama_dicari):
        items_ditemukan = [item for item in self.items if item.nama == nama_dicari]
        return items_ditemukan

    def to_dict(self):
        return {"items": [item.to_dict() for item in self.items]}

def simpan_pesanan(pesanans, filename="laundry_orders.json"):
    with open(filename, "w") as file:
        json.dump([pesanan.to_dict() for pesanan in pesanans], file, indent=1)

def muat_pesanan(filename="laundry_orders.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data_pesanan = json.load(file)
        pesanans = [LaundryOrder() for _ in range(len(data_pesanan))]
        for pesanan, data in zip(pesanans, data_pesanan):
            pesanan.items = [LaundryItem(**item_data) for item_data in data["items"]]
        return pesanans
    else:
        return []

def main():
    st.title("Aplikasi Laundry Barokah")
    laundry_pesanans = muat_pesanan()

    menu_options = {
        "men-0": "Tambah Item Laundry",
        "men-1": "Lihat Pesanan",
        "men-2": "Hitung Total Berat",
        "men-3": "Hitung Total Harga",
        "men-4": "Cari Item Laundry",
        "men-5": "Hapus Item Laundry",
        "men-6": "Keluar"
    }

    menu_keys = menu_options.keys()
    menu_values = menu_options.values()

    pilihan = st.sidebar.selectbox("Menu", menu_values, key="pemuda tersesat")

    if pilihan == "Tambah Item Laundry":
        nama = st.text_input("Masukkan nama item:")
        berat = st.number_input("Masukkan berat item (kg):")

        if st.button("Tambahkan Item"):
            harga = int(10000 * berat)
            item = LaundryItem(nama, berat, harga)
            pesanan_laundry = LaundryOrder()
            pesanan_laundry.tambah_item(item)
            laundry_pesanans.append(pesanan_laundry)
            simpan_pesanan(laundry_pesanans)
            st.success("Item ditambahkan ke pesanan.")

    elif pilihan == "Lihat Pesanan":
        st.subheader("Detail Pesanan:")
        data_tabel = []
        for no_pesanan, pesanan_laundry in enumerate(laundry_pesanans, 1):
            for i, item in enumerate(pesanan_laundry.items, 1):
                data_tabel.append([no_pesanan, item.nama, item.berat, item.harga])
        
        headers = ["No.", "Nama Item", "Berat (kg)", "Total Harga"]
        st.text(tabulate(data_tabel, headers=headers, tablefmt="grid"))

    elif pilihan == "Hitung Total Berat":
        total_berat = sum(pesanan.hitung_total_berat() for pesanan in laundry_pesanans)
        st.info(f"Total Berat Pesanan: {total_berat} kg")

    elif pilihan == "Hitung Total Harga":
        total_harga = sum(pesanan.hitung_total_harga() for pesanan in laundry_pesanans)
        st.info(f"Total Harga Pesanan Rp: {int(total_harga)}")

    elif pilihan == "Cari Item Laundry":
        nama_dicari = st.text_input("Masukkan nama item yang dicari:")
        items_ditemukan = [
            item for pesanan in laundry_pesanans
            for item in pesanan.items
            if nama_dicari.lower() in item.nama.lower()
        ]

        if items_ditemukan:
            st.subheader("Item ditemukan:")
            data_tabel = []
            for i, item_ditemukan in enumerate(items_ditemukan, 1):
                data_tabel.append([i, item_ditemukan.nama, item_ditemukan.berat, item_ditemukan.harga])

            headers = ["No.", "Nama Item", "Berat (kg)", "Total Harga"]
            st.text(tabulate(data_tabel, headers=headers, tablefmt="grid"))
        else:
            st.warning("Item tidak ditemukan.")

    elif pilihan == "Hapus Item Laundry":
        nama_dicari = st.text_input("Masukkan nama item yang dicari:")
        items_ditemukan = [
            (pesanan, item) for pesanan in laundry_pesanans
            for item in pesanan.items
            if nama_dicari.lower() in item.nama.lower()
        ]

        if items_ditemukan:
            st.subheader("Item Dicari:")
            data_tabel = []
            for i, (pesanan, item_ditemukan) in enumerate(items_ditemukan, 1):
                data_tabel.append([i, item_ditemukan.nama, item_ditemukan.berat, item_ditemukan.harga])

            headers = ["No.", "Nama Item", "Berat (kg)", "Total Harga"]
            st.text(tabulate(data_tabel, headers=headers, tablefmt="grid"))
            
            # Hapus
            if st.button("Hapus Item"):
                for pesanan, item_ditemukan in items_ditemukan:
                    pesanan.hapus_item(item_ditemukan)
                simpan_pesanan(laundry_pesanans)
                st.success("Item dihapus dari pesanan.")
        else:
            st.warning("Item tidak ditemukan.")
        
    elif pilihan == "Keluar":
        st.success("Terima kasih. Program selesai.")
        # Anda dapat keluar dari program di sini, tetapi untuk Streamlit, ini tidak diperlukan.
        # st.stop()


if __name__ == "__main__":
    main()













# # Rancang Bangun Sistem Informasi Pengelolaan Data Akademik Berbasis Web
# import streamlit as st
# from tabulate import tabulate

# class Mahasiswa:
#     def __init__(self, nim, nama, jurusan):
#         self.nim = nim
#         self.nama = nama
#         self.jurusan = jurusan

#     def tampilkan_info(self):
#         return [self.nim, self.nama, self.jurusan]

# # Daftar mahasiswa
# daftar_mahasiswa = []

# # Fungsi untuk menambah mahasiswa
# def tambah_mahasiswa():
#     nim = input("Masukkan NIM: ")
#     nama = input("Masukkan Nama: ")
#     jurusan = input("Masukkan Jurusan: ")
#     mahasiswa = Mahasiswa(nim, nama, jurusan)
#     daftar_mahasiswa.append(mahasiswa)
#     print("Data mahasiswa berhasil ditambahkan!")

# # Fungsi untuk menampilkan semua mahasiswa
# def tampilkan_semua_mahasiswa():
#     if not daftar_mahasiswa:
#         print("Tidak ada data mahasiswa.")
#         return

#     # Menggunakan tabulate untuk menampilkan data dalam bentuk tabel dengan perataan tengah
#     tabel = [mahasiswa.tampilkan_info() for mahasiswa in daftar_mahasiswa]
#     print(tabulate(tabel, headers=["NIM", "Nama", "Jurusan"], tablefmt="grid", stralign="center", colalign=("center", "center", "center")))

# # Fungsi untuk mencari mahasiswa berdasarkan 4 angka terakhir NIM
# def cari_mahasiswa(nim_akhir):
#     hasil_pencarian = [mahasiswa for mahasiswa in daftar_mahasiswa if mahasiswa.nim.endswith(nim_akhir)]
#     return hasil_pencarian

# # Fungsi utama
# def main():
#     while True:
#         print("\nMenu:")
#         print("1. Tambah Mahasiswa")
#         print("2. Tampilkan Semua Mahasiswa")
#         print("3. Cari Mahasiswa")
#         print("4. Keluar")

#         pilihan = input("Pilih menu: ")

#         if pilihan == "1":
#             tambah_mahasiswa()
#         elif pilihan == "2":
#             tampilkan_semua_mahasiswa()
#         elif pilihan == "3":
#             nim_akhir = input("Masukkan 4 angka terakhir NIM: ")
#             hasil = cari_mahasiswa(nim_akhir)
#             if hasil:
#                 tabel_hasil = [mahasiswa.tampilkan_info() for mahasiswa in hasil]
#                 print(tabulate(tabel_hasil, headers=["NIM", "Nama", "Jurusan"], tablefmt="grid", stralign="center", colalign=("center", "center", "center")))
#             else:
#                 print("Mahasiswa tidak ditemukan.")
#         elif pilihan == "4":
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# # Menjalankan program utama
# if __name__ == "__main__":
#     main()
