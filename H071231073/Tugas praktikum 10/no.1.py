import re, os
class Data:
    def __init__(self, nama, email, passw):
        self.nama = nama
        self.email = email
        self.passw = passw

    def detail(self):
        print(f'nama        : {self.nama}')
        print(f'email       : {self.email}')
        print(f'password    : {self.passw}')

    def change(self):
        newName = input('New name : ')
        self.nama = newName

    def save(self):
        x = input('file name : ')
        x += '.txt'
        if not os.path.exists(x):
            with open(x, 'w') as f:
                f.write(f"+{'='*74}\n|Data yang tersimpan\n+{'='*74}")
                f.close()
        with open(x, 'a') as f:
            f. write(f"\n|{('Nama').ljust(15)}: {self.nama}\n")
            f. write(f"|{('Email').ljust(15)}: {self.email}\n")
            f. write(f"|{('Password').ljust(15)}: {self.passw}\n")
            f. write(f"+{'='*74}")
                 
while True:
    print(f"{'='*50}\n{('OPTION').center(50)}\n{'-'*50}\n1. Detail\n2. ubah nama\n3. jumlah data pada file\n4. save data pada file\n5. buat data baru\n6. keluar\n{'='*50}")
    while True:
        x = input('input option : ')
        print('='*50)
        if x.isdigit():
            x = int(x)
            break
        else:
            print('re-input the number')
    if x == 1:
        try:
            data.detail()
        except:
            print("Data saat ini kosong")
    elif x == 2:
        try:
            data.change()
        except:
            print("Data saat ini kosong")
    elif x == 3:
        fname = input('search file name : ')
        fname +='.txt'
        if not os.path.exists(fname):
            print(f'{fname} not found')
        else:
            with open(fname, 'r') as f:
                f = f.read()
                x = f.count('@unhas.ac.id')
            print(f'Jumlah data pada file {fname} : {x} Data')
    elif x == 4:
        try:
            data.save()
            del(data)
        except:
            print("Data saat ini kosong")
    elif x == 5:
        nama = input('nama     : ')
        while True:
            email = input('email    : ')
            p = r'^[a-z0-9.]+@unhas\.ac\.id$'
            if re.match(p, email):
                break
            else:
                print('Email yang Anda Masukkan Salah')
        while True: 
            passw = input('password    : ')
            p = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,20}$"
            if len(passw)<8 or len(passw)>20:
                print('Password harus memiliki Panjang 8-20 karakter')
            elif re.match(p, passw):
                break
            else:
                print('Password yang anda masukkan terlalu lemah\nGunakan minimal 1 huruf kapital, huruf kecil, dan angka')
        data = Data(nama, email, passw)
    elif x == 6:
        print(f"{('THE END').center(50)}\n{'='*50}")
        break
    else:
        print('invalid input')