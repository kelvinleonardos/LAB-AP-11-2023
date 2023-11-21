def mencarihuruftertentu(input_string):
    x=len(input_string)
    if x <= 3:
        return input_string
    else:
         huruftengah = x//2
         posisi = input_string[0] + input_string[huruftengah] + input_string[-1]
         return posisi

input_string = "meja"
print(mencarihuruftertentu(input_string))




