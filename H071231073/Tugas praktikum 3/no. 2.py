x = int(input('harga = '))
y = int(input('uang yang dibayarkan = '))

z = y-x
print(f'kembalian asli = {z}')

q = z // 100000
print(f'100.000 sejumlah {q} lembar')

q = q * 100000
s = z - q
q = s // 50000
print(f'50.000 sejumlah {q} lembar')

q = q * 50000
s = s - q
q = s // 20000
print(f'20.000 sejumlah {q} lembar')

q = q * 20000
s = s - q
q = s // 10000
print(f'10.000 sejumlah {q} lembar')

q = q * 10000
s = s - q
q = s // 5000
print(f'5.000 sejumlah {q} lembar')

q = q * 5000
s = s - q
q = s // 2000
print(f'2.000 sejumlah {q} lembar')

q = q * 2000
s = s - q
q = s // 1000
print(f'1000 sejumlah {q} lembar')