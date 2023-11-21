i =  0
while True:
    derajat = float(input('Masukkan Derajat: '))

    if 0 <= derajat < 360:
        break
    else: 
      print('Tidak Valid')
        
    i = i + 3


total_detik = derajat * 240  # Konve1

# if jam >= 24:
#     jam -= 24

sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

waktu = "{:02d}:{:02d}:{:02d}".format(int(jam), int(menit), int(detik))

if 0 <= jam <= 10:
    print('Selamat Pagi')
elif 11 <= jam <= 14:
    print('Selamat Siang')
elif 15 <= jam <= 17:
    print('Selamat Sore')
elif 18 <= jam < 23:
    print('Selamat Malam')

print(waktu)