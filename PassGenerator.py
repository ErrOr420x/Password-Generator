from tkinter import *
import random
passwd=""
element= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!"
fenetre = Tk()
fenetre.iconbitmap("logo.ico")
fenetre.title("Générateur de mot de passe")
def boutton ():	
	passwd=""
	for i in range(12): passwd = passwd + element[random.randint(0, len(element) - 1)]
	print(passwd)
	ligne_texte = Entry(fenetre, textvariable=passwd, width=30)
	ligne_texte.insert(0,"                  "+passwd+"")
	ligne_texte.pack()

Bouton1 = Button(fenetre, text = 'Générer', command = boutton)
Bouton1.pack()

var = StringVar()
label = Label( fenetre, textvariable=var, width=30)
var.set("ErrOr420x")
label.pack()

fenetre.mainloop()
