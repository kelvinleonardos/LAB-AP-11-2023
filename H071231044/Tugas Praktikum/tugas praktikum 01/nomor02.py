print("No.2")
#Buatlah Program yang bisa secara otomatis mengonversi suhu dari skala Celcius ke beberapa skala lain seperti kelvin, Reamur, dan Fahrenheit

print("Konversi Suhu dari celcius ke Kelvin, Reamur, dan Fahrenheit")
c = int(input("masukkan suhu dalam Celcius : "))

k = int(c+273.15)
r = int(c*4/5)
f = int(c*9/5+32)
print (f"Hasil konversi dari suhu {c} derajat celcius ke Kelvin adalah : {k}K")
print (f"Hasil konversi dari suhu {c} derajat celcius ke Reamur adalah : {r}R")
print (f"Hasil konversi dari suhu {c} derajat celcius ke Fahrenheit adalah : {f}F")