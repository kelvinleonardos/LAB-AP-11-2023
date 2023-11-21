import re

ipv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
ipv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

print("Input : ")
x = []
N = int(input())
for i in range (N) :
    i = input()
    x.append(i)

print("\nOutput : ")
for check in x :
    if re.match(ipv4,check):
        print("IPv4")
    elif re.match(ipv6,check):
        print("IPv6")
    else :
        print("Bukan IP Address")
