x = input("Masukkan Input Pertama : ")
y = input("Masukkan Input Kedua : ")
z = input("Masukkan Input Ketiga : ")

if x == "vertebrado" :
    if y == "ave" :
        if z == "carnivoro" :
            print("aguia")
        elif z == "onivoro" :
            print("pomba")
        else:
            print ("Input tidak Valid ! ")
    elif y == "mamifero" :
        if z == "onivoro" :
            print("homem")
        elif z == "herbivoro" :
            print("vaca")
        else:
            print ("Input tidak Valid ! ")
    else:
         print ("Input tidak Valid ! ")
elif x == "invertebrado" :
    if y == "inseto" :
        if z == "hematofago" :
            print("pulga")
        elif z == "herbivoro" :
            print("lagarta")
        else:
            print ("Input tidak Valid ! ")
    elif y == "anelideo" :
        if z == "hematofago" :
            print("sanguessuga")
        elif z == "onivoro" :
            print("minhoca")
        else:
            print ("Input tidak Valid ! ")
    else:
        print ("Input tidak Valid ! ")
else:
    print ("Input tidak Valid ! ")