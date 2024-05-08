class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    
    def show_info(self):
        print(f'nama    : {self.nama}')
        print(f'nim     : {self.nim}')
        print(f'jurusan : {self.jurusan}')
        print(f'ipk     : {self.ipk}')

    def predicate(self):
        if self.ipk >= 3.5:
            print('cumlaude')
        elif self.ipk >= 3.0:
            print('sangat memuaskan')
        elif self.ipk >= 2.5:
            print('memuaskan')
        elif self.ipk >= 2.0:
            print('cukup')
        elif self.ipk < 2.0:
            print('kurang')

x = Mahasiswa('udin', '070', 'sisfo', 3.5)
x.show_info()
x.predicate()