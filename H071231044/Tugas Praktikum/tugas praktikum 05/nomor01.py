s1 = input()
s2 = input()[::-1]
s3_1 = (min(len(s1),(len(s2))))
s3 = ''
for i in range (s3_1):
    s3 = s3+s1[i]+s2[i]
if len(s1)>len(s2):
    s3 +=s1[s3_1:]
elif len(s1)<len(s2):
    s3 +=s2[s3_1:]

print(s3)
