# Mastermind
#########################################
# groupe BI 4
# Flora GHULAM
# Léa LAPALUT
# Tatiana BRAGER
# https://github.com/uvsq22103697/projet_mastermind.git
#########################################

### Biblio

from tkinter import *
import tkinter as tk
import sys
import random

compteur = 0


#########################################
# Fonctions
class Application(tk.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(self, width=1800, height=800, background='white')
        self.attributes('-fullscreen', True)
        self.createWidgets()
        self.title("Mastermind")

        # création du menu principal
        self.welcome()
        self.canvas.grid()
        # création de l'affichage des règles
        # self.rules()
        # création de l'affichage en cas de défaite
        # self.abandonner()

    def createWidgets(self):
        # taille de fenetre
        self.minsize(1400, 500)

        # creation d'un cadre
        cadre = Frame(self)
        cadre.grid()

    color = ["red", "yellow", "dark green", "blue", "brown", "orange", "dark violet", "pink"]
    code_secret = ["","","",""]
    i = 0
    for i in range(4):
        random.shuffle(color)
        code_secret[i] = color[i]
        print(code_secret[i])

# mode 1 joueur
    def jeu(self):
        self.canvas.delete('all')
        n = 10
        m = 4
        r = 60
        y0 = -61
        i = 1
        j = 0
        for j in range(n):
            y0 += 70
            j += 1
            x0 = 11
            for i in range(m):
                x0 += 70
                self.canvas.create_oval(x0, y0, x0 + r, y0 + r)
                i += 1

        r = 20
        y0 = -61
        i = 1
        j = 0
        for j in range(n):
            y0 += 70
            j += 1
            x0 = m * 70 + 70
            for i in range(m):
                x0 += 20
                self.canvas.create_oval(x0, y0, x0 + r, y0 + r)
                i += 1

    # création des ronds de couleur
        self.canvas.create_oval(580 - 15, 26 - 15, 580 + 15, 26 + 15, fill='red')
        self.canvas.create_oval(580 - 15, 79 - 15, 580 + 15, 79 + 15, fill='yellow')
        self.canvas.create_oval(580 - 15, 133 - 15, 580 + 15, 133 + 15, fill='dark green')
        self.canvas.create_oval(580 - 15, 186 - 15, 580 + 15, 186 + 15, fill='blue')
        self.canvas.create_oval(580 - 15, 240 - 15, 580 + 15, 240 + 15, fill='brown')
        self.canvas.create_oval(580 - 15, 293 - 15, 580 + 15, 293 + 15, fill='orange')
        self.canvas.create_oval(580 - 15, 347 - 15, 580 + 15, 347 + 15, fill='dark violet')
        self.canvas.create_oval(580 - 15, 401 - 15, 580 + 15, 401 + 15, fill='pink')

    # variable stockant les choix du joueur
        my_color = ["","","",""]

    # fonction permettant de mettre les points verts
        def green_point(self, my_color):
            green_compteur = 0
            code = self.code_secret
            i = 0
            for i in range(4):
                if code[i] == my_color[i]:
                    green_compteur = green_compteur + 1
            return green_compteur

    # fonction permettant de mettre les points gris
        def grey_point(self, my_color):
            grey_compteur = 0
            code = self.code_secret()
            i = 0
            j = 0
            for i in range(4):
                for j in range(4):
                    if code[i] == my_color[j]:
                        grey_compteur = grey_compteur + 1
                        break
            return grey_compteur

        def green_display(cpt, my_color):
            if cpt == 1:
                self.canvas.create_oval(370, 9 + 40 * (compteur / 4), 370 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
            if cpt == 2:
                self.canvas.create_oval(370, 9 + 40 * (compteur / 4), 370 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
                self.canvas.create_oval(390, 9 + 40 * (compteur / 4), 390 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
            if cpt == 3:
                self.canvas.create_oval(370, 9 + 40 * (compteur / 4), 370 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
                self.canvas.create_oval(390, 9 + 40 * (compteur / 4), 390 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
                self.canvas.create_oval(410, 9 + 40 * (compteur / 4), 410 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
            if cpt == 4:
                self.canvas.create_oval(370, 9 + 40 * (compteur / 4), 370 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
                self.canvas.create_oval(390, 9 + 40 * (compteur / 4), 390 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
                self.canvas.create_oval(410, 9 + 40 * (compteur / 4), 410 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
                self.canvas.create_oval(430, 9 + 40 * (compteur / 4), 430 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="dark green")
            my_color = ["", "", "", ""]

        def grey_display(cpt, my_color):
            if cpt == 1:
                self.canvas.create_oval(430, 9 + 40 * (compteur / 4), 430 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
            if cpt == 2:
                self.canvas.create_oval(430, 9 + 40 * (compteur / 4), 430 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
                self.canvas.create_oval(410, 9 + 40 * (compteur / 4), 410 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
            if cpt == 3:
                self.canvas.create_oval(430, 9 + 40 * (compteur / 4), 430 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
                self.canvas.create_oval(410, 9 + 40 * (compteur / 4), 410 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
                self.canvas.create_oval(390, 9 + 40 * (compteur / 4), 390 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
            if cpt == 4:
                self.canvas.create_oval(430, 9 + 40 * (compteur / 4), 430 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
                self.canvas.create_oval(410, 9 + 40 * (compteur / 4), 410 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
                self.canvas.create_oval(390, 9 + 40 * (compteur / 4), 390 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
                self.canvas.create_oval(370, 9 + 40 * (compteur / 4), 370 + 20, 9 + 40 * (compteur / 4) + 20,
                                        fill="grey")
            my_color = ["", "", "", ""]





    # fonction permettant de mettre un point rouge
        def red_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                my_color[compteur - 1] = "red"
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='red')
                my_color[compteur - 1] = "red"
                print(my_color)
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='red')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='red')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='red')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60, fill='red')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)), y0 + 420,
                                                            x0 + (70 * (compteur - 20)) + 60, y0 + 420 + 60, fill='red')
                                else:
                                    if compteur <= 28:
                                        self.canvas.create_oval(x0 + (70 * (compteur - 24)), y0 + 490,
                                                                x0 + (70 * (compteur - 24)) + 60, y0 + 490 + 60,
                                                                fill='red')
                                    else:
                                        if compteur <= 32:
                                            self.canvas.create_oval(x0 + (70 * (compteur - 28)), y0 + 560,
                                                                    x0 + (70 * (compteur - 28)) + 60, y0 + 560 + 60,
                                                                    fill='red')
                                        else:
                                            if compteur <= 36:
                                                self.canvas.create_oval(x0 + (70 * (compteur - 32)), y0 + 630,
                                                                        x0 + (70 * (compteur - 32)) + 60, y0 + 630 + 60,
                                                                        fill='red')
                                            else:
                                                if compteur <= 40:
                                                    self.canvas.create_oval(x0 + (70 * (compteur - 36)), y0 + 700,
                                                                            x0 + (70 * (compteur - 36)) + 60,
                                                                            y0 + 700 + 60,
                                                                            fill='red')

    # fonction permettant de mettre un point jaune
        def yellow_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='yellow')
                my_color[compteur - 1] = "yellow"
                print(my_color)
                if compteur == 4:
                    green_compteur = green_point(self, my_color)
                    if green_compteur == 1:
                        self.canvas.create_oval(x0, y0, x0 + 20, y0 + 20, fill="dark grey")
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='yellow')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='yellow')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='yellow')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60, fill='yellow')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)), y0 + 420,
                                                            x0 + (70 * (compteur - 20)) + 60, y0 + 420 + 60,
                                                            fill='yellow')
                                else:
                                    if compteur <= 28:
                                        self.canvas.create_oval(x0 + (70 * (compteur - 24)), y0 + 490,
                                                                x0 + (70 * (compteur - 24)) + 60, y0 + 490 + 60,
                                                                fill='yellow')
                                    else:
                                        if compteur <= 32:
                                            self.canvas.create_oval(x0 + (70 * (compteur - 28)), y0 + 560,
                                                                    x0 + (70 * (compteur - 28)) + 60, y0 + 560 + 60,
                                                                    fill='yellow')
                                        else:
                                            if compteur <= 36:
                                                self.canvas.create_oval(x0 + (70 * (compteur - 32)), y0 + 630,
                                                                        x0 + (70 * (compteur - 32)) + 60, y0 + 630 + 60,
                                                                        fill='yellow')
                                            else:
                                                if compteur <= 40:
                                                    self.canvas.create_oval(x0 + (70 * (compteur - 36)), y0 + 700,
                                                                            x0 + (70 * (compteur - 36)) + 60,
                                                                            y0 + 700 + 60,
                                                                            fill='yellow')

    # fonction permettant de mettre un point vert foncé
        def dark_green_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='dark green')
                my_color[compteur - 1] = "dark green"
                print(my_color)
                if compteur == 4:
                    green_compteur = green_point(self, my_color)
                    if green_compteur == 1:
                        self.canvas.create_oval(x0, y0, x0 + 20, y0 + 20, fill="dark grey")
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='dark green')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='dark green')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='dark green')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60,
                                                        fill='dark green')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)), y0 + 420,
                                                            x0 + (70 * (compteur - 20)) + 60, y0 + 420 + 60,
                                                            fill='dark green')
                                else:
                                    if compteur <= 28:
                                        self.canvas.create_oval(x0 + (70 * (compteur - 24)), y0 + 490,
                                                                x0 + (70 * (compteur - 24)) + 60, y0 + 490 + 60,
                                                                fill='dark green')
                                    else:
                                        if compteur <= 32:
                                            self.canvas.create_oval(x0 + (70 * (compteur - 28)), y0 + 560,
                                                                    x0 + (70 * (compteur - 28)) + 60, y0 + 560 + 60,
                                                                    fill='dark green')
                                        else:
                                            if compteur <= 36:
                                                self.canvas.create_oval(x0 + (70 * (compteur - 32)), y0 + 630,
                                                                        x0 + (70 * (compteur - 32)) + 60, y0 + 630 + 60,
                                                                        fill='dark green')
                                            else:
                                                if compteur <= 40:
                                                    self.canvas.create_oval(x0 + (70 * (compteur - 36)), y0 + 700,
                                                                            x0 + (70 * (compteur - 36)) + 60,
                                                                            y0 + 700 + 60,
                                                                            fill='dark green')

    # fonction permettant de mettre un point bleu
        def blue_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='blue')
                my_color[compteur - 1] = "blue"
                print(my_color)
                if compteur == 4:
                    green_compteur = green_point(self, my_color)
                    if green_compteur == 1:
                        self.canvas.create_oval(x0, y0, x0 + 20, y0 + 20, fill="dark grey")
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='blue')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='blue')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='blue')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60, fill='blue')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)), y0 + 420,
                                                            x0 + (70 * (compteur - 20)) + 60, y0 + 420 + 60,
                                                            fill='blue')
                                else:
                                    if compteur <= 28:
                                        self.canvas.create_oval(x0 + (70 * (compteur - 24)), y0 + 490,
                                                                x0 + (70 * (compteur - 24)) + 60, y0 + 490 + 60,
                                                                fill='blue')
                                    else:
                                        if compteur <= 32:
                                            self.canvas.create_oval(x0 + (70 * (compteur - 28)), y0 + 560,
                                                                    x0 + (70 * (compteur - 28)) + 60, y0 + 560 + 60,
                                                                    fill='blue')
                                        else:
                                            if compteur <= 36:
                                                self.canvas.create_oval(x0 + (70 * (compteur - 32)), y0 + 630,
                                                                        x0 + (70 * (compteur - 32)) + 60, y0 + 630 + 60,
                                                                        fill='blue')
                                            else:
                                                if compteur <= 40:
                                                    self.canvas.create_oval(x0 + (70 * (compteur - 36)), y0 + 700,
                                                                            x0 + (70 * (compteur - 36)) + 60,
                                                                            y0 + 700 + 60,
                                                                            fill='blue')

    # fonction permettant de mettre un point marron
        def brown_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='brown')
                my_color[compteur - 1] = "brown"
                print(my_color)
                if compteur == 4:
                    green_compteur = green_point(self, my_color)
                    if green_compteur == 1:
                        self.canvas.create_oval(x0, y0, x0 + 20, y0 + 20, fill="dark grey")
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='brown')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='brown')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='brown')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60, fill='brown')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)))# fonction permettant de mettre un point orange
        def orange_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='orange')
                my_color[compteur - 1] = "orange"
                print(my_color)
                if compteur == 4:
                    green_compteur = green_point(self, my_color)
                    if green_compteur == 1:
                        self.canvas.create_oval(x0, y0, x0 + 20, y0 + 20, fill="dark grey")
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='orange')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='orange')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='orange')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60, fill='orange')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)), y0 + 420,
                                                            x0 + (70 * (compteur - 20)) + 60, y0 + 420 + 60,
                                                            fill='orange')
                                else:
                                    if compteur <= 28:
                                        self.canvas.create_oval(x0 + (70 * (compteur - 24)), y0 + 490,
                                                                x0 + (70 * (compteur - 24)) + 60, y0 + 490 + 60,
                                                                fill='orange')
                                    else:
                                        if compteur <= 32:
                                            self.canvas.create_oval(x0 + (70 * (compteur - 28)), y0 + 560,
                                                                    x0 + (70 * (compteur - 28)) + 60, y0 + 560 + 60,
                                                                    fill='orange')
                                        else:
                                            if compteur <= 36:
                                                self.canvas.create_oval(x0 + (70 * (compteur - 32)), y0 + 630,
                                                                        x0 + (70 * (compteur - 32)) + 60, y0 + 630 + 60,
                                                                        fill='orange')
                                            else:
                                                if compteur <= 40:
                                                    self.canvas.create_oval(x0 + (70 * (compteur - 36)), y0 + 700,
                                                                            x0 + (70 * (compteur - 36)) + 60,
                                                                            y0 + 700 + 60,
                                                                            fill='orange')

        # fonction permettant de mettre un point violet foncé
        def dark_violet_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='dark violet')
                my_color[compteur - 1] = "dark violet"
                print(my_color)
                if compteur == 4:
                    green_compteur = green_point(self, my_color)
                    if green_compteur == 1:
                        self.canvas.create_oval(x0, y0, x0 + 20, y0 + 20, fill="dark grey")
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='dark violet')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='dark violet')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='dark violet')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60,
                                                        fill='dark violet')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)), y0 + 420,
                                                            x0 + (70 * (compteur - 20)) + 60, y0 + 420 + 60,
                                                            fill='dark violet')
                                else:
                                    if compteur <= 28:
                                        self.canvas.create_oval(x0 + (70 * (compteur - 24)), y0 + 490,
                                                                x0 + (70 * (compteur - 24)) + 60, y0 + 490 + 60,
                                                                fill='dark violet')
                                    else:
                                        if compteur <= 32:
                                            self.canvas.create_oval(x0 + (70 * (compteur - 28)), y0 + 560,
                                                                    x0 + (70 * (compteur - 28)) + 60, y0 + 560 + 60,
                                                                    fill='derk violet')
                                        else:
                                            if compteur <= 36:
                                                self.canvas.create_oval(x0 + (70 * (compteur - 32)), y0 + 630,
                                                                        x0 + (70 * (compteur - 32)) + 60, y0 + 630 + 60,
                                                                        fill='dark violet')
                                            else:
                                                if compteur <= 40:
                                                    self.canvas.create_oval(x0 + (70 * (compteur - 36)), y0 + 700,
                                                                            x0 + (70 * (compteur - 36)) + 60,
                                                                            y0 + 700 + 60,
                                                                            fill='dark violet')

        # fonction permettant de mettre un point rose
        def pink_click():
            global compteur
            compteur = compteur + 1
            x0 = 11
            y0 = -61
            if (compteur % 4) == 0:
                green_compteur = green_point(self, my_color)
                green_display(green_compteur, my_color)
                # grey_compteur = grey_point(self,my_color)
                # grey_display(grey_compteur, my_color)
            if compteur <= 4:
                self.canvas.create_oval(x0 + (70 * compteur), y0 + 70, x0 + (70 * compteur) + 60, y0 + 70 + 60,
                                        fill='pink')
                my_color[compteur - 1] = "pink"
                print(my_color)
                if compteur == 4:
                    green_compteur = green_point(self, my_color)
                    if green_compteur == 1:
                        self.canvas.create_oval(x0, y0, x0 + 20, y0 + 20, fill="dark grey")
            else:
                if compteur <= 8:
                    self.canvas.create_oval(x0 + (70 * (compteur - 4)), y0 + 140, x0 + (70 * (compteur - 4)) + 60,
                                            y0 + 140 + 60, fill='pink')
                else:
                    if compteur <= 12:
                        self.canvas.create_oval(x0 + (70 * (compteur - 8)), y0 + 210, x0 + (70 * (compteur - 8)) + 60,
                                                y0 + 210 + 60, fill='pink')
                    else:
                        if compteur <= 16:
                            self.canvas.create_oval(x0 + (70 * (compteur - 12)), y0 + 280,
                                                    x0 + (70 * (compteur - 12)) + 60, y0 + 280 + 60, fill='pink')
                        else:
                            if compteur <= 20:
                                self.canvas.create_oval(x0 + (70 * (compteur - 16)), y0 + 350,
                                                        x0 + (70 * (compteur - 16)) + 60, y0 + 350 + 60, fill='pink')
                            else:
                                if compteur <= 24:
                                    self.canvas.create_oval(x0 + (70 * (compteur - 20)), y0 + 420,
                                                            x0 + (70 * (compteur - 20)) + 60, y0 + 420 + 60,
                                                            fill='pink')
                                else:
                                    if compteur <= 28:
                                        self.canvas.create_oval(x0 + (70 * (compteur - 24)), y0 + 490,
                                                                x0 + (70 * (compteur - 24)) + 60, y0 + 490 + 60,
                                                                fill='pink')
                                    else:
                                        if compteur <= 32:
                                            self.canvas.create_oval(x0 + (70 * (compteur - 28)), y0 + 560,
                                                                    x0 + (70 * (compteur - 28)) + 60, y0 + 560 + 60,
                                                                    fill='pink')
                                        else:
                                            if compteur <= 36:
                                                self.canvas.create_oval(x0 + (70 * (compteur - 32)), y0 + 630,
                                                                        x0 + (70 * (compteur - 32)) + 60, y0 + 630 + 60,
                                                                        fill='pink')
                                            else:
                                                if compteur <= 40:
                                                    self.canvas.create_oval(x0 + (70 * (compteur - 36)), y0 + 700,
                                                                            x0 + (70 * (compteur - 36)) + 60,
                                                                            y0 + 700 + 60,
                                                                            fill='pink')

        # création des boutons associés aux ronds de couleur
        red_btn = Button(text="  ", bg="red", bd='0', highlightcolor='red', activebackground='red', command=red_click)
        red_btn_window = self.canvas.create_window(580, 26, window=red_btn)
        yellow_btn = Button(text="  ", bg="yellow", bd='0', highlightcolor='yellow', activebackground='yellow',
                            command=yellow_click)
        yellow_btn_window = self.canvas.create_window(580, 79, window=yellow_btn)
        green_btn = Button(text="  ", bg="dark green", bd='0', highlightcolor='dark green', activebackground='dark '
                                                                                                             'green',
                           command=dark_green_click)
        green_btn_window = self.canvas.create_window(580, 133, window=green_btn)
        blue_btn = Button(text="  ", bg="blue", bd='0', highlightcolor='blue', activebackground='blue',
                          command=blue_click)
        blue_btn_window = self.canvas.create_window(580, 186, window=blue_btn)
        brown_btn = Button(text="  ", bg="brown", bd='0', highlightcolor='brown', activebackground='brown',
                           command=brown_click)
        brown_btn_window = self.canvas.create_window(580, 240, window=brown_btn)
        orange_btn = Button(text="  ", bg="orange", bd='0', highlightcolor='orange', activebackground='orange',
                            command=orange_click)
        orange_btn_window = self.canvas.create_window(580, 293, window=orange_btn)
        purple_btn = Button(text="  ", bg="dark violet", bd='0', highlightcolor='dark violet', activebackground='dark '
                                                                                                                'violet',
                            command=dark_violet_click)
        purple_btn_window = self.canvas.create_window(580, 347, window=purple_btn)
        pink_btn = Button(text="  ", bg="pink", bd='0', highlightcolor='pink', activebackground='pink',
                          command=pink_click)
        pink_btn_window = self.canvas.create_window(580, 401, window=pink_btn)


    # affichage du menu principal
    def welcome(self):
        self.canvas.delete('all')
        self.canvas.create_text(650, 70, text='Bienvenue dans notre Mastermind', font='arial 60', fill='red')
        # affichage du bouton "jouer"
        btn_start = Button(self.canvas, text='JOUER', font=("", 30), command=self.jeu)
        btn_start_window = self.canvas.create_window(350, 350, window=btn_start)
        # affichege du bouton "règles"
        btn_rules = Button(self.canvas, text='REGLES', font=("", 30), command=self.rules)
        btn_rules_window = self.canvas.create_window(850, 350, window=btn_rules)
        self.canvas.create_text(600, 600, text='AMUSEZ-VOUS BIEN !', font='arial 45', fill='red')

    # affichage des règles
    def rules(self):
        # règles
        self.canvas.delete('all')
        self.canvas.create_text(650, 40, text='Règles', font='arial 60', fill='red')

        self.canvas.create_rectangle(50, 100, 600, 635, outline='white', fill='white')
        self.canvas.create_text(325, 150, text='Voici le but du jeu :', font='Arial 30', fill='black')
        self.canvas.create_text(325, 220, text='Trouve les bonnes couleurs', font='Arial 30', fill='black')
        self.canvas.create_text(325, 270, text='dans le bonne ordre', font='Arial 30', fill='black')
        self.canvas.create_text(325, 360, text='Tout cela en 10 essais et', font='Arial 30', fill='black')
        self.canvas.create_text(325, 410, text='avec 8 couleurs différentes !', font='Arial 30', fill='black')
        self.canvas.create_text(325, 520, text='A toi de jouer ! ', font='Arial 30', fill='black')

        # exemples
        self.canvas.create_rectangle(650, 100, 1250, 635, outline='white', fill='white')
        self.canvas.create_text(950, 170, text='Voici les diffèrentes couleurs :', font='Arial 30', fill='black')
        self.canvas.create_oval(800 - 15, 210 - 15, 800 + 15, 210 + 15, fill='red')
        self.canvas.create_oval(840 - 15, 210 - 15, 840 + 15, 210 + 15, fill='yellow')
        self.canvas.create_oval(880 - 15, 210 - 15, 880 + 15, 210 + 15, fill='dark green')
        self.canvas.create_oval(920 - 15, 210 - 15, 920 + 15, 210 + 15, fill='blue')
        self.canvas.create_oval(960 - 15, 210 - 15, 960 + 15, 210 + 15, fill='brown')
        self.canvas.create_oval(1000 - 15, 210 - 15, 1000 + 15, 210 + 15, fill='orange')
        self.canvas.create_oval(1040 - 15, 210 - 15, 1040 + 15, 210 + 15, fill='dark violet')
        self.canvas.create_oval(1080 - 15, 210 - 15, 1080 + 15, 210 + 15, fill='pink')

        self.canvas.create_text(950, 290, text='lorsque la couleur est bonne:', font='Arial 30', fill='black')
        self.canvas.create_text(950, 340, text='- mais mal placé un rond noir s affiche', font='Arial 30', fill='black')
        self.canvas.create_oval(880 - 15, 390 - 15, 880 + 15, 390 + 15, fill='grey')
        self.canvas.create_oval(920 - 15, 390 - 15, 920 + 15, 390 + 15, fill='white')
        self.canvas.create_oval(960 - 15, 390 - 15, 960 + 15, 390 + 15, fill='white')
        self.canvas.create_oval(1000 - 15, 390 - 15, 1000 + 15, 390 + 15, fill='white')

        self.canvas.create_text(950, 450, text='- et bien placée un rond vert s affiche', font='Arial 30', fill='black')
        self.canvas.create_oval(880 - 15, 490 - 15, 880 + 15, 490 + 15, fill='light green')
        self.canvas.create_oval(920 - 15, 490 - 15, 920 + 15, 490 + 15, fill='white')
        self.canvas.create_oval(960 - 15, 490 - 15, 960 + 15, 490 + 15, fill='white')
        self.canvas.create_oval(1000 - 15, 490 - 15, 1000 + 15, 490 + 15, fill='white')

        # affichage du bouton "jouer"
        btn_start = Button(self.canvas, text='JOUER', font=("", 30), command=self.jeu)
        btn_start_window = self.canvas.create_window(625, 620, window=btn_start)

    def abandonner(self):
        # quand tu as perdus
        self.canvas.delete('all')
        self.canvas.create_text(500, 60, text='TU AS PERDU!', font='arial 70', fill='red')
        self.canvas.create_rectangle(110, 155, 890, 235, outline='blue', fill='red')
        self.canvas.create_text(500, 195, text='appuie sur le bouton quitter pour quitter', font='Arial 30',
                                fill='blue')
        self.canvas.create_rectangle(110, 255, 890, 335, outline='blue', fill='red')
        self.canvas.create_text(500, 295, text='appuie sur le bouton ci dessous pour rejouer', font='Arial 30',
                                fill='blue')
        self.canvas.create_text(500, 500, text='REESSAYER', font='arial 70', fill='red')
        btn_rejouer = Button(self.canvas, text='REJOUER', command=self.welcome)
        btn_rejouer_window = self.canvas.create_window(500, 360, anchor=NW, window=btn_rejouer)


app = Application()

# création de la barre de menu
menu_bar = tk.Menu(app)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="1 joueur", font=("", 16), command=app.jeu)
file_menu.add_command(label="2 joueurs", font=("", 16))
file_menu.add_separator()
file_menu.add_command(label="Règles", font=("", 16), command=app.rules)
file_menu.add_command(label="Menu principal", font=("", 16), command=app.welcome)
file_menu.add_separator()
file_menu.add_command(label="Quitter", font=("", 16), command=app.quit)
menu_bar.add_cascade(label="Menu", font=("", 20), menu=file_menu)
app.config(menu=menu_bar)


# création d'un évènement permettant de fermer la fenêtre
def close(event):
    app.withdraw()  # if you want to bring it back
    sys.exit()  # if you want to exit the entire thing


# utilisation de la touche Echap pour fermer la fenêtre
app.bind('<Escape>', close)

app.mainloop()


