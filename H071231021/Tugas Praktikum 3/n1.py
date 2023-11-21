Suku = int(input())
n1 = 0
n2 = 1
s = 0

if Suku > 0 :
    while s < Suku :
        print(n1, end=" ")
        Un = n1 + n2
        n1 = n2
        n2 = Un
        s += 1        
elif Suku == 1:
    print(n1)
else:
    print('Input Bilangan Positif')