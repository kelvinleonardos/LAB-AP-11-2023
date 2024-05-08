from n1_class import Warrior, Assassin, Support

# Objek
warrior = Warrior("Rehan Wangsaff", 10)
assassin = Assassin("Asep Stroberi", 25)
support = Support("Rusdi Ngawi", 30)


# Memanggil Metode class Human
print(f'Position (before) : {warrior.get_position()}')   # sebelum
warrior.set_speed(5)
warrior.movement('r')
print(f'Position (after)  : {warrior.get_position()}')   # sesudah

print("-"*50)


# Memanggil Metode class Hero
print(f'Health (before)   : {assassin.get_health()}')    # sebelum
warrior.attack(assassin)
print(f'Health (after)    : {assassin.get_health()}')     # sesudah

print("-"*50)

# Memanggil Metode Spesial
# ------------------------- sebelum
print(f'Warrior (health)  : {warrior.get_health()}')
print(f'Support (speed)   : {support.Speed}')
support.special(warrior)
# ------------------------- sesudah
print(f'Warrior (health)  : {warrior.get_health()}')
print(f'Support (speed)   : {support.Speed}')