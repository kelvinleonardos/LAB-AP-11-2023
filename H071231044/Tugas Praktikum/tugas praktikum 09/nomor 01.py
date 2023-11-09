class Human:
    def __init__(self, name, pos_x=None):
        self.name = name
        self.__position = pos_x
        self._speed = None

    def setSpeed(self, speed):
        self._speed = speed
    def getSpeed(self):
        return self._speed

    def setPosition(self, pos_x=None):
        self.__position = pos_x
    def getPosition(self):
        return self.__position

    def movement(self, arah):
        if self.__position is not None and self._speed is not None:
            for i in arah :
                if i == "L":
                    self.__position -= self._speed
                    pos = self.getPosition() - self.getSpeed()
                    self.setPosition(pos)
                elif i == "R":
                    self.__position += self._speed
                    pos = self.getPosition() + self.getSpeed()
                    self.setPosition(pos)

class Hero(Human):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self.setSpeed(3)

    def setPower(self, power):
        self._power = power
    def getPower(self):
        return self._power

    def setArmor(self, armor):
        self._armor = armor
    def getArmor(self):
        return self._armor

    def setHealth(self, health):
        self._health = health
    def getHealth(self):
        return self._health

    def attack(self, target):
        self.target = target
        target_health = target.getHealth() - self.getPower()
        target.setHealth(target_health)


class Warrior(Hero):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self.setPower(26)
        self.setArmor(30)

    def special(self, target):
        self.target = target
        self.setArmor(45)
        self.setPower(32)
        health_target = target.getHealth() - self.getPower()
        target.setHealth(health_target)


class Assasin(Hero):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self.setPower(35)
        self.setSpeed(4)

    def special(self, target):
        self.target = target
        self.setSpeed(7)
        self.setPower(42)
        health_target = target.getHealth() - self.getPower()
        target.setHealth(health_target)

class Support(Hero):
    def __init__(self, name, pos_x=None):
        super().__init__(name, pos_x)
        self.setHealth(500)
        self.setArmor(8)
        self.setSpeed(4)

    def special(self, target):
        self.target = target
        self._speed = 6
        health_target = target.getHealth() + 150
        target.setHealth(health_target)


warrior = Warrior("bambang", pos_x=10)
assasin = Assasin("joko", pos_x=25)
support = Support("udin", pos_x=30)
print("health warrior (before) :", warrior.getHealth())
assasin.attack(warrior)
print("health warrior (after)  :", warrior.getHealth())

print("-"*30)

print("Warrior (health)       :", warrior.getHealth())
print("Support (speed)        :", support.getSpeed())

support.special(warrior)
print("Warrior health (after) :", warrior.getHealth())
print("Support speed (after)  :", support.getSpeed())

print("-"*30)

print("Assasin position (before) :", assasin.getPosition())
assasin.movement("LRRRR")
print("Assasin position now (L)  :", assasin.getPosition())
assasin.movement("R")
print("Assasin position now (R)  :", assasin.getPosition())
