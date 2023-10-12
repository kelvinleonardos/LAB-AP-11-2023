# Nomor 3

a = float(input("a = "))
while a == 0:
    print("a tidak boleh 0")
    a = float(input("a = "))

b = float(input("b = "))
c = float(input("c = "))

x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
print(f"x1 = {x1:.2f}")

x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
print(f"x2 = {x2:.2f}")