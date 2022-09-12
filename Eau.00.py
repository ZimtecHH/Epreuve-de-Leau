#Créez un programme qui affiche toutes les
# différentes combinaisons possibles de
# trois chiffres dans l’ordre croissant,
# dans l’ordre croissant. La répétition est volontaire.

mylist = [0,0,0]
#premier = mylist[0]
#deuxième = mylist[1]
#troisième = mylist[2]

while True :
    if mylist[2] <= 9 :
        mylist[2] = mylist[2]+1

    if mylist[2] == 9 :
        mylist[2] = 0
        mylist[1] = mylist[1] + 1

    if mylist[1] == 9:
        mylist[0] = mylist[0] + 1
        mylist[1]= 0

    if mylist[1] == 9:
        mylist[0] = mylist[0] + 1

    if mylist[0] == 9 and mylist[1] == 9 and mylist[0] == 9:
        break

    if mylist[0] == mylist[1] - 1 and mylist[2] == mylist[1] + 1 :
        print(mylist)