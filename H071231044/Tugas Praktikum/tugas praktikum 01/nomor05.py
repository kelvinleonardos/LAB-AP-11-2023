print("No.5")
print("Konversi Detik ke Jam")
s = int(input("masukkan jumlah detik : "))

Hour = s//3600
Minute = (s-(Hour*3600))//60
Second = (s-(Hour*3600)-(Minute*60))
print(f"{Hour:02d}:{Minute:02d}:{Second:02d}")