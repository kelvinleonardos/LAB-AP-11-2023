array1 = input("Input array 1: ").split(" ")
array1 = [int(i) for i in array1]
array2 = input("Input array 2: ").split(" ")
array2 = [int(i) for i in array2]

set1 = set(array1)
set2 = set(array2)

duplikat = tuple(set1 & set2)
jumlah = len(duplikat)

print(f"Terdapat {jumlah} buah duplikat yaitu {duplikat}")