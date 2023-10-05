

harga = int(input('Harga Barang: '))
uang = int(input('Uang: '))

kembalian = uang - harga  # Calculate the change

if kembalian >= 0:
    print('Kembalian Anda: ')
else:
    print('Uang Tidak Cukup')

uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
# jumlah = [0, 0, 0, 0, 0, 0, 0]

for i in uang_pecahan:
    a = 0
    if kembalian >= i:
        a = kembalian // i
        kembalian = kembalian % i
    print(f'{a} Uang sejumlah Rp.{i}')

# for i in range(len(jumlah)):
#         print(f'{jumlah[i]} Uang sejumlah Rp.{uang_pecahan[i]}')
        
