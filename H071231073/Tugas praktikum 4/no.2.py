x = (input('x = '))
print(len(x))
a = 0
b = -1

for i in range(len(x)):
    if x[a] == x[b]:
        a = a+1
        b = b-1
        q = 1
    else:
        q = 0
        break
# x = print(*x,end='')
if q == 1:
    print(f'{x} adalah palindrom')
if q == 0:
    print(f'{x} bukan palindrome')




# R A D A R
# 1 2 3 4 5
# 0 1 2 3 4
#-5 -4 -3 -2 -1