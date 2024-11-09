# Créé par gdodin, le 03/05/2023 en Python 3.7
from tkinter import *
from tkinter.messagebox import *
from random import *
from time import *
from Generation_grille import Grille, Case
import tkinter as tk


longueur=8 #verticale
largeur=10 #Horizontale
nb_bombes=10
compteur_cases_restantes=longueur*largeur-nb_bombes
taille_image_flag=16
assert nb_bombes<=longueur*largeur, 'Le nombre de bombes ne doit pas dépasser le nombre totale de cases'


#Génération de la grille
Grille1=Grille(nb_bombes,(longueur,largeur))
bombes=Grille1.initialise_bombe()
Grille1.calcule_mines_adjacentes(bombes)


#Génération de la fenêtre
fenetre= Tk()
fenetre.title('Démineur')
fenetre.iconphoto(False, tk.PhotoImage(file = "Images\logo.png"))
fenetre['bg']='#FCE6B6'

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(padx=50, pady=35)




def bomb():
    '''
    Fonction qui permet d'afficher le message de game over
    et qui arrete le programme.
    '''
    temps_fin=time()
    duree=temps_fin-temps_depart
    showerror('Perdu','Game Over\nDurée de la partie : ' + str(int(duree)) + ' secondes')
    fenetre.destroy()


def victoire():
    """
    Fonction qui vérifie si la condition de victoire est valide.
    Si elle l'est, affiche le message de victoire avec le temps mis par le
    joueur pour déminer la grille puis arrete le programme.
    """
    #Utilisation de la variable globale compteur_cases_restantes
    global compteur_cases_restantes
    if compteur_cases_restantes==0:
        temps_fin=time()
        duree=temps_fin-temps_depart
        showinfo('Victoire','Vous avez gagné(e) en ' + str(int(duree)) + ' secondes')
        fenetre.destroy()


def reveal(ligne, colonne):
    '''
    Fonction assignée en tant que commande à chaque boutons/cases de la grille,
    elle permet de dévoiller la case cliquée en différencient les bombes,
    les cases classique ainsi que les cases vides.
    Les cases ne peuvent être dévoiller si elles sont recouvertes
    d'un drapeau.
    La fonction prend en paramêtre la ligne et la colonne de la
    case cliquée/à dévoiller.
    '''
    #On vérifie qu'il n'y a pas de drapeau sur la case à dévoiller
    if Grille1.grille[ligne][colonne].drapeau==False:

        #On vérifie si la case est une bombe ou non
        if Grille1.grille[ligne][colonne].valeur=='*':
            #Gestion de la bombe avec la fonction bomb()
            bomb()

        else:
            #On vérifie que la case n'a pas déja été dévoillée
            if Grille1.grille[ligne][colonne].reveal==False:
                #Utilisation de la variable globale compteur_cases_restantes
                #Modification du compteur de cases restantes
                global compteur_cases_restantes
                compteur_cases_restantes-=1

                #On vérifie si la case est vide ou non
                if Grille1.grille[ligne][colonne].valeur==0:
                    #Gestion des cases vides :
                    #On modifie l'attribut reveal de la case pour ne pas
                    #Dévoiller plusieur fois la même case
                    Grille1.grille[ligne][colonne].reveal=True

                    #On dévoille la case
                    buttons[ligne][colonne].configure(bg="#DACE91", text='')
                    victoire()

                    #On vérifie s'il y a des cases adjacentes et on les dévoillent
                    if ligne+1<longueur:
                        reveal(ligne+1,colonne)
                    if colonne-1>=0 and ligne+1<longueur:
                        reveal(ligne+1,colonne-1)
                    if colonne+1<largeur and ligne+1<longueur:
                        reveal(ligne+1,colonne+1)
                    if ligne-1>=0:
                        reveal(ligne-1,colonne)
                    if ligne-1>=0 and colonne+1<largeur:
                        reveal(ligne-1,colonne+1)
                    if ligne-1>=0 and colonne-1>=0:
                        reveal(ligne-1,colonne-1)
                    if colonne+1<largeur:
                        reveal(ligne,colonne+1)
                    if colonne-1>=0:
                        reveal(ligne,colonne-1)

                else:
                    #Gestion des cases normals :
                    #On modifie l'attribut reveal de la case pour ne pas
                    #Dévoiller plusieur fois la même case
                    Grille1.grille[ligne][colonne].reveal=True

                    #On dévoille la case
                    buttons[ligne][colonne].configure(bg="#DACE91", text=Grille1.grille[ligne][colonne].valeur)
                    victoire()


def right_click(event):
    '''
    Fonction gérant l'évenement lié au clic droit de la souris.
    Permet de mettre ou d'enlever un drapeau d'une case.
    '''
    #On récupère la position dans la grille du bouton cliqué
    row=event.widget.grid_info()['row']
    column=event.widget.grid_info()['column']
    bouton=buttons[row][column]

    #On vérifie qu'il n'y a pas de drapeau sur la case et que la case n'est pas dévoillée
    if Grille1.grille[row][column].drapeau==False and Grille1.grille[row][column].reveal==False:
        Grille1.grille[row][column].drapeau=True
        bouton.configure(bg='red', activebackground='red',image=image_flag)

    #S'il y a déja un drapeau sur la case on l'enlève
    elif Grille1.grille[row][column].drapeau==True:
        Grille1.grille[row][column].drapeau=False
        bouton.configure(bg='#37B13B', activebackground='#FCE6B6',image='')


def debut():
    '''
    Fonction qui découvre une zone vide aléatoirement selectionnée dans la
    grille pour permettre au joueur de commencer.
    '''
    point_de_départ=-1
    while point_de_départ!=0:
        L=randint(0, longueur-1)
        l=randint(0, largeur-1)
        point_de_départ=Grille1.grille[L][l].valeur
    reveal(L,l)




#Adaptation de la taille des cases en fonction du nombre de cases
case_width=8
if longueur>8 or largeur>18:
    case_width=6
if longueur>11 or largeur>24:
    case_width=4
    taille_image_flag=20
if longueur>15 or largeur>32:
    case_width=2
    taille_image_flag=24


#Import et redimension de l'image du drapeau
image_flag = PhotoImage(file = r"Images\flag.png")
image_flag = image_flag.subsample(taille_image_flag,taille_image_flag)


#Génération des boutons dans la grille
buttons = [[None]*largeur for _ in range(longueur)]

for ligne in range(longueur):
    for colonne in range(largeur):
            buttons[ligne][colonne] = Button(Frame1,cursor="tcross", bg='#37B13B', activebackground='#FCE6B6', width=case_width, height=int(case_width/2), command=lambda r=ligne,c=colonne: reveal(r,c))
            buttons[ligne][colonne].bind("<Button-3>", right_click)
            buttons[ligne][colonne].grid(row=ligne, column=colonne, sticky="nsew")


#Début de la partie et du chronomètre
debut()
temps_depart=time()



fenetre.mainloop()

