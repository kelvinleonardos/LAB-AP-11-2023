print("Pengujian jenis karakter \n--------------------------")

karakter = input("Karakter: ")

kapital = karakter >= "A" and karakter <= "Z"
kecil = karakter >= "a" and karakter <= "z"
angka = karakter >= "1" and karakter <= "9"

print(f"Huruf Kapital? {kapital}")
print(f"Huruf Kecil? {kecil}")
print(f"Angka? {angka}")