kata = input("Masukkan kata: ")

if len(kata) % 2 == 0:
    hasil = kata[0] + " " + kata[-1]
    print(hasil)
else:
    hasil = kata[0] + kata[len(kata) // 2] + kata[-1]
    print(hasil)