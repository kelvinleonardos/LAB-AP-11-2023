# Soal 2 : Mengecek apakah sebuah inputan merupakan IPv4, IPv6 atau bukan keduanya
import re

def IPv4(teks):
    pola = r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    cocok = re.match(pola, teks)

    if cocok:
        return True
    else:
        return False
    
def IPv6(teks):
    pola = r'^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}$'
    cocok = re.match(pola, teks)

    return True if cocok else False

def IP_check(teks):
    for i in teks:
        if IPv4(i):
            print('IPv4')
        elif IPv6(i):
            print('IPv6')
        else:
            print('Bukan IP Address')

n = int(input('Banyak Baris : '))

teks1 = []
for i in range(n):
    teks1.append(input())

print()
IP_check(teks1)

# 121.203.197.20
# 260.260.260.260
# 2001:0db8:0000:0000:0000:ff00:0042:8329