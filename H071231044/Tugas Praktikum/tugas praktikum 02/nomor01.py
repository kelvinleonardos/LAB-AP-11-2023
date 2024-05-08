print("BMI Checker")
print("-----------------")

print("Pilih Gender Anda")
print("1.Pria")
print("2.Wanita")
x = int(input("= "))

tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))
bmi = berat / (tinggi/100)**2

match x :
    case 1 :
        if bmi < 18 :
            print(f"Anda tergolong underweight dengan BMI {bmi:.2f}")
        elif 18 <= bmi < 24 :
            print(f"Anda tergolong normal dengan BMI {bmi:.2f}")
        elif bmi >= 24 and bmi <= 26.9 :
            print(f"Anda tergolong overweight dengan BMI {bmi:.2f}") 
        elif bmi >= 27 :
            print(f"Anda tergolong obese dengan BMI {bmi:.2f}") 

    case 2 :
        if bmi < 17 :
           print(f"Anda tergolong underweight dengan BMI {bmi:.2f}")
        elif bmi >= 17 and bmi < 24 :
            print(f"Anda tergolong normal dengan BMI {bmi:.2f}")
        elif 24 <= bmi < 28 :
            print(f"Anda tergolong overweight dengan BMI {bmi:.2f}") 
        elif bmi >= 28 :
            print(f"Anda tergolong obese dengan BMI {bmi:.2f}") 
    case _:
        print ("Gender tidak valid !")