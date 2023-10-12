karakter = input("Masukkan sebuah karakter: ")

if 'a' <= karakter <= 'z':
    print(f"'{karakter}' adalah huruf kecil.")
elif 'A' <= karakter <= 'Z':
    print(f"'{karakter}' adalah huruf besar.")
elif '0' <= karakter <= '9':
    print(f"'{karakter}' adalah angka.")
else:
    print(f"'{karakter}' bukan huruf kecil, bukan huruf besar, dan bukan angka.")
