def maksimum(*angka):
    if not angka:
        return None

    maks = angka[0]
    for angka_terbesar in angka:
        if angka_terbesar > maks:
            maks = angka_terbesar
    return maks


input_angka = input("Masukkan beberapa angka (pisahkan dengan spasi): ")
angka = [int(x) for x in input_angka.split()]
terbesar = maksimum(*angka)

if terbesar is not None:
    print(f'>> {terbesar}')
else:
    print('Tidak ada angka yang dimasukkan.')