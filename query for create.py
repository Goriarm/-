"""
делается запрос
выводится текст : что вы хотите создать армию или строение?

игрок пишет армию или строение

в армию или строение прибавляется единица

если продукция больше 2 то вопрос задается еще раз

в армию или строение прибавляется единица

если продукция больше 3 то вопрос задается еще раз

"""

"""
функция создания
"""

production = 4
buildings = 1
army = 0

if production >= 1:
    query1 = input("что вы хотите создать армию или строение?\n")
    if query1 == "army":
        army += 1
        print("Вы построили армию, Милорд. Армия = ", army)
    if query1 == "building":
        buildings += 1
        print("Вы построили строение, Милорд. Армия = ", buildings)

""" Если производство 2 или больше 
"""
if production >= 2:
    query2 = input("что вы хотите создать армию или строение?\n")
    if query2 == "army":
        army += 1
        print("Вы построили армию, Милорд. Армия = ", army)
    if query2 == "building":
        buildings += 1
        print("Вы построили строение, Милорд. Армия = ", buildings)

""" Если производство 3 или больше 
"""
if production >= 3:
    query3 = input("что вы хотите создать армию или строение?\n")
    if query3 == "army":
        army += 1
        print("Вы построили армию, Милорд. Армия = ", army)
    if query3 == "building":
        buildings += 1
        print("Вы построили строение, Милорд. Армия = ", buildings)

""" Если производство 4
"""
if production == 4:
    query3 = input("что вы хотите создать армию или строение?\n")
    if query3 == "army":
        army += 1
        print("Вы построили армию, Милорд. Армия = ", army)
    if query3 == "building":
        buildings += 1
        print("Вы построили строение, Милорд. Армия = ", buildings)


print("buildings =", buildings)
print("army =", army)