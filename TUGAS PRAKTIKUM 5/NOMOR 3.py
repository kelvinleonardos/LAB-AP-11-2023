
kata1=input('Masukkan Kata Pertama : ')
kata2=input('Masukkan Kata Kedua : ')

for huruf in kata1:
    hasil1=kata1.count(huruf)
    hasil2=kata2.count(huruf)
    if hasil1 == hasil2:
        continue
    else:
        print(False)
        break
if hasil1 == hasil2:
        print(True)   
      
    
