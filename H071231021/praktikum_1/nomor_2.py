celcius = float(input("Masukkan derajat celcius: "))

fahrenheit = int(9/5 * celcius) + 32
kelvin = int(273 + celcius)
reamur = int(4/5 * celcius)

print(f"Hasil konversi dari {celcius}°C ke fahrenheit adalah {fahrenheit}°F")
print(f"Hasil konversi dari {celcius}°C ke kelvin adalah {kelvin}K")
print(f"Hasil konversi dari {celcius}°C ke reamur adalah {reamur}°R")