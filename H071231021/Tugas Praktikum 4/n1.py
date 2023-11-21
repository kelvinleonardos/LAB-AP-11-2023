def stringpermutation(Kata):
    try:
        permutasi = []
        n = len(Kata)
        for i in range(n):
            move = Kata[i:] + Kata[0:i]
            permutasi.append(move)
        print(' | '.join(reversed(permutasi)), '|')
    except TypeError:
        print('Terjadi Kesalahan: Input harus berupa string')

ketik = input("Masukkan kata: ")
stringpermutation(ketik)