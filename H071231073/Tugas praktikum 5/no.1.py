x = 'Abc'
y = 'Xyz123'
y = ''.join(reversed(y)) #321zyX

z = y[len(x):] #321
for i in range(len(x)):
    print(x[i],end='')
    print(y[i],end='')

print(y[len(x):])