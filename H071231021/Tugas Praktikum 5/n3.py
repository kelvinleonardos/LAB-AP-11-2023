Kata1 = input('Masukkan kata pertama: ').replace(' ', '').lower()
Kata2 = input('Masukkan kata kedua: ').replace(' ', '').lower()

def anagram(Kata1, Kata2):
    if len(Kata1) != len(Kata2):
        return False

    for huruf in Kata1:
        if Kata1.count(huruf) != Kata2.count(huruf):
            return False
    return True

print(anagram(Kata1, Kata2))