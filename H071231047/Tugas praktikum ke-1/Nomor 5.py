# Nomor 5

s = int(input("masukan jumlah detik : "))

hour = s//3600
minute = (s-(hour*3600))//60
second = (s-(hour*3600))-(minute*60)
print(f"{hour:02d}:{minute:02d}:{second:02d}")