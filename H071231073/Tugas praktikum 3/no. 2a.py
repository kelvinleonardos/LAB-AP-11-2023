x = int(input("harga = "))
y = int(input("uang yang dibayarkan = "))

z = y - x
print(f'kembalian asli = {z}')

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500]

for i in pecahan:
        q = z // i
        z = z - q*i
        i = f'{i:,}'
        i = i.replace(',','.')
        print(f'\nRp.{i} sejumlah {q} lembar')
        print(f'sisa kembalian = {z}')