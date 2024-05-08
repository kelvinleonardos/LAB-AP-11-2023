import re
def is_valid_username(username):
    pattern = r"^([0-z]){5,20}$"
    return re.search(pattern, username)

def is_valid_email(email):
    pattern = r"^[a-z0-9._]+@[a-z]+\.[a-z]{2,}(\.[a-z]{2,})?$" 
    return re.search(pattern, email)

def is_valid_password(password):
    pattern = r"^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^!@#$%^&*()_+]{8,})$"
    return re.search(pattern, password)

# --------
username = input("Masukkan username: ")

if is_valid_username(username):
    email = input("Masukkan email: ")
    
    if is_valid_email(email):
        password = input("Masukkan password: ")
        
        if is_valid_password(password):
            print("\nRegistrasi berhasil! ...") # TODO: Tambahkan sapaan "Halo (username)"
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")