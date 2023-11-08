x = input('masukkan input pertama = ')

if x == 'vertebrado':
        y = input('masukkan input kedua = ')
        if y == 'ave':
            z = input('masukkan input ketiga = ')
            if z == 'carnivoro':
                  print('agui')
            if z == 'onivoro':
                  print('pomba')
            else:
                 print('invalid input')
        elif y != 'ave':
            if y == 'mamivero':
               z = input('masukkan input ketiga = ')
               if z == 'onivoro':
                  print('homem')
               if z == 'herbivoro':
                  print('vaca')
               else:
                    print('invalid input')
        else:
             print('invalid input')

elif x == 'invertebrado':
        y = input('masukkan input kedua = ')
        if y == 'inseto':
            z = input('masukkan input ketiga = ')
            if z == 'hematofago':
                  print('pulga')
            if z == 'herbivoro':
                  print('lagarta')
            else:
                 print('invalid input')
        elif y != 'inseto':
            if y == 'anelideo':
               z = input('masukkan input kedua = ')
               if z == 'hematofago':
                  print('sanguessuga')
               if z == 'onivoro':
                  print('minhoca')
               else:
                    print('invalid input')
        else:
             print('invalid input')

else:
      print('invalid input')