def palindrom(kata: str)-> str :
    kata = kata.lower()
    if kata == kata[::-1]:
        print ("Palindrom")
    else :
        print ("Bukan Palindrom")

while True :
    kata = input("Masukkan Kata : ")
    palindrom(kata)

    if kata == "lol" :
        palindrom(kata)
        print ("Loop End")
        break