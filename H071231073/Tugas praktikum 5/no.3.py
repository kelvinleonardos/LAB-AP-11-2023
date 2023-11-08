x = input('kata pertama = ')
y = input('kata kedua = ')

x = x.lower()
y = y.lower()
x = sorted(x)
y = sorted(y)

z = ' '
if z in x:
    s = x.count(z)
    x = x[0+s:]
if z in y:
    s = y.count(z)
    y = y[0+s:]

if x == y:
    print('true')
else:
    print('false')