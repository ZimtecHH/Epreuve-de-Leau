#Créez un programme qui détermine si
# une chaîne de caractères ne contient que des chiffres.
testeur = input("Chaine de caractère : ")

verification = testeur.isnumeric()
verification
if verification == False :
    print(verification)
    print("Cette chaine ne contient pas que des chiffres")

else:
    print(verification)
    print("Cette chaine ne contient que des chiffres")
