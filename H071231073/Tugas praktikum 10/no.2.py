from abc import ABC, abstractmethod

class Kantin(ABC):
    def __init__(self, harga):
        self._harga = harga

    @abstractmethod
    def get_harga(self):
        pass

    @abstractmethod
    def set_harga(self, kupon):
        pass
x = Kantin(1000)
print(x.get_harga())
class Makanan(Kantin):
    def __init__(self, harga):
        super().__init__(harga)

    def get_harga(self):
        return self._harga

    def set_harga(self, kupon):
        self._harga -= (self._harga * kupon)

class Minuman(Kantin):
    def __init__(self, harga):
        super().__init__(harga)

    def get_harga(self):
        return self._harga

    def set_harga(self, kupon):
        self._harga -= (self._harga * kupon)

bakso = Makanan(10000)
teh = Minuman(5000)
print(bakso.get_harga())
bakso.set_harga(30/100)
print(bakso.get_harga())