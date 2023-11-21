def palindrome(word: str)-> str:
    
    if word == word[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

x = input("Masukkan sebuah kata: ")
print(palindrome(x))

# z = palindrome (x)
# print(z)
