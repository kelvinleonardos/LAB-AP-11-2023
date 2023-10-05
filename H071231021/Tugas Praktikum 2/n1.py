print("Pilih gender anda!")
print("1. Pria")
print("2. Wanita")

gender = input("= ")
tinggiBadan = float(input("Masukkan tinggi badan (cm): "))
beratBadan = float(input("Masukkan berat badan (kg): "))

tinggi = tinggiBadan / 100

BMI = beratBadan / tinggi**2

if gender == "1":
    if BMI < 18:
        print(f"Anda tergolong underweight dengan BMI {BMI:.2f}")
    elif BMI >= 18 and BMI < 24:
        print(f"Anda tergolong normal dengan BMI {BMI:.2f}")
    elif BMI >= 24 and BMI < 27:
        print(f"Anda tergolong overweight dengan BMI {BMI:.2f}")
    else:
        print(f"Anda tergolong obese dengan BMI {BMI:.2f}")
elif gender == "2":
    if BMI < 17:
        print(f"Anda tergolong underweight dengan BMI {BMI:.2f}")
    elif BMI >= 17 and BMI < 24:
        print(f"Anda tergolong normal dengan BMI {BMI:.2f}")
    elif BMI >= 24 and BMI < 28:
        print(f"Anda tergolong overweight dengan BMI {BMI:.2f}")
    else:
        print(f"Anda tergolong obese dengan BMI {BMI:.2f}")
else:
    print("Masukkan angka 1 atau 2 pada gender.")