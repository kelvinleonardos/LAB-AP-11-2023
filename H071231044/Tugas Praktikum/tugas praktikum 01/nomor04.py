print("No.4")
#Konversi huruf kapital, huruf kecil, dan nomor huruf 
print("Pengujian Jenis Karakter")
print("------------------------")
a = input("masukkan karakter : ")

Hurufkapital = a >= 'A' and a <= 'Z'
Hurufkecil = a >= 'a' and a <= 'z'
Angka = a >= '0' and a <= '9'

print(f'Huruf Kapital? {Hurufkapital}')
print(f'Huruf Kecil? {Hurufkecil}')
print(f'Angka? {Angka}')