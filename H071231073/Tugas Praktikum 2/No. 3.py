# g = input('Golongan = ')
# d = float(input('Daya = '))
# p = float(input('Pemakaian = '))
g = 'B2'
d = 150000
p = 8914
# if g == 'R1':
#     if d == 900:
#         t = 1352
#     elif d == 1300:
#         t = 1444.70
#     elif d == 2200:
#         t = 1444.70
#     else:
#         print('invalid input')
#     x = p*t
#     print(x)
# else:
match g:
        case 'R1':
            if d == 900:
                t = 1352
            elif d == 1300:
                t = 1444.70
            elif d == 2200:
                t = 1444.70
            else:
                print('invalid input')
        case 'R2':
            if d >= 3500 and d <= 5500:
                t = 1699.53
            else:
                print('invalid input')
        case 'R3':
            if d >= 6600:
                t = 1699.53
            else:
                print('invalid input')
        case 'B2':
            if d >= 6600 and d <= 200000:
                t = 1444.70
            else:
                print('invalid input')
        case 'B3':
            if d >= 200000:
                t = 1114.74
            else:
                print('invalid input')
        case 'I3':
            if d >= 200000:
                t = 1314.12
            else:
                print('invalid input')
        case 'P1':
            if d >= 6600 and d <= 200000:
                t = 1523.28
            else:
                print('invalid input')
        case _:
            print('invalid input')
x = p*t
print(x)
    
print(f'jumlah tagihan anda sebesar = Rp. {x:,.1f}')
q = f'{x:,.1f}'
print(q.replace(".",",").replace(",","."))
print(q.replace(",","*").replace(".",",").replace("*","."))