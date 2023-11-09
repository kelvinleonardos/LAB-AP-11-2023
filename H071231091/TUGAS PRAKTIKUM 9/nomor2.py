class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkaninfo(self):
        return f"Nama   :{self.nama} \nNIM    :{self.nim} \nJurusan:{self.jurusan} \nIPK    :{self.ipk}"

    def hitungpredikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif 3.4 >= self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif 2.9 >= self.ipk >= 2.5:
            return "Memuaskan"
        elif 2.4 >= self.ipk >= 2.0:
            return "Cukup"
        else:
            return "kurang"

mahasiswa_list = []

while True:
    nama = input("Nama Mahasiswa: ")
    nim = input("NIM: ")
    jurusan = input("Jurusan: ")
    ipk = float(input("IPK: "))

    orang = Mahasiswa(nama, nim, jurusan, ipk)
    info = orang.tampilkaninfo()
    predikat = orang.hitungpredikat()

    mahasiswa_list.append(orang) 

    lanjut = input("Input data mahasiswa lagi? (y/n): ")
    if lanjut.lower() != 'y':
        break

for mahasiswa in mahasiswa_list:
    print("Mahasiswa:")
    print(mahasiswa.tampilkaninfo())
    print("Predikat yang didapat:")
    print(f"Predikat: {mahasiswa.hitungpredikat()}")
