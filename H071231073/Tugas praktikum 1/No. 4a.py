print("pengujian jenis karakter")
x = input("karakter = ")  # x = dapat berupa int, str, maupun float

if x >= 'A' and x <= 'Z':
    print("huruf besar? : True")
    print("huruf kecil? : False")
    print("angka?       : False")
    
elif x >= 'a' and x <= 'z':
    print("huruf besar? : False")
    print("huruf kecil? : True")
    print("angka?       : False")

elif x >= 0 and x <= 9:
    print("huruf besar? : False")
    print("huruf kecil? : False")
    print("angka?       : True")
