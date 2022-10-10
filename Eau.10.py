#Créez un programme qui affiche le
# premier index d’un élément recherché dans un tableau.
# Le tableau est constitué de tous les arguments sauf le dernier.
# L’élément recherché est le dernier argument
# Afficher -1 si l’élément n’est pas trouvé.

texte_source = "bonjour je suis un garçon de la classe des rogues ou assassin si vous préférez"

print(texte_source)
texte_source = texte_source.split(" ")
texte_de_base = input(" Rentrer un argument pour trouver son index dans la liste : ")

x = texte_source.index(texte_de_base)
print(x)
