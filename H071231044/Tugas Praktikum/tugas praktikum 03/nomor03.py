while True :
    Derajat = float(input("Masukkan Sudut : "))
    s = int((Derajat+90) / 360 * 24 * 3600 )
    if s >= 86400 :
        s = (s-86400)
    Hour = (s)//3600
    Minute = (s-(Hour*3600))//60
    Second = (s-(Hour*3600)-(Minute*60))
    Hasil = (f"{Hour:02d}:{Minute:02d}:{Second:02d}")

    if Derajat < 0 or Derajat > 360 : 
        print ("Error !")

    else :
        if 0 <= Derajat < 75 or 345 <= Derajat <= 360 :
            print("Selamat Pagi")
        elif 75 <= Derajat < 135:
            print("Selamat Siang")
        elif 135 <= Derajat < 195 :
            print("Selamat Sore")
        elif 195 <= Derajat < 345 :
            print("Selamat Malam")
        print(Hasil)

    if b == 10 :
        break