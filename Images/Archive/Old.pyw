# Créé par Nicolas, le 18/11/2021 en Python 3.7

"""Chargement des modules et installation de ceux-ci si non-présents"""

import os
from zipfile import ZipFile
import time
test=True
try:
    import music_tag
except ModuleNotFoundError:
    os.startfile("music_tag.bat")
try:
    import psutil
except ModuleNotFoundError:
    os.startfile("psutil.bat")
try:
    import pygame
except ModuleNotFoundError:
    os.startfile("pygame.bat")
while test:
    try:
        import psutil
        import pygame
        import music_tag
        test=False
    except ModuleNotFoundError:
        time.sleep(1)
from pygame.locals import *

"""Ecriture de la version dans un fichier .py et importation des données de ceux-ci"""

fichier=open("Version_Menu.py","w")
fichier.write("Version_Menu=2.61")
fichier.close()

from Version_Menu import Version_Menu
from Version_Level import Version_Level
from Paramètres import*
from Fond import*
from Couleur import*
from Couleur_r import*
from Transition import*
"""Initialisation des variables des programmes enchassés"""

soundtrack=False
menu_continuer=True
bonus_continuer=False
paramètres=False
upgrade_continuer=False
fond_écran=False
version_continuer=False
continuer = True
animations_continuer=False
full=1
x=0
p=1
lecture=True
titre=""
temps=0
avance=0

"""Iniatialisation de la fenêtre Pygame"""

pygame.init()
fenetre = pygame.display.set_mode((1280,720))
pygame.display.set_icon(pygame.image.load("Images/BNL.png"))

"""Chargement des images"""

if fond_selection==1:
    Gauche = pygame.image.load("Images/Gauche.png").convert()
    fondmenu = pygame.image.load("Images/fondmenu.png").convert()
    Droite = pygame.image.load("Images/Droite.png").convert()
if fond_selection==2:
    Gauche = pygame.image.load("Images/Gauche1.png").convert()
    fondmenu = pygame.image.load("Images/fondmenu1.png").convert()
    Droite = pygame.image.load("Images/Droite1.png").convert()

Son = pygame.image.load("Miniature/Soundtrack.png").convert()
Lecture = pygame.image.load("Images/Lecture.png").convert_alpha()
Pause = pygame.image.load("Images/Pause.png").convert()
Avancer = pygame.image.load("Images/Avancer.png").convert()
Reculer = pygame.image.load("Images/Reculer.png").convert()
Lecture1 = pygame.image.load("Images/Lecture1.png").convert_alpha()
Pause1 = pygame.image.load("Images/Pause1.png").convert()
Avancer1 = pygame.image.load("Images/Avancer1.png").convert()
Reculer1 = pygame.image.load("Images/Reculer1.png").convert()

fondmenu_a = pygame.image.load("Miniature/fondmenu.png").convert()
fondmenu1_a = pygame.image.load("Miniature/fondmenu1.png").convert()

Rouge = pygame.image.load("Paramètres/Rouge.png").convert()
Bleu = pygame.image.load("Paramètres/Bleu.png").convert()
Violet = pygame.image.load("Paramètres/Violet.png").convert()
Vert = pygame.image.load("Paramètres/Vert.png").convert()
Jaune = pygame.image.load("Paramètres/Jaune.png").convert()
Cyan = pygame.image.load("Paramètres/Cyan.png").convert()

