# Nomor 4

a = input("masukan karakter : ")

hurufkapital = a >= 'A' and a <= 'Z'
hurufkecil = a >= 'a' and a <= 'z'
angka = a >= '0' and a <= '9'

print(f'huruf kapital? {hurufkapital}')
print(f'huruf kecil? {hurufkecil}')
print(f'angka? {angka}')