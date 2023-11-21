# Soal 3 : Mengvalidasi registrasi akun user
'''
contoh
username = radinata69
email = explosivenuts69@gmail.com
password = MiraiCantik69
'''
import re

def Validasi_Username(Username):
    Pola = r'^[a-zA-Z0-9]{5,20}$'
    cocok = re.match(Pola, Username)

    return cocok
    
def Validasi_Email(Email):
    Pola = r"^[a-z0-9]{2,}@[a-z]+\.(com|co\.id|unhas.ac\.id|ac.id|[a-z]+)$"
    cocok = re.match(Pola, Email)

    return cocok

def Validasi_Password(Pass):
    Pola = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$'
    cocok = re.match(Pola, Pass)

    return cocok


Username = input('Masukkan username \t: ')

if Validasi_Username(Username):
    Email = input('Masukkan email \t\t: ')
    if Validasi_Email(Email):
        Pass = input('Masukkan Password \t: ')
        if Validasi_Password(Pass):
            print(f'\nRegistrasi berhasil! Selamat datang, {Username}')

        else:
            print('\nPassword yang kamu input tidak valdi. Registrasi gagal!')
    else:
        print('\nEmail yang kamu input tidak valdi. Registrasi gagal!')
else:
    print('\nUsername yang kamu input tidak valdi. Registrasi gagal!')