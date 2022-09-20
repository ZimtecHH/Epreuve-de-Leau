#Créez un programme qui détermine
# si une chaîne de caractère se trouve dans une autre.

premiere_chaine = input("Entrez caractère : ")

deuxieme_chaine = input("Deuxième chaine de caractère : ")

if deuxieme_chaine == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" :
    print("Error")

elif premiere_chaine == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" :
    print("Error")

elif deuxieme_chaine.startswith(premiere_chaine[:4]):
    print(True)
elif deuxieme_chaine.endswith(premiere_chaine[-4:]):
    print(True)

else:
    print(False)