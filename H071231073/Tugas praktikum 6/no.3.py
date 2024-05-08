x = [int(i)for i in (input().split())]
print('x = ',x)

a = []
b = []
c = []

for i in x:
    if i % 2 == 0:
        a.append(i)
    if i % 2 != 0: #else:
        b.append(i)
    if i % 5 == 0:
        c.append(i)

print(f'angka genap =  {a}')
print(f'angka ganil = {b}')
print(f'kelipatan 5 = {c}')