#Créez un programme qui met en majuscule
# la première lettre de chaque mot d’une chaîne de caractères.
# Les autres lettres devront être en minuscules.
# Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.

chaine_de_caractre = input("Entrez une chaîne de caratère : ")

Majuscule = chaine_de_caractre[0:1].upper()

Minuscule = chaine_de_caractre[1:len(chaine_de_caractre)].lower()

print(Majuscule+Minuscule)

