pertama = input("Masukkan input pertama: ")
kedua = input("Masukkan input kedua: ")
ketiga = input("Masukkan input ketiga: ")

match pertama, kedua, ketiga:
    case "vertebrado", "ave", "carnivoro":
        print("aguia")
    case "vertebrado", "ave", "onivoro":
        print("pomba")
    case "vertebrado", "mamifero", "onivoro":
        print("homem")
    case "vertebrado", "mamifero", "herbivoro":
        print("vaca")
    case "invertebrado", "inseto", "hematofago":
        print("pulga")
    case "invertebrado", "inseto", "herbivoro":
        print("lagarta")
    case "invertebrado", "anelideo", "hematofago":
        print("sanguessuga")
    case "invertebrado", "anelideo", "onivoro":
        print("minhoca")
    case _:
        print("Invalid input")