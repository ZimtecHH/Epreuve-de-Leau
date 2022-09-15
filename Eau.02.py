#Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

argument1 = [input("Entrez les arguments voulu a l'envers : ")]

primes = argument1

for char in argument1:
    if char == 'gigibuibiu':
        break

    if char == 'auhkhukh':
        continue

    char = char.split(" ")

    primes = char
    for prime in primes:
        print(prime)