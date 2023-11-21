import os
os.system("cls")

class Mahasiswa:
    def __init__(self, nama, NIM, Jurusan, IPK):
        self.Nama = nama
        self.NIM = NIM
        self.Jurusan = Jurusan
        self.IPK = float(IPK)

    def Tampilkan_info(self):
        print(f'Nama \t : {self.Nama}')
        print(f'NIM \t : {self.NIM}')
        print(f'Jurusan  : {self.Jurusan}')
        print(f'IPK \t : {self.IPK}')

    def Hitung_predikat(self):
        if self.IPK >= 3.5:
            return 'Cumlaude'
        elif self.IPK >= 3.0:
            return 'Sangat Memuaskan'
        elif self.IPK >= 2.5:
            return 'Memuaskan'
        elif self.IPK >= 2.0:
            return 'Cukup'
        else:
            return 'Kurang'

mahasiswa_list = []

while True:
    nama = input("Masukkan Nama Mahasiswa: ")
    NIM = input("Masukkan NIM Mahasiswa: ")
    jurusan = input("Masukkan Jurusan Mahasiswa: ")
    IPK = input("Masukkan IPK Mahasiswa: ")


    mahasiswa = Mahasiswa(nama, NIM, jurusan, IPK)
    mahasiswa_list.append(mahasiswa)

    lanjut = input("Tambahkan mahasiswa lain? (y/n): ")
    if lanjut.lower() != 'y':
        break

for mahasiswa in mahasiswa_list:
    mahasiswa.Tampilkan_info()
    print(f'Predikat : {mahasiswa.Hitung_predikat()}')
    print('-' * 50)