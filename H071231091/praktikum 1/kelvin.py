# Meminta input dari pengguna
a = float(input("Masukkan nilai a (a ≠ 0): "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

# Memeriksa apakah a tidak sama dengan 0
if a == 0:
    print("Nilai a tidak boleh sama dengan 0.")
else:
    # Menghitung diskriminan
    discriminant = b**2 - 4*a*c
    
    # Memeriksa tanda diskriminan
    if discriminant > 0:
        # Dua solusi nyata berbeda
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        print(f"Soluusi x1: {x1:.2f}")
        print(f"Soluusi x2: {x2:.2f}")
    elif discriminant == 0:
        # Satu solusi nyata (solusi ganda)
        x1 = -b / (2*a)
        print(f"Soluusi x1 dan x2 (solusi ganda): {x1:.2f}")
    else:
        # Tidak ada solusi nyata
        print("Tidak ada solusi nyata untuk persamaan ini.")
