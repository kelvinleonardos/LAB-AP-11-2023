from abc import ABC, abstractmethod

class mobil(ABC) :
    def _init_(self,merk,kecepatan,jarak):
        self._merk = merk
        self._kecepatan = kecepatan
        self._jarak = jarak
    def info(self):
        print(f"mobil {self._merk} dengan kecepatan {self._kecepatan} km/jam dapat bergerak sejauh {self._jarak} km")
class bmw(mobil):
    def _init_(self,merk,kecepatan,jarak):
        super(). _init_(merk,kecepatan,jarak)
    def bensin(self):
        print("jenis bahan bakar : Premium")
class pajero(mobil):
    def _init_(self,merk,kecepatan,jarak):
        super(). _init_(merk,kecepatan,jarak)
    def bensin(self):
        print("jenis bahan bakar : Solar")
        
mobil1 = bmw("bmw",100,500)
mobil1.info()
mobil1.bensin()

mobil2 = pajero("pajero",120,600)
mobil2.info()
mobil2.bensin()