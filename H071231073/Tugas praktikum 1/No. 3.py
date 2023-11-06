import math  # ax**2 + bx + c = 0

print("a,b,c != 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

dis = b**2 - 4 * a * c  # menghitung diskriminan

if a == 0:  # kondisi a = 0
    print(" a tidak boleh = 0")

elif dis < 0:
    print("persamaan kuadrat tidak memiliki akar real")
else:
    x1 = (-b + (dis**0.5)) / (2 * a)  # hitung akar-akar persamaan kuadrat
    x2 = (-b - (dis**0.5)) / (2 * a)  # hitung akar-akar persamaan kuadrat

    print("x1 = {:.2f}".format(x1))
    print("x2 = {:.2f}".format(x2))
