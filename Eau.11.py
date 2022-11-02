#Créez un programme qui affiche la différence minimum absolue
# entre deux éléments d’un tableau constitué
# uniquement de nombres. Nombres négatifs acceptés.

nombre = input("Entrez nombre : ")

nombre_split = nombre.split(" ")

taille_de_la_liste = len(nombre_split)
for i in nombre_split:
    if i != 0:
        print(i)


print(taille_de_la_liste)

print(nombre_split)



