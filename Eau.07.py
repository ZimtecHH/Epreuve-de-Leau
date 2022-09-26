#Créez un programme qui met en majuscule
# la première lettre de chaque mot d’une chaîne de caractères.
# Les autres lettres devront être en minuscules.
# Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.

Argument = input("Rentrez autant d'argument que vous voulez sans chiffre : ")

Division = Argument.split()

Majuscule = Argument[0:1].upper()  # première lettre majuscule

Minuscule = Argument[1:len(Argument)].lower() # le reste en minuscule

Argument = Argument[0:1].upper() + Argument[1:len(Argument)].lower()

print(Argument)