print("Selamat datang untuk memulai silahkan input data anda")
nama = input("Masukkan Nama : ")
while True :
    umur = input("Masukkan Umur : ")
    if umur.isnumeric():
        break
    else :
        print("Invalid! Masukkan selain string !")
alamat = input("Masukkan alamat : ")
data = {
    "nama" : nama,
    "umur" : umur,
    "alamat" : alamat
}
while True :
    print("="*100)
    print(f"Selamat datang {data['nama']} silahkan pilih opsi")
    print("="*100)
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*100)
    op = int(input("Input Opsi : "))
    print("="*100)
    match op :
        case 1 :
            print (f"Data Anda adalah \nNama : {data['nama']} \nUmur : {data['umur']} \nAlamat : {data['alamat']}")
        case 2 :
            data["nama"]=input("Masukkan Nama Baru : ")
            print("Data anda sukses di perbaharui")
        case 3 :
            while True :
                    umur = input("Masukkan data umur baru : ")
                    if umur.isnumeric():
                        break
                    else :
                        print("Invalid! Masukkan selain string !")
            data["umur"]=umur
            print("Data anda sukses di perbaharui")
        case 4 :
            data["alamat"]=input("Silahkan input alamat baru : ")
            print("Data anda sukses di perbaharui")
        case 5 :
            print(f"Selamat Tinggal {data['nama']}")
            print("="*100)
            break
        case _ :
            print("Input Diluar Opsi")