a = int(input("Masukkan Jarak Cat A : "))
b = int(input("Masukkan Jarak Cat B : "))
c = int(input("Masukkan Jarak Mouse C : "))

def CatAndMouse(a, b, c):
    if abs(a - c) < abs(b - c):
        return "Cat A"
    elif abs(a - c) > abs(b - c):
        return 'Cat B'
    else:
        return 'Mouse C'
print(CatAndMouse(a, b, c))