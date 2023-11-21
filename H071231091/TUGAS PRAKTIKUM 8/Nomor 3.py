import re

def is_valid_username(username):
    pattern = r"^[0-z.]{5,20}$"
    return re.search(pattern, username)

def is_valid_email(email):
    pattern = r"^[a-z.]+(\d{2,})?@[a-z]+\.(com|co\.id|ac.id|org)$"
    return re.search(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    return re.search(pattern, password)

while True:
    username = input("Masukkan username: ")
    if is_valid_username(username):
        break
    else:
        print("Inputan username tidak valid dalam sistem. Silakan coba lagi.")

while True:
    email = input("Masukkan email: ")
    if is_valid_email(email):
        break
    else:
        print("Email yang kamu input tidak valid. Silakan coba lagi.")

while True:
    password = input("Masukkan password: ")
    if is_valid_password(password):
        break
    else:
        print("Password yang kamu input beresiko dihack. Silakan coba lagi.")

text =f'''
================================================================================
|USERNAME          : {username}                                               
|EMAIL             : {email}                                                  
|PASSWORD          : {password}                                               
================================================================================'''
print(text)
print(f"Registrasi berhasil! Selamat datang, {username}")


