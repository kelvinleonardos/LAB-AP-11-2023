class Human:
    def __init__(self, name, arah):
        self.name = name
        self.__arah = arah
        # self._speed = 0

    def perpindahanarah(self, arah):
        for i in arah:
            if i == 'l':
                self.__arah -= self._speed
            elif i == 'r':
                self.__arah += self._speed
            else:
                print('invalid input')

    def get_perpindahanarah(self):
        return self.__arah

class Hero(Human):
    def __init__(self,name, arah):
        super().__init__(name, arah)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target._health -= self._power
        return target._health

    def gethealth(self):
        return self._health
    def getspeed(self):
        return self._speed
    # def setarmor(self, armor):
    #     self._armor = armor
    def getarmor(self):
        return self._armor
    # def setpower(self, power):
    #     self._power = power
    def getpower(self):
        return self._power

class Warrior(Hero):
    def __init__(self, name, arah):
        super().__init__(name, arah)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._power = 45
        self._armor = 32
        target._health -= self._power

class Assassin(Hero):
    def __init__(self, name, arah):
        super().__init__(name, arah)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power

class Support(Hero):
    def __init__(self, name, arah):
        super().__init__(name, arah)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150

       
