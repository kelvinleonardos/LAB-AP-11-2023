n = int(input("Masukkan jumlah suku Fibonacci yang ingin dijumlahkan: "))
a, b = 0, 1

if n <= 0 :
    print("invalid")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
