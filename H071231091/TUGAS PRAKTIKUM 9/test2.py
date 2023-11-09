from nomor1 import Warrior, Assassin, Support

warrior = Warrior("masha", 10)
assassin = Assassin("luo yi", 25)
support = Support("floryn", 30)

# sebelum
print("health (before attack):", warrior.gethealth())
assassin.attack(warrior)
# sesudah
print("health (after attack):", warrior.gethealth())
print("-"*20)
# sebelum
print("Warrior (health): ", warrior.gethealth())
print("Support (speed) : ",support.getspeed())
support.special(warrior)
# sesudah
print("Warrior (health):", warrior.gethealth())
print("Support (speed) :",support.getspeed())


print("UNTUK PERPINDAHAN")
print('\nposisi awal:', assassin.get_perpindahanarah())
assassin.perpindahanarah('llllgghhjr')
print('posisi akhir:',assassin.get_perpindahanarah(),'\n')



