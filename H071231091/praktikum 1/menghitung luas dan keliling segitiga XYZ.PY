# Input sisi X dan Y
sisi_x = float(input("Masukkan panjang sisi X: "))
sisi_y = float(input("Masukkan panjang sisi Y: "))

# Hitung luas segitiga
luas_segitiga = 0.5 * sisi_x * sisi_y

# Hitung keliling segitiga
sisi_z = (sisi_x**2 + sisi_y**2)**0.5
keliling_segitiga = sisi_x + sisi_y + sisi_z

# Menampilkan hasil dengan dua angka di belakang koma
print(f"Luas Segitiga XYZ: {luas_segitiga:.2f}")
print(f"Keliling Segitiga XYZ: {keliling_segitiga:.2f}")
