s  = input("Masukkan Kata : ")
s1 = (len(s)//2)
if len(s)%2 == 0:
    print(s[0]+s[s1-1]+s[s1]+s[-1])
else :
    print(s[0]+s[s1]+s[-1])
