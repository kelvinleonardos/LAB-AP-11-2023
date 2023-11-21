# Soal 1 : Mengecek dan memvalidasi sebuah string inputan dari user
import re

User = input("Input : ")

def validasi_string(string):
    pola = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
    cocok = re.match(pola, string)

    return bool(cocok)

    # if len(string) == 45:
    #     if cocok:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False
        
result = validasi_string(User)
print(result)

# 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
# 222222222222222222222222222222222222222213 57
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 1357
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1357