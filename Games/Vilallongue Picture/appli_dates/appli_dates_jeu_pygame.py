import random
import pygame
from pygame.locals import *


"""
 Initialisation des constantes
"""
LARGEUR_FENETRE = 1200
HAUTEUR_FENETRE = 563
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


"""
 Définition des fonctions
"""
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

def construit_paquet_de_cartes(liste_de_listes):
    paquet = PaquetDeCartes()
    for e in liste_de_listes:
        carte = Carte(e[0], e[1], e[2])
        paquet.ajoute(carte)
    return paquet

def construit_paquet_joueur(paquet, nb_cartes):
    new_paquet = PaquetDeCartes()
    for i in range(nb_cartes):
        new_paquet.ajoute(paquet.pioche_carte())
    return new_paquet

def afficher_texte(texte_str, color, abscisse, ordonnee, largeur_texte) :
    liste_splitee = texte_str.split()
    nb_mots = len(liste_splitee)
    i = 0 # indice du mot
    chaine = ""
    while i < nb_mots :
        chaine_sans_dernier_mot = chaine
        longueur = font.size(chaine)[0]
        while longueur < largeur_texte and i < nb_mots :
            chaine_sans_dernier_mot = chaine
            chaine = chaine + " " + liste_splitee[i]
            longueur = font.size(chaine)[0]
            i += 1
        if longueur < largeur_texte :
            texte = font.render(chaine.lstrip(), 1, color)
            fenetre.blit(texte, (abscisse, ordonnee))
            chaine = ""
        else :
            texte = font.render(chaine_sans_dernier_mot.lstrip(), 1, color)
            chaine = liste_splitee[i-1]
            fenetre.blit(texte, (abscisse, ordonnee))
        ordonnee += font.get_height()
        if i == nb_mots :
            texte = font.render(chaine, 1, color)
            fenetre.blit(texte, (abscisse, ordonnee))

