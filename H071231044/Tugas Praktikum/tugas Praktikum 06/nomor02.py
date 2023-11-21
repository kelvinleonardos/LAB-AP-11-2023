a1 = input("Input array ke-1 : ").split()
a1 = [int(i)for i in a1]
a2 = input("Input array ke-2 : ").split()
a2 = [int(i)for i in a2]
a3 = set(a1)&set(a2)
if len(a3) == 1:
    print(f"terdapat {len(a3)} buah duplikat yaitu {a3.pop()}")
elif len(a3) > 1:
    a3 = tuple(a3)
    print(f"terdapat {len(a3)} buah duplikat yaitu {a3}")
else:
    print("Tidak Ada Duplikat Di Temukan")