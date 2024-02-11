import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
# Dictionnaire de couleur

couleur = {

    "nero": "#252726",
    "purple": "#800080",
    "white": "#FFFFFF"}


# Paramétrage de la fenetre 
app = tk.Tk()
app.title("Mon application")
app.geometry("500x600")
app.config(bg="gray30")
app.iconbitmap("logo.ico")

#paramétrage du swith

btnEtat = False

#chargement des images app

appIcon = PhotoImage(file='menu.png')
closeIcon = PhotoImage(file='close.png')
imgFond = PhotoImage(file='back_image3.png')

#Top bar 
topFrame = tk.Frame(app, bg=couleur["purple"])
topFrame.pack(side="top" , fill=tk.X)

# Text de top bar

accueilText =tk.Label(topFrame, text ="Hello",
                      font="ExtraCondensed 25",
                      bg=couleur["purple"],
                      fg="white",height=2, padx=20)
accueilText.pack(side="right")

#Banner text et image de fond
can = Canvas(app,width=500 , height=600)
can.create_image(0,0,anchor=NW,
                 image=imgFond)
bannerText = tk.Label(app,text="DEVELOPPEMENT \n WEB",
                      font="ExtraCondensed 25",
                      fg="purple")
bannerText.place(x=100,y=400)
can.pack()

# App Icon

navBarBtn =tk.Button(topFrame, image=appIcon,
                     bg=couleur["purple"],bd=0,padx=30,
                     activebackground=couleur["purple"],
                     command=None)
navBarBtn.place(x=20, y=20)
#parametres appBar latérale

appLatéral = tk.Frame(app, bg="gray30" , width=300, height=600)
appLatéral.place(x=-300, y=0)
tk.Label(appLatéral,font="ExtroaCndensed 15", bg=couleur["purple"],
         fg="black",width=300,height=2,padx=20).place(x=0,y=0)

y=80

# Les options dans le appBar latérale :

option = ["ACUEIL","PAGES","PROFIL","PARAMETRES","AIDE"]

# Positionneement des options dans le appBar
for i in range(5):
    tk.Button(appLatéral,text=option[i],font="ExtroaCndensed 15",
              bg="gray30",fg=couleur["white"],
              activebackground="gray30",bd=0).place(x=25,y=y)
    y +=40


# Start the main event loop
app.mainloop()
