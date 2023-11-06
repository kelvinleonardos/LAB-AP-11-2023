import re

ipv4 = r"^((25[0-5]|2[0-4][\d]|[01]?[\d]?[\d])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
ipv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

x = []
w = int(input("Input berapa IP Address yang ingin di cek : "))
for i in range (w) :
    i = input()
    x.append(i)

print("HASIL PENGECEKAN: ")
for check in x :
    if re.match(ipv4,check):
        print("IPv4")
    elif re.match(ipv6,check):
        print("IPv6")
    else :
        print("Bukan IP Address")

# 2001:db8:3333:4444:CCCC:DDD:EEEE:FFFF