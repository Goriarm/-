armyBlack = int(15) #Power_of_army
armyWhite = int(30) #Power_of_army
if armyBlack > armyWhite:
    combat_loses = int(armyWhite / armyBlack * armyWhite)
    armyBlack = int(armyBlack - combat_loses)
    print(f'Черная армия победила. потери {combat_loses}. Бойцов в живых {armyBlack}')
    armyWhite = 0
if armyWhite > armyBlack:
    combat_loses = int(armyBlack / armyWhite * armyBlack)
    armyWhite = int(armyWhite - combat_loses)
    print(f'Белая армия победила. потери {combat_loses}. Бойцов в живых {armyWhite}')
    armyBlack = 0
if armyBlack == armyWhite:
    armyBlack = 0
    armyWhite = 0
    print('Потери обеих армии 100%')

print(armyBlack)
print(armyWhite)

armyBlack = armyBlack

# после чего происходит удаления класса этой армии