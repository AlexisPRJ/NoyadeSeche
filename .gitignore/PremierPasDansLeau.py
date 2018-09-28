# On importe Tkinter
from tkinter import *

def program():

    #Import des Entry
    iannee = int(aa.get())
    imois = int(mm.get())
    ijour = int(jj.get())

    #On récupère les deux dernier arguments de annee
    sdeux_dernier_annee = str(iannee)[2:4]
    sdeux_premier_annee = str(iannee)[0:2]

    #On divise par le quart
    ideux_dernier_annee = int(sdeux_dernier_annee)
    iresultat = ideux_dernier_annee + (ideux_dernier_annee // 4)

    # On ajoute le jour
    iresultat = iresultat + ijour

    # Selon le mois on rajoute au resultat
    if imois == 1:
        iresultat = iresultat + 0
    elif imois == 2:
        iresultat = iresultat + 3
    elif imois == 3:
        iresultat = iresultat + 3
    elif imois == 4:
        iresultat = iresultat + 6
    elif imois == 5:
        iresultat = iresultat + 1
    elif imois == 6:
        iresultat = iresultat + 4
    elif imois == 7:
        iresultat = iresultat + 6
    elif imois == 8:
        iresultat = iresultat + 2
    elif imois == 9:
        iresultat = iresultat + 5
    elif imois == 10:
        iresultat = iresultat + 0
    elif imois == 11:
        iresultat = iresultat + 3
    elif imois == 12:
        iresultat = iresultat + 5

    # On détermine si l'année est bissextile
    bissextile = False

    if (iannee / 400 == 0) or (iannee / 4 == 0 and not iannee / 100 == 0):
        bissextile = True
    if iannee / 400 == 0:
        bissextile = True
    elif iannee / 100 == 0:
        bissextile = False
    elif iannee / 4 == 0:
        bissextile = True

    # On enlève 1 si bissextile du mois de Janvier ou Fevrier
    if bissextile:
        if imois == 1 or imois == 1:
            iresultat = iresultat - 1

    # On ajoute par rapport au deux premiers termes de l'année
    if sdeux_premier_annee == "16":
        iresultat = iresultat + 6
    elif sdeux_premier_annee == "17":
        iresultat = iresultat + 4
    elif sdeux_premier_annee == "18":
        iresultat = iresultat + 2
    elif sdeux_premier_annee == "19":
        iresultat = iresultat + 0
    elif sdeux_premier_annee == "20":
        iresultat = iresultat + 6
    elif sdeux_premier_annee == "21":
        iresultat = iresultat + 4

    # On divise par 7 et on garde le reste
    iresultat = iresultat % 7

    # On selectionne le jour et on l'affiche
    jour_de_la_semaine = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    i = 0
    for i, jr in enumerate(jour_de_la_semaine):
        if iresultat == i: ll.set(jr)




# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Premier Pas Dans L'eau")

#On bloque la redim* de la fenre
fenetre.resizable(width=FALSE, height=False)
fenetre.geometry('400x200+350+400')

# On crée un label (ligne de texte)
champ_label = Label(fenetre, text="Saisissez une date au format JJ/MM/AAAA:")
champ_label.pack()

'Les champs de saisie pour la date'
jj = StringVar()
j = Entry(fenetre, textvariable=jj, justify='center')
j.place(x=160, y=50, width=20)
mm = StringVar()
m = Entry(fenetre, textvariable=mm, justify='center')
m.place(x=180, y=50, width=20)
aa = StringVar()
a = Entry(fenetre, textvariable=aa, justify='center')
a.place(x=200, y=50, width=40)
ll = StringVar()
l = Label(fenetre, textvariable=ll, justify='center')
l.place(x=155, y=120)
lr = StringVar()
lr = Label(fenetre, text="Le jour etait :", justify='center')
lr.place(x=155, y=100)

# On affiche le Boutton Lancez avec sa commande permettant de lancez le programme
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side=BOTTOM, pady=5, padx=5)
bouton_quitter.place(x='25', y='150')

# On affiche le Boutton QUitter avec sa commande permettant de fermer la fenêtre principal
bouton_lancer = Button(fenetre, text="Lancer", command=program)
bouton_lancer.pack(side=BOTTOM, pady=5, padx=5)
bouton_lancer.place(x='300', y='150')

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
