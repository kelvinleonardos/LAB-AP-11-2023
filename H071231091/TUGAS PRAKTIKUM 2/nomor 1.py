print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
jenis_kelamin_pilihan = input("pilih sesuai gender anda ")

if jenis_kelamin_pilihan == "1":
    jenis_kelamin = "pria"
elif jenis_kelamin_pilihan == "2":
    jenis_kelamin = "wanita"

tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
berat_badan = float(input("Masukkan berat badan (kg): "))

tinggi_badan = tinggi_badan / 100  
bmi = berat_badan / (tinggi_badan ** 2)

if jenis_kelamin == "pria":
    if bmi < 18:
        keterangan = "Underweight"
    elif 18 <= bmi < 24:
        keterangan = "Normal"
    elif 24 <= bmi < 27:
        keterangan = "Overweight"
    else:
        keterangan = "Obesitas"
elif jenis_kelamin == "wanita":
    if bmi < 17:
        keterangan = "Underweight"
    elif 17 <= bmi < 24:
        keterangan = "Normal"
    elif 24 <= bmi < 28:
        keterangan = "Overweight"
    else:
        keterangan = "Obesitas"

print(f"Anda tergolong {keterangan} dengan BMI {bmi:.2f}")
