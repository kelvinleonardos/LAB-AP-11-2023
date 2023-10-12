# def stringPermutation(word):
#     if type(word) == str:
#         word_length = len(word)
#         if word_length < 2:
#             print(word)  # Output kata jika panjangnya kurang dari 2
#         else:
#             permutations = [word]  # Inisialisasi list dengan kata awal
#             for i in range(1, word_length):
#                 word = word[1:] + word[0]  # Geser karakter pertama ke posisi terakhir
#                 permutations.append(word)
#             result = " | ".join(permutations) + " | "
#             print(result)
#     else:
#         print("Error: Input harus berupa string")

# # Test Case 1
# stringPermutation("RADAR")

# # Test Case 2
# stringPermutation("Ayam")

# # Test Case 3 (Input yang tidak valid)
# stringPermutation(123)

# def Permutation(word):
#     try:
#         if len(word) < 2:
#             print(word + " | ")
#         else:
#             permutations = [word[i:] + word[:i] 
#             for i in range(len(word))]
#             result = " | ".join(permutations) + " | "
#             print(result)
#     except ZeroDivisionError :
#         return "error"

# # Test Case 1
# Permutation("mobil")

# # Test Case 2
# Permutation("ayam")

def nilalipermutasi(kata:str):
    try:
        permutasi = " "
        for i in range(len(kata)):
            berputar_kata = kata[-1] + kata[:-1]
            permutasi += berputar_kata + '|'
            kata = berputar_kata

        return permutasi
    
    except:
        return "data bukan merupakan string"
    
hasil1= nilalipermutasi (21212)
hasil2= nilalipermutasi ("ayam")
print(hasil1)
print(hasil2)


