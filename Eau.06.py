# Créez un programme qui met en majuscule une lettre sur
# deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.
# 1 Majuscule sur deux
import copy
chaîne_de_caratère = input("Rentrez une chaîne de caractère : ")
deuxième_chaîne = copy.copy(chaîne_de_caratère)

print("Taille de la chaîne de caractère = %d" % len(chaîne_de_caratère))

int (len(deuxième_chaîne))

for i in range(len(deuxième_chaîne)):
    pair = i % 2 == 0
    if pair :

        # Convert everything to uppercase
        print(deuxième_chaîne.upper())

        print(chaîne_de_caratère[:i])