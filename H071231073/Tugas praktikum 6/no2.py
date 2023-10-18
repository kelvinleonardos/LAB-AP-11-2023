x = input('array 1 = ').split()
y = input('array 2 = ').split()

x = set([int(i) for i in x])
y = set([int(i) for i in y])

z = (x&y)
if len(z) < 1:
    print('tidak terdapat angka duplikat')
else:
    print(f'terdapat {len(z)} buah duplikat yaitu {z}'.replace('{','(').replace('}',')'))