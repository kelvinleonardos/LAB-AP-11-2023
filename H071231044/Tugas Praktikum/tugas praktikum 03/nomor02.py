print("Menghitung Kembalian Uang")
print("-------------------------")

harga = int(input("Masukkan Harga Barang : "))
uang = int(input("Masukkan Nominal Pembayaran : "))
kembalian = uang - harga

if kembalian >= 100000 :
    a = kembalian // 100000
elif kembalian < 100000 :
    a = 0
print (f"{a} uang sejumlah Rp. 100000")
kembalian %= 100000


if kembalian >= 50000 :
    a = kembalian // 50000
elif kembalian < 50000 :
    a = 0
print (f"{a} uang sejumlah Rp. 50000")
kembalian %= 50000

if kembalian >= 20000 :
    a = kembalian // 20000
elif kembalian < 20000 :
    a = 0
print (f"{a} uang sejumlah Rp. 20000")
kembalian %= 20000

if kembalian >= 10000 :
    a = kembalian // 10000
elif kembalian < 10000 :
    a = 0
print (f"{a} uang sejumlah Rp. 10000")
kembalian %= 10000

if kembalian >= 5000 :
    a = kembalian // 5000
elif kembalian < 5000 :
    a = 0
print (f"{a} uang sejumlah Rp. 5000")
kembalian %= 5000

if kembalian >= 2000 :
    a = kembalian // 2000
elif kembalian < 2000 :
    a = 0
print (f"{a} uang sejumlah Rp. 2000")
kembalian %= 2000


if kembalian >= 1000 :
    a = kembalian // 1000
elif kembalian < 1000 :
    a = 0
print (f"{a} uang sejumlah Rp. 1000")
kembalian %= 1000

if kembalian >= 500 :
    a = kembalian // 500
elif kembalian < 500 :
    a = 0
print (f"{a} uang sejumlah Rp. 500")
kembalian %= 500

if kembalian >= 200 :
    a = kembalian // 2000
elif kembalian < 200 :
    a = 0
print (f"{a} uang sejumlah Rp. 200")
kembalian %= 200

if kembalian >= 100 :
    a = kembalian // 100
elif kembalian < 100 :
    a = 0
print (f"{a} uang sejumlah Rp. 100")
kembalian %= 100
