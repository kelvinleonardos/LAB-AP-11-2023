import os, datetime, random

hdl = '='*50
print(f"{hdl}\n{('WELCOME').center(50)}\n{hdl}")
nm = input('nama kasir : ')
print(hdl)
nn = nm[0]+nm[len(nm)//2]+nm[-1]

def invoice(l):
    now = datetime.datetime.now()
    name = f"{nn.upper()}{now.strftime('%y%m%d%H%M%S')}{random.randint(100,999)}"
    fn = f"invoice/{name}.txt"

    if not os.path.exists('invoice'):
        os.mkdir('invoice')

    hdl = '-'*60
    hdll = '='*60
    with open(fn,'w') as f:
        f.write(f"{hdll}\n{('X SHOP').center(60)}\n{hdll}\n")
        f.write(f"id invoice    : {name}\n Nama kasir   : {nm}\n waktu       : {now.strftime('%d/%m/%y %H:%M')}\n{hdll}\n")
        f.write(f"{('Daftar Produk').center(60)}\n{hdl}\n")
        f.write(f"|{('Nama').center(14)}|{('Harga').center(13)}|{('Jumlah').center(12)}|{('Total').center(16)}|\n{hdll}\n")

        for i in l:
            p, h, j = i
            ht = f'Rp.{h*j}'
            h     = f'Rp.{str(h)}'
            if len(p) >14:
                p = f'{p[:11]}...'            
            f.write(f"|{p.ljust(14)}|{h.ljust(13)}|{str(j).center(12)}|{str(ht).ljust(16)}|\n{hdl}\n")

        t = sum([h * j for _, h, j in l])
        f.write(f"|{('Total.').ljust(41)}|Rp{str(t).ljust(14)}|\n{hdll}\n")
        f.write(f"{('TERIMA KASIH').center(60)}\n{hdll}\n")
    print(f'invoice telah dicetak dengan id : {name}\n{"="*50}\n')

    h = 'history.txt'

    if not os.path.exists(h):
        fh = open(h,'w')
        fh.write(f'{"="*70}\n| {("Daftar Transaksi").center(66)} |\n{"="*70}\n')
        fh.write(f"| {'Waktu'.center(17)} | {'ID Transaksi'.center(20)} | {'Nominal Transaksi'.center(23)} |\n{'-'*70}\n")
        fh.close()
    fh = open(h,"a")
    fh.write(f"| {now.strftime('%d/%m/%y %H:%M').center(17)} | {name.ljust(20)} | {('Rp.'+ str(t)).rjust(23)} |\n{'-'*70}\n")
    fh.close()
    return name

def search(inv):
    fn = f'invoice/{inv}.txt'

    if os.path.exists(fn):
        with open(fn, 'r') as f:
            print(f.read())
    else:
        print(f"({inv}) not found\n{hdl}\n")

while True:
    print(f'silahkan pilih opsi:\n1. Buat transaksi\n2. Cari transaksi\n3. Keluar\n{hdl}')
    x = input('input opsi : ')
    print(hdl)

    match x:
        case '1':
            l = []
            while True:
                p = input("Nama Produk    : ")
                h = float(input("Harga Produk   : "))
                j = int(input("Jumlah Produk   : "))

                l.append((p, h, j))

                while True:
                    n = input('tambahkan produk? (y/n)  : ').lower()
                    print(hdl)
                    if n == 'y' or n == 'n':
                        break
                if n == 'n':
                    break
            invoice(l)
        case '2':
            inv = input('enter transaction id   : ')
            search(inv)
        case '3':
            print(f"\n{hdl}\n{('Terima Kasih').center(50)}\n{hdl}")
            break
        case _:
            print(f'invalid input\n{hdl}\n')
