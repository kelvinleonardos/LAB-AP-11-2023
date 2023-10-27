import os
import datetime
import random

print("="*75)
print("Selamat Datang".center(75))
print("="*75)
nama = input("Masukkan Nama kasir : ")
print("="*75)
while True :
    print("pilih opsi : ")
    print("1. Transaksi baru")
    print("2. Cari Transaksi")
    print("3. Keluar")
    print("="*75)
    pilihan = int(input("Masukkan Opsi Pilihan : "))
    print("="*75)
    match pilihan :
        case 1 :
            b = []
            h = []
            j = []
            while True :
                b_1 = input("masukkan nama Produk : ")
                h_1 = int(input("Masukkan harga produk : "))
                j_1 = int(input("masukkan jumlah produk : "))
                b.append(b_1)
                h.append(h_1)
                j.append(j_1)
                print("="*75)
                pilih2 = input("Masukkan t untuk berhenti menambah : ")
                print("="*75)
                if pilih2 == "t":
                    to = []
                    for i in range(len(h)):
                        to.append(h[i]*j[i])
                    m = sum(to)
                    folder_path = "Invoices"
                    if not os.path.exists(folder_path)  :
                        os.mkdir(folder_path)
                    inisial = (nama[0]+nama[len(nama)//2]+nama[-1])
                    t = datetime.datetime.now()
                    acak = str(random.randint(100,999)).zfill(3)
                    time = t.strftime("%y%m%d%H%M")
                    times = t.strftime("%d/%m/%y %H:%M")
                    file_path = folder_path + "/" + inisial.upper() + time + acak + ".txt"
                    nama_file = inisial.upper() + time + acak
                    file_case = open(file_path, "w")
                    file_case.write(f"\n{'TOKO ABDUL'.center(75)}\n\n")
                    file_case.write(f"{'='*75}\n")
                    file_case.write(f"Nama kasir      : {nama}\n")
                    file_case.write(f"Waktu Transaksi : {times}\n")
                    file_case.write(f"{'='*75}\n")
                    file_case.write(f"\n{'Daftar Produk'.center(75)}\n\n")
                    file_case.write(f"{(65*'=').center(75)}\n")
                    file_case.write(f"{' '*5}| {'produk'.center(17)} | {'Harga'.center(14)} | {'Jumlah'.center(7)} | {'Total'.center(14)} | {' '*5}\n")
                    file_case.write(f"{(65*'=').center(75)}\n")
                    for w,x,y,z in zip(b,h,j,to) :
                        if len(w) > 17 :
                            w = w[:14]+"..."
                        file_case.write(f"{' '*5}| {w.ljust(17)} | {('Rp.'+str(x)).rjust(14)} | {str(y).center(7)} | {('Rp.'+str(z)).rjust(14)} | {' '*5}\n")
                    file_case.write(f"{(65*'-').center(75)}\n")
                    file_case.write(f"{' '*5}| {'Total'.ljust(45)}| {('Rp.'+str(m)).rjust(14)} | {' '*5}\n")
                    file_case.write(f"{(65*'=').center(75)}\n")
                    file_case.write(f"\n{'='*75}\n{'Terima Kasih Telah Berbelanja'.center(75)}\n{'='*75}")
                    file_case.close()
                    file_path2 = "trxHistory.txt"
                    if not os.path.exists(file_path2) :
                        file_case2 = open(file_path2,"w")
                        file_case2.write(f"{'='*70}\n| {'DAFTAR TRANSAKSI'.center(66)} |\n{'='*70} \n")
                        file_case2.write(f"| {'Waktu'.center(17)} | {'ID Transaksi'.center(20)} | {'Nominal Transaksi'.center(23)} |\n{'='*70}\n")
                        file_case2.close()
                    file_case2 = open(file_path2,"a")
                    file_case2.write(f"| {times.center(17)} | {nama_file.ljust(20)} | {('Rp.'+str(m)).rjust(23)} |\n{'='*70}\n")
                    file_case2.close()
                    print("TRANSAKSI BERHASIL".center(75))
                    print(f"{'='*75}\n")
                    break     
        case 2 :
            cari = input("Masukkan ID Transaksi : ")
            print("="*75)
            folder_path = "Invoices"
            file_read = folder_path + "/" + cari + ".txt"
            if not os.path.exists(file_read) :
                print(f"File ID {cari} tidak ada")
                print("="*75)
            else :
                read = open(file_read,"r")
                print(read.read())
            x = input("Tekan Apapun untuk Kembali : ")
            print("="*75)
        case 3 :
            print(f"Selamat Tinggal {nama}".center(75))
            print("="*75)
            break