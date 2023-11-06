x = float(input('masukkan derajat kemiringan matahari = '))
z = 60*60*24 #detik dalam sehari = 86400 detik

x = x
z = (x/360) * z
z = z + 21600
print(f'jumlah detik = {z}')

j = int(z//3600)
m1 = (z - j * 3600) / 60
m2 = int(m1)
d = (m1 * 60) - (m2 * 60)
d = int(d)

if j < 6:
    print('subuh')
elif j < 12:
    print('selamat pagi')
elif j < 15:
    print('selamat siang')
elif j < 18:
    print('selamat sore')
else:
    print('selamat malam')
    
print(f"{(j):02}:{(m2):02}:{(d):02}")