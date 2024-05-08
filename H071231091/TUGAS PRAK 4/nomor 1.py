

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


