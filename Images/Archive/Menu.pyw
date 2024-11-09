# Créé par Nicolas, le 18/11/2021 en Python 3.7

"""Chargement des modules et installation si necessaire"""

étape_programme = "Importation des modules"

import pip
import os
from zipfile import ZipFile
import time
import random
import datetime

continuer = True
erreur_report = False
test=True
try:
    import music_tag
    import psutil
    import pygame

    test = False

    from pygame.locals import *
    fenetre = pygame.display.set_mode((1280,720))
    pygame.init()

except ModuleNotFoundError:
    os.startfile("All update.bat")


"""Importation des données externes"""

try:
    étape_programme = "Importation des fichiers externes"
    from Version_Menu import*
    from Version_Level import*
    from Version_LevelC import*
    from Version_Update import*
    from Parametres import*
    from Fond import*
    from Couleur import*
    from Couleur_r import*
    from Transition import*
    from First_start import*
    from AdaptoRAM import*
    from Variables import*
    from Jauge_choix import*
    from Menu_choix import*
    from Widgets_soundtrack_pos import*
    from Widgets_level_pos import*

    """Initialisation des variables des programmes enchassés"""

    étape_programme = "Variables"

    décalage_widget = [0,0]
    RAM_free = 8000000000
    full=1
    x=0
    p=1
    lecture=True
    titre=""
    temps=0
    avance=0
    position_selecteur = 0
    liste = []

    étape_programme = "Analyse des pistes audios (lecteur multimédia)"

    for i in range(1,39):
        f = music_tag.load_file("WALL-E [Original Score]/"+str(i)+".mp3")
        liste.append(str(f ['title']))

    f = music_tag.load_file("WALL-E [Original Score]/1.mp3")

    """Iniatialisation de la fenêtre Pygame"""
    étape_programme = "Configuration/ouverture de la fenêtre"

    pygame.init()
    fenetre = pygame.display.set_mode((1280,720))
    pygame.display.set_icon(pygame.image.load("Images/BNLalpha.png"))
    pygame.display.set_caption("BNL's Box (Windows Python edition)")

    """Chargement des images"""

    # Initialisation du fond d'écran
    étape_programme = "Chargement des images/positions"
    if fond_selection==1:
        Gauche = pygame.image.load("Images/fondmenu/Gauche.png").convert()
        fondmenu = pygame.image.load("Images/fondmenu/fondmenu.png").convert()
        Droite = pygame.image.load("Images/fondmenu/Droite.png").convert()
    elif fond_selection==2:
        Gauche = pygame.image.load("Images/fondmenu1/Gauche.png").convert()
        fondmenu = pygame.image.load("Images/fondmenu1/fondmenu.png").convert()
        Droite = pygame.image.load("Images/fondmenu1/Droite.png").convert()
    elif fond_selection==3:
        Gauche = pygame.image.load("Images/fondmenu3/Gauche.png").convert()
        fondmenu = pygame.image.load("Images/fondmenu3/fondmenu.jpg").convert()
        Droite = pygame.image.load("Images/fondmenu3/Droite.png").convert()
    elif fond_selection==4:
        Gauche = pygame.image.load("Images/fondmenu4/Gauche.png").convert()
        fondmenu = pygame.image.load("Images/fondmenu4/fondmenu.jpg").convert()
        Droite = pygame.image.load("Images/fondmenu4/Droite.png").convert()
    elif fond_selection==5:
        Gauche = pygame.image.load("Images/fondmenu5/Gauche.jpg").convert()
        fondmenu = pygame.image.load("Images/fondmenu5/fondmenu.jpg").convert()
        Droite = pygame.image.load("Images/fondmenu5/Droite.jpg").convert()

    # Chargement des images du lecteur multimédia
    Son = pygame.image.load("Miniature/Soundtrack.png").convert()
    Lecture = pygame.image.load("Images/Lecture.png").convert_alpha()
    Pause = pygame.image.load("Images/Pause.png").convert()
    Avancer = pygame.image.load("Images/Avancer.png").convert()
    Reculer = pygame.image.load("Images/Reculer.png").convert()
    Lecture1 = pygame.image.load("Images/Lecture1.png").convert_alpha()
    Pause1 = pygame.image.load("Images/Pause1.png").convert()
    Avancer1 = pygame.image.load("Images/Avancer1.png").convert()
    Reculer1 = pygame.image.load("Images/Reculer1.png").convert()

    # Chargement du fond d'écran (Paramètres -> Personnalisation)
    fondmenu_a = pygame.image.load("Miniature/fondmenu.png").convert()
    fondmenu1_a = pygame.image.load("Miniature/fondmenu1.png").convert()
    fondmenu3_a = pygame.image.load("Miniature/fondmenu3.jpg").convert()
    fondmenu4_a = pygame.image.load("Miniature/fondmenu4.jpg").convert()
    fondmenu5_a = pygame.image.load("Miniature/fondmenu5.jpg").convert()

    # Chargement des témoins couleurs (Paramètres -> Personnalisation)
    Rouge = pygame.image.load("Parametres/Rouge.png").convert()
    Bleu = pygame.image.load("Parametres/Bleu.png").convert()
    Violet = pygame.image.load("Parametres/Violet.png").convert()
    Vert = pygame.image.load("Parametres/Vert.png").convert()
    Jaune = pygame.image.load("Parametres/Jaune.png").convert()
    Cyan = pygame.image.load("Parametres/Cyan.png").convert()

    # Chargement des sélecteurs du menu principal et du lecteur multimédia
    Selection_menu = pygame.image.load("Menu/Selection_menu.png").convert_alpha()
    Selection_soundtrack = pygame.image.load("Menu/Selection_soundtrack.png").convert_alpha()

    # Chargement du fond de clarté

    fond_visibilité = pygame.image.load("Parametres/fond_visibilite.png").convert_alpha()

    # Chargement des boutons du menu d'information quant aux systèmes de mise à niveau/quant aux nouveautés
    bouton_Python = pygame.image.load("Parametres/Python_bouton.png").convert_alpha()
    bouton_C = pygame.image.load("Parametres/C#_bouton.png").convert_alpha()
    bouton_Abord = pygame.image.load("Parametres/Annuler_bouton.png").convert_alpha()
    bouton_OK = pygame.image.load("Parametres/Bouton_OK.png").convert_alpha()

    # Chargement du témoin de sélection (Paramètres -> Personnalisation)
    Selection = pygame.image.load("Images/BNL1.png").convert_alpha()

    # Chargement des icônes du menu Bonus
    PUB = pygame.image.load("Miniature/PUB.png").convert()
    Truck= pygame.image.load("Miniature/Truck.png").convert()
    Floor= pygame.image.load("Miniature/Floor.png").convert()
    Deck= pygame.image.load("Miniature/Deck.png").convert()
    Dock= pygame.image.load("Miniature/Dock.png").convert()
    Captain= pygame.image.load("Miniature/Captain.png").convert()
    Pool= pygame.image.load("Miniature/Pool.png").convert()
    Earth= pygame.image.load("Miniature/Earth.png").convert()
    Axiom= pygame.image.load("Miniature/Axiom.png").convert()
    Preview= pygame.image.load("Miniature/Preview.png").convert()
    Trash= pygame.image.load("Miniature/Trash.png").convert()

    # Chargement des icônes du menu principal
    BNLmenu= pygame.image.load("Menu/Parametres.png").convert_alpha()
    DVD = pygame.image.load("Images/DVD.png").convert_alpha()
    Soundtrack = pygame.image.load("Menu/Soundtrack.png").convert_alpha()
    Solar = pygame.image.load("Menu/Solar.png").convert_alpha()
    Bonus = pygame.image.load("Menu/Bonus.png").convert_alpha()
    Autre = pygame.image.load("Images/Autre.png").convert()

    # Chargement de l'icône de retour au menu principal
    Menu = pygame.image.load("Images/BNLalpha.png").convert_alpha()

    # Chargement du fond du menu Bonus
    fondbonus = pygame.image.load("Bonus/Bonus88.png").convert_alpha()

    # Chargement des tuiles du menu Paramètres
    Version = pygame.image.load("Miniature/Version.png").convert()

    # Chargement du curseur du lecteur multimédia
    Curseur = pygame.image.load("Images/Statut.png").convert_alpha()

    # Chargement des tuiles du menu Paramètres
    Infos= pygame.image.load("Parametres/Infos.png").convert()
    Infos1= pygame.image.load("Parametres/Infos1.png").convert()
    Modules= pygame.image.load("Parametres/Modules.png").convert()
    Modules1= pygame.image.load("Parametres/Modules1.png").convert()
    Animations= pygame.image.load("Parametres/Animations.png").convert()
    Animations1= pygame.image.load("Parametres/Animations1.png").convert()
    touche_vide= pygame.image.load("Parametres/touche_vide.png").convert()
    Fond_paramètres= pygame.image.load("Parametres/Fond_parametres.png").convert()
    Fond_paramètres1= pygame.image.load("Parametres/Fond_parametres1.png").convert()

    # Chargement du fond noir (universel)
    fondmulti= pygame.image.load("Images/fondmulti.png").convert()

    # Chargement des boutons ON/OFF du menu Paramètres
    ON= pygame.image.load("Parametres/ON.png").convert()
    ON1= pygame.image.load("Parametres/ON1.png").convert()
    OFF= pygame.image.load("Parametres/OFF.png").convert()
    OFF1= pygame.image.load("Parametres/OFF1.png").convert()

    # Chargement de l'icône de retour au menu principal (Lecteur multimédia)
    Menu1 = pygame.image.load("Images/Menu.png").convert()
    Menu11 = pygame.image.load("Images/Menu1.png").convert()

    # Chargement de l'image de présentation des jeux

    Gauche_f = pygame.image.load("Jeux/Mini Picture Original/Cartes/Gauche1.png")
    Gauche_fp = pygame.image.load("Jeux/Mini Picture Original/Cartes/Gauche2.png")
    Droite_f = pygame.image.load("Jeux/Mini Picture Original/Cartes/Droite1.png")
    Droite_fp = pygame.image.load("Jeux/Mini Picture Original/Cartes/Droite2.png")


    Puissance4_logo = pygame.image.load("Images/Puissance4logo.png").convert_alpha()
    Puissance4_logo_Maxime = pygame.image.load("Images/Fond_puissance.png").convert_alpha()
    MPOriginal = pygame.image.load("Images/Mini Picture Original.png").convert_alpha()

    # Chargement des widgets
    # Soundtrack
    widget_soundtrack_skin = pygame.image.load("Menu/Widgets/Soundtrack Widget.png")
    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

    widget_soundtrack_miniature = pygame.image.load("Menu/Widgets/Soundtrack Widget Miniature.png")
    pos_widget_soundtrack_miniature = widget_soundtrack_miniature.get_rect(topleft=(1190,50))

    widget_soundtrack_lecture = pygame.image.load("Menu/Widgets/Lecture_widget.png")
    pos_widget_soundtrack_lecture = widget_soundtrack_lecture.get_rect(topleft=(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
    widget_soundtrack_pause = pygame.image.load("Menu/Widgets/Pause_widget.png")
    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
    widget_soundtrack_reculer = pygame.image.load("Menu/Widgets/Reculer_widget.png")
    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
    widget_soundtrack_avancer = pygame.image.load("Menu/Widgets/Avancer_widget.png")
    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))

    widget_soundtrack_lecture1 = pygame.image.load("Menu/Widgets/Lecture1.png")
    widget_soundtrack_pause1 = pygame.image.load("Menu/Widgets/Pause1.png")

    #Jauge
    widget_level_miniature = pygame.image.load("Menu/Widgets/Level Widget Miniature.png")
    pos_widget_level_miniature = widget_level_miniature.get_rect(topleft=(1190,130))

    widget_level_skin = pygame.image.load("Menu/Widgets/Level Widget.png")
    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

    #Barre

    widget_barre = pygame.image.load("Menu/Widgets/Widgets_barre.png")

    widget_signet_open = pygame.image.load("Menu/Widgets/Signet_open.png")
    pos_widget_signet_open = widget_signet_open.get_rect(topleft=(1152,500))

    widget_signet_close = pygame.image.load("Menu/Widgets/Signet_close.png")
    pos_widget_signet_close = widget_signet_close.get_rect(topleft=(1251,500))

    # Chargement des images du jeu "carte" Mini Picture Original

    cartes_logo = pygame.image.load("Jeux/Mini Picture Original/Cartes/carte logo.png").convert_alpha()

    carte_dos = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()

    carte1_s = [0,1]
    carte2_s = [0,2]
    carte3_s = [0,3]
    carte4_s = [0,4]
    carte5_s = [0,5]
    carte6_s = [0,6]
    carte7_s = [0,7]
    carte8_s = [0,8]
    carte9_s = [0,9]

    carte1_s1 = [0,1]
    carte2_s1 = [0,2]
    carte3_s1 = [0,3]
    carte4_s1 = [0,4]
    carte5_s1 = [0,5]
    carte6_s1 = [0,6]
    carte7_s1 = [0,7]
    carte8_s1 = [0,8]
    carte9_s1 = [0,9]

    liste_cartes_statut = [carte1_s,carte2_s,carte3_s,carte4_s,carte5_s,carte6_s,carte7_s,carte8_s,carte9_s]
    liste_cartes_statut1 = [carte1_s1,carte2_s1,carte3_s1,carte4_s1,carte5_s1,carte6_s1,carte7_s1,carte8_s1,carte9_s1]

    sélection_carte1 = 0
    sélection_carte2 = 0

    liste_cartes = ["Jeux/Mini Picture Original/Cartes/AUTO carte.png","Jeux/Mini Picture Original/Cartes/Axiom carte.png", "Jeux/Mini Picture Original/Cartes/Eve carte.png","Jeux/Mini Picture Original/Cartes/Journal carte.png",
    "Jeux/Mini Picture Original/Cartes/MO carte.png","Jeux/Mini Picture Original/Cartes/Poster carte.png","Jeux/Mini Picture Original/Cartes/Space carte.png","Jeux/Mini Picture Original/Cartes/WALL E2 carte.png",
    "Jeux/Mini Picture Original/Cartes/Shelby Forthright carte.png"]

    liste_cartes2 = random.sample(liste_cartes,9)

    img1 = liste_cartes2[0]
    img2 = liste_cartes2[1]
    img3 = liste_cartes2[2]
    img4 = liste_cartes2[3]
    img5 = liste_cartes2[4]
    img6 = liste_cartes2[5]
    img7 = liste_cartes2[6]
    img8 = liste_cartes2[7]
    img9 = liste_cartes2[8]

    liste_pos = [(100,50),(260,50),(420,50),(580,50),(740,50),(900,50),(100,260),(260,260),(420,260),(580,260),(740,260),(900,260),(100,470),(260,470),(420,470),(580,470),(740,470),(900,470)]

    liste_pos2 = random.sample(liste_pos,18)

    pos1 = liste_pos2[0]
    pos2 = liste_pos2[1]
    pos3 = liste_pos2[2]
    pos4 = liste_pos2[3]
    pos5 = liste_pos2[4]
    pos6 = liste_pos2[5]
    pos7 = liste_pos2[6]
    pos8 = liste_pos2[7]
    pos9 = liste_pos2[8]
    pos10 = liste_pos2[9]
    pos11 = liste_pos2[10]
    pos12 = liste_pos2[11]
    pos13 = liste_pos2[12]
    pos14 = liste_pos2[13]
    pos15 = liste_pos2[14]
    pos16 = liste_pos2[15]
    pos17 = liste_pos2[16]
    pos18 = liste_pos2[17]

    """Définition de la position des images précédement chargées"""

    # Initialisation des positions des icônes du menu Bonus
    pos_PUB = PUB.get_rect(topleft=(20, 20))
    pos_Truck = Truck.get_rect(topleft=(240, 20))
    pos_Earth = Earth.get_rect(topleft=(460, 20))
    pos_Deck = Deck.get_rect(topleft=(680, 20))
    pos_Dock = Dock.get_rect(topleft=(900, 20))
    pos_Floor = Floor.get_rect(topleft=(20, 250))
    pos_Captain = Captain.get_rect(topleft=(240, 250))
    pos_Pool = Pool.get_rect(topleft=(460, 250))
    pos_Preview = Preview.get_rect(topleft=(680, 250))
    pos_Axiom = Axiom.get_rect(topleft=(900, 250))
    pos_Trash = Trash.get_rect(topleft=(20, 500))
    pos_Menu = Menu.get_rect(topleft=(1150,20))

    # Initialisation de la postion initialle du sélecteur du menu principal
    pos_Selecteur = Selection_menu.get_rect(topleft=(0,position_selecteur))

    # Initialisation de la positon des boutons du lecteur multimédia
    pos_Pause = Pause.get_rect(topleft=(1136,144))
    pos_Lecture = Lecture.get_rect(topleft=(1136,576))
    pos_Avancer = Avancer.get_rect(topleft=(1136,432))
    pos_Reculer = Reculer.get_rect(topleft=(1136,288))
    pos_Menu1 = Reculer.get_rect(topleft=(1136,0))

    # Inititialisation de la position des tuiles du menu Paramètres
    pos_Version = Version.get_rect(topleft=(20,20))
    pos_Infos = Infos.get_rect(topleft=(0,0))
    pos_Infos1 = Infos1.get_rect(topleft=(0,0))
    pos_Modules = Modules.get_rect(topleft=(0,180))
    pos_Modules1 = Modules1.get_rect(topleft=(0,180))
    pos_Animations = Modules.get_rect(topleft=(0,360))
    pos_Animations1 = Modules1.get_rect(topleft=(0,360))

    # Inititialisation de la position des boutons du menu Paramètres
    pos_ON = ON.get_rect(topleft=(850,207))
    pos_ON1 = ON1.get_rect(topleft=(850,207))
    pos_OFF = OFF.get_rect(topleft=(920,207))
    pos_OFF1 = OFF1.get_rect(topleft=(920,207))

    pos_ON_t = ON.get_rect(topleft=(850,247))
    pos_ON1_t = ON1.get_rect(topleft=(850,247))
    pos_OFF_t = OFF.get_rect(topleft=(920,247))
    pos_OFF1_t = OFF1.get_rect(topleft=(920,247))

    pos_ON_RAM = ON.get_rect(topleft=(850,287))
    pos_ON1_RAM = ON1.get_rect(topleft=(850,287))
    pos_OFF_RAM = OFF.get_rect(topleft=(920,287))
    pos_OFF1_RAM = OFF1.get_rect(topleft=(920,287))

    pos_ON_Jauge_C = ON.get_rect(topleft=(850,367))
    pos_ON1_Jauge_C = ON1.get_rect(topleft=(850,367))
    pos_OFF_Jauge_C = OFF.get_rect(topleft=(920,367))
    pos_OFF1_Jauge_C = OFF1.get_rect(topleft=(920,367))

    # Inititialisation de la position des fonds miniatures (Paramètres -> Personnalisation)
    pos_Fond_paramètres = Fond_paramètres.get_rect(topleft=(0,540))
    pos_Fond_paramètres1 = Fond_paramètres1.get_rect(topleft=(0,540))
    pos_fondmenu_a = fondmenu_a.get_rect(topleft=(250,150))
    pos_fondmenu1_a = fondmenu1_a.get_rect(topleft=(460,150))
    pos_fondmenu3_a = fondmenu3_a.get_rect(topleft=(670,150))
    pos_fondmenu4_a = fondmenu4_a.get_rect(topleft=(880,150))
    pos_fondmenu5_a = fondmenu5_a.get_rect(topleft=(250,273))

    # Inititialisation de la position des témoins couleurs (Paramètres -> Personnalisation)
    pos_Violet = Violet.get_rect(topleft=(540,400))
    pos_Jaune = Jaune.get_rect(topleft=(580,400))
    pos_Rouge = Rouge.get_rect(topleft=(620,400))
    pos_Vert = Vert.get_rect(topleft=(660,400))
    pos_Cyan = Cyan.get_rect(topleft=(700,400))
    pos_Bleu = Bleu.get_rect(topleft=(740,400))
    pos_Violet_r = Violet.get_rect(topleft=(540,450))
    pos_Jaune_r = Jaune.get_rect(topleft=(580,450))
    pos_Rouge_r = Rouge.get_rect(topleft=(620,450))
    pos_Vert_r = Vert.get_rect(topleft=(660,450))
    pos_Cyan_r = Cyan.get_rect(topleft=(700,450))
    pos_Bleu_r = Bleu.get_rect(topleft=(740,450))

    # Inititialisation de la position des boutons du menu relatif au système de mise à jour/nouveautés
    pos_bouton_Python = bouton_Python.get_rect(topleft=(470,490))
    pos_bouton_Abord = bouton_Abord.get_rect(topleft=(590,490))
    pos_bouton_C = bouton_C.get_rect(topleft=(710,490))
    pos_bouton_OK = bouton_OK.get_rect(topleft=(570,490))

    # Initialisation des positions des boutons relatifs au menu jeux

    pos_Gauche_f = Gauche_f.get_rect(topleft=(30,260))
    pos_Droite_f = Droite_f.get_rect(topleft=(1161,260))

    #pos_Puissance4logo = Puissance4_logo.get_rect(topleft=(553,250))

    # Chargement des positions du jeu "carte" Mini Picture Original

    #pos_cartes_logo = cartes_logo.get_rect(topleft=(500,200))

    """Initialisation des textes et de leur position, du menu principal"""

    font = pygame.font.Font(None, 30)
    font_widget = pygame.font.Font(None, 25)

    texte_accueil = font.render("ACCUEIL", 1, (255,255,255))

    texte_vidéos = font.render("VIDEOS", 1, (255,255,255))

    texte_jauge = font.render("JAUGE", 1, (255,255,255))

    texte_soundtrack = font.render("SOUNDTRACK", 1, (255,255,255))

    texte_jeux = font.render("JEUX", 1, (255,255,255))

    texte_paramètres = font.render("PARAMETRES", 1, (255,255,255))

    texte_credits = font.render("CREDITS", 1, (255,255,255))

    texte_quitter = font.render("QUITTER", 1, (255,255,255))

    pygame.display.flip()

    if AdaptoRAM_check:
        if psutil.virtual_memory()[1] < RAM_free:
            animations = False
            transition_check = False

    """Initialisation des animations et des fonctions"""
    if continuer:
        étape_programme = "Animations d'ouverture"
        # Animations Logo au lancement
        if animations:
            pygame.mixer.music.load("Son/Jingle.mp3")
            pygame.mixer.music.play()
            sortie = True
            for i in range(248):
                if sortie:
                    text="Logo/Logo"+str(i)+".png"
                    fond1 = pygame.image.load(text).convert()
                    fenetre.blit(fond1,(0,0))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                                sortie = False
                    time.sleep(0.02)
            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,1280,720))

            # Animations BNL au lancement
            pygame.mixer.music.load("Son/BNL-start.mp3")
            pygame.mixer.music.play()
            for i in range(85):
                text="BNL animation/Buy N' Large logo-"+str(i)+".png"
                fond1 = pygame.image.load(text).convert()
                fenetre.blit(fond1,(199,100))
                pygame.display.flip()
                for event in pygame.event.get():
                    None
                time.sleep(0.03)
        étape_programme ="Initialisation des fonctions"
        def afficher_batons(n,décalage1,décalage2):
            x = 0
            for i in range(n):
                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+décalage1+125,widget_level_coor[1]+décalage2+255-x,150, 15))
                x +=25

        # Transition entre les onglets
        def transition_ouverture(n):
            translation=0
            if transition_check:
                for i in range(n):
                    fenetre.blit(Gauche,(-640+translation,0))
                    fenetre.blit(Droite,(1281-translation,0))
                    pygame.display.flip()
                    translation+=2

        # Animation BNL à la fermeture
        def fermeture(n):
            if animations:
                fenetre.blit(fondmulti,(0,0))
                x=n
                text="BNL animation/Buy N' Large logo-"+str(x)+".png"
                pygame.mixer.music.load("Son/BNL-shutdown.mp3")
                pygame.mixer.music.play()
                for i in range(n+1):
                    text="BNL animation/Buy N' Large logo-"+str(x)+".png"
                    fond1 = pygame.image.load(text).convert()
                    fenetre.blit(fond1,(199,100))
                    pygame.display.flip()
                    x-=1
                    time.sleep(0.03)

        # Animation du sélecteur au démarrage
        def ouverture_titre(n,check,ost):
            if transition_check:
                x=n
                global position_selecteur
                for i in range(n):
                    fenetre.blit(fondmenu,(0,0))
                    if widget_soundtrack :
                        fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0]+x*10,widget_soundtrack_coor[1]))
                        texte = font_widget.render(str(f['title']), 1, (255,255,255))
                        fenetre.blit(texte, (widget_soundtrack_coor[0]+x*10+50, widget_soundtrack_coor[1]+35))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+x*10+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+x*10+69,widget_soundtrack_coor[1]+152))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+x*10+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+x*10+69,widget_soundtrack_coor[1]+152))

                        fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+x*10+122,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+x*10+174,widget_soundtrack_coor[1]+152))
                        fenetre.blit(Curseur, (widget_soundtrack_coor[0]+x*10+9+avance, widget_soundtrack_coor[1]+103))

                    if widget_level:
                        fenetre.blit(widget_level_skin,(widget_level_coor[0]+x*10,widget_level_coor[1]))

                        try :
                            battery = psutil.sensors_battery()
                            level= battery.percent
                            plugged = battery.power_plugged
                            a_string = level/10
                            float_str = float(a_string)
                            test= int(float_str)
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,x*10,0)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,x*10,0)

                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (widget_level_coor[0]+x*10+150, widget_level_coor[1]+285))

                        except :
                            texte = font.render("ERREUR", 1, (255,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+x*10+155,widget_level_coor[1]+155))

                    if i <= 30 :
                        fenetre.blit(widget_signet_close,(1310-2*i,500))
                    else :
                        fenetre.blit(widget_signet_close,(1252,500))

                    if ost == 1:
                        fenetre.blit(Soundtrack,(500,35))
                    fenetre.blit(texte_accueil, (20-x, 30))
                    fenetre.blit(texte_vidéos, (20-x, 113))
                    fenetre.blit(texte_jauge, (20-x, 196))
                    fenetre.blit(texte_soundtrack, (20-x, 279))
                    if check == 3 :
                        fenetre.blit(texte_jeux, (20, 362))
                    else :
                        fenetre.blit(texte_jeux, (20-x, 362))
                    fenetre.blit(texte_paramètres, (20-x, 445))
                    fenetre.blit(texte_credits, (20-x, 528))
                    fenetre.blit(texte_quitter, (20-x, 611))
                    if check == 1:
                        fenetre.blit(Selection_menu,(0,x))
                    elif check ==2:
                        fenetre.blit(Selection_menu,(-x*2,position_selecteur))
                    elif check == 3:
                        fenetre.blit(Selection_menu,(0,position_selecteur))
                    pygame.display.flip()
                    x-=1
            if widget_signet :
                widget_barre_transition(1)

        # Animation du sélecteur et des titres lors des transitions
        def fermeture_titre(n,check,ost):
            if transition_check:
                x=0
                global position_selecteur
                if widget_signet :
                    widget_barre_transition(2)
                for i in range(n):
                    fenetre.blit(fondmenu, (0,0))
                    if widget_soundtrack:
                        fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0]+i*10,widget_soundtrack_coor[1]))

                        texte = font_widget.render(str(f['title']), 1, (255,255,255))
                        fenetre.blit(texte, (widget_soundtrack_coor[0]+i*10+50, widget_soundtrack_coor[1]+35))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+i*10+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+i*10+69,widget_soundtrack_coor[1]+152))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+i*10+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+i*10+69,widget_soundtrack_coor[1]+152))

                        fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+i*10+122,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+i*10+174,widget_soundtrack_coor[1]+152))
                        fenetre.blit(Curseur, (widget_soundtrack_coor[0]+i*10+9+avance, widget_soundtrack_coor[1]+103))

                    if widget_level:
                        fenetre.blit(widget_level_skin,(widget_level_coor[0]+i*10,widget_level_coor[1]))

                        try :
                            battery = psutil.sensors_battery()
                            level= battery.percent
                            plugged = battery.power_plugged
                            a_string = level/10
                            float_str = float(a_string)
                            test= int(float_str)
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,i*10,0)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,i*10,0)

                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (widget_level_coor[0]+i*10+150, widget_level_coor[1]+285))

                        except:
                            texte = font.render("ERREUR", 1, (255,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+i*10+155,widget_level_coor[1]+155))

                    fenetre.blit(widget_signet_close,(1252+2*i,500))

                    if ost == 1:
                        fenetre.blit(Soundtrack,(500,35))
                    fenetre.blit(texte_accueil, (20-x, 30))
                    fenetre.blit(texte_vidéos, (20-x, 113))
                    fenetre.blit(texte_jauge, (20-x, 196))
                    fenetre.blit(texte_soundtrack, (20-x, 279))
                    if check == 3:
                        fenetre.blit(texte_jeux, (20, 362))
                    else:
                        fenetre.blit(texte_jeux, (20-x, 362))
                    fenetre.blit(texte_paramètres, (20-x, 445))
                    fenetre.blit(texte_credits, (20-x, 528))
                    fenetre.blit(texte_quitter, (20-x, 611))
                    if check == 1:
                        fenetre.blit(Selection_menu,(0,x))
                    elif check ==2:
                        fenetre.blit(Selection_menu,(-x*2,position_selecteur))
                    elif check == 3:
                        fenetre.blit(Selection_menu,(0,position_selecteur))

                    pygame.display.flip()
                    x+=1

            if check == 3 :
                jeux_transitions(position_selecteur)

        def jeux_transitions(n):
            if transition_check:
                x = 1
                for i in range(n):
                    fenetre.blit(fondmenu, (0,0))
                    fenetre.blit(texte_jeux, (20, 362 - x))
                    fenetre.blit(Selection_menu,(0,position_selecteur - x))

                    pygame.display.flip()

                    x += 1

                x = 1
                for i in range(455):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(texte_jeux, (20 + x, 34))
                    fenetre.blit(Selection_menu,(0 + x,0))

                    pygame.display.flip()

                    x += 1

                x = 1
                for i in range(242):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(texte_jeux, (475, 34))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(Puissance4_logo, (1280 - x, 250))

                    pygame.display.flip()

                    x += 3

        def jeux_sortie(jeu):
            if transition_check:
                x = 1
                for i in range(300):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(texte_jeux, (475, 34))
                    fenetre.blit(Selection_menu,(455,0))
                    if jeu == "P4":
                        fenetre.blit(Puissance4_logo, (553 + x, 250))
                    elif jeu == "C":
                        fenetre.blit(cartes_logo, (500 + x, 200))
                    elif jeu == "P4_M":
                        fenetre.blit(Puissance4_logo_Maxime, (520 + x, 200))

                    pygame.display.flip()

                    x += 3

                x = 1
                for i in range(455):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(texte_jeux, (475 - x, 34))
                    fenetre.blit(Selection_menu,(455 - x,0))

                    pygame.display.flip()

                    x += 1

                x = 1
                for i in range(position_selecteur):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(texte_jeux, (20, 34 + x))
                    fenetre.blit(Selection_menu,(0,0 + x))

                    pygame.display.flip()

                    x += 1

                x = 1

        # Fermeture de l'intégralité du programme
        def STOP():
            global continuer
            global paramètres
            global menu_continuer
            global soundtrack
            global bonus_continuer
            global animations_continuer
            global fond_écran
            global upgrade_continuer
            global version_continuer
            global veille
            global jeux
            global jeux_menu
            global Puissance4
            global Puissance4_by_Maxime
            continuer = False
            paramètres=False
            menu_continuer=True
            soundtrack=False
            bonus_continuer=False
            animations_continuer=False
            fond_écran=False
            upgrade_continuer=False
            version_continuer=False
            veille = False
            jeux = False
            jeux_menu = False
            Puissance4 = False
            Puissance4_by_Maxime = False
            fermeture(118)
            pygame.quit()
            if widget_soundtrack :
                fichier=open("Widgets_soundtrack_pos.py","w")
                fichier.write("widget_soundtrack_coor = ["+str(widget_soundtrack_coor[0])+","+str(widget_soundtrack_coor[1])+"]"+"\n")
                fichier.write("widget_soundtrack = True")
                fichier.close()
            if not(widget_soundtrack) :
                fichier=open("Widgets_soundtrack_pos.py","w")
                fichier.write("widget_soundtrack_coor = [0,0]"+"\n")
                fichier.write("widget_soundtrack = False")
                fichier.close()

            if widget_level :
                fichier=open("Widgets_level_pos.py","w")
                fichier.write("widget_level_coor = ["+str(widget_level_coor[0])+","+str(widget_level_coor[1])+"]"+"\n")
                fichier.write("widget_level = True")
                fichier.close()
            if not(widget_level) :
                fichier=open("Widgets_level_pos.py","w")
                fichier.write("widget_level_coor = [0,0]"+"\n")
                fichier.write("widget_level = False")
                fichier.close()

        # Animation des tuiles du menu Paramètres
        def Tuiles_ouverture():
            fenetre.blit(Gauche,(0,0))
            fenetre.blit(Droite,(640,0))
            if transition_check:
                y = 1

                for i in range(180):
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Animations,(-180+y,360))
                    fenetre.blit(Infos,(-180+y,0))
                    fenetre.blit(Modules,(-180+y,180))
                    fenetre.blit(Fond_paramètres,(-180+y,540))
                    pygame.display.flip()
                    y+=1

                y = 1

                for i in range(71):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(fond_visibilité, (-956+y,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(touche_vide,(0,360))
                    fenetre.blit(Animations,(0,360))
                    fenetre.blit(Infos,(0,0))
                    fenetre.blit(Modules,(0,180))
                    fenetre.blit(Fond_paramètres,(0,540))
                    pygame.display.flip()
                    y+=16

            else:
                fenetre.blit(Gauche,(0,0))
                fenetre.blit(Droite,(640,0))
                fenetre.blit(fond_visibilité, (180,0))
                fenetre.blit(Animations,(0,360))
                fenetre.blit(Infos,(0,0))
                fenetre.blit(Modules,(0,180))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))
                pygame.display.flip()

        def Tuiles_fermeture():
            fenetre.blit(Gauche,(0,0))
            fenetre.blit(Droite,(640,0))
            if transition_check:
                y = 1

                for i in range(71):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(fond_visibilité, (180-y,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(touche_vide,(0,360))
                    fenetre.blit(Animations,(0,360))
                    fenetre.blit(Infos,(0,0))
                    fenetre.blit(Modules,(0,180))
                    fenetre.blit(Fond_paramètres,(0,540))
                    pygame.display.flip()
                    y+=16

                y = 1

                for i in range(180):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(touche_vide,(0-y,360))
                    fenetre.blit(Animations,(0-y,360))
                    fenetre.blit(Infos,(0-y,0))
                    fenetre.blit(Modules,(0-y,180))
                    fenetre.blit(Fond_paramètres,(0-y,540))
                    pygame.display.flip()
                    y+=1

        # Animation des tuiles du lecteur multimédia
        def Tuiles_soundtrack_ouverture():
            color2 = (255,0,0)
            fenetre.blit(Gauche,(0,0))
            fenetre.blit(Droite,(640,0))
            fenetre.blit(Soundtrack,(500,35))
            if transition_check:
                y = 1
                x=500
                while x != 315:
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    x-=1
                    fenetre.blit(Soundtrack,(x,35))
                    pygame.display.flip()

                for i in range(144):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, color2, pygame.Rect(350,794-y,580, 2))
                    fenetre.blit(Curseur, (325+avance, 780-y))

                    fenetre.blit(Pause,(1280-y,144))
                    fenetre.blit(Lecture,(1280-y,576))
                    fenetre.blit(Avancer,(1280-y,432))
                    fenetre.blit(Reculer,(1280-y,288))
                    fenetre.blit(Menu1,(1280-y,0))
                    pygame.display.flip()
                    y+=1

                y = 1

                for i in range(71):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(fond_visibilité, (-1136+y,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, color2, pygame.Rect(350,650,580, 2))
                    fenetre.blit(Curseur, (325, 636))

                    fenetre.blit(Pause,(1136,144))
                    fenetre.blit(Lecture,(1136,576))
                    fenetre.blit(Avancer,(1136,432))
                    fenetre.blit(Reculer,(1136,288))
                    fenetre.blit(Menu1,(1136,0))
                    pygame.display.flip()
                    y+=16

            else:
                fenetre.blit(Soundtrack,(315,35))
                fenetre.blit(Lecture,(1136,576))
                fenetre.blit(Avancer,(1136,432))
                fenetre.blit(Reculer,(1136,288))
                fenetre.blit(Menu1,(1136,0))
                pygame.display.flip()

        def Tuiles_soundtrack_fermeture():
            fenetre.blit(Gauche,(0,0))
            fenetre.blit(Droite,(640,0))
            fenetre.blit(Soundtrack,(315,35))
            if transition_check:
                y = 1
                x=315

                for i in range(71):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(fond_visibilité, (0-y,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, color2, pygame.Rect(350,650,580, 2))
                    fenetre.blit(Curseur, (325+avance, 636))

                    fenetre.blit(Pause,(1136,144))
                    fenetre.blit(Lecture,(1136,576))
                    fenetre.blit(Avancer,(1136,432))
                    fenetre.blit(Reculer,(1136,288))
                    fenetre.blit(Menu11,(1136,0))
                    pygame.display.flip()
                    y+=16

                y = 1

                for i in range(144):
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, color2, pygame.Rect(350,650+y,580, 2))
                    fenetre.blit(Curseur, (325+avance, 636+y))

                    fenetre.blit(Pause,(1136+y,144))
                    fenetre.blit(Lecture,(1136+y,576))
                    fenetre.blit(Avancer,(1136+y,432))
                    fenetre.blit(Reculer,(1136+y,288))
                    fenetre.blit(Menu11,(1136+y,0))
                    pygame.display.flip()
                    y+=1

                while x != 500:
                    fenetre.blit(Gauche,(0,0))
                    fenetre.blit(Droite,(640,0))
                    x+=1
                    fenetre.blit(Soundtrack,(x,35))
                    pygame.display.flip()

            else:

                fenetre.blit(Soundtrack,(350,35))
                fenetre.blit(Gauche,(0,0))
                fenetre.blit(Droite,(640,0))
                pygame.display.flip()

        transition_ouverture(320)

        if Old:
            Menu_skin1 = True
            menu_continuer = False
        else :
            ouverture_titre(200,1,0)
            Menu_skin1 = False

        def sélecteur(commande):
            global position_selecteur

            if commande == "UP" and position_selecteur != 0:
                for i in range(41):
                    position_selecteur -= 2
                    fenetre.blit(fondmenu, (0,0))

                    if widget_soundtrack:
                        fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                        texte = font_widget.render(str(f['title']), 1, (255,255,255))
                        fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                        fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    if widget_level:
                        fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                        try :
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,0,0)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,0,0)

                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                        except:
                            texte = font.render("ERREUR", 1, (255,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                    if widget_signet :
                        fenetre.blit(widget_barre,(1180,0))
                        fenetre.blit(widget_signet_open,(1152,500))
                        if not(widget_soundtrack) :
                            fenetre.blit(widget_soundtrack_miniature,(1190,50))
                        if not(widget_level):
                            fenetre.blit(widget_level_miniature,(1190,130))
                    else :
                        fenetre.blit(widget_signet_close,(1252,500))

                    fenetre.blit(texte_accueil, (20, 30))

                    fenetre.blit(texte_vidéos, (20, 113))

                    fenetre.blit(texte_jauge, (20, 196))

                    fenetre.blit(texte_soundtrack, (20, 279))

                    fenetre.blit(texte_jeux, (20, 362))

                    fenetre.blit(texte_paramètres, (20, 445))

                    fenetre.blit(texte_credits, (20, 528))

                    fenetre.blit(texte_quitter, (20, 611))

                    fenetre.blit(Selection_menu,(0,position_selecteur))
                    pygame.display.flip()
                    time.sleep(0.001)

            if commande == "DOWN" and position_selecteur <= 492  :
                for i in range(41):
                    position_selecteur += 2
                    fenetre.blit(fondmenu, (0,0))

                    if widget_soundtrack:
                        fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                        texte = font_widget.render(str(f['title']), 1, (255,255,255))
                        fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                            fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                        fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    if widget_level:
                        fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                        try :
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,0,0)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,0,0)

                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                        except:
                            texte = font.render("ERREUR", 1, (255,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                    if widget_signet :
                        fenetre.blit(widget_barre,(1180,0))
                        fenetre.blit(widget_signet_open,(1152,500))
                        if not(widget_soundtrack) :
                            fenetre.blit(widget_soundtrack_miniature,(1190,50))
                        if not(widget_level):
                            fenetre.blit(widget_level_miniature,(1190,130))
                    else :
                        fenetre.blit(widget_signet_close,(1252,500))

                    fenetre.blit(texte_accueil, (20, 30))

                    fenetre.blit(texte_vidéos, (20, 113))

                    fenetre.blit(texte_jauge, (20, 196))

                    fenetre.blit(texte_soundtrack, (20, 279))

                    fenetre.blit(texte_jeux, (20, 362))

                    fenetre.blit(texte_paramètres, (20, 445))

                    fenetre.blit(texte_credits, (20, 528))

                    fenetre.blit(texte_quitter, (20, 611))

                    fenetre.blit(Selection_menu,(0,position_selecteur))
                    pygame.display.flip()
                    time.sleep(0.001)

    def reset_cartes():
        global carte1_s
        global carte2_s
        global carte3_s
        global carte4_s
        global carte5_s
        global carte6_s
        global carte7_s
        global carte8_s
        global carte9_s

        global carte1_s1
        global carte2_s1
        global carte3_s1
        global carte4_s1
        global carte5_s1
        global carte6_s1
        global carte7_s1
        global carte8_s1
        global carte9_s1

        global sélection_carte1
        global sélection_carte2

        global liste_cartes
        global liste_cartes2

        global img1
        global img2
        global img3
        global img4
        global img5
        global img6
        global img7
        global img8
        global img9

        global liste_pos

        global pos1
        global pos2
        global pos3
        global pos4
        global pos5
        global pos6
        global pos7
        global pos8
        global pos9
        global pos10
        global pos11
        global pos12
        global pos13
        global pos14
        global pos15
        global pos16
        global pos17
        global pos18

        sélection_carte1 = 0
        sélection_carte2 = 0

        carte1_s = [0,1]
        carte2_s = [0,2]
        carte3_s = [0,3]
        carte4_s = [0,4]
        carte5_s = [0,5]
        carte6_s = [0,6]
        carte7_s = [0,7]
        carte8_s = [0,8]
        carte9_s = [0,9]

        carte1_s1 = [0,1]
        carte2_s1 = [0,2]
        carte3_s1 = [0,3]
        carte4_s1 = [0,4]
        carte5_s1 = [0,5]
        carte6_s1 = [0,6]
        carte7_s1 = [0,7]
        carte8_s1 = [0,8]
        carte9_s1 = [0,9]

        liste_cartes = ["Jeux/Mini Picture Original/Cartes/AUTO carte.png","Jeux/Mini Picture Original/Cartes/Axiom carte.png", "Jeux/Mini Picture Original/Cartes/Eve carte.png","Jeux/Mini Picture Original/Cartes/Journal carte.png",
        "Jeux/Mini Picture Original/Cartes/MO carte.png","Jeux/Mini Picture Original/Cartes/Poster carte.png","Jeux/Mini Picture Original/Cartes/Space carte.png","Jeux/Mini Picture Original/Cartes/WALL E2 carte.png",
        "Jeux/Mini Picture Original/Cartes/Shelby Forthright carte.png"]
        liste_cartes2 = random.sample(liste_cartes,9)

        img1 = liste_cartes2[0]
        img2 = liste_cartes2[1]
        img3 = liste_cartes2[2]
        img4 = liste_cartes2[3]
        img5 = liste_cartes2[4]
        img6 = liste_cartes2[5]
        img7 = liste_cartes2[6]
        img8 = liste_cartes2[7]
        img9 = liste_cartes2[8]

        liste_pos = [(100,50),(260,50),(420,50),(580,50),(740,50),(900,50),(100,260),(260,260),(420,260),(580,260),(740,260),(900,260),(100,470),(260,470),(420,470),(580,470),(740,470),(900,470)]
        liste_pos2 = random.sample(liste_pos,18)

        pos1 = liste_pos2[0]
        pos2 = liste_pos2[1]
        pos3 = liste_pos2[2]
        pos4 = liste_pos2[3]
        pos5 = liste_pos2[4]
        pos6 = liste_pos2[5]
        pos7 = liste_pos2[6]
        pos8 = liste_pos2[7]
        pos9 = liste_pos2[8]
        pos10 = liste_pos2[9]
        pos11 = liste_pos2[10]
        pos12 = liste_pos2[11]
        pos13 = liste_pos2[12]
        pos14 = liste_pos2[13]
        pos15 = liste_pos2[14]
        pos16 = liste_pos2[15]
        pos17 = liste_pos2[16]
        pos18 = liste_pos2[17]

    def pop_up():
        m = 1
        for i in range(100):
            pygame.draw.rect(fenetre, color, pygame.Rect(640-m,360-m,1+m*2, 1+m*2))
            pygame.display.flip()
            m += 2
            time.sleep(0.001)
            pygame.draw.rect(fenetre, color, pygame.Rect(638-m,358-m,4+m*2, 4+m*2))
            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(640-m,360-m,1+m*2, 1+m*2))

    def widget_barre_transition(statut):
        if statut == 1 :
            for i in range(50):
                fenetre.blit(fondmenu, (0,0))

                if widget_soundtrack :
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(str(f['title']), 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                    try :
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERREUR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1280-2*i,0))
                fenetre.blit(widget_signet_open,(1252-2*i,500))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1290-2*i,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1290-2*i,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

        if statut == 2 :
            for i in range(50):
                fenetre.blit(fondmenu, (0,0))
                if widget_soundtrack :
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(str(f['title']), 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                    try :
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERREUR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180+2*i,0))
                fenetre.blit(widget_signet_close,(1152+2*i,500))

                if not(widget_soundtrack) :
                    fenetre.blit(widget_soundtrack_miniature,(1190+2*i,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190+2*i,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

    def widget_animation(widget,statut):
        global widget_soundtrack_coor
        global pos_widget_soundtrack_skin
        global widget_level_coor
        global pos_widget_level_skin
        global décalage_widget
        if widget == "soundtrack" and statut == 1:
            for i in range(45):
                fenetre.blit(fondmenu, (0,0))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERREUR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                fenetre.blit(widget_soundtrack_miniature,(1190+2*i,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            for i in range(70):
                fenetre.blit(fondmenu, (0,0))

                fenetre.blit(widget_soundtrack_skin,(1280-2*i,32))
                texte = font_widget.render(str(f['title']), 1, (255,255,255))
                fenetre.blit(texte, (1280-2*i+50, 32+35))

                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_lecture1,(1280-2*i+16,32+152))
                    fenetre.blit(widget_soundtrack_pause,(1280-2*i+69,32+152))
                elif not(pygame.mixer.music.get_busy()):
                    fenetre.blit(widget_soundtrack_lecture,(1280-2*i+16,32+152))
                    fenetre.blit(widget_soundtrack_pause1,(1280-2*i+69,32+152))

                fenetre.blit(widget_soundtrack_reculer,(1280-2*i+122,32+152))
                fenetre.blit(widget_soundtrack_avancer,(1280-2*i+174,32+152))
                fenetre.blit(Curseur, (1280-2*i+9+avance, 32+103))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))
                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERREUR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            widget_soundtrack_coor = [1140,32]
            pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
            décalage_widget = [0,0]

        if widget == "soundtrack" and statut == 2:
            for i in range(300):
                fenetre.blit(fondmenu, (0,0))

                fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0]+2*i,widget_soundtrack_coor[1]))

                texte = font_widget.render(str(f['title']), 1, (255,255,255))
                fenetre.blit(texte, (widget_soundtrack_coor[0]+2*i+50, widget_soundtrack_coor[1]+35))

                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+2*i+16,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+2*i+69,widget_soundtrack_coor[1]+152))
                elif not(pygame.mixer.music.get_busy()):
                    fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+2*i+16,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+2*i+69,widget_soundtrack_coor[1]+152))

                fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+2*i+122,widget_soundtrack_coor[1]+152))
                fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+2*i+174,widget_soundtrack_coor[1]+152))
                fenetre.blit(Curseur, (widget_soundtrack_coor[0]+2*i+9+avance, widget_soundtrack_coor[1]+103))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))
                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERREUR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            for i in range(50):
                fenetre.blit(fondmenu, (0,0))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))
                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERREUR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))
                fenetre.blit(widget_soundtrack_miniature,(1290-2*i,50))

                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            widget_soundtrack_coor = [0,0]
            pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
            décalage_widget = [0,0]

        if widget == "level" and statut == 1:
            for i in range(45):
                fenetre.blit(fondmenu, (0,0))

                if widget_soundtrack:
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(str(f['title']), 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                fenetre.blit(widget_level_miniature,(1190+2*i,130))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            for i in range(70):
                fenetre.blit(fondmenu, (0,0))

                fenetre.blit(widget_level_skin,(1280-2*i,32))

                try :
                    battery = psutil.sensors_battery()
                    level= battery.percent
                    plugged = battery.power_plugged
                    a_string = level/10
                    float_str = float(a_string)
                    test= int(float_str)
                    if level>=10 and level<100:
                        n=test
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                        afficher_batons(n,(widget_level_coor[0])*(-1)+1280-2*i,(widget_level_coor[1])*(-1)+32)
                    elif level==100:
                        n=9
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                        afficher_batons(n,(widget_level_coor[0])*(-1)+1280-2*i,(widget_level_coor[1])*(-1)+32)

                    elif plugged and level<10:
                        n=0
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                    elif level<10 and not(plugged):
                        pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                        texte = font.render("WARNING", 1, (0,0,0))
                        fenetre.blit(texte, (1280-2*i+150, 32+285))

                except Exception as e:
                    texte = font.render("ERREUR", 1, (255,0,0))
                    fenetre.blit(texte, (1280-2*i+155,widget_level_coor[1]+155))

                if widget_soundtrack:
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(str(f['title']), 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            widget_level_coor = [1140,32]
            pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))
            décalage_widget = [0,0]

        if widget == "level" and statut == 2:
            for i in range(300):
                fenetre.blit(fondmenu, (0,0))

                fenetre.blit(widget_level_skin,(widget_level_coor[0]+2*i,widget_level_coor[1]))

                try :
                    battery = psutil.sensors_battery()
                    level= battery.percent
                    plugged = battery.power_plugged
                    a_string = level/10
                    float_str = float(a_string)
                    test= int(float_str)
                    if level>=10 and level<100:
                        n=test
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,2*i,0)
                    elif level==100:
                        n=9
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,2*i,0)

                    elif plugged and level<10:
                        n=0
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                    elif level<10 and not(plugged):
                        pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                        texte = font.render("WARNING", 1, (0,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+2*i+150, widget_level_coor[1]+285))

                except Exception as e:
                    texte = font.render("ERREUR", 1, (255,0,0))
                    fenetre.blit(texte, (widget_level_coor[0]+2*i+155,widget_level_coor[1]+155))

                if widget_soundtrack:
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    texte = font_widget.render(str(f['title']), 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))
                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            for i in range(50):
                fenetre.blit(fondmenu, (0,0))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))
                fenetre.blit(widget_level_miniature,(1290-2*i,130))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))
                else :
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(str(f['title']), 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 30))

                fenetre.blit(texte_vidéos, (20, 113))

                fenetre.blit(texte_jauge, (20, 196))

                fenetre.blit(texte_soundtrack, (20, 279))

                fenetre.blit(texte_jeux, (20, 362))

                fenetre.blit(texte_paramètres, (20, 445))

                fenetre.blit(texte_credits, (20, 528))

                fenetre.blit(texte_quitter, (20, 611))

                if position_selecteur == 82:
                    fenetre.blit(Bonus,(500,20))
                if position_selecteur == 164:
                    fenetre.blit(Solar,(500,20))
                if position_selecteur == 246:
                    fenetre.blit(Soundtrack,(500,35))
                if position_selecteur == 410:
                    fenetre.blit(BNLmenu,(500,20))

                pygame.display.flip()

            widget_level_coor = [0,0]
            pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))
            décalage_widget = [0,0]

    """Programme"""
    for event in pygame.event.get():
        None
    étape_programme = "Entrée dans la boucle principale"
    while continuer:
        p=1
        lecture=True
        widget_soundtrack_play = False
        titre=""
        temps=0
        avance=0
        while menu_continuer:
            étape_programme = "Menu principal"
            if First_start == 1:
                étape_programme = "First_start"
                pop_up()
                x = 1
            while First_start == 1 :

                pygame.draw.rect(fenetre, color, pygame.Rect(638-200,358-200,4+200*2, 4+200*2))
                pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(640-200,360-200,1+200*2, 1+200*2))

                if x <= 273 :
                    text="News/Widgets"+str(x)+".png"
                    News = pygame.image.load(text).convert()
                    fenetre.blit(News,(440,250))
                    x+=1
                else :
                    x = 1

                texte = font.render("Nouveautés "+str(Version_Menu), 5, (255,255,255))
                fenetre.blit(texte, (550, 190))
                texte = font.render("", 1, (255,255,255))
                fenetre.blit(texte, (450, 250))
                texte = font.render("               Ajout des WIDGETS", 1, (255,255,255))
                fenetre.blit(texte, (450, 280))
                texte = font.render("           --> Lecteur multimédia", 1, (255,255,255))
                fenetre.blit(texte, (450, 310))
                texte = font.render("           --> Jauge", 1, (255,255,255))
                fenetre.blit(texte, (450, 340))
                texte = font.render("           --> Plus de contenu à venir !", 1, (255,255,255))
                fenetre.blit(texte, (450, 370))
                texte = font.render("", 1, (255,255,255))
                fenetre.blit(texte, (450, 400))
                texte = font.render("", 1, (255,255,255))
                fenetre.blit(texte, (450, 430))
                texte = font.render("", 1, (255,255,255))
                fenetre.blit(texte, (450, 460))

                fenetre.blit(bouton_OK, (570,490))
                time.sleep(0.02)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pos_bouton_OK.collidepoint(event.pos):
                            fichier=open("First_start.py","w")
                            fichier.write("First_start = 0")
                            fichier.close()
                            First_start = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            fichier=open("First_start.py","w")
                            fichier.write("First_start = 0")
                            fichier.close()
                            First_start = 0
                    if event.type == QUIT:
                        STOP()

            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            fenetre.blit(fondmenu, (0,0))

            if widget_soundtrack:
                fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                texte = font_widget.render(str(f['title']), 1, (255,255,255))
                fenetre.blit(texte, (widget_soundtrack_coor[0]+50, widget_soundtrack_coor[1]+35))
                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_lecture1,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))
                elif not(pygame.mixer.music.get_busy()):
                    fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_pause1,(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))
                fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

            if widget_level:
                fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                try :
                    battery = psutil.sensors_battery()
                    level= battery.percent
                    plugged = battery.power_plugged
                    a_string = level/10
                    float_str = float(a_string)
                    test= int(float_str)
                    if level>=10 and level<100:
                        n=test
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,0,0)
                    elif level==100:
                        n=9
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,0,0)

                    elif plugged and level<10:
                        n=0
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                    elif level<10 and not(plugged):
                        pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        texte = font.render("WARNING", 1, (0,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                except:
                    texte = font.render("ERREUR", 1, (255,0,0))
                    fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

            if widget_signet :
                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))
                if not(widget_soundtrack) :
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))
            else :
                fenetre.blit(widget_signet_close,(1252,500))

            fenetre.blit(Selection_menu,(0,position_selecteur))

            fenetre.blit(texte_accueil, (20, 30))

            fenetre.blit(texte_vidéos, (20, 113))

            fenetre.blit(texte_jauge, (20, 196))

            fenetre.blit(texte_soundtrack, (20, 279))

            fenetre.blit(texte_jeux, (20, 362))

            fenetre.blit(texte_paramètres, (20, 445))

            fenetre.blit(texte_credits, (20, 528))

            fenetre.blit(texte_quitter, (20, 611))

            if position_selecteur == 82:
                fenetre.blit(Bonus,(500,20))
            if position_selecteur == 164:
                fenetre.blit(Solar,(500,20))
            if position_selecteur == 246:
                fenetre.blit(Soundtrack,(500,35))
            if position_selecteur == 410:
                fenetre.blit(BNLmenu,(500,20))

            pygame.display.flip()
            r=0
            a,b= pygame.mouse.get_pos ( )

            if widget_soundtrack and widget_soundtrack_play :

                a_string=pygame.mixer.music.get_pos()/1000
                float_str = float(a_string)
                test= int(float_str)
                avance=temps*test
                pygame.display.flip()

                if not(pygame.mixer.music.get_busy()) and widget_soundtrack_play and p<39:
                    f = music_tag.load_file("WALL-E [Original Score]/"+str(p)+".mp3")
                    pygame.mixer.music.load("WALL-E [Original Score]/"+str(p)+".mp3")
                    pygame.mixer.music.play()

                    p+=1
                    temps = 217/int(float(str(f [ '#length' ])))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9,widget_soundtrack_coor[1]+118))
                    pygame.display.flip()

                if not(pygame.mixer.music.get_busy()):
                    None

                elif not(pygame.mixer.music.get_busy()) and p == 39:
                    p=1
                    pygame.mixer.music.pause()
                    widget_soundtrack_play = False

            for event in pygame.event.get():
                c=0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        sélecteur("DOWN")

                    if event.key == pygame.K_UP:
                        sélecteur("UP")

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                        if position_selecteur == 0:
                            menu_continuer = False
                            veille = True
                            fermeture_titre(200,2,0)

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                        if position_selecteur == 82:
                            menu_continuer=False
                            bonus_continuer=True
                            fermeture_titre(200,2,0)

                            for i in range(88):
                                text="Bonus/Bonus"+str(c)+".png"
                                fond1 = pygame.image.load(text).convert()
                                fenetre.blit(fond1,(0,0))
                                pygame.display.flip()
                                c+=1
                                time.sleep(0.02)

                        if position_selecteur == 164:
                            fermeture_titre(200,2,0)
                            pygame.quit()
                            if Jauge_choix:
                                os.startfile("Jauge\\Level C.exe")
                            else:
                                os.startfile("Level.bat")
                            STOP()

                        if position_selecteur == 246:
                            menu_continuer=False
                            soundtrack=True
                            fermeture_titre(200,2,1)
                            Tuiles_soundtrack_ouverture()

                        if position_selecteur == 328:
                            indice = 0
                            menu_continuer = False
                            jeux = True
                            jeux_menu = True
                            fermeture_titre(200,3,0)

                        if position_selecteur == 410:
                            paramètres=True
                            menu_continuer=False
                            fermeture_titre(200,2,0)
                            Tuiles_ouverture()

                        if position_selecteur == 492:
                            credits = True
                            menu_continuer=False
                            fermeture_titre(200,2,0)

                            for i in range(248):
                                text="Logo/Logo"+str(i)+".png"
                                fond1 = pygame.image.load(text).convert()
                                fenetre.blit(fond1,(0,0))
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    None

                            log = 0
                            for i in range(49):
                                log += 8
                                text="Logo/Logo248.png"
                                fond1 = pygame.image.load(text).convert()
                                fenetre.blit(fond1,(log,0))
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    None

                        if position_selecteur == 574:
                            STOP()

                if event.type == QUIT:
                    STOP()

                a,b= pygame.mouse.get_pos ( )

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos_widget_soundtrack_skin.collidepoint(event.pos) and not(pos_widget_soundtrack_lecture.collidepoint(event.pos) or pos_widget_soundtrack_pause.collidepoint(event.pos) or pos_widget_soundtrack_avancer.collidepoint(event.pos) or pos_widget_soundtrack_reculer.collidepoint(event.pos)) and not(déplacement_widget_level):
                        if déplacement_widget_soundtrack:
                            déplacement_widget_soundtrack = False
                        else :
                            déplacement_widget_soundtrack = True
                            décalage_widget = [a-widget_soundtrack_coor[0],b-widget_soundtrack_coor[1]]

                    if pos_widget_level_skin.collidepoint(event.pos) and not(déplacement_widget_soundtrack):
                        if déplacement_widget_level:
                            déplacement_widget_level = False
                        else :
                            déplacement_widget_level = True
                            décalage_widget = [a-widget_level_coor[0],b-widget_level_coor[1]]

                    if pos_widget_signet_open.collidepoint(event.pos) and widget_signet:
                        widget_signet = False
                        widget_barre_transition(2)
                    if pos_widget_signet_close.collidepoint(event.pos) and not(widget_signet):
                        widget_signet = True
                        widget_barre_transition(1)
                    if pos_widget_soundtrack_miniature.collidepoint(event.pos) and not(widget_soundtrack) :
                        widget_soundtrack = True
                        widget_animation("soundtrack",1)

                    if pos_widget_level_miniature.collidepoint(event.pos) and not(widget_level) :
                        widget_level = True
                        widget_animation("level",1)

                    if pos_widget_soundtrack_pause.collidepoint(event.pos) and widget_soundtrack:
                        pygame.mixer.music.pause()
                        widget_soundtrack_play=False
                    if pos_widget_soundtrack_lecture.collidepoint(event.pos) and widget_soundtrack and p > 1:
                        pygame.mixer.music.unpause()
                        widget_soundtrack_play=True
                    if pos_widget_soundtrack_lecture.collidepoint(event.pos) and widget_soundtrack and p == 1:
                        widget_soundtrack_play=True
                    if pos_widget_soundtrack_avancer.collidepoint(event.pos) and p<39:
                        pygame.mixer.music.pause()
                        widget_soundtrack_play=True
                    if pos_widget_soundtrack_reculer.collidepoint(event.pos) and p>2:
                        pygame.mixer.music.pause()
                        p-=2

                    if b >= 0 and b <= 82 and a <= 371:
                        if position_selecteur >= 82 :
                            while position_selecteur != 0 :
                                sélecteur("UP")
                        menu_continuer = False
                        veille = True
                        fermeture_titre(200,2,0)


                    if b > 82 and b <= 164 and a <= 371:
                        if position_selecteur > 82 :
                            while position_selecteur != 82 :
                                sélecteur("UP")
                        if position_selecteur < 82 :
                            while position_selecteur != 82 :
                                sélecteur("DOWN")

                        menu_continuer=False
                        bonus_continuer=True
                        fermeture_titre(200,2,0)

                        for i in range(44):
                            text="Bonus/Bonus"+str(c)+".png"
                            fond1 = pygame.image.load(text).convert()
                            fenetre.blit(fond1,(0,0))
                            pygame.display.flip()
                            c+=2
                            time.sleep(0.02)

                    if b > 164 and b <= 246 and a <= 371:
                        if position_selecteur > 164 :
                            while position_selecteur != 164 :
                                sélecteur("UP")
                        if position_selecteur < 164 :
                            while position_selecteur != 164 :
                                sélecteur("DOWN")
                        fermeture_titre(200,2,0)
                        pygame.quit()
                        if Jauge_choix:
                            os.startfile("Jauge\\Level C.exe")
                        else:
                            os.startfile("Level.bat")
                        STOP()

                    if b > 164 and b <= 328 and a <= 371:
                        if position_selecteur > 246 :
                            while position_selecteur != 246 :
                                sélecteur("UP")
                        if position_selecteur < 246 :
                            while position_selecteur != 246 :
                                sélecteur("DOWN")
                        soundtrack=True
                        menu_continuer=False
                        if p != 1:
                            p-=1
                        fermeture_titre(200,2,1)
                        Tuiles_soundtrack_ouverture()

                    if b > 328 and b <= 410 and a <= 371:
                        if position_selecteur > 328 :
                            while position_selecteur != 328 :
                                sélecteur("UP")
                        if position_selecteur < 328 :
                            while position_selecteur != 328 :
                                sélecteur("DOWN")
                        indice = 0
                        menu_continuer = False
                        jeux = True
                        jeux_menu = True
                        fermeture_titre(200,3,0)

                    if b > 410 and b <= 492 and a <= 371:
                        if position_selecteur > 410 :
                            while position_selecteur != 410 :
                                sélecteur("UP")
                        if position_selecteur < 410 :
                            while position_selecteur != 410 :
                                sélecteur("DOWN")

                        paramètres=True
                        menu_continuer=False
                        fermeture_titre(200,2,0)
                        Tuiles_ouverture()

                    if b > 492 and b <= 574 and a <= 371:
                        if position_selecteur > 492 :
                            while position_selecteur != 492 :
                                sélecteur("UP")
                        if position_selecteur < 492 :
                            while position_selecteur != 492 :
                                sélecteur("DOWN")
                        credits = True
                        menu_continuer=False
                        fermeture_titre(200,2,0)

                        for i in range(248):
                            text="Logo/Logo"+str(i)+".png"
                            fond1 = pygame.image.load(text).convert()
                            fenetre.blit(fond1,(0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                None

                        log = 0
                        for i in range(49):
                            log += 8
                            text="Logo/Logo248.png"
                            fond1 = pygame.image.load(text).convert()
                            fenetre.blit(fond1,(log,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                None

                    if b > 574 and b <= 656 and a <= 371:
                        if position_selecteur > 574 :
                            while position_selecteur != 574 :
                                sélecteur("UP")
                        if position_selecteur < 574 :
                            while position_selecteur != 574 :
                                sélecteur("DOWN")

                        STOP()

            a,b= pygame.mouse.get_pos ( )

            while b >= 0 and b <= 82 and a <= 371 and position_selecteur != 0:

                if position_selecteur > 0 :
                    while position_selecteur != 0 :
                        sélecteur("UP")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 82 and b <= 164 and a <= 371 and position_selecteur != 82:

                if position_selecteur > 82 :
                    while position_selecteur != 82 :
                        sélecteur("UP")
                if position_selecteur < 82 :
                    while position_selecteur != 82 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 164 and b <= 246 and a <= 371 and position_selecteur != 164:

                if position_selecteur > 164 :
                    while position_selecteur != 164 :
                        sélecteur("UP")
                if position_selecteur < 164 :
                    while position_selecteur != 164 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 246 and b <= 328 and a <= 371 and position_selecteur != 246:

                if position_selecteur > 246 :
                    while position_selecteur != 246 :
                        sélecteur("UP")
                if position_selecteur < 246 :
                    while position_selecteur != 246 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 328 and b <= 410 and a <= 371 and position_selecteur != 328:

                if position_selecteur > 328 :
                    while position_selecteur != 328 :
                        sélecteur("UP")
                if position_selecteur < 328 :
                    while position_selecteur != 328 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 410 and b <= 492 and a <= 371 and position_selecteur != 410:

                if position_selecteur > 410 :
                    while position_selecteur != 410 :
                        sélecteur("UP")
                if position_selecteur < 410 :
                    while position_selecteur != 410 :
                        sélecteur("DOWN")
                a,b= pygame.mouse.get_pos ( )

            while b > 492 and b <= 574 and a <= 371 and position_selecteur != 492:

                if position_selecteur > 492 :
                        while position_selecteur != 492 :
                            sélecteur("UP")
                if position_selecteur < 492 :
                    while position_selecteur != 492 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 574 and b <= 656 and a <= 371 and position_selecteur != 574:

                if position_selecteur > 574 :
                    while position_selecteur != 574 :
                        sélecteur("UP")
                if position_selecteur < 574 :
                    while position_selecteur != 574 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            if widget_soundtrack_coor[0]+décalage_widget[0] > 1180 and not(déplacement_widget_soundtrack) and widget_signet:
                widget_soundtrack = False
                widget_animation("soundtrack",2)

            if widget_level_coor[0]+décalage_widget[0] > 1180 and not(déplacement_widget_level) and widget_signet:
                widget_level = False
                widget_animation("level",2)

            a,b= pygame.mouse.get_pos ( )

            if déplacement_widget_soundtrack:
                n_coord = [a-décalage_widget[0],b-décalage_widget[1]]

                if n_coord[0] > 380 and (n_coord[1] > 10 and n_coord[1] < 490):
                    n_coord = [a-décalage_widget[0],b-décalage_widget[1]]
                    widget_soundtrack_coor = n_coord
                    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    pos_widget_soundtrack_lecture = widget_soundtrack_lecture.get_rect(topleft=(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                elif n_coord[0] < 380 and (n_coord[1] > 10 and n_coord[1] < 490):
                    n_coord = [widget_soundtrack_coor[0],b-décalage_widget[1]]
                    widget_soundtrack_coor = n_coord
                    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    pos_widget_soundtrack_lecture = widget_soundtrack_lecture.get_rect(topleft=(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))
                elif n_coord[0] > 380 and (n_coord[1] < 10 or n_coord[1] > 490):
                    n_coord = [a-décalage_widget[0],widget_soundtrack_coor[1]]
                    widget_soundtrack_coor = n_coord
                    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    pos_widget_soundtrack_lecture = widget_soundtrack_lecture.get_rect(topleft=(widget_soundtrack_coor[0]+16,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+69,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+122,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+174,widget_soundtrack_coor[1]+152))

            if déplacement_widget_level:
                n_coord = [a-décalage_widget[0],b-décalage_widget[1]]

                if n_coord[0] > 380 and (n_coord[1] > 10 and n_coord[1] < 372):
                    n_coord = [a-décalage_widget[0],b-décalage_widget[1]]
                    widget_level_coor = n_coord
                    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

                elif n_coord[0] < 380 and (n_coord[1] > 10 and n_coord[1] < 372):
                    n_coord = [widget_level_coor[0],b-décalage_widget[1]]
                    widget_level_coor = n_coord
                    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

                elif n_coord[0] > 380 and (n_coord[1] < 10 or n_coord[1] > 372):
                    n_coord = [a-décalage_widget[0],widget_level_coor[1]]
                    widget_level_coor = n_coord
                    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

        if widget_soundtrack_play :
            pygame.mixer.music.stop()

        while Menu_skin1 :
            étape_programme = "Menu principal (legacy)"
            BNLmenu_old = pygame.image.load("Images/Old/BNLmenu.png").convert()
            DVD_old = pygame.image.load("Images/Old/DVD.png").convert_alpha()
            Soundtrack_old = pygame.image.load("Images/Old/Soundtrack.png").convert()
            Solar_old = pygame.image.load("Solar/DVD0.png").convert()
            Bonus_old = pygame.image.load("Images/Old/Bonus.png").convert()
            Autre_old = pygame.image.load("Images/Old/Autre.png").convert()

            """Définition de la position des images précédement chargées"""

            pos_Solar_old = Solar_old.get_rect(topleft=(50,450))
            pos_BNLmenu_old = BNLmenu_old.get_rect(topleft=(970,20))
            pos_Soundtrack_old = Soundtrack_old.get_rect(topleft=(500,450))
            pos_Bonus_old = Bonus_old.get_rect(topleft=(50,20))
            pos_Autre_old = Autre_old.get_rect(topleft=(400,20))
            pos_DVD_old = DVD_old.get_rect(topleft=(1000,450))

            fenetre.blit(fondmenu,(0,0))
            fenetre.blit(DVD_old,(1000,450))
            fenetre.blit(BNLmenu_old,(970,20))
            fenetre.blit(Soundtrack_old,(500,450))
            fenetre.blit(Solar_old,(50,450))
            fenetre.blit(Bonus_old,(50,20))
            fenetre.blit(Autre_old,(400,20))
            font = pygame.font.Font(None, 30)
            texte = font.render("BONUS", 1, (255,255,255))
            fenetre.blit(texte, (110, 330))
            font = pygame.font.Font(None, 30)
            texte = font.render("SOUNDTRACK", 1, (255,255,255))
            fenetre.blit(texte, (527, 420))
            font = pygame.font.Font(None, 30)
            texte = font.render("PARAMETRES", 1, (255,255,255))
            fenetre.blit(texte, (1000, 145))
            pygame.display.flip()
            r=0
            a,b= pygame.mouse.get_pos ( )

            while pos_Solar_old.collidepoint(a,b) and r<=93:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Solar_old.collidepoint(event.pos):
                            if Jauge_choix:
                                os.startfile("Jauge\\Level C.exe")
                            else:
                                os.startfile("Level.bat")
                    pass
                text="Solar/DVD"+str(r)+".png"
                SolarG = pygame.image.load(text).convert()
                fenetre.blit(SolarG,(50,450))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            for event in pygame.event.get():
                c=0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if pos_Soundtrack_old.collidepoint(event.pos):
                        soundtrack=True
                        Menu_skin1=False

                    if pos_Bonus_old.collidepoint(event.pos):
                        Menu_skin1=False
                        bonus_continuer=True

                        for i in range(88):
                            text="Bonus/Bonus"+str(c)+".png"
                            fond1 = pygame.image.load(text).convert()
                            fenetre.blit(fond1,(0,0))
                            pygame.display.flip()
                            c+=1
                            time.sleep(0.02)

                    elif pos_BNLmenu_old.collidepoint(event.pos):
                        paramètres=True
                        Menu_skin1=False

                if event.type == QUIT:
                    STOP()

        while bonus_continuer:
            étape_programme = "Bonus"
            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            fenetre.blit(PUB,(20,20))
            fenetre.blit(Truck,(240,20))
            fenetre.blit(Earth,(460,20))
            fenetre.blit(Deck,(680,20))
            fenetre.blit(Dock,(900,20))
            fenetre.blit(Floor,(20,250))
            fenetre.blit(Captain,(240,250))
            fenetre.blit(Pool,(460,250))
            fenetre.blit(Preview,(680,250))
            fenetre.blit(Axiom,(900,250))
            fenetre.blit(Trash,(20,500))
            fenetre.blit(Menu,(1150,20))

            pygame.display.flip()
            r=0
            a,b= pygame.mouse.get_pos ( )

            while pos_PUB.collidepoint(a,b) and r<=208:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_PUB.collidepoint(event.pos):
                            os.startfile("Videos\\PUB.mp4")
                    pass
                text="GIF Miniatures/PUB/PUB"+str(r)+".png"
                PUBG = pygame.image.load(text).convert()
                fenetre.blit(PUBG,(20,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Trash.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Trash.collidepoint(event.pos):
                            os.startfile("Videos\\Trash.mp4")
                    pass
                text="GIF Miniatures/Trash/PUB"+str(r)+".png"
                TrashG = pygame.image.load(text).convert()
                fenetre.blit(TrashG,(20,500))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Floor.collidepoint(a,b) and r<=91:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Floor.collidepoint(event.pos):
                            os.startfile("Videos\\Floor.mp4")
                    pass
                text="GIF Miniatures/Floor/PUB"+str(r)+".png"
                FloorG = pygame.image.load(text).convert()
                fenetre.blit(FloorG,(20,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Deck.collidepoint(a,b) and r<=97:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Deck.collidepoint(event.pos):
                            os.startfile("Videos\\Deck.mp4")
                    pass
                text="GIF Miniatures/Deck/PUB"+str(r)+".png"
                DeckG = pygame.image.load(text).convert()
                fenetre.blit(DeckG,(680,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Dock.collidepoint(a,b) and r<=98:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Dock.collidepoint(event.pos):
                            os.startfile("Videos\\Dock.mp4")
                    pass
                text="GIF Miniatures/Dock/PUB"+str(r)+".png"
                DockG = pygame.image.load(text).convert()
                fenetre.blit(DockG,(900,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Preview.collidepoint(a,b) and r<=115:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Preview.collidepoint(event.pos):
                            os.startfile("Videos\\Preview.mp4")
                    pass
                text="GIF Miniatures/Preview/PUB"+str(r)+".png"
                PreviewG = pygame.image.load(text).convert()
                fenetre.blit(PreviewG,(680,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Axiom.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Axiom.collidepoint(event.pos):
                            os.startfile("Videos\\Axiom.mp4")
                    pass
                text="GIF Miniatures/Axiom/PUB"+str(r)+".png"
                AxiomG = pygame.image.load(text).convert()
                fenetre.blit(AxiomG,(900,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Earth.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Earth.collidepoint(event.pos):
                            os.startfile("Videos\\Earth.mp4")
                    pass
                text="GIF Miniatures/Earth/PUB"+str(r)+".png"
                EarthG = pygame.image.load(text).convert()
                fenetre.blit(EarthG,(460,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Truck.collidepoint(a,b) and r<=138:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Truck.collidepoint(event.pos):
                            os.startfile("Videos\\Truck.mp4")
                    pass
                text="GIF Miniatures/Truck/PUB"+str(r)+".png"
                TruckG = pygame.image.load(text).convert()
                fenetre.blit(TruckG,(240,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Pool.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Pool.collidepoint(event.pos):
                            os.startfile("Videos\\Pool.mp4")
                    pass
                text="GIF Miniatures/Pool/PUB"+str(r)+".png"
                PoolG = pygame.image.load(text).convert()
                fenetre.blit(PoolG,(460,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Captain.collidepoint(a,b) and r<=79:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Captain.collidepoint(event.pos):
                            os.startfile("Videos\\Captain.mp4")
                    pass
                text="GIF Miniatures/Captain/PUB"+str(r)+".png"
                CaptainG = pygame.image.load(text).convert()
                fenetre.blit(CaptainG,(240,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pos_Menu.collidepoint(event.pos):
                    if Old:
                        bonus_continuer = False
                        Menu_skin1 = True
                        menu_continuer = False
                        transition_ouverture(320)
                    else :
                        menu_continuer=True
                        bonus_continuer=False
                        transition_ouverture(320)
                        ouverture_titre(200,2,0)

            for event in pygame.event.get():
                if event.type == QUIT:
                    STOP()

        while soundtrack:
            étape_programme = "Soundtrack"
            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            a_string=pygame.mixer.music.get_pos()/1000
            float_str = float(a_string)
            test= int(float_str)
            color2 = (255,0,0)
            fenetre.blit(Soundtrack,(315,35))
            pygame.draw.rect(fenetre, color2, pygame.Rect(350,650,580, 2))
            fenetre.blit(Curseur, (325+avance, 636))
            avance=temps*test
            pygame.display.flip()

            if not(pygame.mixer.music.get_busy()) and lecture and p<39:
                f = music_tag.load_file("WALL-E [Original Score]/"+str(p)+".mp3")
                pygame.mixer.music.load("WALL-E [Original Score]/"+str(p)+".mp3")
                pygame.mixer.music.play()

                p+=1
                temps  =  580/int(float(str(f [ '#length' ])))
                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(Soundtrack,(315,35))
                font = pygame.font.Font(None, 20)

                g = 15
                fenetre.blit(fond_visibilité, (0,0))
                for i in range(38):
                    texte = font.render(liste[i], 1, (255,255,255))
                    fenetre.blit(texte, (10, g))
                    g += 18
                if p == 2 :
                    fenetre.blit(Selection_soundtrack, (0,13))
                else:
                    fenetre.blit(Selection_soundtrack, (0,13+18*(p-2)))

                pygame.draw.rect(fenetre, color2, pygame.Rect(350,650,580, 2))
                fenetre.blit(Curseur, (325, 636))
                pygame.display.flip()

            if not(pygame.mixer.music.get_busy()):
                fenetre.blit(Pause1,(1136,144))
                pygame.display.flip()

            elif not(pygame.mixer.music.get_busy()) and p == 39:
                fenetre.blit(Pause1,(1136,144))
                p=1
                pygame.mixer.music.pause()
                lecture=False
            else:
                fenetre.blit(Pause,(1136,144))
            fenetre.blit(Lecture,(1136,576))
            fenetre.blit(Avancer,(1136,432))
            fenetre.blit(Reculer,(1136,288))
            fenetre.blit(Menu1,(1136,0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_Pause.collidepoint(event.pos):
                    pygame.mixer.music.pause()
                    lecture=False
                    fenetre.blit(Pause1,(1136,144))

                if pos_Lecture.collidepoint(event.pos):
                    pygame.mixer.music.unpause()
                    lecture=True
                    fenetre.blit(Lecture1,(1136,576))
                    pygame.display.flip()

                if pos_Avancer.collidepoint(event.pos) and p<39:
                    pygame.mixer.music.pause()
                    lecture=True
                    fenetre.blit(Avancer1,(1136,432))
                    pygame.display.flip()
                    time.sleep(0.5)


                if pos_Reculer.collidepoint(event.pos) and p>2:
                    pygame.mixer.music.pause()
                    fenetre.blit(Reculer1,(1136,288))
                    pygame.display.flip()
                    time.sleep(0.5)
                    p-=2

                if pos_Menu1.collidepoint(event.pos):
                    soundtrack=False
                    if Old :
                        Menu_skin1 = True
                        menu_continuer = False
                        pygame.mixer.music.stop()
                        Tuiles_soundtrack_fermeture()
                        transition_ouverture(320)
                    else :
                        menu_continuer=True
                        fenetre.blit(Menu11,(1136,0))
                        pygame.mixer.music.stop()
                        Tuiles_soundtrack_fermeture()
                        ouverture_titre(200,2,1)
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_DOWN and p<39:
                    pygame.mixer.music.pause()
                    lecture=True
                    fenetre.blit(Avancer1,(1136,432))
                    pygame.display.flip()
                    time.sleep(0.5)

                if event.key == pygame.K_UP and p>2:
                    pygame.mixer.music.pause()
                    fenetre.blit(Reculer1,(1136,288))
                    pygame.display.flip()
                    time.sleep(0.5)
                    p-=2

            for event in pygame.event.get():
                if event.type == QUIT:
                    STOP()

        while paramètres:
            étape_programme = "Paramètres"

            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            fenetre.blit(fondmenu, (0,0))
            fenetre.blit(Animations,(0,360))
            fenetre.blit(Infos,(0,0))
            fenetre.blit(Modules,(0,180))
            fenetre.blit(Fond_paramètres,(0,540))
            fenetre.blit(fond_visibilité, (180,0))
            fenetre.blit(Menu,(1150,20))
            pygame.display.flip()

            Console_s = 0
            Console_t = ""

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos_Infos.collidepoint(event.pos):
                        fenetre.blit(Infos1,(0,0))
                        soundtrack=False
                        menu_continuer=False
                        bonus_continuer=False
                        paramètres=True
                        animations_continuer=False
                        fond_écran=False
                        upgrade_continuer=False
                        version_continuer=True
                        pygame.display.flip()

                    if pos_Animations.collidepoint(event.pos):
                        fenetre.blit(Animations1,(0,360))
                        soundtrack=False
                        menu_continuer=False
                        bonus_continuer=False
                        fond_écran=False
                        animations_continuer=True
                        paramètres=True
                        upgrade_continuer=False
                        version_continuer=False
                        pygame.display.flip()

                    if pos_Modules.collidepoint(event.pos):
                        fenetre.blit(Modules1,(0,180))
                        soundtrack=False
                        menu_continuer=False
                        bonus_continuer=False
                        paramètres=True
                        upgrade_continuer=True
                        fond_écran=False
                        animations_continuer=False
                        version_continuer=False
                        pygame.display.flip()

                    if pos_Menu.collidepoint(event.pos):
                        paramètres=False
                        animations_continuer=False
                        fond_écran=False
                        upgrade_continuer=False
                        version_continuer=False
                        if Old :
                            Menu_skin1 = True
                            menu_continuer = False
                            Tuiles_fermeture()
                            transition_ouverture(320)
                        else :
                            menu_continuer=True
                            fenetre.blit(fondmenu,(0,0))
                            Tuiles_fermeture()
                            ouverture_titre(200,2,0)

                    if pos_Fond_paramètres.collidepoint(event.pos):
                        paramètres=False
                        menu_continuer=True
                        soundtrack=False
                        bonus_continuer=False
                        animations_continuer=False
                        fond_écran=True
                        upgrade_continuer=False
                        version_continuer=False

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_DOWN:
                        fenetre.blit(Infos1,(0,0))
                        soundtrack=False
                        menu_continuer=False
                        bonus_continuer=False
                        paramètres=True
                        animations_continuer=False
                        fond_écran=False
                        upgrade_continuer=False
                        version_continuer=True
                        pygame.display.flip()

                if event.type == QUIT:
                    STOP()

            while version_continuer:

                étape_programme = "Paramètres / Versions et mise à jour de BNL's Box"

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(fond_visibilité, (180,0))
                fenetre.blit(Infos1,(0,0))
                fenetre.blit(Modules,(0,180))
                fenetre.blit(Animations,(0,360))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))

                font = pygame.font.Font(None, 40)
                texte = font.render("Version Jauge (Python) --> "+str(Version_Level), 1, (color1))
                fenetre.blit(texte, (250, 270))
                texte = font.render("Version Jauge (C#) --> "+str(Version_LevelC), 1, (color1))
                fenetre.blit(texte, (250, 300))
                texte = font.render("Version Menu --> "+str(Version_Menu), 1, (color1))
                fenetre.blit(texte, (250, 330))
                texte = font.render("Version Update --> "+str(Version_Update), 1, (color1))
                fenetre.blit(texte, (250, 360))

                pygame.draw.rect(fenetre, color, pygame.Rect(245,500,280, 30))
                font = pygame.font.Font(None, 30)
                texte = font.render("Rechercher les mises à jour", 1, (0,0,0))
                fenetre.blit(texte, (250, 502))
                pos_mise_a_jour = texte.get_rect(topleft=(255,502))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if pos_mise_a_jour.collidepoint(event.pos):
                            try:
                                with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                                    selection_update = True
                                    zipObj.extract("Update_check.py")

                                    from Update_check import*

                                    d = 0
                                    for i in range(100):
                                        pygame.draw.rect(fenetre, color, pygame.Rect(640-d,360-d,1+d*2, 1+d*2))
                                        pygame.display.flip()
                                        d += 2
                                        time.sleep(0.001)

                                    if Update_Menu == Version_Menu and Update_Update == Version_Update and Update_Level == Version_Level and Update_LevelC == Version_LevelC :
                                        while selection_update:
                                            pygame.draw.rect(fenetre, color, pygame.Rect(638-d,358-d,4+d*2, 4+d*2))
                                            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(640-d,360-d,1+d*2, 1+d*2))

                                            texte = font.render("    Aucune mise à jour disponible", 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 355))
                                            texte = font.render("", 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 385))
                                            texte = font.render("    Réparer ?", 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 415))

                                            fenetre.blit(bouton_Python, (470,490))
                                            fenetre.blit(bouton_Abord, (590,490))
                                            fenetre.blit(bouton_C, (710,490))
                                            pygame.display.flip()
                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    if pos_bouton_Python.collidepoint(event.pos):
                                                        fichier=open("Update_check.py","w")
                                                        fichier.write("Cible_f = []"+"\ n")
                                                        fichier.write("Cible_d = []"+"")
                                                        fichier.close()

                                                        continuer=False
                                                        selection_update = False
                                                        STOP()
                                                        pygame.quit()
                                                        os.startfile("Update.bat")
                                                    if pos_bouton_C.collidepoint(event.pos):
                                                        continuer=False
                                                        selection_update = False
                                                        STOP()
                                                        pygame.quit()
                                                        os.startfile("Level Update Utility\\bin\\Debug\\net6.0-windows\\Level test1.exe")
                                                    if pos_bouton_Abord.collidepoint(event.pos):
                                                        selection_update = False
                                                if event.type == QUIT:
                                                    STOP()

                                    else :
                                        while selection_update:
                                            pygame.draw.rect(fenetre, color, pygame.Rect(638-d,358-d,4+d*2, 4+d*2))
                                            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(640-d,360-d,1+d*2, 1+d*2))

                                            texte = font.render("Une mise à jour est disponible", 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 200))

                                            texte = font.render("Menu : " + str(Version_Menu) + "  -->  " + str(Update_Menu), 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 250))
                                            texte = font.render("Jauge (Python) : " + str(Version_Level) + "  -->  " + str(Update_Level), 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 274))
                                            texte = font.render("Jauge (C#) : " + str(Version_LevelC) + "  -->  " + str(Update_LevelC), 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 298))
                                            texte = font.render("Update : " + str(Version_Update) + "  -->  " + str(Update_Update), 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 322))

                                            texte = font.render("Informations : ", 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 360))
                                            texte = font.render(Contenu, 0.1, (255,255,255))
                                            fenetre.blit(texte, (450, 400))

                                            fenetre.blit(bouton_Python, (470,490))
                                            fenetre.blit(bouton_Abord, (590,490))
                                            fenetre.blit(bouton_C, (710,490))
                                            pygame.display.flip()
                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    if pos_bouton_Python.collidepoint(event.pos):
                                                        continuer=False
                                                        selection_update = False
                                                        STOP()
                                                        pygame.quit()
                                                        os.startfile("Update.bat")
                                                    if pos_bouton_C.collidepoint(event.pos):
                                                        continuer=False
                                                        selection_update = False
                                                        STOP()
                                                        pygame.quit()
                                                        os.startfile("Level Update Utility\\bin\\Debug\\net6.0-windows\\Level test1.exe")
                                                    if pos_bouton_Abord.collidepoint(event.pos):
                                                        selection_update = False
                                                if event.type == QUIT:
                                                    STOP()

                            except FileNotFoundError:
                                font = pygame.font.Font(None, 30)
                                texte = font.render("Aucun fichier de mise à niveau trouvé", 1, (color1))
                                fenetre.blit(texte, (800, 502))
                                pygame.display.flip()
                                time.sleep(3)
                        if pos_Menu.collidepoint(event.pos):
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False
                            if Old :
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(320)
                            else :
                                menu_continuer=True
                                fenetre.blit(fondmenu,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)

                        if pos_Infos.collidepoint(event.pos):
                            fenetre.blit(Infos1,(0,0))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            upgrade_continuer=False
                            animations_continuer=False
                            version_continuer=True
                            pygame.display.flip()

                        if pos_Fond_paramètres.collidepoint(event.pos):
                            paramètres=False
                            menu_continuer=True
                            soundtrack=False
                            bonus_continuer=False
                            animations_continuer=False
                            fond_écran=True
                            upgrade_continuer=False
                            version_continuer=False

                        if pos_Modules.collidepoint(event.pos):
                            fenetre.blit(Modules1,(0,180))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=True
                            version_continuer=False
                            pygame.display.flip()

                        if pos_Animations.collidepoint(event.pos):
                            fenetre.blit(Animations1,(0,360))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            animations_continuer=True
                            fond_écran=False
                            paramètres=True
                            upgrade_continuer=False
                            version_continuer=False
                            pygame.display.flip()
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_DOWN:
                            fenetre.blit(Modules1,(0,180))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=True
                            version_continuer=False
                            pygame.display.flip()

                    if event.type == QUIT:
                        STOP()

            while upgrade_continuer:
                étape_programme = "Paramètres / Versions et mise à jour des modules"
                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(fond_visibilité, (180,0))
                fenetre.blit(Infos,(0,0))
                fenetre.blit(Modules1,(0,180))
                fenetre.blit(Animations,(0,360))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))
                font = pygame.font.Font(None, 40)
                texte = font.render("Version Pip --> "+str(pip.__version__), 1, (color1))
                fenetre.blit(texte, (250, 150))
                font = pygame.font.Font(None, 40)
                texte = font.render("Version Psutil --> "+str(psutil.__version__), 1, (color1))
                fenetre.blit(texte, (250, 270))
                font = pygame.font.Font(None, 40)
                texte = font.render("Version Pygame --> "+str(pygame.__version__), 1, (color1))
                fenetre.blit(texte, (250, 330))
                font = pygame.font.Font(None, 40)
                texte = font.render("Version Music_tag --> "+str(music_tag.__version__), 1, (color1))
                fenetre.blit(texte, (250, 207))
                pygame.draw.rect(fenetre, color, pygame.Rect(695,270,90, 30))
                pygame.draw.rect(fenetre, color, pygame.Rect(695,330,90, 30))
                pygame.draw.rect(fenetre, color, pygame.Rect(695,397,120, 30))
                pygame.draw.rect(fenetre, color, pygame.Rect(695,447,120, 30))
                pygame.draw.rect(fenetre, color, pygame.Rect(695,207,90, 30))
                pygame.draw.rect(fenetre, color, pygame.Rect(695,150,90, 30))
                font = pygame.font.Font(None, 30)
                texte1 = font.render("Update", 1, (0,0,0))
                texte = font.render("Update", 1, (0,0,0))
                texte4 = font.render("Update", 1, (0,0,0))
                texte2 = font.render("Update all", 1, (0,0,0))
                texte3 = font.render("Delete all", 1, (0,0,0))
                texte5 = font.render("Update", 1, (0,0,0))
                fenetre.blit(texte1, (700, 273))
                fenetre.blit(texte, (700, 333))
                fenetre.blit(texte2, (700, 400))
                fenetre.blit(texte3, (700, 450))
                fenetre.blit(texte4, (700, 210))
                fenetre.blit(texte5, (700, 153))
                pygame.display.flip()
                pos_Update1 = texte1.get_rect(topleft=(695,273))
                pos_Update = texte.get_rect(topleft=(695,333))
                pos_Update2 = texte.get_rect(topleft=(695,400))
                pos_Delete = texte.get_rect(topleft=(695,450))
                pos_Update3 = texte1.get_rect(topleft=(695,210))
                pos_Update4 = texte2.get_rect(topleft=(695,153))

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if pos_Update1.collidepoint(event.pos):
                            continuer = False
                            pygame.quit()
                            os.startfile("psutil update")
                        if pos_Update.collidepoint(event.pos):
                            continuer = False
                            pygame.quit()
                            os.startfile("pygame update")
                        if pos_Update2.collidepoint(event.pos):
                            continuer = False
                            pygame.quit()
                            os.startfile("All update")
                        if pos_Delete.collidepoint(event.pos):
                            continuer = False
                            pygame.quit()
                            os.startfile("Utilitaire")
                        if pos_Menu.collidepoint(event.pos):
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False
                            if Old :
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(320)
                            else :
                                menu_continuer=True
                                fenetre.blit(fondmenu,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)

                        if pos_Update3.collidepoint(event.pos):
                            continuer = False
                            pygame.quit()
                            os.startfile("music_tag update")
                        if pos_Update4.collidepoint(event.pos):
                            continuer = False
                            pygame.quit()
                            os.startfile("pip update")
                        if pos_Infos.collidepoint(event.pos):
                            fenetre.blit(Infos1,(0,0))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=False
                            version_continuer=True
                            pygame.display.flip()

                        if pos_Animations.collidepoint(event.pos):
                            fenetre.blit(Animations1,(0,360))
                            soundtrack=False
                            menu_continuer=True
                            bonus_continuer=False
                            animations_continuer=True
                            fond_écran=False
                            paramètres=False
                            upgrade_continuer=False
                            version_continuer=False
                            pygame.display.flip()

                        if pos_Fond_paramètres.collidepoint(event.pos):
                            paramètres=False
                            menu_continuer=False
                            soundtrack=False
                            bonus_continuer=False
                            animations_continuer=False
                            fond_écran=True
                            upgrade_continuer=False
                            version_continuer=False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_DOWN:
                            fenetre.blit(Animations1,(0,360))
                            soundtrack=False
                            menu_continuer=True
                            bonus_continuer=False
                            animations_continuer=True
                            fond_écran=False
                            paramètres=False
                            upgrade_continuer=False
                            version_continuer=False
                            pygame.display.flip()
                        if event.key == pygame.K_UP:
                            fenetre.blit(Infos1,(0,0))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=True
                            pygame.display.flip()

                    if event.type == QUIT:
                        STOP()

            while animations_continuer:
                étape_programme = "Paramètres / Outils et console"
                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(fond_visibilité, (180,0))
                fenetre.blit(Infos,(0,0))
                fenetre.blit(Modules,(0,180))
                fenetre.blit(Animations1,(0,360))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))
                if animations:
                    fenetre.blit(ON1,(850,207))
                    fenetre.blit(OFF,(920,207))
                else:
                    fenetre.blit(ON,(850,207))
                    fenetre.blit(OFF1,(920,207))

                if transition_check:
                    fenetre.blit(ON1,(850,247))
                    fenetre.blit(OFF,(920,247))
                else:
                    fenetre.blit(ON,(850,247))
                    fenetre.blit(OFF1,(920,247))

                if AdaptoRAM_check:
                    fenetre.blit(ON1,(850,287))
                    fenetre.blit(OFF,(920,287))
                else:
                    fenetre.blit(ON,(850,287))
                    fenetre.blit(OFF1,(920,287))

                if Jauge_choix:
                    fenetre.blit(ON1,(850,367))
                    fenetre.blit(OFF,(920,367))
                else:
                    fenetre.blit(ON,(850,367))
                    fenetre.blit(OFF1,(920,367))


                font = pygame.font.Font(None, 40)
                texte = font.render("Animations d'ouverture/fermeture", 1, (color1))
                fenetre.blit(texte, (250, 207))
                font = pygame.font.Font(None, 40)
                texte = font.render("Transitions", 1, (color1))
                fenetre.blit(texte, (250, 247))
                texte = font.render("AdaptoRAM", 1, (color1))
                fenetre.blit(texte, (250, 287))
                texte = font.render("RAM restante "+ str(int((psutil.virtual_memory()[1])/1000000))+" Mo", 1, (color1))
                fenetre.blit(texte, (250, 327))
                texte = font.render("Jauge C# (Preview Version)", 1, (color1))
                fenetre.blit(texte, (250, 367))

                if Console_s == 0 :
                    pygame.draw.rect(fenetre, color, pygame.Rect(250,447,510, 30))
                else :
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447,510, 30))

                texte = font.render("Console :", 1, (color1))
                fenetre.blit(texte, (250, 407))
                font = pygame.font.Font(None, 30)
                texte = font.render(Console_t, 1, (0,0,0))
                fenetre.blit(texte, (250, 449))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.pos[0] >= 250 and event.pos[0] <= 760 and event.pos[1] >= 449 and event.pos[1] <= 479 :
                            Console_s = 1
                        else :
                            Console_s = 0

                        if pos_Menu.collidepoint(event.pos):
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False
                            if Old :
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(320)
                            else :
                                menu_continuer=True
                                fenetre.blit(fondmenu,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)

                        if pos_Infos.collidepoint(event.pos):
                            fenetre.blit(Infos1,(0,0))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            upgrade_continuer=False
                            animations_continuer=False
                            version_continuer=True
                            pygame.display.flip()

                        if pos_Modules.collidepoint(event.pos):
                            fenetre.blit(Modules1,(0,180))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=True
                            version_continuer=False
                            pygame.display.flip()

                        if pos_Fond_paramètres.collidepoint(event.pos):
                            paramètres=False
                            menu_continuer=True
                            soundtrack=False
                            bonus_continuer=False
                            animations_continuer=False
                            fond_écran=True
                            upgrade_continuer=False
                            version_continuer=False

                        if pos_ON.collidepoint(event.pos) or pos_ON1.collidepoint(event.pos):
                            fichier=open("Parametres.py","w")
                            fichier.write("animations=True")
                            fichier.close()
                            animations=True

                        if pos_OFF.collidepoint(event.pos) or pos_OFF1.collidepoint(event.pos):
                            fichier=open("Parametres.py","w")
                            fichier.write("animations=False")
                            fichier.close()
                            animations=False

                        if pos_ON_t.collidepoint(event.pos) or pos_ON1_t.collidepoint(event.pos):
                            fichier=open("Transition.py","w")
                            fichier.write("transition_check=True")
                            fichier.close()
                            transition_check=True

                        if pos_OFF_t.collidepoint(event.pos) or pos_OFF1_t.collidepoint(event.pos):
                            fichier=open("Transition.py","w")
                            fichier.write("transition_check=False")
                            fichier.close()
                            transition_check=False

                        if pos_ON_RAM.collidepoint(event.pos) or pos_ON1_RAM.collidepoint(event.pos):
                            fichier=open("AdaptoRAM.py","w")
                            fichier.write("AdaptoRAM_check=True")
                            fichier.close()
                            AdaptoRAM_check=True


                        if pos_OFF_RAM.collidepoint(event.pos) or pos_OFF1_RAM.collidepoint(event.pos):
                            fichier=open("AdaptoRAM.py","w")
                            fichier.write("AdaptoRAM_check=False")
                            fichier.close()
                            AdaptoRAM_check=False
                            animations=True
                            transition_check = True

                        if pos_ON_Jauge_C.collidepoint(event.pos) or pos_ON1_Jauge_C.collidepoint(event.pos):
                            fichier=open("Jauge_choix.py","w")
                            fichier.write("Jauge_choix=True")
                            fichier.close()
                            Jauge_choix = True


                        if pos_OFF_Jauge_C.collidepoint(event.pos) or pos_OFF1_Jauge_C.collidepoint(event.pos):
                            fichier=open("Jauge_choix.py","w")
                            fichier.write("Jauge_choix=False")
                            fichier.close()
                            Jauge_choix = False

                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_DOWN:
                            paramètres=False
                            menu_continuer=True
                            soundtrack=False
                            bonus_continuer=False
                            animations_continuer=False
                            fond_écran=True
                            upgrade_continuer=False
                            version_continuer=False
                        if event.key == pygame.K_UP:
                            fenetre.blit(Modules1,(0,180))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=True
                            version_continuer=False
                            pygame.display.flip()

                        if Console_s == 1:
                            if event.key == pygame.K_SPACE :
                                Console_t += " "
                            elif event.key == pygame.K_BACKSPACE :
                                Console_t = Console_t[:-1]
                            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                                if Console_t == "Old.Skin/activate":
                                    Old = True
                                    fichier=open("Menu_choix.py","w")
                                    fichier.write("Old = True")
                                    fichier.close()
                                elif Console_t == "Old.Skin/desactivate":
                                    Old = False
                                    fichier=open("Menu_choix.py","w")
                                    fichier.write("Old = False")
                                    fichier.close()
                                elif Console_t.upper() == "STOP":
                                    STOP()
                                elif Console_t.upper() == "RESTART":
                                    STOP()
                                    os.startfile("Menu.bat")
                                elif Console_t == "error/":
                                    animations_continuer = False
                                    paramètres = False
                                    continuer = False
                                    erreur_report = True
                                    erreur_détail = "Test lancé via console intégrée..."
                                elif Console_t == "log/read":
                                    os.startfile("log.txt")
                                elif Console_t == "log/erase":
                                    fichier=open("log.txt","w")
                                    fichier.write("")
                                    fichier.close()
                                    Console_t = "Done..."
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447,510, 30))
                                    texte = font.render(Console_t, 1, (0,0,0))
                                    fenetre.blit(texte, (250, 449))
                                    pygame.display.flip()
                                    time.sleep(1)

                                elif Console_t == "Update/":
                                    with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                                        selection_update = True
                                        zipObj.extract("Update_check.py")
                                    STOP()
                                    os.startfile("Update.bat")
                                elif Console_t == "Update/all":
                                    fichier=open("Update_check.py","w")
                                    fichier.write("")
                                    fichier.close()
                                    STOP()
                                    pygame.quit()
                                    os.startfile("Update.bat")
                                elif Console_t == "color/":
                                    color_selection = True

                                    color_input_var_s = 0
                                    color_input_var_t = ""

                                    color_input_a_s = 0
                                    color_input_a_t = ""

                                    color_input_b_s = 0
                                    color_input_b_t = ""

                                    color_input_c_s = 0
                                    color_input_c_t = ""

                                    color_check_var = 0

                                    color_config = [0,0,0]
                                    color_test = (0,0,0)
                                    color_select = 0

                                    animations_continuer = False
                                    paramètres = False
                                    pop_up()
                                else :
                                    Console_t = "Commande non reconnue..."
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447,510, 30))
                                    texte = font.render(Console_t, 1, (0,0,0))
                                    fenetre.blit(texte, (250, 449))
                                    pygame.display.flip()
                                    time.sleep(1)
                                Console_t = ""
                            elif len(Console_t) > 55 :
                                Console_t = ""

                            else :
                                Console_t += event.unicode

                    if event.type == QUIT:
                        STOP()

            while fond_écran:
                étape_programme = "Paramètres / Personnalisation"
                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(fond_visibilité, (180,0))
                fenetre.blit(Infos,(0,0))
                fenetre.blit(Modules,(0,180))
                fenetre.blit(Animations,(0,360))
                fenetre.blit(Fond_paramètres1,(0,540))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(fondmenu_a,(250,150))
                fenetre.blit(fondmenu1_a,(460,150))
                fenetre.blit(fondmenu3_a,(670,150))
                fenetre.blit(fondmenu4_a,(880,150))
                fenetre.blit(fondmenu5_a,(250,273))
                font = pygame.font.Font(None, 40)
                texte = font.render("Image de base :", 1, (color1))
                fenetre.blit(texte, (250, 100))

                font = pygame.font.Font(None, 40)
                texte = font.render("Couleur des textes :", 1, (color1))
                fenetre.blit(texte, (250, 400))
                pygame.draw.rect(fenetre, color, pygame.Rect(250,445,270, 35))
                font = pygame.font.Font(None, 40)
                texte = font.render("Couleur des cases :", 1, (0,0,0))
                fenetre.blit(texte, (250, 450))

                fenetre.blit(Violet,(540,400))
                fenetre.blit(Jaune,(580,400))
                fenetre.blit(Rouge,(620,400))
                fenetre.blit(Vert,(660,400))
                fenetre.blit(Cyan,(700,400))
                fenetre.blit(Bleu,(740,400))
                fenetre.blit(Violet,(540,450))
                fenetre.blit(Jaune,(580,450))
                fenetre.blit(Rouge,(620,450))
                fenetre.blit(Vert,(660,450))
                fenetre.blit(Cyan,(700,450))
                fenetre.blit(Bleu,(740,450))

                if fond_selection==1:
                    Gauche = pygame.image.load("Images/fondmenu/Gauche.png").convert()
                    fondmenu = pygame.image.load("Images/fondmenu/fondmenu.png").convert()
                    Droite = pygame.image.load("Images/fondmenu/Droite.png").convert()
                    fenetre.blit(Selection,(245,150))
                elif fond_selection==2:
                    Gauche = pygame.image.load("Images/fondmenu1/Gauche.png").convert()
                    fondmenu = pygame.image.load("Images/fondmenu1/fondmenu.png").convert()
                    Droite = pygame.image.load("Images/fondmenu1/Droite.png").convert()
                    fenetre.blit(Selection,(455,150))
                elif fond_selection==3:
                    Gauche = pygame.image.load("Images/fondmenu3/Gauche.png").convert()
                    fondmenu = pygame.image.load("Images/fondmenu3/fondmenu.jpg").convert()
                    Droite = pygame.image.load("Images/fondmenu3/Droite.png").convert()
                    fenetre.blit(Selection,(665,150))
                elif fond_selection==4:
                    Gauche = pygame.image.load("Images/fondmenu4/Gauche.png").convert()
                    fondmenu = pygame.image.load("Images/fondmenu4/fondmenu.jpg").convert()
                    Droite = pygame.image.load("Images/fondmenu4/Droite.png").convert()
                    fenetre.blit(Selection,(875,150))
                elif fond_selection==5:
                    Gauche = pygame.image.load("Images/fondmenu5/Gauche.jpg").convert()
                    fondmenu = pygame.image.load("Images/fondmenu5/fondmenu.jpg").convert()
                    Droite = pygame.image.load("Images/fondmenu5/Droite.jpg").convert()
                    fenetre.blit(Selection,(245,273))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pos_Menu.collidepoint(event.pos):
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False
                            if Old :
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(320)
                            else :
                                menu_continuer=True
                                fenetre.blit(fondmenu,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)

                        if pos_Infos.collidepoint(event.pos):
                            fenetre.blit(Infos1,(0,0))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            upgrade_continuer=False
                            animations_continuer=False
                            version_continuer=True
                            pygame.display.flip()

                        if pos_Modules.collidepoint(event.pos):
                            fenetre.blit(Modules1,(0,180))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=True
                            version_continuer=False
                            pygame.display.flip()

                        if pos_Animations.collidepoint(event.pos):
                            fenetre.blit(Animations1,(0,360))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            animations_continuer=True
                            paramètres=True
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False
                            pygame.display.flip()

                        if pos_fondmenu_a.collidepoint(event.pos):
                            fichier=open("Fond.py","w")
                            fichier.write("fond_selection=1")
                            fichier.close()
                            fond_selection=1

                        if pos_fondmenu1_a.collidepoint(event.pos):
                            fichier=open("Fond.py","w")
                            fichier.write("fond_selection=2")
                            fichier.close()
                            fond_selection=2

                        if pos_fondmenu3_a.collidepoint(event.pos):
                            fichier=open("Fond.py","w")
                            fichier.write("fond_selection=3")
                            fichier.close()
                            fond_selection=3

                        if pos_fondmenu4_a.collidepoint(event.pos):
                            fichier=open("Fond.py","w")
                            fichier.write("fond_selection=4")
                            fichier.close()
                            fond_selection=4

                        if pos_fondmenu5_a.collidepoint(event.pos):
                            fichier=open("Fond.py","w")
                            fichier.write("fond_selection=5")
                            fichier.close()
                            fond_selection=5

                        if pos_Violet.collidepoint(event.pos):
                            fichier=open("Couleur.py","w")
                            fichier.write("color1=(255,0,255)")
                            fichier.close()
                            color1=(255,0,255)
                        if pos_Rouge.collidepoint(event.pos):
                            fichier=open("Couleur.py","w")
                            fichier.write("color1=(255,0,0)")
                            fichier.close()
                            color1=(255,0,0)
                        if pos_Cyan.collidepoint(event.pos):
                            fichier=open("Couleur.py","w")
                            fichier.write("color1=(0,255,255)")
                            fichier.close()
                            color1=(0,255,255)
                        if pos_Bleu.collidepoint(event.pos):
                            fichier=open("Couleur.py","w")
                            fichier.write("color1=(0,0,255)")
                            fichier.close()
                            color1=(0,0,255)
                        if pos_Vert.collidepoint(event.pos):
                            fichier=open("Couleur.py","w")
                            fichier.write("color1=(0,255,0)")
                            fichier.close()
                            color1=(0,255,0)
                        if pos_Jaune.collidepoint(event.pos):
                            fichier=open("Couleur.py","w")
                            fichier.write("color1=(255,255,0)")
                            fichier.close()
                            color1=(255,255,0)

                        if pos_Violet_r.collidepoint(event.pos):
                            fichier=open("Couleur_r.py","w")
                            fichier.write("color=(255,0,255)")
                            fichier.close()
                            color=(255,0,255)
                        if pos_Rouge_r.collidepoint(event.pos):
                            fichier=open("Couleur_r.py","w")
                            fichier.write("color=(255,0,0)")
                            fichier.close()
                            color=(255,0,0)
                        if pos_Cyan_r.collidepoint(event.pos):
                            fichier=open("Couleur_r.py","w")
                            fichier.write("color=(0,255,255)")
                            fichier.close()
                            color=(0,255,255)
                        if pos_Bleu_r.collidepoint(event.pos):
                            fichier=open("Couleur_r.py","w")
                            fichier.write("color=(0,0,255)")
                            fichier.close()
                            color=(0,0,255)
                        if pos_Vert_r.collidepoint(event.pos):
                            fichier=open("Couleur_r.py","w")
                            fichier.write("color=(0,255,0)")
                            fichier.close()
                            color=(0,255,0)
                        if pos_Jaune_r.collidepoint(event.pos):
                            fichier=open("Couleur_r.py","w")
                            fichier.write("color=(255,255,0)")
                            fichier.close()
                            color=(255,255,0)
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_UP:
                            fenetre.blit(Animations1,(0,360))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            animations_continuer=True
                            paramètres=True
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False
                            pygame.display.flip()
                    if event.type == QUIT:
                        STOP()

        while credits:
            étape_programme = "Crédits"
            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,1280, 720))
            font = pygame.font.Font(None, 40)
            text="Logo/Logo248.png"
            fond1 = pygame.image.load(text).convert()
            fenetre.blit(fond1,(392,0))
            texte = font.render("MINI Picture, anciennement Nicolas Picture présente :", 10, (255,255,255))
            fenetre.blit(texte, (10, 130))
            font = pygame.font.Font(None, 27)
            texte = font.render("Level, un programme Python fait par un fan de WALL-E, pour des fans de WALL-E", 10, (255,255,255))
            fenetre.blit(texte, (10, 200))
            texte = font.render("Tout droits réservés, ce programme est néanmoins en open-source, pour peu", 10, (255,255,255))
            fenetre.blit(texte, (10, 230))
            texte = font.render("qu'il soit mentionné sur le logiciel : MINI Picture Original", 10, (255,255,255))
            fenetre.blit(texte, (10, 260))
            texte = font.render("Pour tout renseignement ou assistance, m'adresser un mail à l'adresse suivante :", 10, (255,255,255))
            fenetre.blit(texte, (10, 300))
            texte = font.render("nicolachampy@gmail.com", 10, (255,255,255))
            fenetre.blit(texte, (10, 330))
            texte = font.render("Toute copie à usage commercial est formellement interdite...", 10, (255,255,255))
            fenetre.blit(texte, (10, 390))
            texte = font.render("Tout les jeux ne comportant pas le label MINI Picture Original appartiennent", 10, (255,255,255))
            fenetre.blit(texte, (10, 450))
            texte = font.render("à leur propriétaires respectifs et sont soumis aux lois concernant les droits d'auteur.", 10, (255,255,255))
            fenetre.blit(texte, (10, 480))
            texte = font.render("Toute reproduction de ces jeux est interdite sauf autorisations de leur part.", 10, (255,255,255))
            fenetre.blit(texte, (10, 510))
            font = pygame.font.Font(None, 40)
            texte = font.render("Presser la touche ENTER pour revenir au menu principal...", 10, (255,255,255))
            fenetre.blit(texte, (10, 600))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                        menu_continuer = True
                        credits = False
                        transition_ouverture(320)
                        ouverture_titre(200,2,0)

                if event.type == QUIT:
                    STOP()


        while jeux :
            étape_programme = "Jeux"
            jeux_liste = ["P4","C","P4_M"]
            pos_logo_jeu = Puissance4_logo.get_rect(topleft=(553,250))
            while jeux_menu :

                étape_programme = "Jeux / Menu"

                jeu_selection = jeux_liste[indice]

                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(texte_jeux, (475, 34))
                fenetre.blit(Selection_menu,(455,0))

                if jeu_selection == "P4" :
                    fenetre.blit(Puissance4_logo, (553, 250))
                    pos_logo_jeu = Puissance4_logo.get_rect(topleft=(553,250))

                    font = pygame.font.Font(None, 30)
                    texte = font.render("Puissance 4 : la réplique numérique du célèbre jeu à deux. Gracieusement fournit par Raphaël Picture (touts droits réservés),", 1, (color1))
                    fenetre.blit(texte, (10, 450))
                    texte = font.render("il constitue le premier jeu à intégrer la BNL's Box v3.7. Raphaël Picture vous livre ici un jeu simple et intuitif, qui saura ", 1, (color1))
                    fenetre.blit(texte, (10, 480))
                    texte = font.render("distraire petits et grands. Une page d'aide y est également intégrée. ", 1, (color1))
                    fenetre.blit(texte, (10, 510))

                elif jeu_selection == "C" :
                    fenetre.blit(cartes_logo, (500, 200))
                    pos_logo_jeu = cartes_logo.get_rect(topleft=(500,200))
                    fenetre.blit(MPOriginal,(650,200))

                    font = pygame.font.Font(None, 30)
                    texte = font.render("WALL-E's Memory : aidez WALL-E à rassembler les paires ! Second jeu de la BNL's Box, et premier de Mini Picture, ce jeu simple", 1, (color1))
                    fenetre.blit(texte, (10, 450))
                    texte = font.render("divertira petits et grands aussi longtemps qu'ils le souhaiteront. Un algorithme simple, des cartes aléatoirement distribuées,", 1, (color1))
                    fenetre.blit(texte, (10, 480))
                    texte = font.render("il vous suffit de cliquer sur les cartes, BNL's Box s'occupe du reste...", 1, (color1))
                    fenetre.blit(texte, (10, 510))

                elif jeu_selection == "P4_M" :
                    fenetre.blit(Puissance4_logo_Maxime, (520, 200))
                    pos_logo_jeu = Puissance4_logo_Maxime.get_rect(topleft=(520,200))

                    font = pygame.font.Font(None, 30)
                    texte = font.render("Puissance 4 by Maxime : fournit gracieusement par Maxime Picture (touts droits réservés), cette version du célèbre jeu", 1, (color1))
                    fenetre.blit(texte, (10, 450))
                    texte = font.render("offre une revisite numérique classique, mais moderne, et vient compléter celui de Raphaël Picture, plus déjanté.", 1, (color1))
                    fenetre.blit(texte, (10, 480))
                    texte = font.render("A savourer au même titre que ce dernier...", 1, (color1))
                    fenetre.blit(texte, (10, 510))

                fenetre.blit(Menu,(1150,20))

                fenetre.blit(Gauche_f,(30,260))
                fenetre.blit(Droite_f,(1161,260))

                pygame.display.flip()

                for event in pygame.event.get():

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pos_logo_jeu.collidepoint(event.pos) and jeu_selection == "P4":
                           jeux_menu = False
                           Puissance4 = True

                        elif pos_logo_jeu.collidepoint(event.pos) and jeu_selection == "C":
                           jeux_menu = False
                           Cartes = True
                           reset_cartes()
                           compte = 0

                        elif pos_logo_jeu.collidepoint(event.pos) and jeu_selection == "P4_M":
                           jeux_menu = False
                           Puissance4_by_Maxime = True

                        if pos_Droite_f.collidepoint(event.pos):
                            indice += 1
                            if indice < len(jeux_liste):
                                jeu_selection = jeux_liste[indice]
                            else:
                                indice = 0
                                jeu_selection = jeux_liste[indice]
                        if pos_Gauche_f.collidepoint(event.pos):
                            indice -= 1
                            if indice >= 0:
                                jeu_selection = jeux_liste[indice]
                            else:
                                indice = len(jeux_liste)-1
                                jeu_selection = jeux_liste[indice]

                        if pos_Menu.collidepoint(event.pos):
                            jeux_menu = False
                            Puissance4 = False
                            Cartes = False
                            jeux = False
                            menu_continuer = True
                            jeux_sortie(jeu_selection)
                            ouverture_titre(200,3,0)

                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_RIGHT:
                            indice += 1
                            if indice < len(jeux_liste):
                                jeu_selection = jeux_liste[indice]
                            else:
                                indice = 0
                                jeu_selection = jeux_liste[indice]
                        if event.key == pygame.K_LEFT:
                            indice -= 1
                            if indice >= 0:
                                jeu_selection = jeux_liste[indice]
                            else:
                                indice = len(jeux_liste)-1
                                jeu_selection = jeux_liste[indice]
                    if event.type == QUIT:
                        STOP()

            while Puissance4 :

                étape_programme = "Jeux / Puissance 4 by Raphaël Picture"

                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(Menu,(1150,20))

                # Jeux : Puissance 4 avec l'aimable autorisation de Raphaël Bobille ( alias Raphaël Picture )
                # Des modifications ont cependant été effectuées afin de le rendre compatible avec BNL's Box...

                import json
                from random import randint

                def aide():
                    global jeux_menu
                    global Puissance4

                    fenetre.blit(fondmenu, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/help.png").convert(), (0,0))
                    pygame.display.flip()
                    while Puissance4:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                jeux = False
                                jeux_menu = False
                                Puissance4 = False
                                STOP()
                            if event.type == KEYDOWN:
                                return
                            if event.type == MOUSEBUTTONDOWN:

                                if pos_Menu.collidepoint(event.pos):
                                    return
                def menu():
                    global jeux_menu
                    global Puissance4

                    time.sleep(1.5)
                    menu = pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/menu.png").convert()

                    fenetre.blit(fondmenu, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(menu, (230, 200))
                    pygame.display.flip()
                    while Puissance4:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                STOP()
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    if 200 < event.pos[1] < 239:
                                        if 230 < event.pos[0] < 364:
                                            return
                                        if 364 < event.pos[0] < 498:
                                            puissance4()

                                if pos_Menu.collidepoint(event.pos):
                                    return

                            if event.type == KEYDOWN:
                                if event.key == K_KP0:
                                    return
                                if event.key == K_KP1:
                                    puissance4()

                def puissance4():
                    n = 0
                    global jeux_menu
                    global Puissance4

                    fenetre.blit(fondmenu, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/grille.png").convert_alpha(), (0, 0))

                    pygame.display.flip()
                    background = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
                    w = 0
                    plein = 0
                    player = randint(1,2)
                    tyellow = pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/tyellow.png").convert()
                    tred = pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/tred.png").convert()
                    while Puissance4:
                        while Puissance4:
                            if n > 41:
                                fenetre.blit(pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/equality.png").convert(), (245, 100))
                                pygame.display.flip()
                                menu()
                                return
                            if player == 1:
                                fenetre.blit(tyellow, (500, 550))
                                pygame.display.flip()
                            else:
                                fenetre.blit(tred, (500, 550))
                                pygame.display.flip()
                            col = selectcol()

                            if col == 7 :
                                return

                            for k in range(6):
                                if background[col][k] == 0:
                                    background[col][k] = player
                                    grille(k, col, player)
                                    break
                                if k == 5:
                                    plein = 1
                            if plein == 0:
                                break
                            plein = 0
                        n += 1
                        if player == 1:
                            player = 2
                        else:
                            player = 1
                        if n > 6:
                            w = gagnant(background)
                            if w == 1 or w == 2:
                                menu()
                                return

                def selectcol():

                    global Puissance4
                    global jeux_menu

                    while Puissance4:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                STOP()
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    if 10 < event.pos[1] < 525:
                                        if 31 < event.pos[0] < 103:
                                            return 0
                                        if 118 < event.pos[0] < 187:
                                            return 1
                                        if 202 < event.pos[0] < 272:
                                            return 2
                                        if 287 < event.pos[0] < 357:
                                            return 3
                                        if 373 < event.pos[0] < 443:
                                            return 4
                                        if 457 < event.pos[0] < 527:
                                            return 5
                                        if 542 < event.pos[0] < 612:
                                            return 6

                                if pos_Menu.collidepoint(event.pos):
                                    return 7

                            if event.type == KEYDOWN:
                                if event.key == K_KP1:
                                    return 0
                                if event.key == K_KP2:
                                    return 1
                                if event.key == K_KP3:
                                    return 2
                                if event.key == K_KP4:
                                    return 3
                                if event.key == K_KP5:
                                    return 4
                                if event.key == K_KP6:
                                    return 5
                                if event.key == K_KP7:
                                    return 6

                def gagnant(b):
                    if ligne(b)[0] == 1:
                        résultat(ligne(b)[1], ligne(b)[2], ligne(b)[3], ligne(b)[4], ligne(b)[5], ligne(b)[6], ligne(b)[7], ligne(b)[8], ligne(b)[9])
                        return 1
                    if colone(b)[0] == 1:
                        résultat(colone(b)[1], colone(b)[2], colone(b)[3], colone(b)[4], colone(b)[5], colone(b)[6], colone(b)[7], colone(b)[8], colone(b)[9])
                        return 1
                    if diaglltr(b)[0] == 1:
                        résultat(diaglltr(b)[1], diaglltr(b)[2], diaglltr(b)[3], diaglltr(b)[4], diaglltr(b)[5], diaglltr(b)[6], diaglltr(b)[7], diaglltr(b)[8], diaglltr(b)[9])
                        return 1
                    if diagtllr(b)[0] == 1:
                        résultat(diagtllr(b)[1], diagtllr(b)[2], diagtllr(b)[3], diagtllr(b)[4], diagtllr(b)[5], diagtllr(b)[6], diagtllr(b)[7], diagtllr(b)[8], diagtllr(b)[9])
                        return 1
                    if ligne(b)[0] == 2:
                        résultat(ligne(b)[1], ligne(b)[2], ligne(b)[3], ligne(b)[4], ligne(b)[5], ligne(b)[6], ligne(b)[7], ligne(b)[8], ligne(b)[9])
                        return 2
                    if colone(b)[0] == 2:
                        résultat(colone(b)[1], colone(b)[2], colone(b)[3], colone(b)[4], colone(b)[5], colone(b)[6], colone(b)[7], colone(b)[8], colone(b)[9])
                        return 2
                    if diaglltr(b)[0] == 2:
                        résultat(diaglltr(b)[1], diaglltr(b)[2], diaglltr(b)[3], diaglltr(b)[4], diaglltr(b)[5], diaglltr(b)[6], diaglltr(b)[7], diaglltr(b)[8], diaglltr(b)[9])
                        return 2
                    if diagtllr(b)[0] == 2:
                        résultat(diagtllr(b)[1], diagtllr(b)[2], diagtllr(b)[3], diagtllr(b)[4], diagtllr(b)[5], diagtllr(b)[6], diagtllr(b)[7], diagtllr(b)[8], diagtllr(b)[9])
                        return 2
                    return 0

                def ligne(b):
                    for l in range(6):
                        for k in range(4):
                            if b[k][l] == b[k+1][l] == b[k+2][l] == b[k+3][l] == 1:
                                return [1,b,k,l,k+1,l,k+2,l,k+3,l]
                            if b[k][l] == b[k+1][l] == b[k+2][l] == b[k+3][l] == 2:
                                return [2,b,k,l,k+1,l,k+2,l,k+3,l]
                    return [0]

                def colone(b):
                    for k in range(7):
                        for l in range(3):
                            if b[k][l] == b[k][l+1] == b[k][l+2] == b[k][l+3] == 1:
                                return [1,b,k,l,k,l+1,k,l+2,k,l+3]
                            if b[k][l] == b[k][l+1] == b[k][l+2] == b[k][l+3] == 2:
                                return [2,b,k,l,k,l+1,k,l+2,k,l+3]
                    return [0]

                def diaglltr(b):
                    for k in range(4):
                        for l in range(3):
                            if b[k][l] == b[k+1][l+1] == b[k+2][l+2] == b[k+3][l+3] == 1:
                                return [1,b,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
                            if b[k][l] == b[k+1][l+1] == b[k+2][l+2] == b[k+3][l+3] == 2:
                                return [2,b,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
                    return [0]

                def diagtllr(b):
                	for k in range(4):
                		for l in range(3):
                			if b[k][5-l] == b[k+1][4-l] == b[k+2][3-l] == b[k+3][2-l] == 1:
                				return [1,b,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
                			if b[k][5-l] == b[k+1][4-l] == b[k+2][3-l] == b[k+3][2-l] == 2:
                				return [2,b,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
                	return [0]

                def grille(coord1, coord2, color):
                    pioncollin = [coord1, coord2]
                    c = [440 + pioncollin[0]*-85, 28 + pioncollin[1]*85]
                    if color == 1:
                        pionj = pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/pionj.png").convert()
                        fenetre.blit(pionj, (c[1], c[0]))
                    else:
                        pionr = pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/pionr.png").convert()
                        fenetre.blit(pionr, (c[1], c[0]))
                    pygame.display.flip()

                def résultat(b, k1, c1, k2, c2, k3, c3, k4, c4):

                    fenetre.blit(fondmenu, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/grille.png").convert_alpha(), (0, 0))
                    c = b[k1][c1]
                    grille(c1, k1, c)
                    grille(c2, k2, c)
                    grille(c3, k3, c)
                    grille(c4, k4, c)
                    if b[k1][c1] == 1:
                        fenetre.blit(pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/jaune.png").convert(), (80, 525))
                    else:
                        fenetre.blit(pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/rouge.png").convert(), (80, 525))
                    pygame.display.flip()

                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(Menu,(1150,20))

                fenetre.blit(pygame.image.load("Jeux/Raphael Picture/Puissance_4.2/images/start.png").convert(), (0,0))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if 489 > event.pos[1] and 648 > event.pos[0]:
                                puissance4()
                            if 488 < event.pos[1] and 648 > event.pos[0]:
                                aide()
                            if event.type == KEYDOWN:
                                puissance4()

                        if pos_Menu.collidepoint(event.pos):
                            Puissance4 = False
                            jeux_menu = True

                    if event.type == QUIT:
                        STOP()

            while Cartes :
                étape_programme = "Jeux / WALL-E's Memory"
                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(Menu,(1150,20))

                """ Chargement des cartes (dos) """

                liste_cartes_statut = [carte1_s,carte2_s,carte3_s,carte4_s,carte5_s,carte6_s,carte7_s,carte8_s,carte9_s]
                liste_cartes_statut1 = [carte1_s1,carte2_s1,carte3_s1,carte4_s1,carte5_s1,carte6_s1,carte7_s1,carte8_s1,carte9_s1]

                # carte 1
                if carte1_s[0] == 1 or carte1_s[0] == 2 :
                    carte1_i = pygame.image.load(img1).convert_alpha()
                else:
                    carte1_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 2
                if carte2_s[0] == 1 or carte2_s[0] == 2 :
                    carte2_i = pygame.image.load(img2).convert_alpha()
                else:
                    carte2_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 3
                if carte3_s[0] == 1 or carte3_s[0] == 2 :
                    carte3_i = pygame.image.load(img3).convert_alpha()
                else:
                    carte3_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 4
                if carte4_s[0] == 1 or carte4_s[0] == 2 :
                    carte4_i = pygame.image.load(img4).convert_alpha()
                else:
                    carte4_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 5
                if carte5_s[0] == 1 or carte5_s[0] == 2 :
                    carte5_i = pygame.image.load(img5).convert_alpha()
                else:
                    carte5_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 6
                if carte6_s[0] == 1 or carte6_s[0] == 2 :
                    carte6_i = pygame.image.load(img6).convert_alpha()
                else:
                    carte6_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 7
                if carte7_s[0] == 1 or carte7_s[0] == 2 :
                    carte7_i = pygame.image.load(img7).convert_alpha()
                else:
                    carte7_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 8
                if carte8_s[0] == 1 or carte8_s[0] == 2 :
                    carte8_i = pygame.image.load(img8).convert_alpha()
                else:
                    carte8_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 9
                if carte9_s[0] == 1 or carte9_s[0] == 2 :
                    carte9_i = pygame.image.load(img9).convert_alpha()
                else:
                    carte9_i = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()

                # carte 1 bis
                if carte1_s1[0] == 1 or carte1_s1[0] == 2 :
                    carte1_i1 = pygame.image.load(img1).convert_alpha()
                else:
                    carte1_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 2 bis
                if carte2_s1[0] == 1 or carte2_s1[0] == 2 :
                    carte2_i1 = pygame.image.load(img2).convert_alpha()
                else:
                    carte2_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 3 bis
                if carte3_s1[0] == 1 or carte3_s1[0] == 2 :
                    carte3_i1 = pygame.image.load(img3).convert_alpha()
                else:
                    carte3_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 4 bis
                if carte4_s1[0] == 1 or carte4_s1[0] == 2 :
                    carte4_i1 = pygame.image.load(img4).convert_alpha()
                else:
                    carte4_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 5 bis
                if carte5_s1[0] == 1 or carte5_s1[0] == 2 :
                    carte5_i1 = pygame.image.load(img5).convert_alpha()
                else:
                    carte5_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 6 bis
                if carte6_s1[0] == 1 or carte6_s1[0] == 2 :
                    carte6_i1 = pygame.image.load(img6).convert_alpha()
                else:
                    carte6_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 7 bis
                if carte7_s1[0] == 1 or carte7_s1[0] == 2 :
                    carte7_i1 = pygame.image.load(img7).convert_alpha()
                else:
                    carte7_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 8 bis
                if carte8_s1[0] == 1 or carte8_s1[0] == 2 :
                    carte8_i1 = pygame.image.load(img8).convert_alpha()
                else:
                    carte8_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()
                # carte 9 bis
                if carte9_s1[0] == 1 or carte9_s1[0] == 2 :
                    carte9_i1 = pygame.image.load(img9).convert_alpha()
                else:
                    carte9_i1 = pygame.image.load("Jeux/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()

                fenetre.blit(carte1_i,pos1)
                fenetre.blit(carte2_i,pos2)
                fenetre.blit(carte3_i,pos3)
                fenetre.blit(carte4_i,pos4)
                fenetre.blit(carte5_i,pos5)
                fenetre.blit(carte6_i,pos6)

                pos_carte1_i = carte1_i.get_rect(topleft=pos1)
                pos_carte2_i = carte2_i.get_rect(topleft=pos2)
                pos_carte3_i = carte3_i.get_rect(topleft=pos3)
                pos_carte4_i = carte4_i.get_rect(topleft=pos4)
                pos_carte5_i = carte5_i.get_rect(topleft=pos5)
                pos_carte6_i = carte6_i.get_rect(topleft=pos6)

                fenetre.blit(carte7_i,pos7)
                fenetre.blit(carte8_i,pos8)
                fenetre.blit(carte9_i,pos9)
                fenetre.blit(carte1_i1,pos10)
                fenetre.blit(carte2_i1,pos11)
                fenetre.blit(carte3_i1,pos12)

                pos_carte7_i = carte7_i.get_rect(topleft=pos7)
                pos_carte8_i = carte8_i.get_rect(topleft=pos8)
                pos_carte9_i = carte9_i.get_rect(topleft=pos9)
                pos_carte1_i1 = carte1_i1.get_rect(topleft=pos10)
                pos_carte2_i1 = carte2_i1.get_rect(topleft=pos11)
                pos_carte3_i1 = carte3_i1.get_rect(topleft=pos12)

                fenetre.blit(carte4_i1,pos13)
                fenetre.blit(carte5_i1,pos14)
                fenetre.blit(carte6_i1,pos15)
                fenetre.blit(carte7_i1,pos16)
                fenetre.blit(carte8_i1,pos17)
                fenetre.blit(carte9_i1,pos18)

                pos_carte4_i1 = carte4_i1.get_rect(topleft=pos13)
                pos_carte5_i1 = carte5_i1.get_rect(topleft=pos14)
                pos_carte6_i1 = carte6_i1.get_rect(topleft=pos15)
                pos_carte7_i1 = carte7_i1.get_rect(topleft=pos16)
                pos_carte8_i1 = carte8_i1.get_rect(topleft=pos17)
                pos_carte9_i1 = carte9_i1.get_rect(topleft=pos18)

                pygame.display.flip()

                # Système de comparaison
                if sélection_carte1 != 0 and sélection_carte2 != 0 :
                    for i in range(len(liste_cartes_statut)) :
                        if sélection_carte1 == liste_cartes_statut[i][1]:
                            if sélection_carte2 == liste_cartes_statut1[i][1]:
                                liste_cartes_statut[i][0] = 2
                                liste_cartes_statut1[i][0] = 2
                                sélection_carte1 = 0
                                sélection_carte2 = 0
                                compte += 1
                            else :
                                for j in range(len(liste_cartes_statut1)) :
                                    if liste_cartes_statut1[j][0] == 1 :
                                        liste_cartes_statut1[j][0] = 0
                                for j in range(len(liste_cartes_statut)) :
                                    if liste_cartes_statut[j][0] == 1 :
                                        liste_cartes_statut[j][0] = 0

                                sélection_carte1 = 0
                                sélection_carte2 = 0

                    time.sleep(1)

                if compte == 9 :
                    pop_up()
                    font = pygame.font.Font(None, 60)
                    texte = font.render("BRAVO !", 5, (color1))
                    fenetre.blit(texte, (550, 250))
                    pygame.display.flip()
                    reset_cartes()
                    compte = 0
                    time.sleep(2)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pos_carte1_i.collidepoint(event.pos):
                            carte1_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte1_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte1_s[1]

                        if pos_carte2_i.collidepoint(event.pos):
                            carte2_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte2_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte2_s[1]

                        if pos_carte3_i.collidepoint(event.pos):
                            carte3_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte3_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte3_s[1]

                        if pos_carte4_i.collidepoint(event.pos):
                            carte4_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte4_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte4_s[1]

                        if pos_carte5_i.collidepoint(event.pos):
                            carte5_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte5_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte5_s[1]

                        if pos_carte6_i.collidepoint(event.pos):
                            carte6_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte6_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte6_s[1]

                        if pos_carte7_i.collidepoint(event.pos):
                            carte7_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte7_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte7_s[1]

                        if pos_carte8_i.collidepoint(event.pos):
                            carte8_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte8_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte8_s[1]

                        if pos_carte9_i.collidepoint(event.pos):
                            carte9_s[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte9_s[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte9_s[1]


                        if pos_carte1_i1.collidepoint(event.pos):
                            carte1_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte1_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte1_s1[1]

                        if pos_carte2_i1.collidepoint(event.pos):
                            carte2_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte2_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte2_s1[1]

                        if pos_carte3_i1.collidepoint(event.pos):
                            carte3_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte3_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte3_s1[1]

                        if pos_carte4_i1.collidepoint(event.pos):
                            carte4_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte4_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte4_s1[1]

                        if pos_carte5_i1.collidepoint(event.pos):
                            carte5_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte5_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte5_s1[1]

                        if pos_carte6_i1.collidepoint(event.pos):
                            carte6_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte6_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte6_s1[1]

                        if pos_carte7_i1.collidepoint(event.pos):
                            carte7_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte7_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte7_s1[1]

                        if pos_carte8_i1.collidepoint(event.pos):
                            carte8_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte8_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte8_s1[1]

                        if pos_carte9_i1.collidepoint(event.pos):
                            carte9_s1[0] = 1
                            if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                sélection_carte1 = carte9_s1[1]
                            elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                sélection_carte2 = carte9_s1[1]

                        if pos_Menu.collidepoint(event.pos):
                            jeux_menu = True
                            indice = 1
                            compte = 0
                            reset_cartes()
                            Cartes = False

                    if event.type == QUIT:
                        STOP()

            while Puissance4_by_Maxime :
                étape_programme = "Jeux / Puissance 4 by Maxime Picture"
                fenetre.blit(fondmenu, (0,0))
                fenetre.blit(Menu,(1150,20))

                #Début bibliothèque
                import pygame
                import math
                import random
                from pygame.locals import *
                def chargement(nom_chargement):

                    global fenetre
                    fenêtre = fenetre

                    font = pygame.font.Font("Jeux/Maxime Picture/Multi-game/police.ttf", 10)
                    Fond_chargement=pygame.image.load("Jeux/Maxime Picture/Multi-game/Fond_chargement.png").convert_alpha()
                    texte_chargement= font.render("Chargement", 1, (255,255,255))
                    texte_chargement2= font.render(nom_chargement, 1, (255,255,255))
                    fenêtre.blit(Fond_chargement,(490,310))
                    fenêtre.blit(texte_chargement,(490+55,310+5))
                    fenêtre.blit(texte_chargement2,(135+490,5+310))
                    pygame.display.flip()
                    charge_bar=50+490
                    for i in range(200):
                        pygame.draw.rect(fenêtre,(255,255,255),pygame.Rect(charge_bar,30+310,1,40))
                        pygame.display.flip()
                        charge_bar+=1
                        pygame.time.delay(random.randint(0,5))
                #Menu principal
                def Menu_principal():

                    d = 190
                    d1 = 60

                    global fenetre
                    fenêtre = fenetre
                    global Puissance4_by_Maxime
                    global jeux_menu

                    fenetre.blit(fondmenu, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    Menu_principal_actif=True
                    selection=1
                    Validation=False
                    changement=True
                    Bouton_puissance=Rect(((25+d,45+d1),(260,50)))
                    Bouton_quitter=Rect(((25+d,135+d1),(260,50)))
                    chargement(" du menu principal...")
                    pygame.display.flip()
                    Fond_puissance=pygame.image.load("Jeux/Maxime Picture/Multi-game/Fond_puissance.png").convert_alpha()
                    Fond_quitter=pygame.image.load("Jeux/Maxime Picture/Multi-game/Fond_quitter.png").convert_alpha()
                    font = pygame.font.Font("Jeux/Maxime Picture/Multi-game/police.ttf", 30)
                    #actions
                    while Menu_principal_actif==True:
                        for event in pygame.event.get():
                            if event.type==KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Menu_principal_actif = False
                                    jeux_menu = True
                                    Puissance4_by_Maxime = False
                                    Menu_principal_actif = False
                                    return
                                if event.key == K_DOWN:
                                    if selection!=2:
                                        selection+=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_UP:
                                    if selection!=1:
                                        selection-=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_RETURN or event.key == K_SPACE:
                                    Validation=True
                            elif event.type == pygame.MOUSEMOTION:
                                if Bouton_quitter.collidepoint(event.pos):
                                    selection=2
                                    changement=True
                                if Bouton_puissance.collidepoint(event.pos):
                                    selection=1
                                    changement=True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if Bouton_quitter.collidepoint(event.pos):
                                    Validation=True
                                elif Bouton_puissance.collidepoint(event.pos):
                                    Validation=True
                                elif pos_Menu.collidepoint(event.pos):
                                    jeux_menu = True
                                    Puissance4_by_Maxime = False
                                    Menu_principal_actif = False
                                    return
                            elif event.type == QUIT:
                                STOP()
                        if Validation==True and selection==1:
                            Menu_principal_actif = False
                            puissance4()
                        elif Validation==True and selection==2:
                            Menu_principal_actif = False
                            jeux_menu = True
                            Puissance4_by_Maxime = False
                            Menu_principal_actif = False
                            return
                        if changement==True:
                            changement=False
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0+d,0+d1,300,600))
                            pygame.draw.rect(fenêtre,(255,255,255),pygame.Rect(300+d,0+d1,600,600))
                            pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(20+d,-30+d1+70*selection,260,60))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(25+d,-25+d1+70*selection,250,50))
                            texte_menu1=font.render("Puissance 4", 1, (255,255,255))
                            texte_menu2=font.render("Quitter", 1, (255,255,255))
                            fenêtre.blit(texte_menu1,(45+d,55+d1))
                            fenêtre.blit(texte_menu2,(45+d,125+d1))
                            if selection==1:
                                fenêtre.blit(Fond_puissance,(350+d,45+d1))
                            if selection==2:
                                fenêtre.blit(Fond_quitter,(325+d,0+d1))
                            pygame.display.flip()
                def puissance4():

                    global fenetre
                    fenêtre = fenetre
                    global Puissance4_by_Maxime
                    global jeux_menu

                    fenetre.blit(fondmenu, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    dis = 170
                    dis2 = 160
                    dis1 = 10

                    chargement("du puissance 4")
                    Menu_puissance=True
                    selection=1
                    selection2=1
                    Jeu=False
                    fin=False
                    Validation=False
                    changement=True
                    Bouton_puissance_commencer=Rect(((300+dis,400-dis1),(370,80)))
                    Bouton_puissance_quitter=Rect(((360+dis,550-dis1),(260,80)))
                    Boutonj1=Rect(((280+dis,230-dis1),(140,140)))
                    Boutonj2=Rect(((530+dis,230-dis1),(140,140)))
                    font = pygame.font.Font("Jeux/Maxime Picture/Multi-game/police.ttf", 10)
                    font_titre = pygame.font.Font("Jeux/Maxime Picture/Multi-game/police.ttf", 50)
                    font2 = pygame.font.Font("Jeux/Maxime Picture/Multi-game/police.ttf", 30)
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(360,20-dis1,560,700))
                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(365,25-dis1,550,690))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(370,30-dis1,540,680))
                    titre=font_titre.render("Puissance 4", 1, (255,255,255))
                    t1=font2.render("Qui commence ?", 1, (255,255,255))
                    t2=font_titre.render("Commencer", 1, (255,255,255))
                    t3=font_titre.render("Quitter", 1, (255,255,255))
                    t4=font_titre.render("Victoire", 1, (255,255,255))
                    t5=font_titre.render("du Joueur", 1, (255,255,255))
                    v1=font_titre.render("1", 1, (255,255,255))
                    v2=font_titre.render("2", 1, (255,255,255))
                    v3=font_titre.render("Egalité", 1, (255,255,255))
                    fenêtre.blit(titre,(300+dis,50))
                    fenêtre.blit(t1,(350+dis,150-dis1))
                    fenêtre.blit(t2,(320+dis,400-dis1))
                    fenêtre.blit(t3,(380+dis,550-dis1))
                    pygame.display.flip()
                    while Menu_puissance==True:
                        for event in pygame.event.get():
                            #quitter
                            if event.type==KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Menu_puissance = False
                                    Menu_principal()
                                if event.key == K_DOWN:
                                    if selection!=2:
                                        selection+=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_UP:
                                    if selection!=1:
                                        selection-=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_LEFT:
                                    if selection2!=1:
                                        selection2-=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_RIGHT:
                                    if selection2!=2:
                                        selection2+=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_RETURN or event.key == K_SPACE:
                                    Validation=True
                            elif event.type == pygame.MOUSEMOTION:
                                if Bouton_puissance_commencer.collidepoint(event.pos):
                                    selection=1
                                    changement=True
                                if Bouton_puissance_quitter.collidepoint(event.pos):
                                    selection=2
                                    changement=True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if Bouton_puissance_commencer.collidepoint(event.pos):
                                    Validation=True
                                elif Bouton_puissance_quitter.collidepoint(event.pos):
                                    Validation=True
                                elif Boutonj1.collidepoint(event.pos):
                                    changement=True
                                    selection2=1
                                elif Boutonj2.collidepoint(event.pos):
                                    changement=True
                                    selection2=2
                                elif pos_Menu.collidepoint(event.pos):
                                    jeux_menu = True
                                    Puissance4_by_Maxime = False
                                    return
                            elif event.type == QUIT:
                                STOP()
                            if Validation==True and selection==1:
                                Menu_puissance = False
                                Jeu=True
                            if Validation==True and selection==2:
                                Menu_puissance = False
                                Menu_principal()
                            if changement==True:
                                changement=False
                                pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(370,230-dis1,540,400))
                                if selection2==1:
                                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(280+dis,230-dis1,140,140))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(285+dis,235-dis1,130,130))
                                    joueur=1
                                elif selection2==2:
                                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(530+dis,230-dis1,140,140))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(535+dis,235-dis1,130,130))
                                    joueur=2
                                if selection==1:
                                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(300+dis,400-dis1,370,80))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(305+dis,405-dis1,360,70))
                                elif selection==2:
                                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(360+dis,550-dis1,260,80))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(365+dis,555-dis1,250,70))
                                pygame.draw.circle(fenêtre,(255,0,0), (350+dis,300-dis1),50,0)
                                pygame.draw.circle(fenêtre,(255,255,0), (600+dis,300-dis1),50,0)
                                fenêtre.blit(t2,(320+dis,400-dis1))
                                fenêtre.blit(t3,(380+dis,550-dis1))
                                pygame.display.flip()
                    m1,m2=0,0
                    if Jeu==True:
                        changement_puissance=True
                        selection_puissance=38
                        case=3
                        b=5
                        victoire=0
                        c=False
                        d=0
                        emplacements=[5,5,5,5,5,5,5]
                        grille=[[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0]]
                        Colone1=Rect(((60+dis2,0),(120,740)))
                        Colone2=Rect(((180+dis2,0),(120,740)))
                        Colone3=Rect(((300+dis2,0),(120,740)))
                        Colone4=Rect(((420+dis2,0),(120,740)))
                        Colone5=Rect(((540+dis2,0),(120,740)))
                        Colone6=Rect(((660+dis2,0),(120,740)))
                        Colone7=Rect(((780+dis2,0),(120,740)))
                        while Jeu==True:
                            for event in pygame.event.get():
                                if event.type==KEYDOWN:
                                    if event.key == K_ESCAPE:
                                        Jeu=False
                                        puissance4()
                                    if event.key == K_LEFT:
                                        if case!=0:
                                            a=[]
                                            for i in range(case):
                                                if emplacements[case-1-i]!=-1:
                                                    a.append(case-1-i)
                                            if a!=[]:
                                                case=a[0]
                                            changement_puissance=True
                                            pygame.time.delay(50)
                                    if event.key == K_RIGHT:
                                        if case!=6:
                                            a=[]
                                            for i in range(6-case):
                                                if emplacements[case+1+i]!=-1:
                                                    a.append(case+1+i)
                                            if a!=[]:
                                                case=a[0]
                                            changement_puissance=True
                                            pygame.time.delay(50)
                                    if event.key == K_RETURN or event.key == K_SPACE:
                                        if joueur==1:
                                            grille[b][case]=1
                                            joueur=2
                                        else:
                                            grille[b][case]=5
                                            joueur=1
                                        if emplacements[case]>=0:
                                                emplacements[case]-=1
                                        pygame.time.delay(50)
                                        changement_puissance=True
                                elif event.type == pygame.MOUSEMOTION:
                                    if Colone1.collidepoint(event.pos):
                                        case=0
                                        changement_puissance=True
                                    elif Colone2.collidepoint(event.pos):
                                        case=1
                                        changement_puissance=True
                                    elif Colone3.collidepoint(event.pos):
                                        case=2
                                        changement_puissance=True
                                    elif Colone4.collidepoint(event.pos):
                                        case=3
                                        changement_puissance=True
                                    elif Colone5.collidepoint(event.pos):
                                        case=4
                                        changement_puissance=True
                                    elif Colone6.collidepoint(event.pos):
                                        case=5
                                        changement_puissance=True
                                    elif Colone7.collidepoint(event.pos):
                                        case=6
                                        changement_puissance=True
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                        if joueur==1:
                                            grille[b][case]=1
                                            joueur=2
                                        else:
                                            grille[b][case]=5
                                            joueur=1
                                        if emplacements[case]>=0:
                                                emplacements[case]-=1
                                        pygame.time.delay(50)
                                        changement_puissance=True
                                        if pos_Menu.collidepoint(event.pos):
                                            jeux_menu = True
                                            Puissance4_by_Maxime = False
                                            return
                                elif event.type == QUIT:
                                    STOP()
                            if changement_puissance==True:
                                changement_puissance=False
                                pygame.draw.rect(fenêtre,(0,0,255),pygame.Rect(0+dis2,0,960,740))
                                for i in range(7):
                                    for i in range(6):
                                     for j in range(7):
                                            if grille[i][j]==0:
                                                pygame.draw.circle(fenêtre,(255,255,255), (120+j*120+dis2,70+i*120),50,0)
                                            elif grille[i][j]==1:
                                                pygame.draw.circle(fenêtre,(255,0,0), (120+j*120+dis2,70+i*120),50,0)
                                            elif grille[i][j]==5:
                                                pygame.draw.circle(fenêtre,(255,255,0), (120+j*120+dis2,70+i*120),50,0)
                                b=emplacements[case]
                                if b!=-1:
                                    pygame.draw.circle(fenêtre,(0,150,255), (120+case*120+dis2,70+b*120),25,0)
                                else:
                                    c=True
                                    d=0
                                    while c==True:
                                        if emplacements[case]!=-1:
                                            c=False
                                        elif case!=6:
                                            case+=1
                                        else:
                                            case=0
                                        d+=1
                                        if d==10:
                                            c=False
                                    b=emplacements[case]
                                    pygame.draw.circle(fenêtre,(0,150,255), (120+case*120+dis2,70+b*120),25,0)
                                pygame.display.flip()
                                for i in range(6):
                                    for j in range(4):
                                        if grille[i][j]+grille[i][j+1]+grille[i][j+2]+grille[i][j+3]==4:
                                            victoire=1
                                            fin=True
                                        elif grille[i][j]+grille[i][j+1]+grille[i][j+2]+grille[i][j+3]==20:
                                            victoire=2
                                            fin=True
                                for i in range(3):
                                    for j in range(7):
                                        if grille[i][j]+grille[i+1][j]+grille[i+2][j]+grille[i+3][j]==4:
                                            victoire=1
                                            fin=True
                                        elif grille[i][j]+grille[i+1][j]+grille[i+2][j]+grille[i+3][j]==20:
                                            victoire=2
                                            fin=True
                                for i in range(3):
                                    for j in range(4):
                                        if grille[i][j]+grille[i+1][j+1]+grille[i+2][j+2]+grille[i+3][j+3]==4:
                                            victoire=1
                                            fin=True
                                        elif grille[i][j]+grille[i+1][j+1]+grille[i+2][j+2]+grille[i+3][j+3]==20:
                                            victoire=2
                                            fin=True
                                for i in range(3):
                                    for j in range(3,7):
                                        if grille[i][j]+grille[i+1][j-1]+grille[i+2][j-2]+grille[i+3][j-3]==4:
                                            victoire=1
                                            fin=True
                                        elif grille[i][j]+grille[i+1][j-1]+grille[i+2][j-2]+grille[i+3][j-3]==20:
                                            victoire=2
                                            fin=True
                                if emplacements==[-1,-1,-1,-1,-1,-1,-1]:
                                    victoire=3
                                    fin=True
                                if fin==True:
                                    pygame.time.delay(500)
                                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(205+dis,25-dis1,550,690))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(210+dis,30-dis1,540,680))
                                    if victoire==1:
                                        fenêtre.blit(t4,(350+dis,150-dis1))
                                        fenêtre.blit(t5,(320+dis,200-dis1))
                                        fenêtre.blit(v1,(600+dis,200-dis1))
                                        pygame.draw.circle(fenêtre,(255,0,0), (480+dis,370-dis1),50,0)
                                    elif victoire==2:
                                        fenêtre.blit(t4,(350+dis,150-dis1))
                                        fenêtre.blit(t5,(320+dis,200-dis1))
                                        fenêtre.blit(v2,(600+dis,200-dis1))
                                        pygame.draw.circle(fenêtre,(255,255,0), (480+dis,370-dis1),50,0)
                                    elif victoire==3:
                                        fenêtre.blit(v3,(320+dis+20,200-dis1))
                                    pygame.display.flip()
                                    pygame.time.delay(2000)
                                    Jeu=False
                                    puissance4()
                if Puissance4_by_Maxime:
                    Menu_principal()

        while veille :
            étape_programme = "Mode veille"
            fenetre.blit(fondmenu, (0,0))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    veille = False
                    menu_continuer = True
                    ouverture_titre(200,2,0)

                if event.type == KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                        veille = False
                        menu_continuer = True
                        ouverture_titre(200,2,0)

                if event.type == QUIT:
                    STOP()

        while color_selection :
            étape_programme = "Utilitaire de personnalisation des couleurs (console)"
            pygame.draw.rect(fenetre, color, pygame.Rect(638-200,358-200,4+200*2, 4+200*2))
            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(640-200,360-200,1+200*2, 1+200*2))

            texte = font.render("Sélectionner votre couleur", 5, (255,255,255))
            fenetre.blit(texte, (510, 190))

            texte = font.render("Sélection :", 5, (255,255,255))
            fenetre.blit(texte, (460, 240))

            if color_select == 0:
                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(600,240,80, 30))
                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(700,240,100, 30))
            if color_select == 1 :
                pygame.draw.rect(fenetre, (0,255,0), pygame.Rect(600,240,80, 30))
                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(700,240,100, 30))
            if color_select == 2 :
                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(600,240,80, 30))
                pygame.draw.rect(fenetre, (0,255,0), pygame.Rect(700,240,100, 30))
            if color_select == 3 :
                pygame.draw.rect(fenetre, (0,255,0), pygame.Rect(600,240,80, 30))
                pygame.draw.rect(fenetre, (0,255,0), pygame.Rect(700,240,100, 30))
            texte = font.render("Texte", 5, (255,255,255))
            fenetre.blit(texte, (605, 240))
            texte = font.render("Encadrés", 5, (255,255,255))
            fenetre.blit(texte, (705, 240))

            texte = font.render("Variables (dev) :", 5, (255,255,255))
            fenetre.blit(texte, (460, 290))

            if color_check_var == 1 :
                texte = font.render("OK", 5, (255,255,255))
                fenetre.blit(texte, (795, 290))
            else :
                texte = font.render("", 5, (255,255,255))
                fenetre.blit(texte, (795, 290))

            texte = font.render("Couleur :", 5, (255,255,255))
            fenetre.blit(texte, (460, 340))

            texte = font.render("Aperçu :", 5, (255,255,255))
            fenetre.blit(texte, (460, 390))

            fenetre.blit(bouton_OK, (570,490))

            if color_input_var_s == 0 :
                pygame.draw.rect(fenetre, color, pygame.Rect(630,290,160, 30))
            else :
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(630,290,160, 30))

            if color_input_a_s == 0 :
                pygame.draw.rect(fenetre, color, pygame.Rect(560,340,70, 30))
            else :
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(560,340,70, 30))

            if color_input_b_s == 0 :
                pygame.draw.rect(fenetre, color, pygame.Rect(640,340,70, 30))
            else :
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(640,340,70, 30))

            if color_input_c_s == 0 :
                pygame.draw.rect(fenetre, color, pygame.Rect(720,340,70, 30))
            else :
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(720,340,70, 30))

            texte = font.render(color_input_var_t, 1, (0,0,0))
            fenetre.blit(texte, (630, 290))
            texte = font.render(color_input_a_t, 1, (0,0,0))
            fenetre.blit(texte, (560, 340))
            texte = font.render(color_input_b_t, 1, (0,0,0))
            fenetre.blit(texte, (640, 340))
            texte = font.render(color_input_c_t, 1, (0,0,0))
            fenetre.blit(texte, (720, 340))

            color_test = (color_config[0],color_config[1],color_config[2])

            if color_input_a_t == "" and color_input_a_s == 0:
                color_input_a_t = "0"
                color_config[0] = 0

            if color_input_b_t == "" and color_input_b_s == 0:
                color_input_b_t = "0"
                color_config[1] = 0

            if color_input_c_t == "" and color_input_c_s == 0:
                color_input_c_t = "0"
                color_config[2] = 0

            if color_input_var_t == "color1" or color_select == 1:
                texte = font.render("Test", 5, color_test)
                fenetre.blit(texte, (560, 390))
            if color_input_var_t == "color" or color_select == 2 :
                pygame.draw.rect(fenetre, color_test, pygame.Rect(560,390,25,25))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.pos[0] >= 630 and event.pos[0] <= 790 and event.pos[1] >= 290 and event.pos[1] <= 320 :
                            color_input_var_s = 1
                            color_select = 0
                        else :
                            color_input_var_s = 0

                        if event.pos[0] >= 560 and event.pos[0] <= 630 and event.pos[1] >= 340 and event.pos[1] <= 370 :
                            color_input_a_s = 1
                        else :
                            color_input_a_s = 0

                        if event.pos[0] >= 640 and event.pos[0] <= 710 and event.pos[1] >= 340 and event.pos[1] <= 370 :
                            color_input_b_s = 1
                        else :
                            color_input_b_s = 0

                        if event.pos[0] >= 720 and event.pos[0] <= 790 and event.pos[1] >= 340 and event.pos[1] <= 370 :
                            color_input_c_s = 1
                        else :
                            color_input_c_s = 0

                        if event.pos[0] >= 600 and event.pos[0] <= 680 and event.pos[1] >= 240 and event.pos[1] <= 270 :
                            color_select = 1
                            color_input_var_t = ""
                        elif event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 240 and event.pos[1] <= 270 :
                            color_select = 2
                            color_input_var_t = ""

                    if pos_bouton_OK.collidepoint(event.pos):
                        color_selection = False
                        animations_continuer = True
                        paramètres = True

                        if color_input_var_t == "color" or color_select == 2:
                            color = color_test
                            fichier=open("Couleur_r.py","w")
                            fichier.write("color="+str(color))
                            fichier.close()
                        if color_input_var_t == "color1" or color_select == 1:
                            color1 = color_test
                            fichier=open("Couleur.py","w")
                            fichier.write("color1="+str(color1))
                            fichier.close()

                if event.type == pygame.KEYDOWN:
                    if color_input_var_s == 1:
                        if event.key == pygame.K_SPACE :
                            color_input_var_t += " "
                            if color_input_var_t == "color":
                                color_check_var = 1
                            elif color_input_var_t == "color1":
                                color_check_var = 1
                            else :
                                color_check_var = 0
                        elif event.key == pygame.K_BACKSPACE :
                            color_input_var_t = color_input_var_t[:-1]
                            if color_input_var_t == "color":
                                color_check_var = 1
                            elif color_input_var_t == "color1":
                                color_check_var = 1
                            else :
                                color_check_var = 0
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            if color_input_var_t == "color":
                                color_check_var = 1
                            elif color_input_var_t == "color1":
                                color_check_var = 1
                            else :
                                color_input_var_t = "Erreur"
                                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(630,290,160, 30))
                                texte = font.render(color_input_var_t, 1, (0,0,0))
                                fenetre.blit(texte, (630, 290))
                                pygame.display.flip()
                                time.sleep(1)
                                color_check_var = 0
                            if color_check_var != 1:
                                color_input_var_t = ""
                            color_input_var_s = 0
                        elif len(color_input_var_t) > 10 :
                            color_input_var_t = ""
                        else :
                            color_input_var_t += event.unicode
                            if color_input_var_t == "color":
                                color_check_var = 1
                            elif color_input_var_t == "color1":
                                color_check_var = 1
                            else :
                                color_check_var = 0

                    elif color_input_a_s == 1:
                        if event.key == pygame.K_SPACE :
                            None

                        elif event.key == pygame.K_BACKSPACE :
                            color_input_a_t = color_input_a_t[:-1]

                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            if color_input_var_t == "color" or color_input_var_t == "color1" or color_select == 1 or color_select == 2 :
                                try :
                                    if int(color_input_a_t) <= 255 and int(color_input_a_t) >= 0:
                                        color_config[0] = int(color_input_a_t)
                                    else :
                                        color_input_a_t = "Erreur"
                                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(560,340,70, 30))
                                        texte = font.render(color_input_a_t, 1, (0,0,0))
                                        fenetre.blit(texte, (560, 340))
                                        pygame.display.flip()
                                        time.sleep(1)
                                        color_input_a_t = ""
                                except:
                                    color_input_a_t = "Erreur"
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(560,340,70, 30))
                                    texte = font.render(color_input_a_t, 1, (0,0,0))
                                    fenetre.blit(texte, (560, 340))
                                    pygame.display.flip()
                                    time.sleep(1)
                                    color_input_a_t = ""

                            else :
                                color_input_a_t = "Erreur"
                                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(560,340,70, 30))
                                texte = font.render(color_input_a_t, 1, (0,0,0))
                                fenetre.blit(texte, (560, 340))
                                pygame.display.flip()
                                time.sleep(1)
                                color_input_a_t = ""

                            color_input_a_s = 0
                        elif len(color_input_a_t) > 2 :
                            color_input_a_t = ""
                        else :
                            color_input_a_t += event.unicode

                    elif color_input_b_s == 1:
                        if event.key == pygame.K_SPACE :
                            None

                        elif event.key == pygame.K_BACKSPACE :
                            color_input_b_t = color_input_b_t[:-1]

                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            if color_input_var_t == "color" or color_input_var_t == "color1" or color_select == 1 or color_select == 2:
                                try :
                                    if int(color_input_b_t) <= 255 and int(color_input_b_t) >= 0:
                                        color_config[1] = int(color_input_b_t)
                                    else :
                                        color_input_b_t = "Erreur"
                                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(640,340,70, 30))
                                        texte = font.render(color_input_b_t, 1, (0,0,0))
                                        fenetre.blit(texte, (640, 340))
                                        pygame.display.flip()
                                        time.sleep(1)
                                        color_input_b_t = ""
                                except:
                                    color_input_b_t = "Erreur"
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(640,340,70, 30))
                                    texte = font.render(color_input_b_t, 1, (0,0,0))
                                    fenetre.blit(texte, (640, 340))
                                    pygame.display.flip()
                                    time.sleep(1)
                                    color_input_b_t = ""

                            else :
                                color_input_b_t = "Erreur"
                                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(640,340,70, 30))
                                texte = font.render(color_input_b_t, 1, (0,0,0))
                                fenetre.blit(texte, (640, 340))
                                pygame.display.flip()
                                time.sleep(1)
                                color_input_b_t = ""

                            color_input_b_s = 0
                        elif len(color_input_b_t) > 2 :
                            color_input_b_t = ""
                        else :
                            color_input_b_t += event.unicode

                    elif color_input_c_s == 1:
                        if event.key == pygame.K_SPACE :
                            None

                        elif event.key == pygame.K_BACKSPACE :
                            color_input_c_t = color_input_c_t[:-1]

                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            if color_input_var_t == "color" or color_input_var_t == "color1" or color_select == 1 or color_select == 2:
                                try :
                                    if int(color_input_c_t) <= 255 and int(color_input_c_t) >= 0:
                                        color_config[2] = int(color_input_c_t)
                                    else :
                                        color_input_c_t = "Erreur"
                                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(720,340,70, 30))
                                        texte = font.render(color_input_c_t, 1, (0,0,0))
                                        fenetre.blit(texte, (720, 340))
                                        pygame.display.flip()
                                        time.sleep(1)
                                        color_input_c_t = ""

                                except:
                                    color_input_c_t = "Erreur"
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(720,340,70, 30))
                                    texte = font.render(color_input_c_t, 1, (0,0,0))
                                    fenetre.blit(texte, (720, 340))
                                    pygame.display.flip()
                                    time.sleep(1)
                                    color_input_c_t = ""

                            else :
                                color_input_c_t = "Erreur"
                                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(720,340,70, 30))
                                texte = font.render(color_input_c_t, 1, (0,0,0))
                                fenetre.blit(texte, (720, 340))
                                pygame.display.flip()
                                time.sleep(1)
                                color_input_c_t = ""

                            color_input_c_s = 0
                        elif len(color_input_c_t) > 2 :
                            color_input_c_t = ""
                        else :
                            color_input_c_t += event.unicode

                if event.type == QUIT:
                    STOP()

