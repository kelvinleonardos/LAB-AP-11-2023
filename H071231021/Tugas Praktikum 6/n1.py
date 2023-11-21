print("Selamat datang, untuk memulai silahkan masukkan data anda")

Nama = input("Input nama : ")
while True:
    Umur = input("Input umur : ")
    if Umur.isnumeric():
        break
Alamat = input("Input alamat : ")

Data = {
    "Nama" : Nama,
    "Umur" : Umur,
    "Alamat" : Alamat,
}

while True:
    print(f'''         
===================================================
Selamat datang {Data["Nama"]}, silahkan pilih opsi
===================================================
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar ''')
    
    print("===================================================")
    opsi = input("Input opsi : ")
    print("===================================================")

    if opsi == "1":
        print(f'''Data anda adalah
Nama = {Data["Nama"]}
Umur = {Data["Umur"]}
Alamat = {Data["Alamat"]}''')
    elif opsi == "2":
        nama_baru = input("Silahkan input nama baru : ")
        Data["Nama"] = nama_baru
        print("Data anda sukses diperbarui")
    elif opsi == "3":
        umur_baru = input("Silahkan input umur baru : ")
        Data["Umur"] = umur_baru
        print("Data anda sukses diperbarui")
    elif opsi == "4":
        alamat_baru = input("Silahkan input alamat baru : ")
        Data["Alamat"] = alamat_baru
        print("Data anda sukses diperbarui")
    elif opsi == "5":
        print(f"Selamat tinggal, {Data['Nama']}")
        break
    else:
        print("Opsi Invalid")