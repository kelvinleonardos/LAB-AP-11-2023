while True:
   M = float(input())
   if 0 <= M < 360:
      break
   else:
      print('End Of File')
      

detik = int(M * 240) # 1 derajat sama dengan 4 menit (240 detik)

jam = detik // 3600 + 6
if jam >= 24:
   jam = jam % 24
menit = detik % 3600 // 60
detik = detik % 60

if 6 <= jam < 11:
   print('Selamat Pagi')
elif 11 <= jam < 15 :
   print('Selamat Siang')
elif 15 <= jam < 18:
   print('Selamat Sore')
else:
   print('Selamat Malam')

print(f'{jam:02}:{menit:02}:{detik:02}')