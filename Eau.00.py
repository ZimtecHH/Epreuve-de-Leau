#Créez un programme qui affiche toutes les
# différentes combinaisons possibles de
# trois chiffres dans l’ordre croissant,
# dans l’ordre croissant. La répétition est volontaire.

c1 = 0
c2 = 0
c3 = 0

while True:
 while c3 < 9 :
    c3 = c3 + 1
    print(c1,c2,c3)
    break
    c3 = 0
    if c3 < 9 :
        c3 = c3 + 1
    c2 = 1;
    print(c1, c2, c3)

if c1 == c2 and c2 == c3 and c1 == c3: #Cas des trois valeurs identiques
    print("Mauvaises valeurs x3")

    if c1 == c2 and c3 != c1 and c3 != c2 : #Cas de deux valeurs identiques
        print(c1, c2, c3)

    if c1 != c2 and c1!=c3 and c2 != c3 : #Cas quand toutes les valeurs sont différentes
        print(c1,c2,c3)
else:
    testeur = str(c1)+str(c2)+str(c3)
    print(testeur)
