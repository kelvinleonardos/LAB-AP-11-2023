x = (input('x = '))
print(len(x))

def palindrom(x: str) ->str:
    a = 0
    b = -1
    for i in range(len(x)//2):
        if x[a] == x[b]:
            a = a+1
            b = b-1
            return 'palindrom'
        else:
            return 'bukan palindrom'
        break
        
print(f'{x} adalah {palindrom(x)}')

# R A D A R
# 1 2 3 4 5
# 0 1 2 3 4