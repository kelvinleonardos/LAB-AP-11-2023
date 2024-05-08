print("menghitung luas permukaan dan keliling segitiga")
x = float(input("panjang sisi X = "))
y = float(input("panjang sisi Y = "))

# z = sisi miring
z = (((x**2) + (y**2))) ** 0.5
print(f"sisi miring = {(z):.2f}")

# l = luas_segitiga
l = (x * y) / 2
print(f"Luas Permukaan = {(l)}")

# k = keliling segitiga
k = x + y + z
print(f"keliling segitiga = {(k)}")
