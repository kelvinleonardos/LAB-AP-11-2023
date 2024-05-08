Angka = list(map(int, input('Masukkan beberapa angka: ').split(' ')))

genap = []
ganjil = []
bagi5 = []

for Num in Angka:
    if Num % 2 == 0:
        genap.append(Num)
    else:
        ganjil.append(Num)

    if Num % 5 == 0:
        bagi5.append(Num)

print(f'''
Angka Genap: {genap}
Angka Ganjil: {ganjil}
Angka yang habis dibagi 5: {bagi5}''')