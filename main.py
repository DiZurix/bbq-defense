from tkinter import *
from random import *

#CONSTANTES + VARIABLES
C = 64                 #Coté d'un carré
NbC = 9                 #Nombre de carré
W, H = NbC*C, NbC*C     #Zone de jeu
WE, HE = 300, NbC*C     #Zone d'achat

root = Tk()
root.title('The Carré Quest')
root.resizable(False, False)

#FENETRE + CANEVAS

win = Canvas(root, width=W, height=H, highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
win.pack(side=LEFT)
win['bg']='black'

#CARTE

COLOR = ["crimson", "red","chartreuse", "lightgreen","cyan", "turquoise"]

tab = [['M','M','M','M','M','M','M','M','M'], #1
        ['M','M','M','M','M','M','M','M','M'], #2
        ['M','M','M','M','M','M','M','M','M'], #3
        ['M','M','M','M','M','M','M','M','M'], #4
        ['M','M','M','M','M','M','M','M','M'], #5
        ['M','M','M','M','M','M','M','M','M'], #6
        ['M','M','M','M','M','M','M','M','M'], #7
        ['M','M','M','M','M','M','M','M','M'], #8
        ['M','M','M','M','M','M','M','M','M']] #9
        # 1   2   3   4   5   6   7    8    9

def createMap():
        for y in range(NbC):
                for x in range(NbC):
                        if tab[y][x]=='M':
                                murs = win.create_rectangle(x*C, y*C, x*C+C,y*C+C, fill = COLOR[randint(0, 5)])

createMap()
	
root.mainloop()
