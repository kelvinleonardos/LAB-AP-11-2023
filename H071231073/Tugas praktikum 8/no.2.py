import re

x = int(input('how many ip address? =  '))

v4 = r'^(([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
v6 = r'^(([0-9a-f]?[0-9a-f]?[0-9a-f]?[0-9a-f]?)\:){7}([0-9a-f]?[0-9a-f]?[0-9a-f]?[0-9a-f]?)'

ip = []
for i in range(x):
    z = str(input())
    ip.append(z)

for i in ip:
    z = re.match(v4,i)
    if z:
        print('IPv4')
    else:
        z = re.match(v6,i)
        if z:
            print('IPv6')
        else:
            print('not an ip address')