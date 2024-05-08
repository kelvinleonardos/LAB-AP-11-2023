import re
Input = input("Masukkan kata : ")
susunan_kata = r"^[a-zA-Z02468]{40}[13579 ]{5}$"
x = re.match(susunan_kata, Input)

if x :
    print ("Susunan kata sudah benar")
else :
    print ("masih ada kesalahan")

# t = "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"
# t = "x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779"

# x ="2222222222aaBBBBaa2222222222aaaaaaaaaa13 57"
# print (len(x))
