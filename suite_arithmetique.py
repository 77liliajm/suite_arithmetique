# programme suite arithmetique : exercice 3 de mon cours d'algorithmique
# but : conception d'un algorithme affichant les nb premiers termes de la suite et la somme des nb premiers termes de la suite
# date : 07/02/2025
# auteur : Lilia

# saisie des valeurs de la suite : le premier terme (u0), la raison (r) et le nombre de terme à gérer (nb)
"""uo = int(input("Entrez le premier terme de la suite = "))
r = int(input("Entrez la raison de la suite = "))
nb = int(input("Entrez le nombre de termes = "))

# initialisation de terme (qui démarre à u0)
terme = uo

# boucle pour afficher les nb premiers termes de la suite
for k in range (0, nb):
    print("u", k, " = ", terme)
    terme = terme + r

# boucle pour afficher la somme des nb premiers terme de la suite
somme = 0
for i in range (1, nb+1):
    somme = somme + i
print("la somme des nb premiers termes de la suite est égal à " + str(somme))"""

u0 = int(input("Entrez le premier terme de la suite = "))
r = int(input("Entrez la raison de la suite = "))
nb = int(input("Entrez le nombre termes de la suite = "))

terme = u0
somme = 0

for k in range (0, nb):
    print(f"u{k} = {terme}")
    somme += terme
    terme += r

print("la somme des termes de la suite = ", somme)
