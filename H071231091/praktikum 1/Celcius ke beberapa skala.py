suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))

suhu_kelvin = suhu_celsius + 273.15
suhu_reamur = 0.8 * suhu_celsius
suhu_fahrenheit = (suhu_celsius * 9/5) + 32

print(f"Suhu dalam Kelvin: {int(suhu_kelvin)} K")
print(f"Suhu dalam Reamur: {int(suhu_reamur)} Reamur")
print(f"Suhu dalam Fahrenheit: {int(suhu_fahrenheit)} °F")