def affiche_jeu_central(jeu, y_énoncé, i):
    """ Affichage concernant le jeu central
    """
    global zc1, zc2, bouton_prev_jeu_central, pos_bouton_prev_jeu_central, bouton_next_jeu_central, pos_bouton_next_jeu_central, zc_c, zc_g, zc_d
    largeur_zone_cliquable = 70
    hauteur_zone_cliquable = 40
    y_date = y_énoncé + 150
    if len(jeu.contenu) == 1:
        carte = jeu.contenu[i]
        date, énoncé = str(carte.date), carte.énoncé
        x = LARGEUR_FENETRE / 2 - Carte.largeur / 2
        # affichage carte
        pygame.draw.rect(fenetre, Carte.couleur, (x, y_énoncé, Carte.largeur, Carte.hauteur))
        pygame.draw.rect(fenetre, Carte.couleur_bord, (x, y_énoncé, Carte.largeur, Carte.hauteur), 5)
        afficher_texte(énoncé, Carte.couleur_texte, x+10, y_énoncé, Carte.largeur)
        afficher_texte(date, Carte.couleur_texte, x+Carte.largeur-75, y_date, Carte.largeur)
        # affichage de zone cliquables
        zc1 = pygame.draw.rect(fenetre, RED, ((LARGEUR_FENETRE/2-Carte.largeur/2)/2 - largeur_zone_cliquable/2, y_énoncé + Carte.hauteur - hauteur_zone_cliquable, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
        zc2 = pygame.draw.rect(fenetre, RED, ((LARGEUR_FENETRE/2+Carte.largeur/2+LARGEUR_FENETRE)/2 - largeur_zone_cliquable/2, y_énoncé + Carte.hauteur - hauteur_zone_cliquable, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
    else: # deux cartes ou plus dans le jeu
        carte = jeu.contenu[i]
        carte2 = jeu.contenu[i+1]
        date, énoncé = str(carte.date), carte.énoncé
        date2, énoncé2 = str(carte2.date), carte2.énoncé
        x1 = (LARGEUR_FENETRE - 2 * Carte.largeur) / 3
        x2 = 2 * (LARGEUR_FENETRE - 2 * Carte.largeur) / 3 + Carte.largeur
        # affichage carte 1
        pygame.draw.rect(fenetre, Carte.couleur, (x1, y_énoncé, Carte.largeur, Carte.hauteur))
        pygame.draw.rect(fenetre, Carte.couleur_bord, (x1, y_énoncé, Carte.largeur, Carte.hauteur), 5)
        afficher_texte(énoncé, Carte.couleur_texte, x1+10, y_énoncé, Carte.largeur)
        afficher_texte(date, Carte.couleur_texte, x1+Carte.largeur-75, y_date, Carte.largeur)
        # affichage carte 2
        pygame.draw.rect(fenetre, Carte.couleur, (x2, y_énoncé, Carte.largeur, Carte.hauteur))
        pygame.draw.rect(fenetre, Carte.couleur_bord, (x2, y_énoncé, Carte.largeur, Carte.hauteur), 5)
        afficher_texte(énoncé2, Carte.couleur_texte, x2+10, y_énoncé, Carte.largeur)
        afficher_texte(date2, Carte.couleur_texte, x2+Carte.largeur-75, y_date, Carte.largeur)
        # affichage zone cliquable centrale
        zc_c = pygame.draw.rect(fenetre, RED, (LARGEUR_FENETRE/2- largeur_zone_cliquable/2, y_énoncé + Carte.hauteur - hauteur_zone_cliquable, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
        if i == 0:
            # affichage à gauche d'une zone cliquable
            zc_g = pygame.draw.rect(fenetre, RED, (x1/2 - largeur_zone_cliquable/2, y_énoncé + Carte.hauteur - hauteur_zone_cliquable, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
        else:
            # affichage à gauche un bouton
            largeur_bouton = 50
            hauteur_bouton =  50
            bouton_prev_jeu_central = pygame.image.load("images/prev.png").convert_alpha()
            pos_bouton_prev_jeu_central = bouton_prev_jeu_central.get_rect(topleft=(x1/2 - largeur_zone_cliquable/2, y_énoncé + Carte.hauteur/2 - hauteur_bouton/2))
            fenetre.blit(bouton_prev_jeu_central, pos_bouton_prev_jeu_central)
        if i == jeu.get_nb_cartes() - 2 :
            # affichage à droite d'une zone cliquable
            zc_d = pygame.draw.rect(fenetre, RED, ((x2 + Carte.largeur + LARGEUR_FENETRE)/2 - largeur_zone_cliquable/2, y_énoncé + Carte.hauteur - hauteur_zone_cliquable, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
        else:
            # affichage à droite un bouton
            largeur_bouton = 50
            hauteur_bouton =  50
            bouton_next_jeu_central = pygame.image.load("images/next.png").convert_alpha()
            pos_bouton_next_jeu_central = bouton_next_jeu_central.get_rect(topleft=((x2 + Carte.largeur + LARGEUR_FENETRE)/2 - largeur_bouton/2, y_énoncé + Carte.hauteur/2 - hauteur_bouton/2))
            fenetre.blit(bouton_next_jeu_central, pos_bouton_next_jeu_central)


def affiche_jeu_joueur(jeu, y_énoncé, i):
    """ Affichage concernant un joueur
        Affiche la ième carte
    """
    global bouton_prev_joueur, pos_bouton_prev_joueur, bouton_next_joueur, pos_bouton_next_joueur
    y_date = y_énoncé + 150
    if len(jeu.contenu) >= 1:
        carte = jeu.contenu[i]
        date, énoncé = str(carte.date), carte.énoncé
        x = LARGEUR_FENETRE / 2 - Carte.largeur / 2
        # affichage carte
        pygame.draw.rect(fenetre, Carte.couleur, (x, y_énoncé, Carte.largeur, Carte.hauteur))
        pygame.draw.rect(fenetre, Carte.couleur_bord, (x, y_énoncé, Carte.largeur, Carte.hauteur), 5)
        afficher_texte(énoncé, Carte.couleur_texte, x+10, y_énoncé, Carte.largeur)
        #afficher_texte(date, Carte.couleur_texte, x+Carte.largeur-75, y_date, Carte.largeur)
        # affichage des boutons
        hauteur_bouton = 50
        bouton_prev_joueur = pygame.image.load("images/prev.png").convert_alpha()
        pos_bouton_prev_joueur = bouton_prev_joueur.get_rect(topleft=(LARGEUR_FENETRE / 4, y_énoncé_joueur_courant + Carte.hauteur/2 - hauteur_bouton/2))
        bouton_next_joueur = pygame.image.load("images/next.png").convert_alpha()
        pos_bouton_next_joueur = bouton_next_joueur.get_rect(topleft=(3 * LARGEUR_FENETRE / 4, y_énoncé_joueur_courant + Carte.hauteur/2 - hauteur_bouton/2))
        if jeu.get_nb_cartes() > 1:
            if i != 0:
                fenetre.blit(bouton_prev_joueur, pos_bouton_prev_joueur)
            if i != jeu.get_nb_cartes() - 1:
                fenetre.blit(bouton_next_joueur, pos_bouton_next_joueur)

"""
 Définition des classes
"""
class Carte():

    largeur = 350
    hauteur = 200
    couleur = (255, 255, 255)
    couleur_bord = (0, 0, 0)
    couleur_texte = (0, 0, 0)

    def __init__(self, date, énoncé, catégorie, sens="recto"):
        self.date = date
        self.énoncé = énoncé
        self.catégorie = catégorie
        self.sens = sens

    def retourne(self):
        if self.sens == "recto":
            self.sens = "verso"
        else:
            self.sens = "recto"

    def get_date(self):
        return self.date

    def get_énoncé(self):
        return self.énoncé

    def get_catégorie(self):
        return self.catégorie

    def get_sens(self):
        return self.sens


class PaquetDeCartes():

    def __init__(self):
        self.contenu = []

    def ajoute(self, carte):
        self.contenu.append(carte)

    def ajoute_carte_indice_i(self, i, carte):
        self.contenu.insert(i, carte)

    def retire_carte_indice_i(self, i):
        return self.contenu.pop(i)

    def get_carte_indice_i(self, i):
        return self.contenu[i]

    def filtre_sur_catégorie(self, catégorie):
        new_contenu = []
        for carte in self.contenu:
            if carte.catégorie == catégorie:
                new_contenu.append(carte)
        self.contenu = new_contenu

    def filtre_sur_dates(self, a, b):
        new_contenu = []
        for carte in self.contenu:
            if a <= carte.date <= b:
                new_contenu.append(carte)
        self.contenu = new_contenu

    def pioche_carte(self):
        nb_cartes = len(self.contenu)
        x = random.randint(0, nb_cartes - 1)
        carte = self.contenu[x]
        del self.contenu[x]
        return carte

    def get_nb_cartes(self):
        return len(self.contenu)


class Joueur():

    def __init__(self, nom, paquet):
        self.nom = nom
        self.paquet = paquet

    def get_paquet(self):
        return self.paquet

#======================
# Partie Construction de la liste de liste
#======================
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
 Initialisation de la fenêtre Pygame
"""
# Initialisation de la bibliothèque Pygame
pygame.init()
# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
pygame.display.set_icon(pygame.image.load("images/jblt_80_80.jpg"))
fond = pygame.image.load("images/pngtree-pastel-colorful-background-clouds-picture-image_1162170.jpg").convert()

fenetre.blit(fond,(0,0))
# Gestion du titre en haut de la fenêtre
pygame.display.set_caption("Appli")

#-------------------------------------
# Pour afficher un texte dans pygame
#-------------------------------------
font = pygame.font.Font("BradBunR.ttf", 40)

# Mélange aléatoire des cartes
#random.seed(0.7) # pour tester en ayant toujours les mêmes jeux

paquet = construit_paquet_de_cartes(liste_de_listes)
#paquet.filtre_sur_catégorie("histoire de france")
#paquet.filtre_sur_dates(1000, 2000)

joueur1 = Joueur("J1", construit_paquet_joueur(paquet, 10))
i_joueur1 = 0
joueur2 = Joueur("J2", construit_paquet_joueur(paquet, 5))
i_joueur2 = 0

jeu_central = PaquetDeCartes()
jeu_central.ajoute(paquet.pioche_carte())

i_paquet_central = 0

jeu_joueur_courant = joueur1.paquet
i_joueur_courant = i_joueur1

y_énoncé = 50
y_énoncé_joueur_courant = 350

texte = font.render("Jeu central", 1, BLACK)
fenetre.blit(texte, (20, 0))

zc_c, zc1, zc2 = None, None, None
affiche_jeu_central(jeu_central, y_énoncé, i_paquet_central)

texte = font.render("Jeu joueur "+joueur1.nom, 1, BLACK)
fenetre.blit(texte, (20, 300))
affiche_jeu_joueur(jeu_joueur_courant, y_énoncé_joueur_courant, i_joueur_courant)

continuer = True
while continuer :

    pygame.display.flip() # Rafraichissement

    # Gestion des événements
    for event in pygame.event.get():

        # Evènements liés à la zone centrale
        # Partie zones cliquables
        if event.type == pygame.MOUSEBUTTONUP:
            if jeu_central.get_nb_cartes() == 1 and zc1.collidepoint(event.pos) or \
                jeu_central.get_nb_cartes() > 1 and i_paquet_central == 0 and zc_g.collidepoint(event.pos):
                print('clic à gauche')
                if jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() <= jeu_central.get_carte_indice_i(i_paquet_central).get_date():
                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                    jeu_central.ajoute_carte_indice_i(0, carte_jouée)
                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                        i_joueur_courant -= 1

            # ajout à droite avec une seule carte dans le jeu central
            elif jeu_central.get_nb_cartes() == 1 and zc2.collidepoint(event.pos):
                print('clic à droite')
                if jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() >= jeu_central.get_carte_indice_i(i_paquet_central).get_date():
                    print('cas ok')
                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                    jeu_central.ajoute_carte_indice_i(jeu_central.get_nb_cartes(), carte_jouée)
                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                        i_joueur_courant -= 1

            # ajout à droite avec au moins deux cartes dans le jeu central
            elif jeu_central.get_nb_cartes() > 1 and i_paquet_central == jeu_central.get_nb_cartes() - 2 and zc_d.collidepoint(event.pos):
                print('clic à droite')
                if jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() >= jeu_central.get_carte_indice_i(i_paquet_central + 1).get_date():
                    print('cas ok')
                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                    jeu_central.ajoute_carte_indice_i(jeu_central.get_nb_cartes(), carte_jouée)
                    i_paquet_central += 1
                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                        i_joueur_courant -= 1

            elif jeu_central.get_nb_cartes() > 1 and zc_c.collidepoint(event.pos):
                print('clic au milieu')
                if jeu_central.get_carte_indice_i(i_paquet_central).get_date() <= jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() <= jeu_central.get_carte_indice_i(i_paquet_central+1).get_date():
                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                    jeu_central.ajoute_carte_indice_i(i_paquet_central + 1, carte_jouée)
                    #i_paquet_central += 1
                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                        i_joueur_courant -= 1
            # Evènements liés à la zone centrale
            # Partie zones de défilement : previous et next
            elif jeu_central.get_nb_cartes() > 1 and i_paquet_central != 0 and pos_bouton_prev_jeu_central.collidepoint(event.pos) :
                i_paquet_central -= 1
                print(i_paquet_central)
            elif jeu_central.get_nb_cartes() > 1 and i_paquet_central != jeu_central.get_nb_cartes() - 2 and pos_bouton_next_jeu_central.collidepoint(event.pos) :
                i_paquet_central += 1
                print(i_paquet_central)
            # Evènements liés à la zone du joueur
            elif pos_bouton_prev_joueur.collidepoint(event.pos) and i_joueur_courant > 0:
                i_joueur_courant -= 1
            elif pos_bouton_next_joueur.collidepoint(event.pos) and i_joueur_courant < jeu_joueur_courant.get_nb_cartes()-1:
                i_joueur_courant += 1

            fenetre.blit(fond,(0,0))
            texte = font.render("Jeu central", 1, BLACK)
            fenetre.blit(texte, (20, 0))
            texte = font.render("Jeu joueur "+joueur1.nom, 1, BLACK)
            fenetre.blit(texte, (20, 300))

            print()
            print(i_paquet_central)
            print(i_joueur_courant)

            affiche_jeu_joueur(jeu_joueur_courant, y_énoncé_joueur_courant, i_joueur_courant)
            affiche_jeu_central(jeu_central, y_énoncé, i_paquet_central)

        # Pour quitter en fermant la fenêtre
        if event.type == QUIT:
            pygame.quit()
            continuer = False
    """
    if jeu_joueur_courant.get_nb_cartes() == 0:
        pygame.quit()
        continuer = False
    """