except Exception as e:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    fichier=open("log.txt","a")
    fichier.write(str(e)+"\n")
    fichier.write("Localisation : "+ étape_programme +"\n")
    fichier.write(str(dt_string) +"\n")
    fichier.write("\n")
    fichier.close()
    continuer = False
    erreur_report = True
    erreur_détail = e

# Menu sécurisé d'erreur (accueil)
while erreur_report and not(test):
    check_up = True
    pygame.draw.rect(fenetre, (0,0,255), pygame.Rect(0,0,1280,720))
    font = pygame.font.Font(None, 40)
    texte = font.render("Security mode", 5, (255,255,255))
    fenetre.blit(texte, (530, 10))
    texte = font.render("BNL's Box a rencontré une erreur...", 1, (255,255,255))
    fenetre.blit(texte, (10, 60))
    texte = font.render("L'anomalie peut avoir été engendrée par un fichier manquant, ou un défaut de codage.", 1, (255,255,255))
    fenetre.blit(texte, (10, 100))
    texte = font.render("Dans ce dernier cas, relancez le programme et contactez MINI Picture. Un correctif sera", 1, (255,255,255))
    fenetre.blit(texte, (10, 140))
    texte = font.render("publié dans les plus brefs délais pour corriger le problème.", 1, (255,255,255))
    fenetre.blit(texte, (10, 180))
    texte = font.render("Pensez à consulter le fichier log.txt pour plus d'informations sur l'erreur...", 1, (255,255,255))
    fenetre.blit(texte, (10, 220))
    texte = font.render("Ce dernier devra d'ailleurs être envoyé au développeur pour une meilleure assistance.", 1, (255,255,255))
    fenetre.blit(texte, (10, 260))
    texte = font.render("Appuyez sur ENTER pour plus d'options...", 1, (255,0,0))
    fenetre.blit(texte, (10, 300))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                continuer = True

        if event.type == QUIT:
            pygame.quit()
            erreur_report = False
    # Menu sécurisé d'erreur (diagnostic)
    while continuer :
        pygame.draw.rect(fenetre, (0,0,255), pygame.Rect(0,0,1280,720))
        texte = font.render("Option d'erreur", 5, (255,0,0))
        fenetre.blit(texte, (510, 10))
        texte = font.render("Redémarrage du programme : press R", 5, (255,255,255))
        fenetre.blit(texte, (10, 150))
        texte = font.render("Utilitaire de réparation (réinitialisation complète) : press U", 5, (255,255,255))
        fenetre.blit(texte, (10, 250))
        texte = font.render("Détail de l'erreur (log file) : press L", 5, (255,255,255))
        fenetre.blit(texte, (10, 200))
        texte = font.render("", 5, (255,255,255))
        fenetre.blit(texte, (10, 300))
        texte = font.render("", 5, (255,255,255))
        fenetre.blit(texte, (10, 350))
        texte = font.render("Quitter : press ENTER", 5, (255,255,255))
        fenetre.blit(texte, (10, 400))
        texte = font.render("", 5, (255,255,255))
        fenetre.blit(texte, (10, 450))
        texte = font.render("", 5, (255,255,255))
        fenetre.blit(texte, (10, 500))
        texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
        fenetre.blit(texte, (300, 685))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.quit()
                    erreur_report = False
                    continuer = False
                    os.startfile("Menu.bat")
                if event.key == pygame.K_u:
                    pygame.quit()
                    fichier=open("Update_check.py","w")
                    fichier.write("")
                    fichier.close()
                    erreur_report = False
                    continuer = False
                    os.startfile("Update.bat")
                if event.key == pygame.K_l:
                    os.startfile("log.txt")
                if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                    pygame.quit()
                    erreur_report = False
                    continuer = False

            if event.type == QUIT:
                pygame.quit()
                erreur_report = False
                continuer = False
