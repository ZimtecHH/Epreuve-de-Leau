#Créez un programme qui affiche toutes les valeurs comprises
# entre deux nombres dans l’ordre croissant. Min inclus, max exclus.

Entier = input("Entrez les deux valeurs séparé par un espace : ")

Entier = Entier.split(" ")
# Conversion premier chiffre
Entier[0] = int(Entier[0])
# Conversion deuxième chiffre
Entier[1] = int(Entier[1])


if Entier[0] < Entier[1] :
    for i in range(Entier[0],Entier[1]):
        print(i)

if Entier[1] < Entier[0] :
    for i in range(Entier[1],Entier[0]):
        print(i)

