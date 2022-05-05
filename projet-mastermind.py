# Mastermind
#########################################
# groupe BI 4
# Flora GHULAM
# Léa LAPALUT
# Tatiana BRAGER
# https://github.com/uvsq22103697/projet_mastermind.git
#########################################

### Biblio

import tkinter as tk
import copy
import random as rd
from tracemalloc import stop

#########################################
# Constantes

# taille de la grille rectangle joueur 1
N = 10
M = 4
# dimensions du canvas et de la grille joueur 1
LARGEUR = 100
HAUTEUR = 250
LARGEUR_CASE = LARGEUR // M
HAUTEUR_CASE = HAUTEUR // N

# taille de la grille rectangle joueur 2
N2 = 10
M2 = 4
# dimensions du canvas et de la grille joueur 2
LARGEUR2 = 100
HAUTEUR2 = 250
LARGEUR2_CASE = LARGEUR2 // M2
HAUTEUR2_CASE = HAUTEUR2 // N2

#########################################
# Variables Glo et Widgets

#########################################
# Fonctions

#########################################
# Programme principal

# Définitions des widgets

# Placement des widgets

# Liaisons d'évènements

# Boucle principale
racine.mainloop()

#### EXEMPLE TROUV2 SUR INTERNET


#Transformation d'une chaine en liste (def to_list(s))
#chaine = "123456"
#lst_chaine = list(chaine)
#print("chaine = ", chaine, "        liste = ", lst_chaine)

#liste des couleurs des pions
#lst_init_couleurs = ["bleu", "rose", "vert", "jaune", "violet"]

#Copie d'une liste dans une autre liste (def copie(liste):)
#lst_melange_couleurs = list(lst_init_couleurs)

#Mélange aléatoire de la liste (def cache(n,k))
#shuffle(lst_melange_couleurs)

#print(lst_init_couleurs, "couleurs initiales")
#print(lst_melange_couleurs, "couleurs mélangées")

#Controle couleur bien ou mal placée
#i = 0
#for element in lst_init_couleurs:
    #if lst_melange_couleurs[i] == element:
        #print("OK couleur", element,  "en position ", i)
    #else:
        #print("KO couleur en position ", i)

    #i += 1
