from prettytable import PrettyTable

class TokoLaptop:
    def __init__(self):
        self.laptops = {}

    def tambah_laptop(self, kode, merk, tipe, harga, stok):
        if kode not in self.laptops:
            self.laptops[kode] = {'Merk': merk, 'Tipe': tipe, 'Harga': harga, 'Stok': stok}
            print(f"Laptop {merk} {tipe} berhasil ditambahkan.")
        else:
            print(f"Laptop dengan kode {kode} sudah ada.")

    def lihat_laptop(self, kode=None):
        if kode is None:
            if not self.laptops:
                print("Tidak ada laptop yang tersedia.")
                return

            for kode, laptop in self.laptops.items():
                table = PrettyTable()
                table.field_names = ["Field", "Value"]
                table.add_row(["Kode", kode])
                for key, value in laptop.items():
                    table.add_row([key, value])
                print(f"Detail Laptop {kode}:\n{table}")
        else:
            if kode in self.laptops:
                laptop = self.laptops[kode]
                table = PrettyTable()
                table.field_names = ["Field", "Value"]
                table.add_row(["Kode", kode])
                for key, value in laptop.items():
                    table.add_row([key, value])
                print(f"Detail Laptop {kode}:\n{table}")
            else:
                print(f"Laptop dengan kode {kode} tidak ditemukan.")

    def ubah_laptop(self, kode, field, nilai_baru):
        if kode in self.laptops:
            if field in self.laptops[kode]:
                self.laptops[kode][field] = nilai_baru
                print(f"Data {field} untuk laptop dengan kode {kode} berhasil diubah.")
            else:
                print(f"Field {field} tidak valid.")
        else:
            print(f"Laptop dengan kode {kode} tidak ditemukan.")

    def hapus_laptop(self, kode):
        if kode in self.laptops:
            del self.laptops[kode]
            print(f"Laptop dengan kode {kode} berhasil dihapus.")
        else:
            print(f"Laptop dengan kode {kode} tidak ditemukan.")

    def lihat_semua_laptop(self):
        if not self.laptops:
            print("Tidak ada laptop yang tersedia.")
            return

        table = PrettyTable()
        table.field_names = ["Kode", "Merk", "Tipe", "Harga", "Stok"]
        for kode, laptop in self.laptops.items():
            table.add_row([kode, laptop['Merk'], laptop['Tipe'], laptop['Harga'], laptop['Stok']])
        print("Daftar Laptop:\n", table)

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Laptop")
            print("2. Lihat Laptop")
            print("3. Ubah Laptop")
            print("4. Hapus Laptop")
            print("5. Lihat Semua Laptop")
            print("0. Keluar")

            choice = input("Pilih menu (0-5): ")

            if choice == '1':
                kode = input("Masukkan kode laptop: ")
                merk = input("Masukkan merk laptop: ")
                tipe = input("Masukkan tipe laptop: ")
                harga = int(input("Masukkan harga laptop: "))
                stok = int(input("Masukkan stok laptop: "))
                self.tambah_laptop(kode, merk, tipe, harga, stok)

            elif choice == '2':
                kode = input("Masukkan kode laptop (atau biarkan kosong untuk melihat semua): ")
                self.lihat_laptop(kode)

            elif choice == '3':
                kode = input("Masukkan kode laptop: ")
                field = input("Masukkan field yang ingin diubah (Merk/Tipe/Harga/Stok): ")
                nilai_baru = input("Masukkan nilai baru: ")
                self.ubah_laptop(kode, field, nilai_baru)

            elif choice == '4':
                kode = input("Masukkan kode laptop yang ingin dihapus: ")
                self.hapus_laptop(kode)

            elif choice == '5':
                self.lihat_semua_laptop()

            elif choice == '0':
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# Contoh penggunaan
toko_laptop = TokoLaptop()
 
toko_laptop.tambah_laptop('1', 'Asus', 'ROG Strix', 15000000, 10)
toko_laptop.tambah_laptop('2', 'Dell', 'Inspiron', 8000000, 15)
toko_laptop.tambah_laptop('3', 'Acer', 'Nitro 5', 18000000, 3)

toko_laptop.menu()
