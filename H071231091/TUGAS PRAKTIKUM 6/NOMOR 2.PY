input1 = input("Input ke-1 : ").split()
input2 = input("Input ke-2 : ").split()

satu = [int(i) for i in input1 ]
dua = [int(i) for i in input2 ]

x = set(satu) & set(dua)
if len(x) == 1:
    print(f"Terdapat {len(x)} buah duplikat yaitu ({x.pop()})")
elif len(x) > 1:
    x = tuple(x)
    print(f"terdapat {len(x)}  buah duplikat yaitu {x} ")
else:
    print("Tidak ada duplikasi ditemukan.")
