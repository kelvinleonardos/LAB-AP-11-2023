# Encapsulation and Abstract class
class Hero:
    def __init__(self, nama, role):
        self.__nama = nama
        self.__role = role

    def show_info(self):
        pass  # Abstract method, to be implemented by subclasses

    def setNama(self, nama):
        self.__nama = nama

    def getNama(self):
        return self.__nama

    def setRole(self, role):
        self.__role = role

    def getRole(self):
        return self.__role

# Inheritance
class Tank(Hero):
    def __init__(self, nama):
        # Inheritance: Calling the constructor of the base class using super()
        super().__init__(nama, "Tank")

    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

# Inheritance
class Assassin(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Assassin")

    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

# Inheritance
class Fighter(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Fighter")

    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

# Inheritance
class Marksman(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Marksman")

    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

# Inheritance
class Mage(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Mage")

    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

# Inheritance
class Support(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Support")

    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

# Polymorphism
tank = Tank("Tigreal")
assassin = Assassin("Saber")
fighter = Fighter("Balmond")
marksman = Marksman("Lesley")
mage = Mage("Odette")
support = Support("Angela")

print("=" * 30)
# Utilizing polymorphism to display information about different types of heroes
tank.show_info()
assassin.show_info()
fighter.show_info()
marksman.show_info()
mage.show_info()
support.show_info()
print("=" * 30)
