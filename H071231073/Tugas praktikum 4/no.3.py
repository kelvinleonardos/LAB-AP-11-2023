x = (input('x = '))
x = x.split(',')

try:
    def maks(x):
        a = x[0]
        for i in range(0, len(x)):
            if int(x[i]) > int(a):
                a = x[i]
        return a
    print(maks(x))
    print(5/0)
except ValueError:
    print('error')


x = [1,3,20,12,13,42,34,54]
print(maks(x))