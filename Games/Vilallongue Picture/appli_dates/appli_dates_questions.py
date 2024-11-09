import random

def construction_listes(liste_de_paquets):
    liste = []
    for paquet in liste_de_paquets:
        nom_paquet = 'paquets/chroni/' + paquet
        with open(nom_paquet, 'r', encoding='utf8') as fichier:
            while True:
                txt = fichier.readline()
                if txt == '':
                    break
                liste.append(txt[:-1].split(";")+[paquet[:-4]]) # on ajoute le nom du paquet sans l'extension .csv
    return liste

def mise_en_forme_date(liste_de_listes):
    for e in liste_de_listes:
        e[0] = int(e[0].replace(" ","").replace("Vers","").split(',')[0])
    return liste_de_listes


def affiche_liste(liste_de_listes):
    for e in liste_de_listes:
        print(str(e)[1:-1]) # ne pas afficher les crochets

def filtre_dates(liste_de_listes, inf, sup):
    liste_filtre = []
    for e in liste_de_listes:
        if  inf <= e[0] <= sup:
            liste_filtre.append(e)
    return liste_filtre

def question_au_hasard(liste_de_listes):
    ligne = random.choice(liste_de_listes)
    question = ligne[1]
    reponse = ligne[0]
    x = int(input(question))
    if x == reponse:
        print("Exact!")
    else:
        print("Non, la réponse était",reponse)
        print("Vous vous êtes trompé de", abs(reponse-x))

def quiz_de_n_questions(liste_de_listes, n):
    lignes = random.sample(liste_de_listes, n)
    erreur_totale = 0
    reponse_ok = 0
    for ligne in lignes:
        question = ligne[1]
        reponse = ligne[0]
        x = int(input(question))
        if x == reponse:
            print("Exact!")
            reponse_ok += 1
        else:
            print("Non, la réponse était",reponse)
            erreur = abs(reponse-x)
            print("Vous vous êtes trompé de", erreur)
            erreur_totale += erreur
    print("Vous avez un total de", reponse_ok, "sur", n)
    print("Vous vous êtes en moyenne trompé de", erreur_totale / n)

def recherche(liste_de_listes, texte):
    liste_res = []
    for e in liste_de_listes:
        if texte in e[1]:
            liste_res.append(e)
    return liste_res

def annees_en_doublons(liste_de_listes):
    n = len(liste_de_listes)
    liste_res = []
    # cas de la permière ligne
    if n>=2 and liste_de_listes[0][0] == liste_de_listes[1][0]:
        liste_res.append(liste_de_listes[0])
    # cas général
    for i in range(1, n-1):
        if liste_de_listes[i][0] == liste_de_listes[i-1][0] or \
            liste_de_listes[i][0] == liste_de_listes[i+1][0]:
            liste_res.append(liste_de_listes[i])
    # cas de la dernière ligne
    if n>=2 and liste_de_listes[n-2][0] == liste_de_listes[n-1][0]:
        liste_res.append(liste_de_listes[n])
    return liste_res

ma_liste_de_paquets = ['histoire de france.csv', \
                        'histoire du monde.csv', \
                        'histoire de la litterature.csv', \
                        'histoire des arts.csv', \
                        'les femmes celebres.csv', \
                        'les merveilles du monde.csv', \
                        'les rois et reines de france.csv', \
                        'les grandes inventions.csv', \
                        'les monuments de france.csv']
liste_de_listes = construction_listes(ma_liste_de_paquets)
liste_de_listes = mise_en_forme_date(liste_de_listes)
liste_de_listes.sort()

"""
    PARTIE QUESTIONS / REPONSES
"""

"""
# Affiche tout
affiche_liste(liste_de_listes)

# Combien de cartes au 20ème siècle?
Q1 = len(filtre_dates(liste_de_listes, 1900, 2000))
print(Q1)

# Combien de cartes au 19ème siècle?
Q2 = len(filtre_dates(liste_de_listes, 1800, 1900))
print(Q2)

# Toutes les cartes entre 1650 et 1700
Q3 = filtre_dates(liste_de_listes, 1650, 1700)
affiche_liste(Q3)

# Que s'est-il passé en telle année?
x = 400
Q4 = filtre_dates(liste_de_listes, x, x)
affiche_liste(Q4)

# Tire une question au hasard
question_au_hasard(liste_de_listes)

# Fait un quiz de n questions et affiche la note
n = 5
quiz_de_n_questions(liste_de_listes, n)

# Fait une recherche
mot = "Rochelle"
affiche_liste(recherche(liste_de_listes, mot))

# Quelles sont les années les plus importantes, car en doublons?
affiche_liste(annees_en_doublons(liste_de_listes))

# Eléments ayant la même dates étant à la fois dans la rubrique 'histoire du monde'
# et dans la rubrique 'les merveilles du monde' ?
res = []
for e in liste_de_listes:
    if e[2] == 'histoire du monde' or e[2] == 'les merveilles du monde':
        res.append(e)
affiche_liste(annees_en_doublons(res))
"""

"""
    PARTIE JEUX
"""

def filtre_paquet(liste_de_listes):
    paquet = []
    for e in liste_de_listes:
        if e[2] == "histoire de france":
            paquet.append(e)
    return paquet

