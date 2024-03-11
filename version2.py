
import fonctions
grille1=fonctions.initialiserGrille()
grille2=fonctions.initialiserGrille()

fonctions.placerBateaux5_joueur1(grille1)
fonctions.placerBateaux4_joueur1(grille1)
fonctions.placerBateaux31_joueur1(grille1)
fonctions.placerBateaux32_joueur1(grille1)
fonctions.placerBateaux2_joueur1(grille1)


fonctions.afficher_secrete(grille2)
#fonctions.placerBateaux5_joueur2(grille2)
fonctions.afficher_secrete(grille2)

#fonctions.placerBateaux4_joueur2(grille2)
fonctions.afficher_secrete(grille2)

#fonctions.placerBateaux31_joueur2(grille2)
fonctions.afficher_secrete(grille2)

#fonctions.placerBateaux32_joueur2(grille2)
fonctions.afficher_secrete(grille2)

fonctions.placerBateaux2_joueur2(grille2)
fonctions.afficher_secrete(grille2)

while not (fonctions.partieFinie(grille1) or fonctions.partieFinie(grille2)):
    print("votre grille : ")
    fonctions.tirer_joueur1(grille2)
    print("####################################")

    fonctions.afficher_secrete(grille2)
    print("####################################")

    print("grille de l'ennemi :")
    fonctions.afficher(grille1)
    print("####################################")
    fonctions.tirer_joueur2(grille1)
    print("####################################")


if (fonctions.partieFinie(grille2)):
    print("vous avez perdu, essayez une autre fois héro!")
else:
    print("vous avez gagné !!!!!! Mabrouk!")