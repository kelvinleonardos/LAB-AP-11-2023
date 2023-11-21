x = input("Masukkan beberapa angka : ").split()
x = [int(i)for i in x]
genap = [i for i in x if i%2 == 0]
ganjil = [i for i in x if i%2 != 0]
lima = [i for i in x if i%5 == 0]

print("Genap :", genap)
print("Ganjil :", ganjil)  
print("Angka yang habis di bagi 5 :", lima)