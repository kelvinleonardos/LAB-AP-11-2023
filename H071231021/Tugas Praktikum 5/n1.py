kata1 = input("kata1 = ").replace(" ", "")
kata2 = input("kata2 = ").replace(" ", "")[::-1]
kata3 = ""
p = min(len(kata1), len(kata2))

for i in range(p):
    acak = kata1[i] + kata2[i]
    kata3 += acak

kata3 += kata1[p:] + kata2[p:]

print(f'Hasil acak = "{kata3}"')