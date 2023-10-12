# Nomor 1

x = int(input("masukan nilai x (tinggi) : "))
y = int(input("masukan nilai y (alas) : "))
z = (x**2 + y**2)**0.5

L = x*y/2
K = x+y+z
print(f"luas permukaan {L:.2f}")
print(f"keliling {K:.2f}")