#Créez un programme qui détermine
# si une chaîne de caractère se trouve dans une autre.

premiere_chaine = input("Entrez caractère : ")

if( premiere_chaine.isdigit()):
    print("Error")
    pass

deuxieme_chaine = input("entrez 4 chaine de caractère : ")

if( deuxieme_chaine.isdigit()):
    print("Error")
    pass

if deuxieme_chaine.startswith(premiere_chaine[:4]):
    print(True)

elif deuxieme_chaine.endswith(premiere_chaine[-4:]):
    print(True)

else:
    print(False)