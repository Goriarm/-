production = 4
buildings = 1
army = 0
count_of_query = 1

while count_of_query <= production:
    print("что вы хотите создать армию или строение?")
    query = input()
    if query == "army":
        army += 1
        print("Вы построили армию, Милорд. Армия = ", army)
        count_of_query += 1
    elif query == "building":
        buildings += 1
        print("Вы построили строение, Милорд. Строения = ", buildings)
        count_of_query += 1
    else:
        print("Что, простите?! Вы можете построить еще", production - (count_of_query-1), "раза, Милорд")


print("buildings =", buildings)
print("army =", army)

