import re
username = input("Masukkan Username : ")
p1 = r"^[A-Za-z0-9]{5,20}$"
if not re.match(p1,username) :
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")
    exit()

email = input("Masukkan Email : ")
p2 = r"^[a-z]+(\d{2,})?@[a-z]+\.[a-z]+(\.id)?$"
if not re.match(p2,email):
    print("\nEmail yang kamu input tidak valid. Registrasi gagal")
    exit()

password = input("Masukkan Password : ")
p3 = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
if not re.match(p3,password):
    print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    exit()
else :
    print(f"\nRegistrasi berhasil! Selamat datang, {username}")