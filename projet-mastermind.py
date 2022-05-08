# Mastermind
#########################################
# groupe BI 4
# Flora GHULAM
# Léa LAPALUT
# Tatiana BRAGER
# https://github.com/uvsq22103697/projet_mastermind.git
#########################################

### COMMENTAIRE ET CHOSE A FAIRE :
# vérifier les dimensions de la grille dans les constantes en mettant le programme en marche (faire en sorte de le démarresi pas encore fait)
# me dier qu'il y a bien toutes les bibliothèques svp je suis pas sure mdr
# mettre en état les fonctions pour nous les approrpier et les adapter au code
## => je voulais faire 1 fenetre qui represente chacunes la table du joueurs (j'ai déjà mit le bon nombre de case il faut juste trouver la bonne dimensions)
## => j'ai aussi def les bonnes couleurs pour les pions mais j'ai pas encore trouver comment les faire intervenir
## => il faut créer le choix des pions par l'utilisateur 1 
## => puis la façon de choisir pour l'utilisateur 2
## => puis comment les solutions vont s'afficher si le joueur 2 à trouvé ou non

### Biblio

import tkinter as tk
from tracemalloc import stop
import random
import collections

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

### pour le moment j'ai juste repris la mtd du prof dans sa correction pour sandpile

# objets graphiques représentant la grille dans un tableau 2D
grille = None
# configuration courante dans un tableau 2D de dimension N+2 pour tenir compte des bords
config_cur = None
# deux variables booléeennes por savoir si il faut ajouter ou soustraire la config créée quand on clique dessus
add_active = False
sous_active = False
# variable booléenne pour savoir si le mode cinéma est actif ou pas
arret = True
# identifiant de la méthode after qui sert à pouvoir arrêter le compte à rebours
id_after = 0
#liste des couleurs des pions
lst_init_couleurs = ["bleu", "rose", "vert", "jaune", "violet"]

#########################################
# Fonctions


class Mastermind:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent)
        self.status = tk.Label(parent)
        self.draw_board()

    def draw_board(self, event=None):
        self.canvas.destroy()
        self.status.destroy()
        self.canvas = tk.Canvas(self.parent, width=1027, height=400)
        self.canvas.pack()
        self.bag = {'pi':self.canvas.create_oval(960, 0, 1027, 66, fill='pink', outline='pink'),
                    'p':self.canvas.create_oval(960, 66, 1027, 131, fill='purple', outline='purple'),
                    'y':self.canvas.create_oval(960, 131, 1027, 200, fill='yellow', outline='yellow'),
                    'g':self.canvas.create_oval(960, 200, 1027, 267, fill='green', outline='green'),
                    'b':self.canvas.create_oval(960, 267, 1027, 334, fill='blue', outline='blue'),
                   }
        self.ids = {v:k for k,v in self.bag.items()}
        self.colors = {'pi':'pink', 'p':'purple', 'y':'yellow',
                       'g':'green', 'b':'blue'}
        self.guesses = ['']
        self.status = tk.Label(self.parent)
        self.status.pack()
        self.canvas.bind('<1>', self.check)
        self.parent.bind('<Control-n>', self.draw_board)
        self.parent.bind('<Control-N>', self.draw_board)
        self.pattern = [random.choice('roygbp') for _ in range(4)]
        self.counted = collections.Counter(self.pattern)
        
    def check(self, event=None):
        id = self.canvas.find_withtag("current")[0]
        guess = self.ids[id]
        self.guesses[-1] += guess
        y_offset = (len(self.guesses[-1]) - 1) * 80
        x_offset = (len(self.guesses) - 1) * 80
        self.canvas.create_oval(x_offset, y_offset,
                                x_offset+80, y_offset+80,
                                fill=self.colors[guess],
                                outline=self.colors[guess])
        if len(self.guesses[-1]) < 4:
            return
        guess_count = collections.Counter(self.guesses[-1])
        close = sum(min(self.counted[k], guess_count[k]) for k in self.counted)
        exact = sum(a==b for a,b in zip(self.pattern, self.guesses[-1]))
        close -= exact
        colors = exact*['black'] + close*['white']
        key_coordinates = [(x_offset, 320, x_offset+40, 360),
                           (x_offset, 360, x_offset+40, 400),
                           (x_offset+40, 320, x_offset+80, 360),
                           (x_offset+40, 360, x_offset+80, 400)]
        for color, coord in zip(colors, key_coordinates):
            self.canvas.create_oval(coord, fill=color, outline=color)
        if exact == 4:
            self.status.config(text='Gagné!')
            self.canvas.unbind('<1>')
        elif len(self.guesses) > 11:
            self.status.config(
                               text='Aucune autre idées. La réponse est {}.'.format(
                                ''.join(self.pattern)))
            self.canvas.unbind('<1>')
        else:
            self.guesses.append('')
        
root = tk.Tk()
game = Mastermind(root)
root.mainloop()
## déf une fonction qui fait apparaitre le table de jeu (bouton start) et qui demande à l'utilisateur les 4 couleurs qu'il veut puis qui enregistre le choix
## def une fonction qui permet de cacher le choix qd les couleurs sont validées (bouton ok) et qui demande au joueur 2 de joueur
## def une fonction qui propose toutes les couleurs au joueur 2 (un bouton par couleur) et qui permette au joueur de sélectionner un enchainement de 4 coueleurs
## def une fonction qui permet de vérifier les choix du joueur 2 et qui affiche les bonnes ET les mauvaise réponse (en créant une crois rouge sous le mauvais piont par exemple ou en faisant des points sur le cotés rouge ou blanc comme le prof)
## def une fonction qui demande au joueur 2 de faire un 2ème tour (bouton next ?) etc jusqu'à ce que le joueur est fait 10 tours ou est trouvé la solution
## def une fonction qui donne les résultats en dévoilant la solution et qui félicite ou non le joueur 2 si il a rtouvé la solution

#########################################
# Programme principal

 ## => suivre l'enchainement des étapes dans les fonctions (question joueur 1, son choix, cacher la solution, demander joueur 2 en modfifiant la fenêtre, valider ou non les reponse a chq fois puis finir le jeu au bout de 10 essais)

# Définitions des widgets

 ## => créer des boutons pour chq étapes en se référant au commentaire dans fonctions (bouton start, ok, next, solution ...)

# Placement des widgets

 ## => placer les boutons dans la fenetre en bas à droite pour passer à chq étapes suivante et mettre les choix de couleur dans chq bande horizontale à chq nouvelle décisions)

# Liaisons d'évènements

 ## => lier l'apparition de la fentre avec le debut du jeu
 ## => lier le clic des boutons avec les actions voulues

# Boucle principale
#racine.mainloop()

#### EXEMPLE TROUV2 SUR INTERNET


#Transformation d'une chaine en liste (def to_list(s))
#chaine = "123456"
#lst_chaine = list(chaine)
#print("chaine = ", chaine, "        liste = ", lst_chaine)



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
