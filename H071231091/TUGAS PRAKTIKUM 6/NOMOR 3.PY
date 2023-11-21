input_angka = (input("Masukkan beberapa angka: ")).split()

angka_genap = []
angka_ganjil = []
angka_habis_dibagi_5 = []

for angka in input_angka:
    angka  = int(angka)
    if angka % 2 == 0:
        angka_genap.append(angka)
    if angka % 2 != 0:
        angka_ganjil.append(angka)
    if angka % 5 == 0:
        angka_habis_dibagi_5.append(angka)

print("Angka Genap:", angka_genap)
print("Angka Ganjil:", angka_ganjil)
print("Angka yang habis dibagi 5:", angka_habis_dibagi_5)
