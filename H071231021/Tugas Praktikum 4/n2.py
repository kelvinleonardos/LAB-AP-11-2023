def palindrom(kata: str) -> str:
    kata = kata.replace(' ', '').lower()
    if kata == kata[::-1]:
        return 'Palindrom'
    else:
        return 'Bukan Palindrom'
    
while True:
    word = input('Masukkan Kata atau ketik "dahlah" untuk menghentikan program : ')
    if word == "dahlah":
        break
    else:
        print(palindrom(word))