print('Selamat datang, untuk memulai program silahkan input data anda')
x = input('Nama     = ')
while True:
    y = input('umur     = ')
    if y.isnumeric():
        break

z = input('alamat   = ')

b = "="*55

def data(x, y, z):
    a = {'nama': x, 'umur': y, 'alamat': z}


    c = 'selamat datang ' + a['nama']+ ', silahkan pilih opsi'
    print('\n'+b+'\n'+c+'\n'+b)
    print('1. Detail anda\n2. ubah nama\n3. ubah umur\n4. ubah alamat\n5. keluar')
    
    i = input(f'\n{b}\nInput opsi : ')
    print(b)
    match i:
        case '1':
            def detail():
                print('berikut adalah data anda')
                for i in a:
                    print(f'{i} : {a[i]}')
                data(x,y,z)
            detail()
        case '2':
            def nama():
                x = input('ubah nama = ')
                data(x,y,z)
            nama()
        case '3':
            def umur():
                y = input('ubah umur = ')
                data(x,y,z)
            umur()
        case '4':
            def alamat():
                z = input('ubah alamat = ')
                data(x,y,z)
            alamat()
        case '5':
            print('program berakhir')
        case _:
            print('invalid input')

data(x,y,z)