def pioche_carte(paquet):
    nb_cartes = len(paquet)
    x = random.randint(0, nb_cartes - 1)
    carte = paquet[x]
    del paquet[x]
    return carte

def init_jeux_joueurs(jeu_joueur1, jeu_joueur2, nb_cartes):
    for i in range(nb_cartes):
        jeu_joueur1.append(pioche_carte(paquet))
    for i in range(nb_cartes):
        jeu_joueur2.append(pioche_carte(paquet))

def affiche_cartes(liste_de_listes):
    for i in range(len(liste_de_listes)):
        print("    "+str(i)+" -> "+str(liste_de_listes[i])[1:-1]) # ne pas afficher les crochets

def affiche_recto(liste_de_listes):
    for i in range(len(liste_de_listes)):
        print("    "+str(i)+" -> "+str(liste_de_listes[i][1:])[1:-1]) # ne pas afficher les crochets

def affiche_plateau(jeu_joueur1, jeu_joueur2, jeu_central):
    print("Jeu du joueur 1 :")
    #affiche_recto(jeu_joueur1)
    affiche_cartes(jeu_joueur1)
    print()
    print("Jeu du joueur 2 :")
    #affiche_recto(jeu_joueur2)
    affiche_cartes(jeu_joueur2)
    print()
    print("Jeu central")
    affiche_cartes(jeu_central)
    print()


def affiche_jeu_joueur_courant(jeu_joueur_courant, nom_joueur_courant):
    print("Jeu du joueur : "+ nom_joueur_courant)
    #affiche_recto(jeu_joueur_courant)
    affiche_cartes(jeu_joueur_courant)
    print()

def affiche_jeu_central(jeu_central):
    print("Jeu central")
    for i in range(len(jeu_central)):
        print(" --> "+str(i))
        print("    "+str(jeu_central[i])[1:-1]) # ne pas afficher les crochets
    print(" --> "+str(i+1))


# Jouer avec un paquet précis
paquet = filtre_paquet(liste_de_listes)

# Mélange aléatoire des cartes
random.seed(0.7) # pour tester en ayant toujours les mêmes jeux
random.shuffle(paquet)

# Chacun pioche 5 cartes (différentes) aléatoirement pour constituer son jeu
jeu_joueur1 = []
jeu_joueur2 = []
nb_cartes = 2
init_jeux_joueurs(jeu_joueur1, jeu_joueur2, nb_cartes)

# initialisation du jeu central
jeu_central = [pioche_carte(paquet)]

#=================================
# boucle principale du jeu
#=================================
gagné = False
nom_joueur_courant = "J1" # c'est le tour du joueur 1
jeu_joueur_courant = jeu_joueur1
while not gagné: # tant qu'aucun des deux joueurs n'a gagné
    # affichage du plateau
    affiche_jeu_joueur_courant(jeu_joueur_courant, nom_joueur_courant)
    affiche_jeu_central(jeu_central)
    ind_carte = int(input(nom_joueur_courant + " : quel numéro de carte choisissez-vous?"))
    carte = jeu_joueur_courant[ind_carte]
    print("Vous avez sélectionné la carte : "+str(carte))
    i = int(input(nom_joueur_courant + " : où placez-vous votre carte?"))
    # si l'index i est le bon, on met à jour le jeu central
    if i == 0: # cas particulier 1 : en début de jeu central
        if jeu_joueur_courant[ind_carte][0] < jeu_central[0][0]: # ok
            print("La carte choisie est bien placée.")
            del jeu_joueur_courant[ind_carte]
            jeu_central.insert(0, carte)
        else: # erreur et on pioche
            carte_piochée = pioche_carte(paquet)
            jeu_joueur_courant.append(carte_piochée)
            print("La carte choisie est mal placée. Vous piochez et obtenez :"+str(carte_piochée))
    elif i == len(jeu_central): # cas particulier 2 : en fin de jeu central
        if jeu_joueur_courant[ind_carte][0] > jeu_central[len(jeu_central)-1][0]: # ok
            del jeu_joueur_courant[ind_carte]
            jeu_central.insert(len(jeu_central), carte)
        else: # erreur et on pioche
            carte_piochée = pioche_carte(paquet)
            jeu_joueur_courant.append(carte_piochée)
            print("La carte choisie est mal placée. Vous piochez et obtenez :"+str(carte_piochée))
    else: # cas général
        if jeu_central[i-1][0] < jeu_joueur_courant[ind_carte][0]  and jeu_joueur_courant[ind_carte][0] < jeu_central[i][0]: # ok
            del jeu_joueur_courant[ind_carte]
            jeu_central.insert(i, carte)
        else:  # erreur et on pioche
            carte_piochée = pioche_carte(paquet)
            jeu_joueur_courant.append(carte_piochée)
            print("La carte choisie est mal placée. Vous piochez et obtenez :"+str(carte_piochée))
    print()

    # on teste si le jeu est vide, auquel cas le joueur a gagné
    if len(jeu_joueur_courant) == 0:
        gagné = True
        print("Bravo au joueur "+nom_joueur_courant+". Vous avez gagné!")
    else:
        # changement de joueur
        if nom_joueur_courant == "J1":
            nom_joueur_courant = "J2"
            jeu_joueur_courant = jeu_joueur2
        else: # nom_joueur_courant == "J2"
            nom_joueur_courant = "J1"
            jeu_joueur_courant = jeu_joueur1

