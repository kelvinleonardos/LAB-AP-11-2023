# Nomor 1

print("Pilih gender anda")
print("1. Pria")
print("2. Wanita")
x = int(input("masukkan gender anda = "))

tinggi = float(input("masukan tinggi badan : "))
berat = float(input("masukan berat badan : "))
bmi = berat / (tinggi/100)**2

if x == 1:
    if bmi < 18:
        print(f"Anda tergolong underweight dengan BMI {bmi:.2f}")
    elif 18 <= bmi < 24:
        print(f"Anda tergolong normal dengan BMI {bmi:.2f}")
    elif 24 <= bmi < 27:
        print(f"Anda tergolong overweight dengan BMI {bmi:.2f}")
    elif bmi >= 27:
        print(f"Anda tergolong obese dengan BMI {bmi:.2f}")
elif x == 2:
    if bmi < 17:
        print(f"Anda tergolong underweight dengan BMI {bmi:.2f}")
    elif 17 <= bmi < 24:
        print(f"Anda tergolong normal dengan BMI {bmi:.2f}")
    elif 24 <= bmi < 28:
        print(f' Anda tergolong overweight dengan BMI {bmi:.2f}')
    elif bmi >= 28:
        print(f"Anda tergolong obese dengan BMI {bmi:.2f}")