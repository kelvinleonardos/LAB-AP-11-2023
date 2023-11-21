class mahasiswa :
    def __init__(self,nama,nim,jurusan,ipk) :
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self) :
        print(f"Nama Mahasiswa : {self.nama}\nNim            : {self.nim}\nJurusan        : {self.jurusan} \nIPK            : {self.ipk}")
    
    def Hitung_predikat(self) :
        if self.ipk >= 3.5 :
            print("Cumlaude")
        elif self.ipk >= 3.0 :
            print("Sangat Memuaskan")
        elif self.ipk >= 2.5 :
            print ("Memuaskan")
        elif self.ipk >= 2.0 :
            print ("Cukup")
        elif self.ipk < 2.0 :
            print ("kurang")
while True :
    nama = input()
    nim = input()
    jurusan = input()
    ipk = float(input())
    mhs = mahasiswa(nama,nim,jurusan,ipk)
    mhs.tampilkan_info()
    mhs.Hitung_predikat()
    while True :
        x = input("lanjut ? ") 
        if x == "ya" or x == "tidak" :
            break
        else :
            print("ya atau tidak")
    if x == "tidak" :
        break