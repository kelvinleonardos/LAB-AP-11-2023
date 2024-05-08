import os

def clear():
    os.system("cls")

clear()

# Modul Abstract Class
from abc import ABC, abstractmethod

class InvalidInputError(Exception):
    pass

# Class Utama, Encapsulation dan Abstract Method
class Orang(ABC):
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur

    def get_nama(self):
        return self._nama

    def get_umur(self):
        return self._umur

    @abstractmethod
    def cek_Jomok(self):
        pass

# Inheritance, Polymorphism
class Normal(Orang):
    def cek_Jomok(self):
        return f"{self._nama} berumur {self._umur}, dan dia normal."

class Jomok(Orang):
    def cek_Jomok(self):
        return f"{self._nama} berumur {self._umur}, dan dia jomok."

Manusia = []
while True:
    print("\n" + "=" * 40)
    print("---- JOMOK CHECKER (100% accurate) ----")
    print("=" * 40 + "\n")
    print("Menu:")
    print("1. Tambah Orang")
    print("2. Tampilkan Data Orang")
    print("3. Keluar")

    try:
        print("=" * 40)
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan not in ['1', '2', '3']:
            raise InvalidInputError("Pilihan invalid. Pilih antara 1-3.")

        if pilihan == '1':
            clear()
            print("=" * 40)
            while True:
                nama = input("Masukkan nama: ")
                if all(char.isalpha() or char == '.' or char == ' ' for char in nama):
                    break
                else:
                    print("Nama hanya boleh mengandung huruf, spasi dan titik. Silakan coba lagi.")

            while True:
                try:
                    umur = int(input("Masukkan umur: "))
                    break
                except ValueError:
                    print("Error: Masukkan umur harus berupa angka. Silakan coba lagi.")

            while True:
                jomok_pilihan = input("Apakah orang ini menyukai sesama jenis? (y/n): ").lower()
                if jomok_pilihan in ['y', 'n']:
                    break
                else:
                    print("Pilihan tidak valid. Harap masukkan 'y' atau 'n'. Silakan coba lagi.")

            clear()

            if jomok_pilihan == 'y':
                manusia = Jomok(nama, umur)
            else:
                manusia = Normal(nama, umur)

            Manusia.append(manusia)

            print("Orang telah ditambahkan")


        elif pilihan == '2':
            clear()
            print("=" * 40)
            if not Manusia:
                print("Belum ada data orang.")
                print("=" * 40)
            else:
                Manusia.sort(key=lambda x: isinstance(x, Normal), reverse=True)
                
                for orang in Manusia:
                    print(orang.cek_Jomok())
                print("=" * 40)

        elif pilihan == '3':
            print("Program selesai.")
            print("=" * 40)
            break

    except ValueError:
        clear()
        print("=" * 40)
        print("Error: Masukkan umur harus berupa angka.")

    except InvalidInputError as pesan:
        clear()
        print("=" * 40)
        print(f"Error: {pesan}")

    input("Tekan Enter untuk melanjutkan...")
    clear()