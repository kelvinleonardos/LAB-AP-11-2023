# CARA 1: Menggunakan Fungsi abs()
def catAndMouse(catA, catB, mosC):
    A = abs(mosC - catB)
    B = abs(mosC - catA)

    if A > B :
        return "Cat A"
    elif B > A :
        return "Cat B"
    else:
        return "Mouse C"

try:
    catA = int(input('Cat A : '))
    catB = int(input('Cat B : '))
    mosC = int(input('Mouse C : '))
    print(catAndMouse(catA=catA, catB=catB, mosC=mosC))
except:
    print("Masukkan angka saja")