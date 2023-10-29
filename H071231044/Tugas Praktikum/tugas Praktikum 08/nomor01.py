import re
t = input("Masukkan kata : ")
p = r"[a-zA-Z02468]{40}[13579\s]{5}"
r = re.fullmatch(p,t)
if r :
    print (True)
else :
    print (False)

# t = "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"
# t = "x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779"
