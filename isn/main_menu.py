from main import *

WC = W + WE
M = WC/2
select_map = 0

merguez = PhotoImage(file="merguez1.gif")
merguez = merguez.zoom(2)
barbecue = PhotoImage(file="bbq1.gif")
barbecue = barbecue.zoom(2)
m1_img = PhotoImage(file="map1.gif")
m2_img = PhotoImage(file="map2.gif")

def menu():
	global can
	global Y
	can = Canvas(root, width=WC, height=H, highlightbackground="black", highlightcolor="black", cursor = 'circle', highlightthickness=2, bd=0)
	can.pack()
	can['bg']='Dark Olive Green'
	
	b_play = Button(can, text='Jouer', font="Arial 16")
	b_play_window = can.create_window(M, H/2.75, anchor='center', width = 200, window=b_play)
	b_play.configure(bg= 'LemonChiffon2', activebackground = 'LemonChiffon1', pady = 15, relief = FLAT, command = lambda : start_game())

	b_settings = Button(can, text='Choix de la carte', font="Arial 16" )
	b_settings_window = can.create_window(M, H/1.75, anchor = 'center', width = 200, window=b_settings)
	b_settings.configure(bg= 'LemonChiffon2', activebackground = 'LemonChiffon1', pady = 15, relief = FLAT, command = settings)

	b_exit = Button(can, text='Fermer le jeu', font="Arial 16" )
	b_exit_window = can.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200, window=b_exit)
	b_exit.configure(bg= 'LemonChiffon2', activebackground = 'LemonChiffon1', pady = 15, relief = FLAT, command = lambda : close_window(root))

	copyright = can.create_text(W+250, H-20, text="©Ruislor", font="Arial 16 italic", fill="Black")

	title = Label(can,text = 'BBQ DEFENSE', font= 'Arial 30', justify = 'center', background = 'tomato4')
	title_window = can.create_window(M, H/6, anchor = 'center', width = WC+5, window=title)
	
	########ANIMATIONS DANS LE MENU######
	
	X, Y = WC-WC/5, M/1.5
	mrgz_img = can.create_image(X, Y, image=merguez, anchor='center')
	bbq_img = can.create_image(WC/5, Y, image=barbecue, anchor='center')
	
	def up():
		x0, y0, x1, y1 = can.bbox(mrgz_img)
		x2, y2, x3, y3 = can.bbox(bbq_img)
		mmove = can.after(10, up)
		can.move(mrgz_img, 0, 1)
		can.move(bbq_img, 0, -1)
		if y0 == W/2:# or y2 == M/2
			can.after_cancel(mmove)
			down()
		
	def down():
		x0, y0, x1, y1 = can.bbox(mrgz_img)
		x2, y2, x3, y3 = can.bbox(bbq_img)
		mmove = can.after(10, down)
		can.move(mrgz_img, 0, -1)
		can.move(bbq_img, 0, 1)
		if y0 == W/3:#or y2 == M/1.5
			can.after_cancel(mmove)
			up()
			
	up()

	########################################

	

def settings():
	can.destroy()
	win = Canvas(root, width=WC, height=H, highlightbackground="black", highlightcolor="black", cursor = 'circle', highlightthickness=2, bd=0)
	win.pack()
	win['bg']='Dark Olive Green'

	def close_settings(root):
		win.destroy()
		menu()
		print(select_map)
		
	def map1():
		global map1_box		#WC/3
		x0, y0 = WC/6, WC/8
		x1, y1 = WC/2.5, WC/2.5+(y0-x0)
		map1_box = win.create_rectangle(x0, y0, x1, y1, width=2, fill='LemonChiffon2')
		map1_img = win.create_image((x0+x1)/2, (y0+y1)/2, image=m1_img, anchor='center')
		map1_title = win.create_text((WC/6+WC/2.5)/2, WC/2.6, text='Carte 1', font=('Times', '18', 'bold'))
		
	
	def map2():
		global map2_box
		x0, y0 = WC-WC/2.5, WC/8
		x1, y1 = WC-WC/6, WC-WC/6+(y0-x0)
		map2_box = win.create_rectangle(x0, y0, x1, y1, width=2, fill='LemonChiffon2')
		map2_img = win.create_image((x0+x1)/2, (y0+y1)/2, image=m2_img, anchor='center')
		map2_title = win.create_text((WC-WC/2.5+WC-WC/6)/2, WC/2.6, text='Carte 2', font=('Times', '18', 'bold'))
		
	def map_select(evt):
		global select_map
		x, y = evt.x, evt.y
		if WC/8 < y < WC/3:
			if WC/6 < x < WC/2.5:
				win.itemconfig(map1_box, fill="LemonChiffon4")
				win.itemconfig(map2_box, fill="LemonChiffon2")
				select_map = 0
			elif WC-WC/2.5 < x < WC-WC/6:
				win.itemconfig(map1_box, fill="LemonChiffon2")
				win.itemconfig(map2_box, fill="LemonChiffon4")
				select_map = 1

	b_close = Button(win, text='Fermer', font="Arial 16" )
	b_close_window = win.create_window(M, H/2 + H/4, anchor = 'center', width = 150, window=b_close)
	b_close.configure(bg= 'LemonChiffon2', activebackground = 'LemonChiffon1', pady = 30, relief = FLAT, command = lambda : close_settings(root))
	
	map1()
	map2()
	win.bind("<Button-1>", map_select)
	root.mainloop()

def close_window(root):
    root.destroy()

def start_game():
	can.pack_forget()
	if select_map == 0:
		launch(0)
	else:
		launch(1)

menu()
root.mainloop()
