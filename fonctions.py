# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:16:47 2023

@author: nassim Sbai
         EL BADRAOUI Abderrahmane
"""
import itertools


#joueur 1 est l'ordianteur
#joueur 2 est l'utilisateur



import random
dic = {'A': 1, 'B': 2, 'C': 3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
def initialiserGrille():
    l=[[0 for i in range(12)] for i in range(12)]    #on a fait exprès une liste de 12x12 pour éviter de faire des conditions à chaque placement de 2
                                                     #mais dans l'affichage on va afficher que la grille 10x10 au milieu
    return l

#ceux sont des listes qui vont contenir les coordonées des cases de chaque bateau
#ceux sont des variables globales qu'on va modifier  à l'interieur des fonctions placer_bateaux
bateau5_joueur1=[]
bateau4_joueur1=[]
bateau31_joueur1=[]
bateau32_joueur1=[]
bateau2_joueur1=[]

bateau5_joueur2=[]
bateau4_joueur2=[]
bateau31_joueur2=[]
bateau32_joueur2=[]
bateau2_joueur2=[]

bateaux_joueur2=[bateau5_joueur2, bateau4_joueur2, bateau31_joueur2, bateau32_joueur2, bateau2_joueur2]

bateaux_joueur1=[bateau5_joueur1, bateau4_joueur1, bateau31_joueur1, bateau32_joueur1, bateau2_joueur1]


bateau5_a_couler_joueur1=[]
bateau4_a_couler_joueur1=[]
bateau31_a_couler_joueur1=[]
bateau32_a_couler_joueur1=[]
bateau2_a_couler_joueur1=[]

bateau5_a_couler_joueur2=[]
bateau4_a_couler_joueur2=[]
bateau31_a_couler_joueur2=[]
bateau32_a_couler_joueur2=[]
bateau2_a_couler_joueur2=[]

bateaux_a_couler_joueur1=[bateau5_a_couler_joueur1, bateau4_a_couler_joueur1, bateau31_a_couler_joueur1, bateau32_a_couler_joueur1, bateau2_a_couler_joueur1]
bateaux_a_couler_joueur2=[bateau5_a_couler_joueur2, bateau4_a_couler_joueur2, bateau31_a_couler_joueur2, bateau32_a_couler_joueur2, bateau2_a_couler_joueur2]



def placerBateaux5_joueur1(grille):
    parking1=False
    while(not parking1):
        ligne_debut = random.randint(1, 10)
        col_debut = random.randint(1, 10)
        methode=random.randint(1,4)
        if(methode==1):        # on place le bateau vers le haut
            ligne_fin=ligne_debut-4
            col_fin=col_debut
        if(methode==2):  #on place le bateau à droite
            ligne_fin=ligne_debut
            col_fin=col_debut+4
        if(methode==3):  #on place le bateau vers le bas
            ligne_fin=ligne_debut+4
            col_fin=col_debut
        if(methode==4):  #on place le bateau à gauche
            ligne_fin=ligne_debut
            col_fin=col_debut-4
        if(ligne_fin<=10 and col_fin<=10 and ligne_fin>=1 and col_fin>=1):
            parking1=True
    global bateau5_joueur1
    #placer des 1 et des 2 dans la grille
    if methode==1:
        grille[ligne_fin-1][col_fin]=grille[ligne_fin-1][col_fin-1]=grille[ligne_fin-1][col_fin+1]=2
        grille[ligne_debut+1][col_debut]=grille[ligne_debut+1][col_debut-1]=grille[ligne_debut+1][col_debut+1]=2
        for i in range(5):
            grille[ligne_fin+i][col_debut]=1
            grille[ligne_fin+i][col_debut-1]=2
            grille[ligne_fin+i][col_debut+1]=2
            bateau5_joueur1.append((ligne_fin + i, col_debut))
    if methode==3:   #methode3
        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][col_debut + 1] = 2
        for i in range(5):
            grille[ligne_debut+i][col_debut]=1
            grille[ligne_debut+i][col_debut-1]=2
            grille[ligne_debut+i][col_debut+1]=2
            bateau5_joueur1.append((ligne_debut + i, col_debut))
    if methode==4:      #methode 4
        grille[ligne_fin][col_fin-1]=grille[ligne_fin-1][col_fin-1]=grille[ligne_fin+1][col_fin-1]=2
        grille[ligne_debut][col_debut+1]=grille[ligne_debut-1][col_debut+1]=grille[ligne_debut+1][col_debut+1]=2
        for i in range(5):
            grille[ligne_debut][col_fin+i]=1
            grille[ligne_debut+1][col_fin+i]=2
            grille[ligne_debut-1][col_fin+i]=2
            bateau5_joueur1.append((ligne_debut, col_fin + i))

    if methode==2:     #methode 2
        grille[ligne_fin][col_fin+1]=grille[ligne_fin-1][col_fin+1]=grille[ligne_fin+1][col_fin+1]=2
        grille[ligne_debut][col_debut-1]=grille[ligne_debut-1][col_debut-1]=grille[ligne_debut+1][col_debut-1]=2
        for i in range(5):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau5_joueur1.append((ligne_debut, col_debut + i))




def placerBateaux4_joueur1(grille):
        parking2 = False
        while (not parking2):
            ligne_debut = random.randint(1, 10)
            col_debut = random.randint(1, 10)
            methode = random.randint(1, 4)
            if (methode == 1):  # on place le bateau vers le haut
                ligne_fin = ligne_debut - 3
                col_fin = col_debut
            if (methode == 2):  # on place le bateau à droite
                ligne_fin = ligne_debut
                col_fin = col_debut + 3
            if (methode == 3):  # on place le bateau vers le bas
                ligne_fin = ligne_debut + 3
                col_fin = col_debut
            if (methode == 4):  # on place le bateau à gauche
                ligne_fin = ligne_debut
                col_fin = col_debut - 3
            condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1

            if (condition1):
                condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2,1])
                if (condition2):
                    parking2 = True
        global bateau4_joueur1
        # placer des 1 et des 2 dans la grille
        if methode == 1:
            grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
            grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
                col_debut + 1] = 2
            for i in range(4):
                grille[ligne_fin + i][col_debut] = 1
                grille[ligne_fin + i][col_debut - 1] = 2
                grille[ligne_fin + i][col_debut + 1] = 2
                bateau4_joueur1.append((ligne_fin + i, col_debut))
        if methode==3:  # methode3
            grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
                col_fin + 1] = 2
            grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
                col_debut + 1] = 2
            for i in range(4):
                grille[ligne_debut + i][col_debut] = 1
                grille[ligne_debut + i][col_debut - 1] = 2
                grille[ligne_debut + i][col_debut + 1] = 2

                bateau4_joueur1.append((ligne_debut + i, col_debut))
        if methode==4:  # methode 4
            grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
            grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
                col_debut + 1] = 2
            for i in range(4):
                grille[ligne_debut][col_fin + i] = 1
                grille[ligne_debut + 1][col_fin + i] = 2
                grille[ligne_debut - 1][col_fin + i] = 2
                bateau4_joueur1.append((ligne_debut, col_fin + i))
        if methode==2:
            grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
            grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
                col_debut - 1] = 2
            for i in range(4):
                grille[ligne_debut][col_fin - i] = 1
                grille[ligne_debut + 1][col_fin - i] = 2
                grille[ligne_debut - 1][col_fin - i] = 2
                bateau4_joueur1.append((ligne_debut, col_debut + i))


def placerBateaux31_joueur1(grille):
    parking = False
    while (not parking):
        ligne_debut = random.randint(1, 10)
        col_debut = random.randint(1, 10)
        methode = random.randint(1, 4)
        if (methode == 1):  # on place le bateau vers le haut
            ligne_fin = ligne_debut - 2
            col_fin = col_debut
        if (methode == 2):  # on place le bateau à droite
            ligne_fin = ligne_debut
            col_fin = col_debut + 2
        if (methode == 3):  # on place le bateau vers le bas
            ligne_fin = ligne_debut + 2
            col_fin = col_debut
        if (methode == 4):  # on place le bateau à gauche
            ligne_fin = ligne_debut
            col_fin = col_debut - 2
        condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1

        if (condition1):
            condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2, 1])
            if (condition2):

                parking = True
    global bateau31_joueur1
    # placer des 1 et des 2 dans la grille
    if methode == 1:
        grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
        grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_fin + i][col_debut] = 1
            grille[ligne_fin + i][col_debut - 1] = 2
            grille[ligne_fin + i][col_debut + 1] = 2
            bateau31_joueur1.append((ligne_fin + i, col_debut))
    if methode==3:
        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
            col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_debut + i][col_debut] = 1
            grille[ligne_debut + i][col_debut - 1] = 2
            grille[ligne_debut + i][col_debut + 1] = 2
            bateau31_joueur1.append((ligne_debut + i, col_debut))

    if methode==4:
        grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
        grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_debut][col_fin + i] = 1
            grille[ligne_debut + 1][col_fin + i] = 2
            grille[ligne_debut - 1][col_fin + i] = 2
            bateau31_joueur1.append((ligne_debut, col_fin + i))

    if methode==2:
        grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
        grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut - 1] = 2
        for i in range(3):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau31_joueur1.append((ligne_debut, col_debut + i))

def placerBateaux32_joueur1(grille):
    parking = False
    while (not parking):
        ligne_debut = random.randint(1, 10)
        col_debut = random.randint(1, 10)
        methode = random.randint(1, 4)
        if (methode == 1):  # on place le bateau vers le haut
            ligne_fin = ligne_debut - 2
            col_fin = col_debut
        if (methode == 2):  # on place le bateau à droite
            ligne_fin = ligne_debut
            col_fin = col_debut + 2
        if (methode == 3):  # on place le bateau vers le bas
            ligne_fin = ligne_debut + 2
            col_fin = col_debut
        if (methode == 4):  # on place le bateau à gauche
            ligne_fin = ligne_debut
            col_fin = col_debut - 2
        condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1

        if (condition1):
            condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2, 1])
            if (condition2):

                parking = True
    global bateau32_joueur1
    # placer des 1 et des 2 dans la grille
    if methode == 1:
        grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
        grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_fin + i][col_debut] = 1
            grille[ligne_fin + i][col_debut - 1] = 2
            grille[ligne_fin + i][col_debut + 1] = 2
            bateau32_joueur1.append((ligne_fin + i, col_debut))

    if methode==3:
        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
            col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_debut + i][col_debut] = 1
            grille[ligne_debut + i][col_debut - 1] = 2
            grille[ligne_debut + i][col_debut + 1] = 2
            bateau32_joueur1.append((ligne_debut + i, col_debut))

    if methode==4:
        grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
        grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_debut][col_fin + i] = 1
            grille[ligne_debut + 1][col_fin + i] = 2
            grille[ligne_debut - 1][col_fin + i] = 2
            bateau32_joueur1.append((ligne_debut, col_fin + i))

    if methode==2:
        grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
        grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut - 1] = 2
        for i in range(3):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau32_joueur1.append((ligne_debut, col_debut + i))

def placerBateaux2_joueur1(grille):
    parking = False
    while (not parking):
        ligne_debut = random.randint(1, 10)
        col_debut = random.randint(1, 10)
        methode = random.randint(1, 4)
        if (methode == 1):  # on place le bateau vers le haut
            ligne_fin = ligne_debut - 1
            col_fin = col_debut
        if (methode == 2):  # on place le bateau à droite
            ligne_fin = ligne_debut
            col_fin = col_debut + 1
        if (methode == 3):  # on place le bateau vers le bas
            ligne_fin = ligne_debut + 1
            col_fin = col_debut
        if (methode == 4):  # on place le bateau à gauche
            ligne_fin = ligne_debut
            col_fin = col_debut - 1
        condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1

        if (condition1):
            condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2, 1])
            if (condition2):

                parking = True
    global bateau2_joueur1
    # placer des 1 et des 2 dans la grille
    if methode == 1:
        grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
        grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(2):
            grille[ligne_fin + i][col_debut] = 1
            grille[ligne_fin + i][col_debut - 1] = 2
            grille[ligne_fin + i][col_debut + 1] = 2
            bateau2_joueur1.append((ligne_fin + i, col_debut))

    if methode==3:
        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
            col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
            col_debut + 1] = 2
        for i in range(2):
            grille[ligne_debut + i][col_debut] = 1
            grille[ligne_debut + i][col_debut - 1] = 2
            grille[ligne_debut + i][col_debut + 1] = 2
            bateau2_joueur1.append((ligne_debut + i, col_debut))

    if methode==4:
        grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
        grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(2):
            grille[ligne_debut][col_fin + i] = 1
            grille[ligne_debut + 1][col_fin + i] = 2
            grille[ligne_debut - 1][col_fin + i] = 2
            bateau2_joueur1.append((ligne_debut, col_fin + i))

    if methode==2:
        grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
        grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut - 1] = 2
        for i in range(2):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau2_joueur1.append((ligne_debut, col_debut + i))

def afficher(grille):
    print("  1  2  3  4  5  6  7  8  9  10")
    alphabet=["A","B","C","D","E","F","G","H","I","J"]
    for i in range(10):
        print(alphabet[i], end="  ")
        for j in range(10):
            if(grille[i+1][j+1]=="*"):
                print("*", end="  ")
            elif(grille[i+1][j+1]=="+"):
                print("+",end ="  ")
            elif(grille[i+1][j+1]=="X"):
                print("X",end="  ")
            else:
                print(".", end="  ")
        print("\n")

dic = {'A': 1, 'B': 2, 'C': 3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}

def tirer_joueur2(grille):
    controle_saisie=False
    while(not controle_saisie):
        print("Saisissez la position du prochain tir :")
        lettre = input("lettre :").upper()
        colonne = int(input("Colonne :"))
        if lettre in ["A","B","C","D","E","F","G","H","I","J"] and colonne >=1 and colonne <=10:
            lettre=dic[lettre]
            if(grille[lettre][colonne]in["+","*","X"]):
                print("vous avez déjà tiré dans cette case, veuillez choisir une autre héro!")
            else:
                controle_saisie=True

    if(grille[lettre][colonne]in[0,2]):
        print("** Dans l'eau !")
        grille[lettre][colonne]="*"
    if(grille[lettre][colonne]==1):

        grille[lettre][colonne]="+"
        for i,bateau in zip(range(5), bateaux_joueur1):
            if (lettre,colonne) in bateau:
                indice_tuple = bateau.index((lettre,colonne))
                bateaux_a_couler_joueur1[i].append((lettre, colonne))
                bateau.pop(indice_tuple)
                if(len(bateau)==0):
                    for j in range(len(bateaux_a_couler_joueur1[i])):
                        grille[bateaux_a_couler_joueur1[i][j][0]] [bateaux_a_couler_joueur1[i][j][1]] = "X"
                    print("** Coulé!")
                else:
                    print("** Touché ! ")



def placerBateaux5_joueur2(grille):
    parking1=False
    while(not parking1):
        print("plaçons le bateau porte-avion constitué de 5 cases")
        ligne_debut=input("lettre :").upper()

        if ligne_debut in "ABCDEFGHIJ":
            ligne_debut=dic[ligne_debut]
            col_debut = int(input("colonne : "))

            methode=int(input("rentrer la methode de placement, 1 vers le haut, 2 vers la droite, 3 vers le bas et 4 vers le gauche"))
            if(methode==1):        # on place le bateau vers le haut
                ligne_fin=ligne_debut-4
                col_fin=col_debut
            if(methode==2):  #on place le bateau à droite
                ligne_fin=ligne_debut
                col_fin=col_debut+4
            if(methode==3):  #on place le bateau vers le bas
                ligne_fin=ligne_debut+4
                col_fin=col_debut
            if(methode==4):  #on place le bateau à gauche
                ligne_fin=ligne_debut
                col_fin=col_debut-4
            if(ligne_fin<=10 and col_fin<=10 and ligne_fin>=1 and col_fin>=1):
                parking1=True
    global bateau5_joueur2
    #placer des 1 et des 2 dans la grille
    if methode==1:
        grille[ligne_fin-1][col_fin]=grille[ligne_fin-1][col_fin-1]=grille[ligne_fin-1][col_fin+1]=2
        grille[ligne_debut+1][col_debut]=grille[ligne_debut+1][col_debut-1]=grille[ligne_debut+1][col_debut+1]=2
        for i in range(5):
            grille[ligne_fin+i][col_debut]=1
            grille[ligne_fin+i][col_debut-1]=2
            grille[ligne_fin+i][col_debut+1]=2
            bateau5_joueur2.append((ligne_fin + i, col_debut))
    if ligne_fin>ligne_debut:   #methode3
        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][col_debut + 1] = 2
        for i in range(5):
            grille[ligne_debut+i][col_debut]=1
            grille[ligne_debut+i][col_debut-1]=2
            grille[ligne_debut+i][col_debut+1]=2
            bateau5_joueur2.append((ligne_debut + i, col_debut))
    if col_fin<col_debut:      #methode 4
        grille[ligne_fin][col_fin-1]=grille[ligne_fin-1][col_fin-1]=grille[ligne_fin+1][col_fin-1]=2
        grille[ligne_debut][col_debut+1]=grille[ligne_debut-1][col_debut+1]=grille[ligne_debut+1][col_debut+1]=2
        for i in range(5):
            grille[ligne_debut][col_fin+i]=1
            grille[ligne_debut+1][col_fin+i]=2
            grille[ligne_debut-1][col_fin+i]=2
            bateau5_joueur2.append((ligne_debut, col_fin + i))

    if col_fin>col_debut:     #methode 2
        grille[ligne_fin][col_fin+1]=grille[ligne_fin-1][col_fin+1]=grille[ligne_fin+1][col_fin+1]=2
        grille[ligne_debut][col_debut-1]=grille[ligne_debut-1][col_debut-1]=grille[ligne_debut+1][col_debut-1]=2
        for i in range(5):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau5_joueur2.append((ligne_debut, col_debut + i))

def placerBateaux4_joueur2(grille):
    parking2 = False

    while (not parking2):
        print("plaçons le bateau croiseur constitué de 4 cases")
        ligne_debut = input("lettre :").upper()

        if ligne_debut in "ABCDEFGHIJ":
            ligne_debut = dic[ligne_debut]
            col_debut = int(input("colonne : "))
            methode = int(input("rentrer la methode de placement, 1 vers le haut, 2 vers la droite, 3 vers le bas et 4 vers le gauche"))

            if (methode == 1):  # on place le bateau vers le haut
                ligne_fin = ligne_debut - 3
                col_fin = col_debut
            if (methode == 2):  # on place le bateau à droite
                ligne_fin = ligne_debut
                col_fin = col_debut + 3
            if (methode == 3):  # on place le bateau vers le bas
                ligne_fin = ligne_debut + 3
                col_fin = col_debut
            if (methode == 4):  # on place le bateau à gauche
                ligne_fin = ligne_debut
                col_fin = col_debut - 3
            condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1

            if (condition1):
                condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2, 1])
                if (condition2):
                    parking2 = True
    global bateau4_joueur2
    # placer des 1 et des 2 dans la grille
    if methode == 1:
        grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
        grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(4):
            grille[ligne_fin + i][col_debut] = 1
            grille[ligne_fin + i][col_debut - 1] = 2
            grille[ligne_fin + i][col_debut + 1] = 2
            bateau4_joueur2.append((ligne_fin + i, col_debut))
    if ligne_fin > ligne_debut:  # methode3
        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
            col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
            col_debut + 1] = 2
        for i in range(4):
            grille[ligne_debut + i][col_debut] = 1
            grille[ligne_debut + i][col_debut - 1] = 2
            grille[ligne_debut + i][col_debut + 1] = 2

            bateau4_joueur2.append((ligne_debut + i, col_debut))
    if col_fin < col_debut:  # methode 4
        grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
        grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(4):
            grille[ligne_debut][col_fin + i] = 1
            grille[ligne_debut + 1][col_fin + i] = 2
            grille[ligne_debut - 1][col_fin + i] = 2
            bateau4_joueur2.append((ligne_debut, col_fin + i))
    if col_fin > col_debut:  # methode 2
        grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
        grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut - 1] = 2
        for i in range(4):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau4_joueur2.append((ligne_debut, col_debut + i))

def placerBateaux31_joueur2(grille):
    parking = False
    while (not parking):
        print("plaçons le bateau contre-torpilleur constitué de 3 cases")
        ligne_debut = input("lettre :").upper()
        if ligne_debut in "ABCDEFGHIJ":
            ligne_debut = dic[ligne_debut]
            col_debut = int(input("colonne : "))
            methode = int(input("rentrer la methode de placement, 1 vers le haut, 2 vers la droite, 3 vers le bas et 4 vers le gauche"))
            if (methode == 1):  # on place le bateau vers le haut
                ligne_fin = ligne_debut - 2
                col_fin = col_debut
            if (methode == 2):  # on place le bateau à droite
                ligne_fin = ligne_debut
                col_fin = col_debut + 2
            if (methode == 3):  # on place le bateau vers le bas
                ligne_fin = ligne_debut + 2
                col_fin = col_debut
            if (methode == 4):  # on place le bateau à gauche
                ligne_fin = ligne_debut
                col_fin = col_debut - 2
            condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1

            if (condition1):
                condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2, 1])
                if (condition2):

                    parking = True
        global bateau31_joueur2
        # placer des 1 et des 2 dans la grille
        if methode == 1:
            grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
            grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
                col_debut + 1] = 2
            for i in range(3):
                grille[ligne_fin + i][col_debut] = 1
                grille[ligne_fin + i][col_debut - 1] = 2
                grille[ligne_fin + i][col_debut + 1] = 2
                bateau31_joueur2.append((ligne_fin + i, col_debut))
        if ligne_fin > ligne_debut:  # methode3
            grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
                col_fin + 1] = 2
            grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
                col_debut + 1] = 2
            for i in range(3):
                grille[ligne_debut + i][col_debut] = 1
                grille[ligne_debut + i][col_debut - 1] = 2
                grille[ligne_debut + i][col_debut + 1] = 2
                bateau31_joueur2.append((ligne_debut + i, col_debut))

        if col_fin < col_debut:  # methode 4
            grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
            grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
                col_debut + 1] = 2
            for i in range(3):
                grille[ligne_debut][col_fin + i] = 1
                grille[ligne_debut + 1][col_fin + i] = 2
                grille[ligne_debut - 1][col_fin + i] = 2
                bateau31_joueur2.append((ligne_debut, col_fin + i))

        if col_fin > col_debut:  # methode 2
            grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
            grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
                col_debut - 1] = 2
            for i in range(3):
                grille[ligne_debut][col_fin - i] = 1
                grille[ligne_debut + 1][col_fin - i] = 2
                grille[ligne_debut - 1][col_fin - i] = 2
                bateau31_joueur2.append((ligne_debut, col_debut + i))

def placerBateaux32_joueur2(grille):
    parking = False
    while (not parking):
        print("plaçons le bateau sous-marin constitué de 3 cases")
        ligne_debut = input("lettre :").upper()
        if ligne_debut in "ABCDEFGHIJ":
            ligne_debut = dic[ligne_debut]
            col_debut = int(input("colonne : "))
            methode = int(input("rentrer la methode de placement, 1 vers le haut, 2 vers la droite, 3 vers le bas et 4 vers le gauche"))
            if (methode == 1):  # on place le bateau vers le haut
                ligne_fin = ligne_debut - 2
                col_fin = col_debut
            if (methode == 2):  # on place le bateau à droite
                ligne_fin = ligne_debut
                col_fin = col_debut + 2
            if (methode == 3):  # on place le bateau vers le bas
                ligne_fin = ligne_debut + 2
                col_fin = col_debut
            if (methode == 4):  # on place le bateau à gauche
                ligne_fin = ligne_debut
                col_fin = col_debut - 2
            condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1
            if (condition1):
                condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2, 1])
                if (condition2):

                    parking = True
    global bateau32_joueur2
    # placer des 1 et des 2 dans la grille
    if methode == 1:
        grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
        grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_fin + i][col_debut] = 1
            grille[ligne_fin + i][col_debut - 1] = 2
            grille[ligne_fin + i][col_debut + 1] = 2
            bateau32_joueur2.append((ligne_fin + i, col_debut))

    if ligne_fin > ligne_debut:  # methode3

        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
            col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_debut + i][col_debut] = 1
            grille[ligne_debut + i][col_debut - 1] = 2
            grille[ligne_debut + i][col_debut + 1] = 2
            bateau32_joueur2.append((ligne_debut + i, col_debut))

    if col_fin < col_debut:  # methode 4
        grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
        grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(3):
            grille[ligne_debut][col_fin + i] = 1
            grille[ligne_debut + 1][col_fin + i] = 2
            grille[ligne_debut - 1][col_fin + i] = 2
            bateau32_joueur2.append((ligne_debut, col_fin + i))

    if col_fin > col_debut:  # methode 2
        grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
        grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut - 1] = 2
        for i in range(3):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau32_joueur2.append((ligne_debut, col_debut + i))


def placerBateaux2_joueur2(grille):
    parking = False
    while (not parking):
        print("plaçons le bateau torpilleur constitué de 2 cases")
        ligne_debut = input("lettre :").upper()
        if ligne_debut in "ABCDEFGHIJ":
            ligne_debut = dic[ligne_debut]
            col_debut = int(input("colonne : "))
            methode = int(input("rentrer la methode de placement, 1 vers le haut, 2 vers la droite, 3 vers le bas et 4 vers le gauche"))
            if (methode == 1):  # on place le bateau vers le haut
                ligne_fin = ligne_debut - 1
                col_fin = col_debut
            if (methode == 2):  # on place le bateau à droite
                ligne_fin = ligne_debut
                col_fin = col_debut + 1
            if (methode == 3):  # on place le bateau vers le bas
                ligne_fin = ligne_debut + 1
                col_fin = col_debut
            if (methode == 4):  # on place le bateau à gauche
                ligne_fin = ligne_debut
                col_fin = col_debut - 1
            condition1 = ligne_fin <= 10 and col_fin <= 10 and ligne_fin >= 1 and col_fin >= 1

            if (condition1):
                condition2 = not (grille[ligne_debut][col_debut] in [2, 1] or grille[ligne_fin][col_fin] in [2, 1])
                if (condition2):

                    parking = True
    global bateau2_joueur2
    # placer des 1 et des 2 dans la grille
    if methode == 1:
        grille[ligne_fin - 1][col_fin] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin - 1][col_fin + 1] = 2
        grille[ligne_debut + 1][col_debut] = grille[ligne_debut + 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(2):
            grille[ligne_fin + i][col_debut] = 1
            grille[ligne_fin + i][col_debut - 1] = 2
            grille[ligne_fin + i][col_debut + 1] = 2
            bateau2_joueur2.append((ligne_fin + i, col_debut))

    if ligne_fin > ligne_debut:  # methode3
        grille[ligne_debut - 1][col_fin] = grille[ligne_debut - 1][col_fin - 1] = grille[ligne_debut - 1][
            col_fin + 1] = 2
        grille[ligne_fin + 1][col_debut] = grille[ligne_fin + 1][col_debut - 1] = grille[ligne_fin + 1][
            col_debut + 1] = 2
        for i in range(2):
            grille[ligne_debut + i][col_debut] = 1
            grille[ligne_debut + i][col_debut - 1] = 2
            grille[ligne_debut + i][col_debut + 1] = 2
            bateau2_joueur2.append((ligne_debut + i, col_debut))

    if col_fin < col_debut:  # methode 4
        grille[ligne_fin][col_fin - 1] = grille[ligne_fin - 1][col_fin - 1] = grille[ligne_fin + 1][col_fin - 1] = 2
        grille[ligne_debut][col_debut + 1] = grille[ligne_debut - 1][col_debut + 1] = grille[ligne_debut + 1][
            col_debut + 1] = 2
        for i in range(2):
            grille[ligne_debut][col_fin + i] = 1
            grille[ligne_debut + 1][col_fin + i] = 2
            grille[ligne_debut - 1][col_fin + i] = 2
            bateau2_joueur2.append((ligne_debut, col_fin + i))

    if col_fin > col_debut:  # methode 2
        grille[ligne_fin][col_fin + 1] = grille[ligne_fin - 1][col_fin + 1] = grille[ligne_fin + 1][col_fin + 1] = 2
        grille[ligne_debut][col_debut - 1] = grille[ligne_debut - 1][col_debut - 1] = grille[ligne_debut + 1][
            col_debut - 1] = 2
        for i in range(2):
            grille[ligne_debut][col_fin - i] = 1
            grille[ligne_debut + 1][col_fin - i] = 2
            grille[ligne_debut - 1][col_fin - i] = 2
            bateau2_joueur2.append((ligne_debut, col_debut + i))



combinations_list = list(itertools.combinations(range(1, 11), 2))
combinations = [(x, x) for x in range(1, 11)]
liste = combinations + combinations_list            #alors liste contient tous les couples possibles de la grille
liste_tire=[]                                       #et on la met en global variable pour pouvoir l'utiliser à l'interieur de la fonction tirer

def tirer_joueur1_version3(grille,cible=(0,0)):  #version plus intelligente
    global liste
    global liste_tire
    choosen = False
    if (cible==(0,0)):
        element_aleatoire = random.choice(liste)
    else:
        methodes_utilisees=[]  # pour ne pas répéter la meme methode plus qu'une fois
        while(not choosen):
            methode = random.randint(1, 4)
            element_aleatoire = list(cible)
            if methode==1 and 1 not in methodes_utilisees:             #on choisit la case au dessus
                element_aleatoire[0]-=1
            elif methode==2 and 2 not in methodes_utilisees:           #on choisit la case à droite
                element_aleatoire[1]+=1
            elif methode==3 and 3 not in methodes_utilisees:           #on choisit la case en dessous
                element_aleatoire[0]+=1
            elif methode==4 and  4 not in methodes_utilisees :                     #on choisit la case à gauche
                element_aleatoire[1]-=1
            elif len(methodes_utilisees)==4:   # ça veut dire que le programme ne trouve pas une case à coté et qui n'a pas été encore ciblé
                break                           #notre programme n'est pas assez intelligent pour aller regarder l'autre sens :p
            methodes_utilisees.append(methode)
            element_aleatoire = tuple(element_aleatoire)
            if (element_aleatoire[0] <= 10 and element_aleatoire[1] >= 1 and element_aleatoire[1] <= 10 and element_aleatoire[0] >= 1 and element_aleatoire in liste):
                choosen = True
    if(choosen==False):
        element_aleatoire = random.choice(liste)
    liste.pop(liste.index(element_aleatoire))
    liste_tire.append(element_aleatoire)

    lettre=element_aleatoire[0]
    colonne=element_aleatoire[1]

    resultat=[]  #liste resultat qui retourne les coordonées de point ciblé et 1 si dans l'eau et 2 si touché et 3 si coulé
    resultat.append(element_aleatoire)
    if(grille[lettre][colonne]in[0,2]):
        print("** Dans l'eau !")
        grille[lettre][colonne]="*"
        resultat.append(1)
        return resultat
    if(grille[lettre][colonne]==1):

        grille[lettre][colonne]="+"
        for i,bateau in zip(range(5), bateaux_joueur2):
            if (lettre,colonne) in bateau:    #on cherche si les coordonées choisit sont des caes de bateaux ou pas (et on meme temps on saura quelle bateau)
                indice_tuple = bateau.index((lettre,colonne))
                bateaux_a_couler_joueur2[i].append((lettre, colonne))
                bateau.pop(indice_tuple)  #si les coordonées se trouvent effectivement dans une liste de bateau , alors on l'enleve du bateau
                if(len(bateau)==0):        #si la liste de ce bateau est vide ça veut dire que le joueur a visé toutes les cases, et donc il doit couler
                    for j in range(len(bateaux_a_couler_joueur2[i])):
                        grille[bateaux_a_couler_joueur2[i][j][0]] [bateaux_a_couler_joueur2[i][j][1]] = "X"
                    print("** il vous a coulé un bateau :(")
                    resultat.append(3)
                    return resultat
                else:
                    print("** aie! il vous a touché")
                    resultat.append(2)
                    return resultat


combinations_list = list(itertools.combinations(range(1, 11), 2))
combinations = [(x, x) for x in range(1, 11)]
liste = combinations + combinations_list
liste_tire=[]

def tirer_joueur1(grille):

    global liste
    global liste_tire
    element_aleatoire = random.choice(liste)

    liste.pop(liste.index(element_aleatoire))
    liste_tire.append(element_aleatoire)

    lettre=element_aleatoire[0]
    colonne=element_aleatoire[1]

    if(grille[lettre][colonne]in[0,2]):
        print("** dans l'eau !")
        grille[lettre][colonne]="*"
    if(grille[lettre][colonne]==1):

        grille[lettre][colonne]="+"
        for i,bateau in zip(range(5), bateaux_joueur2):
            if (lettre,colonne) in bateau:       #on cherche si les coordonées choisit sont des caes de bateaux ou pas (et on meme temps on saura quelle bateau)
                indice_tuple = bateau.index((lettre,colonne))
                bateaux_a_couler_joueur2[i].append((lettre, colonne))
                bateau.pop(indice_tuple)        #si les coordonées se trouvent effectivement dans une liste de bateau , alors on l'enleve du bateau
                if(len(bateau)==0):             #si la liste de ce bateau est vide ça veut dire que le joueur a touché toutes les cases, et donc le bateau doit couler
                    for j in range(len(bateaux_a_couler_joueur2[i])):
                        grille[bateaux_a_couler_joueur2[i][j][0]] [bateaux_a_couler_joueur2[i][j][1]] = "X"
                    print("** il vous a coulé un bateau dans ")
                else:
                    print("** aie! il vous a touché")

def partieFinie(grille):
    cpt=0
    for i in range(1,11):
        for j in range(1,11):
            if grille[i][j]=="X":           #si le nombre de X est égale à la somme de longueurs de tous les bateaux (17) alors la partie est fini
                cpt+=1
    if cpt==17:
        return True
    else:
        return False


def afficher_secrete(grille):
    print("   1  2  3  4  5  6  7  8  9  10")
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in range(1,11):                               #on commence à 1 et on finit à 10  pour ne pas afficher les "bords"
        print(alphabet[i-1], end="  ")
        for j in range(1,11):
            print(grille[i][j],end="  ")
        print("\n")
