class Human:
    def __init__(self, name, pos):
        self.name = name
        self.__pos = pos
        self._speed = 0

    def move(self, arah):
        for i in arah:
            if i == 'l':
                self.__pos -= self._speed
            elif i == 'r':
                self.__pos += self._speed
            else:
                print('invalid input')

    def get_pos(self):
        return self.__pos
    
class Hero(Human):
    def __init__(self,name, pos):
        super().__init__(name, pos)
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

class Warrior(Hero):
    def __init__(self, name, pos):
        super().__init__(name, pos)
        self._power = 26
        self._armor = 30
    
    def special(self, target):
        self._power = 45
        self._armor = 32
        target._health -= self._power

class Assassin(Hero):
    def __init__(self, name, pos):
        super().__init__(name, pos)
        self._power = 35
        self._speed = 4
    
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power
    
class Support(Hero):
    def __init__(self, name, pos):
        super().__init__(name, pos)
        self._health = 500
        self._armor = 8
        self._speed = 4
    
    def special(self, target):
        self._speed = 6
        target._health += 150

warrior = Warrior("bambang", 10)
assassin = Assassin("joko", 25)
support = Support("udin", 30)

# sebelum
print("health (before attack)  :", warrior.gethealth())
assassin.attack(warrior)

# sesudah
print("health (after attack)   :", warrior.gethealth())
print('\nposisi awal  :', assassin.get_pos())
assassin.move("l")
print('posisi akhir :',assassin.get_pos(),'\n')
print("-"*20)
# sebelum
print("Warrior (health) : ", warrior.gethealth())
print("Support (speed)  : ",support.getspeed())
support.special(warrior)
# sesudah
print('\nafter support')
print("Warrior (health) :", warrior.gethealth())
print("Support (speed)  :",support.getspeed())