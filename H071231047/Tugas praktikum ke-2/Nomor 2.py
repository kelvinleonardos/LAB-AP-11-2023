# Nomor 2

x = input("masukan input pertama : ")
y = input("masukan input kedua : ")
z = input("masukan input ketiga : ")

if x == "vertebrado":
    if y == "ave":
        if z == "carnivoro":
            print("aguia")
        elif z == "onivoro":
            print("pomba")
        else:
            print("tidak valid")
    elif y == "mamifero":
        if z == "onivoro":
            print("homen")
        elif z == "herbivoro":
            print("vaca")
        else:
            print("tidak valid")
if x == "invertebrado":
    if y == "inseto":
        if z == "hematofago":
            print("pulga")
        elif z == " onivoro":
            print("lagarta")
        else:
            print("tidak valid")
    elif y == "anelideo":
        if z == "hematofago":
            print("sanguessuga")
        elif z == "onivoro":
            print("minhoca")
        else:
            print("tidak valid")


