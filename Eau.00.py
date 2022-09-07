#Créez un programme qui affiche toutes les
# différentes combinaisons possibles de
# trois chiffres dans l’ordre croissant,
# dans l’ordre croissant. La répétition est volontaire.

c1 = 0
c2 = 0
c3 = 0


while True :

    if c1 == c2 and c2 == c3 and c1 == c3: #Cas des trois valeurs identiques
        while c3 in range(9) :
            c3 = c3 + 1
            print(c1, c2, c3)


    if c1 == c2 and c3 != c1 and c3 != c2 : #Cas de deux valeurs identiques
        while c2 in range(9) :
            c3 = 0
            c2 = c2 + 1
            print(c1, c2, c3)
        while c1 in range(9) :
            c3 = 0
            c2 = 0
            c1 = c1 + 1
            print(c1, c2, c3)
    break

    if c1 != c2 and c1!=c3 and c2 != c3 : #Cas quand toutes les valeurs sont différentes
        c1 = c1 + 1
        c2 = c2 + 1
        c3 = c3 + 1
    print(c1,c2,c3)
else:
    testeur = str(c1)+str(c2)+str(c3)
    print(testeur)