Selection = pygame.image.load("Images/BNL1.png").convert_alpha()
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
BNLmenu= pygame.image.load("Miniature/BNLmenu.png").convert()
DVD = pygame.image.load("Images/DVD.png").convert_alpha()
Soundtrack = pygame.image.load("Images/Soundtrack.png").convert()
Solar = pygame.image.load("Solar/DVD0.png").convert()
Bonus = pygame.image.load("Images/Bonus.png").convert()
Autre = pygame.image.load("Images/Autre.png").convert()
Menu = pygame.image.load("Images/BNLalpha.png").convert_alpha()
fondbonus = pygame.image.load("Bonus/Bonus88.png").convert_alpha()
Version = pygame.image.load("Miniature/Version.png").convert()
Curseur = pygame.image.load("Images/Statut.png").convert_alpha()
fondmulti= pygame.image.load("Images/fondmulti.png").convert()
Infos= pygame.image.load("Paramètres/Infos.png").convert()
Infos1= pygame.image.load("Paramètres/Infos1.png").convert()
Modules= pygame.image.load("Paramètres/Modules.png").convert()
Modules1= pygame.image.load("Paramètres/Modules1.png").convert()
Animations= pygame.image.load("Paramètres/Animations.png").convert()
Animations1= pygame.image.load("Paramètres/Animations1.png").convert()
ON= pygame.image.load("Paramètres/ON.png").convert()
ON1= pygame.image.load("Paramètres/ON1.png").convert()
OFF= pygame.image.load("Paramètres/OFF.png").convert()
OFF1= pygame.image.load("Paramètres/OFF1.png").convert()
touche_vide= pygame.image.load("Paramètres/touche_vide.png").convert()
Fond_paramètres= pygame.image.load("Paramètres/Fond_paramètres.png").convert()
Fond_paramètres1= pygame.image.load("Paramètres/Fond_paramètres1.png").convert()
Menu1 = pygame.image.load("Images/Menu.png").convert()
Menu11 = pygame.image.load("Images/Menu1.png").convert()

"""Définition de la position des images précédement chargées"""

pos_Solar = Solar.get_rect(topleft=(50,450))
pos_BNLmenu = BNLmenu.get_rect(topleft=(970,20))
pos_Soundtrack = Soundtrack.get_rect(topleft=(500,450))
pos_Bonus = Bonus.get_rect(topleft=(50,20))
pos_Autre = Autre.get_rect(topleft=(400,20))
pos_DVD = DVD.get_rect(topleft=(1000,450))
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
pos_Version = Version.get_rect(topleft=(20,20))

pos_Pause = Pause.get_rect(topleft=(1136,144))
pos_Lecture = Lecture.get_rect(topleft=(1136,576))
pos_Avancer = Avancer.get_rect(topleft=(1136,432))
pos_Reculer = Reculer.get_rect(topleft=(1136,288))
pos_Menu1 = Reculer.get_rect(topleft=(1136,0))

pos_Infos = Infos.get_rect(topleft=(0,0))
pos_Infos1 = Infos1.get_rect(topleft=(0,0))
pos_Modules = Modules.get_rect(topleft=(0,180))
pos_Modules1 = Modules1.get_rect(topleft=(0,180))
pos_Animations = Modules.get_rect(topleft=(0,360))
pos_Animations1 = Modules1.get_rect(topleft=(0,360))

pos_ON = ON.get_rect(topleft=(1000,207))
pos_ON1 = ON1.get_rect(topleft=(1000,207))
pos_OFF = OFF.get_rect(topleft=(1070,207))
pos_OFF1 = OFF1.get_rect(topleft=(1070,207))
pos_ON_t = ON.get_rect(topleft=(1000,247))
pos_ON1_t = ON1.get_rect(topleft=(1000,247))
pos_OFF_t = OFF.get_rect(topleft=(1070,247))
pos_OFF1_t = OFF1.get_rect(topleft=(1070,247))

pos_Fond_paramètres = Fond_paramètres.get_rect(topleft=(0,540))
pos_Fond_paramètres1 = Fond_paramètres1.get_rect(topleft=(0,540))
pos_fondmenu_a = fondmenu_a.get_rect(topleft=(400,150))
pos_fondmenu1_a = fondmenu1_a.get_rect(topleft=(700,150))

pos_Violet = Violet.get_rect(topleft=(680,300))
pos_Jaune = Jaune.get_rect(topleft=(720,300))
pos_Rouge = Rouge.get_rect(topleft=(760,300))
pos_Vert = Vert.get_rect(topleft=(800,300))
pos_Cyan = Cyan.get_rect(topleft=(840,300))
pos_Bleu = Bleu.get_rect(topleft=(880,300))
pos_Violet_r = Violet.get_rect(topleft=(680,350))
pos_Jaune_r = Jaune.get_rect(topleft=(720,350))
pos_Rouge_r = Rouge.get_rect(topleft=(760,350))
pos_Vert_r = Vert.get_rect(topleft=(800,350))
pos_Cyan_r = Cyan.get_rect(topleft=(840,350))
pos_Bleu_r = Bleu.get_rect(topleft=(880,350))

pygame.display.flip()

"""Initialisation de l'animation de lancement"""

