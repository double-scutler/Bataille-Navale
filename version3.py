
import fonctions

#joueur 1 est l'ordinateur
#joueur 2 est l'utilisateur

grille1=fonctions.initialiserGrille()
grille2=fonctions.initialiserGrille()

fonctions.placerBateaux5_joueur1(grille1)
fonctions.placerBateaux4_joueur1(grille1)
fonctions.placerBateaux31_joueur1(grille1)
fonctions.placerBateaux32_joueur1(grille1)
fonctions.placerBateaux2_joueur1(grille1)

fonctions.placerBateaux5_joueur2(grille2)
fonctions.afficher_secrete(grille2)
fonctions.placerBateaux4_joueur2(grille2)
fonctions.afficher_secrete(grille2)
fonctions.placerBateaux31_joueur2(grille2)
fonctions.afficher_secrete(grille2)
fonctions.placerBateaux32_joueur2(grille2)
fonctions.afficher_secrete(grille2)
fonctions.placerBateaux2_joueur2(grille2)
fonctions.afficher_secrete(grille2)

resultat=[(0,0),1]
while not (fonctions.partieFinie(grille1) or fonctions.partieFinie(grille2)):
    if resultat[1]==1 or resultat[1]==3:
        resultat=fonctions.tirer_joueur1_version3(grille2)
    elif resultat[1]==2:

        cible=resultat[0]
        resultat=fonctions.tirer_joueur1_version3(grille2,cible)
        if (resultat[1]==1):   #il a raté mais on doit essayer une autre case à coté
            resultat[1]=2
            resultat[0]=cible

    print("votre grille : ")
    #fonctions.afficher_secrete(grille2)
    print("####################################")

    print("grille de l'ennemi :")
    fonctions.afficher(grille1)
    print("####################################")
    fonctions.tirer_joueur2(grille1)
    print("####################################")

if (fonctions.partieFinie(grille2)):
    print("vous avez perdu, essayez une autre fois héro!")
else:
    print("vous avez gagné !!!!!!")