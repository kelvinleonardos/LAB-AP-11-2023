def catAndMouse (catA, catB, mosC):
    A = abs(mosC-catA)
    B = abs(mosC-catB)

    if A < B :
        return "cat A"
    elif B < A :
        return "cat B"
    else :
        return "mouse"
    
A = int(input("Cat A : "))
B = int(input("Cat B : "))
C = int(input("Mouse : "))

Hasil = catAndMouse (A, B, C)
print (Hasil)