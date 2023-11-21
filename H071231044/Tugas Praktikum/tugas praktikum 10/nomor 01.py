import re
import os

data = []

class Akun :
    def __init__(self,nama,email,password) :
        self.nama = nama
        self.email = email
        self.password = password

    def detail(self):
        print(f"Nama     : {self.nama}\nEmail    : {self.email}\nPassword : {self.password}\n{'='*100}")

    def data_baru(self):
        data.append(nama)
        data.append(email)
        data.append(password)
        print(f"{'='*100}\nData berhasil ditambah\n{'='*100}")

    def ubah_nama(self):
        nama = input("Masukkan Nama Baru : ")
        data[0] = nama
        self.nama = nama
        print(f"{'='*100}\nBerhasil Mengubah Nama\n{'='*100}")

    def save(self):
        file = input()
        x = file + ".txt"
        if not os.path.exists(x) :
            with open(x,"w") as files :
                files.write(f"+{'='*99}\n|Data yang Tersimpan\n+{'='*99}\n")
        with open(x,"a") as files :
            files.write(f"|{'nama'.ljust(9)}: {self.nama}\n|{'Email'.ljust(9)}: {self.email}\n|{'Password'.ljust(9)}: {self.password}\n+{'='*99}\n")
        data.clear()
        self.nama = None
        self.email = None
        self.password = None
        print(f"{'='*100}\nBerhasil Menyimpan data\n{'='*100}")  

print(f"{'='*100}\n{'Selamat Datang'.center(100)}\n{'='*100}")

while True :
    print(f"1. Detail Anda\n2. Ubah Nama\n3. jumlah data pada file\n4. Save Data pada File\n5. Buat Data Baru\n6. Keluar\n{'-'*100}")
    pilihan = input("Silahkan Input Opsi Anda : ")
    print("-"*100)

    match pilihan :

        case "1":
            if data == [] :
                print(f"Data Kosong\n{'-'*100}")
            else :
                ac.detail()

        case "2":
            if data == [] :
                print(f"Data Kosong\n{'-'*100}")
            else :
                ac.ubah_nama()

        case "3":
            file = input("Masukkan Nama File yang ingin dicari : ")
            cari = file + ".txt"
            if not os.path.exists(cari):
                print(f"{'-'*100}\nFile {cari} tidak ditemukan\n{'-'*100}")
            else :
                with open(cari,"r") as files :
                    x = files.read()
                    hitung = x.count("nama")
                    print(f"{'-'*100}\nterdapat {hitung} data dalam {cari}\n{'-'*100}")

        case "4":
            if data == [] :
                print(f"Data Kosong\n{'-'*100}")
            else :
                ac.save()

        case "5":
            nama = input("Masukkan Nama : ")

            while True :
                email = input("Masukkan Email : ")
                patt = r"^[a-z]+[0-9]{2,}+@student\.unhas\.ac\.id$"
                if re.match(patt,email):
                    break
                else :
                    print(f"{'-'*100}\nEmail yang anda Masukkan Salah\n{'-'*100}")
                
            while True :
                password = input("Masukkan Password : ")
                patt = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$"
                if len(password) < 8 or len(password) > 20 :
                    print(f"{'='*100}\nPassword Harus Memiliki panjang 8-20\n{'='*100}")
                else :
                    if re.match(patt,password):
                        break
                    else :
                        print(f"{'-'*100}\nPassword Yang anda masukkan terlalu lemah\nGunakan minimal 1 huruf kapital,huruf kecil dan angka\n{'-'*100}")

            ac = Akun(nama,email,password)
            ac.data_baru()

        case "6":
            print(f"{'Selamat Tinggal'.center(100)}\n{'-'*100}")
            break

        case _:
            print(f"Input Diluar Opsi\n{'='*100}")
            