print('pilih gender anda \n1. Pria \n2. Wanita')
gender = input('= ')

cm = float(input('masukkan tinggi badan (cm) = '))
kg = float(input('masukkan berat badan (kg) = '))

m = cm / 100
print(f'tinggi badan dalam meter = {m}')

bmi = kg / (m**2)
print(bmi)

if gender == '1':
    if bmi < 18:
        x = 'underweight'
    elif bmi < 23.9:
        x = 'normal'
    elif bmi < 26.9:
        x = 'overweight'
    else:
        x = 'obese'
    print(f"anda tergolong {x} dengan BMI {bmi:.2f}")
elif gender == '2':
    if bmi < 17:
        x = 'underweight'
    elif bmi < 23.9:
        x = 'normal'
    elif bmi < 27.9:
        x = 'overweight'
    else:
        x = 'obese'
    print(f"anda tergolong {x} dengan BMI {bmi:.2f}")        
else:
    print('Invalid gender input')