if animations:

    pygame.mixer.music.load("Son/BNL-start.mp3")
    pygame.mixer.music.play()
    for i in range(85):
        text="BNL animation/Buy N' Large logo-"+str(x)+".png"
        fond1 = pygame.image.load(text).convert()
        fenetre.blit(fond1,(199,100))
        pygame.display.flip()
        x+=1
        time.sleep(0.03)

"""Définition de la transition entre onglets"""

def transition_ouverture(n):
    translation=0
    if transition_check:
        for i in range(n):
            fenetre.blit(Gauche,(-640+translation,0))
            fenetre.blit(Droite,(1281-translation,0))
            pygame.display.flip()
            translation+=1
            time.sleep(0.001)

"""Définition de la fermeture du programme"""

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

transition_ouverture(640)

"""Programme"""

while continuer:
    p=1
    lecture=True
    titre=""
    temps=0
    avance=0
    while menu_continuer:
        fenetre.blit(Gauche,(0,0))
        fenetre.blit(Droite,(640,0))
        fenetre.blit(DVD,(1000,450))
        fenetre.blit(BNLmenu,(970,20))
        fenetre.blit(Soundtrack,(500,450))
        fenetre.blit(Solar,(50,450))
        fenetre.blit(Bonus,(50,20))
        fenetre.blit(Autre,(400,20))
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

        while pos_Solar.collidepoint(a,b) and r<=93:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                    x, y = event.pos
                    if pos_Solar.collidepoint(event.pos):
                        pygame.quit()
                        continuer = False
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
                if pos_Soundtrack.collidepoint(event.pos):
                    paramètres=False
                    menu_continuer=False
                    soundtrack=True
                    menu_continuer=False
                    bonus_continuer=False
                    upgrade_continuer=False
                    version_continuer=False

                if pos_Bonus.collidepoint(event.pos):
                    paramètres=False
                    menu_continuer=False
                    soundtrack=False
                    menu_continuer=False
                    bonus_continuer=True
                    upgrade_continuer=False
                    version_continuer=False

                    for i in range(88):
                        text="Bonus/Bonus"+str(c)+".png"
                        fond1 = pygame.image.load(text).convert()
                        fenetre.blit(fond1,(0,0))
                        pygame.display.flip()
                        c+=1
                        time.sleep(0.02)

                elif pos_BNLmenu.collidepoint(event.pos):
                    paramètres=True
                    menu_continuer=False
                    soundtrack=False
                    menu_continuer=False
                    bonus_continuer=False
                    upgrade_continuer=False
                    version_continuer=False

            if event.type == QUIT:
                paramètres=False
                menu_continuer=False
                soundtrack=False
                menu_continuer=False
                bonus_continuer=False
                upgrade_continuer=False
                version_continuer=False
                continuer=False
                fermeture(118)
                pygame.quit()

    while bonus_continuer:

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
                        os.startfile("PUB.mp4")
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
                        os.startfile("Trash.mp4")
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
                        os.startfile("Floor.mp4")
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
                        os.startfile("Deck.mp4")
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
                        os.startfile("Dock.mp4")
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
                        os.startfile("Preview.mp4")
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
                        os.startfile("Axiom.mp4")
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
                        os.startfile("Earth.mp4")
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
                        os.startfile("Truck.mp4")
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
                        os.startfile("Pool.mp4")
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
                        os.startfile("Captain.mp4")
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
                paramètres=False
                menu_continuer=True
                soundtrack=False
                bonus_continuer=False
                upgrade_continuer=False
                version_continuer=False
                transition_ouverture(640)
        for event in pygame.event.get():
            if event.type == QUIT:
                paramètres=False
                menu_continuer=False
                soundtrack=False
                menu_continuer=False
                bonus_continuer=False
                upgrade_continuer=False
                version_continuer=False
                continuer=False
                fermeture(118)
                pygame.quit()

    while soundtrack:
        a_string=pygame.mixer.music.get_pos()/1000
        float_str = float(a_string)
        test= int(float_str)
        color2 = (255,0,0)
        fenetre.blit(Son,(280,0))
        pygame.draw.rect(fenetre, color2, pygame.Rect(315,650,650, 2))
        fenetre.blit(Curseur, (300+avance, 636))
        avance=temps*test
        pygame.display.flip()

        if not(pygame.mixer.music.get_busy()) and lecture:
            f = music_tag.load_file("WALL-E [Original Score]/"+str(p)+".mp3")
            pygame.mixer.music.load("WALL-E [Original Score]/"+str(p)+".mp3")
            pygame.mixer.music.play()
            p+=1
            temps  =  650/int(float(str(f [ '#length' ])))
            titre  =  str(f [ 'title' ])
            fenetre.blit(fondmulti,(0,0))
            fenetre.blit(Son,(280,0))
            font = pygame.font.Font(None, 20)
            texte = font.render(titre, 1, (255,255,255))
            fenetre.blit(texte, (10, 50))
            pygame.draw.rect(fenetre, color2, pygame.Rect(315,650,650, 2))
            fenetre.blit(Curseur, (300, 636))
            pygame.display.flip()
        if not(pygame.mixer.music.get_busy()):
            fenetre.blit(Pause1,(1136,144))
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
                pygame.display.flip()

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
                menu_continuer=True
                bonus_continuer=False
                paramètres=False
                upgrade_continuer=False
                version_continuer=False
                fenetre.blit(Menu11,(1136,0))
                pygame.display.flip()
                pygame.mixer.music.stop()
                transition_ouverture(640)
        for event in pygame.event.get():
            if event.type == QUIT:
                paramètres=False
                menu_continuer=False
                soundtrack=False
                menu_continuer=False
                bonus_continuer=False
                upgrade_continuer=False
                version_continuer=False
                continuer=False
                fermeture(118)
                pygame.quit()

    while paramètres:

        fenetre.blit(fondmulti,(0,0))
        fenetre.blit(Menu,(1150,20))
        fenetre.blit(touche_vide,(0,360))
        fenetre.blit(Animations,(0,360))
        fenetre.blit(Infos,(0,0))
        fenetre.blit(Modules,(0,180))
        fenetre.blit(Fond_paramètres,(0,540))
        pygame.display.flip()

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
                    menu_continuer=True
                    soundtrack=False
                    bonus_continuer=False
                    animations_continuer=False
                    fond_écran=False
                    upgrade_continuer=False
                    version_continuer=False
                    transition_ouverture(640)

                if pos_Fond_paramètres.collidepoint(event.pos):
                    paramètres=False
                    menu_continuer=True
                    soundtrack=False
                    bonus_continuer=False
                    animations_continuer=False
                    fond_écran=True
                    upgrade_continuer=False
                    version_continuer=False

            if event.type == QUIT:
                paramètres=False
                menu_continuer=False
                soundtrack=False
                bonus_continuer=False
                upgrade_continuer=False
                version_continuer=False
                fond_écran=False
                animations_continuer=False
                continuer=False
                fermeture(118)
                pygame.quit()

        while version_continuer:
            fenetre.blit(fondmulti,(0,0))
            fenetre.blit(Infos1,(0,0))
            fenetre.blit(Modules,(0,180))
            fenetre.blit(Animations,(0,360))
            fenetre.blit(Fond_paramètres,(0,540))
            fenetre.blit(Menu,(1150,20))
            if Version_Menu==Version_Level:
                font = pygame.font.Font(None, 40)
                texte = font.render("Aucun problème détecté", 1, (color1))
                fenetre.blit(texte, (400, 200))
            else:
                font = pygame.font.Font(None, 40)
                texte = font.render("ATTENTION ! Versions non conformes...", 1, (color1))
                fenetre.blit(texte, (400, 200))

            font = pygame.font.Font(None, 40)
            texte = font.render("Version Jauge --> "+str(Version_Level), 1, (color1))
            fenetre.blit(texte, (400, 270))
            font = pygame.font.Font(None, 40)
            texte = font.render("Version Menu --> "+str(Version_Menu), 1, (color1))
            fenetre.blit(texte, (400, 300))

            pygame.draw.rect(fenetre, color, pygame.Rect(400,500,280, 30))
            font = pygame.font.Font(None, 30)
            texte = font.render("Mettre à jour le programme", 1, (0,0,0))
            fenetre.blit(texte, (405, 502))
            pos_mise_a_jour = texte.get_rect(topleft=(405,502))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if pos_mise_a_jour.collidepoint(event.pos):
                        try:
                            with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                            # Extract all the contents of zip file in current directory
                                continuer=False
                                pygame.quit()
                                os.startfile("Mise à jour.bat")

                        except FileNotFoundError:
                            font = pygame.font.Font(None, 30)
                            texte = font.render("Aucun fichier de mise à niveau trouvé", 1, (color1))
                            fenetre.blit(texte, (800, 502))
                            pygame.display.flip()
                            time.sleep(3)
                    if pos_Menu.collidepoint(event.pos):
                        paramètres=False
                        menu_continuer=True
                        soundtrack=False
                        bonus_continuer=False
                        animations_continuer=False
                        upgrade_continuer=False
                        fond_écran=False
                        version_continuer=False
                        transition_ouverture(640)
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

                if event.type == QUIT:
                    paramètres=False
                    menu_continuer=False
                    soundtrack=False
                    bonus_continuer=False
                    fond_écran=False
                    upgrade_continuer=False
                    version_continuer=False
                    animations_continuer=False
                    continuer=False
                    fermeture(118)
                    pygame.quit()

        while upgrade_continuer:
            fenetre.blit(fondmulti,(0,0))
            fenetre.blit(Infos,(0,0))
            fenetre.blit(Modules1,(0,180))
            fenetre.blit(Animations,(0,360))
            fenetre.blit(Fond_paramètres,(0,540))
            fenetre.blit(Menu,(1150,20))
            font = pygame.font.Font(None, 40)
            texte = font.render("Version Psutil --> "+str(psutil.__version__), 1, (color1))
            fenetre.blit(texte, (400, 270))
            font = pygame.font.Font(None, 40)
            texte = font.render("Version Pygame --> "+str(pygame.__version__), 1, (color1))
            fenetre.blit(texte, (400, 330))
            font = pygame.font.Font(None, 40)
            texte = font.render("Version Music_tag --> "+str(music_tag.__version__), 1, (color1))
            fenetre.blit(texte, (400, 207))
            pygame.draw.rect(fenetre, color, pygame.Rect(845,270,90, 30))
            pygame.draw.rect(fenetre, color, pygame.Rect(845,330,90, 30))
            pygame.draw.rect(fenetre, color, pygame.Rect(845,397,120, 30))
            pygame.draw.rect(fenetre, color, pygame.Rect(845,447,120, 30))
            pygame.draw.rect(fenetre, color, pygame.Rect(845,207,90, 30))
            font = pygame.font.Font(None, 30)
            texte1 = font.render("Update", 1, (0,0,0))
            texte = font.render("Update", 1, (0,0,0))
            texte4 = font.render("Update", 1, (0,0,0))
            texte2 = font.render("Update all", 1, (0,0,0))
            texte3 = font.render("Delete all", 1, (0,0,0))
            fenetre.blit(texte1, (855, 273))
            fenetre.blit(texte, (855, 333))
            fenetre.blit(texte2, (855, 400))
            fenetre.blit(texte3, (855, 450))
            fenetre.blit(texte4, (855, 210))
            pygame.display.flip()
            pos_Update1 = texte1.get_rect(topleft=(855,273))
            pos_Update = texte.get_rect(topleft=(855, 333))
            pos_Update2 = texte.get_rect(topleft=(855, 400))
            pos_Delete = texte.get_rect(topleft=(855, 450))
            pos_Update3 = texte1.get_rect(topleft=(855,210))

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
                    menu_continuer=True
                    paramètres=False
                    upgrade_continuer=False
                    version_continuer1=False
                    fond_écran=False
                    soundtrack=False
                    transition_ouverture(640)
                if pos_Update3.collidepoint(event.pos):
                    continuer = False
                    pygame.quit()
                    os.startfile("music_tag update")
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

            for event in pygame.event.get():
                if event.type == QUIT:
                    paramètres=False
                    menu_continuer=False
                    soundtrack=False
                    menu_continuer=False
                    bonus_continuer=False
                    fond_écran=False
                    upgrade_continuer=False
                    animations_continuer=False
                    version_continuer=False
                    continuer=False
                    fermeture(118)
                    pygame.quit()

        while animations_continuer:
            fenetre.blit(fondmulti,(0,0))
            fenetre.blit(Infos,(0,0))
            fenetre.blit(Modules,(0,180))
            fenetre.blit(Animations1,(0,360))
            fenetre.blit(Fond_paramètres,(0,540))
            fenetre.blit(Menu,(1150,20))
            if animations:
                fenetre.blit(ON1,(1000,207))
                fenetre.blit(OFF,(1070,207))
            else:
                fenetre.blit(ON,(1000,207))
                fenetre.blit(OFF1,(1070,207))

            if transition_check:
                fenetre.blit(ON1,(1000,247))
                fenetre.blit(OFF,(1070,247))
            else:
                fenetre.blit(ON,(1000,247))
                fenetre.blit(OFF1,(1070,247))

            font = pygame.font.Font(None, 40)
            texte = font.render("Animations d'ouverture/fermeture", 1, (color1))
            fenetre.blit(texte, (400, 207))
            font = pygame.font.Font(None, 40)
            texte = font.render("Transitions", 1, (color1))
            fenetre.blit(texte, (400, 247))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos_Menu.collidepoint(event.pos):
                        paramètres=False
                        menu_continuer=True
                        soundtrack=False
                        bonus_continuer=False
                        upgrade_continuer=False
                        fond_écran=False
                        animations_continuer=False
                        version_continuer=False
                        transition_ouverture(640)

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
                        fichier=open("Paramètres.py","w")
                        fichier.write("animations=True")
                        fichier.close()
                        animations=True

                    if pos_OFF.collidepoint(event.pos) or pos_OFF1.collidepoint(event.pos):
                        fichier=open("Paramètres.py","w")
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

                if event.type == QUIT:
                    paramètres=False
                    menu_continuer=True
                    soundtrack=False
                    bonus_continuer=False
                    animations_continuer=False
                    fond_écran=False
                    upgrade_continuer=False
                    version_continuer=False
                    fermeture(118)
                    pygame.quit()

        while fond_écran:
            fenetre.blit(fondmulti,(0,0))
            fenetre.blit(Infos,(0,0))
            fenetre.blit(Modules,(0,180))
            fenetre.blit(Animations,(0,360))
            fenetre.blit(Fond_paramètres1,(0,540))
            fenetre.blit(Menu,(1150,20))
            fenetre.blit(fondmenu_a,(400,150))
            fenetre.blit(fondmenu1_a,(700,150))
            font = pygame.font.Font(None, 40)
            texte = font.render("Image de base :", 1, (color1))
            fenetre.blit(texte, (400, 100))

            font = pygame.font.Font(None, 40)
            texte = font.render("Couleur des textes :", 1, (color1))
            fenetre.blit(texte, (400, 300))

            font = pygame.font.Font(None, 40)
            texte = font.render("Couleur des cases :", 1, (color1))
            fenetre.blit(texte, (400, 350))

            fenetre.blit(Violet,(680,300))
            fenetre.blit(Jaune,(720,300))
            fenetre.blit(Rouge,(760,300))
            fenetre.blit(Vert,(800,300))
            fenetre.blit(Cyan,(840,300))
            fenetre.blit(Bleu,(880,300))
            fenetre.blit(Violet,(680,350))
            fenetre.blit(Jaune,(720,350))
            fenetre.blit(Rouge,(760,350))
            fenetre.blit(Vert,(800,350))
            fenetre.blit(Cyan,(840,350))
            fenetre.blit(Bleu,(880,350))

            if fond_selection==1:
                Gauche = pygame.image.load("Images/Gauche.png").convert()
                fondmenu = pygame.image.load("Images/fondmenu.png").convert()
                Droite = pygame.image.load("Images/Droite.png").convert()
                fenetre.blit(Selection,(390,150))
            if fond_selection==2:
                Gauche = pygame.image.load("Images/Gauche1.png").convert()
                fondmenu = pygame.image.load("Images/fondmenu1.png").convert()
                Droite = pygame.image.load("Images/Droite1.png").convert()
                fenetre.blit(Selection,(690,150))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos_Menu.collidepoint(event.pos):
                        paramètres=False
                        menu_continuer=True
                        fond_écran=False
                        soundtrack=False
                        bonus_continuer=False
                        upgrade_continuer=False
                        animations_continuer=False
                        version_continuer=False
                        transition_ouverture(640)

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
                        fenetre.blit(Selection,(690,150))

                    if pos_fondmenu1_a.collidepoint(event.pos):
                        fichier=open("Fond.py","w")
                        fichier.write("fond_selection=2")
                        fichier.close()
                        fond_selection=2
                        fenetre.blit(Selection,(390,150))

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

                if event.type == QUIT:
                    paramètres=False
                    menu_continuer=True
                    soundtrack=False
                    bonus_continuer=False
                    animations_continuer=False
                    fond_écran=False
                    upgrade_continuer=False
                    version_continuer=False
                    fermeture(118)
                    pygame.quit()
