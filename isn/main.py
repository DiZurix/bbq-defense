from tkinter import *
import random

#CONSTANTES + VARIABLES
C = 64                 #Coté d'un carré
NbC = 9                 #Nombre de carré
W, H = NbC*C, NbC*C     #Zone de jeu
WE, HE = 300, NbC*C     #Zone d'achat
select_tower = 0
Price = 50
Life = 3
Wave = 0
Money = 150
Nb_enmywave = 5
towertab = []

root = Tk()
root.title('BBQ Defense')
root.resizable(False, False)

def launch(select_map):
	
	#FENETRE + CANEVAS

	win = Canvas(root, width=W, height=H, highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
	win.pack(side=LEFT)
	win['bg']='black'
	
	#IMPORT IMAGES

	bbq = PhotoImage(file='./bbq1.gif')
	tower = PhotoImage(file='./tower1.gif')
	tower2 = PhotoImage(file='./tower2.gif')
	tower3 = PhotoImage(file='./tower3.gif')
	gameover = PhotoImage(file='./gameover.gif')
	winner_img = PhotoImage(file='./winner.gif')
	merguez = PhotoImage(file='./merguez1.gif')
	title = PhotoImage(file='./title.gif')

	#MENU TOURELLES

	menu = Canvas(root, width=WE, height=HE, highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
	menu['bg']='ivory'
	menu.pack(side=RIGHT)

	def menu_buttons():
		global b_wave
		x0, y0 = WE/2+WE/3.5, HE/10
		x1, y1 = WE/2+WE/3.5, HE/6
		b_wave = Button(root, text='Lancer la vague !')
		b_wave.configure(activebackground = "LemonChiffon1", relief = FLAT, bg="LemonChiffon2", command = lambda : wave(Nb_enmywave))
		b_wave_window = menu.create_window(x0, y0, anchor='center', window=b_wave)

		b_quit = Button(root, text='Quitter')
		b_quit.configure(activebackground = "LemonChiffon1", relief = FLAT, bg="LemonChiffon2", command = lambda : close_window(root))
		b_quit_window = menu.create_window(x1, y1, anchor='center', window=b_quit)


	def info_box():
		x0, y0, x1, y1 = WE/10, HE/30, WE/1.75, HE/4.25		#BOX
		x2, y2 = (x0+x1)/2, HE/16							#TEXTE
		yl, yw, ym = HE/9, HE/6.5, HE/5						#RESTE
		infos = menu.create_rectangle(x0, y0, x1, y1, width=2, fill='LemonChiffon2')
		infos_text = menu.create_text(x2, y2, text='Informations', font=('Times', '16', 'bold'))
		infos_lifes = menu.create_text(x2, yl, text=('Vie(s) : ' + str(Life)), font=('Times', '12'), anchor="center")
		infos_waves = menu.create_text(x2, yw, text=('Vague(s) : ' + str(Wave) + '/10'), font=('Times', '12'), anchor="center")
		infos_money = menu.create_text(x2, ym, text=('Argent : ' + str(Money) + '$'), font=('Times', '12'), anchor="center")

	#ACHATS TOURELLES

	def tower1_box():
		global box1
		global box1_img
		x0, y0 = WE/15, HE/3.5
		x1, y1 = WE-x0, y0+HE/7
		xi, yi, xt, yt, xp, yp = (x0+x1)/5, (y0+y1)/2, (x0+x1)/2, (y0+y1)/2-HE/22, WE/1.6, (y0+y1)/2
		box1 = menu.create_rectangle(x0, y0, x1, y1, width=2, fill="LemonChiffon2")
		box1_img = menu.create_image(xi, yi, image=tower, anchor='center')
		box1_title = menu.create_text(xt, yt, text='Ketchup', font=('Times', '14', 'bold'))
		box1_price = menu.create_text(xp, yp, text=('Prix : ' + str(Price) + '$'), font=('Times', '12'))

	def tower2_box():
		global box2
		x0, y0 = WE/15, HE/2.15
		x1, y1 = WE-x0, y0+HE/7
		xi, yi, xt, yt, xp, yp = (x0+x1)/5, (y0+y1)/2, (x0+x1)/2, (y0+y1)/2-HE/22, WE/1.6, (y0+y1)/2
		box2 = menu.create_rectangle(x0, y0, x1, y1, width=2, fill="LemonChiffon2")
		box2_img = menu.create_image(xi, yi, image=tower2, anchor='center')
		box2_title = menu.create_text(xt, yt, text='Moutarde', font=('Times', '14', 'bold'))
		box2_price = menu.create_text(xp, yp, text=('Prix : ' + str(Price*2) + '$'), font=('Times', '12'))

	def tower3_box():
		global box3
		x0, y0 = WE/15, HE/1.55
		x1, y1 = WE-x0, y0+HE/7
		xi, yi, xt, yt, xp, yp = (x0+x1)/5, (y0+y1)/2, (x0+x1)/2, (y0+y1)/2-HE/22, WE/1.6, (y0+y1)/2
		box3 = menu.create_rectangle(x0, y0, x1, y1, width=2, fill="LemonChiffon2")
		box3_img = menu.create_image(xi, yi, image=tower3, anchor='center')
		box3_title = menu.create_text(xt, yt, text='Sel', font=('Times', '14', 'bold'))
		box3_price = menu.create_text(xp, yp, text=('Prix : ' + str(Price*4) + '$'), font=('Times', '12'))

	def tower_select(evt):
		global select_tower
		x, y = evt.x, evt.y
		if WE/15 < x < WE-WE/15:
			if HE/3.5 < y < HE/3.5+HE/7:
				menu.itemconfig(box1, fill="LemonChiffon4")
				menu.itemconfig(box2, fill="LemonChiffon2")
				menu.itemconfig(box3, fill="LemonChiffon2")
				select_tower = 1
			elif HE/2.15 < y < HE/2.15+HE/7:
				menu.itemconfig(box1, fill="LemonChiffon2")
				menu.itemconfig(box2, fill="LemonChiffon4")
				menu.itemconfig(box3, fill="LemonChiffon2")
				select_tower = 2
			elif HE/1.55 < y < HE/1.55+HE/7:
				menu.itemconfig(box1, fill="LemonChiffon2")
				menu.itemconfig(box2, fill="LemonChiffon2")
				menu.itemconfig(box3, fill="LemonChiffon4")
				select_tower = 3

	def tower_sell(evt):
		x, y = evt.x, evt.y
		if tto[int(y/C)][int(x/C)]=='1':
			#towertab.delete()
			print(tto)

	#GRILLE DU JEU

	tab = [['M','S','M','M','M','M','M','A','M'], #1
		   ['M','B','M','D','D','B','M','H','M'], #2
		   ['M','B','M','H','M','B','M','H','M'], #3
		   ['M','B','M','H','M','B','M','H','M'], #4
		   ['M','B','M','H','M','B','M','H','M'], #5
		   ['M','B','M','H','M','B','M','H','M'], #6
		   ['M','B','M','H','M','B','M','H','M'], #7
		   ['M','D','D','H','M','D','D','H','M'], #8
		   ['M','M','M','M','M','M','M','M','M']] #9
		   # 1   2   3   4   5   6   7    8    9
	
	if select_map == 1:
		tab = [['M','S','M','D','D','D','D','B','M'], #1
			   ['M','D','D','H','M','M','M','B','M'], #2
			   ['M','M','M','M','M','B','G','G','M'], #3
			   ['B','G','G','G','M','B','M','M','M'], #4
			   ['B','M','M','H','G','G','M','D','A'], #5
			   ['B','M','M','M','M','M','M','H','M'], #6
			   ['B','M','D','D','B','M','M','H','M'], #7
			   ['D','D','H','M','B','M','M','H','M'], #8
			   ['M','M','M','M','D','D','D','H','M']] #9
		       # 1   2   3   4   5   6   7    8    9

	tto = [['0','0','0','0','0','0','0','0','0'], #1
		   ['0','0','0','0','0','0','0','0','0'], #2
		   ['0','0','0','0','0','0','0','0','0'], #3
		   ['0','0','0','0','0','0','0','0','0'], #4
		   ['0','0','0','0','0','0','0','0','0'], #5
		   ['0','0','0','0','0','0','0','0','0'], #6
		   ['0','0','0','0','0','0','0','0','0'], #7
		   ['0','0','0','0','0','0','0','0','0'], #8
		   ['0','0','0','0','0','0','0','0','0']] #9
		   # 1   2   3   4   5   6   7   8   9

	def createMap(root):
		for y in range(NbC):
			for x in range(NbC):
				if tab[y][x]=='M' and tto[y][x]=='0':
					murs = win.create_rectangle(x*C, y*C, x*C+C,y*C+C, fill = "darkolivegreen")
				elif tab[y][x]=='D' or tab[y][x]=='G'  or tab[y][x]=='B' or tab[y][x]=='H':
					chemin = win.create_rectangle(x*C, y*C, x*C+C,y*C+C, fill = "khaki", outline = "")
				elif tab[y][x]=='S' or tab[y][x]=='A':
					arrivee = win.create_rectangle(x*C, y*C, x*C+C,y*C+C, fill = "darkgoldenrod", outline = "")

	createMap(root)

	#RETOURNE LA CASE DE DEPART

	def Start(carte):
		for i, l in enumerate(carte):
			for j, v in enumerate(l):
				if v == 'S':
					return i, j

	#RETOURNE LA CASE D'ARRIVE

	def End(carte):
		for i, l in enumerate(carte):
			for j, v in enumerate(l):
				if v == 'A':
					return i, j

	#LIGNE/COLONNE en (X, Y)

	def ijVersxy(ij):
		i, j = ij
		x = j * C + C/2
		y = i * C + 1 +C/2
		return (x, y)

	#APPARITION ENNEMI ET OBJECTIF

	bbq_img = win.create_image(ijVersxy(End(tab)), image=bbq, anchor='center')
	titlebbq = menu.create_image(WE/2, HE/1.12, image=title, anchor='center')

	#APPARITION TOURELLES

	def tower_spawn(evt):
		global Money
		x, y = evt.x, evt.y
		if tto[int(y/C)][int(x/C)]=='0':
			if tab[int(y/C)][int(x/C)]=='M' and Life > 0 and Wave < 11:
				if select_tower == 1 and Money >= Price:
					towertab.append(Tower((int(x/C)*C+C/2),(int(y/C)*C+C/2),"tower1.gif", 1))
					Money -= Price
					tto[int(y/C)][int(x/C)] = '1'
				elif select_tower == 2 and Money >= Price*2:
					towertab.append(Tower((int(x/C)*C+C/2),(int(y/C)*C+C/2),"tower2.gif", 1.2))
					Money -= Price*2
					tto[int(y/C)][int(x/C)] = '1'
				elif select_tower == 3 and Money >= Price*4:
					towertab.append(Tower((int(x/C)*C+C/2),(int(y/C)*C+C/2),"tower3.gif", 1.8))
					Money -= Price*4
					tto[int(y/C)][int(x/C)] = '1'
				info_box()

	#DEPLACEMENT AUTO

	def normalize_xy(x, y):
		"produit le xC, yC du centre de la case dans laquelle tombe x, y"
		return (int((x+C/2)/C)*C)+C/2,(int((y+C/2)/C)*C)+C/2

	#CLASSE POUR LES ENNEMIS

	class Merguez:

		def __init__(self):
			self.image = PhotoImage(file="merguez1.gif")
			self.id = win.create_image(ijVersxy(Start(tab)), image=self.image, anchor='center')
			self.hp = random.randint(3,4) + int(Wave*1.2)
	
		def range_tower(self):
			global Money
			mx0, my0, mx1, my1 = win.bbox(self.id)
			mx, my = int((mx0 + mx1) / 2), int((my0 + my1) / 2)
			for i, tow in enumerate(towertab):
				x0, y0, x1, y1 = win.bbox(tow.id)
				tx, ty = int((x0 + x1)/2), int((y0 + y1)/2)
				if mx <= tx + tow.range and my <= ty + tow.range and mx >= tx - tow.range and my >= ty - tow.range:
					if tow.timeshot <= 0:
						tow.timeshot = tow.savetimeshot
						if self.hp >= 0:
							shotter = win.create_line(tx, ty, mx, my, joinstyle="round", width=2)
							win.after(125, destroy_shot, shotter)
							self.hp -= 1
							#print(self.hp)
							if self.hp <= 0:
								win.delete(self.id)
								win.after_cancel(imove)
								Money += 15
								info_box()

		def move(self, d):
			global Life
			global imove
			x0, y0, x1, y1 = win.bbox(self.id)
			mx, my = (x0 + x1) / 2,(y0 + y1) / 2
			xC, yC = normalize_xy(x0, y0)
			if mx == xC and my == yC:
				d = tab[int(y0/C)][int(x0/C)]
			imove = win.after(10, lambda : self.move(d))
			self.range_tower()
			if d == 'D':
				win.move(self.id, 1, 0)
			elif d == 'G':
				win.move(self.id, -1, 0)
			elif d == 'B':
				win.move(self.id, 0, 1)
			elif d == 'H':
				win.move(self.id, 0, -1)
			elif d == 'A':
				win.after_cancel(imove)
				win.delete(self.id)
				Life -= 1
				info_box()
				game_over()
				
				
	#CLASSE POUR LES TOURELLES

	class Tower:

		def __init__(self, posx, posy, img, multiply):
			self.image = PhotoImage(file=img)
			self.id = win.create_image(posx, posy, image=self.image, anchor='center')
			self.timeshot = 0
			self.savetimeshot = 20 / multiply
			self.multiply = multiply
			self.range = 2*C*multiply
			
			
	#INTERVALLE DE TEMPS ENTRE LES TIRS

	def timingshot():
		global shotter
		for i, tow in enumerate(towertab):
			tow.timeshot -= 1
		win.after(75, timingshot)
		
		
	#DETRUIT LES TIRS
	
	def destroy_shot(shotter):
		win.delete(shotter)


	#VAGUES D'ENNEMIS

	def wave(n = Nb_enmywave):
		global Wave
		global Nb_enmywave
		if n == Nb_enmywave:
			Wave += 1
			winner()
		if n > 0 and Wave < 11:
			win.after(random.randint(1750,2000), lambda : wave(n-1))
			m = Merguez()
			m.move(('B'))
			b_wave.configure(state='disabled')
		elif n == 0 and not Life == 0:
			Nb_enmywave += random.randint(3, 5)
			b_wave.configure(state='active')
		info_box()
	
		
	#SYSTEME D'ARGENT

	def money_up():
		global Money
		global stopmoney
		Money += 1
		stopmoney = win.after(2000, money_up)
		info_box()
		
	#DEFAITE

	def game_over():
		global Life
		if Life <= 0:
			win.create_image(H/2, W/2, image=gameover, anchor='center')
			win.after_cancel(stopmoney)
			b_wave.configure(state='disabled')
			Life = 0
			info_box()
			win.unbind("<Button-1>")
			menu.unbind("<Button-1>")
		
	#VICTOIRE
	
	def winner():
		global Wave
		if Wave > 10:
			win.create_image(H/2, W/2, image=winner_img, anchor='center')
			win.after_cancel(stopmoney)
			b_wave.configure(state='disabled')
			Wave = 10
			win.unbind("<Button-1>")
			menu.unbind("<Button-1>")
		
	
	#FERME LE JEU

	def close_window(root):
		root.destroy()
		

	#CALLS

	money_up()
	timingshot()
	tower1_box()
	tower2_box()
	tower3_box()
	menu_buttons()
	win.bind("<Button-3>", tower_sell)
	win.bind("<Button-1>", tower_spawn)
	menu.bind("<Button-1>", tower_select)
	win.bind("<Motion>", lambda evt: None)  #BUG ACCELERATION SOURIS

	root.mainloop()
