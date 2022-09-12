#Créez un programme qui affiche toutes
# les différentes combinaisons
# de deux nombre entre 00 et 99 dans l’ordre croissant.

list1 = [0,0]
list2 = [0,0]
list1[1] = 0
list1[0] = 0

while True :

    if list1[1] < 9 :
        list1[1] = list1[1] + 1
        print(list2, list1)


    if list1[0] < 9 and list1[1] == 9 :
        list1[1] = 0
        list1[0] = list1[0] + 1

