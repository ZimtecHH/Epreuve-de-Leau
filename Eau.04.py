#Créez un programme qui affiche le premier
#nombre premier supérieur au nombre donné en argument

liste = [0]
# 1 not being a prime number, is ignored
liste[0] = int(input("Rentrer un chiffre : "))
while True :
    if liste[0] < 100 :
        liste[0] = liste[0] + 1
        print(liste)
        k = 13

        if liste[0] > 1:
            for i in range(2, int(liste[0] / 2) + 1):
                if (liste[0] % i) == 0:
                    print("It is not a prime number")
                    break
            else:
                print("It is a prime number")

        else:
            print("It is not a prime number")