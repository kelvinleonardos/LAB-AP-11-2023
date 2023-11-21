def fibonacci(n):
    fib_1 = []
    a, b = 0, 1
    for j in range(n):
        fib_1.append(a)
        a, b = b, a + b
    return fib_1

n = int(input("Masukkan Bilangan : "))
hasil = fibonacci(n)
for i in hasil :
    print (i,end=" ")