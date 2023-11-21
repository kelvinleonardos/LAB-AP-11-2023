input_1 = (input("Masukkan Input Pertama : "))
input_2 = (input("Masukkan Input Kedua : "))
input_3 = (input("Masukkan Input Ketiga : "))

match input_1, input_2, input_3:
    case "vertebrado", "ave", "carnivoro":
        hasil = "aguia"
    case "vertebrado", "ave", "onivoro":
        hasil = "pomba"
    case "vertebrado", "mamifero", "onivoro":
        hasil = "homem"
    case "vertebrado", "mamifero", "herbivoro":
        hasil = "vaca"
    case "invertebrado", "inseto", "hematofago":
        hasil = "pulga"
    case "invertebrado", "inseto", "herbivoro":
        hasil = "lagarta"
    case "invertebrado", "anelideo", "hematofago":
        hasil = "sanguessuga"
    case "invertebrado", "anelideo", "onivoro":
        hasil = "minhoca"
    case _ :
        hasil = "data tidak valid"
print(hasil)
