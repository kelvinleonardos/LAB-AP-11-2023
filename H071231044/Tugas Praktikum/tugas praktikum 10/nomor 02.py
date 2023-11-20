class mobil :
    def __init__(self,merk,kecepatan,jarak) :
        self._merk = merk
        self._kecepatan = kecepatan
        self._jarak = jarak

    def get_merk(self):
        return self._merk

    def get_kecepatan(self):
        return self._kecepatan

    def get_jarak(self):
        return self._kecepatan


class BMW(mobil):
        def __init__(self,merk,kecepatan,jarak) :
            super().__init__(merk,kecepatan,jarak)
        def klakson(self):
            print("Bunyi Klakson : Rawr")

class Toyota(mobil):
        def __init__(self,merk,kecepatan,jarak) :
            super().__init__(merk,kecepatan,jarak)
        def klakson(self):
            print("Bunyi Klakson : Beep")

mbl1 = BMW("BMW",100,500)
print(f"Mobil {mbl1.get_merk} dengan kecepatan {mbl1._kecepatan} km/jam dapat bergerak sejauh {mbl1._jarak} km tanpa henti")
mbl1.klakson()
mbl2 = Toyota("Toyota",60,300)
print(f"Mobil {mbl2._merk} dengan kecepatan {mbl2._kecepatan} km/jam dapat bergerak sejauh {mbl2._jarak} km tanpa henti")
mbl2.klakson()