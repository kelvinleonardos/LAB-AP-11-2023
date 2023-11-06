x = input('masukkan input pertama = ')

match x:
    case 'vertebrado':
        y = input('masukkan input kedua = ')
        match y:
            case 'ave':
                z = input('masukkan input ketiga = ')
                match z:
                    case 'carnivoro':
                        print('agui')
                    case 'onivoro':
                        print('pomba')
                    case _:
                        print('invalid input')
            case 'mamivero':
                z = input('masukkan input ketiga = ')
                match z:
                    case 'onivoro':
                        print('homem')
                    case 'herbivoro':
                        print('vaca')
                    case _:
                        print('invalid input')
            case _:
                print('invalid input')
    case 'invertebrado':
        y = input('masukkan input kedua = ')
        match y:
            case 'inseto':
                z = input('masukkan input ketiga = ')
                match z:
                    case 'hematofago':
                        print('pulga')
                    case 'herbivoro':
                        print('lagarta')
                    case _:
                        print('invalid input')
            case 'anelideo':
                z = input('masukkan input kedua = ')
                match z:
                    case 'hematofago':
                        print('sanguessuga')
                    case 'onivoro':
                        print('minhoca')
                    case _:
                        print('invalid input')
            case _:
                print('invalid input')
    case _:
        print('invalid input')