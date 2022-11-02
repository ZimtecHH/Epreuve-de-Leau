#Créez un programme qui trie une liste de nombres.
# Votre programme devra implémenter
# l’algorithme du tri à bulle.

def tri_a_bulle():
    bulle = input("Rentrez vos valeurs : ")
    bulle = bulle.split(" ")
    bulle = sorted(bulle)
    bulle = print(bulle)
    return bulle

tri_a_bulle()