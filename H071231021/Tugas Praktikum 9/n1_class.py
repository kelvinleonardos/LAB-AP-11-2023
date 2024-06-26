import os
os.system("cls")

# Class Race - Grandparent
class Human:
    def __init__(self, name, pos_x):
        self.Name = name
        self.__Position = int(pos_x)
        self._Speed = 0

    # --------------- Method Movement
    def movement(self, arah):
        for i in arah:
            if i == 'l':
                self.__Position -= self._Speed
            elif i == 'r':
                self.__Position += self._Speed
            else:
                print("Invalid Input")

    # Getter    
    def get_position(self):
        return self.__Position
    def get_speed(self):
        return self._Speed
    
    # Setter
    def set_position(self, position):
        self.__Position = position
    def set_speed(self, speed):
        self._Speed = speed

# Class Hero - Parent
class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._Power = 15
        self._Health = 400
        self._Armor = 15
        self._Speed = 3

    # --------------- Method Attack
    def attack(self, target):
        target._Health -= self._Power

    # Getter
    def get_power(self):
        return self._Power
    def get_health(self):
        return self._Health
    def get_armor(self):
        return self._Armor
    def get_speed(self):
        return self._Speed

    # Setter
    def set_power(self, power):
        self._Power = power
    def set_health(self, health):
        self._Health = health
    def set_armor(self, armor):
        self._Armor = armor  
    def set_speed(self, speed):
        self._Speed = speed

# Class Role - Child
class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._Power = 26
        self._Armor = 30

    # --------------- Method Special
    def special(self, target):
        self.set_power(32)
        self.set_armor(45)
        target._Health -= self._Power

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._Power = 35
        self.Speed = 4

    # --------------- Method Special
    def special(self, target):
        self.Speed = 7
        self.set_power(42)
        target._Health -= self._Power

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._Health = 500
        self._Armor = 8
        self.Speed = 4

    # --------------- Method Spesial
    def special(self, target):
        self.Speed = 6
        target._Health += 150