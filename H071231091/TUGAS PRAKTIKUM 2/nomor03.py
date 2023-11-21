print("Menghitung Tagihan Listrik")

Golongan = input("Golongan = ")
Daya = int(input("Daya = "))
Pemakaian = int(input("Pemakaian = "))

R1 = 1352
R1_1 = 1444.70
B2 = 1444.70
R2 = 1699.53
R3 = 1699.53
B3 = 1114.74
I3 = 1314.12
P1 = 1523.28

match Golongan :
    case "R1":
        if Daya == 900 :
            T1 = R1*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T1:,.1f}".format(T1).replace(",","x").replace(".",",").replace("x","."))
        elif Daya == 1300 :
            T2 = R1_1*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T2:,.1f}".format(T2).replace(",","x").replace(".",",").replace("x","."))
        elif Daya == 2200 :
            T3 = R1_1*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T3:,.1f}".format(T3).replace(",","x").replace(".",",").replace("x","."))
        else :
            print ("Daya tidak valid !")
    case "R2":
        if Daya >= 3300 and Daya <= 5500 :
            T4 = R2*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T4:,.1f}".format(T4).replace(",","x").replace(".",",").replace("x","."))
        else :
            print ("Daya tidak valid !")
    case "R3":   
        if Daya >= 6600 :
            T5 = R3*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T5:,.1f}".format(T5).replace(",","x").replace(".",",").replace("x","."))
        else :
            print ("Daya Tidak Valid !")
    case "B2" :
        if Daya >= 6600 and Daya <= 200000 :
            T6 = B2*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T6:,.1f}".format(T6).replace(",","x").replace(".",",").replace("x","."))
    case "B3":   
        if Daya > 200000 :
            T7 = B3*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T7:,.1f}".format(T7).replace(",","x").replace(".",",").replace("x","."))
        else :
            print ("Daya Tidak Valid !")
    case "I3":   
        if Daya >= 200000 :
            T8 = I3*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp, {T8:,.1f}".format(T8).replace(",","x").replace(".",",").replace("x","."))
        else :
            print ("Daya Tidak Valid !")
    case "P1":   
        if Daya >= 6600 and Daya <= 200000 :
            T9 = P1*Pemakaian
            print(f"Jumlah tagihan anda sebesar : Rp,{T9:,.1f}".format(T9).replace(",","x").replace(".",",").replace("x","."))
        else :
            print ("Daya Tidak Valid !")
    case _:
        print ("Golongan tidak Valid !")