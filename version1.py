
import fonctions

print("#######################################################################")
print("############# Bienvenue dans ma Bataille Navale ############")
print("#######################################################################")
print("Vous jouez contre l'ordinateur : il a placé ses bateaux aléatoirement.")
print("Il dispose d’:")
print(" - 1 Porte-avion (5 cases)")
print(" - 1 Croiseur (4 cases)")
print(" - 1 Contre-torpilleur (3 cases)")
print(" - 1 Sous-marin (3 cases)")
print(" - 1 Torpilleur (2 cases)")
print("Règles :")
print(" - Les bateaux ne peuvent être disposés qu’horizontalement ou")
print("   verticalement, mais jamais en diagonale.")
print(" - Deux bateaux ne peuvent ni se chevaucher, ni être collés l’un à")
print("   l'autre.")
print("Prêt ? C'est parti, bonne chance ! ")

grille=fonctions.initialiserGrille()

fonctions.placerBateaux5_joueur1(grille)
fonctions.placerBateaux4_joueur1(grille)
fonctions.placerBateaux31_joueur1(grille)
fonctions.placerBateaux32_joueur1(grille)
fonctions.placerBateaux2_joueur1(grille)

fonctions.afficher(grille)
while(not fonctions.partieFinie(grille)):
    fonctions.tirer_joueur2(grille)
    fonctions.afficher(grille)
print("#######################################################################")
print("###################### Bravo, vous avez gagné !!! #####################")
print("#######################################################################")

