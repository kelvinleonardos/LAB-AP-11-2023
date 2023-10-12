def anagram(x,y):
    x = x.replace(" ","").lower()
    y = y.replace(" ","").lower()
    if sorted(x)==sorted(y):
        return True
    else :
        return False

x = input()
y = input()
print(anagram(x,y))