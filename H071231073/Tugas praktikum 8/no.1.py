import re

x = input('x = ')
p = r'^[a-zA-Z24680]{40}[13579\s]{5}$'
z = re.match(p,x)
print(bool(z))