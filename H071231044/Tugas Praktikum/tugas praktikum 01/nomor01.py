print("No.1")
#Diketahui sebuah sebuah segitiga yang mempunyai sisi X, Y, dan Z. Buatlah program yang menghitung luas dan keliling segitiga XYZ!
print("Menghitung luas permukaan dan keliling segitiga")
x = int(input("masukkan nilai x (tinggi) : "))
y = int(input("masukkan nilai y (alas) : "))
z = (x**2 + y**2)**0.5

L = x*y/2
K = x+y+z
print (f"luas Permukaan {L:.2f}")
print (f"Keliling {K:.2f}")
# Keterangan :
# x = 23
# Y = 43
# Luas segitiga = 494.50
# Keliling Segitiga = 114.76

