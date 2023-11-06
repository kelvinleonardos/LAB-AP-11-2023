x = (input('x = '))
print('\n',x)
print('\n')

try:
    y = -1
    for i in x:
        print(x[y:len(x)],end='')
        print(x[0:(len(x)+y)], end=' | ')
        y = y - 1
except:
    print("something error")

#  M  I  L  O 
#  0  1  2  3  4 #indeks 0
# -4 -3 -2 -1  #indeks minus
# len(x) = 4

# print(*x[-1:len(x)], end=' ')
# print(*x[0:3],end=' | ')

# print(*x[-2:len(x)],end=' ')
# print(*x[0:2],end=' | ')

# print(*x[-3:len(x)],end=' ')
# print(*x[0:1],end=' | ')

# print(*x[-4:len(x)])

# while True:
# 	try:
# 		x = list(input('x = '))
# 		print('\n', x)
# 		print('\n')
# 		y = -1
		
# 		for i in x:
# 			print(*x[y:len(x)],end=' ')
# 			print(*x[0:(len(x)+y)], end=' | ')
# 			y = y - 1
# 	except:
# 		print("error")