print("Selamat datang untuk memulai, silakan input data Anda:")
data = {
    "nama":input("Input nama : "),
    "umur":int(input("input umur: ")),
    "alamat": input("input alamat: ")
}

    
while True:
    if data["umur"].isnumeric():
        break
    data["umur"] = input("input ulang umur")

# Menu utama
while True:
    print("=" * 50)
    print(f"Selamat datang {data['nama']}, silakan pilih opsi:")
    print("=" * 50)
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("=" * 50)
    
    opsi = input("Input opsi: ")
    
    if opsi == "1":
        print("=" * 50)
        print("Data Anda adalah")
        print(f"Nama: {data['nama']}")
        print(f"Umur: {data['umur']}")
        print(f"Alamat: {data['alamat']}")
        print("=" * 50)
    elif opsi == "2":
        new_nama = input("Silakan input nama baru: ")
        data["nama"] = new_nama
        print("Data Anda berhasil diperbarui.")
        print("=" * 50)
    elif opsi == "3":
        new_umur = input("Silakan input umur baru: ")
        data["umur"] = new_umur
        print("Data Anda berhasil diperbarui.")
        print("=" * 50)
    elif opsi == "4":
        new_alamat = input("Silakan input alamat baru: ")
        data["alamat"] = new_alamat
        print("Data Anda berhasil diperbarui.")
        print("=" * 50)
    elif opsi == "5":
        print("=" * 50)
        print(f"Selamat Tinggal {data['nama']}")
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi 1-5.")
